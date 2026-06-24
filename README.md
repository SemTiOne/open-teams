<p align="center">
  <img src="assets/logo.svg" alt="open-teams logo" width="120" />
</p>

<p align="center">
  <strong>English</strong> | <a href="README.zh-CN.md">中文</a>
</p>

<h1 align="center">open-teams</h1>

<p align="center">
  <strong>The AI collaboration workspace template.</strong><br>
  Turn AI from a one-shot tool into a <em>first-class team member</em> — with context, memory, and shared skills.
</p>

<p align="center">
  <a href="https://github.com/struggling-bird/open-teams/stargazers">
    <img src="https://img.shields.io/github/stars/struggling-bird/open-teams?style=flat-square&color=yellow" alt="Stars" />
  </a>
  <a href="https://github.com/struggling-bird/open-teams/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/struggling-bird/open-teams?style=flat-square&color=blue" alt="License: MIT" />
  </a>
  <a href="https://github.com/struggling-bird/open-teams/issues">
    <img src="https://img.shields.io/github/issues/struggling-bird/open-teams?style=flat-square" alt="Issues" />
  </a>
  <a href="https://github.com/struggling-bird/open-teams/pulls">
    <img src="https://img.shields.io/github/issues-pr/struggling-bird/open-teams?style=flat-square" alt="Pull Requests" />
  </a>
  <a href="https://github.com/struggling-bird/open-teams/discussions">
    <img src="https://img.shields.io/github/discussions/struggling-bird/open-teams?style=flat-square&color=purple" alt="Discussions" />
  </a>
  <img src="https://img.shields.io/badge/workspace-Markdown%20%2B%20Git-green?style=flat-square" alt="Markdown + Git" />
  <img src="https://img.shields.io/badge/AI%20tools-Cursor%20%7C%20Copilot%20%7C%20Claude--Code-blueviolet?style=flat-square" alt="Compatible with all AI coding tools" />
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#why-open-teams">Why?</a> •
  <a href="#features">Features</a> •
  <a href="#project-structure">Structure</a> •
  <a href="#comparison">Comparison</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="https://github.com/struggling-bird/open-teams/discussions">Discussions</a>
</p>

---

<!-- ANIMATED DEMO PLACEHOLDER -->
<!--
  Suggested GIF/demo content:
  1. Clone open-teams → 2. Run init.sh → 3. Open in Cursor → 4. AI reads AGENTS.md automatically
  5. Show AI using code-review skill → 6. Show MEMORY.md being updated after a session

  Tools to create: Screen Studio (macOS), OBS Studio (cross-platform), or VHS (terminal GIFs)
  Dimensions: 16:9, ~60s, keep under 10MB
-->

---

<p align="center">
  <a href="https://github.com/struggling-bird/open-teams/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/struggling-bird/open-teams"></a>
  <a href="https://github.com/struggling-bird/open-teams/actions"><img alt="CI" src="https://github.com/struggling-bird/open-teams/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/struggling-bird/open-teams/releases"><img alt="Release" src="https://img.shields.io/github/v/release/struggling-bird/open-teams"></a>
  <a href="https://github.com/struggling-bird/open-teams/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/struggling-bird/open-teams?style=social"></a>
  <a href="https://github.com/struggling-bird/open-teams/discussions"><img alt="Discussions" src="https://img.shields.io/github/discussions/struggling-bird/open-teams"></a>
</p>


## Why open-teams?

Your team loves AI coding tools. Cursor, Copilot, Claude Code — everyone's using them. Productivity is up. But after a few sprints, you notice something:

- **Context vanishes.** Every new AI chat starts from zero. Yesterday's architecture decision? Gone.
- **Standards diverge.** Five team members, five different Cursor rules. Code review is a style-war zone.
- **Knowledge leaks.** Wang's killer prompt lives in his chat history. Li's debugging trick stays in her DMs. Nobody else benefits.
- **Onboarding is manual.** Every new hire re-teaches AI from scratch. Two weeks before they're productive.

**The problem isn't the AI. It's the layer between the AI and the team.**

open-teams is that layer — a lightweight, Git-native workspace template that gives your AI:

- 🧠 **Memory** — so it remembers what happened last session
- 📋 **Shared Standards** — so everyone's AI follows the same rules
- 🔌 **Modular Skills** — reusable workflows for code review, API design, architecture review
- 📝 **Knowledge Capture** — so insights become team assets, not lost chat history

> **"Not a new AI tool. An operating system for how your team collaborates with AI."**

---

## Architecture Overview

