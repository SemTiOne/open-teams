# Contributing to open-teams 🚀

Thank you for your interest in contributing! **open-teams** is an AI collaboration workspace template that makes AI a first-class team member. We welcome contributions of all kinds — code, documentation, bug reports, feature ideas, and community building.

This guide will help you get started.

---

## 📖 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Non-Code Contributions](#non-code-contributions)
  - [Documentation](#documentation)
  - [Translations](#translations)
  - [Design](#design)
  - [Community Support](#community-support)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [License](#license)

---

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## Ways to Contribute

| Type | Description | Good for |
|------|-------------|----------|
| 🐛 **Bug reports** | File clear, reproducible bug reports | Everyone |
| 💡 **Feature requests** | Propose new features with use cases | Everyone |
| 📝 **Documentation** | Fix typos, improve docs, write tutorials | First-time contributors |
| 💻 **Code** | Fix bugs, implement features, improve tests | Developers |
| 🎨 **Design** | Improve visual assets, diagrams, workspace templates | Designers |
| 🌍 **Translations** | Translate docs into other languages | Bilingual contributors |
| 🤝 **Community** | Answer questions, share the project, write blog posts | Everyone |
| 🧪 **Testing** | Write tests, test edge cases, report flaky tests | QA-minded devs |
| 🔒 **Security** | Report vulnerabilities responsibly | Security researchers |

**First time?** Look for issues labeled [`good first issue`](https://github.com/struggling-bird/open-teams/labels/good%20first%20issue) or [`help wanted`](https://github.com/struggling-bird/open-teams/labels/help%20wanted).

**Not a developer?** The sections below are written specifically for you. No code required.

---

## Non-Code Contributions

open-teams improves just as much from good docs, accurate translations, clear diagrams, and an active community as it does from code. This section explains exactly how to contribute each type.

### Documentation

Documentation lives alongside the code and is treated as a first-class part of the project. You do not need to be a developer to improve it, you just need to read carefully and write clearly.

#### What counts as a documentation contribution

- **Fixing errors**: typos, broken links, outdated commands, wrong file paths
- **Improving clarity**: rewriting confusing explanations, adding missing context, shortening verbose sections
- **Adding examples**: real-world usage scenarios that show how a feature works end-to-end
- **Writing guides**: tutorials, how-tos, or walkthroughs for specific use cases
- **Updating stale content**: docs that no longer match what the project actually does

#### Where docs live

| File/Directory | Purpose |
|---|---|
| `README.md` | Project overview, quick start, feature summary |
| `CONTRIBUTING.md` | This file — contributor guidelines |
| `QUICKSTART.md` | Fast onboarding guide for new users |
| `AGENTS.md` | Instructions for AI agents working in the workspace |
| `TOOLS.md` | Reference for available tools and scripts |
| `docs/` | Extended documentation (guides, references) |

#### How to submit a documentation fix

1. **Small fixes** (typos, broken links): you can edit directly in the GitHub UI, click the pencil icon on any file.
2. **Larger changes**: fork the repo, make your edits, and open a PR (see [Pull Request Process](#pull-request-process)).
3. Reference the relevant issue if one exists (e.g., `Fixes #42`).

#### Documentation style guide

- Write in plain English. Avoid jargon unless you define it.
- Use second person ("you") when addressing the reader.
- Use present tense: "The command runs..." not "The command will run..."
- Keep sentences short. One idea per sentence.
- Use code blocks for all commands, file paths, and code snippets, even short ones.
- Prefer concrete examples over abstract descriptions.

---

### Translations

open-teams is used by people across different languages and regions. Translating the docs makes the project accessible to a wider audience. The project already maintains a Chinese translation (`README.zh-CN.md`) and welcomes additional languages.

#### What can be translated

| File | Priority | Notes |
|---|---|---|
| `README.md` | High | Main entry point for new users |
| `QUICKSTART.md` | High | Critical for fast onboarding |
| `CONTRIBUTING.md` | Medium | Helps non-English contributors participate |
| `AGENTS.md` | Medium | Important for AI tool configuration |
| `TOOLS.md` | Low | Reference material, lower urgency |

#### File naming convention

Follow the pattern already used in the project:

```
README.md           → README.{lang}.md
QUICKSTART.md       → QUICKSTART.{lang}.md
CONTRIBUTING.md     → CONTRIBUTING.{lang}.md
```

Use [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) two-letter language codes. For regional variants, append the region: `pt-BR` (Brazilian Portuguese), `zh-TW` (Traditional Chinese).

**Examples:**
```
README.id.md        ← Indonesian
README.ja.md        ← Japanese
README.pt-BR.md     ← Brazilian Portuguese
README.de.md        ← German
README.fr.md        ← French
```

#### How to submit a translation

1. **Check open issues and PRs first**, someone may already be working on the same language. Search for your language name or code in [Issues](https://github.com/struggling-bird/open-teams/issues) and [Pull Requests](https://github.com/struggling-bird/open-teams/pulls).

2. **Open an issue** before starting a large translation. Title it `[Translation] Add {Language} translation` and mention which files you plan to translate. This prevents duplicate work.

3. **Fork the repo** and create a branch:
   ```bash
   git checkout -b translation/add-indonesian
   ```

4. **Translate the file(s)**. A few guidelines:
   - Keep all Markdown formatting intact (headers, code blocks, links, badges)
   - Do not translate code blocks, commands, file paths, or variable names
   - Do not translate proper nouns like `open-teams`, `AGENTS.md`, `Cursor`, `Copilot`
   - Translate UI text and prose only
   - When in doubt about a technical term, keep the English term and add a brief explanation in parentheses

5. **Update the language switcher** in `README.md` if your translation adds a new language. The existing pattern is at the top of the file:
   ```html
   <p align="center">
     <strong>English</strong> | <a href="README.zh-CN.md">中文</a>
   </p>
   ```
   Add your language to this list.

6. **Submit a PR** (see [Pull Request Process](#pull-request-process)). In the PR description, note:
   - Which files you translated
   - Your language and locale
   - Whether this is a full or partial translation

#### Keeping translations in sync

When the English source changes, translations may fall out of date. If you notice a translation that is outdated compared to the English version, open an issue tagged `translation` or submit a PR with the updated sections. You do not need to be the original translator to update one.

---

### Design

Design contributions improve how the project looks and how clearly it communicates. This includes visual assets, diagrams, workspace layout improvements, and UX feedback on the template structure.

#### Types of design contributions

**Visual assets**
- Logo refinements (current logo: `assets/logo.svg`)
- Badge designs for the README
- Social preview images for GitHub/social sharing
- Animated demos or screen recordings showing how the workspace works

**Diagrams and illustrations**
- Architecture diagrams explaining how open-teams workspace components connect
- Flowcharts for the AI collaboration workflow
- Annotated screenshots for the quickstart guide

**Workspace template design**
- Improvements to the structure or formatting of core files (`AGENTS.md`, `MEMORY.md`, `TOOLS.md`)
- Better organization of the `skills/` or `workspace-config/` directories
- Clearer visual separation within Markdown files using tables, callout blocks, or diagrams

**UX feedback**
- If you tried setting up the workspace and found a step confusing, that is a valid design contribution. Open an issue describing the friction point and what would have made it clearer.

#### Design file formats

| Format | When to use |
|---|---|
| SVG | Logos, icons, diagrams — preferred for anything that needs to scale |
| PNG | Screenshots, raster illustrations (export at 2x for retina) |
| Mermaid (`.md` embedded) | Diagrams inside Markdown files — keeps them version-controllable |
| GIF/WebP | Animated demos in README |

#### How to submit a design contribution

1. **Open an issue first** for anything beyond small asset tweaks. Describe what you want to improve and why, and share a rough concept if you have one. Design is subjective, getting early feedback saves iteration time.
2. For asset additions/replacements, put new files in `assets/` and reference them from the relevant Markdown file.
3. For diagram proposals using Mermaid, you can embed them directly in a GitHub issue comment to get feedback before submitting a PR.
4. Submit a PR with a clear description of what changed and why, including before/after screenshots where relevant.

---

### Community Support

Community contributors help the project grow by supporting users, spreading the word, and keeping discussions healthy. This is one of the highest-leverage ways to contribute — a helpful answer in a Discussion can benefit dozens of future readers.

#### Answering questions in GitHub Discussions

The [Discussions board](https://github.com/struggling-bird/open-teams/discussions) is where users ask for help, share how they use the project, and propose ideas.

- Check the Discussions board periodically for unanswered questions
- Share what you know, you do not have to know everything to be helpful
- If you are not sure of an answer, say so and suggest where to look
- Link to relevant docs, issues, or PRs when they exist
- Mark answers as helpful when a discussion gets resolved (if you are the OP)

#### Issue triage

Triaging issues means reviewing new issues and helping maintainers understand them faster.

Things you can do without special permissions:
- Reproduce a reported bug and confirm or deny it
- Ask for missing information on bug reports (OS, version, reproduction steps)
- Add `👍` reactions to issues you can also reproduce
- Link duplicate issues together in a comment
- Search for and reference existing related issues or PRs

#### Sharing the project

The simplest community contribution: star the repo and tell someone who might find it useful.

More impactful:
- Write a blog post or dev.to article about how you use open-teams in your workflow
- Share the project in relevant communities (Discord servers, Slack workspaces, subreddits, forums)
- Mention it in conference talks or meetup presentations
- Record a short demo video or tutorial

When sharing, please be accurate about what the project does and does not do. Avoid overclaiming.

#### Writing tutorials and case studies

If you have built something interesting on top of open-teams, or found a particularly effective way to configure the workspace for a specific team type, consider writing it up and submitting it to the `docs/` directory as a tutorial or case study.

A useful tutorial includes:
- The specific problem or use case
- Step-by-step setup instructions
- What the result looks like (screenshots, file listings)
- Any gotchas or tradeoffs you encountered

Open an issue or [start a Discussion](https://github.com/struggling-bird/open-teams/discussions) to propose a tutorial before writing it, maintainers can give early feedback and ensure it fits the docs structure.

---

## Development Setup

### Prerequisites

- **Python 3.10+** (we target 3.10 for broad compatibility)
- **Git**
- **pip** or **uv** (package manager)

### Getting Started

```bash
# 1. Fork and clone the repo
git clone https://github.com/YOUR_USERNAME/open-teams.git
cd open-teams

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -e ".[dev]"

# 4. Verify your setup
python -c "import open_teams; print('✅ Ready!')"
```

### Running Tests

```bash
# Run the full test suite
pytest

# Run with coverage
pytest --cov=open_teams --cov-report=term-missing

# Run specific tests
pytest tests/test_workspace.py -v
```

---

## Code Style

We use automated tooling to keep the codebase consistent. Before submitting a PR:

### Python Style

- **[PEP 8](https://peps.python.org/pep-0008/)** — the Python style guide
- **[Black](https://black.readthedocs.io/)** — automatic code formatter (line length: 88)
- **[isort](https://pycqa.github.io/isort/)** — import sorting
- **[Ruff](https://docs.astral.sh/ruff/)** — fast linter (replaces flake8 + pylint)
- **[mypy](https://mypy-lang.org/)** — static type checking (where annotated)

### Quick Format

```bash
# Format and lint your code
black .
isort .
ruff check .
mypy open_teams/
```

### Docstrings

- Use **[Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)**
- Every public function, class, and module should have a docstring
- Document parameters, return values, and exceptions

```python
def initialize_workspace(path: Path, *, template: str = "default") -> Workspace:
    """Create a new open-teams workspace from a template.

    Args:
        path: Directory where the workspace will be created.
        template: Name of the template to use. Options: "default", "minimal".

    Returns:
        A configured Workspace instance.

    Raises:
        FileExistsError: If the target path already exists.
        TemplateNotFoundError: If the template name is not recognized.
    """
    ...
```

### Commit Messages

- Use imperative mood: `Add` not `Added`, `Fix` not `Fixed`
- First line: 72 characters max, capitalize, no period
- Body (optional): explain **what** and **why**, not the "how"
- Reference issues: `Fixes #123` or `Related to #456`

```
Add workspace validation CLI command

Introduces `open-teams validate` that checks workspace structure
and reports missing or malformed assets. Includes JSON output
format for CI pipelines.

Fixes #42
```

---

## Pull Request Process

1. **Fork** the repository and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write code** following our [Code Style](#code-style) conventions.

3. **Add tests** for new functionality. We aim for >80% coverage on new code.

4. **Update documentation** if your change affects user-facing behavior.

5. **Run the full test suite and linters** to catch issues early:
   ```bash
   pytest && ruff check . && mypy open_teams/
   ```

6. **Submit a Pull Request** using our [PR template](PULL_REQUEST_TEMPLATE.md).
   - Fill out all relevant sections
   - Reference any related issues
   - Be responsive to review feedback

7. **CI checks** must pass. We run linting, type checking, and tests automatically.

8. **Code review** — a maintainer will review your PR. Expect feedback and discussion.
   - Small PRs get reviewed faster. Keep them focused.
   - If your PR is large, consider opening an issue first to discuss the approach.

9. **Merge!** 🎉 Once approved and CI is green, a maintainer will merge your PR.

### Review Expectations

| PR Size | Typical Review Time | Tips |
|---------|-------------------|------|
| < 100 lines | 1–3 days | Small fixes, typos, simple features |
| 100–500 lines | 3–7 days | Medium features, refactors |
| 500+ lines | 1–2 weeks | Please discuss in an issue first! |

---

## Issue Guidelines

### Bug Reports 🐛

Use the [Bug Report template](https://github.com/struggling-bird/open-teams/issues/new?template=bug_report.md) and include:

- Clear, minimal reproduction steps
- Expected vs. actual behavior
- Environment details (OS, Python version, etc.)
- Error messages and logs

### Feature Requests ✨

Use the [Feature Request template](https://github.com/struggling-bird/open-teams/issues/new?template=feature_request.md) and include:

- The problem you're trying to solve
- Your proposed solution
- Alternatives you've considered
- Who would benefit

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE). You retain copyright of your contributions but grant the project a license to use and distribute them under the same terms.

**No CLA (Contributor License Agreement) is required.** We use the MIT license which is permissive and straightforward. If this changes in the future, it will be announced prominently.

---

## ❓ Questions?

If you have questions that aren't covered here:

- Open a [GitHub Discussion](https://github.com/struggling-bird/open-teams/discussions)
- Comment on a relevant issue
- Reach out to the maintainers

**Happy contributing!** 🚀