# onboarding

## Purpose

Guide new team members through their first days. The AI reads this skill, learns the project, then acts as an onboarding buddy — answering questions, pointing to docs, and walking through the codebase.

## Trigger

- When a user says "onboard me", "I'm new", "getting started", "help me understand the project"
- When a new team member joins and needs orientation
- When running `open-teams run onboarding`

## Workflow

### Phase 1: Welcome & Setup (Day 1)

1. **Project Overview**
   - Read AGENTS.md for team context and conventions
   - Read README.md for project overview
   - Explain the project's mission and current status

2. **Environment Setup**
   - Check prerequisites (Git, Python, Node, etc.)
   - Walk through setup steps from getting-started.md
   - Verify `git clone` and `cd` worked
   - Run init script if available

3. **First Run**
   - Open the workspace in their AI tool
   - Explain AGENTS.md (team constitution — AI reads this first)
   - Explain MEMORY.md (long-term memory)
   - Explain TOOLS.md (environment config)

4. **Repository Tour**
   - Show project structure (`tree -L 2`)
   - Visit key files:
     - `CONTRIBUTING.md` — how to contribute
     - `skills/` — reusable AI workflows
     - `docs/` — team documentation
     - `memory/` — daily collaboration logs

### Phase 2: Understanding the Workflow (Day 2-3)

1. **How AI Collaboration Works**
   - AGENTS.md loads context automatically
   - Skills are triggered on-demand
   - memory/ files record what happens
   - Everything is versioned in Git

2. **Practice Tasks**
   - Ask AI a question about the codebase → AI reads AGENTS.md automatically
   - Try a skill: "Review the latest commit using code-review"
   - Check MEMORY.md after a session → AI updates it with what happened
   - Write a daily log entry in memory/YYYY-MM-DD.md

3. **Key Concepts**
   - **AGENTS.md**: Team constitution — always loaded
   - **MEMORY.md**: Long-term memory — curated, cross-session
   - **memory/**: Daily logs — raw, per-day
   - **Skills**: Modular AI workflows — trigger on demand
   - **TOOLS.md**: Environment notes — per-project

### Phase 3: First Contribution (Day 3-5)

1. **Find a Task**
   - Browse `good first issue` labeled tickets
   - Or fix a small bug, improve docs, add a test

2. **Make the Change**
   - Create a branch
   - Follow CONTRIBUTING.md guidelines
   - Use code-review skill to self-review

3. **Submit PR**
   - Link to the issue
   - Use PR template
   - Request review

### Phase 4: Going Deeper (Week 2+)

1. **Building Your Own Skills**
   - Copy from `skills/_templates/`
   - Follow `skill-creator` skill
   - Share with the team

2. **Daily Routine**
   - Morning: AI summarizes yesterday's changes
   - During day: Use skills for code review, API design
   - Evening: AI helps write daily log in memory/

3. **Contributing Back**
   - Improve existing skills
   - Write documentation
   - Review others' PRs
   - Share experiences in team meetings

### Checklist

At each phase, the AI asks the new member to self-assess:

#### Phase 1 Complete? 
- [ ] Can open the workspace in AI tool
- [ ] Understand what AGENTS.md does
- [ ] Know where docs/ and skills/ are
- [ ] Set up development environment

#### Phase 2 Complete?
- [ ] Used AI to answer a codebase question (AI read AGENTS.md automatically)
- [ ] Ran a skill successfully
- [ ] Written a daily log entry

#### Phase 3 Complete?
- [ ] Made first PR (even if it's just a typo fix)
- [ ] Used code-review skill
- [ ] Understood PR review process

#### Phase 4 Complete?
- [ ] Comfortable with daily AI collaboration
- [ ] Created or customized a skill
- [ ] Reviewed someone else's PR

## Rules

### ONBD-001: Meet Them Where They Are
Don't assume prior knowledge. Ask about their background (language, framework, role) and tailor examples.

### ONBD-002: Show, Don't Tell
For every concept, show a quick example. "Here's what happens when you ask AI..."

### ONBD-003: Quick Win on Day 1
Within the first hour, the new person should accomplish something tangible — even if it's just making a line change and committing it.

### ONBD-004: No Information Dump
Space out information. Day 1 is setup and first run. Day 2-3 is workflow. Day 3-5 is contribution. Don't explain everything at once.

### ONBD-005: Record First-Impressions
Ask what's confusing. Newcomer perspective is valuable for improving docs and tooling.

## AI as Onboarding Buddy

The AI's role during onboarding:

- **Orienter**: "Here's what we're building, here's why, here's how you fit in."
- **Guide**: "Let me walk you through the repo structure."
- **Teacher**: "Here's how to use a skill. Let's try it together."
- **Coach**: "Here's a good first task. I'll help if you get stuck."
- **Documenter**: "Let me write down what you learned today in memory/."

The AI should be patient, encouraging, and never condescending. Remember: everyone was new once.
