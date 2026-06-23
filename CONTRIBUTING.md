# Contributing to open-teams 🚀

Thank you for your interest in contributing! **open-teams** is an AI collaboration workspace template that makes AI a first-class team member. We welcome contributions of all kinds — code, documentation, bug reports, feature ideas, and community building.

This guide will help you get started.

---

## 📖 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Documentation](#documentation)
- [Community](#community)
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
| 🎨 **Design** | Improve UI/UX of workspace templates | Designers |
| 🧪 **Testing** | Write tests, test edge cases, report flaky tests | QA-minded devs |
| 🌍 **Community** | Answer questions, share the project, write blog posts | Everyone |
| 🔒 **Security** | Report vulnerabilities responsibly | Security researchers |

**First time?** Look for issues labeled [`good first issue`](https://github.com/struggling-bird/open-teams/labels/good%20first%20issue) or [`help wanted`](https://github.com/struggling-bird/open-teams/labels/help%20wanted).

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

## Documentation

Documentation lives in the `docs/` directory and is just as important as code.

### What to Document

- New features or significant changes
- CLI commands and options
- Configuration files and formats
- API interfaces
- Tutorials and examples

### Style

- Write in clear, simple English
- Use code blocks for commands and snippets
- Keep it beginner-friendly — assume the reader is new to the project

---

## Community

- **Discussions**: Use [GitHub Discussions](https://github.com/struggling-bird/open-teams/discussions) for questions, ideas, and community conversations.
- **Issues**: Use [Issues](https://github.com/struggling-bird/open-teams/issues) for bugs and specific feature requests.
- **Be respectful**: We're building something together. Assume good intentions.

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
