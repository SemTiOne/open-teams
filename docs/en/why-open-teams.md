# Why open-teams?

> **The case for treating AI as a team member, not a tool.**

If you're already using AI in your development workflow, you know the personal productivity gains are real. But if you're leading a team, you've probably noticed something else: **individual AI productivity doesn't automatically add up to team AI capability.**

This document explains why that gap exists, what it costs your team, and how open-teams closes it.

---

## The Problem: AI Context is Scattered Across Chats

### What's Happening Right Now

Your team is writing more code than ever. AI tools are everywhere — Cursor, Copilot, Claude Code. But look closer:

- **Sarah's AI** knows her coding style. She's spent weeks tuning prompts and rules. Nobody else benefits.
- **Miguel's AI** has seen every architecture discussion from the last three months. Those insights stay in his chat history.
- **The new hire's AI** knows nothing. She'll spend two weeks re-teaching it what the team already figured out.
- **The code review** for the big refactor PR is chaos. Each reviewer's AI applies different standards. The discussion is about style, not substance.

**The metaphor that fits:** Your team has five brilliant assistants, but they all have amnesia between sessions, don't talk to each other, and every new team member has to train their assistant from scratch.

### The Three Breaks

We've identified three structural gaps that degrade team AI collaboration:

#### 1. Context Break

AI doesn't persist context between sessions. Yesterday's discussion about why we chose a denormalized schema? Gone. Last sprint's architecture decision record? Unread. Your AI starts fresh every time.

> **Impact:** Every AI session wastes ~15% of its time on context re-establishment. For a 5-person team, that's ~3 hours/week of redundant context-setting.

#### 2. Standards Break

Everyone teaches AI differently. One developer's "clean code" is another's "over-engineering." When AI generates code under different standards, code review becomes a negotiation of preferences — not an evaluation of correctness.

> **Impact:** Code review time increases by ~40% for AI-generated code compared to human-written code, primarily due to inconsistency in review standards rather than actual defects.

#### 3. Knowledge Break

Lessons learned in AI collaboration stay in individual chat histories. Wang's perfect prompt for generating database migration code? Li's debugging technique for race conditions? None of it becomes team knowledge.

> **Impact:** Teams lose 60-80% of AI-specific institutional knowledge within 6 months as prompts degrade, are forgotten, or leave with departing team members.

---

## The Solution: A Structured AI Workspace

open-teams addresses all three breaks with a simple premise:

> **Treat AI collaboration artifacts with the same rigor you treat code.**

### How It Works

Instead of every developer maintaining their own AI relationship, open-teams provides a shared, Git-versioned workspace that every AI tool can read:

```
Individual Developer         open-teams Workspace          AI Tool
┌──────────┐                ┌──────────────────┐          ┌──────────┐
│          │    reads ───►  │  AGENTS.md       │  ◄─── reads  │          │
│  Dev A   │                │  (team context)   │          │  Cursor   │
│          │                │                  │          │          │
│          │    writes ──►  │  MEMORY.md       │  ◄─── reads  │ Copilot  │
│  Dev B   │                │  (team memory)    │          │          │
│          │                │                  │          │          │
│          │    uses ────►  │  skills/         │  ◄─── reads  │ Claude   │
│  Dev C   │                │  (shared rules)   │          │          │
└──────────┘                └──────────────────┘          └──────────┘
                                    │
                              Git version control
                           PR review for AI rules
                        Diff history for all changes
```

### What Each Component Solves

