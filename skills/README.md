# 项目场景化 Skills 模板

本目录用于沉淀可复用的 installable skill 模板。

使用规则：

- 目录分组统一为 `skills/<project-slug>/<scene>/`。
- 模板资产统一放在 `skills/_templates/` 下，供新项目复制或脚本生成。
- 每个具体 scene skill 目录至少包含 `SKILL.md`、`references/` 和 `examples.md`。
- 所有模板内容都应以“真实代码 + 当前文档 + 当前任务事实”为前提，不鼓励脱离事实猜测。

## 模板分组

- `skills/_templates/backend-project/`：后端或服务类项目模板
- `skills/_templates/frontend-project/`：前端项目模板
- `skills/_templates/common-scenes/`：跨项目通用场景模板

## 推荐场景

- `new-feature-dev`
- `bugfix`
- `security-fix`
- `api-refactor`
- `feature-refactor`
- `performance-tuning`

## 使用方式

1. 先复制一个项目模板目录。
2. 再按项目类型选择需要的场景模板。
3. 将占位符替换为真实项目名、真实路径、真实命令和真实验证方式。
4. 补充该项目的 `references/` 与 `examples.md`。
