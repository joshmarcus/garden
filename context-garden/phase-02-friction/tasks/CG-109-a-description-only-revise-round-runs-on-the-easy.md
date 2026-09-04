---
id: CG-109
title: A description-only revise round runs on the easy tier
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/review.py
- src/garden/harness.py
created: '2026-09-04T21:23:07+00:00'
updated: '2026-09-04T21:23:07+00:00'
---

## Goal

When a review's only finding is the PR description, the revise round runs on the easy tier, whatever the task's difficulty.

## Context

Found on the first live run. CG-081's review (PR #48) said the code was correct and well tested and asked only for the description to change (`description_ok: false`, no code findings); the revise round went out on the medium tier (opus 4.8) with a 13k-token brief, which is what a rewrite of a paragraph costs at that tier several times over. The review result already distinguishes description findings from code findings (CG-038 uses the same distinction for the stall check). At dispatch of a revise round, if `pending_feedback` has no code findings, pick the easy tier's model and say so in the dispatch note ("description only; easy tier"). A round with any code finding keeps the task's tier. Trials and persona reviews are unaffected.

## Acceptance criteria

- [ ] a description-only round dispatches on the easy tier's model and the note says why.
- [ ] a round with a code finding keeps the task's tier.
- [ ] a test with the fake harness for both.
