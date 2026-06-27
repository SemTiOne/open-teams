# TEAM.md — Team Roster

## Purpose

This file defines who is on the team. Your AI reads TEAM.md to identify the current user (via `git config user.name` + `user.email`) and provide role-aware service — recommending relevant Skills, surfacing role-specific reminders, and triggering onboarding flows for newcomers.

Think of it as the team's structural memory — not a contacts list, but the foundation for AI context personalization.

## How to Use

This file is maintained by AI through conversation — not manually edited. Your AI reads this at the start of every session alongside MEMORY.md.

- Add members when someone joins the project
- Update roles when responsibilities shift
- Remove members when they leave (move to Alumni section)
- Keep role definitions current with the team's actual workflow
- Review and prune quarterly to keep context fresh

## Template (AI fills this as it learns about your team)

### Team Info

- **Team Name:** (AI will fill this in)
- **Working Language:** (AI will fill this in — e.g., zh-CN, en)
- **Last Updated:** (AI will fill this in)

### Members

| Git Email | Name | Git Account | Role | Division | Joined |
|-----------|------|-------------|------|----------|--------|
| (AI will fill this in) | (AI) | (AI) | (AI) | (AI) | (AI) |

**Column Guide:**
- **Git Email:** The email configured in `git config user.email` — used as the primary lookup key
- **Name:** Display name (Chinese or English, as preferred)
- **Git Account:** GitHub / GitLab username
- **Role:** Must match one of the roles defined in the Role Definitions table below
- **Division:** Functional area (Frontend / Backend / DevOps / QA / Design / PM / Full-stack / Other)
- **Joined:** ISO date of joining the project (YYYY-MM-DD)

### Role Definitions

| Role | Abbreviation | Responsibilities | Typical Skill Triggers |
|------|-------------|------------------|----------------------|
| Project Lead | PL | Final decision on roadmap, release approval, stakeholder communication | workspace-health-check, release-management |
| Tech Lead | TL | Architecture decisions, code review final sign-off, technical debt management | architecture-review, code-review-workflow |
| Frontend Developer | FE | UI implementation, component library, responsive design, accessibility | frontend-dev-workflow, component-design |
| Backend Developer | BE | API design, data modeling, service architecture, performance optimization | backend-dev-workflow, api-design |
| Full-stack Developer | FS | End-to-end feature delivery across frontend and backend | fullstack-workflow, integration-testing |
| QA Engineer | QA | Test strategy, automated testing, bug triage, quality metrics | test-automation, bug-triage |
| DevOps Engineer | DO | CI/CD pipelines, infrastructure, monitoring, deployment automation | ci-cd-management, infrastructure-as-code |
| Designer | DE | UI/UX design, design system, user research, prototyping | design-system, user-research |
| Technical Writer | TW | Documentation, changelogs, API references, translation coordination | documentation-workflow, translation-review |
| Community Manager | CM | Issue triage, discussion moderation, contributor onboarding, external communication | community-engagement, contributor-onboarding |
| (AI will fill — add team-specific roles above this line) | | | |

### Role-Aware Service Behaviors

When AI identifies the current user, it provides these automatic services:

| Trigger Condition | AI Behavior |
|-------------------|-------------|
| User matched as **Project Lead** | Prompt workspace-health-check; surface release-blocking items; flag un-reviewed PRs |
| User matched as **Tech Lead** | Surface architecture-debt items; offer code-review workflow; highlight breaking changes in pending PRs |
| User matched as any **registered member** | Mark role in session context; recommend role-specific Skills from Role Definitions table |
| User email **not found** in TEAM.md | Trigger onboarding flow: introduce project structure, suggest reading QUICKSTART.md, prompt to register in TEAM.md |
| `git config user.email` **not set** | Remind user to configure Git identity; provide the command `git config user.email "your@email.com"` |

### Alumni

| Git Email | Name | Git Account | Former Role | Active Period | Notes |
|-----------|------|-------------|-------------|---------------|-------|
| *(Members who have left the project — kept for historical context)* | | | | | |

### Maintenance Rules

1. **Add a member:** AI registers name, email, Git account, role, division, and join date in the Members table
2. **Change a role:** AI updates the member's Role and Division fields; adds a note in the member row or in a session diary
3. **Remove a member:** AI moves the member row from Members to Alumni, records the active period and any notes
4. **Add a role:** AI adds a new row to Role Definitions, ensuring the role name is used consistently in Members table
5. **Role conflicts:** If a member's listed role doesn't match any defined role, AI flags it and asks for clarification
6. **Duplicate detection:** AI checks for duplicate email or Git account entries before adding a new member
7. **Review cycle:** Every 90 days, AI reviews TEAM.md against recent activity and asks: "Are all members and roles up to date?"

---

*TEAM.md is part of the open-teams workspace. Paired with MEMORY.md for AI context. Maintained by AI through conversation — see AGENTS.md for governance.*