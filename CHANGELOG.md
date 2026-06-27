# Changelog

All notable changes to open-teams will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v0.4.4] — 2026-06-27

### Added
- `TEAM.md` and `TASKS.md` as team governance files (team composition, role definitions, task tracking)
- `skills/api-design-review/checklist.md`: 6-category review checklist (design, response, security, compatibility, performance, documentation)
- `skills/api-design-review/examples.md`: 3 real-world API review examples (clean/needs-work/rejected)
- `skills/architecture-review/checklist.md`: 5-category review checklist (problem, solution, NFRs, integration, implementation)
- `skills/architecture-review/examples.md`: 3 real-world architecture review examples (pass/fail/conditional)
- `skills/onboarding/SKILL.md`: 5-phase onboarding workflow with AI-driven customization prompt (template skeleton, not pre-filled)

### Changed
- `MEMORY.md`: restructured from single-line placeholder to guided template with 6 sections, per-section AI fill-in annotations, and boundary documentation distinguishing it from diary/docs/change-history
- `docs/overall-architecture/README.md`: rewritten as architecture system entry with 7-layer diagram, data flow, 6 architecture principles, 5 key design decisions, and 4-phase project growth guide
- `docs/product-knowledge/README.md`: rewritten with product positioning, 3 user personas (solo/small team/large org), 7 core scenarios mapped to Skills, 8-item competitor comparison matrix
- `docs/projects/README.md`: upgraded from directory usage guide to full project documentation entry with workspace asset relationship diagram and maintenance triggers
- `docs/development-specs/workspace-upgrade-model.md` §7: expanded capability list from 4 to 11 to match actual `workspace-version.yaml` entries
- `skills/api-design-review/SKILL.md` and `rules/README.md`: expanded rules from 5 to 14 with severity levels, added report format template
- `skills/architecture-review/SKILL.md` and `rules/README.md`: expanded rules from 4 to 10 with severity levels, added ADR template and report format
- `skills/_templates/project/scene-template/examples.md`: fixed references from non-existent skills to real core skills (code-review, api-design-review, architecture-review)
- `workspace-config/workspace-version.yaml`: synced version to 0.4.3 (match CHANGELOG)

### Fixed
- `docs/development-specs/README.md`: added missing link to `workspace-upgrade-prompts.md`
- `task-plans/2026-05-26-feature-refactor-version-records.md`: fixed `<your-project>` placeholder to `open-teams`

## [v0.4.3] — 2026-06-25

### Added
- 「首次会话初始化工作口令」：AI 检测 `MEMORY.md` 模板占位内容后自动触发引导式对话，按顺序收集业务背景、技术概况、团队情况、参考材料和工作语言，随后深度阅读源码并生成初始长期记忆
- 「契约维护原则」：明确约束工作空间契约文件（`AGENTS.md`、`MEMORY.md`、`docs/`、`skills/`）必须通过对话生成和维护，禁止手动编辑
- `QUICKSTART.md` 步骤 2 重写为对话式初始化流程描述，替代模糊的「让 AI 接管」表述

## [v0.4.2] — 2026-06-23

### Added
- `init.sh` and `init-command.py` as unified workspace initialization entrypoints
- `.github/workflows/ci.yml` for automated template layout and Python syntax validation
- Core skill registry in `skills/README.md` with bilingual descriptions

### Fixed
- `skills/README.md` workflow skill links required by `validate_template_layout.py`
- `workspace-health-check.py` usage documentation (correct script filename)
- `QUICKSTART.md` initialization instructions aligned with `init.sh`
- Removed unused Dependabot `pip` ecosystem (project uses stdlib-only Python)
- `.gitignore` extended to exclude Python `__pycache__/` artifacts

### Changed
- `skills/README.md` bilingual structure for workflow and core skills

## [v0.4.1] — 2026-06-01

### Added
- Node-level version maintenance gate: commit and push workspace changes before proceeding to the next node

## [v0.4.0] — 2026-06-01

### Added
- AI-guided workspace adoption via `QUICKSTART.md` prompts and `scripts/adopt_workspace.py`
- Template history cleanup guide and `scripts/prepare_clean_workspace.py`

## [v0.3.0] — 2026-05-29

### Added
- Implementation plan confirmation gate before coding
- Template adoption cleanup for `task-plans/` and `change-history/`
- `sources/` gitignore protection for business source code

## [v0.2.0] — 2026-05-25

### Added
- Complete English README with architecture diagram and comparison tables
- Dual-language README (EN + ZH-CN)
- 4 core Skills: code-review, api-design-review, architecture-review, onboarding
- Community health files: CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, FUNDING
- Issue templates and PR template
- Dependabot configuration for GitHub Actions
- `init/` Python package (modular workspace initialization)
- `workspace-health-check.py` script
- Logo and brand assets
- AGENTS.md update with team collaboration rules
- Documentation restructured under `docs/en/`

### Changed
- `QUICKSTART.md` updated with bilingual version

## [v0.1.0] — 2026-05-15

### Added
- Core workspace structure: AGENTS.md, MEMORY.md, TOOLS.md
- Skill framework: skills/_templates/, skills/_workflow/
- Documentation framework: docs/, README.md
- Task planning: task-plans/, task-plans/TEMPLATE.md
- Change tracking: change-history/, change-history/TEMPLATE.md
- Workspace config: workspace-config/
- Workflow skills design and validation (`scripts/validate_template_layout.py`)
- MIT License
