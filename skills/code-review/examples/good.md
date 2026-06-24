# Good Code Review Example

## PR: Add rate limiting to API endpoints

### Summary
- **Author:** @dev-a
- **Reviewer:** @dev-b
- **Scope:** 3 files changed, +45 -12 lines
- **Risk:** Low

---

## Reviewer's Report

### ✅ What's Good

1. **Security:** Rate limit uses Redis with atomic counters — no race conditions
2. **Error Handling:** Returns proper 429 with Retry-After header
3. **Config:** Rate limits are configurable via env vars, not hardcoded
4. **Testing:** Tests cover normal flow, rate limit exceeded, and Redis failure fallback
5. **Documentation:** Added inline comments explaining the token bucket algorithm choice

### ⚠️ 2 Warnings

1. **`middleware/rate_limiter.ts:42`** — Token bucket window resets at fixed intervals (every 60s). Under burst traffic at window boundaries, users may get 2x the configured limit. Consider sliding window instead.
   - *Severity: Medium*
   - *Author response: Good catch. Will switch to sliding window in follow-up PR #156.*

2. **`config/rate_limits.ts:8`** — Default rate limit of 100 req/min is too permissive for auth endpoints (`/login`, `/register`). These should be 10 req/min to prevent brute force.
   - *Severity: Medium*
   - *Author response: Fixed in latest commit.*

### 💡 1 Suggestion

1. **`middleware/rate_limiter.ts:28`** — `getClientIp()` falls back to `req.ip` when `X-Forwarded-For` is missing, but doesn't validate the header. Consider adding a trust proxy check for production.
   - *Severity: Low*
   - *Author response: Added --trust-proxy flag note to deployment docs.*

### Verdict
✅ **Approve with suggestions.** Non-blocking warnings addressed in follow-up. Ship it.
