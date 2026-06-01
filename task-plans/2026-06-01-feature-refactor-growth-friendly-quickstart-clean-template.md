# 推广友好、极简上手与模板去污染优化方案

## 1. 基本信息

- 任务标题：推广友好、极简上手与模板去污染优化
- 日期：2026-06-01
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 责任范围：模板定位表达、快速上手路径、初始化边界、模板资产卫生、版本与校验闭环
- 对应目录 / 仓库：`/Users/qiang/github/open-teams`

## 2. 目标与背景

- 需求目标：
  - 优化项目对外表达，使模板更适合推广、传播和获取 GitHub star。
  - 进一步极致简化上手路径，让用户能快速把壳工程用于自己的项目。
  - 避免用户基于模板创建业务工作空间时，将模板自身迭代记录、任务计划或历史沉淀一并带过去造成信息污染。
- 背景说明：
  - 当前模板已经具备工作空间骨架、workflow skills、版本维护、任务计划和变更历史机制，但首屏价值表达仍偏工程治理说明，对新用户的即时吸引力不足。
  - 当前初始化步骤较完整，但对首次使用者来说路径偏长，缺少“最小可用”和“推荐增强”的分层入口。
  - `task-plans/`、`change-history/`、`CHANGELOG.md`、`workspace-version.yaml` 等资产在模板仓库内有维护价值，但被用户复制为业务工作空间时需要明确哪些应保留、重置或清理。
- 当前现状：
  - 当前分支：`codex/superpowers-workspace-improvements`，远端跟踪分支为 `origin/codex/superpowers-workspace-improvements`。
  - 当前工作区已有未提交改动：
    - `skills/_workflow/branch-and-worktree-workflow/SKILL.md`
    - `skills/_workflow/verification-before-completion/SKILL.md`
    - `skills/_workflow/workspace-upgrade/SKILL.md`
    - `skills/_workflow/writing-implementation-plan/SKILL.md`
    - `task-plans/2026-05-29-feature-refactor-node-version-maintenance-gate.md`
  - `workspace-config/code-sources.yaml` 当前仍为示例映射，本任务暂不涉及真实 `sources/` 源码仓库。
- 已知约束：
  - 已完成分支信息与总体方案确认。
  - 方案确认不等于实施计划确认；本文档落地后，仍必须等待用户明确确认实施计划，才能进入实际实施。
  - 不得覆盖、回退或清理用户已有改动；实施时需区分既有脏改动与本任务新增改动。
- 不在本次范围：
  - 不修改真实业务源码。
  - 不直接发布 GitHub Release 或创建 PR。
  - 不重构 workflow governance 的核心确认门禁。
  - 不清理当前仓库已有历史任务记录本身，只定义模板复制或初始化时的去污染边界。

## 3. 方案内容

- 方案结论：
  - 以“先提高新用户理解和传播效率，再压缩上手路径，最后建立模板复制去污染机制”为主线，分节点优化模板对外入口、初始化体验和模板卫生规则。
- 目标落点：
  - 对外表达：让 README 首屏更像开源项目入口，突出价值、使用场景、快速开始和可信治理能力。
  - 上手简化：建立最短路径文档或入口，让用户可以按“最小可用 -> 推荐增强 -> 治理闭环”逐步采用。
  - 模板去污染：明确模板自身维护资产与用户业务工作空间资产的保留、重置、清理边界，必要时补充初始化脚本或校验规则。
- 涉及模块 / 页面 / 服务：
  - 根 README、资产索引、初始化文档、模板配置、初始化/校验脚本、版本记录与变更历史。
- 涉及目录 / 文件：
  - `README.md`
  - `workspace-assets-index.md`
  - `docs/README.md`
  - `workspace-config/README.md`
  - `workspace-config/workspace-version.yaml`
  - `scripts/validate_template_layout.py`
  - `scripts/` 下可能新增的初始化辅助脚本
  - `CHANGELOG.md`
  - `change-history/open-teams/`
  - `task-plans/` 中本文档
- 预期影响范围：
  - 新用户更容易理解 open-teams 的价值与使用路径。
  - 用户将模板应用到自己项目时，能更清晰地区分“模板能力”和“模板仓库自身迭代记录”。
  - 模板校验和初始化说明更能支撑长期复用与传播。
- 风险点：
  - README 若过度营销化，可能削弱工程可信度；需要保持推广友好但不夸大能力。
  - 去污染机制若过度自动化，可能误删用户希望保留的资料；应优先采用明确清单与可选脚本，并保留确认边界。
  - 当前工作区已有未提交改动，实施时必须避免混入或覆盖无关变更。
