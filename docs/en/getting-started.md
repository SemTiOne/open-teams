# Getting Started with open-teams

> **5 minutes to a structured AI workspace.** No dependencies. No configuration files. Just clone, initialize, and start collaborating with your AI.

---

## Prerequisites

| Requirement | Why |
|-------------|-----|
| **Git** (any version) | Your workspace is a Git repository |
| **An AI coding tool** | Cursor, GitHub Copilot, Claude Code, Continue.dev — any tool that reads project files |
| **A code editor** | VS Code, Cursor, or any editor with AI integration |
| **5 minutes** | That's really all it takes |

> **No Python required.** open-teams is a template of Markdown files + a bash init script. There's nothing to install or compile.

---

## Installation

### Option 1: Start a New Project (Recommended)

Use open-teams as the foundation for a brand-new project:

```bash
# 1. Clone the template
git clone https://github.com/struggling-bird/open-teams.git my-project
cd my-project

# 2. Remove the template's Git history and start fresh
rm -rf .git
git init
git add .
git commit -m "Initialize from open-teams template"

# 3. Run the interactive setup wizard
./init.sh

# 4. Open with your AI tool
cursor .   # or: code .  /  claude .
```

The setup wizard will guide you through:

- Entering your project name and description
- Describing your tech stack (language, framework, database, etc.)
- Selecting initial Skills to activate (code-review, api-design-review, etc.)
- Configuring team conventions (naming, formatting, git workflow)
- Setting up project-specific tool notes in `TOOLS.md`

### Option 2: Add to an Existing Project

Already have a project? Copy the open-teams structure in:

```bash
# 1. Clone open-teams separately
git clone https://github.com/struggling-bird/open-teams.git /tmp/open-teams

# 2. Copy the workspace structure into your project
cp /tmp/open-teams/AGENTS.md ./AGENTS.md
cp /tmp/open-teams/MEMORY.md ./MEMORY.md
cp /tmp/open-teams/TOOLS.md ./TOOLS.md
cp -r /tmp/open-teams/skills ./skills
cp -r /tmp/open-teams/memory ./memory
cp /tmp/open-teams/docs ./docs
cp /tmp/open-teams/templates ./templates

# 3. Let AI handle the rest
# Open your AI coding tool in the project directory.
# AI reads AGENTS.md, understands the governance model, and adapts
# the workspace to your project through conversation.
# You don't edit files manually — AI does it for you.

# 4. Commit
git add AGENTS.md MEMORY.md TOOLS.md skills/ memory/ docs/ templates/
git commit -m "Add open-teams AI workspace structure"
```

### Option 3: Adopt Without Full Structure

If your team isn't ready for the full template, start minimal:

```bash
# Just the three core files — they give 80% of the value
cp /tmp/open-teams/AGENTS.md ./AGENTS.md
cp /tmp/open-teams/MEMORY.md ./MEMORY.md
cp /tmp/open-teams/skills/code-review ./skills/code-review -r

# Open your AI tool in the project directory.
# AI reads AGENTS.md and adapts the workspace to your project
# through conversation — no manual editing needed.
```

---

## First Workspace Setup

Open your AI coding tool in the workspace directory. The AI reads `AGENTS.md` and starts a conversation to understand your project. **You talk, AI writes.** Quickest path: tell your AI about your project and let it handle the rest.

For reference, here's what a fully adapted workspace looks like after the AI conversation:

### AGENTS.md (after AI adaptation)

Your AI will fill AGENTS.md with information like this, based on your conversation:

```markdown
# AGENTS.md - Your Project

## Project Overview
[AI asks you and fills this in]

## Tech Stack
- Language: TypeScript
- Framework: Next.js 14
- Database: PostgreSQL (via Prisma)
- Deployment: Vercel

## Conventions
- File naming: kebab-case
- Component naming: PascalCase
- Git: trunk-based, squash merge
- Linting: ESLint + Prettier

## Red Lines
- Never commit secrets
- No direct database access from frontend
- All API routes must have input validation
```

### MEMORY.md (after AI adapts it)

Your AI maintains this as it works with you:

```markdown
# MEMORY.md

## Key Decisions
- 2026-06-01: Chose Next.js App Router over Pages Router for server components
- 2026-06-05: Decided on Prisma over raw SQL for type safety
- 2026-06-10: Selected shadcn/ui over custom components for velocity

## Architecture Rationale
- Monorepo with Turborepo: faster builds, shared types package
- Edge functions for auth middleware: lower latency for global users

## Lessons Learned
- Don't use server actions for complex mutations — use API routes
- Always paginate list endpoints, even if "we won't have that many items"
```

### 3. Select Your Skills

Browse `skills/` and keep what you need. Delete what you don't — dead Skills confuse the AI.

| Skill | When to use |
|-------|-------------|
| `code-review` | Always — standardize how AI reviews code |
| `api-design-review` | If you build APIs or make API changes |
| `architecture-review` | Before major architecture decisions |
| `onboarding` | When new team members join |

