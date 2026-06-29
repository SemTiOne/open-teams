# 工作空间资产索引模板

## 首读入口

1. `QUICKSTART.md`
2. `docs/README.md`
3. `skills/README.md`
4. `docs/overall-architecture/README.md`
5. `workspace-config/code-sources.yaml`
6. `task-completion-checklist.md`
7. `CHANGELOG.md`

## 初始化路径

### 快速初始化

1. 运行 `./init.sh`（或 `python3 init-command.py`）交互式初始化工作空间
2. 读取 `QUICKSTART.md`，让 AI 确认目标目录、项目名称、源码路径和采用方式

### AI 对话式最小可用

1. 读取 `QUICKSTART.md`，让 AI 确认目标目录、项目名称、源码路径和采用方式
2. 由 AI 调用 `scripts/adopt_workspace.py` 复制模板、清理模板自身历史记录、写入源码映射并运行校验
3. 由 AI 协助调整 `AGENTS.md` 中的业务线专属约束

### 推荐增强

1. 由 AI 根据 `workspace-config/code-sources.yaml` 确认采用新建工作空间还是存量工程渐进式转型
2. 由 AI 检查 `workspace-config/workspace-version.yaml` 中的采用方式、已应用能力和本地定制说明
3. 由 AI 创建首批 `docs/projects/<project>/` 文档入口
4. 由 AI 使用 `scripts/init_project_skills.py` 初始化首批项目 skill
5. 由 AI 在 `workspace-assets-index.md` 登记真实项目阅读路径

### 治理闭环

1. 使用 `task-plans/` 记录已确认方案、实施计划和节点状态
2. 使用 `task-completion-checklist.md` 约束完成前验证与用户确认
3. 使用 `change-history/` 记录已完成任务的复盘与资料同步
4. 通过 `CHANGELOG.md` 和 `workspace-config/workspace-version.yaml` 跟踪模板升级

## 资产分层

| 目录 | 职责 | 默认是否首读 |
| --- | --- | --- |
| `docs/` | 架构、源码说明、开发规范 | 是 |
| `skills/` | 项目场景化执行流程 | 是 |
| `workspace-config/` | 代码源与配置事实 | 按需 |
| `references/` | 数据字典、报文、环境等外围事实 | 按需 |
| `scripts/` | 初始化与校验脚本 | 按需 |
| `task-plans/` | 已确认方案与实施计划 | 否 |
| `change-history/` | 历史任务记录 | 否 |

## 推荐阅读路径

### 全局理解

1. `QUICKSTART.md`
2. `docs/README.md`
3. `skills/README.md`
4. `docs/development-specs/README.md`
5. `workspace-config/README.md`

### 单项目任务

1. `docs/projects/README.md`
2. 对应项目源码说明
3. 对应项目开发规范
4. `skills/README.md` 中的任务流程路由
5. 已落地且与当前阶段匹配的 `skills/_workflow/<workflow>/SKILL.md`
6. `skills/<project>/<scene>/SKILL.md`

### 补充事实查询

1. `references/README.md`
2. 与当前问题直接相关的具体资料

### 流程资产建设

1. `docs/development-specs/workflow-skills-design.md`
2. `docs/development-specs/template-adoption-cleanup.md`
3. `scripts/adopt_workspace.py`
4. `scripts/prepare_clean_workspace.py`
5. `skills/README.md`
6. `skills/_workflow/<workflow>/SKILL.md`
7. `skills/_templates/project/scene-template/SKILL.md`

### 版本维护与升级

1. `CHANGELOG.md`
2. `workspace-config/workspace-version.yaml`
3. `docs/development-specs/workspace-versioning.md`
4. `docs/development-specs/workspace-upgrade-model.md`
5. `docs/development-specs/workspace-upgrade-prompts.md`
6. `docs/development-specs/workspace-migration-guide.md`
7. `skills/_workflow/workspace-upgrade/SKILL.md`

### 增长运营入口

1. `docs/product-knowledge/README.md`
2. `TEAM.md`
3. `TASKS.md`
