# Quick Start / 快速上手

## 中文

1. **克隆工作空间**
   ```bash
   git clone https://github.com/struggling-bird/open-teams.git my-project
   cd my-project
   ./init.sh
   ```

2. **首次会话 — 对话式初始化**

   在你的 AI 编码工具（Cursor / Copilot / Claude Code）中打开工作空间目录。

   AI 会自动检测 `MEMORY.md` 仍为模板状态，触发首次会话初始化引导：

   ```
   AI: "检测到本工作空间尚未初始化，请花几分钟向我介绍你的项目…"
   你: "我们做的是一个电商平台…技术栈是 TypeScript + React…"
   AI: [读取源码，分析架构，生成 MEMORY.md]
   ```

   **你只需要自然描述项目背景** — 不需要手动编辑任何契约文件。AI 会完成源码分析、记忆生成和治理配置的全套流程。

3. **开始协作** — AI 按 `AGENTS.md` 中的治理流程运行（方案确认 → 实施计划 → 节点验收 → 复盘沉淀），所有契约通过对话持续演进。

## English

1. **Initialize**
   ```bash
   git clone https://github.com/struggling-bird/open-teams.git
   cd open-teams
   ./init.sh
   ```

2. **Let AI take over** — Open your AI coding tool in the workspace directory. AI reads `AGENTS.md` automatically, understands the governance model, and guides you through adaptation to your project via conversation.

3. **Start collaborating** — AI reads `workspace-assets-index.md` for asset layout, follows `task-completion-checklist.md` for task closure.

---

> 更多文档：[GitHub Discussions](https://github.com/struggling-bird/open-teams/discussions) | [贡献指南](CONTRIBUTING.md)
