---
id: CG-485
title: Show accurate remote and manual run lifecycle without phantom process slots
status: done
product: context-garden
phase: phase-05
depends_on: []
kind: bug
priority: 0
difficulty: medium
reading:
- src/garden/runs.py
- src/garden/now1.py
- src/garden/scheduler/review.py
branch: codex/accurate-remote-run-lifecycle
pr: https://github.com/joshmarcus/context-garden/pull/385
attempts: 1
last_dispatched_at: '2026-09-09T16:20:45+00:00'
created: '2026-09-09T15:13:47+00:00'
updated: '2026-09-09T16:30:19+00:00'
---

## Goal

Replace the local-PID assumption in run presentation with accurate lifecycle labels for remote queued and claimed runs, finished results awaiting collection, manual reservations, and truly unlaunched local records. Align Now capacity figures with the scheduler's existing counters without changing admission, leases, reaping, or run completion.

## Context

The shared `Run.no_process` predicate currently treats remote and manual records like local subprocesses. This makes the Now page and queued-review explanations claim that remote work has no process and holds a slot until reaped. A valid remote lease alone is not proof that a remote model remains alive. Preserve CG-455's Now presentation and every durable run record.

## Acceptance criteria

- [ ] Remote queued/unclaimed, claimed, and result-awaiting-collection runs have truthful distinct presentation states without asserting liveness from lease expiry.
- [ ] Manual reservations and genuinely unlaunched local records receive accurate labels.
- [ ] Now worker/review capacity figures use the scheduler's existing active-run counters and do not present manual reservations or remote queue records as local processes.
- [ ] Focused regressions cover the lifecycle labels, review wait reason, and capacity accounting; scheduler admission and reap semantics are unchanged.

## Log

- 2026-09-09T15:13:48+00:00 approved (operator)
- 2026-09-09T15:14:15+00:00 dispatched work run 20260909T151414Z-work via manual [human] (fresh session, base main, ~14561 tokens)
- 2026-09-09T15:46:25+00:00 external PR attached at codex/accurate-remote-run-lifecycle; existing CI is SUCCESS
- 2026-09-09T15:53:36+00:00 automated review: approve — Lifecycle presentation and capacity accounting match the scheduler’s existing semantics, with no blocking defects found. cost=$0.34
- 2026-09-09T15:56:24+00:00 automated review: approve — Lifecycle presentation and capacity accounting accurately follow existing scheduler semantics without changing admission or reaping behavior. cost=$0.32
- 2026-09-09T15:56:34+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/now1.py, src/garden/runs.py, src/garden/scheduler/review.py, tests/test_now1.py); a rebase agent will resolve it
- 2026-09-09T16:03:08+00:00 kept 1 local-only commit(s) on `backup/20260909T160307Z-rebase` before syncing to origin/codex/accurate-remote-run-lifecycle's head: 12a799449 Show accurate remote run lifecycle
- 2026-09-09T16:03:12+00:00 dispatched rebase run 20260909T160307Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1476 tokens)
- 2026-09-09T16:04:15+00:00 preserved uncommitted worktree changes from run 20260909T160307Z-rebase outside the PR: `git stash apply efdf553462c5ad4a9e60818eae94ac8c7c7b4b29` in /home/joshua/work/worktrees/CG-485 (garden:CG-485:20260909T160307Z-rebase:reap)
- 2026-09-09T16:06:47+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.01
- 2026-09-09T16:17:26+00:00 dispatched revise run 20260909T161725Z-revise via manual [human] (fresh session, base main, ~15489 tokens)
- 2026-09-09T16:17:28+00:00 external PR attached at codex/accurate-remote-run-lifecycle; existing CI is SUCCESS
- 2026-09-09T16:20:22+00:00 automated review requested changes: Lifecycle behavior and capacity accounting are correct, but the current head fails the applicable Ruff check. cost=$0.38
- 2026-09-09T16:20:45+00:00 dispatched revise run 20260909T162039Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15566 tokens)
- 2026-09-09T16:23:05+00:00 preserved uncommitted worktree changes from run 20260909T162039Z-revise outside the PR: `git stash apply 2fc242b08b9985545202ce80464f7de00e43b624` in /home/joshua/work/worktrees/CG-485 (garden:CG-485:20260909T162039Z-revise:reap)
- 2026-09-09T16:23:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T16:24:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/385: Current head 9b937827 contains the requested Ruff import-order correction. Verified lifecycle presentation, review wait reasons, and capacity accounting with the focused Now suite (32 passed), then ran Ruff cleanly. cost=$0.22
- 2026-09-09T16:28:46+00:00 automated review: approve — Lifecycle presentation and capacity accounting match the scheduler’s existing semantics without changing admission or reaping behavior. cost=$0.54
- 2026-09-09T16:30:19+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/385
