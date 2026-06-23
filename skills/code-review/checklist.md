# Code Review Checklist

## Before You Start
- [ ] Read the PR description / commit message
- [ ] Understand the change's purpose
- [ ] Check if related issues exist

## Security
- [ ] No secrets, tokens, or passwords in code
- [ ] User input is validated and sanitized
- [ ] SQL queries use parameterization
- [ ] Authentication/authorization on sensitive endpoints
- [ ] No sensitive data in logs

## Correctness
- [ ] Logic handles edge cases (null, empty, boundary)
- [ ] Error cases are handled gracefully
- [ ] Race conditions considered (if concurrent)
- [ ] Return types match expectations

## Performance
- [ ] Algorithm complexity is appropriate
- [ ] No unnecessary database queries
- [ ] Appropriate use of caching
- [ ] No memory leaks (event listeners, timers, large objects)

## Maintainability
- [ ] Code is readable and self-documenting
- [ ] Complex logic has comments
- [ ] No magic numbers
- [ ] Functions are small and focused
- [ ] No duplicated code

## Testing
- [ ] Tests cover the new functionality
- [ ] Tests cover error paths
- [ ] Test names describe what's being tested
- [ ] No flaky tests

## Style & Conventions
- [ ] Follows project style guide
- [ ] Consistent naming conventions
- [ ] Proper formatting (linting passes)

## Dependencies
- [ ] New dependencies are justified
- [ ] Versions are pinned
- [ ] License compatibility
