# MEMORY.md — open-teams Team Memory

## Project Identity

- **Project:** open-teams — AI 协作工作空间模板
- **Goal:** 10,000+ GitHub stars, 成为 AI 协作工作空间的行业标准
- **License:** MIT
- **Created:** 2026-05-15

## Key Decisions

### Architecture
- **Markdown + Git native** — AI 原生读 Markdown，Git 追踪一切
- **Tool-agnostic** — 兼容 Cursor、Copilot、Claude Code、通义灵码
- **Skills modular** — 每个 Skill 有 SKILL.md、rules、checklist、examples
- **Dual-language** — README.md (EN) + README.zh-CN.md (ZH)

### Project Structure
- AGENTS.md → 团队宪法（每次对话自动加载）
- MEMORY.md → 长期记忆（决策与理由）
- TOOLS.md → 环境配置（不共享上下文）
- skills/ → 模块化 AI 工作流
- memory/ → 每日协作纪要
- docs/ → 团队文档

### Community Files
- CODE_OF_CONDUCT.md with reporting email: dong.stupidboy@gmail.com
- SECURITY.md with security contact: dong.stupidboy@gmail.com
- CONTRIBUTING.md with contribution guidelines
- GitHub Discussions enabled (6 categories)
- 10 Topics for discoverability

## Lessons Learned

### 2026-06-23 — Repo Configuration
- REST API cannot create Discussions categories → Use GraphQL
- Issue Template "MISS" is GitHub cache delay — files are uploaded correctly
- Python f-strings with special chars (…) in tokens fail HTTP headers → use string concat
- Always verify after API mutations — Topics set via PATCH didn't take effect, needed PUT /topics endpoint

### Content Strategy
- Marketing files (articles, growth plan, review report) → NOT in repo, keep in open-teams-team/
- Content published externally first, then tracked via links
- Chinese developer community: Juejin → Zhihu → V2EX → CSDN
- English: Dev.to → Medium → Hacker News → Reddit

## Growth Milestones

| Date | Stars | Event |
|------|-------|-------|
| 2026-05-15 | 0 | Repository created |
| 2026-06-23 | 5 | Full repo config complete, 100% health |
| Target Q4'26 | 100 | Community traction |
| Target Q1'27 | 500 | Organic growth + content marketing |
| Target Q2'27 | 1,000+ | Platform effect |
| Target 2027 | 10,000+ | Industry standard |

## Contact

- **Owner:** struggling-bird
- **Email:** dong.stupidboy@gmail.com
- **GitHub:** https://github.com/struggling-bird/open-teams
- **Discussions:** https://github.com/struggling-bird/open-teams/discussions
