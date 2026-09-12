---
id: CG-578
title: Use stable identities for preserved worktree changes
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-359
  after: merge
- id: CG-483
  after: merge
priority: 3
difficulty: medium
reading:
- src/garden/gitops.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/fence.py
branch: garden/cg-578-use-stable-identities-for-preserved-worktree-cha
pr: https://github.com/joshmarcus/context-garden/pull/467
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T17:47:33+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T19:19:58+00:00'
---

## Goal

Audit remaining preservation paths for positional shared-stash references. Use stable object identities and verify the restored content while preserving unrelated work. CG-483 reduces generated snapshot churn but does not remove Git's shared stash namespace.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Find every preservation path that consumes a shared positional stash reference. Retain a stable commit/object/ref identity through save, retry, restore and cleanup, verify the restored content, and never drop another attempt's stash. Use disposable Git repositories to check concurrent/unrelated stashes and interrupted restoration. Existing stable paths need no rewrite.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:47:33+00:00 dispatched work run 20260910T174733Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~11498 tokens)
- 2026-09-10T17:53:35+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:58:25+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.49
- 2026-09-10T18:34:22+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:24+00:00 opened https://github.com/joshmarcus/context-garden/pull/467 (base main): Recorded preserved worktree changes now use the stash object's stable SHA even when another linked worktree updates the shared stash namespace. Focused Git and reap/restart tests passed (77 tests); changed-file lint passed.
- 2026-09-10T18:34:24+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T19:09:49+00:00 automated review: approve — Preserved worktree recovery now records the intended stash object even when another linked worktree changes the shared stash tip. cost=$0.24
- 2026-09-10T19:18:30+00:00 automated review: approve — Stable stash identities are correctly retained and unrelated concurrent stashes remain untouched. cost=$0.26
- 2026-09-10T19:19:58+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/467
