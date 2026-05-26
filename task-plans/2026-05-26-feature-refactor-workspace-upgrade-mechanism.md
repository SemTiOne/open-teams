# 工作空间版本维护与提示词驱动升级机制方案

## 1. 基本信息

- 任务标题：工作空间版本维护与提示词驱动升级机制
- 日期：2026-05-26
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 责任范围：通用工作空间模板的版本元信息、升级流程、提示词资产、入口索引与校验机制
- 对应目录 / 仓库：`/Users/qiang/github/open-teams`
- 开发分支：`codex/superpowers-workspace-improvements`

## 2. 目标与背景

- 需求目标：为当前工作空间提供版本维护机制，使具体业务场景能够通过 AI 交互提示词触发并持续按需升级工作空间。
- 背景说明：当前模板已具备 workflow skill、任务计划、节点验收、复盘和变更历史机制，但还缺少描述模板版本、已应用能力和升级策略的元信息，以及面向业务工作空间的升级提示词与执行流程。
- 当前现状：已在当前分支完成流程资产与校验能力增强；本任务将在该分支继续追加，不拆分新的开发分支。
- 已知约束：升级机制必须遵循当前工作空间的方案确认、计划落档、节点验收和变更历史规则；不得设计成无确认地自动覆盖业务线本地定制。
- 不在本次范围：不实现远程模板拉取、自动合并、跨仓库发布服务或真实业务线升级迁移。

## 3. 方案内容

- 方案结论：新增提示词驱动的工作空间升级机制，以版本元信息记录模板能力基线，以 `workspace-upgrade` workflow skill 约束升级流程，以提示词文档提供可复制交互入口，以校验脚本保证升级资产完整。
- 目标落点：
  - `workspace-config/workspace-version.yaml`：记录模板版本、修订、已应用能力、升级策略和本地定制说明。
  - `docs/development-specs/workspace-upgrade-model.md`：说明版本维护模型、升级边界和采用方式。
  - `skills/_workflow/workspace-upgrade/SKILL.md`：提供提示词触发后的升级执行流程。
  - `docs/development-specs/workspace-upgrade-prompts.md`：沉淀面向 AI 的升级交互提示词。
  - 入口文档与校验脚本：接入 README、索引、skills 入口、开发规范入口和模板校验。
- 涉及模块 / 页面 / 服务：工作空间模板文档、workflow skills、工作空间配置和校验脚本。
- 涉及目录 / 文件：`workspace-config/`、`docs/development-specs/`、`skills/_workflow/`、`README.md`、`workspace-assets-index.md`、`skills/README.md`、`scripts/validate_template_layout.py`、`task-plans/`、`change-history/`。
- 预期影响范围：提升业务工作空间按需升级模板能力的可操作性和可审计性；不改变业务代码或运行行为。
- 风险点：如果升级提示词被理解为“无确认自动覆盖”，可能破坏业务线本地定制；因此文档和 skill 必须明确先方案、再确认、再节点实施的流程。
- 方案调整规则：
  - 若方案、实施路径、节点拆分、验收方式或优先级发生调整，必须先与用户确认，再同步更新本文档。

## 4. 实施计划

### 4.1 节点总览

| 节点 | 名称 | 状态 | 验收结论 |
| --- | --- | --- | --- |
| 节点 1 | 版本维护模型设计 | 已验收 | 验收通过 |
| 节点 2 | 升级 workflow skill 与提示词文档 | 已验收 | 验收通过 |
| 节点 3 | 入口与校验接入 | 已验收 | 验收通过 |
| 节点 4 | 验证、复盘和变更历史 | 已验收 | 验收通过 |

状态说明：

- `未开始`：节点尚未启动
- `进行中`：节点正在实施
- `已完成`：节点已完成实现和自检，待用户验收
- `已验收`：节点已获用户明确验收通过

### 4.2 节点实施明细

#### 节点 1

- 节点名称：版本维护模型设计
- 当前状态：`已验收`
- 目标：建立版本元信息和升级模型说明，明确提示词驱动升级的边界、对象、能力记录和风险控制。
- 前置条件：用户明确确认在当前分支追加实施本方案。
- 实施步骤：
  1. 新增 `workspace-config/workspace-version.yaml`，记录模板身份、版本、修订、能力清单与升级策略。
  2. 新增 `docs/development-specs/workspace-upgrade-model.md`，说明版本维护模型和提示词驱动升级边界。
  3. 按最小范围更新 `workspace-config/README.md` 与 `docs/development-specs/README.md` 的入口说明。
- 验证方式：检查新增元信息和模型说明不包含业务线专有事实；运行 `python3 scripts/validate_template_layout.py .` 确保既有校验仍通过。
- 验收标准：版本维护模型能支撑 AI 识别当前模板基线、已应用能力、升级策略和本地定制边界。
- 完成说明：已新增 `workspace-config/workspace-version.yaml`，记录模板身份、版本修订、已应用能力、升级策略和本地定制说明；已新增 `docs/development-specs/workspace-upgrade-model.md`，说明版本维护模型、升级触发方式、本地定制保护、能力粒度和验收标准；已更新 `workspace-config/README.md` 与 `docs/development-specs/README.md` 入口。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已检索新增文档，确认当前节点只落地版本元信息和升级模型说明，`workspace-upgrade` workflow 与升级提示词仍保留在节点 2 范围。
- 遗留事项：节点 1 当前仅待用户验收；节点 2 尚需落地升级 workflow skill 与提示词文档。
- 用户验收结论：用户明确回复“验收通过，继续”。
- 用户验收时间：2026-05-26

