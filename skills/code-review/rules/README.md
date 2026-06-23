# code-review Rules

## SEC-001: No Hardcoded Secrets
**Severity:** Critical
Never commit passwords, tokens, API keys, or private keys in source code.

## SEC-002: Input Validation
**Severity:** High
Validate all user and external inputs for type, length, format, and range.

## QUAL-001: Meaningful Names
**Severity:** Medium
Variables, functions, and classes should have self-explanatory names.

## QUAL-002: Focused Functions
**Severity:** Low
Functions should do one thing well. Split large functions into smaller, testable units.

## PERF-001: Avoid N+1 Queries
**Severity:** High
Use eager loading, batch queries, or joins instead of looping database calls.

## Add Your Rules Below
Customize with your team's code standards:
- Framework-specific patterns
- Language-specific conventions
- Project-specific architectural constraints
