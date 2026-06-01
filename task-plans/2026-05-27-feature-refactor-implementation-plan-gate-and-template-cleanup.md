# 实施计划确认门禁与模板清理方案

## 1. 基本信息

- 任务标题：实施计划确认门禁与模板清理
- 日期：2026-05-27
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 责任范围：工作空间执行约束、实施计划模板、workflow skill、升级提示词、模板目录结构和 Git 忽略规则
- 对应目录 / 仓库：`/Users/qiang/github/open-teams`

## 2. 目标与背景

- 需求目标：
  - 补充“实施计划必须经用户确认后才能进入实施阶段”的强约束。
  - 移除价值较低且可能造成误导的 `example-project/` 示例目录。
  - 在 `.gitignore` 中补充 `sources/` 忽略规则，避免业务源码库进入模板仓库造成 Git 污染。
- 背景说明：
  - 当前已有“方案确认 -> 计划落档 -> 节点验收”机制，但仍需显式补充“实施计划确认”门禁，避免把“方案确认”误当成“计划已确认”。
  - 当前模板已经具备 `docs/`、`skills/_templates/`、workflow skills 和升级机制，`example-project/` 的示例价值降低。
  - `sources/` 可承载真实业务源码，但模板仓库不应默认提交业务代码。
- 当前现状：
  - 当前分支 `codex/superpowers-workspace-improvements` 已推送远端且工作区干净。
  - 根 README 仍列出 `example-project/`。
  - `.gitignore` 当前仅包含 `.DS_Store`。
- 已知约束：
  - 本次用户新增强约束：实施计划必须与用户确认后，才能进入实施阶段。
  - 本方案文档落地后，仍必须等待用户明确确认实施计划，才可进入实施。
- 不在本次范围：
  - 不调整真实业务项目源码。
  - 不改变 `sources/README.md` 的说明文件保留策略。
  - 不做自动迁移或发布版本。

## 3. 方案内容

- 方案结论：新增实施计划确认门禁，清理 `example-project/` 示例目录，并通过 `.gitignore` 默认忽略 `sources/` 下业务源码，仅保留 `sources/README.md`。
- 目标落点：
  - `AGENTS.md`：在方案记录机制、实施计划与节点验收机制中明确“实施计划确认”门禁。
  - `skills/_workflow/writing-implementation-plan/SKILL.md`：退出条件改为计划文档落地且经用户确认后才能进入实施。
  - `task-plans/TEMPLATE.md`：补充实施计划确认字段。
  - `docs/development-specs/workspace-upgrade-prompts.md`：升级计划相关提示词要求计划落地后等待用户确认。
  - `README.md`：删除 `example-project/` 目录说明，并补充 `sources/` 默认忽略真实源码的说明。
  - `.gitignore`：增加 `sources/*` 和 `!sources/README.md`。
  - `example-project/`：删除示例目录。
  - 版本和历史记录：按需更新 `CHANGELOG.md`、`workspace-version.yaml`、`change-history/open-teams/`。
- 涉及模块 / 页面 / 服务：
  - 工作空间治理约束、workflow skill、任务计划模板、升级提示词、模板目录结构和版本记录。
- 涉及目录 / 文件：
  - `AGENTS.md`
  - `README.md`
  - `.gitignore`
  - `example-project/`
  - `task-plans/TEMPLATE.md`
  - `skills/_workflow/writing-implementation-plan/SKILL.md`
  - `docs/development-specs/workspace-upgrade-prompts.md`
  - `CHANGELOG.md`
  - `workspace-config/workspace-version.yaml`
  - `change-history/open-teams/`
- 预期影响范围：
  - AI 执行流程更严格，避免未经确认的实施计划直接进入修改阶段。
  - 模板结构更干净，避免示例项目和真实业务源码污染模板仓库。
- 风险点：
  - 删除 `example-project/` 后，若某些说明仍引用它会造成断链，需要同步清理。
  - `sources/` 忽略规则需保留 `sources/README.md`，否则模板说明文件会丢失。
- 方案调整规则：
  - 若方案、实施路径、节点拆分、验收方式或优先级发生调整，必须先与用户确认，再同步更新本文档。

## 4. 实施计划

### 4.1 节点总览

| 节点 | 名称 | 状态 | 验收结论 |
| --- | --- | --- | --- |
| 节点 1 | 实施计划确认门禁与模板清理 | 已验收 | 验收通过 |
| 节点 2 | 验证、版本记录与提交 | 已验收 | 验收通过 |

状态说明：

- `未开始`：节点尚未启动
- `进行中`：节点正在实施
- `已完成`：节点已完成实现和自检，待用户验收
- `已验收`：节点已获用户明确验收通过

### 4.2 节点实施明细

#### 节点 1

- 节点名称：实施计划确认门禁与模板清理
- 当前状态：`已验收`
- 目标：
  - 将“实施计划必须经用户确认后才能实施”写入最高约束、计划模板和相关 workflow/prompt。
  - 删除 `example-project/` 并更新根 README。
  - 为 `sources/` 增加 Git 忽略规则。
- 前置条件：
  - 本实施计划经用户明确确认。
