# code-review

## Purpose

Standardized code review workflow for consistent quality, security, and style across the team. Every team member's AI assistant follows the same checklist when reviewing code.

## When to Use

- When asked to "review this code", "check this PR", or "code review"
- Before merging any pull request
- As a self-review step before submitting changes

## Structure

- `SKILL.md` — This file: the review workflow, dimensions, and report format
- `checklist.md` — Quick pre-review and per-dimension checklist items
- `rules/` — Enforceable review rules with severity levels
- `examples/` — Good and bad patterns for each review dimension

## Quick Example

```
User: "Review this PR"
AI: Reads changed files -> Checks security, performance, correctness, style
    -> Generates report: Critical(0), Warnings(2), Suggestions(3)
    -> Flags: hardcoded API key in config.py:15, N+1 query in users.py:42
```

## How to Customize

Add your team's specific rules to `rules/README.md` with severity levels (Critical/High/Medium/Low). Extend the checklist in `checklist.md` with language-specific or framework-specific items. Update the review dimensions in this file to match your tech stack and quality standards.