Delete a Skill: `rm -rf skills/<skill-name>`
Customize a Skill: tell your AI what rules you need — it edits `skills/<skill-name>/SKILL.md` and the rules/ inside it.

### 4. Verify It Works

Open your AI tool in the workspace directory and try:

```
"Based on AGENTS.md, what tech stack are we using?"
```

The AI should respond with the information you put in AGENTS.md. If it does — the workspace is working.

Now try a real workflow:

```
"Review the latest commit using the code-review skill."
```

---

## Using Your First Workflow Skill

Let's walk through the `code-review` Skill as an example of how Skills work.

### How Skills Work

1. **You trigger the Skill** by mentioning it in a prompt
2. **The AI reads `SKILL.md`** — which tells it the workflow, checklists, and rules
3. **The AI executes** — following the exact structure defined in the Skill
4. **Results are consistent** — every team member gets the same quality of output

### The code-review Skill in Action

```bash
# Make a commit
git add -A && git commit -m "feat: add user authentication middleware"

# Ask your AI
"Review my latest commit using the code-review skill"
```

The AI reads `skills/code-review/SKILL.md` which tells it:

- **What to check:** Security, performance, error handling, code style, tests
- **How to check:** Against the rules in `skills/code-review/rules/` and `skills/code-review/checklist.md`
- **How to report:** Structured format with severity (critical/high/medium/low), location, issue description, and fix suggestion
- **What NOT to do:** Don't review files in `.gitignore`, don't comment on style that isn't in the rules

The output looks like:

```
## Code Review: feat: add user authentication middleware

### Critical (must fix)
- **File:** src/middleware/auth.ts:42
  **Issue:** JWT secret read from environment variable without fallback validation
  **Fix:** Add early validation: `if (!process.env.JWT_SECRET) throw new Error(...)`

### High
- **File:** src/middleware/auth.ts:67
  **Issue:** No rate limiting on auth attempts
  **Fix:** Add rate-limit middleware before auth check

### Medium
- **File:** src/middleware/auth.ts:15
  **Issue:** Error message leaks internal implementation details
  **Fix:** Return generic error to client, log details server-side

### Low
- **File:** src/middleware/auth.ts:89
  **Issue:** Magic number `3600` used for token expiry
  **Fix:** Extract to named constant `TOKEN_EXPIRY_SECONDS`
```

Every team member's AI produces this same structure. No more "well, *my* AI doesn't check for that."

### Customizing a Skill

Say your team has specific security rules. Tell your AI and it will update `skills/code-review/rules/security.md`:

```markdown
# Security Review Rules

## Authentication
- JWT tokens must use RS256, not HS256
- Token expiry must be ≤ 15 minutes (with refresh)
- Never store tokens in localStorage

## Input Validation
- All user input must pass Zod schema validation
- SQL queries must use parameterized inputs (no string interpolation)

## Secrets
- No hardcoded secrets, API keys, or tokens
- Environment variables must be validated at startup

## Dependencies
- No packages with known CVEs (check `npm audit`)
- No deprecated packages (check npm deprecation notices)
```

Now every code review from every team member enforces these standards — automatically.

---

## Daily Workflow

### Start of Day

```bash
# Pull the latest team updates (including AI memory)
git pull

# Open your project with AI
cursor .
```

Your AI loads `AGENTS.md` + `MEMORY.md` + applicable Skills. Context is ready.

### During Work

Use Skills naturally in your prompts:

- `"Review this PR using the api-design-review skill"`
- `"Check the architecture of this new service against our architecture-review skill"`
- `"Help the new team member onboard using the onboarding skill"`

### End of Day / After Major Decisions

```bash
# AI updates the daily log
# (You can prompt: "Update memory/2026-06-22.md with today's key decisions")

# Review and commit
git add memory/ MEMORY.md
git commit -m "docs: update AI memory — auth middleware decision"
git push
```

---

## Common Patterns

### Pattern 1: The "Quick Context" Check

Before deep work, verify your AI has context:

```
"Summarize what you know about this project from AGENTS.md and MEMORY.md"
```

This catches config drift — if someone updated the files but your AI hasn't re-read them.

### Pattern 2: Decision Documentation

After a big decision, capture it:

```
"Update MEMORY.md with today's decision to switch from REST to GraphQL. Include: why we decided, alternatives considered, and migration plan."
```

### Pattern 3: Post-Mortem Learning

After an incident:

```
"Based on today's outage in the payment service, update skills/code-review/rules/error-handling.md to include: always validate webhook signatures before processing, always have idempotency keys on payment endpoints."
```

The lesson becomes a rule. The rule becomes automatic enforcement.

---

## Troubleshooting

### AI doesn't seem to read AGENTS.md

**Check:** Is your AI tool configured to read context from the workspace directory?
- **Cursor:** Works automatically when you open the project folder
- **Copilot Chat:** Use `@workspace` to reference workspace files
- **Claude Code:** Use `--add-dir .` or open from the project directory
- **Tip:** Explicitly tell the AI: "Read AGENTS.md in this project"

### Skills aren't triggering

