# 工作空间资产索引

## 1. 文档目的

本文用于整理当前工作区中 `sources/` 之外的全部已落地资产，帮助后续在不直接进入源码目录的前提下，快速定位可复用的：

- 架构文档
- 接口文档
- 开发规范
- installable skills
- 数据字典与补充参考资料
- 自动化脚本

本文应只描述当前仓库中已实际存在的资产，不对缺失资产做主观补充。

## 2. 资产分层

- `docs/`：基于真实源码提炼出的高质量知识入口
- `skills/`：面向具体项目和具体场景的执行型模板资产
- `references/`：补充事实、字典、外围资料和占位示例
- `scripts/`：模板生成、初始化和维护脚本
- `change-history/`：任务级变更历史归档，默认非必读
- `task-plans/`：任务方案归档，默认非必读

## 3. 总体优先级索引

### P0：进入任何项目工作前应先读

1. `docs/overall-architecture/`
2. `docs/development-specs/README.md`
3. `skills/README.md`
4. 本文件
5. `task-completion-checklist.md`

### P1：进入单项目任务时必须先定位

1. `docs/projects/<project>/源码说明文档.md`
2. `docs/projects/<project>/开发规范文档.md`
3. `skills/<project>/<scene>/SKILL.md`
4. `skills/<project>/<scene>/references/*`
5. `skills/<project>/<scene>/examples.md`

### P2：补充查询时使用

1. `references/README.md`
2. `references/templates/`
3. `references/examples/`

### P3：维护优先级

1. `scripts/`
2. `change-history/TEMPLATE.md`
3. `task-plans/TEMPLATE.md`

## 4. 推荐阅读路径

### 场景 A：先理解工作空间怎么用

1. 读 `AGENTS.md`
2. 读本文件
3. 读 `task-completion-checklist.md`
4. 读 `skills/README.md`

### 场景 B：已定位到单项目

1. 先看 `docs/projects/<project>/`
2. 再看 `skills/<project>/<scene>/`
3. 再进入 `sources/<project>/`

### 场景 C：要扩展模板体系

1. 先看 `scripts/`
2. 再看 `docs/templates/`
3. 再看 `skills/_templates/`

## 5. 维护要求

1. 新增文档、skill、脚本或参考资料后，应同步更新本索引。
2. 若入口路径、优先级或阅读顺序失效，应优先修正本索引。
3. 本索引只做入口和优先级说明，不替代具体文档正文。
