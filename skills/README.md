# Skills 入口模板

## 资产分层

Skills 分为两类：

| 类型 | 目录结构 | 用途 |
| --- | --- | --- |
| 工作空间流程 skill | `skills/_workflow/<workflow>/SKILL.md` | 承载跨项目通用的阶段门禁、执行流程与验证要求 |
| 项目场景 skill | `skills/<project>/<scene>/SKILL.md` | 承载真实项目、模块或技术场景的具体路径与处理方法 |

当前仓库已经提供项目场景 skill 模板和首批通用流程 skill。流程 skill 的结构与编写规范见 [流程 Skill 设计规范](../docs/development-specs/workflow-skills-design.md)。

## 可用流程 Skill

| 流程 skill | 入口 | 用途 |
| --- | --- | --- |
| `solution-confirmation` | [`skills/_workflow/solution-confirmation/SKILL.md`](./_workflow/solution-confirmation/SKILL.md) | 在任何实施前确认目标、范围、方案与授权 |
| `writing-implementation-plan` | [`skills/_workflow/writing-implementation-plan/SKILL.md`](./_workflow/writing-implementation-plan/SKILL.md) | 将已确认方案拆为落档、可验收的节点计划 |
| `systematic-debugging` | [`skills/_workflow/systematic-debugging/SKILL.md`](./_workflow/systematic-debugging/SKILL.md) | 以复现与证据定位异常根因并验证修复 |
| `verification-before-completion` | [`skills/_workflow/verification-before-completion/SKILL.md`](./_workflow/verification-before-completion/SKILL.md) | 在节点或任务完成陈述前获得新鲜验证证据 |
| `branch-and-worktree-workflow` | [`skills/_workflow/branch-and-worktree-workflow/SKILL.md`](./_workflow/branch-and-worktree-workflow/SKILL.md) | 确认开发分支、工作区边界与版本维护门禁 |
| `workspace-upgrade` | [`skills/_workflow/workspace-upgrade/SKILL.md`](./_workflow/workspace-upgrade/SKILL.md) | 通过 AI 提示词检查、规划和执行工作空间按需升级 |

## 项目场景结构

统一使用以下结构：

- `skills/<project>/README.md`
- `skills/<project>/<scene>/SKILL.md`
- `skills/<project>/<scene>/references/`
- `skills/<project>/<scene>/examples.md`

推荐项目场景：

- `new-feature-dev`
- `bugfix`
- `security-fix`
- `api-refactor`
- `feature-refactor`
- `performance-tuning`

## 流程路由

| 任务类型或阶段 | 优先流程 skill | 项目场景 skill |
| --- | --- | --- |
| 需求澄清与方案确认 | `solution-confirmation` | 按需读取目标项目场景 |
| 方案确认后的节点计划 | `writing-implementation-plan` | 与实施类型对应的项目场景 |
| Bug 定位与修复 | `solution-confirmation`、`systematic-debugging`、`writing-implementation-plan`、`verification-before-completion` | `bugfix` |
| 新功能、重构、性能或安全改造 | `solution-confirmation`、`writing-implementation-plan`、`verification-before-completion` | 对应推荐项目场景 |
| 进入代码修改阶段 | `branch-and-worktree-workflow` | 与任务类型对应的项目场景 |
| 节点汇报与整体收口 | `verification-before-completion` | 按需读取 |
| 工作空间版本维护与升级 | `workspace-upgrade`、`solution-confirmation`、`writing-implementation-plan`、`verification-before-completion` | 按需读取 |

流程 skill 与 `AGENTS.md` 配套使用：`AGENTS.md` 提供工作空间最高优先级约束，流程 skill 提供对应阶段的执行步骤、证据与退出条件。
