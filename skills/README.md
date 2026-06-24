# Skills / 技能库

**English** | Skills are modular, AI-executable workflows that standardize how your team tackles common tasks. Each Skill is a self-contained directory that your AI tools can load on demand.

**中文** | Skills 是可模块化加载的 AI 工作流，用于统一团队常见任务的执行方式。每个 Skill 是独立目录，供 AI 工具按需读取。

## Skill Categories / 技能分类

| Type | Directory | Purpose |
|------|-----------|---------|
| Workflow Skills | `skills/_workflow/<name>/SKILL.md` | Cross-project process gates: solution confirmation, implementation planning, debugging, verification |
| Core Skills | `skills/<name>/SKILL.md` | Reusable team workflows: code review, API design, architecture review, onboarding |
| Project Skills | `skills/<project>/<scene>/SKILL.md` | Project-specific workflows: new features, bug fixes, refactors, performance tuning |

## Available Workflow Skills / 工作空间流程 Skill

| Skill | Path | Description |
|-------|------|-------------|
| `solution-confirmation` | [./_workflow/solution-confirmation/SKILL.md](./_workflow/solution-confirmation/SKILL.md) | Confirm scope, approach, and authorization before any implementation |
| `writing-implementation-plan` | [./_workflow/writing-implementation-plan/SKILL.md](./_workflow/writing-implementation-plan/SKILL.md) | Break confirmed solutions into verifiable, step-by-step plans |
| `systematic-debugging` | [./_workflow/systematic-debugging/SKILL.md](./_workflow/systematic-debugging/SKILL.md) | Reproduce and diagnose issues with evidence, not guesswork |
| `verification-before-completion` | [./_workflow/verification-before-completion/SKILL.md](./_workflow/verification-before-completion/SKILL.md) | Validate results before claiming completion |
| `branch-and-worktree-workflow` | [./_workflow/branch-and-worktree-workflow/SKILL.md](./_workflow/branch-and-worktree-workflow/SKILL.md) | Manage branches, worktrees, and version control discipline |
| `workspace-upgrade` | [./_workflow/workspace-upgrade/SKILL.md](./_workflow/workspace-upgrade/SKILL.md) | Plan and execute workspace template upgrades safely |

## Available Core Skills / 内置核心 Skill

| Skill | Path | Description |
|-------|------|-------------|
| `code-review` | [./code-review/SKILL.md](./code-review/SKILL.md) | Standardized code review with checklist, rules, and examples |
| `api-design-review` | [./api-design-review/SKILL.md](./api-design-review/SKILL.md) | API design consistency, versioning, and contract review |
| `architecture-review` | [./architecture-review/SKILL.md](./architecture-review/SKILL.md) | Architecture decision and system design review |
| `onboarding` | [./onboarding/SKILL.md](./onboarding/SKILL.md) | New team member onboarding workflow |

## Creating a New Skill

### Quick Start: Copy the Template

```bash
# For a new project skill
cp -r skills/_templates/project/scene-template skills/<your-project>/<your-scene>
```

### Required Structure

Every Skill must have:
```
skills/<project>/<scene>/
  SKILL.md          # Main skill file (required)
  examples.md       # Usage examples (recommended)
  references/       # Supporting documents (optional)
    README.md
```

For workflow skills (cross-project processes):
```
skills/_workflow/<name>/
  SKILL.md          # Main skill file (required)
```

### SKILL.md Required Sections

Every `SKILL.md` must include:

1. **Title** — `# skill-name`
2. **Purpose** — 1-2 sentences on what this skill accomplishes
3. **When to Use** — Trigger conditions that activate this skill
4. **Structure** — Brief description of supporting files (rules/, examples/, etc.)
5. **Quick Example** — A 3-5 line concrete usage example
6. **How to Customize** — Guidance for teams to adapt this skill

Optional but recommended:
- **Pre-requisites** — What must be known or available before using
- **Output/Exit Conditions** — What constitutes completion
- **Verification Checklist** — How to confirm the skill ran correctly

### Naming Conventions

- **Skill directories:** `kebab-case` (e.g., `code-review`, `api-design-review`)
- **Project directories:** `snake_case` or `kebab-case` matching your project conventions
- **Scene directories:** descriptive and action-oriented (e.g., `new-feature`, `bugfix`, `performance-tuning`)
- **Files:** `SKILL.md` (capitalized, required), `checklist.md`, `examples.md`, `rules/README.md`

### Best Practices

1. **Keep skills focused** — One skill = one workflow. Don't make "mega-skills" that do everything.
2. **Make examples concrete** — Show real commands, real file paths, real outputs. Abstract descriptions aren't helpful.
3. **Design for composability** — Skills should chain together. `solution-confirmation` feeds into `writing-implementation-plan`, which feeds into verification.
4. **Version with your project** — Skills live in your repo and evolve with your codebase.
5. **Review and prune** — Remove outdated skills. Keep the set small and high-quality.

## Project Skill Template

The template at `skills/_templates/project/scene-template/` provides a starting structure:
- `SKILL.md` — Template with all required sections
- `examples.md` — Example usage patterns
- `references/README.md` — Placeholder for supporting documents
