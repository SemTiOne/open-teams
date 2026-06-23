# architecture-review

## Purpose

Review architectural decisions, system designs, and technical proposals. Ensure significant design choices are documented, justified, and aligned with team principles.

## When to Use

- Before committing to a new system component, pattern, or dependency
- When evaluating technical proposals or design documents
- When asked to "review architecture" or "design review"

## Structure

- `SKILL.md` — This file: the review workflow, ADR template, and report format
- `rules/` — Enforceable architecture rules with severity levels

## Quick Example

```
User: "Review the proposal to add Redis caching layer"
AI: Checks design doc -> Verifies alternatives considered, scalability path, cost
    -> Report: Clear problem statement (good), 2 alternatives evaluated (good)
    -> Concerns: No failure mode analysis for cache miss storms
    -> Recommendation: Add circuit breaker + graceful degradation plan
```

## How to Customize

Define your team's architectural principles in `rules/README.md`. Customize the ADR template with your preferred sections and decision categories. Add technology-specific review dimensions (e.g., event-driven patterns, microservice boundaries, data consistency models) as your system evolves.
