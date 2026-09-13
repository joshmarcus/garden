---
id: CG-681
title: Align merge-policy guides with delivered behavior
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 2
difficulty: easy
reading:
- context-garden/phase-08/goals.md
- docs/operations.md
- docs/architecture.md
- src/garden/scheduler/poll.py
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T17:06:27+00:00'
---

## Goal

Update docs/operations.md and docs/architecture.md to explain one accepted current-head approval, legacy count normalization and the independent CI, conflict, dependency, protected-path and explicit human gates that remain applicable. Remove obsolete count-only and default second-opinion promises without restoring those policies. Check the revised explanations against current scheduler behavior and existing tests. File as a frozen Phase 08 draft.

## Context

A follow-up carried into phase-08 by the context-garden/phase-07 retro verdict.

## Acceptance criteria

- [ ] Update operating/architecture explanations to match delivered one-independent-approval behavior and legacy review-count normalization, removing obsolete mandatory second-opinion promises.
- [ ] Keep applicable CI, dependency, protected-path, conflict, explicit human gates and source-evidence requirements clear. A mechanical rebase or changed SHA alone does not create a new review requirement.
- [ ] Check statements against current implementation and existing acceptance tests; documentation-only verification is sufficient unless a real implementation discrepancy is discovered.

## Planning boundary

Retrospective draft in frozen Phase08; no implementation approval, runtime activation, private-data access, new workers or spending is implied. Address each outcome with meaningful observations; alternate evidence and reasoned criteria amendments are welcome. Preserve substantive findings and avoid process-only author rounds.
