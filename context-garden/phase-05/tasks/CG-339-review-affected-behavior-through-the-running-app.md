---
id: CG-339
title: Review affected behavior through the running application before accepting interaction claims
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
created: '2026-09-06T13:46:32+00:00'
updated: '2026-09-06T13:46:34+00:00'
---

## Goal

Review affected behavior through the running application before accepting interaction claims

## Context

Build on CG-315 capture evidence and CG-324 required evidence. Add actual interaction coverage for applicable PRs, with task objective, empty and failure states, browser observations and evidence tied to the tested head. Treat no_change and attention prompts as user outcomes, not just state transitions. Use disposable gardens, never the live operator queue.

## Acceptance criteria

- [ ] A reviewer can replay an affected flow in the real running app and distinguish screenshot-only evidence from performed actions. Applicable PRs with missing, failed or stale interaction evidence cannot be accepted as verified. Non-UI changes keep proportionate validation.
- [ ] The report cites commands, observed results and artifact paths, distinguishes automated checks from real interaction, and states all unverified requirements.

## Log

- 2026-09-06T13:46:34+00:00 approved (cli)

## Web-incident retro extension, 2026-09-06

CG-357 initially claimed performance evidence using inert worker records and ten in-process HTTP samples; an extrapolated p95 exceeded the maximum. Require applicable scalability claims to include a served disposable app, representative and larger history sizes, repeated cache-expiry intervals, actual executing bounded workload processes, empirical latency distribution and read/scan counts. Explicitly distinguish controlled load from real model harnesses. Tie evidence to reviewed head; a reviewer must refresh the comparison base before claiming unrelated history. Counterfactual: this evidence gate before the Now rollout would have exposed repeated full-history reads before normal operation failed. Existing operator recovery benchmark in product docs/design/cg357-validation is a starting point, not proof this policy is enforced.
