<div align="center">

<a href="https://github.com/hlfzsi/LazyTea-Client">
  <img src="https://socialify.git.ci/hlfzsi/LazyTea-Client/image?description=1&descriptionEditable=%E2%9C%A8%20%E4%B8%80%E6%AC%BE%E5%8F%AF%E7%8B%AC%E7%AB%8B%E8%BF%90%E8%A1%8C%E7%9A%84%E6%9C%AC%E5%9C%B0%E5%9B%BE%E5%BD%A2%E5%8C%96%E7%95%8C%E9%9D%A2%20%E2%9C%A8&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2Fhlfzsi%2Fnonebot_plugin_lazytea%2Fmain%2Fimages%2FREADME%2Fapp.png&name=1&owner=1&pattern=Plus&stargazers=1&theme=Auto" alt="LazyTea Client" width="640" height="320" />
</a>

_—— 来喝一杯下午茶，享受片刻的宁静与高效？ ——_

[![GitHub release](https://img.shields.io/github/v/release/hlfzsi/LazyTea-Client.svg)](https://github.com/hlfzsi/LazyTea-Client/releases)

</div>

**LazyTea Client** 是一个独立的桌面应用程序，旨在提供一个优雅、高效的图形化界面，用于管理您的远程或本地bot(s)服务。

# 📌 项目关系

为了更好地理解 LazyTea 生态，请注意以下几个项目的区别与联系：


| 项目                          | 主要职责                                       | 仓库地址                                                                                     |
| :---------------------------- | :--------------------------------------------- | :------------------------------------------------------------------------------------------- |
| 🍵**LazyTea Client (本项目)** | **独立桌面客户端**，用于连接并管理后端服务。   | [LazyTea-Client](https://github.com/hlfzsi/LazyTea-Client)                                   |
| 🌐**LazyTea Web**             | **Web管理界面**，提供跨平台的浏览器访问体验。  | [LazyTea-Web](https://github.com/hlfzsi/LazyTea-Web)                                         |
| 📱**LazyTea Mobile**          | **跨平台移动客户端**，随时随地管理机器人。     | [LazyTea-mobile](https://github.com/hlfzsi/LazyTea-mobile)                                   |
| 🔌**nonebot_plugin_lazytea**  | **NoneBot2 插件**，作为 LazyTea 的后端服务端。 | [nonebot_plugin_lazytea](https://github.com/hlfzsi/nonebot_plugin_lazytea)                   |
| 🐚**lazytea-shell-extension** | **命令行扩展**，允许通过聊天消息执行管理命令。 | [lazytea-shell-extension](https://github.com/hlfzsi/nonebot_plugin_lazytea_shell_extension/) |

简单来说，您需要在您的机器人上安装 `nonebot_plugin_lazytea` 作为服务端，然后使用本客户端（`LazyTea Client`）连接到它，即可开始享受图形化管理的便捷。

若您使用其他框架，欢迎贡献相应的后端插件。

<br>

# ✨ 优势

LazyTea Client 继承了插件版的全部优点，并在此基础上提供了更强大的灵活性：

### **远程管理能力**

* **独立运行**: 无需与您的 NoneBot2 实例在同一台机器上。您可以从任何地方连接并管理您的机器人。
* **多实例支持**: 通过保存不同的连接配置，轻松切换并管理多个不同的机器人实例。

### **坚如磐石的稳定性**

* **进程隔离**: 客户端与您的机器人核心业务完全分离。**即使 GUI 界面意外崩溃，您的机器人也丝毫不受影响**，确保 7x24 小时稳定在线。

### **优雅先进的架构**

* **现代化 UI 框架 (PySide6)**: 借助 Qt 6.x 强大的跨平台能力，在 Windows, macOS, Linux 上提供原生、流畅的操作体验。
* **高度解耦**: 基于 WebSocket 实现与后端的通信，为未来支持更多类型的后端服务提供了可能。

### **触手可及的便捷**

* **告别混乱配置**: 为每个插件自动生成专属的可视化配置页面。
* **插件生态尽在掌握**: 一键检查与更新插件，版本、作者、说明等信息聚合展示。
* **精细灵活的权限管控**: 提供非侵入式的 Matcher 级权限控制。
* **高效的话题追踪**: 右键点击任意消息，即可提取关键词并快速检索相关历史。
* **数据驱动决策**: 通过清晰的图表洞察插件调用情况。

> **💡 温馨提示:**
>
> * 为了获得最佳性能体验，建议在挂机时将 LazyTea 最小化或停留在“概览”页面，以减少不必要的资源占用。

<br>

# 📱 应用速览


|                                                     概览页面                                                     |                                                     Bot 页面                                                     |
| :---------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------: |
|   ![概览](https://raw.githubusercontent.com/hlfzsi/nonebot_plugin_lazytea/main/images/README/1753779214444.png)   | ![Bot设置](https://raw.githubusercontent.com/hlfzsi/nonebot_plugin_lazytea/main/images/README/1753779501509.png) |
|                                                **消息与话题追踪**                                                |                                                **插件管理与配置**                                                |
| ![消息页面](https://raw.githubusercontent.com/hlfzsi/nonebot_plugin_lazytea/main/images/README/1753779612117.png) | ![插件列表](https://raw.githubusercontent.com/hlfzsi/nonebot_plugin_lazytea/main/images/README/1753779698765.png) |

<br>

# 🚀 快速入门

### **1. 系统要求**


| 配置级别     | 最低要求    | 推荐配置   |
| :----------- | :---------- | :--------- |
| **CPU**      | 任意现代CPU | 双核及以上 |
| **内存**     | 100 MB      | 120MB+     |
| **硬盘空间** | 50 MB       | 100 MB+    |

### **2. 安装与配置**

1. **安装后端服务**: 在您的 NoneBot2 项目中，安装 `nonebot_plugin_lazytea` 插件。
   ```bash
   nb plugin install nonebot_plugin_lazytea
   ```
2. 设置环境: 在`.env`中进行以下基础设置：
   ```dotenv
   headless = True # 是否禁用LazyTea的本地GUI
   host = 0.0.0.0 # 允许外部IP连接, 需要注意, 此操作有危险性, 会将您的nonebot向外暴露
   ```
3. **获取连接信息**: 启动 NoneBot2，连接所需的 `IP`, `PORT` 和 `TOKEN`应当显而易见。`TOKEN`默认为 `疯狂星期四V我50`
4. **下载并运行客户端**:
   * 前往 [Releases](https://github.com/hlfzsi/LazyTea-Client/releases) 页面下载最新的 `LazyTea.exe` (Windows) 或自行部署本仓库的Python脚本。
   * 运行客户端，在弹出的登录窗口中填入上一步获取的连接信息。
   * 勾选“记住我”，下次启动即可自动输入信息。

# 区别

本项目与`nonebot_plugin_lazytea`所提供的nonebot绑定有其功能上的细微区别，下表仅指出有区别与易误解的部分。


| 功能             | 🍵**LazyTea Client (本项目)** | 🔌**nonebot_plugin_lazytea** |
| ---------------- | ----------------------------- | ---------------------------- |
| 导入自定义处理器 | `√`                          | `√`                         |
| 自定义UI         | `×`                          | `√`                         |

# 🗺️ 项目蓝图 & 生命周期

### **开发蓝图**

* [X]  **赋能开发者**: 提供更完整的接口，让插件与 LazyTea 无缝协作。
* [X]  **远程控制**: 提供独立的 GUI 客户端，允许远程操作您的 Bot 实例。
* [ ]  **极致性能**: 持续优化内存占用，提供更轻快的体验。
* [ ]  **生态合作**: 积极寻求与其他插件开发者的合作，共建 NoneBot 的 UI 生态。
* [X]  **多平台支持**: 探索在移动端支持的可能性。
* [X]  **更完善的用户支持**: 加入QQ群 972526136 以获得进一步支持。

### **版本管理**

本项目遵循 PEP 440 标准。

> 通常，每个次版本号的正式发布会经过 Alpha (功能实现), Beta (修正错误), rc (发布前排错) 三个阶段。由于精力有限，新版本的 Alpha 发布代表着上一版本停止修订。

---

### **你可能在寻找**（友情链接）

* [LazyTea Web](https://github.com/hlfzsi/LazyTea-Web)：现代化的 Web 管理界面，支持所有浏览器访问
* [LazyTea Mobile](https://github.com/hlfzsi/LazyTea-mobile)：移动设备专用客户端，随时随地管理机器人
* [NoneBot WebUI](https://webui.nbgui.top/)：✨ 新一代 NoneBot Web 管理界面 ✨
* [nonebot_plugin_lazytea](https://github.com/hlfzsi/nonebot_plugin_lazytea)：LazyTea 的后端服务插件与nonebot2绑定
* [nonebot_plugin_lazytea_shell_extension](https://github.com/hlfzsi/nonebot_plugin_lazytea_shell_extension/)：为 LazyTea 启用命令管理，允许通过聊天消息管理权限

<br>

![Star History](https://api.star-history.com/svg?repos=hlfzsi/LazyTea-Client,hlfzsi/LazyTea-Web,hlfzsi/nonebot_plugin_lazytea&type=Date)
