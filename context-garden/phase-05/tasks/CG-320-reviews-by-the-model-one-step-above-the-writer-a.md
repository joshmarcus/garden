---
id: CG-320
title: 'Reviews by the model one step above the writer: a review ladder across harnesses picks the reviewer
  from the PR''s last work or revise model'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/review.py
- src/garden/scheduler/edits.py
- src/garden/scheduler/__init__.py
- src/garden/config.py
- examples/garden.work.yaml
- tests/scheduler/test_dispatch.py
branch: garden/cg-320-reviews-by-the-model-one-step-above-the-writer-a
attempts: 1
last_dispatched_at: '2026-09-06T06:17:02+00:00'
created: '2026-09-06T03:18:47+00:00'
updated: '2026-09-06T06:17:02+00:00'
---

## Goal

Every automated review is done by a model one rung stronger than the one that wrote the code under review. `review.ladder` lists `harness:model` entries from weakest to strongest across harnesses (for this garden: codex:gpt-5.6-luna, claude:claude-sonnet-5, codex:gpt-5.6-terra, codex:gpt-5.6-sol, claude:claude-opus-4-8, claude:claude-fable-5-1, codex:gpt-6-astra, in the owner's order); the reviewer for a PR is the entry after the model of the PR's last work or revise run, the top entry reviews itself, and a model not on the ladder falls back to `review.difficulty` as today. The rung is recorded on the review run and shown on the task page ("reviewed by sol, one above terra"). Persona reviews and the retro keep `retro_model`.

## Context

Owner, 2026-09-06 03:20Z: "let's do all reviews by an agent that's one step up from the strength of the agent that wrote the PR." Today the reviewer is one model for all PRs (`review.difficulty` picks a tier, or `harnesses.<h>.review_model` fixes it), so a luna easy task and a fable design get the same reviewer. Measured tonight: reviews cost $0.24 on terra, $0.73 on sonnet 5, $0.82 on opus 4.8, about $1.90 on fable; 141 rounds a day in phase 04. The interim setting is every review on the hard tier (sol).

## Acceptance criteria

- [ ] `review.ladder` (list of `harness:model`) is read live; `_dispatch_review` picks the entry after the PR's last work or revise run's `harness:model`, the top entry reviews itself, and an unlisted model uses the tier rule; the chosen rung and the writer's model are logged on the task and stored on the run.
- [ ] A cross-harness step works: a codex terra PR reviewed by codex sol, a claude fable PR reviewed by codex astra, a codex luna PR reviewed by claude sonnet 5, each dispatched on the reviewer's harness with its own credentials and paused-harness check.
- [ ] The Config page lists the ladder among the live keys; `examples/garden.work.yaml` shows it; the task page names the rung.
- [ ] Tests with the fake harnesses for the three steps above, the top rung, the unlisted fallback, and a paused reviewer harness deferring the round.

## Log
- 2026-09-06T03:18:48+00:00 approved (cli)
- 2026-09-06T05:24:07+00:00 dispatched work run 20260906T052209Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~21312 tokens)
- 2026-09-06T06:16:10+00:00 pre-PR checks failed (checks); no PR opened yet; revise run will fix cost=$0.92
- 2026-09-06T06:17:02+00:00 dispatched revise run 20260906T061658Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~21599 tokens)