**Check:** Did you mention the Skill by name? The AI looks for keywords like "code-review skill" or "use the code-review skill."
- Make sure `skills/<skill-name>/SKILL.md` exists
- Make sure the Skill directory isn't empty
- Try: "Read skills/code-review/SKILL.md and follow its instructions"

### MEMORY.md is getting too long

**Clean it up:**
- Move raw daily notes to `memory/` directory
- MEMORY.md should be curated — only decisions, lessons, and rationale
- Delete outdated decisions if they've been superseded
- Archive old entries to `memory/archive/` if you want to keep them

### Team members have different AI tools — does this still work?

**Yes.** That's the point. Cursor, Copilot, Claude Code, Continue.dev, Cursor with any LLM — they all read files. open-teams is just structured Markdown. No tool-specific configuration needed (except for `workspace-config/` overrides).

### The init.sh script doesn't work on my system

**Fallback:** init.sh is a convenience. You can manually create the structure:

```bash
mkdir -p memory workspace-config
cp templates/AGENTS.template.md AGENTS.md
cp templates/MEMORY.template.md MEMORY.md
# Edit files manually
git add -A && git commit -m "Initialize open-teams workspace"
```

---

## Next Steps

Now that you have a working workspace:

### Week 1: Establish Fundamentals
- [ ] Customize AGENTS.md with your actual tech stack and conventions
- [ ] Use the code-review Skill for one real PR review
- [ ] Start a daily `memory/` log

### Week 2: Deepen Adoption
- [ ] Add another Skill relevant to your team (api-design-review, architecture-review)
- [ ] Update MEMORY.md after your first team decision
- [ ] Share with a teammate — have them clone and try one Skill

### Week 3: Make It Stick
- [ ] Run a team retro: "What should be in our AGENTS.md that isn't?"
- [ ] Start using PR reviews for AI rule changes (treat rules like code)
- [ ] Customize a Skill's rules to match your team's actual standards

### Ongoing
- [ ] Update MEMORY.md weekly
- [ ] Review and prune outdated Skills
- [ ] Contribute useful Skills back to the open-teams community

---

## Troubleshooting

### init.sh says "git not found"

**Problem:** The initialization script fails with `git: command not found`.

**Fix:** Install git or initialize the workspace manually:

```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt install git

# Or manually create the workspace structure
mkdir -p my-workspace/.open-teams/{skills,memory}
mkdir -p my-workspace/docs/en
cp -r ~/.openclaw/workspace/skills/* my-workspace/.open-teams/skills/
```

### Skills don't appear after copying

**Problem:** You copied a Skill directory but the AI doesn't recognize it.

**Fix:** Skills must have a `SKILL.md` at minimum. Verify the structure:

```bash
ls my-workspace/.open-teams/skills/*/SKILL.md
```

Common issues:
- **Missing SKILL.md**: Create one with a frontmatter trigger and instructions
- **Wrong location**: Skills must be in `.open-teams/skills/<skill-name>/`
- **Wrong permissions**: Ensure the Skill directory and files are readable

### AI keeps forgetting team conventions

**Problem:** The AI doesn't consistently follow the rules in `AGENTS.md`.

**Fix:**

1. **Use specific, actionable rules** — instead of "write clean code", say "use type hints on all public functions, max line length 100"
2. **Keep AGENTS.md current** — stale rules get ignored by both humans and AI
3. **Reference AGENTS.md in prompts** — when starting a new session, say "review AGENTS.md first"
4. **Put high-priority rules first** — AI models weight earlier context more heavily

### Workspace health check shows warnings

**Problem:** `open-teams status` reports warnings about missing files or directories.

**Fix:** The health check compares your workspace against the template skeleton. Warnings mean optional files are missing. Only errors (red) require immediate action:

| Warning | Severity | Action |
|---------|----------|--------|
| Missing `FUNDING.yml` | Low | Optional for private repos |
| Missing `CHANGELOG.md` | Low | Create when you release |
| Missing `CODEOWNERS` | Medium | Add for multi-contributor repos |
| Missing `docs/en/` | Medium | Only needed for English docs |

### Git initialization doesn't work

**Problem:** `git init` fails inside the workspace directory.

**Fix:**

```bash
# Check if .git already exists
ls -la .git 2>/dev/null && echo "Already initialized"

# Remove and reinitialize if corrupted
rm -rf .git
git init --initial-branch=main
```

### Error: "workspace template not found"

**Problem:** The init script can't locate template files.

**Fix:** This usually happens when running from outside the open-teams directory.

```bash
# Clone the repo fresh if template is missing
git clone https://github.com/struggling-bird/open-teams.git /tmp/open-teams
cd /tmp/open-teams
./templates/init.sh
```

---

## Resources

- [Why open-teams?](why-open-teams.md) — The problem and ROI
- [GitHub Discussions](https://github.com/struggling-bird/open-teams/discussions) — Questions and community
- [Contributing Guide](../../CONTRIBUTING.md) — How to contribute
- [Repository README](../../README.md) — Full project overview
- [Documentation Index](../../README.md) — All English docs

---

> **"The best time to start structuring your AI collaboration was when your team had 2 people. The second best time is now."**
