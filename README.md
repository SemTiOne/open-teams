# Best Practice Workspace Template

本目录是一个可跨产品、跨业务复用的工作空间模板库。

目标：

- 提供统一的非源码资产组织方式
- 提供可复用的文档模板、skill 模板与执行约束
- 提供面向真实项目落地的资产化工作流骨架

## 适用场景

- 需要为新产品线或新业务线快速搭建 AI 协作工作空间
- 需要建立“docs + skills + references + scripts” 的非源码资产体系
- 需要把项目研发经验沉淀为可持续复用的模板库

## 建议阅读顺序

1. `AGENTS.md`
2. `workspace-assets-index.md`
3. `task-completion-checklist.md`
4. `skills/README.md`

## 目录说明

- `docs/`：通用文档模板与项目文档模板
- `skills/`：项目化、场景化 skill 模板
- `references/`：模板参考资料和占位示例
- `scripts/`：模板初始化脚本
- `change-history/`：任务级历史记录模板
- `task-plans/`：方案记录模板

## 快速开始

1. 复制本目录作为新工作空间基础骨架。
2. 先阅读 `AGENTS.md`、`workspace-assets-index.md` 和 `task-completion-checklist.md`。
3. 按真实项目情况补齐：
   - `docs/projects/<project>/`
   - `skills/<project>/<scene>/`
   - `references/` 中的真实外围资料
4. 使用 `scripts/init_project_skills.py` 初始化某个项目的 scene skill 目录。
5. 以 `example-project/` 为参考，替换所有占位符为真实项目事实。

## 初始化示例

为一个前端项目 `sample-web` 初始化 skill 目录：

```bash
python3 scripts/init_project_skills.py sample-web --project-type frontend
```

为一个后端项目 `sample-api` 初始化 skill 目录：

```bash
python3 scripts/init_project_skills.py sample-api --project-type backend
```

## 使用原则

- 模板只提供结构、方法和占位内容，不应直接承载真实业务事实。
- 所有项目事实、接口边界、运行约束、环境信息都必须基于目标业务的真实代码和真实资料填写。
- 若模板与实际项目现状冲突，应优先以实际项目为准，再回补修正文档和 skill。
