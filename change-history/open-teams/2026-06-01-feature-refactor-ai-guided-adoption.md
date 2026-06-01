# AI 对话式采用与模板去污染优化

## 1. 基本信息

- 日期：2026-06-01
- 项目：`open-teams`
- 任务类型：`feature-refactor`
- 标题：AI 对话式采用与模板去污染优化
- 对应方案 / 实施计划：`task-plans/2026-06-01-feature-refactor-growth-friendly-quickstart-clean-template.md`

## 2. 任务背景

- 背景：模板已具备 workflow skills、任务计划、版本记录和变更历史能力，但对新用户来说，上手路径仍偏手动，且复制模板时容易带入模板仓库自身迭代记录。
- 触发原因：用户要求项目更推广友好、帮助快速涨星、进一步极致简化上手，并避免模板自身历史污染用户业务工作空间；实施中进一步要求复制模板和初始化也交给 AI 对话完成。
- 目标：优化 README 对外表达，建立 AI 对话式快速上手路径，并提供模板历史清理边界和脚本化支持。

## 3. 核心改动

- 改动概述：
  - 重构 `README.md` 首屏表达，突出 open-teams 的定位、价值、适用人群、能力总览和 AI 初始化入口。
  - 新增 `QUICKSTART.md`，将快速上手改为用户提供少量信息后由 AI 完成复制、清理、初始化和校验。
  - 新增 `scripts/adopt_workspace.py`，支持复制模板、清理历史、写入源码映射、更新版本元信息和运行模板校验。
  - 新增 `scripts/prepare_clean_workspace.py` 和 `docs/development-specs/template-adoption-cleanup.md`，定义模板自身历史记录清理边界。
  - 更新 `workspace-assets-index.md`、`docs/README.md`、`workspace-config/README.md`、`docs/development-specs/README.md` 和 `scripts/validate_template_layout.py`，同步入口、采用路径和校验规则。
  - 更新 `CHANGELOG.md` 与 `workspace-config/workspace-version.yaml` 到 `0.4.0`。
- 关键目录 / 文件：
  - `README.md`
  - `QUICKSTART.md`
  - `workspace-assets-index.md`
  - `docs/development-specs/template-adoption-cleanup.md`
  - `scripts/adopt_workspace.py`
  - `scripts/prepare_clean_workspace.py`
  - `scripts/validate_template_layout.py`
  - `CHANGELOG.md`
  - `workspace-config/workspace-version.yaml`
  - `task-plans/2026-06-01-feature-refactor-growth-friendly-quickstart-clean-template.md`
- 是否涉及代码、配置、脚本、文档或接口行为变化：涉及模板文档、初始化脚本、校验脚本和版本元信息，不涉及业务接口行为。

## 4. 验证结果

- 已执行验证：
  - `python3 scripts/validate_template_layout.py .`
  - `python3 scripts/adopt_workspace.py --help`
  - 在临时目录运行 `scripts/adopt_workspace.py --template-root . --target <tmp>/demo-workspace --project-slug demo-app --project-name "Demo App" --source-path /tmp/demo-app --default-branch main`
  - 检索 README、QUICKSTART、资产索引和清理指南中的 AI 对话式采用入口。
- 验证通过项：
  - 模板校验通过。
  - `adopt_workspace.py` 参数说明可用。
  - 临时目录采用测试可复制模板、清理 `task-plans/YYYY-*.md` 与 `change-history/open-teams/`、保留模板说明文件、写入源码映射、更新版本元信息，并通过目标工作空间校验。
  - AI 对话式采用入口已在 README、QUICKSTART、资产索引、清理指南和校验脚本中同步。
- 未验证项：
  - 未连接真实远程 Git 仓库执行 clone 或 push。
  - 未验证 GitHub star 增长效果。
- 风险与遗留：
  - `AGENTS.md` 的业务线专属约束仍需 AI 在初始化对话中结合用户团队规则改写，不在脚本中强行生成。
  - 已初始化业务工作空间升级到 0.4.0 时，应先保护本地 `AGENTS.md`、源码映射和已有历史记录。

## 5. 用户确认

- 用户是否确认任务完成：是
- 用户确认时间：2026-06-01
- 用户确认结论：用户已验收节点 1 至节点 4，并明确回复“确认任务完成”。

## 6. 复盘结论

- 是否进行了复盘：是
- 复盘结论：原模板治理能力完整，但新用户采用路径偏手动，容易形成“先读文档、手动复制、手动改配置”的上手负担；同时复制模板时容易把 open-teams 自身 `task-plans/` 与 `change-history/` 带入业务工作空间。此次通过 README 首屏重构、AI 对话式 QUICKSTART、`adopt_workspace.py`、`prepare_clean_workspace.py`、模板采用清理指南和校验规则同步，把采用方式升级为由 AI 复制模板、清理历史、写入源码映射、更新版本元信息并校验。后续应继续保持“能力可发现、脚本可执行、校验可覆盖、版本可追溯”的闭环。
- 若免复盘，原因：不适用。

## 7. 资料同步

- 已同步资料：
  - `README.md`
  - `QUICKSTART.md`
  - `workspace-assets-index.md`
  - `docs/README.md`
  - `workspace-config/README.md`
  - `docs/development-specs/README.md`
  - `docs/development-specs/template-adoption-cleanup.md`
  - `scripts/adopt_workspace.py`
  - `scripts/prepare_clean_workspace.py`
  - `scripts/validate_template_layout.py`
  - `CHANGELOG.md`
  - `workspace-config/workspace-version.yaml`
  - `task-plans/2026-06-01-feature-refactor-growth-friendly-quickstart-clean-template.md`
- 同步原因：
  - 保证快速上手、模板复制、去污染清理、版本记录和校验规则一致。
  - 沉淀 AI 对话式采用能力，降低新用户使用门槛。
- 未同步资料及原因：
  - `references/` 未更新：本次没有新增外围事实资料。

## 8. 备注

- 其他补充：用户已确认复盘结论；本次资料同步已覆盖 README、QUICKSTART、资产索引、开发规范入口、初始化脚本、校验脚本、版本记录、版本元信息、任务计划和变更历史。`sources` 源码仓库提交推送不适用。
