# Task 2

请补充个人信息后，在此完成报告！

@Author: 斩风千雪   
@Email: me@chyk.ink

—— 我得了一种看到学生管理系统就会大叫的病。

第一代源码位于 `src` 目录中。

<!--剩余的 medium 难度项目需要重写整个项目，把 `input` 之类的交互和业务逻辑函数分开，就先不做了吧。-->

由于原项目灵活度不高，因此我重新写编写了一版第二代，存放于 `stumgmt2` 文件夹中，把学生管理逻辑单独分开（`StudentManagement` 类），提供了 `web` 和 `tui` 两种操作方式。`web` 使用 [FastAPI](https://fastapi.tiangolo.com/) 实现了一个 web 后端，采用 REST API 交互，在启动后访问 http://localhost:8000/docs/ 即可看到交互式的 API 文档。`tui` 是用第一代改的，仍然是输入数字的操作方法。

（第二代）已实现的任务：

- 结合面向对象思想（使用 [Pydantic](https://docs.pydantic.dev) 库，比起自带 `dataclass` 多了序列化和反序列化等功能），存储学生信息 (easy)
- 使用 `pyyaml` 库，以 `yaml` 文件的形式，存储学生信息 (easy)
- 基于 `unittest`，编写单元测试（包含正反例） (easy)
- 基于 `asyncio.queues.Queue`，实现“待办事项” (medium)
- 结合 `logging` 库，实现“日志记录” (medium)

下面两个没有实现：

- 基于 `set` 实现 分班操作 (medium)
- 基于栈，实现“历史记录” (medium)

可能是因为我人不够抽象，所以不知道怎么去抽象这些操作。