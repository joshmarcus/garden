---
id: CG-321
title: 'Reviews suggest fixes and improvements, not only a verdict: each finding carries a concrete fix,
  a separate improvements list goes beyond the criteria, and the revise brief carries both to the worker'
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/review.py
- src/garden/scheduler/review.py
- src/garden/brief.py
- src/garden/web/templates/task.html
- principles/00-index.md
- tests/test_review.py
branch: garden/cg-321-reviews-suggest-fixes-and-improvements-not-only
attempts: 1
last_dispatched_at: '2026-09-06T05:55:55+00:00'
created: '2026-09-06T03:19:28+00:00'
updated: '2026-09-06T06:52:14+00:00'
---

## Goal

A review is the strongest model's advice on the change, not only its grade. Besides the verdict and the per-criterion evidence, the reviewer returns for every finding a concrete `fix` (what to change, where, with a short code sketch when one fits), and a separate `improvements` list of non-blocking suggestions beyond the acceptance criteria: simplifications that lower cognitive complexity at its level (the principle), better names, a missing test, a doc line, a cheaper implementation. The revise brief hands the worker the findings with their fixes as the round's work and the improvements as optional items to take or decline with a sentence; the task page and the PR comment show both lists; the retro's friction harvest keeps declined improvements so a pattern can become a task.

## Context

Owner, 2026-09-06 03:22Z: "reviews can actually suggest fixes and improvements and not just evaluate acceptance criteria." Today the GARDEN_REVIEW block carries a verdict, criteria evidence, description feedback and findings with a summary; the revise brief is generic (CG-293 fixes its shape). With reviews now on a model one rung above the writer (CG-320), the reviewer's advice is worth more than its verdict, and a weaker writer given the fix in words lands it in one round instead of two.

## Acceptance criteria

- [ ] The review prompt and the GARDEN_REVIEW schema carry `fix` on every finding (required for blocking and high, encouraged otherwise) and a top-level `improvements` list (each with area, suggestion, why, and an effort of small or medium); the parser tolerates their absence from older reviewers.
- [ ] The revise brief lists findings with their fixes as the round's work and improvements as optional items; the worker's result names which improvements it took and which it declined, and the task page shows both.
- [ ] The PR comment posted by the garden shows fixes under each finding and an Improvements section; a review that returns no fix for a blocking finding is re-asked once.
- [ ] Tests: the review parser with and without the new fields; the revise brief builder including both lists; the PR comment rendering.

## Log
- 2026-09-06T03:19:29+00:00 approved (cli)
- 2026-09-06T05:55:55+00:00 dispatched work run 20260906T054128Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15339 tokens)
- 2026-09-06T06:52:14+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$1.11
