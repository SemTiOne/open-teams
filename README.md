# open-teams

一个面向真实研发团队的 AI 协作工作空间模板：把源码入口、项目文档、执行 skill、任务计划、验证证据和经验沉淀放进同一套可复用的工程壳里。

如果你的团队已经在用 AI 写代码、排查问题或整理文档，但上下文散在聊天记录、个人笔记和临时提示词里，`open-teams` 解决的是另一件更基础的事：让 AI 协作从一次性对话变成可继承、可验证、可持续升级的团队资产。

## 为什么值得用

- **新项目能快速开局**：直接复制模板，就有 `docs/`、`skills/`、`workspace-config/`、`references/`、`task-plans/`、`change-history/` 等标准资产层。
- **老项目能渐进接入**：不要求搬仓库、不要求重构现有研发流程，可先用 `workspace-config/code-sources.yaml` 映射真实代码源。
- **AI 不再只靠临场发挥**：通过 workflow skills 固化方案确认、实施计划、系统化排错、完成前验证、分支与工作区边界等高频流程。
- **任务交付更容易追溯**：方案、节点状态、验收结论、版本记录和变更历史都有明确位置，方便团队复盘和继续推进。
- **模板能力可持续升级**：通过 `workspace-version.yaml`、`CHANGELOG.md` 和升级提示词，让业务工作空间按需吸收模板新能力。

## 适合谁

- 正在给一个或多个项目建立 AI 协作规范的研发团队
- 希望把项目知识、排错经验、交付规则沉淀成长期资产的技术负责人
- 想让 AI 更稳定地参与需求分析、代码实施、联调排查和文档同步的个人开发者
- 已有存量工程，但希望低风险逐步引入 AI 协作工作流的团队

## 你会得到什么

| 能力 | 目录或入口 | 作用 |
| --- | --- | --- |
| 工作空间总入口 | `workspace-assets-index.md` | 统一索引 docs、skills、references、配置与推荐阅读路径 |
| AI 协作约束 | `AGENTS.md` | 约束方案确认、实施计划、节点验收、分支边界和收口流程 |
| 项目文档层 | `docs/` | 沉淀架构、源码说明、开发规范和业务知识 |
| 执行 skill 层 | `skills/` | 拆分通用 workflow skill 与项目场景 skill |
| 源码映射 | `workspace-config/code-sources.yaml` | 记录真实项目仓库位置、默认分支和代码源策略 |
| 任务计划 | `task-plans/` | 归档已确认方案、实施计划和节点状态 |
| 变更历史 | `change-history/` | 记录完成任务的背景、改动、验证、复盘和资料同步 |
| 模板校验 | `scripts/validate_template_layout.py` | 检查必需结构、workflow skill 登记和模板卫生 |

## 快速开始

完整操作见 [快速上手](./QUICKSTART.md)。推荐方式是把目标目录、项目名称和源码路径告诉 AI，让 AI 完成复制模板、清理历史、写入配置和运行校验。

AI 可调用内置脚本完成主要初始化：

```bash
python3 scripts/adopt_workspace.py \
  --template-root . \
  --target <目标工作空间路径> \
  --project-slug <项目标识> \
  --project-name <项目名称> \
  --source-path <真实源码路径或仓库地址>
```

初始化后，再让 AI 按需补 `AGENTS.md`、`docs/projects/<project>/` 和 `skills/<project>/`。

## 内置工作流程

本模板提供以下工作空间级 workflow skills，并与 `AGENTS.md` 的确认和验收约束配套使用：

| 流程 skill | 作用 |
| --- | --- |
| `solution-confirmation` | 在实施前澄清目标、范围、方案与授权 |
| `writing-implementation-plan` | 将已确认方案落地为可执行、可验收的节点计划 |
| `systematic-debugging` | 以复现和证据定位异常根因并指导修复验证 |
| `verification-before-completion` | 在报告完成前核对改动范围、验证结果与风险 |
| `branch-and-worktree-workflow` | 明确分支、工作区边界与版本维护门禁 |
| `workspace-upgrade` | 通过 AI 提示词检查、规划和执行工作空间按需升级 |

