---
id: CG-321
title: 'Reviews suggest fixes and improvements, not only a verdict: each finding carries a concrete fix,
  a separate improvements list goes beyond the criteria, and the revise brief carries both to the worker'
status: in_review
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
pr: https://github.com/joshmarcus/context-garden/pull/226
attempts: 1
last_dispatched_at: '2026-09-06T11:20:43+00:00'
created: '2026-09-06T03:19:28+00:00'
updated: '2026-09-06T12:41:03+00:00'
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
- 2026-09-06T08:55:08+00:00 dispatched revise run 20260906T085506Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~17506 tokens)
- 2026-09-06T09:17:40+00:00 opened https://github.com/joshmarcus/context-garden/pull/226 (base main): Preserved legacy fix-less review verdicts during restart recovery while retaining the one-time re-ask for freshly reaped blocking findings. cost=$0.48
- 2026-09-06T09:27:43+00:00 automated review requested changes: The actionable review fields render correctly, but high-priority findings are omitted from revision work. The PR description also needs to describe the complete feature and motivation. cost=$0.92
- 2026-09-06T10:24:25+00:00 dispatched revise run 20260906T102422Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~17379 tokens)
- 2026-09-06T11:18:54+00:00 pre-PR checks failed (test) (still failing after a rebase onto `main`); revise run will fix before the PR is updated cost=$0.99
- 2026-09-06T11:20:43+00:00 dispatched revise run 20260906T112039Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~23343 tokens)
- 2026-09-06T11:57:24+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 56af81dfcba5, not because of this branch; waiting for the base to go green, no revise round cost=$0.47
- 2026-09-06T12:15:26+00:00 base branch `main` recovered (moved to 40fc26107ed2); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-06T12:15:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/226: Automated reviews now provide concrete fixes and optional improvements, carry all findings into revision briefs, render them on PRs and task pages, and retain declined improvements as retro-visible friction.
- 2026-09-06T12:39:11+00:00 automated review: approve — Automated reviews now carry actionable fixes and optional improvements through comments, task pages, revision briefs, and retro-visible friction. The focused parser, scheduler, brief, friction, and web tests passed. cost=$0.72
- 2026-09-06T12:41:03+00:00 rebasing before merge; already on main's tip; not rebased or pushed
