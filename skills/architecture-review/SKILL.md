# architecture-review

## Purpose

Review architectural decisions, system designs, and technical proposals. Ensure design decisions are documented, justified, and aligned with team standards.

## Trigger

- When a user asks to "review architecture", "arch review", "design review"
- Before significant technical decisions
- When evaluating a new system component or pattern
- When running `open-teams run architecture-review`

## Workflow

### 1. Context
- Read the design document / proposal / diagram
- Read AGENTS.md for architecture principles
- Read MEMORY.md for relevant past decisions
- Check existing Architecture Decision Records (ADRs)

### 2. Review Dimensions

#### 🏛️ Design Quality
- [ ] Clear problem statement — what are we solving?
- [ ] Alternatives considered with trade-offs
- [ ] Decision is justified with data/experience
- [ ] Scope is well-defined (what's in, what's out)
- [ ] Non-functional requirements addressed (scalability, reliability, security, cost)

#### 🔗 System Fit
- [ ] Compatible with existing architecture
- [ ] Follows established patterns (or justifies deviation)
- [ ] Integration points clearly defined
- [ ] Data flow diagram or sequence diagram
- [ ] API contracts defined

#### 📈 Scalability
- [ ] Handles expected load (with buffer)
- [ ] Horizontal scaling path defined
- [ ] Bottlenecks identified
- [ ] Caching strategy
- [ ] Database scaling plan (sharding, replication)

#### 🛡️ Reliability
- [ ] Failure modes identified
- [ ] Graceful degradation strategy
- [ ] Error handling and recovery
- [ ] Monitoring and alerting plan
- [ ] Backup and disaster recovery

#### 💰 Cost
- [ ] Infrastructure cost estimated
- [ ] Operational cost (maintenance, on-call)
- [ ] Migration cost from current state
- [ ] Cost optimization opportunities

#### 🔒 Security
- [ ] Data classification and handling
- [ ] Authentication and authorization flow
- [ ] Network security (VPC, firewall, TLS)
- [ ] Compliance requirements (GDPR, SOC2, etc.)
- [ ] Secrets management

#### 📅 Implementation
- [ ] Migration path from current state
- [ ] Rollout plan (phased vs big bang)
- [ ] Rollback plan
- [ ] Feature flags / toggles considered
- [ ] Testing strategy for the new design

### 3. ADR Format

Generate an Architecture Decision Record:

```markdown
# ADR-[NNN]: [Title]

**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** [YYYY-MM-DD]
**Deciders:** [names]
**Supersedes:** ADR-[xxx] (if any)

## Context
[What is the issue motivating this decision?]

## Decision
[What is the change we're proposing?]

## Alternatives Considered
| Alternative | Pros | Cons | Verdict |
|-------------|------|------|---------|
| Option A    | ...  | ...  | ...     |
| Option B    | ...  | ...  | ...     |

## Consequences
### Positive
- ...

### Negative
- ...

### Neutral
- ...

## Implementation Plan
- [ ] Task 1
- [ ] Task 2

## References
- [Link to related docs]
```

### 4. Report Generated

```markdown
# Architecture Review: [proposal name]

**Date:** [date]
**Reviewer:** AI (architecture-review skill)

## Executive Summary
[2-3 sentence summary]

## Strengths
- [What's well-designed]

## Concerns
### Critical
- [Must-address issues]

### Major
- [Should-address issues]

### Minor
- [Nice-to-address issues]

## Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|

## Recommendations
1. [Actionable recommendation]

## Assessment
[✅ Approved with recommendations / ⚠️ Changes required / ❌ Rejected]
```

## Rules

### ARCH-001: ADR Required
**Severity:** High
Any significant architectural decision MUST be documented as an ADR.
"Significant" = affects system behavior, cost, or team workflow.

### ARCH-002: At Least 2 Alternatives
**Severity:** Medium
Every design proposal must compare at least 2 alternatives (including "do nothing").

### ARCH-003: Non-Functional Requirements
**Severity:** High
All designs must address: scalability limits, availability target, latency budget, security model, cost estimate.

### ARCH-004: State Management
**Severity:** Medium
Clearly identify stateful components and their data consistency requirements.

### ARCH-005: Simplicity Bias
**Severity:** Low
Prefer simpler designs. Complex solutions require stronger justification. "You aren't gonna need it."