- 方案调整规则：
  - 若方案、实施路径、节点拆分、验收方式或优先级发生调整，必须先与用户确认，再同步更新本文档。

## 4. 实施计划

### 4.1 节点总览

| 节点 | 名称 | 状态 | 验收结论 |
| --- | --- | --- | --- |
| 节点 1 | 推广友好入口与价值表达优化 | 已验收 | 验收通过 |
| 节点 2 | 极简上手路径与初始化指引优化 | 已验收 | 验收通过 |
| 节点 3 | 模板去污染边界与辅助机制 | 已验收 | 验收通过 |
| 节点 4 | 校验、版本记录、变更历史与收口 | 已验收 | 验收通过 |

状态说明：

- `未开始`：节点尚未启动
- `进行中`：节点正在实施
- `已完成`：节点已完成实现和自检，待用户验收
- `已验收`：节点已获用户明确验收通过

### 4.2 节点实施明细

#### 节点 1

- 节点名称：推广友好入口与价值表达优化
- 当前状态：`已验收`
- 目标：
  - 优化 `README.md` 首屏与主体结构，使项目定位、价值、适用人群和 star 友好传播点更清晰。
- 前置条件：
  - 本实施计划经用户明确确认。
- 实施步骤：
  1. 重构 `README.md` 首屏，包括项目一句话定位、核心价值、适用场景和快速开始入口。
  2. 将治理能力从“先讲规则”调整为“先讲收益，再给路径和边界”。
  3. 保留模板真实能力边界，不描述尚不存在的自动化能力。
- 验证方式：
  - 检查 README 链接有效性。
  - 检查 README 是否仍与现有目录和能力一致。
  - 人工复核是否存在夸大表述或业务线专有事实。
- 验收标准：
  - README 首屏能在短时间内说明项目解决的问题、适用对象和上手路径。
  - 不引入不存在的能力描述。
- 完成说明：已重构 `README.md` 首屏和主体结构，将项目标题调整为 `open-teams`，补充一句话定位、价值说明、适用人群、能力总览、三步快速开始、内置 workflow skills、采用方式、持续升级和模板边界。表达顺序从原先偏治理说明调整为先说明用户收益，再进入目录、流程和边界。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已检索 README 中的 Markdown 链接，确认 `docs/development-specs/workspace-upgrade-prompts.md`、`CHANGELOG.md` 和 `docs/development-specs/workspace-versioning.md` 均为真实存在路径；已检索 README 中涉及业务线、账号、测试地址、自动化等表述，未发现引入业务线专有事实或不存在能力。
- 遗留事项：节点 1 仅完成推广友好入口与价值表达优化；更完整的极简上手路径、初始化指引一致性和模板去污染机制仍按计划留在节点 2、节点 3 处理。
- 用户验收结论：用户明确回复“验收通过，继续”。
- 用户验收时间：2026-06-01

#### 节点 2

- 节点名称：极简上手路径与初始化指引优化
- 当前状态：`已验收`
- 目标：
  - 建立更短、更分层的上手路径，让用户可以先跑通最小可用工作空间，再逐步接入完整治理。
- 前置条件：
  - 节点 1 已完成并获用户验收。
- 实施步骤：
  1. 优化或新增快速上手入口，明确“最小可用”“推荐增强”“治理闭环”三层采用方式。
  2. 同步更新 `workspace-assets-index.md`、`docs/README.md` 或 `workspace-config/README.md` 中的阅读路径。
  3. 明确 `workspace-config/code-sources.yaml`、`AGENTS.md`、`docs/projects/`、`skills/<project>/` 的最小改动顺序。
- 验证方式：
  - 检查入口文档之间的推荐路径一致。
  - 确认初始化步骤不会要求用户一次性理解全部治理资产。
- 验收标准：
  - 用户可以按一条短路径完成首次可用初始化。
  - 进阶治理能力仍可从索引中按需进入。
- 完成说明：已新增 `QUICKSTART.md`，将首次采用路径拆为 `5 分钟最小可用`、`30 分钟推荐增强`、`持续治理闭环` 三层，并补充第一次应修改文件和第一次不用读的内容；已在 `README.md` 快速开始中链接该入口；已同步更新 `workspace-assets-index.md` 的首读入口、初始化路径和全局理解路径；已在 `docs/README.md` 和 `workspace-config/README.md` 中补充首次采用说明。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已检索 `README.md`、`QUICKSTART.md`、`workspace-assets-index.md`、`docs/README.md`、`workspace-config/README.md`，确认均围绕最小可用、推荐增强、治理闭环保持一致；已检索 Markdown 链接，确认新增的 `QUICKSTART.md`、`code-sources.yaml`、`workspace-version.yaml` 等链接路径真实存在。
- 遗留事项：节点 2 只处理上手路径和初始化指引一致性；模板自身迭代记录去污染边界和辅助机制仍按计划留在节点 3 处理。
- 用户验收结论：用户明确回复“验收通过”。
- 用户验收时间：2026-06-01

