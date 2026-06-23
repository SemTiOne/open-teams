# Changelog

All notable changes to open-teams will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Dual-language README (EN + ZH-CN)
- 4 core Skills: code-review, api-design-review, architecture-review, onboarding
- Community health files: CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, FUNDING
- Issue templates and PR template
- GitHub Discussions (6 categories with seeds)
- 10 repository Topics for discoverability
- Good First Issues (5 issues for new contributors)
- Logo and brand assets
- Dependabot configuration
- CHANGELOG.md (this file)

## [v0.2.0] — 2026-06-23

### Added
- Complete English README with architecture diagram and comparison tables
- AGENTS.md update with team collaboration rules
- init/ Python package (modular workspace initialization)
- workspace-health-check.py script
- GitHub Actions CI template
- Installation script (installation-script.sh)

### Changed
- init-command.py refactored to init/ package (ui.py, templates.py, workspace.py, cli.py)
- Documentation restructured under docs/en/
- QUICKSTART.md updated with bilingual version

## [v0.1.0] — 2026-05-15

### Added
- Core workspace structure: AGENTS.md, MEMORY.md, TOOLS.md
- Skill framework: skills/_templates/, skills/_workflow/
- Documentation framework: docs/, README.md
- Task planning: task-plans/, task-plans/TEMPLATE.md
- Change tracking: change-history/, change-history/TEMPLATE.md
- Workspace config: workspace-config/, .cursorrules
- MIT License
- Initial README in Chinese
