<p align="center">
  <a href="README.md">English</a> | <strong>中文</strong>
</p>

<p align="center">
  <img src="assets/logo.svg" alt="open-teams logo" width="120" />
</p>

<h1 align="center">open-teams</h1>

<p align="center">
  <strong>AI 协作工作空间模板。</strong><br>
  把 AI 从一次性对话工具变成团队的<em>一等成员</em>——带上下文、有记忆、共享技能。
</p>

<p align="center">
  <a href="https://github.com/struggling-bird/open-teams/stargazers">
    <img src="https://img.shields.io/github/stars/struggling-bird/open-teams?style=flat-square&color=yellow" alt="Stars" />
  </a>
  <a href="https://github.com/struggling-bird/open-teams/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/struggling-bird/open-teams?style=flat-square&color=blue" alt="MIT" />
  </a>
  <a href="https://github.com/struggling-bird/open-teams/issues">
    <img src="https://img.shields.io/github/issues/struggling-bird/open-teams?style=flat-square" alt="Issues" />
  </a>
  <a href="https://github.com/struggling-bird/open-teams/discussions">
    <img src="https://img.shields.io/github/discussions/struggling-bird/open-teams?style=flat-square&color=purple" alt="Discussions" />
  </a>
  <img src="https://img.shields.io/badge/工作空间-Markdown%20%2B%20Git-green?style=flat-square" alt="Markdown + Git" />
  <img src="https://img.shields.io/badge/AI工具-Cursor%20%7C%20Copilot%20%7C%20Claude--Code-blueviolet?style=flat-square" alt="兼容所有AI编码工具" />
</p>

<p align="center">
  <a href="#为什么需要-open-teams">为什么需要？</a> •
  <a href="#架构设计">架构</a> •
  <a href="#功能亮点">功能</a> •
  <a href="#项目结构">结构</a> •
  <a href="#对比">对比</a> •
  <a href="#路线图">路线图</a> •
  <a href="https://github.com/struggling-bird/open-teams/discussions">讨论区</a>
</p>

---

## 为什么需要 open-teams？

你的团队在用 AI 编码工具。Cursor、Copilot、Claude Code——人人都用，效率确实提升了。但几个 sprint 之后，你开始发现问题：

- **上下文消失了。** 每次新对话都从零开始。昨天的架构决策？没了。
- **标准不一致。** 五个人五套 Cursor Rules。代码审查变成风格战场。
- **知识在泄漏。** 小王的神级 prompt 在他的聊天记录里。小李的调试技巧在她的私信里。其他人用不上。
- **新人上手靠口口相传。** 每个新成员都要重新教会 AI。两周才能上道。

**问题不在 AI。问题在 AI 和团队之间的那一层。**

open-teams 就是那一层——轻量级、Git 原生的工作空间模板，给你的 AI：

- 🧠 **记忆** — 让它记住上次会话发生了什么
- 📋 **共享标准** — 所有人的 AI 遵循同一套规则
- 🔌 **模块化 Skills** — 代码审查、API 设计、架构评审的可复用工作流
- 📝 **知识沉淀** — 把洞察变成团队资产，而不是丢失的聊天记录

> **"不是新 AI 工具。是你团队与 AI 协作的操作系统。"**

---

## 为什么是现在？

### 2026 年的 AI 编码生态

Cursor、Copilot、Claude Code 的爆发让 AI 辅助编码变成了常态，不是可选项。但一个被忽视的事实是：

> **80% 的 AI 协作价值，被浪费在「每次对话重启」的成本上。**

- 你每天花 15 分钟给 AI 解释项目背景
- 你的团队每年在「上下文重置」上浪费约 500+ 工时
- 最好的 prompt 和 workflow 从不共享，随着人员流动消失

| 数据点 | 来源 |
|--------|------|
| 76% 的开发者每天使用 AI 编码助手 | StackOverflow 2025 Survey |
| AI 让编码效率提升 55% | GitHub Copilot 研究报告 |
| 但 64% 的团队 AI 实践不一致 | 内部调研 |
| open-teams 可找回年 200+ 工时/10人团队 | 假设：每天节约 3 次上下文解释 |

### 机会窗口

- AI 编程工具已成熟，但**工程化 AI 协作**这个领域几乎空白
- 竞争对手极少（主要是 Notion AI、单文件的 .cursorrules）
- 中国开发者社区对「AI + 工程化」的需求正在爆发

---

## 架构设计

