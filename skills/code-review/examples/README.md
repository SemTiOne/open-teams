# Good Examples: Code Review

## Example 1: Input Validation (Python)

### ❌ Bad
```python
def get_user(user_id: str) -> User:
    return db.query(f"SELECT * FROM users WHERE id = {user_id}").first()
```
**Issues:** SQL injection via string interpolation. No input validation.

### ✅ Good
```python
import uuid
from models import User

def get_user(user_id: str) -> User | None:
    """Fetch a user by UUID, or None if not found."""
    try:
        uid = uuid.UUID(user_id)
    except ValueError:
        raise ValueError(f"Invalid UUID: {user_id}")
    
    user = db.query(User).filter(User.id == uid).first()
    if user is None:
        logger.warning("User not found: %s", user_id)
    return user
```
**Fixes:** Input validated and normalized to UUID. Parameterized ORM query. Type hint uses `| None`. Logger uses `%s` for lazy eval.

## Example 2: Error Handling (TypeScript)

### ❌ Bad
```typescript
async function fetchData(url: string): Promise<Data> {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}
```
**Issues:** No error handling. Assumes successful response. No timeout.

### ✅ Good
```typescript
async function fetchData(
    url: string, 
    timeoutMs = 5000
): Promise<Data> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    
    try {
        const response = await fetch(url, {
            signal: controller.signal,
            headers: { 'Accept': 'application/json' }
        });
        
        if (!response.ok) {
            throw new FetchError(
                `HTTP ${response.status}: ${response.statusText}`,
                response.status
            );
        }
        
        const data: unknown = await response.json();
        return validateData(data);
    } finally {
        clearTimeout(timer);
    }
}
```
**Fixes:** Timeout with AbortController. HTTP status check. Type-safe deserialization. Cleanup in finally.

## Example 3: Security Review Finding

**Review Comment:**
```
🔒 CRITICAL — SEC-001: GitHub token in source code
File: src/deploy.py:23
```python
GITHUB_TOKEN = "ghp_xxxxx"  # ← hardcoded token
```

This token has repository access. If committed, anyone can read it forever 
even after deletion (it stays in git history).

Fix:
```python
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ConfigError("GITHUB_TOKEN environment variable required")
```

Also: rotate this token immediately — it's been in a file.
```

## Example 4: Performance Finding

**Review Comment:**
```
⚡ MEDIUM — PERF-001: N+1 query in user list
File: src/api/users.py:45-48
```python
users = db.query(User).all()
for user in users:
    posts = db.query(Post).filter(Post.author_id == user.id).all()  # N+1!
```

With 100 users, this generates 101 queries (1 for users + 100 for posts).

Fix using eager loading:
```python
users = db.query(User).options(
    joinedload(User.posts)
).all()
```
```
