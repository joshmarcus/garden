---
id: CG-538
title: Explain accepted completion before historical reviews
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-362
  after: merge
- id: CG-487
  after: merge
- id: CG-536
  after: merge
priority: 1
difficulty: medium
reading:
- src/garden/web/pages/task.py
- src/garden/web/templates/task.html
- src/garden/scheduler/human.py
- src/garden/runs.py
branch: garden/cg-538-explain-accepted-completion-before-historical-re
pr: https://github.com/joshmarcus/context-garden/pull/463
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T17:32:13+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T18:45:21+00:00'
---

## Goal

User value: understand why a task is complete without reconstructing its timeline. Why now: three personas found historical rejection presented as current. Size: medium. Dependencies: existing completion provenance, CG-362/487 and the canonical acceptance correction; retain complete dated, source-specific findings.

## Context

Proposed at the context-garden/phase-05 retro. Clear completion provenance makes the existing workflow understandable without weakening review history.


## Reviewed scope and verification

Present the current accepted completion and its source/reason first, then retain historical reviews, failures and interventions as dated history. Distinguish reviewed/merged acceptance, explicit owner acceptance and forced status completion according to CG-536. Verify that historical rejection does not falsely describe the current outcome, while every original finding remains accessible. Absorb CG-551 completion presentation; check-run presentation remains CG-539.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:32:13+00:00 dispatched work run 20260910T173213Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~13932 tokens)
- 2026-09-10T17:41:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:47:11+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$1.26
- 2026-09-10T18:34:12+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/463 (base main): Task pages now show current completion provenance before review history, distinguish accepted merge, owner acceptance, and forced completion, and retain dated source-specific review findings. Verified with four focused task-page web tests; scoped lint passes.
- 2026-09-10T18:34:14+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:42:05+00:00 automated review: approve — Current accepted or forced completion is presented before historical automated reviews, with clear provenance and preserved findings. cost=$0.38
- 2026-09-10T18:43:34+00:00 automated review: approve — Current accepted or forced completion is clearly presented before dated, source-specific historical reviews while preserving prior findings. cost=$0.29
- 2026-09-10T18:45:21+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/463
