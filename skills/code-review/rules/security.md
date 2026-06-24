# Security Review Rules

> These rules are checked during every code review. Flag violations with their severity level.

---

## 🔴 Critical (Block Merge)

- **SEC-001:** Secrets, tokens, passwords, or API keys in source code — use environment variables or a vault
- **SEC-002:** SQL/NoSQL injection via unsanitized user input in queries — use parameterized queries or ORM
- **SEC-003:** Authentication bypass — any endpoint handling private data must validate `req.user` / session
- **SEC-004:** PII (email, phone, address, SSN, etc.) returned in API responses without explicit consent — use DTOs/projections

---

## 🟠 High (Must Fix)

- **SEC-005:** Missing authorization check — ensure the authenticated user has permission for the requested resource
- **SEC-006:** Unsafe deserialization of user-supplied data (e.g., `eval()`, `pickle.loads()`, `JSON.parse` on user input without schema validation)
- **SEC-007:** Hardcoded cryptographic keys, salts, or nonces — generate and store securely
- **SEC-008:** Sensitive data logged (passwords, tokens, full request bodies with PII) — strip sensitive fields before logging
- **SEC-009:** Open redirect via unvalidated `redirect_uri` or `next` parameter — whitelist allowed redirect domains

---

## 🟡 Medium (Should Fix)

- **SEC-010:** Missing rate limiting on auth endpoints (`/login`, `/register`, `/password-reset`, `/2fa`)
- **SEC-011:** CORS configured with `Access-Control-Allow-Origin: *` on authenticated endpoints
- **SEC-012:** Cookies missing `HttpOnly`, `Secure`, or `SameSite` flags
- **SEC-013:** File upload without type/size validation — restrict allowed MIME types and enforce max size
- **SEC-014:** Error messages exposing internal details (stack traces, database errors, server paths) — use generic error responses

---

## 🟢 Low (Nice to Have)

- **SEC-015:** CSP headers not set or too permissive — use `Content-Security-Policy` to restrict inline scripts
- **SEC-016:** Dependency with known CVE — check `npm audit` / `pip audit` / `bundler audit` output
- **SEC-017:** Missing subresource integrity (SRI) hashes on third-party CDN scripts
- **SEC-018:** Password strength requirements not enforced — minimum 8 chars, no common passwords

---

## How to Add Team-Specific Rules

Add your own rules below using the same format:

```
- **SEC-XXX:** Rule description — guidance for fixing
```