workflow skill 处理跨项目的推进方法与质量门禁；真实项目的代码入口、接口边界和专项验证要求应继续沉淀到 `skills/<project>/<scene>/`。

## 目录结构

- `AGENTS.md`：工作空间级 AI 协作约束模板
- `CHANGELOG.md`：用户可读的模板版本记录
- `workspace-assets-index.md`：非源码资产入口模板
- `task-completion-checklist.md`：任务收尾闭环检查模板
- `docs/`：通用文档入口与占位结构
- `docs/development-specs/workflow-skills-design.md`：流程 skill 与项目场景 skill 的边界及编写规范
- `docs/development-specs/template-adoption-cleanup.md`：模板复制后的历史记录清理与去污染指南
- `docs/development-specs/workspace-versioning.md`：版本号规则、版本记录格式与版本资产关系
- `docs/development-specs/workspace-upgrade-model.md`：工作空间版本维护与升级模型
- `docs/development-specs/workspace-upgrade-prompts.md`：可复制的 AI 升级交互提示词
- `skills/_workflow/`：工作空间级通用流程 skill
- `skills/_templates/`：项目场景 skill 模板
- `workspace-config/`：机器可读工作空间配置模板
- `workspace-config/workspace-version.yaml`：模板版本、已应用能力与升级策略元信息
- `references/`：可补充的外围事实模板
- `scripts/`：初始化与自检脚本
- `scripts/adopt_workspace.py`：AI 对话式复制模板、清理历史、写入源码映射并运行校验的辅助脚本
- `task-plans/`：已确认方案与实施计划归档目录
- `change-history/`：已完成任务历史归档目录

## 采用方式

### 新建工作空间

适合新业务线或新工程从一开始即采用统一的 AI 协作资产与治理流程：

1. 复制本目录为业务线工作空间。
2. 按真实工程补齐源码映射、项目文档与场景 skill。
3. 以工作空间流程 skill 约束后续研发任务推进。

### 存量工程渐进式转型

适合已有传统工程在不搬迁原有仓库、不一次性重构研发方式的前提下逐步接入：

1. 先通过 `workspace-config/code-sources.yaml` 维护现有代码仓库映射，或按需将源码纳入 `sources/`。
2. 从高频协作项目或问题场景开始，补齐 `docs/projects/` 与 `skills/<project>/<scene>/` 的最小必要资产。
3. 在实际任务中使用通用 workflow skills 执行方案确认、计划、验证和资料沉淀，让资产随真实工作逐步成长。

## 持续升级

本模板支持提示词驱动的工作空间按需升级。业务工作空间可通过 `workspace-config/workspace-version.yaml` 记录当前模板基线和已应用能力，再使用 [工作空间升级提示词](./docs/development-specs/workspace-upgrade-prompts.md) 触发 AI 检查、规划和实施升级。

用户可通过 [CHANGELOG.md](./CHANGELOG.md) 了解每个模板版本新增了什么、升级影响和推荐升级提示词；版本规则见 [工作空间版本规则](./docs/development-specs/workspace-versioning.md)。

升级必须遵循以下边界：

- 先输出升级方案，获得用户确认后再修改文件。
- 先将升级计划写入 `task-plans/`，经用户确认实施计划后再按节点实施。
- 保护业务线本地定制和真实源码映射，不用模板示例覆盖。
- 每个节点完成后等待用户验收。
- 升级完成后运行模板校验，并补充复盘与 `change-history/`。

## 模板边界

本仓库不包含以下内容：

- 当前业务线的真实源码
- 当前业务线的项目级文档
- 当前业务线的项目级 skill
- 当前业务线的环境账号、测试地址或数据字典

如果使用 `sources/` 接入真实业务源码，默认只保留 `sources/README.md`，真实源码目录不提交到模板仓库。

## 验收标准

- 可独立作为新工作空间的起点目录
- 不依赖当前业务线专有目录与专有名词
- 目录职责清晰，可按需扩展
- 通用 workflow skills 可从入口定位，且具备触发、产物、验证与退出条件
- 用户可通过 `CHANGELOG.md` 感知每个模板版本的能力变化和升级影响
- `scripts/validate_template_layout.py` 能识别缺失的流程资产、升级资产、入口登记或模板卫生问题