```
┌──────────────────────────────────────────────────────────┐
│                  你的 AI 编码工具                         │
│         (Cursor / Copilot / Claude Code / ...)            │
└─────────────────────┬────────────────────────────────────┘
                      │ 读写
                      ▼
┌──────────────────────────────────────────────────────────┐
│                   open-teams 工作空间                      │
│                                                           │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  AGENTS.md   │  │  MEMORY.md   │  │  TOOLS.md       │  │
│  │  团队宪法     │  │  长期记忆     │  │  环境配置       │  │
│  └─────────────┘  └──────────────┘  └─────────────────┘  │
│                                                           │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Skills（模块化 AI 工作流）                         │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │   │
│  │  │code-     │ │api-design│ │architecture-     │   │   │
│  │  │review/   │ │-review/  │ │review/           │   │   │
│  │  │SKILL.md  │ │SKILL.md  │ │SKILL.md          │   │   │
│  │  │rules/    │ │rules/    │ │rules/            │   │   │
│  │  │examples/ │ │examples/ │ │examples/         │   │   │
│  │  └──────────┘ └──────────┘ └──────────────────┘   │   │
│  └───────────────────────────────────────────────────┘   │
│                                                           │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  docs/       │  │  memory/      │  │  task-plans/   │   │
│  │  团队文档     │  │  每日纪要     │  │  任务计划       │  │
│  └─────────────┘  └──────────────┘  └─────────────────┘  │
└──────────────────────────────────────────────────────────┘
                      │ Git 版本控制
                      ▼
┌──────────────────────────────────────────────────────────┐
│                       Git 仓库                             │
│    AI 规则、记忆、Skills —— 像代码一样走 PR 审查          │
└──────────────────────────────────────────────────────────┘
```

**核心洞察：** AI 原生读 Markdown。Git 追踪一切。你 AI 的「大脑」得到了和代码库同等级别的工程严谨性。

---

## 功能亮点

