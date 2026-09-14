---
id: CG-700
title: Reuse validated Git coordination history
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 3
difficulty: medium
reading:
- context-garden/phase-11/goals.md
- src/garden/git_coordination.py
- tests/test_git_coordination.py
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:11:17+00:00'
---

## Goal

User value: authority checks remain responsive as the garden accumulates operations. Why now: every refresh validates history from its root. Size: medium. Dependencies: CG-631 and bounded transport. Cache immutable validated ancestry, batch reads and retain rewrite detection; define checkpoint and retention constraints that preserve ambiguous-operation resolution.

## Context

Proposed at the context-garden/phase-10 retro. Addressing demonstrable history-dependent work early avoids changing the coordination architecture later.

## Acceptance criteria

- [ ] Reuse validation of immutable accepted ancestry and validate only new descendants where safe, while still checking the current remote state and detecting rewritten or invalid history.
- [ ] Batch object access where useful and preserve durable operation replay, claims, permits and unresolved obligations; do not silently prune live recovery evidence to reduce history cost.
- [ ] Use deterministic Git command/read counts for unchanged-head and one-commit advancement cases, plus invalid-history controls. Larger stress measurements remain separately bounded and optional.

## Planning boundary

Frozen Phase11 retrospective draft. No implementation approval, production activation, extra worker capacity, spending or deadline extension is implied. Address every intended outcome substantively; alternate evidence and justified criteria amendments are welcome. Retain material failures and avoid cosmetic or mechanical-rebase rejection rounds.
