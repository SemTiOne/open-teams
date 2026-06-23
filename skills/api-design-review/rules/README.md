# api-design-review Rules

## REST-001: Plural Resource Names
**Severity:** High
Always use plural nouns for collection endpoints.

## REST-002: No Verbs in Paths
**Severity:** High
Use HTTP methods (GET, POST, PUT, DELETE) to express actions.

## REST-003: Consistent Status Codes
**Severity:** High
Use standard HTTP status codes consistently.

## REST-004: Pagination
**Severity:** High
All list endpoints must support pagination (cursor-based preferred).

## REST-005: Error Format
**Severity:** Medium
Use a consistent error envelope with code, message, and optional field.

## SEC-API-001: No IDs in Auth Tokens
**Severity:** Critical
Never send authentication tokens in URL query parameters or paths.

## SEC-API-002: Input Validation
**Severity:** Critical
Validate all input: type, length, format, range. Never trust client input.

## SEC-API-003: Rate Limiting
**Severity:** High
All public endpoints should have rate limiting configured.

## REL-001: Idempotency
**Severity:** Medium
PUT and DELETE operations should be idempotent.

## REL-002: Timeouts
**Severity:** Medium
All API calls should have configured timeouts (default: 30s).
