# 版本记录

本文件面向工作空间使用者记录模板版本变化，帮助判断每个版本新增了什么、是否需要升级以及如何通过 AI 提示词完成升级。

版本号规则见 [工作空间版本规则](./docs/development-specs/workspace-versioning.md)。机器可读的当前版本和已应用能力见 [workspace-version.yaml](./workspace-config/workspace-version.yaml)。

## 0.4.0 - 2026-06-01

### 新增能力

- 重构 README 首屏表达，突出 open-teams 的价值、适用人群、能力总览和 AI 协作资产化定位。
- 新增 `QUICKSTART.md`，将快速上手调整为 AI 对话式采用：用户提供目标目录、项目名称、源码路径和采用方式，由 AI 完成复制、清理、初始化和校验。
- 新增 `scripts/adopt_workspace.py`，支持 AI 将模板复制到目标工作空间、清理模板自身历史记录、写入源码映射、更新版本元信息并运行模板校验。
- 新增 `scripts/prepare_clean_workspace.py` 和 `docs/development-specs/template-adoption-cleanup.md`，明确业务工作空间副本中应清理模板自身 `task-plans/YYYY-*.md` 与 `change-history/open-teams/`，避免模板迭代记录污染用户项目。
- 更新资产索引、开发规范入口和模板校验脚本，使 AI 对话式采用、模板去污染指南和相关脚本成为可发现、可校验的模板能力。

### 升级影响

- 新用户可以优先通过 AI 对话完成模板复制和初始化，不再需要手动复制目录、判断历史记录清理范围或手写源码映射。
- 已初始化业务工作空间可按需引入 `QUICKSTART.md`、`template-adoption-cleanup.md`、`adopt_workspace.py` 和 `prepare_clean_workspace.py`，但引入前应保护本地 `AGENTS.md`、源码映射和版本元信息。
- 模板校验新增对 AI 采用脚本与去污染指南登记的检查。

### 兼容性

- 不涉及业务代码或接口行为变化。
- 对既有业务工作空间是可选增强；采用时需由 AI 先输出方案并等待用户确认，避免覆盖本地定制。

### 推荐升级提示词

```text
请检查当前工作空间是否需要升级到 open-teams 0.4.0 的 AI 对话式采用与模板去污染能力。

要求：
1. 先读取 workspace-assets-index.md、QUICKSTART.md、workspace-config/workspace-version.yaml 和当前 AGENTS.md。
2. 识别当前工作空间是否已经有本地初始化流程、源码映射、任务计划或变更历史。
3. 只输出升级差异、推荐引入文件、需保护的本地定制和风险，不要修改文件。
4. 等我确认方案和实施计划后，再按节点实施。
```

## 0.3.1 - 2026-05-29

### 调整内容

- 强化实施计划确认门禁：方案确认后必须先落地实施计划，且实施计划经用户明确确认后才能进入实施阶段。
- 清理 `example-project/` 示例目录，降低模板初始化后的误导和维护噪音。
- 更新 `.gitignore`，默认忽略 `sources/` 下真实业务源码，仅保留 `sources/README.md`，避免业务代码污染工作空间模板仓库。

### 升级影响

- AI 任务推进顺序更严格：`方案确认 -> 计划落档 -> 用户确认实施计划 -> 实施节点`。
- 已初始化业务工作空间如使用 `sources/` 托管真实源码，应确认 `.gitignore` 保留 `sources/README.md` 例外。

### 兼容性

- 不涉及业务代码或接口行为变化。
- 对已有业务工作空间的主要影响是协作流程门禁更严格。

## 0.3.0 - 2026-05-26

### 新增能力

- 新增工作空间版本维护与提示词驱动升级机制。
- 新增 `workspace-config/workspace-version.yaml`，记录模板版本、已应用能力、升级策略和本地定制说明。
- 新增 `workspace-upgrade` workflow skill，用于检查、规划、实施和收口工作空间升级。
- 新增工作空间升级提示词，覆盖升级检查、计划生成、节点实施、完成验证、复盘和版本元信息维护。
- 模板校验脚本新增升级资产检查，能识别缺失升级模型、提示词、版本元信息或升级 skill 章节不完整。

### 升级影响

- 基于旧模板的业务工作空间可以按需引入版本元信息和升级提示词，不需要搬迁原有源码。
- 初始化新工作空间时，应按业务线情况调整 `workspace-config/workspace-version.yaml`。
- 后续新增模板能力时，应同步更新本文件、`workspace-version.yaml` 和相关入口。

### 兼容性

- 不涉及业务代码或接口行为变化。
- 对已有业务工作空间的影响取决于是否选择应用该版本能力。

### 推荐升级提示词

```text
请检查当前工作空间是否需要升级到 open-teams 0.3.0 的版本维护与提示词驱动升级机制。

要求：
1. 先读取 workspace-assets-index.md、task-completion-checklist.md 和 workspace-config/workspace-version.yaml。
2. 识别当前工作空间类型、已应用能力、本地定制和潜在风险。
3. 只输出升级差异、可选升级项、推荐方案和风险，不要修改文件。
4. 等我确认方案后再进入实施。
```

## 0.2.0 - 2026-05-26

### 新增能力

- 新增工作空间级 workflow skill 分层，区分跨项目流程门禁和项目场景事实。
- 新增五类基础 workflow skills：方案确认、实施计划、系统化排错、完成前验证、分支与工作树流程。
- 新增工作空间流程 skill 设计规范，定义 workflow skill 与项目场景 skill 的职责边界和必备章节。
- 增强模板校验脚本，检查 workflow skill 文件、必备章节、入口登记和模板卫生。
- 支持新建工作空间和存量传统工程渐进式 AI 协作转型两种采用方式。

### 升级影响

- 业务工作空间可按需引入 `skills/_workflow/`，将通用任务推进流程从长规则拆成可触发的 skill。
- 项目场景 skill 模板新增触发条件、前置输入、产物与退出条件、验证清单等章节。
- 根 README、`AGENTS.md` 和资产索引需要同步承认 workflow skill 层。

### 兼容性

- 不涉及业务代码或接口行为变化。
- 若业务工作空间已有自定义 `AGENTS.md`，升级时必须先保护本地约束，再合并 workflow 层说明。

### 推荐升级提示词

```text
请检查当前工作空间是否需要升级到 open-teams 0.2.0 的 workflow skills 基线能力。

要求：
1. 对照 skills/README.md、docs/development-specs/workflow-skills-design.md 和 skills/_workflow/。
2. 列出缺失、过时或与 AGENTS.md 不自洽的地方。
3. 给出最小升级方案和验证方式。
4. 不要修改文件，先等我确认。
```

## 0.1.0 - 2026-05-16

### 初始能力

- 提供通用 AI 协作工作空间壳工程骨架。
- 提供 `docs/`、`skills/`、`references/`、`workspace-config/`、`task-plans/` 和 `change-history/` 基础目录。
- 提供项目场景 skill 模板和模板结构校验脚本。

### 兼容性

- 作为基础模板版本，不包含工作空间级 workflow skill 和版本升级机制。
