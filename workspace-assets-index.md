# 工作空间资产索引模板

## 首读入口

1. `docs/README.md`
2. `skills/README.md`
3. `workspace-config/code-sources.yaml`
4. `task-completion-checklist.md`

## 初始化必做清单

1. 替换 `workspace-config/code-sources.yaml` 中的示例代码源
2. 确认真实源码是进入 `sources/` 还是仅维护外部仓库映射
3. 调整 `AGENTS.md` 中的业务线专属约束
4. 创建首批 `docs/projects/<project>/` 文档入口
5. 使用 `scripts/init_project_skills.py` 初始化首批项目 skill
6. 运行 `scripts/validate_template_layout.py` 完成模板结构校验

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
3. `workspace-config/README.md`

### 单项目任务

1. `docs/projects/README.md`
2. 对应项目源码说明
3. 对应项目开发规范
4. `skills/<project>/<scene>/SKILL.md`

### 补充事实查询

1. `references/README.md`
2. 与当前问题直接相关的具体资料