```
┌──────────────────────────────────────────────────────────┐
│                  Your AI Coding Tool                      │
│         (Cursor / Copilot / Claude Code / ...)            │
└─────────────────────┬────────────────────────────────────┘
                      │ reads & writes
                      ▼
┌──────────────────────────────────────────────────────────┐
│                   open-teams Workspace                     │
│                                                           │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  AGENTS.md   │  │  MEMORY.md   │  │  TOOLS.md       │  │
│  │  Team        │  │  Long-term   │  │  Environment-   │  │
│  │  Constitution│  │  Memory      │  │  specific Notes │  │
│  └─────────────┘  └──────────────┘  └─────────────────┘  │
│                                                           │
│  ┌───────────────────────────────────────────────────┐   │
│  │  Skills (Modular AI Workflows)                     │   │
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
│  │  Team Docs   │  │  Daily Notes  │  │  Sprint Plans  │   │
│  └─────────────┘  └──────────────┘  └─────────────────┘  │
└──────────────────────────────────────────────────────────┘
                      │ version controlled
                      ▼
┌──────────────────────────────────────────────────────────┐
│                       Git Repository                       │
│    AI rules, memory, and skills — reviewed in PRs like code │
└──────────────────────────────────────────────────────────┘
```

**Key insight:** AI reads Markdown natively. Git tracks everything. Your AI's "brain" gets the same rigor as your codebase.

---

## Features

