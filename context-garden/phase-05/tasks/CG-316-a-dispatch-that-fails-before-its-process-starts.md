---
id: CG-316
title: A dispatch that fails before its process starts closes the run record at once, and the orphan sweep
  closes any running record with no live process
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/reap.py
- src/garden/runner/local.py
- src/garden/runs.py
- src/garden/web/pages/board.py
- tests/scheduler/test_dispatch.py
- tests/scheduler/test_orphan_sweep.py
branch: garden/cg-316-a-dispatch-that-fails-before-its-process-starts
pr: https://github.com/joshmarcus/context-garden/pull/212
attempts: 1
last_dispatched_at: '2026-09-06T04:06:55+00:00'
created: '2026-09-06T02:11:57+00:00'
updated: '2026-09-06T04:06:55+00:00'
---

## Goal

A run record is `running` only while a process is running. When `dispatch` fails after creating the record but before the worker starts (setup error, disk full, a refused command), the record is closed as `failed` with the error in the same tick; and each tick the orphan sweep closes any `running` record whose `pid` is missing or dead, instead of waiting for the 90-minute timeout. The rail's Running now list and the in-flight guard (CG-238) therefore never see a run that is not there.

## Context

2026-09-06 01:01Z: three revise dispatches (CG-242, CG-245, CG-249) failed with ENOSPC while creating a temp directory. Each task was marked failed, but its run record stayed `running` with no pid. Seventy minutes later the rail still listed "CG-242 revise · 70 min", the owner asked why, and the in-flight guard blocked the revises the operator re-queued, because the dead record counted as a run in flight. The reaper only closes such a record after `timeout_minutes` plus five.

## Acceptance criteria

- [ ] `dispatch` wraps runner start so that any exception after `runs.new_run` marks the record `failed` with `finished_at` and the error text, emits `run_finished`, and re-raises or logs as today; a test provokes the failure with a broken setup command and asserts the record.
- [ ] The orphan sweep marks a `running` record with no pid, or a pid that is not alive and no exit code within one tick, as `failed` (reason "process never started" or "process vanished"), and the task's status follows the same path as a worker crash.
- [ ] The Board's Running now list reads only records with a live process; a test renders it with a dead record and sees nothing.

## Log
- 2026-09-06T02:11:57+00:00 approved (cli)
- 2026-09-06T02:53:33+00:00 dispatched work run 20260906T025240Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~24078 tokens)
- 2026-09-06T03:07:59+00:00 opened https://github.com/joshmarcus/context-garden/pull/212 (base main): Dispatch-start failures and orphaned worker records now close immediately, and the Running list only shows live processes. cost=$0.13
- 2026-09-06T03:10:12+00:00 automated review requested changes: The start-failure handler does not cover all exceptions after run creation, and pid-less records with stdout are still treated as live. Focused tests pass (4 passed). cost=$0.18
- 2026-09-06T03:10:54+00:00 dispatched revise run 20260906T031053Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~24640 tokens)
- 2026-09-06T03:37:01+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$0.06
- 2026-09-06T04:06:55+00:00 dispatched revise run 20260906T040653Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~25880 tokens)