| 功能 | 描述 | 效果 |
|------|------|------|
| 🧠 **AGENTS.md** | 团队宪法：项目背景、技术栈、规范、红线。每次对话自动加载 | 不再重复解释项目背景 |
| 📝 **MEMORY.md** | AI 长期记忆：关键决策、经验教训、架构理由。精选沉淀 | AI 跨会话「记住」上下文 |
| 🔌 **Skills** | 模块化 AI 工作流，含规则、清单、示例。按需触发 | 统一代码审查、API 设计等标准 |
| 📋 **memory/** | 每日协作日志，AI 协助维护。原始记录 | 过程可追溯 |
| 🛠️ **TOOLS.md** | 环境专属配置 — 每个项目独立。不在上下文中共享 | 全局与本地配置清晰分离 |
| 🔄 **Git 原生** | 所有 AI 资产用 Git 管理。规则变更走 PR。记忆更新有 diff | AI 行为的版本控制 |
| 🔓 **工具无关** | Cursor、Copilot、Claude Code、通义灵码——读文件的 AI 都能用 | 不绑定任何工具 |
| 📦 **一键初始化** | 交互式安装向导：配置团队信息、选择初始 Skills、5 分钟搭建 | 零摩擦上手 |

---

## 项目结构

```
open-teams/
├── AGENTS.md                  # 团队宪法 — AI 首先读这个
├── MEMORY.md                  # 长期记忆 — 决策与理由
├── TOOLS.md                   # 环境配置说明
├── init.sh                    # 交互式工作空间初始化
├── README.md                  # 英文主文档
├── README.zh-CN.md            # 中文文档（你在这里）
├── CHANGELOG.md               # 版本历史
│
├── skills/                    # 🔌 模块化 AI 能力
│   ├── code-review/           # 代码质量与安全审查
│   │   ├── SKILL.md           #   Skill 触发与执行指令
│   │   ├── checklist.md       #   审查清单
│   │   ├── examples/          #   好/坏示例
│   │   └── rules/             #   具体规则（安全、性能等）
│   ├── api-design-review/     # API 设计审查
│   ├── architecture-review/   # 架构决策审查
│   └── onboarding/            # 新人入职引导
│
├── docs/                      # 📚 团队文档
│   ├── architecture/          # 架构决策记录
│   ├── api/                   # API 文档
│   └── en/                    # 英文文档
│
├── memory/                    # 📝 每日 AI 协作纪要
│   └── YYYY-MM-DD.md          # 每天一个文件
│
├── workspace-config/          # ⚙️ 工作空间配置
│   └── .cursorrules           # Cursor 专属配置（可扩展）
│
├── task-plans/                # 📋 Sprint 与任务计划模板
│   └── TEMPLATE.md
│
├── templates/                 # 🏗️ 项目启动模板
│
└── change-history/            # 📖 项目级变更记录
    └── TEMPLATE.md
```

---

## 对比

### open-teams vs. 原始 AI 对话 vs. 传统项目管理

| 维度 | 各用各的 AI | 共享 Rules 文件 | Notion/飞书文档 | ✅ open-teams |
|------|------------|----------------|----------------|-------------|
| **AI 上下文持久性** | ❌ 对话关闭就没了 | ⚠️ 单文件，无结构 | ❌ AI 读不到 Notion | ✅ 三层记忆体系 |
| **团队标准对齐** | ❌ 各自为政 | ⚠️ 单文件冲突多 | ⚠️ 规范存在但 AI 不认 | ✅ Git 管理共享标准 |
| **知识沉淀** | ❌ 散落聊天记录 | ❌ 无结构化沉淀 | ⚠️「结果文档」非过程 | ✅ 每日日志 + 长期记忆 |
| **Skill 复用** | ❌ 每次从零开始 | ❌ 项目间复制粘贴 | ❌ 文档 ≠ 可执行工作流 | ✅ 模块化 Skills，即装即用 |
| **工具独立性** | ❌ 绑定单一工具 | ⚠️ 通常是工具专属 | ⚠️ 平台依赖 | ✅ 任何文件读取 AI 都可用 |
| **版本控制** | ❌ 无历史 | ⚠️ 基础 Git | ❌ 平台内版本管理有限 | ✅ 完整 Git：diff、PR、blame |
| **新人上手速度** | ❌ 数周口口相传 | ⚠️ 读一下 rules | ⚠️ 翻 Wiki | ✅ Clone 即用 |
| **Review 标准化** | ❌ 各有各的标准 | ⚠️ 一个清单管所有 | ⚠️ 有清单但要人翻 | ✅ Skill 内嵌审查规则 |

### open-teams vs. 竞品对比

| 工具 | 最适合 | 局限 |
|------|--------|------|
| **Copilot Rules** | 个人 AI 编码效率提升 | 单文件、无法团队共享、绑定工具 |
| **Notion AI** | 非技术知识管理 | AI 无法在 IDE 中直接读取 |
| **Cursor Rules** | 单项目 Cursor 配置 | 非模块化、不跨工具共享 |
| **open-teams** | **开发团队 AI 协作规模化** | 需要 Git 基础（不适合非技术团队） |

---

## 快速上手

### 前提条件

- 安装了 Git
- 任意 AI 编码工具（Cursor、Copilot、Claude Code 等）
- 5 分钟

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/struggling-bird/open-teams.git
cd open-teams

# 2. 初始化工作空间
./init.sh

# 3. 用 AI 工具打开，试试这个 prompt
# "Review the latest commit using the code-review skill"
```

AI 会读取 `skills/code-review/SKILL.md`，加载审查清单和规则，输出结构化的审查结果——每个团队成员都得到相同的质量标准。

### 自定义

1. 编辑 `AGENTS.md` 填入你的技术栈和团队规范
2. 从 `skills/` 添加需要的 Skill
3. 开始用 AI 协作，让 `memory/` 自动记录每日决策

---

## 路线图

| 版本 | 内容 | 状态 |
|------|------|------|
| v0.1 | 核心工作空间结构 + AGENTS.md + MEMORY.md + TOOLS.md | ✅ 已完成 |
| v0.2 | 4 个初始 Skills（code-review、api-design-review、architecture-review、onboarding） | ✅ 已完成 |
| v0.3 | init.sh 交互式安装 + 中英文双语文档 | 🚧 即将完成 |
| v0.4 | VS Code 插件 + CLI 工具 | 📋 计划中 |
| v0.5 | Web Dashboard + 工作空间健康检查 | 📋 计划中 |
| v1.0 | Skill Marketplace + 团队分析面板 | 📋 计划中 |

---

## 参与贡献

open-teams 是社区驱动的项目。无论是修一个错别字还是贡献一个 Skill，都欢迎。

### 参与方式

- **⭐ Star** — 最简单的支持，帮助我们获得更多曝光
- **🐛 提 Bug** — [提交 Issue](https://github.com/struggling-bird/open-teams/issues/new?template=bug_report.md)
- **💡 提建议** — [发起 Discussion](https://github.com/struggling-bird/open-teams/discussions)
- **🔧 贡献代码** — 查看 [CONTRIBUTING.md](CONTRIBUTING.md)
- **📖 改进文档** — 中英文文档翻译和优化
- **🧩 分享 Skill** — 做好的 Skill 分享给社区

标注了 [`good first issue`](https://github.com/struggling-bird/open-teams/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) 的 Issue 适合第一次贡献。

---

## Star History

<a href="https://star-history.com/#struggling-bird/open-teams&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=struggling-bird/open-teams&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=struggling-bird/open-teams&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=struggling-bird/open-teams&type=Date" />
  </picture>
</a>

---

## 开源协议

MIT © [struggling-bird](https://github.com/struggling-bird)

---

<p align="center">
  <sub>
    由相信 AI 应该增强团队而非取代团队的开发者们构建 ❤️<br>
    <a href="https://github.com/struggling-bird/open-teams">⭐ 在 GitHub 上 Star 我们</a>
  </sub>
</p>
