# Security Policy 🔒

## Supported Versions

We release security patches for the latest stable version and, where feasible,
the previous minor release.

| Version | Supported          |
| ------- | ------------------ |
| latest (main)   | :white_check_mark: |
| previous minor  | :white_check_mark: |
| < previous minor | :x:                |

## Reporting a Vulnerability

**Do not open a public issue for security vulnerabilities.**

We take security seriously. If you discover a security vulnerability in 
open-teams, please report it privately so we can address it before public 
disclosure.

### Reporting Process

📧 **Email:** dong.stupidboy@gmail.com

Please include as much detail as possible:

- A clear description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)
- Your contact information

### What to Expect

| Timeline | Action |
|----------|--------|
| **0–48 hours** | We will acknowledge your report and begin investigation |
| **48 hours–7 days** | We will triage, validate, and determine severity |
| **7–90 days** | We will develop, test, and release a fix (timeline depends on complexity) |
| **After fix** | We will publish a security advisory and credit you (unless you prefer anonymity) |

### Our Commitment

- **Confidentiality**: Your report will be handled confidentially and shared only with maintainers who need to address the issue.
- **No retaliation**: We will never pursue legal action against researchers who report vulnerabilities responsibly.
- **Credit**: With your permission, we will publicly credit you in the advisory and release notes.
- **Transparency**: After the fix is released, we will publish a detailed advisory via [GitHub Security Advisories](https://github.com/struggling-bird/open-teams/security/advisories).

## Scope

Security reports are welcome for:

- The open-teams core library and CLI
- Workspace template generation
- File system operations and path handling
- Input validation and sanitization
- Dependency vulnerabilities with real-world exploitability

### Out of Scope

- Theoretical vulnerabilities without a proof of concept
- Vulnerabilities in user-created workspace content (these are the user's responsibility)
- Social engineering attacks
- Physical security
- Third-party services (GitHub, PyPI, etc.)

## Security Best Practices for Users

When using open-teams in your projects:

1. **Review generated workspace content** before committing sensitive data
2. **Keep dependencies updated**: Run `pip list --outdated` regularly
3. **Use virtual environments**: Always isolate project dependencies
4. **Audit `.env` files**: Never commit secrets or API keys
5. **Pin dependency versions** in production environments

## Recognition

We maintain a [Security Hall of Fame](SECURITY_HOF.md) (optional) to recognize
researchers who have responsibly disclosed vulnerabilities.

---

> 🙏 Thank you for helping keep open-teams and its users safe!
