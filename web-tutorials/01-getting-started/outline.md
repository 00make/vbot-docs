# 01 快速开始 · 网页版教程大纲

- **源料**：`vbot-docs/01-getting-started/1.0~1.2`（固件基准 V1.6.0，Aorta/Zenoh + ROS 2 Humble）
- **受众**：二开极客 / 高校学生 / Coding Agent 双读者
- **风格**：预设 A 清爽技术文档风（白底、`--accent:#0e7490`、左侧 TOC、代码块浅灰底）
- **输出**：每课一个自包含 HTML（CSS 全内联），图片相对路径引用 `vbot-docs/assets/`
- **课数**：3

---

## Lesson 01｜走进 VBOT 大头 EDU（lesson_01.html）

- **内容角色**：概念讲解 + 对比选型
- **知识点**：产品定位与"大头"双自由度交互头部；发布视频四幕拆解（敏捷运控/情感交互/声源伴随/开放生态）；核心规格总览（S100P 128TOPS、14 关节、激光雷达/双目/4 麦阵列、594Wh）；消费版 vs EDU 六维权限对比；萌新准备清单
- **代码示例**：无
- **所需图片**：
  - `../../assets/01-brand-hardware/vbot-dog-edu.png` — 主视觉整机白底照；严格输入资产
  - `../../assets/01-brand-hardware/vbot-dog-photo-1.png` — 实操姿态图；严格输入资产
- **版式要点**：hero 头图 + 规格卡片网格 + 六维对比表 + 视频四幕时间线（CSS 实现，无外部 JS）

## Lesson 02｜极速开箱与网络接入（lesson_02.html）★ 样张

- **内容角色**：操作步骤 + 故障排查
- **知识点**：双计算单元与 IP 拓扑（计算主板 192.168.126.2 / 网关板 192.168.127.10）；方案 A Type-C 有线直连与静态 IP 避坑（严禁 .2、网关留空）；方案 B 1.6 固件板载 WiFi 直连；SSH ed25519 免密与 `~/.ssh/config` 别名；Host Key 冲突排错
- **代码示例**：PowerShell 网卡配置（2 行）、bash ifconfig（1 行）、ping（1 行）、ssh-keygen/ssh-copy-id（2 行）、ssh config（7 行）、排错命令（1 行）
- **所需图片**：
  - `../../assets/01-brand-hardware/vbot-dog-edu.png` — 端口位置示意；严格输入资产
  - `../../assets/03-dev-env/ssh-access-init.png` — 初次连接流程；严格输入资产
  - `../../assets/03-dev-env/ssh-access.png` — SSH 登录成功自检；严格输入资产
- **版式要点**：CSS 网络拓扑图（替代 mermaid）、Windows/macOS-Linux 双 Tab 代码块、参数表格 + 危险项红色警示、编号步骤列表

## Lesson 03｜Hello World：/vel_cmd 20Hz 运控（lesson_03.html）

- **内容角色**：代码实战（motion_control 安全级）
- **知识点**：`/vbot/sportmode_cmd` 已废弃警示；`/vel_cmd` + `geometry_msgs/msg/Twist` + Domain 178 规范；500ms 看门狗与 20Hz 连续发包原理；`hello_motion.py` 全脚本（--confirm-motion 安全授权）；三步实机验证（source 环境 → 离线预览 → 实跑）
- **代码示例**：Python 完整脚本（~95 行，源码照录）、bash 环境加载（2 行）、运行命令（2 条）、预期输出（text）
- **所需图片**：无（安全提示框 + CSS 看门狗时序示意代替）
- **版式要点**：危险级红色警示框、代码块带复制按钮、安全清单卡片、prev=lesson_02 / 返回目录，进阶指向 02 模块（暂以文字说明）

---

## 页脚导航约定

- Lesson 01：next → lesson_02.html
- Lesson 02：prev → lesson_01.html，next → lesson_03.html
- Lesson 03：prev → lesson_02.html
- 每课均有 home → index.html（Phase 5 组装时生成）
