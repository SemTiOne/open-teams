# Projects

本目录为工作空间中的每个项目建立文档入口。这是你的项目在 AI 协作中的"首页"。

## 目录

1. [为什么需要项目文档入口](#为什么需要项目文档入口)
2. [如何创建首个项目入口](#如何创建首个项目入口)
3. [目录结构规范](#目录结构规范)
4. [与 workspace 其他资产的关系](#与-workspace-其他资产的关系)

---

## 为什么需要项目文档入口

open-teams 模板不携带任何业务代码。当模板被 clone 到你的项目后，**AI 需要通过这里的文档来理解你的业务**。一个清晰的 `docs/projects/<project>/` 能让 AI：

- 知道每个项目做什么、用什么技术栈
- 理解模块边界和关键代码路径
- 按正确的开发规范进行代码审查和方案设计
- 新团队成员快速获得上下文（而不需要读几十万行代码）

**一个项目入口 ≈ 项目的"README for AI"**。

---

## 如何创建首个项目入口

### 最小可用（5 分钟）

在 `docs/projects/<your-project>/` 下创建 `README.md`：

```markdown
# Project: [项目名]

- **一句话目标：** [这个项目解决什么问题]
- **技术栈：** [语言 / 框架 / 数据库 / 部署方式]
- **代码位置：** [sources/ 下或 code-sources.yaml 中映射的路径]
- **团队：** [负责人 + 角色]
- **状态：** Active / Maintenance / Archived

## 快速入口
- 开发环境配置：
- 本地启动命令：
- 运行测试命令：
- 关键 API / 页面入口：
- 常见问题：
```

### 使用脚本创建项目 Skill 骨架

如果你需要为项目创建场景化的 Skill（如 `bugfix`、`feature-dev`），使用模板自带脚本：

```bash
python3 scripts/init_project_skills.py <project-name>
```

这会基于 `skills/_templates/project/scene-template/` 创建骨架文件。

---

## 目录结构规范

```
docs/projects/<project-name>/
├── README.md            # 项目概览（必选）
├── architecture.md      # 架构说明（推荐）
├── development.md       # 开发规范（推荐，如果与全局不同）
└── api/                 # API 文档（按需）
```

### 各文件职责

| 文件 | 内容 | 何时创建 |
|------|------|----------|
| `README.md` | 项目目标、技术栈、入口指针 | 初始化时必创 |
| `architecture.md` | 模块结构、数据流、关键设计决策 | 项目有 ≥3 个模块时推荐 |
| `development.md` | 项目特有的开发规范（如全局 AGENTS.md 有则不必重复） | 项目规范与全局不同时 |
| `api/` | 接口文档、数据模型 | 有对外接口的项目 |

### 与 skills/ 项目场景 Skill 的关系

`docs/projects/<project>/` 描述**"这个项目是什么样的"**（事实）。

`skills/<project>/<scene>/` 描述**"在这个项目里做某件事要怎么做"**（流程）。

两者互补：AI 先读 docs 理解项目事实，再读 skills 按流程执行。

---

## 与 workspace 其他资产的关系

```
                              open-teams Workspace
                                      │
              ┌───────────────────────┼───────────────────────┐
              ▼                       ▼                       ▼
     AGENTS.md                  docs/projects/           workspace-config/
     (全局约束)                  (项目事实)               (源码映射)
              │                       │                       │
              └───────────────────────┼───────────────────────┘
                                      │
                    AI 读取后自动组装上下文
```

- **AGENTS.md** 提供跨项目的全局约束（技术栈、命名规范、红线）
- **docs/projects/** 提供每个项目的个性化事实（模块结构、特有规范）
- **workspace-config/code-sources.yaml** 告诉 AI 源码在哪里
- **skills/<project>/** 提供项目内特定场景的执行流程

一个完整的 AI 会话 = AGENTS.md（规则）+ MEMORY.md（记忆）+ docs/projects/（项目事实）+ skills/（流程）+ sources/（代码）。

---

## 持续维护

| 触发条件 | 更新内容 |
|----------|----------|
| 新增模块/服务 | 更新 `architecture.md` 的模块关系 |
| 技术栈变更 | 更新 `README.md` 的技术栈字段 |
| API 行为变更 | 更新 `api/` 下的文档 |
| 开发规范调整 | 更新 `development.md` |
| 项目归档 | 将状态改为 Archived，标注替代项目 |

> 文档不是一次写完就丢的。每次代码 MR 时，检查是否需要同步更新项目文档——这与 code review 同样重要。