#### 节点 3

- 节点名称：模板去污染边界与辅助机制
- 当前状态：`已验收`
- 目标：
  - 避免用户创建业务工作空间时继承 open-teams 模板自身迭代记录，明确应保留、应重置、应清理的资产边界。
- 前置条件：
  - 节点 2 已完成并获用户验收。
- 实施步骤：
  1. 补充模板复制或初始化时的去污染说明，覆盖 `task-plans/`、`change-history/`、`CHANGELOG.md`、`workspace-version.yaml` 等易混淆资产。
  2. 评估并按需新增可选初始化辅助脚本，用于生成业务工作空间的干净初始状态。
  3. 按需更新 `scripts/validate_template_layout.py`，让模板卫生校验覆盖新增边界或脚本入口。
- 验证方式：
  - 检查去污染清单与当前真实文件结构一致。
  - 如新增脚本，运行脚本的无破坏性帮助命令或在临时目录验证输出边界。
  - 运行模板校验。
- 验收标准：
  - 用户能明确知道哪些模板资产复制后应保留、重置或删除。
  - 不会默认把模板自身任务计划和变更历史误当成业务项目事实。
- 完成说明：已将快速上手和模板去污染方案调整为 AI 对话式采用：`QUICKSTART.md` 改为让用户复制提示词给 AI，由 AI 确认目标目录、项目名称、源码路径和采用方式；新增 `scripts/adopt_workspace.py`，支持 AI 将模板复制到目标目录、调用 `prepare_clean_workspace.py --apply` 清理模板自身历史记录、写入 `workspace-config/code-sources.yaml`、更新 `workspace-config/workspace-version.yaml` 并运行模板校验；同步更新 `README.md`、`workspace-assets-index.md`、`docs/development-specs/template-adoption-cleanup.md` 和 `scripts/validate_template_layout.py`，让 AI 复制、清理、初始化与校验路径可发现、可执行、可校验。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已运行 `python3 scripts/adopt_workspace.py --help`，确认参数说明可用；已在临时目录运行 `scripts/adopt_workspace.py --template-root . --target <tmp>/demo-workspace --project-slug demo-app --project-name \"Demo App\" --source-path /tmp/demo-app --default-branch main`，确认脚本完成模板复制、清理 `task-plans/YYYY-*.md` 和 `change-history/open-teams/`、保留 `task-plans/README.md`、`task-plans/TEMPLATE.md`、`change-history/README.md`、`change-history/TEMPLATE.md`、写入源码映射、更新版本元信息，并通过目标工作空间模板校验。
- 遗留事项：`adopt_workspace.py` 已覆盖复制、清理、源码映射、版本元信息和校验；`AGENTS.md` 的业务线专属约束仍需 AI 在初始化对话中结合用户团队规则继续改写，不在脚本中强行生成。
- 用户验收结论：用户明确回复“验收通过”。
- 用户验收时间：2026-06-01

#### 节点 4

- 节点名称：校验、版本记录、变更历史与收口
- 当前状态：`已验收`
- 目标：
  - 完成本次优化的最终校验、版本记录、变更历史和任务收口。
- 前置条件：
  - 节点 3 已完成并获用户验收。
- 实施步骤：
  1. 运行 `python3 scripts/validate_template_layout.py .`。
  2. 更新 `CHANGELOG.md` 和 `workspace-config/workspace-version.yaml`，记录本次模板能力变化。
  3. 在 `change-history/open-teams/` 补充任务级变更记录。
  4. 检查 Git 变更范围，区分本任务新增改动与进入任务前已有改动。
  5. 等用户验收通过后，按节点级门禁提交并推送当前分支。
- 验证方式：
  - 模板校验通过。
  - Git diff 范围符合本任务目标。
  - 版本记录、任务计划状态和变更历史同步。
- 验收标准：
  - 本次优化具备可追溯记录，且没有引入无关文件漂移。
