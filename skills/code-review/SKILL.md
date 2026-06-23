# code-review

## Purpose

Standardized code review workflow that ensures consistent quality, security, and style across the team. Every team member's AI follows the same review checklist.

## Trigger

- When a user asks to "review this code", "code review", "review PR", "check this code"
- When a PR is opened and the reviewer wants AI-assisted review
- When running `open-teams run code-review`

## Workflow

### 1. Context Gathering (auto)
- Read the changed files / target code
- Read AGENTS.md for team standards and conventions
- Read related MEMORY.md entries for known gotchas

### 2. Review Dimensions

For each file, review against these dimensions:

#### 🔒 Security
- [ ] No hardcoded secrets, tokens, or passwords
- [ ] Input validation on all user/external inputs
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention in HTML/JS output
- [ ] Authentication/authorization checks on sensitive operations
- [ ] No sensitive data in logs or error messages
- [ ] Dependency versions are pinned and audited

#### ⚡ Performance
- [ ] No N+1 queries
- [ ] Efficient data structures (correct Big-O for the use case)
- [ ] Appropriate caching strategy
- [ ] No unnecessary allocations or copies
- [ ] Database queries are indexed properly
- [ ] Lazy loading where appropriate

#### 🏗️ Architecture
- [ ] Follows the project's architectural patterns
- [ ] Single Responsibility Principle
- [ ] Proper separation of concerns
- [ ] No circular dependencies
- [ ] Interfaces are well-defined
- [ ] Error handling is consistent and comprehensive

#### 📝 Code Quality
- [ ] Follows the project's style guide (AGENTS.md)
- [ ] Meaningful variable and function names
- [ ] Functions are small and focused (< 50 lines ideally)
- [ ] No commented-out code
- [ ] Docstrings for public functions/classes
- [ ] Complex logic has explanatory comments
- [ ] No magic numbers — use named constants

#### 🧪 Testing
- [ ] New code has corresponding tests
- [ ] Edge cases are covered
- [ ] Error paths are tested
- [ ] Tests are readable and maintainable
- [ ] No flaky tests (time-dependent, order-dependent)

#### 📦 Dependencies
- [ ] New dependencies are justified
- [ ] No duplicate dependencies
- [ ] Dependencies are the latest stable versions
- [ ] License compatibility with the project

### 3. Report Generation

Generate a structured review report:

```markdown
# Code Review: [file/branch/PR]

**Reviewer:** AI (code-review skill)
**Date:** [date]
**Files Reviewed:** [count]

## Summary
[One-paragraph summary of overall quality]

## Critical Issues (must fix)
- [Issue] — [File:Line] — [Why it matters] — [Suggested fix]

## Warnings (should fix)
- [Issue] — [File:Line] — [Why it matters] — [Suggested fix]

## Suggestions (nice to have)
- [Suggestion] — [File:Line] — [Why it's better]

## Security Scan
[Any security findings, even if low severity]

## Performance Notes
[Performance concerns or optimizations]

## Positive Findings
[Things done well — give credit where it's due]

## Overall Assessment
[✅ Approved / ⚠️ Changes Requested / ❌ Rejected]
```

### 4. Verification
- [ ] All findings reference specific file:line
- [ ] Each finding has a suggested fix
- [ ] Severity classification is justified
- [ ] No false positives (check against team conventions)

## Rules

### Language-Specific Rules

#### Python
- Use type hints for all function signatures
- Prefer `pathlib` over `os.path`
- Use `with` statements for resource management
- Follow PEP 8 with 100-char line limit
- Use `dataclasses` or `pydantic` for data objects
- Prefer `logging` over `print`

#### JavaScript/TypeScript
- Prefer `const` over `let`, never `var`
- Use async/await over raw promises
- Validate with TypeScript strict mode
- Use optional chaining (`?.`)
- Prefer `for...of` over `for` loops

#### Go
- Handle all errors explicitly
- Keep goroutine lifecycle clear
- Use `context.Context` for cancellation
- Follow effective Go conventions

### General Rules

- **Don't review generated code** (protobuf, OpenAPI, etc.) — note it and skip
- **Don't flag style issues** that the linter/formatter handles
- **Be constructive** — every criticism should include a suggested fix
- **Acknowledge good work** — positive reinforcement matters
- **Focus on the important** — security > correctness > performance > style

## Examples

### Good Review Comment
```
❌ Bad: "This is wrong."
✅ Good: "⚠️ `user_id` is not validated before the DB query (line 42).
   An attacker could inject arbitrary IDs. Add input validation
   and use parameterized query. Suggested fix:
   `user_id = validate_uuid(user_id)`"
```

### Positive Acknowledgment
```
✅ "Clean error handling pattern on lines 15-30.
   The custom exception hierarchy is well-designed and
   makes debugging easy."
```

## Integration

### With CI/CD
```yaml
# .github/workflows/code-review.yml
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: AI Code Review
        run: open-teams run code-review --pr ${{ github.event.number }}
```

### With Pre-commit
```bash
# Add to .pre-commit-config.yaml
- repo: local
  hooks:
    - id: ai-code-review
      name: AI Code Review
      entry: open-teams run code-review
      language: system
      stages: [pre-push]
```

## Changelog

- **v1.0** — Initial version: 6 review dimensions, 3 language rulesets, CI/CD integration