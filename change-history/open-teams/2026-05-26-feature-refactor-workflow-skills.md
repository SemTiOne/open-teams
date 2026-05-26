# 参考 Superpowers 优化工作空间流程资产

## 1. 基本信息

- 日期：2026-05-26
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 标题：参考 `obra/superpowers` 优化工作空间流程资产
- 对应方案 / 实施计划：`task-plans/2026-05-26-feature-refactor-superpowers-workflow-assets.md`

## 2. 任务背景

- 背景：当前模板已有较强的 `AGENTS.md` 治理约束，但主要集中在长规则文档中，缺少可按任务阶段触发、复用和校验的流程型 skill。
- 触发原因：用户要求参考 `obra/superpowers` 检查当前工作空间优化空间，并在方案确认后逐节点实施。
- 目标：保留原有方案确认、节点验收、复盘沉淀机制，同时补齐 workflow skill 层、入口路由、自动校验与模板定位说明。

## 3. 核心改动

- 改动概述：
  - 新增工作空间流程 skill 设计规范，明确 workflow skill 与项目场景 skill 的职责边界。
  - 新增五类 workflow skills：方案确认、实施计划、系统化排错、完成前验证、分支与工作树流程。
  - 更新 `AGENTS.md`、根 `README.md`、`skills/README.md`、`workspace-assets-index.md` 和项目场景 skill 模板，确保新流程资产和原有约束自洽。
  - 增强 `scripts/validate_template_layout.py`，校验 workflow 文件、必备章节、入口登记和模板卫生。
  - 新增 `.gitignore` 并移除已跟踪的 `.DS_Store`。
- 关键目录 / 文件：
  - `AGENTS.md`
  - `README.md`
  - `docs/development-specs/workflow-skills-design.md`
  - `skills/README.md`
  - `skills/_workflow/*/SKILL.md`
  - `skills/_templates/project/scene-template/SKILL.md`
  - `workspace-assets-index.md`
  - `scripts/validate_template_layout.py`
  - `.gitignore`
- 是否涉及代码、配置、脚本、文档或接口行为变化：涉及文档、skill 资产、校验脚本和模板文件卫生，不涉及业务接口行为。

## 4. 验证结果

- 已执行验证：
  - `python3 scripts/validate_template_layout.py .`
  - 临时副本异常用例验证：缺 workflow 文件、缺必备章节、入口未登记、缺 `.DS_Store` 忽略规则、存在 `.DS_Store` 文件。
- 验证通过项：
  - 当前模板结构校验通过。
  - 五类 workflow skills 均具备必备章节并在入口登记。
  - 异常用例均能被校验脚本拦截。
- 未验证项：
  - 未在真实业务线工作空间中进行迁移试用。
- 风险与遗留：
  - 后续新增或调整 workflow skill 时，需要同步 `skills/README.md`、`docs/development-specs/workflow-skills-design.md` 和 `scripts/validate_template_layout.py`；若影响最高协作规则，还需同步 `AGENTS.md`。

## 5. 用户确认

- 用户是否确认任务完成：是
- 用户确认时间：2026-05-26
- 用户确认结论：用户明确回复“任务完成”，并确认复盘结论。

## 6. 复盘结论

- 是否进行了复盘：是
- 复盘结论：本次改动将原本集中在 `AGENTS.md` 中的长规则，拆解为可触发、可复用、可校验的 workflow skill 层；同时保留工作空间原有的人机确认和节点验收机制。关键经验是新增流程资产不能只加 skill 文件，还必须同步最高约束、入口路由、根 README、设计规范和自动校验，否则容易出现组织层级与执行顺序不自洽。
- 若免复盘，原因：不适用。

## 7. 资料同步

- 已同步资料：
  - `docs/development-specs/workflow-skills-design.md`
  - `skills/_workflow/*/SKILL.md`
  - `skills/README.md`
  - `skills/_templates/project/scene-template/SKILL.md`
  - `workspace-assets-index.md`
  - `README.md`
  - `AGENTS.md`
  - `task-plans/2026-05-26-feature-refactor-superpowers-workflow-assets.md`
- 同步原因：
  - 保证工作空间入口、最高约束、流程资产、项目场景模板和校验脚本对同一套 workflow 机制有一致描述。
  - 沉淀可复用的 AI 协作流程资产，避免后续任务重新依赖临场解释。
  - 避免新增 workflow skill 后出现入口未登记、章节不完整或模板卫生问题。
- 未同步资料及原因：
  - `references/` 未更新：本次没有新增外围事实、数据字典或外部系统资料。

## 8. 备注

- 其他补充：本任务的源码/文档变更尚未提交；如需版本维护，应在用户确认后再执行提交或推送。
