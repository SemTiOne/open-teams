# 节点级版本维护门禁

## 1. 基本信息

- 日期：2026-06-01
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 标题：节点级版本维护门禁
- 对应方案 / 实施计划：`task-plans/2026-05-29-feature-refactor-node-version-maintenance-gate.md`

## 2. 任务背景

- 背景：工作空间已有方案确认、实施计划确认和节点验收机制，但 workflow skill、任务计划模板和升级提示词还需要更明确地承载节点验收后的提交推送门禁。
- 触发原因：用户要求每次任务开始显式确认分支信息，并要求每个节点验收通过后先提交推送，再进入下一个节点。
- 目标：让根约束、workflow skill、任务计划模板、升级提示词和版本记录都能表达节点级版本维护规则。

## 3. 核心改动

- 改动概述：
  - 更新 `branch-and-worktree-workflow`、`writing-implementation-plan`、`verification-before-completion`、`workspace-upgrade` 四个 workflow skill，补充分支/远端跟踪确认、节点验收后提交推送、`sources` 仓库适用性和具体下一步推荐语要求。
  - 更新 `task-plans/TEMPLATE.md`，新增分支与工作区状态、节点验收后版本维护字段。
  - 更新 `docs/development-specs/workspace-upgrade-prompts.md`，要求升级计划和节点推进提示词包含节点级提交推送门禁。
  - 更新 `CHANGELOG.md` 与 `workspace-config/workspace-version.yaml` 到 `0.4.1`。
- 关键目录 / 文件：
  - `skills/_workflow/branch-and-worktree-workflow/SKILL.md`
  - `skills/_workflow/writing-implementation-plan/SKILL.md`
  - `skills/_workflow/verification-before-completion/SKILL.md`
  - `skills/_workflow/workspace-upgrade/SKILL.md`
  - `task-plans/TEMPLATE.md`
  - `docs/development-specs/workspace-upgrade-prompts.md`
  - `CHANGELOG.md`
  - `workspace-config/workspace-version.yaml`
- 是否涉及代码、配置、脚本、文档或接口行为变化：涉及模板文档、workflow skill、升级提示词和版本元信息，不涉及业务接口行为。

## 4. 验证结果

- 已执行验证：
  - `python3 scripts/validate_template_layout.py .`
  - 检索 workflow skill、任务计划模板、升级提示词和版本记录中的分支确认、节点提交推送、`sources` 和具体推荐语表述。
- 验证通过项：
  - 模板校验通过。
  - 四个 workflow skill 均覆盖分支/远端跟踪、用户验收后提交推送、`sources` 适用性和具体推荐语要求。
  - 任务计划模板和升级提示词能承载节点级版本维护字段。
- 未验证项：
  - 未对真实 `sources` 源码仓库执行提交推送。
- 风险与遗留：
  - 该规则会让多节点任务更严格；纯讨论或不进入实施阶段的任务仍不应强制套用提交推送门禁。

## 5. 用户确认

- 用户是否确认任务完成：是
- 用户确认时间：2026-06-01
- 用户确认结论：用户已验收节点 2、节点 3、节点 4，并明确回复确认任务完成与复盘结论。

## 6. 复盘结论

- 是否进行了复盘：是，极简复盘。
- 复盘结论：原有治理规则已覆盖方案确认、实施计划确认和节点验收，但 workflow skill、任务计划模板、升级提示词、版本记录之间对“节点验收后必须提交推送”的表达不够一致。本次补齐四个 workflow skill、任务计划模板、升级提示词、版本记录、版本元信息和变更历史，让“任务开始确认分支、节点验收后提交推送、再进入下一节点”成为可执行、可追溯的模板能力。该规则适合进入实施阶段且有节点产物的任务；纯讨论、评估、只读分析任务不应机械套用提交推送门禁。
- 若免复盘，原因：不适用。

## 7. 资料同步

- 已同步资料：
  - `skills/_workflow/branch-and-worktree-workflow/SKILL.md`
  - `skills/_workflow/writing-implementation-plan/SKILL.md`
  - `skills/_workflow/verification-before-completion/SKILL.md`
  - `skills/_workflow/workspace-upgrade/SKILL.md`
  - `task-plans/TEMPLATE.md`
  - `docs/development-specs/workspace-upgrade-prompts.md`
  - `CHANGELOG.md`
  - `workspace-config/workspace-version.yaml`
  - `task-plans/2026-05-29-feature-refactor-node-version-maintenance-gate.md`
- 同步原因：
  - 保证节点级提交推送门禁在执行 skill、计划模板、升级提示词和版本记录中一致。
- 未同步资料及原因：
  - `references/` 未更新：本次没有新增外围事实资料。

## 8. 备注

- 其他补充：用户已确认任务完成并确认极简复盘。`sources` 源码仓库提交推送不适用。
