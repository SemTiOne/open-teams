# Code Review Rules

## Security Rules

### SEC-001: No Hardcoded Secrets
**Severity:** Critical
Never commit secrets, API keys, tokens, or passwords. Use environment variables or a secrets manager.

### SEC-002: SQL Injection Prevention
**Severity:** Critical
Always use parameterized queries. Never concatenate user input into SQL strings.

### SEC-003: Input Validation
**Severity:** High
Validate all user input at the boundary. Use allowlists over blocklists. Validate type, length, format, and range.

### SEC-004: XSS Prevention
**Severity:** High
Escape all user-controlled data in HTML. Use Content-Security-Policy headers. Prefer template engines with auto-escaping.

### SEC-005: Auth Checks
**Severity:** Critical
Every endpoint that accesses protected data must verify authentication and authorization. Don't rely on client-side checks alone.

## Performance Rules

### PERF-001: N+1 Queries
**Severity:** High
Use eager loading, batch queries, or DataLoader patterns. Each loop iteration should not trigger a new database query.

### PERF-002: Memory Leaks
**Severity:** Medium
Clean up event listeners, timers, and subscriptions. Check for circular references. Use WeakMap/WeakRef where appropriate.

### PERF-003: Appropriate Data Structures
**Severity:** Medium
Use `Set` for membership checks, `Map` for key-value lookups. Avoid O(n²) where O(n log n) is possible.

## Code Quality Rules

### QUAL-001: Function Size
**Severity:** Low
Functions should do one thing. Target < 50 lines. Extract helper functions for complex logic.

### QUAL-002: Magic Numbers
**Severity:** Low
Use named constants instead of literal numbers. Exceptions: 0, 1, -1 in obvious contexts.

### QUAL-003: Commented-Out Code
**Severity:** Low
Remove commented-out code before merging. Git history preserves it if needed.

### QUAL-004: Error Handling
**Severity:** High
Don't swallow exceptions silently. Log with context. Provide meaningful error messages to users.

## Python-Specific Rules

### PY-001: Type Hints
Use type hints on all public function signatures. Use `Optional[X]` not `Union[X, None]`.

### PY-002: Context Managers
Use `with` statements for file I/O, database connections, and locks.

### PY-003: F-Strings
Prefer f-strings over `.format()` for readability. Exception: logging uses `%s` for lazy evaluation.
