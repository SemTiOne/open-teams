# open-teams — AI 协作工作空间

> open-teams 的团队工作空间。这个 AGENTS.md 是给 open-teams 项目的协作者看的。
> 
> 用户工作空间的 AGENTS.md 由 `init.sh` 自动生成，形态完全不同：它是 AI 引导者的「脚本」，引导 AI 通过对话帮用户适配工作空间。详见 `scripts/init/templates.py`。

## 项目信息

```
                    ┌─────────────────────┐
                    │   Team Lead (我)      │
                    │   协调/审查/整合       │
                    └──────┬──────────────┘
           ┌───────────────┼───────────────────┐
           │               │                   │
    ┌──────▼──────┐ ┌─────▼──────┐    ┌───────▼───────┐
    │ Repo 工程师  │ │ 文档工程师  │    │ 内容策略师     │
    │ repo-setup  │ │ docs-writer│    │ content-cn    │
    └─────────────┘ └────────────┘    └───────────────┘
           │               │                   │
    ┌──────▼──────┐ ┌─────▼──────┐    ┌───────▼───────┐
    │ 视觉设计师   │ │ 社区建设者  │    │ 开发增强       │
    │ visual-art  │ │ community  │    │ dev-enhance   │
    └─────────────┘ └────────────┘    └───────────────┘
```

## Agent Registry

| Agent ID | 角色 | 职责 | 输出目录 |
|----------|------|------|----------|
| repo-setup | GitHub仓库工程师 | Topics、Issue/PR模板、CONTRIBUTING、Discussions配置 | deliverables/repo-setup/ |
| docs-writer | 文档工程师 | 英文README、英文文档站内容、API文档 | deliverables/docs-en/ |
| content-cn | 中文内容策略师 | 掘金/知乎首发文章、内容日历、SEO策略 | deliverables/content-cn/ |
| visual-art | 技术视觉设计师 | 架构图、Logo概念、README插图、品牌色板 | deliverables/visuals/ |
| community | 社区建设者 | 社群架构、贡献者体系、Discord设置、激励方案 | deliverables/community/ |
| dev-enhance | 开发增强 | CLI工具增强、更多workflow skill、GitHub Actions模板 | deliverables/dev-enhance/ |

## Agent Communication Protocol

- 每个 Agent 独立工作，写入指定目录
- Agent 完成后 Team Lead 审查并整合
- 跨 Agent 依赖通过 deliverable 文件传递
- 所有输出格式：Markdown + 可执行文件（如适用）

## Output Manifest

所有 Agent 交付物将合并后提交到 open-teams 仓库。
