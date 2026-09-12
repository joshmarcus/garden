---
id: CG-494
title: Show standalone scheduler health and coordinate manual ticks
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/web/common.py
- src/garden/cli/loop.py
- src/garden/scheduler/__init__.py
- docs/architecture.md
branch: garden/cg-494-show-standalone-scheduler-health-and-coordinate
pr: https://github.com/joshmarcus/context-garden/pull/404
attempts: 1
last_dispatched_at: '2026-09-10T01:59:23+00:00'
created: '2026-09-09T18:52:57+00:00'
updated: '2026-09-10T02:13:43+00:00'
---

## Goal

Make the UI and manual tick controls truthful when web serving and the scheduler watch run as
separate supported processes.

## Context

RC14 is operating as `garden serve --no-watch` plus one `garden watch` service under a shared
aggregate slice. This removed shared-interpreter contention and restored navigation. The
current UI can describe the embedded loop as off even while the standalone watcher is healthy,
and a manual tick must coordinate with that watcher through the existing `tick.lock` rather
than suggesting the scheduler is absent. Use the split activation and post-resume evidence in
`/home/joshua/work/operator-test-tmp/rc14-split-20260909`; do not infer health only from the
web process.

## Acceptance criteria

- [ ] UI status distinguishes embedded-watch state from effective scheduler health and shows
      a healthy standalone watcher without claiming scheduling is off.
- [ ] Health uses bounded, auditable process/unit or scheduler-heartbeat evidence and reports
      stale, missing, duplicated, or failed watcher state accurately.
- [ ] Manual tick remains supported and serializes with the standalone watcher through the
      existing tick lock; concurrent invocation cannot produce overlapping scheduler passes.
- [ ] Served navigation, watcher failure/recovery, and manual-tick coordination have focused
      regression coverage with truthful user-facing wording.

## Out of scope

- Replacing the validated split units, changing controller resource caps, or merging the
  operational isolation into this task.
- PR 395's bounded discovery/CI retention scope and unrelated scheduler performance work.

## Log

- 2026-09-09T18:53:52+00:00 approved (cli)
- 2026-09-09T21:52:59+00:00 dispatched work run 20260909T215255Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18708 tokens)
- 2026-09-09T22:06:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T22:07:53+00:00 opened https://github.com/joshmarcus/context-garden/pull/404 (base main): Added durable standalone watcher health evidence and truthful web status while preserving manual tick coordination through the existing cross-process tick lock. Verified the committed head with 233 focused CLI/web/Now/health tests and the complete requested Ruff lint command. cost=$1.75
- 2026-09-09T22:11:26+00:00 automated review requested changes: Standalone health is surfaced clearly, but startup reaping can overlap a manual tick and mixed watcher states can be incorrectly reported as healthy. cost=$0.42
- 2026-09-09T22:11:39+00:00 dispatched revise run 20260909T221135Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20038 tokens)
- 2026-09-09T22:16:06+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T22:17:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/404: Startup recovery now serializes with manual and standalone ticks through tick.lock, while scheduler health accounts for all bounded live, failed, and stale watcher evidence. Committed as 19fb3595; 140 focused tests passed, the final 6-test health suite passed, and Ruff passed across src, tests, and scripts. cost=$0.72
- 2026-09-09T22:19:44+00:00 automated review requested changes: Standalone health and cross-process locking work, but effective health still treats embedded-watch configuration as proof of health. cost=$0.45
- 2026-09-09T22:19:56+00:00 dispatched revise run 20260909T221953Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20227 tokens)
- 2026-09-09T22:25:32+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T22:26:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/404: Embedded scheduler health now uses actual loop success, failure, freshness, and thread-liveness evidence instead of treating configuration as proof of health. Focused health/navigation/coordination coverage passed (11 tests), the dedicated health suite passed again (8 tests), and Ruff passed across src, tests, and scripts. cost=$0.89
- 2026-09-09T22:29:10+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: ui distinguishes embedded-watch state ; run `garden triage CG-494 --changes "<feedback>" to unblock`
- 2026-09-09T22:59:58+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T00:59:23+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T01:09:05+00:00 dispatched revise run 20260910T010902Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20474 tokens)
- 2026-09-10T01:12:42+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:14:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/404: Standalone watcher startup is now reported as starting until running or successful-tick evidence exists, including truthful user-facing rail wording. Verified commit 453100061f822d0b0c22b7863a7f72796fca363b with 12 focused health/navigation/coordination tests and clean Ruff lint across src, tests, and scripts. cost=$0.50
- 2026-09-10T01:16:36+00:00 automated review requested changes: Locking and displayed state behavior are covered, but accumulated historical leases can hide the active watcher and falsely report it missing. cost=$0.33
- 2026-09-10T01:43:22+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T01:59:23+00:00 dispatched revise run 20260910T015919Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20732 tokens)
- 2026-09-10T02:01:32+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T02:02:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/404: Scheduler health now prioritizes parsed leases by heartbeat freshness before applying the 64-record bound, so accumulated expired leases cannot mask an active standalone watcher. Verified commit bf973c90bfd8b69c559b8645e0226644b9f7d8e8 with all 11 focused scheduler-health/navigation/coordination tests and repository-wide Ruff lint passing. cost=$0.46
- 2026-09-10T02:05:20+00:00 automated review: approve — The current head truthfully separates embedded and standalone scheduler state, bounds and prioritizes watcher evidence, and serializes startup recovery and ticks through the shared lock. cost=$0.23
- 2026-09-10T02:12:26+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T02:13:43+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/404
