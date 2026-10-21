# VBOT 开发者文档库 Agent 路由规约 (AGENTS.md)

本文件专为 **AI Coding Agent** (如 Cursor, Claude Code, Codex 等) 量身定制。在执行任何用户指令前，请严格遵守以下任务路由规则与安全准则。

---

## 🧭 任务路由表 (Task Routing Table)

根据用户的开发目标，引导其或直接加载对应的契约文档，**严禁凭空臆造 Topic 名称或 Service 结构**：

| 用户任务意图 | 推荐优先阅读文档 | 核心参考能力 ID |
| :--- | :--- | :--- |
| 了解 VBOT 大头 EDU 版产品全景、地瓜 S100P 128TOPS 算力、14 关节电机、消费版 vs EDU 对比、官方发布视频拆解 | [01-getting-started/1.0-vbot-edu-overview.md](01-getting-started/1.0-vbot-edu-overview.md) | `device.edu_overview` |
| 机器狗开箱、物理连接、配静态 IP、SSH 连不上、1.6 板载 WiFi | [01-getting-started/1.1-unboxing-and-network.md](01-getting-started/1.1-unboxing-and-network.md) | `device.network.connect` |
| 编写第一个运动脚本、让机器狗走两步、测试 /vel_cmd 20Hz | [01-getting-started/1.2-hello-world-motion.md](01-getting-started/1.2-hello-world-motion.md) | `locomotion.vel_cmd.basic` |
| 搞懂双脑结构、计算板与网关板分工、网卡为什么没 wlan0 | [02-architecture-comm/2.1-dual-brain-architecture.md](02-architecture-comm/2.1-dual-brain-architecture.md) | `system.architecture.dual_brain` |
| 解决电脑端能收到 Topic 但发控制指令机器狗不动、Aorta 46 话题破壁 | [02-architecture-comm/2.2-zenoh-and-ros2-bridge.md](02-architecture-comm/2.2-zenoh-and-ros2-bridge.md) | `comm.middleware.zenoh_ros2` |
| 配置 DevContainer、五步端到端部署工作流、Bazel 编译配方、Python 骨架 | [02-architecture-comm/2.3-dev-environment-setup.md](02-architecture-comm/2.3-dev-environment-setup.md) | `dev.environment.recipes_common` |
| 编排动作、趴下/站起/比心、声光表情联动、RCP 任务图 (DAG) | [03-embodied-agent/3.1-motion-control-and-rcp.md](03-embodied-agent/3.1-motion-control-and-rcp.md) | `motion.rcp.dag_execution` |
| 读取激光雷达点云、双目相机 H.265 解码、17 点人体骨骼 (Logit 转概率) | [03-embodied-agent/3.2-perception-data-streams.md](03-embodied-agent/3.2-perception-data-streams.md) | `perception.sensors.stream` |
| 接入大模型 (GPT-4o/Qwen)、语音唤醒词修改、开发 18080 MCP 服务 | [03-embodied-agent/3.3-ai-native-multimodal.md](03-embodied-agent/3.3-ai-native-multimodal.md) | `agent.multimodal.mcp_service` |
| 额定 5kg/极限 12kg 负重边界、算力隔离预留 2 核 (taskset -c 2-7) | [04-hardware-recipes/4.1-specs-and-constraints.md](04-hardware-recipes/4.1-specs-and-constraints.md) | `hardware.specs.constraints` |
| 3D 打印外壳受力、加装 PiPER 六轴机械臂 CAN 总线、外接 RDK/Orin | [04-hardware-recipes/4.2-hardware-modifications.md](04-hardware-recipes/4.2-hardware-modifications.md) | `hardware.modifications.arm` |
| 参考 6 大黑客松标杆案例（聆灵陪诊、伽伽狗、牛来芭比、PoopSense、她的视界、小安）及演示视频 | [04-hardware-recipes/4.3-hackathon-blueprints.md](04-hardware-recipes/4.3-hackathon-blueprints.md) | `cases.hackathon.blueprints` |
| 设备报错排查、自底向上四层排障法 (物理-网络-中间件-应用) 与 15+ FAQ | [05-diagnostics-faq/5.1-four-layer-diagnostics.md](05-diagnostics-faq/5.1-four-layer-diagnostics.md) | `diagnostics.four_layers` |
| 安全看门狗、三大交通规则、开机自启动守护脚本 (flock 防死锁)、硬件急停 | [05-diagnostics-faq/5.2-safety-and-guardrails.md](05-diagnostics-faq/5.2-safety-and-guardrails.md) | `safety.guardrails.watchdog` |

---

## ⚠️ 事实与边界准则 (Facts & Safety Guardrails)

1. **版本基准**：
   - 当前针对硬件应用版本为 **V1.6.0 (foot_quadruped)**，通信中间件为 **Aorta (Zenoh)** 与配套 ROS 2 Humble 桥接子集。
   - 不要推断或猜测其他未开放型号（如 `wheel_quadruped` / `foot_humanoid`）在当前版本的支持情况。

2. **控制接口真实性**：
   - **禁止生成**废弃接口 `/vbot/sportmode_cmd` 的控制代码（该接口在 1.6 已废弃，无后端监听，指令将被静默丢弃）。
   - 现行底盘速度控制话题为 `/vel_cmd`，消息类型为 `geometry_msgs/msg/Twist`。
   - 复杂姿态与声光动作请使用 RCP 任务图接口（`ExecuteTaskGoal`），**禁止在直接服务控制与 RCP 之间无序并发打架**。

3. **安全代码生成规范**：
   - **有界控制**：生成的控制循环必须具备明确的超时阈值（如 `--timeout 10`）与看门狗机制（至少 10~20Hz 连续投递，一旦中断需在 0.5 秒内自动下发零速度安全停车）。
   - **离线安全优先**：默认生成的 CLI 程序应当提供 `--execute` 和 `--confirm-motion` 显式确认参数；在未传入确认参数前，仅输出 JSON 离线预览，不得直接发送危险硬件位移指令。
   - **物理急停至上**：代码中任何软件急停不能替代物理急停开关，在说明中必须提醒用户处于开阔且安全的测试场地。

4. **算力隔离准则**：
   - 当用户要求运行高负载感知推理（如 YOLOv11、MediaPipe 或大型 VLM）时，必须提醒并为底盘运控进程 `locomotion_exec` 预留至少 2 个 CPU 核心（通过 `taskset -c 2-7`），严禁将 CPU 占满导致运控通信断流摔机。

