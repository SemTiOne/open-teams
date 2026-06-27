# Overall Architecture

open-teams 自身的系统架构，以及你的项目如何在此基础上生长。

## 目录

1. [open-teams 分层架构](#open-teams-分层架构)
2. [架构原则](#架构原则)
3. [关键设计决策](#关键设计决策)
4. [你的项目如何生长](#你的项目如何生长)
5. [ADR 指引（给你的项目）](#adr-指引给你的项目)

---

## open-teams 分层架构

open-teams 是一个 **7 层资产体系**。从外部入口到内部工具，每一层有自己的职责和更新节奏。

```
┌─────────────────────────────────────────────────────────┐
│  1. ENTRY LAYER         对外入口层                        │
│     README.md / README.zh-CN.md / QUICKSTART.md          │
│     CHANGELOG.md                                          │
│     docs/en/why-open-teams.md / getting-started.md       │
│                           │                               │
│  2. GOVERNANCE LAYER    治理层                            │
│     AGENTS.md / MEMORY.md / TEAM.md / TASKS.md            │
│     CONTRIBUTING.md / CODE_OF_CONDUCT.md / SECURITY.md    │
│     LICENSE                                               │
│                           │                               │
│  3. SKILLS LAYER        技能层                            │
│     Core:     code-review / api-design-review             │
│               architecture-review / onboarding            │
│     Workflow: solution-confirmation                       │
│               writing-implementation-plan                 │
│               systematic-debugging                        │
│               verification-before-completion              │
│               branch-and-worktree-workflow                │
│               workspace-upgrade                           │
│                           │                               │
│  4. MEMORY LAYER        记忆层                            │
│     memory/YYYY-MM-DD.md   (日记)                         │
│     task-plans/             (方案 + 实施计划)              │
│     planning/               (日/周/月计划 + 收件箱)        │
│     change-history/         (已完成任务归档)              │
│                           │                               │
│  5. CONFIG LAYER        配置层                            │
│     workspace-config/workspace-version.yaml               │
│     workspace-config/code-sources.yaml                    │
│     TOOLS.md (local, not committed)                       │
│                           │                               │
│  6. KNOWLEDGE LAYER     知识层                            │
│     docs/                   (项目文档 + 开发规范)         │
│     references/             (外部参考资料)                │
│     sources/                (源码仓库映射)                │
│                           │                               │
│  7. TOOLING LAYER       工具层                            │
│     scripts/                (校验/初始化/健康检查)        │
│     init.sh / init-command.py                              │
│     extensions/vscode/      (VS Code 扩展)               │
│     .github/workflows/      (CI)                         │
└─────────────────────────────────────────────────────────┘
```

### 每一层的职责

| 层 | 职责 | 谁改 | 更新频率 |
|----|------|------|----------|
| **Entry** | 给人类和搜索引擎看的项目门面 | 团队 + AI | 版本发布时 |
| **Governance** | 给 AI 的行为约束和项目元规则 | 团队 + AI | 有决策/教训时 |
| **Skills** | 标准化 AI 的工作流程和质量标准 | AI（人审批） | 有新的协作模式时 |
| **Memory** | 时间线事实和任务状态追踪 | AI | 每天 |
| **Config** | 工作空间版本和源码映射 | 团队 | 源码仓库变更时 |
| **Knowledge** | 可被 AI 检索的领域知识 | 团队 + AI | 随项目演进 |
| **Tooling** | 自动化脚本和 CI 流程 | dev 团队 | 按需 |

### 层间数据流

```
用户指令 → AI 读取 Entry + Governance → AI 按需加载 Skills
                                              │
                                              ▼
                                        执行任务
                                              │
                          ┌───────────────────┴───────────────────┐
                          ▼                                       ▼
                    产出代码/文档                            记忆/日记更新
                          │                                       │
                          ▼                                       ▼
                   sources/ 源码仓库                    memory/ + MEMORY.md
                          │                                       │
                          └───────────────────┬───────────────────┘
                                              ▼
                                    change-history/ 归档
```

**关键规则：**
- **Governance > Skills** — AGENTS.md 是最高约束，Skills 不能绕过
- **Memory 不是文档** — 日记写"发生了什么"，MEMORY.md 写"决策和教训"，docs/ 写"怎么工作"
- **Skills 模块化加载** — 一次任务只加载所需 Skill，不全部读入上下文
- **Config 驱动 Tooling** — CI 和脚本依赖 workspace-config/ 判断当前状态

---

## 架构原则

| # | 原则 | 为什么 |
|----|------|--------|
| 1 | **Markdown + Git native** | AI 原生读 Markdown，Git 追踪一切。不引入数据库、配置服务、或私有格式。 |
| 2 | **Tool-agnostic** | Cursor、Copilot、Claude Code、通义灵码 — 都能读 Markdown。不做工具绑定。 |
| 3 | **Skills modular** | 每个 Skill = SKILL.md + rules + checklist + examples。独立加载，独立迭代。 |
| 4 | **Dual-language** | README.md (EN) + README.zh-CN (ZH)。中英各自独立，不混排。 |
| 5 | **Conversation-driven** | 用户不手动编辑配置。AI 通过对话理解需求后，自主维护治理文件。 |
| 6 | **Layer isolation** | 每层只读自己需要的信息。Memory 不读 Skills；Skills 不依赖 Memory 内容。 |

---

## 关键设计决策

| 决策 | 理由 | 记录于 |
|------|------|--------|
| 不内置源码，用 code-sources.yaml 做外部映射 | 模板不能假设用户的源码结构；映射层让模板适配任何仓库 | [workspace-versioning](../development-specs/workspace-versioning.md) |
| Skills 分核心和 workflow 两类 | 核心 Skill 管代码质量，workflow Skill 管流程门禁 — 关注点分离 | [workflow-skills-design](../development-specs/workflow-skills-design.md) |
| AGENTS.md 作为最高约束，不可被 Skills 覆盖 | 防止模块化 Skills 各自为政，需要一个统一的宪法 | AGENTS.md § 适用范围 |
| 方案确认强制前置（未确认不进开发） | 防止 AI 基于猜测实现，确保人始终掌握决策权 | AGENTS.md § 方案确认强约束 |
| 节点级提交推送门禁 | 防止多个节点改动堆积到最后一次性提交，降低 diff 可读性和回滚粒度 | AGENTS.md § 实施计划与节点验收机制 |

---

## 你的项目如何生长

open-teams 模板 clone 后，按以下阶段逐层填充：

### Phase 1：初始化（首次对话）
- AI 通过对话填充 AGENTS.md（项目名、技术栈、约定）
- AI 填充 MEMORY.md 的 Identity 和 Contact
- `init.sh` 或手动设置 workspace-config/

### Phase 2：激活 Skills（第一周）
- 按需激活 `code-review`（最优先）
- 有 API 的项目激活 `api-design-review`
- 按团队规范自定义 Skill 的 rules/

### Phase 3：积累记忆（持续）
- 每天自动产出 `memory/YYYY-MM-DD.md`
- 有决策/教训时更新 MEMORY.md
- 任务完成后归档到 change-history/

### Phase 4：自成长（循环）
- 每次任务完成后复盘 → 更新 Skills → 规则越来越准
- 每完成一个真实任务，代码/文档/Skills 更接近一致
- 见 [workspace-upgrade-model](../development-specs/workspace-upgrade-model.md)

---

## ADR 指引（给你的项目）

当你的项目需要做架构决策时，在此目录下写 ADR（Architecture Decision Record）。

### 什么时候写 ADR

- 选择新的技术栈、框架或服务
- 重大架构变更
- 影响多个模块的决策
- 废弃或替换现有系统

### ADR 格式

```markdown
# [YYYY-MM-DD] 决策标题

## Context
为什么需要这个决策？现状是什么？

## Decision
我们选择了什么方案？

## Alternatives Considered
还考虑了哪些替代方案？为什么没选？

## Consequences
正面和负面影响。需要注意什么？
```

### 命名规范

`YYYY-MM-DD-title.md` — 例如 `2026-01-15-use-postgres-for-primary-db.md`

### 相关阅读

- [why-open-teams.md](../en/why-open-teams.md) — open-teams 的架构理念（三大断裂 → 解决方案 → ROI）
- [getting-started.md](../en/getting-started.md) — 5 分钟上手指南
- [workflow-skills-design.md](../development-specs/workflow-skills-design.md) — Skills 系统设计
- [workspace-versioning.md](../development-specs/workspace-versioning.md) — 版本机制