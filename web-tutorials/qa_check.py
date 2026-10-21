# -*- coding: utf-8 -*-
"""web-tutorial QA checker. Usage: python qa_check.py <lesson.html> [...]"""
import sys, os, re
from html.parser import HTMLParser

VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
PAIR = {"div","section","main","nav","header","footer","ol","ul","li","table","thead","tbody","tr","td","th","figure","figcaption","details","summary","aside","article","span","p","h1","h2","h3","h4","h5","h6","pre","code","b","i","a","button","style","script","html","head","body","title"}
MOJIBAKE = ["ã€", "å®", "æ–", "çš„", "â€™", "Ã©", "ï¼"]

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.imgs = []
        self.hrefs = []
        self.ids = set()
        self.headings = []
        self.h1_count = 0
        self.has_charset = False
        self.has_viewport = False
        self.external = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))
        if tag == "img":
            self.imgs.append((a.get("src",""), self.getpos()[0]))
        if tag == "a":
            self.hrefs.append((a.get("href",""), self.getpos()[0]))
        if "id" in a:
            self.ids.add(a["id"])
        if re.match(r"h[1-6]$", tag):
            self.headings.append((int(tag[1]), self.getpos()[0]))
            if tag == "h1": self.h1_count += 1
        if tag == "meta":
            if a.get("charset","").lower() == "utf-8": self.has_charset = True
            if a.get("name","").lower() == "viewport": self.has_viewport = True
        if tag == "link" and a.get("href","").startswith(("http://","https://")):
            self.external.append(("link", a["href"], self.getpos()[0]))
        if tag == "script" and a.get("src",""):
            self.external.append(("script", a["src"], self.getpos()[0]))
    def handle_endtag(self, tag):
        if tag in VOID: return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i][0] == tag:
                    unclosed = self.stack[i+1:]
                    self.errors.append(f"line {self.getpos()[0]}: </{tag}> closes over unclosed {unclosed}")
                    del self.stack[i:]
                    break
            else:
                self.errors.append(f"line {self.getpos()[0]}: stray </{tag}>")

def check(path):
    fails, warns = [], []
    raw = open(path, "rb").read()
    text = raw.decode("utf-8", errors="replace")
    base = os.path.dirname(os.path.abspath(path))

    c = Checker()
    try:
        c.feed(text); c.close()
    except Exception as e:
        fails.append(f"[1] parse error: {e}")
        return fails, warns
    if c.stack:
        fails.append(f"[1] unclosed tags: {[(t,l) for t,l in c.stack if t in PAIR]}")
    fails += [f"[1] {e}" for e in c.errors]

    for src, line in c.imgs:
        if src.startswith(("http://","https://")):
            warns.append(f"[2] line {line}: remote img {src}")
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, src.split("#")[0]))):
            fails.append(f"[2] line {line}: img missing {src}")

    if c.h1_count != 1:
        fails.append(f"[3] h1 count = {c.h1_count} (expect 1)")
    prev = 0
    for lvl, line in c.headings:
        if prev and lvl > prev + 1:
            fails.append(f"[3] line {line}: heading skip h{prev}->h{lvl}")
        prev = lvl

    for href, line in c.hrefs:
        if href.startswith("#"):
            if href[1:] not in c.ids:
                fails.append(f"[4] line {line}: anchor {href} has no target id")
        elif not href.startswith(("http://","https://","mailto:")):
            target = os.path.normpath(os.path.join(base, href.split("#")[0]))
            if not os.path.exists(target):
                warns.append(f"[5] line {line}: link target not yet exists {href}")

    for kind, url, line in c.external:
        fails.append(f"[6] line {line}: external {kind} {url}")
    if "@import" in text and re.search(r"@import\s+(url\()?['\"]?http", text):
        fails.append("[6] external @import found")

    if not c.has_charset: fails.append("[7] missing <meta charset=UTF-8>")
    if not c.has_viewport: fails.append("[7] missing viewport meta")

    for m in MOJIBAKE:
        if m in text:
            fails.append(f"[8] mojibake marker {m!r}")

    return fails, warns

ok = True
for p in sys.argv[1:]:
    f, w = check(p)
    name = os.path.basename(p)
    for x in f: print(f"FAIL {name}: {x}")
    for x in w: print(f"WARN {name}: {x}")
    if not f:
        print(f"PASS {name}: all checks passed ({len(w)} warnings)")
    else:
        ok = False
sys.exit(0 if ok else 1)
