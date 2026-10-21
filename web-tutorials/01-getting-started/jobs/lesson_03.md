# 任务包：Lesson 03（1.2 极速跑通 Hello World：/vel_cmd 20Hz 运控）

## 输出
`C:/GitHub/Vbot/vbot-docs/web-tutorials/01-getting-started/lesson_03.html`（单文件 HTML，UTF-8，CSS 全内联）

## 必读
1. 源料：`C:/GitHub/Vbot/vbot-docs/01-getting-started/1.2-hello-world-motion.md`（Python 源码必须照录，一字不改）
2. 风格样张：`C:/GitHub/Vbot/vbot-docs/web-tutorials/01-getting-started/lesson_02.html`
   - 复制其 `<style>` 中 `:root` 变量块与全部基础组件样式（TOC/页头/徽章/callout/table/codewrap/copy/lab/result/figure/footer.nav/@media）
   - **不得改动配色、字体、间距体系**；只允许追加本课专属组件样式（如时序图、状态灯、进度条）
   - 版式按本课内容角色重新组织，不复制样张的章节结构
3. 全局约定：`C:/GitHub/Vbot/vbot-docs/web-tutorials/01-getting-started/tutorial_spec.json`（deck_context 与安全规则）

## 页面结构
- 左侧 TOC + 右侧正文，骨架与样张一致
- 页头徽章：`Lesson 03` · `安全级别：运动控制（motion_control）`——此徽章用 danger 红色系 · `固件基准 V1.6.0`
- 本课无合适配图，不放 hero 图；页头下加一条醒目的危险提示条（CSS 实现）
- 前置：`<a href="lesson_02.html">1.1 极速开箱与网络接入</a>`；页脚：上一课 lesson_02.html + 返回目录 index.html（无下一课，正文末尾用文字说明进阶方向是 02 架构模块）
- 直播口播导语用 `<details class="talk">` 折叠保留（源文档开头口播全文）
- 全课学习目标 `<ul class="goals">`

## 内容（源自 1.2，按此组织）
1. **控制接口剖析与避坑**
   - danger callout：`/vbot/sportmode_cmd` 在 V1.6.0 已彻底废弃，向其发包无节点订阅、指令被静默丢弃
   - 官方唯一现行接口表格：话题 `/vel_cmd`、消息 `geometry_msgs/msg/Twist`、中间件 ROS 2 Humble / Aorta Bridge、Domain ID 178
2. **为什么必须维持 20Hz 连续发包**
   - 看门狗机制：500ms 未收到新指令 → 自动安全悬停归零；单发一条只会"抽搐一下"；需 10–20Hz
   - CSS 时序图：两行时间轴（上行 20Hz 绿点连续投喂；下行演示超时 500ms 断流 → 红色"看门狗触发/悬停"），配文字图例
3. **编写生产级脚本 hello_motion.py**
   - 完整 Python 代码照录源文档（~95 行，含 argparse --speed/--turn/--duration/--confirm-motion、20Hz timer、emergency_stop 连发 5 次零速、KeyboardInterrupt 兜底）
   - 代码块语言角标 python + 复制按钮；代码前后各加一段要点解读（不用改动代码本身）
4. **实机运行与验证**（编号步骤）
   - 步骤 1：加载 ROS 2 环境（`source /opt/vita/ros/humble/setup.bash`、`export ROS_DOMAIN_ID=178`）
   - 步骤 2：离线安全预览（不带 --confirm-motion，附终端输出 text 块）
   - 步骤 3：迈出第一步（--speed 0.2 --duration 2.0 --confirm-motion）
5. **🧪 交互小实验 1：看门狗模拟器**（内联 JS）
   - 模拟器：一个"📡 发送速度指令（喂狗）"按钮 + 状态灯 + 倒计时/超时进度条
   - 逻辑：每次点击刷新 lastFeed；setInterval 100ms 检测，超过 500ms 未点击 → 状态变红"⚠️ 看门狗触发：已自动下发零速，机器狗悬停"；再次点击恢复"🟢 运行中，速度 vx=0.2 m/s"
   - 页面加载后 1s 自动进入运行态并开始倒计时，便于用户直接观察超时
   - 附一段说明：真实节点里这条链路由 20Hz timer 保证，500ms 是安全底线而不是目标频率
6. **🧪 交互小实验 2：安全参数命令生成器**（内联 JS）
   - 输入：线速度 slider 0.1–0.5 m/s（默认 0.2）、持续时间 slider 1–5 s（默认 2）
   - 输出：`python3 hello_motion.py --speed {v} --duration {t} --confirm-motion` 代码块 + 复制按钮
   - 当速度 >0.4 时输出结果旁出现 warn 提示"高速仅建议熟练后在开阔场地使用"
7. **安全检查清单**（ok/warn 卡片列表，必须包含）
   - 场地 ≥2m×2m 平整无障碍、有人在旁监护
   - 先跑离线预览，确认参数后再加 --confirm-motion
   - 物理急停开关在手边；软件急停 ≠ 物理急停
   - 上报数据前确认电池电量与关节温度正常
8. **本课小结**：接口事实表（/vel_cmd + Twist + 178 + 20Hz + 500ms 看门狗）+ 进阶预告（02 架构拓扑与通信机制，文字说明）

## 硬性约束
- 严禁把 `/vbot/sportmode_cmd` 写成可用接口（只能作为"已废弃"警示出现）
- Python 源码照录，不得改写逻辑；不得添加依赖或外部脚本
- 单文件自包含：无外部 `<link>`/`<script src>`/CDN/webfont；JS 只允许内联
- h1 恰好 1 个；标题层级不跳级；TOC 锚点全部有对应 id
- 运动安全文案必须完整（物理急停至上、开阔场地）

## 自查（必须执行）
```bash
cd C:/GitHub/Vbot/vbot-docs/web-tutorials && python qa_check.py 01-getting-started/lesson_03.html
```
要求 PASS（若提示 lesson_01.html/index.html 目标不存在属正常，其它 FAIL 必须修复）

## 返回
仅返回：输出文件路径 + 一句话 QA 说明。不要修改 outline.md、tutorial_spec.json、lesson_01/02.html、jobs/ 或 index.html。