- 实施步骤：
  1. 更新 `AGENTS.md`，补充实施计划确认门禁。
  2. 更新 `skills/_workflow/writing-implementation-plan/SKILL.md`，要求计划落地并经用户确认后才能进入实施。
  3. 更新 `task-plans/TEMPLATE.md`，新增实施计划确认字段。
  4. 更新 `docs/development-specs/workspace-upgrade-prompts.md`，让升级计划提示词明确“计划确认后再实施”。
  5. 删除 `example-project/`，并从 `README.md` 移除相关目录说明。
  6. 更新 `.gitignore`，添加 `sources/*` 和 `!sources/README.md`。
- 验证方式：
  - 检索确认不再引用 `example-project/`。
  - 检查 `.gitignore` 包含 `sources/` 忽略和 `sources/README.md` 例外。
  - 检索确认实施计划确认门禁在约束、workflow 和模板中均有体现。
- 验收标准：
  - 文档和 workflow 均明确“方案确认不等于实施计划确认”。
  - `example-project/` 已删除且无残留引用。
  - `sources/README.md` 保留，`sources/` 真实源码默认不会被 Git 跟踪。
- 完成说明：已在 `AGENTS.md`、`writing-implementation-plan` workflow、`task-plans/TEMPLATE.md` 和升级提示词中补充实施计划确认门禁；已从根 README 移除 `example-project/` 说明并删除该示例目录；已在 `.gitignore` 中补充 `sources/*` 与 `!sources/README.md`，默认避免真实业务源码进入模板仓库。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已检索正式入口文档和资产目录，确认无 `example-project` 残留引用；已确认 `.gitignore` 包含 `sources/` 忽略和 `sources/README.md` 例外；已确认最高约束、workflow 和计划模板均体现实施计划确认门禁。
- 遗留事项：节点 1 当前仅待用户验收；节点 2 尚需更新版本记录/变更历史并提交推送。
- 用户验收结论：用户明确回复“验收通过，继续”。
- 用户验收时间：2026-05-29

#### 节点 2

- 节点名称：验证、版本记录与提交
- 当前状态：`已验收`
- 目标：
  - 完成模板校验、版本记录和变更历史收口，并提交推送追加改动。
- 前置条件：
  - 节点 1 获得用户明确验收通过。
- 实施步骤：
  1. 运行 `python3 scripts/validate_template_layout.py .`。
  2. 按需更新 `CHANGELOG.md`、`workspace-version.yaml` 和 `change-history/open-teams/`。
  3. 检查变更范围。
  4. 提交并推送当前分支追加改动。
- 验证方式：
  - 模板校验通过。
  - Git 状态和提交记录清晰。
- 验收标准：
  - 本次补充改动已形成追加提交并推送到当前远端分支。
- 完成说明：已运行最终模板校验，更新 `CHANGELOG.md` 与 `workspace-version.yaml` 到 `0.3.1`，补充 `change-history/open-teams/2026-05-29-feature-refactor-plan-gate-and-template-cleanup.md`，并准备提交推送当前分支追加改动。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已检索确认 `0.3.1`、实施计划确认门禁、`sources/` 忽略规则和变更历史记录均已同步。
- 遗留事项：无。提交和推送完成后，本任务收口。
- 用户验收结论：用户明确回复“验收通过，继续”。
- 用户验收时间：2026-05-29

## 5. 验证与验收计划

- 整体验证策略：
  - 节点 1 只验证本次约束与模板清理改动。
  - 节点 2 负责最终校验、版本记录和提交推送。
- 关键验证项：
  - 实施计划确认门禁是否贯穿最高约束、计划模板和 workflow。
  - `example-project/` 是否完全清理。
  - `sources/` 忽略规则是否保护真实业务源码。
  - 模板校验是否通过。
- 用户验收方式：
  - 先确认本实施计划，确认后进入节点 1。
  - 每个节点完成后等待用户验收。
- 不纳入本次验证的内容：
  - 不创建真实业务源码目录测试仓库。
  - 不验证 GitHub PR 创建能力。

## 6. 用户确认

### 6.1 方案确认

- 用户是否已明确同意该方案：是
- 用户确认原话 / 结论：用户回复“确认”。
- 确认时间：2026-05-27

### 6.2 实施计划确认

- 用户是否已明确同意实施计划：是
- 用户确认原话 / 结论：用户回复“确认”。
- 确认时间：2026-05-27

### 6.3 实施中调整记录

| 日期 | 调整内容 | 调整原因 | 是否已获用户确认 | 文档是否已同步 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 7. 完成判定

- 是否已完成全部实施节点：是，节点 1 与节点 2 均已完成并验收。
- `task-plans` 文档状态是否已同步到最新：是，节点 1 与节点 2 均为 `已验收`。
- 是否仍存在未完成项 / 风险项：无明确未完成项；真实业务工作空间升级时仍需确认本地 `sources/` 管理策略。
- 最终完成结论：任务已完成，实施计划确认门禁、模板清理、`sources/` 忽略规则、版本记录和变更历史均已收口。

## 8. 备注

- 后续补充：
  - 用户确认实施计划后，再开始节点 1。
