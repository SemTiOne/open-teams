# 工作空间版本维护与提示词驱动升级机制

## 1. 基本信息

- 日期：2026-05-26
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 标题：工作空间版本维护与提示词驱动升级机制
- 对应方案 / 实施计划：`task-plans/2026-05-26-feature-refactor-workspace-upgrade-mechanism.md`

## 2. 任务背景

- 背景：当前模板已有 workflow skills、任务计划、节点验收、复盘和变更历史机制，但缺少记录模板能力基线和提示词驱动升级流程的版本维护资产。
- 触发原因：用户希望具体业务场景能够持续更新升级工作空间，并希望升级方式以 AI 交互提示词形式触发，由工作空间自动按需完成升级。
- 目标：新增版本元信息、升级模型、升级 workflow、升级提示词、入口索引和校验接入，使业务工作空间可通过 AI 提示词按治理流程升级。

## 3. 核心改动

- 改动概述：
  - 新增 `workspace-config/workspace-version.yaml`，记录模板版本、已应用能力、升级策略和本地定制说明。
  - 新增 `docs/development-specs/workspace-upgrade-model.md`，定义版本维护模型、升级边界、本地定制保护和能力粒度。
  - 新增 `skills/_workflow/workspace-upgrade/SKILL.md`，约束升级检查、规划、实施、验证和收口流程。
  - 新增 `docs/development-specs/workspace-upgrade-prompts.md`，提供可复制的升级检查、规划、实施、验证、复盘和版本元信息维护提示词。
  - 更新 README、资产索引、skills 入口、流程设计规范、工作空间配置入口和校验脚本，将升级机制接入模板。
- 关键目录 / 文件：
  - `workspace-config/workspace-version.yaml`
  - `docs/development-specs/workspace-upgrade-model.md`
  - `docs/development-specs/workspace-upgrade-prompts.md`
  - `skills/_workflow/workspace-upgrade/SKILL.md`
  - `README.md`
  - `workspace-assets-index.md`
  - `skills/README.md`
  - `docs/development-specs/workflow-skills-design.md`
  - `scripts/validate_template_layout.py`
- 是否涉及代码、配置、脚本、文档或接口行为变化：涉及模板配置、文档、workflow skill 和校验脚本，不涉及业务接口行为。

## 4. 验证结果

- 已执行验证：
  - `python3 scripts/validate_template_layout.py .`
  - 临时副本异常用例验证：缺升级模型、缺升级提示词、缺 `workspace-upgrade` skill、缺 `workspace-version.yaml`、升级 skill 缺必备章节。
- 验证通过项：
  - 当前模板结构校验通过。
  - 升级机制入口可从 README、资产索引、skills 入口和开发规范入口定位。
  - 缺失升级关键资产或章节时，校验脚本能失败并输出原因。
- 未验证项：
  - 未在真实业务工作空间中执行一次完整升级迁移。
- 风险与遗留：
  - 后续真实业务工作空间升级时，仍需先识别本地定制和真实源码映射，不能用模板示例覆盖业务事实。

## 5. 用户确认

- 用户是否确认任务完成：是
- 用户确认时间：2026-05-26
- 用户确认结论：用户逐节点验收通过，并要求提交所有改动、提交 MR 到主分支。

## 6. 复盘结论

- 是否进行了复盘：是
- 复盘结论：本次机制将“工作空间持续升级”设计为提示词触发、方案确认、计划落档、节点实施、验证和变更历史沉淀的闭环，而不是无确认自动覆盖。关键经验是升级能力必须同时具备版本元信息、执行 workflow、可复制提示词、入口索引和校验脚本，否则业务工作空间难以判断自己已具备哪些模板能力、该如何按需升级，以及如何保护本地定制。
- 若免复盘，原因：不适用。

## 7. 资料同步

- 已同步资料：
  - `workspace-config/workspace-version.yaml`
  - `workspace-config/README.md`
  - `docs/development-specs/workspace-upgrade-model.md`
  - `docs/development-specs/workspace-upgrade-prompts.md`
  - `docs/development-specs/README.md`
  - `skills/_workflow/workspace-upgrade/SKILL.md`
  - `skills/README.md`
  - `workspace-assets-index.md`
  - `README.md`
  - `scripts/validate_template_layout.py`
  - `task-plans/2026-05-26-feature-refactor-workspace-upgrade-mechanism.md`
- 同步原因：
  - 保证版本维护机制可从根入口、配置入口、开发规范入口和 workflow skill 入口定位。
  - 沉淀可复制的 AI 升级提示词，支持业务工作空间按需升级。
  - 避免升级资产缺失、入口未登记或 workflow 章节不完整。
- 未同步资料及原因：
  - `references/` 未更新：本次没有新增外围事实、环境信息或第三方资料。

## 8. 备注

- 其他补充：本任务与同一分支上已完成的 workflow skills 基线任务一起提交。
