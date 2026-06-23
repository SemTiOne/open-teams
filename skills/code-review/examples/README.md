# code-review Examples

## Good Example
```python
def get_active_users(limit: int = 20) -> list[User]:
    '''Return active users, paginated.'''
    return User.query.filter_by(is_active=True).limit(limit).all()
```
✅ Clear name, type hints, docstring, single responsibility, parameterized.

## Bad Example
```python
def get():
    return db.execute("SELECT * FROM users WHERE active=1 AND name='" + name + "'")
```
❌ Vague name, SQL injection, no pagination, no type safety.

## Add Your Examples
Document patterns from your own codebase to help new team members learn conventions quickly.
