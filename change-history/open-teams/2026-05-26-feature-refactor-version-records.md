# 工作空间版本记录机制

## 1. 基本信息

- 日期：2026-05-26
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 标题：工作空间版本记录机制
- 对应方案 / 实施计划：`task-plans/2026-05-26-feature-refactor-version-records.md`

## 2. 任务背景

- 背景：已有 `workspace-version.yaml` 偏机器可读，`change-history/` 偏任务过程追溯，缺少面向工作空间使用者的版本说明入口。
- 触发原因：用户指出当前工作空间缺少对应的版本记录说明，使用者无法直接感知每个版本做了什么。
- 目标：新增用户可读版本记录和版本规则说明，使模板版本变化、升级影响和推荐升级提示词可被直接查看。

## 3. 核心改动

- 改动概述：
  - 新增 `CHANGELOG.md`，记录 `0.1.0`、`0.2.0`、`0.3.0` 的能力变化、升级影响、兼容性和推荐升级提示词。
  - 新增 `docs/development-specs/workspace-versioning.md`，说明版本号规则、版本记录格式，以及 `CHANGELOG.md`、`workspace-version.yaml`、`change-history/` 的职责边界。
  - 更新 `workspace-config/workspace-version.yaml` 到 `0.3.0`，补充 changelog 路径、版本规则路径和 `user-readable-version-records` 能力。
  - 更新 README、资产索引、开发规范入口和校验脚本。
- 关键目录 / 文件：
  - `CHANGELOG.md`
  - `docs/development-specs/workspace-versioning.md`
  - `workspace-config/workspace-version.yaml`
  - `README.md`
  - `workspace-assets-index.md`
  - `docs/development-specs/README.md`
  - `scripts/validate_template_layout.py`
- 是否涉及代码、配置、脚本、文档或接口行为变化：涉及模板文档、配置和校验脚本，不涉及业务接口行为。

## 4. 验证结果

- 已执行验证：
  - `python3 scripts/validate_template_layout.py .`
  - 临时副本删除 `CHANGELOG.md` 的失败用例。
- 验证通过项：
  - 当前模板校验通过。
  - 缺少 `CHANGELOG.md` 时校验脚本会失败。
  - README、资产索引和版本元信息均可定位版本记录。
- 未验证项：
  - 未实现自动生成版本记录。
- 风险与遗留：
  - 后续新增模板能力时，需要同步维护 `CHANGELOG.md`、`workspace-version.yaml` 和相关入口，避免版本说明与实际能力不一致。

## 5. 用户确认

- 用户是否确认任务完成：是
- 用户确认时间：2026-05-26
- 用户确认结论：用户确认补充版本记录机制，并要求在当前分支追加。

## 6. 复盘结论

- 是否进行了复盘：是
- 复盘结论：版本感知不能只依赖机器可读元信息或任务级变更历史。`CHANGELOG.md` 面向用户回答“每个版本做了什么”，`workspace-version.yaml` 面向 AI 回答“当前应用了哪些能力”，`change-history/` 面向追溯回答“某次任务怎么做的”。三者职责分离后，业务工作空间用户才能判断是否需要升级以及如何触发 AI 升级。
- 若免复盘，原因：不适用。

## 7. 资料同步

- 已同步资料：
  - `CHANGELOG.md`
  - `docs/development-specs/workspace-versioning.md`
  - `workspace-config/workspace-version.yaml`
  - `README.md`
  - `workspace-assets-index.md`
  - `docs/development-specs/README.md`
  - `scripts/validate_template_layout.py`
  - `task-plans/2026-05-26-feature-refactor-version-records.md`
- 同步原因：
  - 保证用户可读版本记录、机器可读版本元信息和模板校验规则一致。
  - 帮助业务工作空间使用者感知版本变化和升级影响。
- 未同步资料及原因：
  - `references/` 未更新：本次没有新增外围事实。

## 8. 备注

- 其他补充：本记录随当前 PR 分支追加提交。
