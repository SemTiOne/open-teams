# Bad Code Review Example

## PR: Add user profile API

### Summary
- **Author:** @dev-c
- **Reviewer:** @dev-d
- **Scope:** 5 files changed, +120 -8 lines
- **Risk:** High (touches auth, database, and PII)

---

## Reviewer's Report

### 🔴 1 Critical Issue

1. **`api/users.ts:67`** — `GET /api/users/:id/profile` returns full user object including `password_hash`, `email`, and `phone` fields. This is a **PII leak**. The endpoint must use a DTO/projection to only return public profile fields.
   - *Severity: Critical*
   - *Action: Block merge until fixed.*

### ⚠️ 3 Warnings

2. **`api/users.ts:45`** — No authentication check before returning profile data. An unauthenticated user can query any user ID. Add `req.user` check and scope to current user + public profiles only.
   - *Severity: High*

3. **`db/user_repo.ts:23`** — Raw SQL string interpolation: `` `SELECT * FROM users WHERE id = ${userId}` ``. Use parameterized queries to prevent SQL injection.
   - *Severity: High*

4. **`api/users.ts:89`** — `PUT /api/users/:id` has no input validation. Currently accepts any JSON body and writes it directly to the database. Add Zod/Yup schema validation before the DB write.
   - *Severity: Medium*

### 💡 2 Suggestions

5. **`api/users.ts:1-120`** — The user controller mixes route handlers, validation logic, and database queries in one file. Consider splitting into controller → service → repository layers.
   - *Severity: Low*

6. **`db/user_repo.ts:12`** — `getUserById()` doesn't handle the case where `userId` is `undefined` or `NaN`. Add a guard clause.
   - *Severity: Low*

### Verdict
❌ **Request Changes.** The PII leak and missing auth are blockers. Fix Critical and Warnings before re-submission.
