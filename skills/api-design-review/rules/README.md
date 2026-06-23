# api-design-review Rules

## REST-001: Plural Resource Names
**Severity:** High
Always use plural nouns for collection endpoints (`/users`, not `/getUsers`).

## REST-002: HTTP Methods by Semantic
**Severity:** High
GET=read, POST=create, PUT=replace, PATCH=update, DELETE=remove. No verbs in URL paths.

## REST-003: Pagination Required
**Severity:** High
All list endpoints must support pagination. Cursor-based preferred for large datasets.

## SEC-API-001: Authenticate Sensitive Endpoints
**Severity:** Critical
Public endpoints exposing user data or performing mutations must require authentication.

## REL-API-001: Idempotent Mutations
**Severity:** Medium
PUT and DELETE operations should be idempotent — repeated calls produce the same result.

## Add Your Rules Below
Customize with your team's API standards:
- Error envelope format (`{ errors: [{ code, message, field }] }`)
- Versioning strategy (URL path vs. header)
- Rate limiting thresholds
