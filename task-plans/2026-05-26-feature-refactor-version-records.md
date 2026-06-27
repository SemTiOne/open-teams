# 工作空间版本记录机制方案

## 1. 基本信息

- 任务标题：工作空间版本记录机制
- 日期：2026-05-26
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 责任范围：用户可读版本记录、版本规则说明、版本元信息和校验接入
- 对应目录 / 仓库：open-teams 模板仓库根目录

## 2. 目标与背景

- 需求目标：让使用者能够直接感知每个工作空间模板版本做了什么、是否需要升级、如何升级。
- 背景说明：当前已有 `workspace-version.yaml` 和任务级 `change-history/`，但前者偏机器可读，后者偏任务过程追溯，缺少面向用户的版本说明入口。
- 当前现状：当前分支已完成 workflow skill、升级机制和版本元信息建设，并已推送远端；本任务在同一分支追加小提交。
- 已知约束：版本记录应保持模板级、用户可读，不引入业务线专有事实；仍需通过模板校验。
- 不在本次范围：不实现自动生成 changelog，不重写历史 Git 提交。

## 3. 方案内容

- 方案结论：新增根目录 `CHANGELOG.md` 作为用户可读版本记录，新增版本规则说明文档，更新版本元信息和入口文档，并将版本记录资产纳入模板校验。
- 目标落点：
  - `CHANGELOG.md`：记录每个模板版本的新增能力、升级影响、兼容性和建议升级提示词。
  - `docs/development-specs/workspace-versioning.md`：说明版本号规则、版本记录格式和 `CHANGELOG.md`、`workspace-version.yaml`、`change-history/` 的关系。
  - `workspace-config/workspace-version.yaml`：补充版本记录路径和当前版本说明。
  - `README.md`、`docs/development-specs/README.md`、`workspace-assets-index.md`：补充版本记录入口。
  - `scripts/validate_template_layout.py`：检查版本记录资产存在。
- 涉及模块 / 页面 / 服务：模板文档、配置和校验脚本。
- 涉及目录 / 文件：`CHANGELOG.md`、`docs/development-specs/`、`workspace-config/workspace-version.yaml`、`README.md`、`workspace-assets-index.md`、`scripts/validate_template_layout.py`。
- 预期影响范围：增强用户对模板版本变化的可感知性，辅助业务工作空间决定是否升级。
- 风险点：版本号与实际能力不一致会误导升级判断；因此版本记录需与 `workspace-version.yaml` 和变更历史保持一致。
- 方案调整规则：
  - 若版本号规则或记录格式需要调整，应先与用户确认，再同步本文档和相关入口。

## 4. 实施计划

### 4.1 节点总览

| 节点 | 名称 | 状态 | 验收结论 |
| --- | --- | --- | --- |
| 节点 1 | 版本记录资产与校验接入 | 已验收 | 验收通过 |
| 节点 2 | 版本迁移指南 | 已验收 | 验收通过 |

状态说明：

- `未开始`：节点尚未启动
- `进行中`：节点正在实施
- `已完成`：节点已完成实现和自检，待用户验收
- `已验收`：节点已获用户明确验收通过

### 4.2 节点实施明细

#### 节点 1

- 节点名称：版本记录资产与校验接入
- 当前状态：`已验收`
- 目标：补齐用户可读版本记录、版本规则说明、版本元信息引用和校验脚本检查。
- 前置条件：用户明确确认补充版本记录机制。
- 实施步骤：
  1. 新增 `CHANGELOG.md`，记录当前版本能力。
  2. 新增 `docs/development-specs/workspace-versioning.md`，说明版本规则和记录关系。
  3. 更新 `workspace-version.yaml`、README、资产索引和开发规范入口。
  4. 更新模板校验脚本并执行验证。
- 验证方式：运行 `python3 scripts/validate_template_layout.py .`；构造缺失 `CHANGELOG.md` 的失败用例。
- 验收标准：用户可从根入口看到版本记录，AI 可从版本元信息定位 changelog，校验能发现版本记录缺失。
- 完成说明：已新增 `CHANGELOG.md` 和 `docs/development-specs/workspace-versioning.md`，更新 `workspace-config/workspace-version.yaml` 的版本号、修订标识、版本记录路径和已应用能力，并在 README、资产索引、开发规范入口和模板校验脚本中接入版本记录资产。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已在临时复制目录删除 `CHANGELOG.md`，确认校验脚本会失败并提示缺失版本记录。
- 遗留事项：无。该小任务作为当前 PR 分支追加提交收口。
- 用户验收结论：用户已确认补充版本记录机制，并要求当前分支追加。
- 用户验收时间：2026-05-26

#### 节点 2

- 节点名称：版本迁移指南
- 当前状态：`已验收`
- 目标：为已采用模板的用户提供版本升级操作手册，覆盖常见迁移场景、本地定制保护策略和故障回退。
- 前置条件：节点 1 已完成（CHANGELOG + versioning 规范已就位）。
- 实施步骤：
  1. 创建 `docs/development-specs/workspace-migration-guide.md`，包含：版本体系速览、升级前检查、三步标准升级流程、3 个常见迁移场景（v0.4.2→v0.4.3 / v0.4.3→v0.4.4 / v0.3→v0.4）、本地定制保护矩阵、故障回退、FAQ。
  2. 更新 `docs/development-specs/README.md` 添加入口链接。
  3. 更新 `task-plans/` 记录节点 2 完成。
  4. 更新 `TASKS.md` 标记任务完成。
- 验证方式：文件存在且内容覆盖所有设计章节；README 入口链接可跳转；模板校验通过。
- 验收标准：用户可从开发规范入口找到迁移指南，覆盖了 PATCH/MINOR 两种常见升级场景，本地定制保护策略明确。
- 完成说明：已创建 `docs/development-specs/workspace-migration-guide.md`（8 个章节），更新开发规范 README 入口。
- 验证结果：`python3 scripts/validate_template_layout.py .` 通过。
- 遗留事项：无。
- 用户验收结论：用户确认推进节点 2。
- 用户验收时间：2026-06-27

## 5. 验证与验收计划

- 整体验证策略：验证版本记录资产、入口接入和迁移指南，不扩大到其他工作空间机制。
- 关键验证项：`CHANGELOG.md` 可读、版本规则清晰、入口可定位、校验脚本有效、迁移指南覆盖常见场景。
- 用户验收方式：提交完成说明、验证结果和后续提交状态。
- 不纳入本次验证的内容：自动发布版本、自动生成版本记录。

## 6. 用户确认

### 6.1 方案确认

- 用户是否已明确同意该方案：是
- 用户确认原话 / 结论：`确认补充版本记录机制`
- 确认时间：2026-05-26

### 6.2 实施中调整记录

| 日期 | 调整内容 | 调整原因 | 是否已获用户确认 | 文档是否已同步 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 7. 完成判定

- 是否已完成全部实施节点：是，节点 1 和节点 2 均已完成并验收。
- `task-plans` 文档状态是否已同步到最新：是，节点 1 和节点 2 均已标记为 `已验收`。
- 是否仍存在未完成项 / 风险项：无。
- 最终完成结论：任务已完成。用户可读版本记录、版本规则说明、版本元信息、校验接入和版本迁移指南均已收口。

## 8. 备注

- 后续补充：本任务作为当前 PR 分支的追加小提交。