- 完成说明：已完成最终收口：`CHANGELOG.md` 新增 `0.4.0` 版本记录，`workspace-config/workspace-version.yaml` 更新到 `0.4.0 / ai-guided-workspace-adoption` 并登记 `ai-guided-workspace-adoption`、`template-history-cleanup` 能力；新增 `change-history/open-teams/2026-06-01-feature-refactor-ai-guided-adoption.md` 记录任务级变更历史；已同步本文档节点 4 状态和节点 1 至节点 3 的提交推送记录。
- 验证结果：已运行 `python3 scripts/validate_template_layout.py .`，输出 `Template layout validation passed.`；已运行 `python3 scripts/adopt_workspace.py --help`，确认参数说明可用；已在临时目录运行 `scripts/adopt_workspace.py --template-root . --target <tmp>/demo-workspace --project-slug demo-app --project-name \"Demo App\" --source-path /tmp/demo-app --default-branch main`，确认目标工作空间可完成模板复制、历史清理、源码映射写入、版本元信息更新和模板校验；已检索确认 `CHANGELOG.md`、`workspace-version.yaml`、README、QUICKSTART、资产索引、校验脚本和变更历史中 `0.4.0`、`adopt_workspace.py`、`prepare_clean_workspace.py`、`template-adoption-cleanup.md` 信息一致。
- 遗留事项：当前工作区仍存在进入本任务前已有的 workflow skill 与 `task-plans/2026-05-29-feature-refactor-node-version-maintenance-gate.md` 脏改动，不属于本任务新增改动；节点 4 待用户验收通过后，再提交并推送本节点相关改动。
- 用户验收结论：用户明确回复“验收通过”。
- 用户验收时间：2026-06-01

## 5. 验证与验收计划

- 整体验证策略：
  - 每个节点完成后先更新本文档节点状态和完成说明，再向用户说明完成内容、验证结果和遗留事项，等待用户明确验收。
  - 每个节点验收通过后，按当前工作空间门禁执行必要的提交推送动作，再进入下一节点。
- 关键验证项：
  - README 和入口文档是否与当前模板真实能力一致。
  - 快速上手路径是否足够短且可执行。
  - 模板去污染边界是否覆盖历史计划、变更历史、版本记录和工作空间配置。
  - `scripts/validate_template_layout.py` 是否通过。
  - Git 变更范围是否只包含本任务相关改动。
- 用户验收方式：
  - 用户先确认本实施计划。
  - 节点 1 至节点 4 均分别等待用户明确验收。
- 不纳入本次验证的内容：
  - 不验证 GitHub star 实际增长数据。
  - 不发布正式版本或创建 GitHub Release。
  - 不验证真实业务源码仓库改造。

## 6. 用户确认

### 6.1 方案确认

- 用户是否已明确同意该方案：是
- 用户确认原话 / 结论：用户回复“确认”。
- 确认时间：2026-06-01

### 6.2 实施计划确认

- 用户是否已明确同意实施计划：是
- 用户确认原话 / 结论：用户回复“确认”。
- 确认时间：2026-06-01

### 6.3 实施中调整记录

| 日期 | 调整内容 | 调整原因 | 是否已获用户确认 | 文档是否已同步 |
| --- | --- | --- | --- | --- |
| 2026-06-01 | 将快速上手与模板复制方式从“用户手动复制、手动清理、手动初始化”调整为“AI 对话式复制模板、清理模板历史、写入源码映射、更新版本元信息并运行校验” | 用户要求快速上手通过 AI 对话完成，且复制模板也交给 AI 来完成，以进一步降低采用难度 | 是，用户回复“确认” | 是 |

## 7. 完成判定

- 是否已完成全部实施节点：是，节点 1 至节点 4 均已验收。
- `task-plans` 文档状态是否已同步到最新：是，当前已记录已确认方案、已确认实施计划、节点 1 至节点 4 验收通过状态。
- 是否仍存在未完成项 / 风险项：当前工作区存在进入本任务前已有未提交改动，后续实施需持续区分。
- 最终完成结论：全部实施节点已验收通过，待完成节点 4 提交推送后进入最终完成确认与复盘判断。

## 8. 备注

- 后续补充：
  - 节点 1 已提交并推送到 `origin/codex/superpowers-workspace-improvements`，提交为 `a3869f6 Improve project README positioning`。
  - 节点 2 已提交并推送到 `origin/codex/superpowers-workspace-improvements`，提交为 `996cefb Add quickstart adoption path`。
  - 节点 3 已提交并推送到 `origin/codex/superpowers-workspace-improvements`，提交为 `87e8085 Add AI-guided workspace adoption`。
  - 本任务暂不涉及 `sources/` 下真实源码仓库，`sources` 提交推送不适用。
