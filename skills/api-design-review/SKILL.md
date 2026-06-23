# api-design-review

## Purpose

Review REST/GraphQL API designs for consistency, security, and usability. Standardize API design across the team so all endpoints follow the same patterns.

## Trigger

- When a user asks to "review this API", "API review", "design review"
- When creating new API endpoints or modifying existing ones
- When running `open-teams run api-design-review`

## Workflow

### 1. Gather Context
- Read the API spec / code / OpenAPI file
- Read AGENTS.md for API conventions
- Check existing API patterns in the codebase

### 2. Review Dimensions

#### 🏗️ RESTful Design
- [ ] Resources use plural nouns (`/users`, `/projects`)
- [ ] HTTP methods used correctly (GET=read, POST=create, PUT=replace, PATCH=update, DELETE=remove)
- [ ] No verbs in URL paths (use `/users/{id}/activate` over `/activateUser`)
- [ ] Nested resources only 2 levels deep max
- [ ] Consistent naming (kebab-case, camelCase, or snake_case — pick one)

#### 📦 Request/Response Design
- [ ] Consistent envelope format (`{ data, meta, errors }`)
- [ ] Pagination for list endpoints (cursor-based preferred)
- [ ] Filtering and sorting documented
- [ ] Field selection support (`?fields=id,name`)
- [ ] Appropriate HTTP status codes

#### 🔒 Security
- [ ] Authentication required where appropriate
- [ ] Authorization checks per endpoint
- [ ] Rate limiting considered
- [ ] Input validation on all parameters
- [ ] No sensitive data in URLs (IDs in path OK, tokens in path NOT OK)
- [ ] CORS headers configured correctly

#### 📝 Documentation
- [ ] OpenAPI/Swagger or GraphQL schema
- [ ] Request/response examples
- [ ] Error codes documented
- [ ] Authentication requirements documented
- [ ] Deprecation notices for old endpoints

#### 🔄 Versioning
- [ ] Versioning strategy defined (URL path vs header)
- [ ] Backward-compatible changes preferred
- [ ] Deprecation schedule for breaking changes
- [ ] Migration guides for version upgrades

#### 🧪 Testing & Reliability
- [ ] Idempotency for PUT/DELETE
- [ ] Timeouts configured
- [ ] Retry strategy for transient failures
- [ ] Circuit breaker for downstream failures
- [ ] Graceful degradation

### 3. Report Generated

```markdown
# API Design Review: [endpoint/service]

**Date:** [date]
**Endpoints Reviewed:** [count]

## Summary
[Overall assessment]

## Critical Issues
- [Issue] — [Rule] — [Fix]

## Design Issues
- [Issue] — [Pattern] — [Suggested change]

## Security Concerns
- [Concern] — [Risk level] — [Mitigation]

## Consistency Issues
- [Issue] — [Current] vs [Standard] — [Action]

## Suggestions
- [Suggestion] — [Rationale]

## Assessment
[✅ Ready / ⚠️ Changes Requested]
```

## Rules

### REST-001: Plural Resource Names
Always use plural nouns for collection endpoints.
- ✅ `GET /api/users`
- ❌ `GET /api/getUsers`

### REST-002: No Verbs in Paths
Use HTTP methods to express actions.
- ✅ `POST /api/projects/{id}/archive`
- ❌ `POST /api/archiveProject`

### REST-003: Consistent Status Codes
- 200: Success (GET, PUT, PATCH)
- 201: Created (POST)
- 204: No Content (DELETE)
- 400: Bad Request
- 401: Unauthenticated
- 403: Forbidden
- 404: Not Found
- 409: Conflict
- 422: Unprocessable Entity
- 429: Too Many Requests
- 500: Internal Server Error

### REST-004: Pagination
All list endpoints MUST support pagination.
```json
{
  "data": [...],
  "meta": {
    "cursor": "abc123",
    "has_more": true,
    "total": 1432
  }
}
```

### REST-005: Consistent Error Format
```json
{
  "errors": [
    {
      "code": "VALIDATION_ERROR",
      "message": "Email is required",
      "field": "email"
    }
  ]
}
```

## Examples

### Good API Design
```
GET /api/users?status=active&sort=-created_at&limit=20&cursor=abc123

Response: 200 OK
{
  "data": [{ "id": "1", "name": "Alice", ... }],
  "meta": {
    "cursor": "abc124",
    "has_more": true
  }
}
```

### Bad API Design
```
GET /api/getActiveUsers?sortBy=nameDesc

Issues:
- Verb in path ("getActiveUsers") → use GET /api/users?status=active
- Custom sort syntax → use standard: ?sort=-name
- No pagination → add limit + cursor
- No envelope → wrap in { data, meta }
```