| Feature | Description | Impact |
|---------|-------------|--------|
| 🧠 **AGENTS.md** | Team constitution file — project context, tech stack, conventions, red lines. Read by AI on every session. | Eliminates repetitive context-setting |
| 📝 **MEMORY.md** | Long-term AI memory — key decisions, lessons learned, architecture rationale. Curated, not raw logs. | AI "remembers" across sessions |
| 🔌 **Skills** | Modular, pluggable AI workflows with rules, checklists, and examples. Trigger on-demand. | Standardize code review, API design, architecture review |
| 📋 **memory/** | Daily collaboration logs — raw records of what happened. AI helps maintain them. | Process visibility and traceability |
| 🛠️ **TOOLS.md** | Environment-specific configuration — per-project, per-team notes. Not shared between contexts. | Clean separation of global vs. local config |
| 🔄 **Git-Native** | All AI assets live in Git. PRs for rule changes. Diff for memory updates. | Version control for AI behavior |
| 🔓 **Tool-Agnostic** | Works with Cursor, Copilot, Claude Code, Continue.dev, and any AI tool that reads files. | No vendor lock-in |
| 📦 **init.sh** | Interactive setup wizard — configure team info, pick initial skills, scaffold workspace in 5 minutes. | Zero-friction adoption |

---

## Quick Start

### Prerequisites

- Git installed
- Any AI coding tool (Cursor, Copilot, Claude Code, etc.)
- 5 minutes

### Setup

```bash
# 1. Clone the template
git clone https://github.com/struggling-bird/open-teams.git
cd open-teams

# 2. Initialize your workspace (interactive wizard)
./init.sh

# 3. Open with your AI tool of choice
cursor .        # or: code ., claude .
```

**That's it.** Your AI now:

- ✅ Knows your project structure and tech stack (from `AGENTS.md`)
- ✅ Remembers past decisions (from `MEMORY.md`)
- ✅ Follows shared review standards (from `skills/`)
- ✅ Writes daily collaboration notes (in `memory/`)

### Try your first Skill

```bash
# Open your AI tool in the workspace directory, then prompt:
"Review the latest commit using the code-review skill"
```

The AI reads `skills/code-review/SKILL.md`, loads the checklist and rules, and delivers a structured review — every team member gets the same quality standard.

---

## Project Structure

```
open-teams/
├── AGENTS.md                  # Team constitution — AI reads this first
├── MEMORY.md                  # Long-term team memory — decisions & rationale
├── TOOLS.md                   # Environment notes (camera names, SSH hosts, etc.)
├── init.sh                    # Interactive workspace setup wizard
├── README.md                  # You are here
├── CHANGELOG.md               # Version history
│
├── skills/                    # 🔌 Modular AI capabilities
│   ├── code-review/           # Code quality and security review
│   │   ├── SKILL.md           #   Skill trigger + execution instructions
│   │   ├── checklist.md       #   Review checklist
│   │   ├── examples/          #   Good/bad examples
│   │   └── rules/             #   Specific rules (security, performance, etc.)
│   ├── api-design-review/     # API design review
│   ├── architecture-review/   # Architecture decision review
│   └── onboarding/            # New team member onboarding
│
├── docs/                      # 📚 Team documentation
│   ├── architecture/          # Architecture decision records
│   ├── api/                   # API documentation
│   └── en/                    # English docs (getting-started, why, etc.)
│
├── memory/                    # 📝 Daily AI collaboration logs
│   └── YYYY-MM-DD.md          # One file per day
│
├── workspace-config/          # ⚙️ Workspace configuration
│   └── .cursorrules           # Cursor-specific config (extensible)
│
├── task-plans/                # 📋 Sprint & task planning templates
│   └── TEMPLATE.md
│
├── templates/                 # 🏗️ Project bootstrap templates
│
└── change-history/            # 📖 Project-level change log
    └── TEMPLATE.md
```

---

## Comparison

### open-teams vs. Raw AI Chat vs. Traditional Project Management

| Dimension | Raw AI Chat | Shared Rules File | Notion/Confluence Docs | ✅ open-teams |
|-----------|-------------|-------------------|------------------------|----------------|
| **Context persistence** | ❌ Lost when chat ends | ⚠️ One flat file, no structure | ❌ AI can't read Notion | ✅ Multi-layer: AGENTS.md + MEMORY.md + daily logs |
| **Team alignment** | ❌ Everyone teaches AI differently | ⚠️ Single-file contention | ⚠️ Docs exist, but AI ignores them | ✅ Git-managed shared standards |
| **Knowledge capture** | ❌ Scattered in chat histories | ❌ No structured capture | ⚠️ "Result docs," not process | ✅ Daily logs + curated long-term memory |
| **Skill reusability** | ❌ Every session starts fresh | ❌ Copy-paste between projects | ❌ Docs ≠ executable workflows | ✅ Modular Skills — install and reuse |
| **Tool independence** | ❌ Tied to one chat tool | ⚠️ Usually tool-specific | ⚠️ Platform-dependent | ✅ Works with any file-reading AI |
| **Version control** | ❌ No history | ⚠️ Basic Git tracking | ❌ Notion versioning is limited | ✅ Full Git: diff, PR review, blame |
| **Onboarding speed** | ❌ Weeks of oral tradition | ⚠️ Read the rules file | ⚠️ Read the wiki | ✅ Clone → AI knows the team |
| **Review standardization** | ❌ Each reviewer has own bar | ⚠️ One checklist fits all | ⚠️ Checklist exists, manual usage | ✅ Skill-embedded review rules |

### open-teams vs. Competitors (Detailed)

| Tool | Best For | Limitation |
|------|----------|------------|
| **Copilot Rules** | Individual AI coding efficiency | Single-file, no team sharing, tool-locked |
| **Notion AI** | Non-technical knowledge management | AI doesn't natively read Notion in your IDE |
| **Cursor Rules** | Per-project cursor configuration | Not modular, not shared across tools |
| **open-teams** | **Dev team AI collaboration at scale** | Requires Git basics (not for non-tech teams) |

---

## Roadmap

| Version | Status | Highlights |
|---------|--------|------------|
| **v0.1 – v0.4** | ✅ Done | Core template, AGENTS.md governance, 4 core Skills + 6 workflow Skills, init.sh, CI/CD, template validation |
| **v0.5** | 📋 Planned | VS Code extension, CLI tool enhancements |
| **v0.6** | 📋 Planned | Web Dashboard, workspace health visualization |
| **v1.0** | 📋 Planned | Skills marketplace, team analytics, enterprise features |

> 💡 Have a feature idea? [Open a Discussion](https://github.com/struggling-bird/open-teams/discussions/categories/ideas).

---

## Contributing

open-teams is community-first. Whether you're fixing a typo or proposing a new Skill, you're welcome.

### Ways to Contribute

- **⭐ Star the repo** — it helps more people find us
- **🐛 Report bugs** — [Open an Issue](https://github.com/struggling-bird/open-teams/issues/new?template=bug_report.md)
- **💡 Suggest features** — [Start a Discussion](https://github.com/struggling-bird/open-teams/discussions)
- **🔧 Submit PRs** — See [CONTRIBUTING.md](CONTRIBUTING.md)
- **📖 Improve docs** — English + Chinese translations welcome
- **🧩 Share Skills** — Built a useful Skill? Share it with the community
- **🌍 Translate** — Help localize docs for global teams

### Good First Issues

Check out issues labeled [`good first issue`](https://github.com/struggling-bird/open-teams/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) — we'll help you through your first PR.

### Community

- 💬 [GitHub Discussions](https://github.com/struggling-bird/open-teams/discussions) — Questions, ideas, RFCs
- 📢 Follow for updates (links coming soon)

---

## Star History

<!--
  Placeholder for star-history.com chart.
  Add after repo gains traction:
  <a href="https://star-history.com/#struggling-bird/open-teams&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=struggling-bird/open-teams&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=struggling-bird/open-teams&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=struggling-bird/open-teams&type=Date" />
    </picture>
  </a>
-->

---

## License

MIT © [struggling-bird](https://github.com/struggling-bird)

---

<p align="center">
  <sub>
    Built with ❤️ by developers who believe AI should augment teams, not replace them.<br>
    <a href="https://github.com/struggling-bird/open-teams">⭐ Star us on GitHub</a>
  </sub>
</p>