# Claude Code Configuration & Agent Directives

> 本文件直接导入 [AGENTS.md](AGENTS.md)，为 Claude Code 提供任务执行约束。

## 核心开发指令与规范

1. **查阅事实优先**：
   - 在生成代码前，先查阅 [catalog/capabilities.json](catalog/capabilities.json) 确认接口是否存在与开放级别。
   - 严禁凭空构造 ROS 2 话题名或 Aorta 路由名。

2. **生产级脚本骨架**：
   - 编写 Python 任务脚本时，参考 `vbot-lab` 的 `recipes/common.py` 设计模式：
     - 队列深度固定为 16，溢出显式报错；
     - 接收超时强制有界 `(0, 120]` 秒；
     - 捕获 `KeyboardInterrupt` 必须发送全零速度急停；
     - 未带 `--execute` 参数时仅打印运行参数预览。

3. **双脑网络认知**：
   - 计算板：`192.168.126.2`（默认 SSH 用户 `vbot`）
   - 网关板：`192.168.127.10`（RTOS，管理 Wi-Fi / 蓝牙）
   - 本机有线网卡配置：`192.168.126.100/24`
   - 通信主干：Aorta (Zenoh, Domain 178) 为主，ROS 2 桥接为辅。