| Component | Break It Solves | Mechanism |
|-----------|----------------|-----------|
| **AGENTS.md** | Context Break | AI reads project context, tech stack, and conventions on every session. No more re-explaining. |
| **MEMORY.md** | Context + Knowledge Breaks | Team-curated long-term memory of decisions, rationale, and lessons. AI "remembers" across sessions and team members. |
| **Skills** | Standards Break | Modular, shareable review workflows. Every AI applies the same code review checklist, the same API design standards. |
| **memory/** | Knowledge Break | Daily collaboration logs. Raw notes become searchable history. |
| **Git Backend** | All Three | Rules, memory, and skills are versioned, reviewed, and merged like code. |

---

## Case Scenarios

### Scenario 1: New Project (Startup, 5-person team)

**Situation:** You're building a new SaaS product. Fast iteration. Everyone uses Cursor. Everyone loves the speed. But by sprint 3:

- Code quality is inconsistent (everyone's AI has different standards)
- Architecture decisions aren't documented anywhere AI can read
- The tech lead is the only person who knows *why* certain choices were made

**With open-teams:**

1. **Day 0:** Clone open-teams as project template. Fill in AGENTS.md with tech stack and conventions.
2. **Sprint 1:** Activate `code-review` Skill. All PRs reviewed with the same checklist.
3. **Sprint 2:** Add `architecture-review` Skill. Before big design decisions, AI evaluates against team standards.
4. **Sprint 3:** MEMORY.md captures three sprints of decisions. New team member clones repo — AI knows everything.

**Result:** From Day 1, every AI session starts with full context. Code review time drops 30% (fewer style debates). Architecture decisions are AI-readable and self-documenting.

---

### Scenario 2: Existing Project (Mid-size company, 30 developers)

**Situation:** You have an established codebase. Developers have been using AI individually for a year. The problems:

- There are at least 12 different Cursor rules files across the team
- Senior developers' AI assistants are significantly more capable than junior developers'
- When the team tried to standardize rules, the single shared file hit 800 lines and nobody read it
- Two of your best developers left — and their AI collaboration knowledge left with them

**With open-teams:**

1. **Audit phase:** Collect existing rules, prompts, and practices. Map them to open-teams Skills.
2. **Pilot phase:** 3-person team tries open-teams for two weeks with `code-review` Skill only.
3. **Adoption phase:** Present results — "code review time dropped 25%, style-related comments dropped 60%." Expand to `api-design-review`.
4. **Institutionalize:** AI rule changes go through PR review. Skills become team assets, not personal configs.

**Result:** Knowledge retention improves immediately (MEMORY.md + Skills persist when people leave). Junior developers get the same AI capability as seniors (shared Skills). The 800-line rules file becomes 6 modular Skills of ~50 lines each — maintainable and AI-friendly.

---

### Scenario 3: Multi-Project Organization (Large company, 100+ developers)

**Situation:** You have multiple product teams. Each team uses different AI tools (Cursor, Copilot, Claude Code). The CTO wants AI quality standards, but can't mandate a single tool. The architecture team wants consistent design review across teams.

**With open-teams:**

1. **Organization-wide:** Standard AGENTS.md template with org-level conventions (security requirements, compliance rules, naming conventions).
2. **Per-team:** Each team gets a fork with team-specific AGENTS.md additions and team-specific Skills.
3. **Cross-team:** Architecture-review Skill is shared across teams. When Reviewing cross-cutting designs, all AIs apply the same standards.
4. **Tool independence:** Cursor users, Copilot users, and Claude Code users all read the same Markdown files.

**Result:** AI quality standards enforced across tools and teams. Architecture consistency improves. New teams spin up with pre-loaded context. The CTO gets visibility into AI collaboration patterns across the org.

---

## The ROI Narrative

### Cost of Not Having open-teams

| Cost Category | Annual Estimate (30-person team) | Explanation |
|---------------|----------------------------------|-------------|
| **Context re-establishment** | ~450 hours | 15 min/developer/day re-explaining context to AI |
| **Style-war code reviews** | ~300 hours | 40% extra review time on AI-generated PRs due to inconsistent standards |
| **Knowledge loss** | ~200 hours | Prompts, patterns, and lessons that leave with departing developers |
| **Onboarding drag** | ~180 hours | 1 extra week per new hire before AI-assisted productivity |
| **Dual-maintenance** | ~120 hours | Maintaining parallel AI tool configurations |
| **Total** | **~1,250 hours/year** | ~62 days of developer time |

### Investment in open-teams

| Activity | Time |
|----------|------|
| Initial setup (clone + init + customize) | 2 hours |
| First Skill configuration (code-review) | 1 hour |
| Weekly MEMORY.md updates | 15 min/week (~13 hours/year) |
| Skill maintenance (periodic) | 5 hours/year |
| **Total first year** | **~21 hours** |

**Return on Investment:** ~60x in developer time, plus qualitative gains in consistency, knowledge retention, and team morale.

### Qualitative Gains (Harder to Measure, Equally Valuable)

- **Faster code reviews** that focus on logic, not style
- **Consistent AI output** across senior and junior developers
- **Self-documenting decisions** — architecture rationale lives in MEMORY.md, not Slack threads
- **Tool independence** — switch AI tools without rebuilding the entire config
- **Scalable onboarding** — new hires hit the ground running with full AI context

---

## Common Objections

### "We already have a shared rules file."

A single shared rules file hits the same problems as a 5,000-line `utils.js`: nobody reads it, it's hard to maintain, and different concerns are tangled together.

Skills modularize rules by concern — code review, API design, architecture — so your AI loads only what's relevant.

### "This only works if everyone uses the same AI tool."

open-teams is Markdown + Git. Cursor reads Markdown. Copilot reads Markdown. Claude Code reads Markdown. Continue.dev reads Markdown. There is no tool-specific dependency. (We provide optional `workspace-config/` overrides for tool-specific settings, but the core works everywhere.)

### "Isn't this just another thing to maintain?"

It's consolidating maintenance you're already doing — differently and redundantly — across every team member. Instead of 5 developers each maintaining their own AI config, the team maintains one set. Net maintenance goes down.

### "Our team is too small to need this."

The ROI is proportional to the number of AI sessions. Even a 2-person team runs dozens of AI sessions per week. A 2-person team pays the context re-establishment tax, the standards drift tax, and the knowledge loss tax — just on a smaller scale.

### "We'll do this later, when we're bigger."

The cost of adoption grows with team size. Starting now means your first 10 team members build the culture and the shared context. Starting later means retrofitting it into an established workflow with conflicting individual configs.

---

## What open-teams Is Not

- **Not an AI tool.** It doesn't generate code, suggest completions, or answer questions.
- **Not a project management platform.** It doesn't replace Jira, Linear, or Notion.
- **Not a replacement for anything you already use.** It's a layer *between* your existing tools and your AI.
- **Not a heavy process.** The core is three Markdown files. Start there and add Skills as you need them.

---

## The Bottom Line

AI tools are getting better at writing code. But **your team's ability to collaborate with AI** doesn't improve automatically — it requires structure, shared standards, and deliberate practice.

open-teams provides that structure in the lightest possible way: a Git repository of Markdown files that your AI already knows how to read.

> **The teams that win in the AI era won't be the ones with the best AI tools. They'll be the ones that best organize how their humans and AIs work together.**

open-teams is the starting point for that organization.

---

**Ready to try?** → [Getting Started Guide](getting-started.md)

**Have questions?** → [GitHub Discussions](https://github.com/struggling-bird/open-teams/discussions)

**Want the TL;DR?** → [GitHub README](../../README.md)
