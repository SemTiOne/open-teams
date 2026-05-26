# 工作空间资产索引模板

## 首读入口

1. `CHANGELOG.md`
2. `docs/README.md`
3. `skills/README.md`
4. `workspace-config/code-sources.yaml`
5. `task-completion-checklist.md`

## 初始化必做清单

1. 替换 `workspace-config/code-sources.yaml` 中的示例代码源
2. 确认采用新建工作空间还是存量工程渐进式转型，并决定真实源码进入 `sources/` 还是仅维护外部仓库映射
3. 调整 `workspace-config/workspace-version.yaml` 中的采用方式、已应用能力和本地定制说明
4. 调整 `AGENTS.md` 中的业务线专属约束
5. 创建首批 `docs/projects/<project>/` 文档入口
6. 使用 `scripts/init_project_skills.py` 初始化首批项目 skill
7. 运行 `scripts/validate_template_layout.py` 完成模板结构校验

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

1. `docs/README.md`
2. `skills/README.md`
3. `docs/development-specs/README.md`
4. `workspace-config/README.md`

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
2. `skills/README.md`
3. `skills/_workflow/<workflow>/SKILL.md`
4. `skills/_templates/project/scene-template/SKILL.md`

### 版本维护与升级

1. `CHANGELOG.md`
2. `workspace-config/workspace-version.yaml`
3. `docs/development-specs/workspace-versioning.md`
4. `docs/development-specs/workspace-upgrade-model.md`
5. `docs/development-specs/workspace-upgrade-prompts.md`
6. `skills/_workflow/workspace-upgrade/SKILL.md`
