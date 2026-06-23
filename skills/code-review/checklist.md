# Code Review Checklist

## Before You Start
- [ ] Read the PR description or commit message
- [ ] Understand the change's purpose and scope
- [ ] Check if related issues or ADRs exist

## Security
- [ ] No secrets, tokens, or passwords in code
- [ ] User input is validated and sanitized
- [ ] Authentication/authorization on sensitive endpoints
- [ ] No sensitive data in logs or error messages

## Correctness
- [ ] Logic handles edge cases (null, empty, boundary values)
- [ ] Error cases are handled gracefully
- [ ] Return types and contracts are consistent

## Quality
- [ ] Meaningful variable and function names
- [ ] Functions are focused and reasonably sized
- [ ] No commented-out or dead code
- [ ] Complex logic has explanatory comments

## Testing
- [ ] New code has corresponding tests
- [ ] Edge cases and error paths are covered
