# 快速上手

这份指南的目标是让用户不用手动复制模板、手动清理历史、手动改配置，而是把初始化交给 AI 对话完成。

## 交给 AI 初始化

在任意能操作本地文件的 AI 编程助手中，发送下面这段提示词：

```text
请帮我基于 open-teams 模板创建一个新的 AI 协作工作空间。

目标工作空间路径：<填写目标目录>
业务或项目名称：<填写名称>
项目标识 project_slug：<填写英文短标识>
真实源码路径或仓库地址：<填写本地路径或 Git 地址>
默认分支：<main/master/其他>
采用方式：<新建工作空间 / 存量工程渐进接入>

要求：
1. 先确认目标目录、源码路径、采用方式和是否允许创建目录。
2. 复制 open-teams 模板到目标工作空间。
3. 清理模板自身历史记录，避免带入 open-teams 的 task-plans 和 change-history。
4. 写入 workspace-config/code-sources.yaml。
5. 更新 workspace-config/workspace-version.yaml 的采用方式、源码策略和本地定制说明。
6. 根据我的团队情况，协助调整 AGENTS.md。
7. 运行 scripts/validate_template_layout.py 校验初始化结果。
8. 最后告诉我初始化了哪些文件、哪些仍需我确认。
```

AI 可以直接使用模板内置脚本完成复制、清理和校验：

```bash
python3 scripts/adopt_workspace.py \
  --template-root . \
  --target <目标工作空间路径> \
  --project-slug <项目标识> \
  --project-name <项目名称> \
  --source-path <真实源码路径或仓库地址> \
  --default-branch <默认分支>
```

## AI 会做什么

| 阶段 | AI 负责 | 用户只需提供 |
| --- | --- | --- |
| 复制模板 | 将 `open-teams` 复制到目标目录 | 目标工作空间路径 |
| 清理历史 | 删除模板自身 `task-plans/YYYY-*.md` 与 `change-history/open-teams/` | 是否允许清理 |
| 写入源码映射 | 生成 `workspace-config/code-sources.yaml` | 源码路径、项目名、默认分支 |
| 更新版本元信息 | 标记采用方式、源码策略和本地定制说明 | 新建或存量接入 |
| 调整协作约束 | 协助改写 `AGENTS.md` | 团队分支、验收和交付规则 |
| 运行校验 | 执行模板结构校验并报告结果 | 是否继续补项目 docs/skills |

## 初始化后继续让 AI 补齐

模板跑通后，可以继续让 AI 做推荐增强：

```text
请继续为这个工作空间补齐首个项目的 docs/projects 和 skills/<project>。

要求：
1. 先读取 workspace-assets-index.md、docs/README.md、skills/README.md。
2. 根据 workspace-config/code-sources.yaml 定位真实源码。
3. 只读取当前项目最必要的源码入口。
4. 生成项目入口文档、项目 README 和首批场景 skill。
5. 运行模板校验，并说明仍缺哪些资料。
```

## 第一次不用自己做什么

- 不用自己复制目录，让 AI 执行复制。
- 不用自己判断哪些历史记录该删，让 AI 按 [模板采用清理指南](./docs/development-specs/template-adoption-cleanup.md) 和脚本处理。
- 不用自己先读完所有 workflow skill，任务触发到对应阶段时再按需读取。
- 不用一次性补齐所有项目文档，优先让 AI 补当前最常改或最常排查的项目。
- 不用把真实源码提交进模板仓库；如果使用 `sources/`，默认只保留 `sources/README.md`。
