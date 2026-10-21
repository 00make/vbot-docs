# 任务包：Lesson 01（1.0 走进 VBOT 大头 EDU）

## 输出
`C:/GitHub/Vbot/vbot-docs/web-tutorials/01-getting-started/lesson_01.html`（单文件 HTML，UTF-8，CSS 全内联）

## 必读
1. 源料：`C:/GitHub/Vbot/vbot-docs/01-getting-started/1.0-vbot-edu-overview.md`（内容以此为准，不得杜撰参数）
2. 风格样张：`C:/GitHub/Vbot/vbot-docs/web-tutorials/01-getting-started/lesson_02.html`
   - 复制其 `<style>` 中 `:root` 变量块与全部基础组件样式（TOC/页头/徽章/callout/table/codewrap/copy/tabs/figure/footer.nav/@media）
   - **不得改动配色、字体、间距体系**；只允许追加本课专属组件样式（如卡片网格、时间线）
   - 版式按本课内容角色重新组织，不复制样张的章节结构
3. 全局约定：`C:/GitHub/Vbot/vbot-docs/web-tutorials/01-getting-started/tutorial_spec.json`（deck_context 与禁用事实）

## 页面结构
- 左侧 TOC（锚点与正文 id 一一对应）+ 右侧正文，页面骨架与样张完全一致
- 页头徽章：`Lesson 01` · `安全级别：信息型` · `固件基准 V1.6.0`；hero 头图 `../../assets/01-brand-hardware/vbot-dog-photo-1.png`（loading="lazy"）
- 前置：无；页脚：`返回目录 index.html` + `下一课 lesson_02.html`（无上一课卡片）
- 直播口播导语用 `<details class="talk">` 折叠块保留（源文档 1.0 开头口播全文）
- 全课学习目标 `<ul class="goals">`

## 内容（源自 1.0，按此组织）
1. **产品全景**：大白头（Pitch/Yaw 双自由度 + LCD 表情屏）、128 TOPS、14 关节、全栈开放 Ubuntu 22.04 + ROS 2 Humble + Aorta(Zenoh)。用统计卡片网格展示 6 个关键数字（128 TOPS / 14 关节 / 24.5 N·m / 16 kg / 5 kg 额定负载 / 594 Wh）
2. **官方发布视频四幕拆解**（37 秒竖屏）：CSS 时间线组件，四幕：
   - 00:00–00:08 高动态敏捷运控（Trot、跳跃、楼梯、扰动平衡恢复；14 颗 VGeer 电机）
   - 00:08–00:18 大头情感交互（双自由度转头、LCD 眼神、抬爪挥手）
   - 00:18–00:28 空间听觉与伴随（4 麦 DOA、0.3s 转头调速、并排行走）
   - 00:28–00:37 开放极客生态（模块化快拆、PiPER 六轴机械臂、CAN-FD/24V）
3. **核心规格总览**：按系统分组的表格（计算/动力关节/全景感知/机身负载/电池续航/外设通信），数值严格照源文档（S100P、8×A78AE、128 TOPS INT8、24.5 N·m、360° 16 线激光雷达 0.1–30m、SC230AI 双目、4 麦阵列、6 轴 IMU + GNSS、16 kg、650×380×450mm、5 kg 额定 / 12 kg 极限、594 Wh、2–4h、24V/10A、Type-C eth2、双路隔离 CAN-FD、WiFi 6 + BT5.2 + UWB）。配图 `../../assets/01-brand-hardware/vbot-dog-edu.png`（figure + figcaption）
4. **消费版 vs EDU 六维对比**：表格六行（系统权限/通信中间件/传感器裸数据/头部交互/硬件电气扩展/AI 范式），EDU 列用 ok 色强调、普通版用 danger 色；末尾用 CSS 流程对比图（左：App→闭源黑盒→固定宏动作；右：SSH/Type-C→Ubuntu Root→Aorta 46 Topics→ROS 2/RCP/MCP→硬件）
5. **🧪 交互小实验：NPU 算力预算器**（内联 JS）
   - 复选框 workloads（勾选即累加估算 TOPS）：YOLOv11 目标检测 ≈1.5、MediaPipe 姿态 ≈0.5、Whisper 语音 ≈1.0、端侧 VLM(2B 级) ≈18、SLAM/避障 ≈2
   - 右侧/下方进度条显示 已用/128 TOPS，>80% 变 warn、>100% 变 bad
   - 文案注明"以上为工程估算，非官方跑分"；并提示高负载推理需为运控预留 CPU 核心（taskset -c 2-7）
6. **萌新第一问：准备清单**：硬件（开发主机/WSL2、双头 Type-C 或 Type-C 转 RJ45、2m×2m 安全场地）、软件与思维（终端基础、拥抱 AI Coding Agent、敬畏物理硬件）
7. **本课小结** + 下一课预告（链接 lesson_02.html）

## 硬性约束
- 严禁出现 `/vbot/sportmode_cmd` 作为可用接口；本课可完全不提
- 单文件自包含：无外部 `<link>`/`<script src>`/CDN/webfont；JS 只允许内联
- 图片一律相对路径 `../../assets/...`，必须带 alt 与 loading="lazy"
- h1 恰好 1 个；标题层级不跳级；TOC 锚点全部有对应 id
- 中文文案与源文档口径一致；不添加源文档没有的硬件参数

## 自查（必须执行）
```bash
cd C:/GitHub/Vbot/vbot-docs/web-tutorials && python qa_check.py 01-getting-started/lesson_01.html
```
要求 PASS（若提示 lesson_03.html/index.html 目标不存在属正常，其它 FAIL 必须修复）

## 返回
仅返回：输出文件路径 + 一句话 QA 说明。不要修改 outline.md、tutorial_spec.json、lesson_02/03.html、jobs/ 或 index.html。