#### 节点 2

- 节点名称：升级 workflow skill 与提示词文档
- 当前状态：`已验收`
- 目标：落地 `workspace-upgrade` workflow skill 与可复制升级提示词。
- 前置条件：节点 1 获得用户明确验收通过。
- 实施步骤：新增 `skills/_workflow/workspace-upgrade/SKILL.md` 与 `docs/development-specs/workspace-upgrade-prompts.md`。
- 验证方式：检查 skill 具备必备章节，提示词覆盖检查、规划、实施、验证和收口场景。
- 验收标准：用户可通过提示词触发 AI 按治理流程完成按需升级。
- 完成说明：已新增 `skills/_workflow/workspace-upgrade/SKILL.md`，定义工作空间升级的触发条件、前置输入、产物与退出条件、工作流程、验证清单和禁止事项；已新增 `docs/development-specs/workspace-upgrade-prompts.md`，提供升级检查、规划、实施、验证、复盘和版本元信息维护的可复制提示词。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已检索 `workspace-upgrade` skill，确认具备八个必备章节；已检索提示词文档，确认检查阶段要求不修改文件，实施阶段要求写入计划、节点验收和复盘变更历史。
- 遗留事项：节点 2 当前仅待用户验收；节点 3 尚需将升级机制接入入口文档和模板校验脚本。
- 用户验收结论：用户明确回复“通过，继续”。
- 用户验收时间：2026-05-26

#### 节点 3

- 节点名称：入口与校验接入
- 当前状态：`已验收`
- 目标：将升级机制接入 README、索引、skills 入口和校验脚本。
- 前置条件：节点 2 获得用户明确验收通过。
- 实施步骤：更新相关入口文档；增强 `scripts/validate_template_layout.py` 对升级资产的校验。
- 验证方式：执行成功校验与缺失升级资产的失败用例。
- 验收标准：升级机制可从根入口定位，缺失关键升级资产能被校验发现。
- 完成说明：已将工作空间升级机制接入根 `README.md`、`workspace-assets-index.md`、`skills/README.md` 和 `docs/development-specs/workflow-skills-design.md`；已增强 `scripts/validate_template_layout.py`，将 `workspace-version.yaml`、升级模型、升级提示词和 `workspace-upgrade` workflow 纳入必需资产与章节校验。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已在临时复制目录构造缺失升级模型、缺失升级提示词、缺失 `workspace-upgrade` skill、缺失 `workspace-version.yaml`、升级 skill 缺少必备章节五类异常，脚本均返回失败并输出对应原因。
- 遗留事项：节点 3 当前仅待用户验收；节点 4 尚需执行最终验证、复盘确认和变更历史记录。
- 用户验收结论：用户明确回复“通过，继续”。
- 用户验收时间：2026-05-26

#### 节点 4

- 节点名称：验证、复盘和变更历史
- 当前状态：`已验收`
- 目标：完成最终验证、复盘确认和任务级变更历史记录。
- 前置条件：节点 3 获得用户明确验收通过。
- 实施步骤：执行最终校验，输出复盘并等待确认，补充 `change-history/open-teams/` 记录。
- 验证方式：运行模板校验并检查变更范围。
- 验收标准：任务完成结论、复盘和变更历史均已闭环。
- 完成说明：已将 `workspace-upgrade-mechanism` 追加到 `workspace-config/workspace-version.yaml` 的已应用能力清单；已完成最终模板校验和变更范围检查。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已检索 README、资产索引、skills 入口、升级模型、升级提示词、升级 workflow 和版本元信息，确认升级机制入口完整且能力基线已记录。
- 遗留事项：节点 4 已验收；复盘与变更历史已补充，后续按用户要求进行提交和创建到主分支的 MR/PR。
- 用户验收结论：用户明确回复“验收通过”，并要求提交所有改动、提交 MR 到主分支。
- 用户验收时间：2026-05-26

## 5. 验证与验收计划

- 整体验证策略：每个节点仅验证当节点新增资产的完整性和与既有模板机制的兼容性；节点完成后等待用户验收。
- 关键验证项：版本元信息格式、升级边界表达、提示词可执行性、入口可发现性、校验脚本有效性。
- 用户验收方式：按节点汇报完成内容、验证结果和遗留事项，由用户明确回复验收通过后进入下一节点。
- 不纳入本次验证的内容：真实业务工作空间升级迁移、远程模板版本对比和自动合并。

## 6. 用户确认

### 6.1 方案确认

- 用户是否已明确同意该方案：是
- 用户确认原话 / 结论：`当前分支上进行追加，确认方案`
- 确认时间：2026-05-26

### 6.2 实施中调整记录

| 日期 | 调整内容 | 调整原因 | 是否已获用户确认 | 文档是否已同步 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 7. 完成判定

- 是否已完成全部实施节点：是，四个节点均已获得用户明确验收。
- `task-plans` 文档状态是否已同步到最新：是，节点 1、节点 2、节点 3 与节点 4 均为 `已验收`。
- 是否仍存在未完成项 / 风险项：实现、验证、复盘和变更历史均已收口；后续仅剩用户要求的版本维护动作：提交、推送并创建 MR/PR。
- 最终完成结论：任务已完成，版本维护机制、升级提示词、入口校验、复盘与变更历史均已收口。

## 8. 备注

- 后续补充：本任务在当前已有未提交改动的分支上追加实施，不单独创建新分支。
