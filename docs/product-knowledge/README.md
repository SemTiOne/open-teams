# Product Knowledge

open-teams 的产品定位、目标用户和竞争分析。理解"为什么"和"为谁"，比理解"怎么做"更重要。

## 目录

1. [产品定位](#产品定位)
2. [目标用户](#目标用户)
3. [核心场景](#核心场景)
4. [竞品对比](#竞品对比)
5. [给你的产品知识文档](#给你的产品知识文档)

---

## 产品定位

### 一句话

**open-teams 是 AI 协作工作空间的模板和标准——让 AI 不再是个人工具，而是团队成员。**

### 核心问题

AI 编码工具的普及带来三个断裂：

| 断裂 | 现象 | 代价 |
|------|------|------|
| **上下文断裂** | 每个开发者的 AI 各学各的，会话间不继承 | 每次 AI 会话 ~15% 时间浪费在重新建立上下文 |
| **标准断裂** | 不同人的 AI 应用不同代码规范，code review 变成风格辩论 | AI 生成代码的 review 时间增加 ~40% |
| **知识断裂** | AI 协作中学到的经验和提示词留在个人聊天记录里 | 6 个月内 60-80% 的 AI 协作知识流失 |

### 解决方案

用 Git 版本化的 Markdown 工作空间，让团队的每个 AI 工具共享同一套：

- **AGENTS.md** — 项目上下文（技术栈、规范、红线）
- **MEMORY.md** — 团队长期记忆（决策、教训、偏好）
- **Skills** — 标准化工作流（code review、API review、架构审查）

**核心理念：把 AI 协作资产当代码一样管理——版本化、review、merge。**

详见 [why-open-teams.md](../en/why-open-teams.md)。

---

## 目标用户

### 画像 1：技术创始人 / Solo Developer

| 属性 | 描述 |
|------|------|
| **身份** | 独立开发者、初创 CTO、side project 作者 |
| **工具** | Cursor 主力、偶尔用 Claude |
| **痛点** | 一个人写全栈，AI 是唯一协作者。但每次开新会话都要重新解释项目背景。一周前的设计决策 AI 完全不记得。 |
| **使用方式** | Clone open-teams 作为项目模板 → AGENTS.md 里写好技术栈 → Skills 激活 code-review → MEMORY.md 记录每次关键决策 |
| **核心价值** | AI 的"长期记忆"——不需要每次重新教 AI |

### 画像 2：中小技术团队（3-30 人）

| 属性 | 描述 |
|------|------|
| **身份** | 技术团队 lead、工程经理 |
| **工具** | 团队成员混用 Cursor / Copilot / Claude Code |
| **痛点** | 每个人的 AI 标准不一样。code review 一半时间争论风格而非逻辑。高级工程师的 AI 明显比新人强。有人离职，AI 协作经验跟着走。 |
| **使用方式** | 团队共享 workspace → PR review 加入 Skill 规则 → 新人 clone 后 AI 立刻有完整上下文 → MEMORY.md 团队共建 |
| **核心价值** | 团队 AI 能力均等化——新人的 AI 和老手的 AI 用同一套标准 |

### 画像 3：大中型组织（30+ 人，多团队）

| 属性 | 描述 |
|------|------|
| **身份** | CTO、架构团队、平台工程 |
| **工具** | 多个产品团队、多种 AI 工具 |
| **痛点** | 没法统一 AI 工具，但需要统一 AI 产出质量标准。跨团队架构审查缺乏一致性。安全/合规规则难以在 AI 层面强制。 |
| **使用方式** | 组织级 AGENTS.md 模板 → 各团队 fork + 定制 → 共享 architecture-review Skill → CI 中验证模板合规 |
| **核心价值** | 工具无关的 AI 治理——不绑工具，只约束标准 |

---

## 核心场景

| 场景 | 用户诉求 | open-teams 怎么解决 | 对应 Skill |
|------|---------|-------------------|-----------|
| **新项目启动** | "怎么让 AI 从一开始就理解项目？" | init.sh 生成骨架 → AI 首次对话填充 AGENTS.md | onboarding |
| **Code Review** | "怎么让 AI review 统一标准？" | code-review Skill 提供检查清单 + 安全规则 | code-review |
| **架构决策** | "怎么确保 AI 参与架构讨论有共同基准？" | architecture-review Skill + MEMORY.md 记录决策理由 | architecture-review |
| **新人入职** | "怎么让新人第一天的 AI 和老员工一样强？" | Clone workspace → AI 自动加载全部历史上下文 | onboarding |
| **知识传承** | "有人离职，怎么不丢 AI 协作经验？" | MEMORY.md + Skills + change-history/ 全部在 Git 中 | 全体系 |
| **API 设计** | "怎么让 AI 审 API 时考虑安全/性能/向后兼容？" | api-design-review Skill + 项目自定义规则 | api-design-review |
| **工作空间升级** | "open-teams 发新版了，怎么升级我的 workspace？" | workspace-upgrade Skill 引导 diff + 合并 | workspace-upgrade |

---

## 竞品对比

### 直接对标

| 产品 | 定位 | 与 open-teams 的差异 |
|------|------|---------------------|
| **.cursorrules** | Cursor 专用规则文件 | 单文件、单工具、无版本管理、无模块化 Skill |
| **Copilot instructions** | GitHub Copilot 自定义指令 | 单工具绑定、无团队共享机制 |
| **Claude Code CLAUDE.md** | Claude Code 项目上下文 | 单文件、无 Skills 体系、无 memory 分层 |

### 相邻产品（非直接竞争）

| 产品 | 定位 | 关系 |
|------|------|------|
| **Continue.dev** | 开源 AI 编码助手（可配置 rules） | 互补——Continue 是工具，open-teams 是规则体系。Continue 用户可以直接用 open-teams 作为配置源 |
| **Aider** | AI 结对编程 CLI 工具 | 互补——Aider 是终端 AI 工具，open-teams 可以提供 conventions 文件 |
| **PR-Agent (Codium)** | 自动化 PR review | 重叠但侧重不同——PR-Agent 自动运行，open-teams 的 code-review Skill 需人工触发。PR-Agent 更自动化，open-teams 更灵活可定制 |

### 差异化优势

| 维度 | open-teams | 竞品 |
|------|-----------|------|
| **工具绑定** | 无——任何读 Markdown 的 AI 都能用 | 大部分绑定特定工具 |
| **团队共享** | Git 原生——clone 即用 | 多为个人配置文件 |
| **知识结构** | 分层存储（决策/日记/文档/规则分离） | 单一文件，无分层 |
| **Skill 体系** | 模块化 Skill（SKILL.md + rules + checklist + examples） | 无体系 |
| **版本管理** | Git——规则变更可 review、diff、回滚 | 很少版本化 |
| **中文支持** | 一等公民（AGENTS.md 中文 + README.zh-CN） | 几乎全英文 |
| **开源** | MIT | 部分是开源（Continue、Aider），部分闭源 |

---

## 给你的产品知识文档

> 以下是你可以在本目录下为**你自己的项目**创建的产品知识文档指引。

### 建议创建的文档

| 文档 | 内容 | 何时创建 |
|------|------|----------|
| 产品需求文档（PRD） | 功能描述、用户场景、验收标准 | 新功能启动前 |
| 用户画像 | 目标用户特征、痛点、使用场景 | 项目初期 |
| 功能规格说明 | 详细的功能行为定义 | 开发实施前 |
| 竞品分析 | 竞争对手功能和策略对比 | 产品定位时、周期性更新 |
| 领域知识 | 行业概念、术语、规则 | 需要统一团队认知时 |

### 命名规范

`feature-name.md` 或 `YYYY-MM-DD-topic.md`

### 文档模板

每个文档开头应包含：

```markdown
## Purpose
这个文档解决什么问题？

## Users
谁受益？（角色、画像）

## Scope
范围内 / 范围外

## Success Metrics
怎么衡量成功？
```

### 相关阅读

- [整体架构](../overall-architecture/README.md) — 系统设计层面
- [为什么选择 open-teams](../en/why-open-teams.md) — 产品理念完整论述
- [开发规范](../development-specs/) — Skills 和版本机制的设计规范