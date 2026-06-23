# api-design-review

## Purpose

Review REST and GraphQL API designs for consistency, security, and usability. Ensure all endpoints across the team follow shared conventions and best practices.

## When to Use

- When creating or modifying API endpoints
- Before finalizing an API specification or OpenAPI document
- When asked to "review this API" or "check endpoint design"

## Structure

- `SKILL.md` — This file: the review workflow and report format
- `rules/` — Enforceable API design rules with severity and rationale

## Quick Example

```
User: "Review our /users endpoint design"
AI: Checks REST conventions -> Verifies auth, pagination, error format
    -> Report: Uses plural nouns (good), Has pagination (good)
    -> Issues: Missing rate limiting, no field selection support
```

## How to Customize

Define your team's API conventions in `rules/README.md` — naming patterns, error envelope format, versioning strategy, and authentication standards. Extend the review dimensions to cover GraphQL schemas, gRPC service definitions, or event-driven messaging contracts as your architecture grows.
