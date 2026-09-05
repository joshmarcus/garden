---
id: CG-144
title: A superseded review run is closed when a newer review starts; no run record outlives its process
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/runs.py
- tests/test_scheduler.py
created: '2026-09-05T02:28:49+00:00'
updated: '2026-09-05T03:19:58+00:00'
---

## Goal

When a second review is dispatched for a task while an earlier one is still running (a person pressed "one more review" after a push, or the poll re-reviewed a new push), the earlier run is closed as superseded, its process stopped, and its verdict ignored. More generally, a run record whose process has exited is reaped on the next tick whatever pointer the task holds, so no record stays `running` with no process behind it.

## Context

Found on the last PR of the first live run. CG-079 had a review dispatched at 02:11 on the pre-rebase push; its rebase pushed at 02:17 and a second review was pressed at 02:18. The second review approved; the first one's process finished unreaped because `reap_review` follows the task's `review_run` pointer (now the second run) and the orphan sweep (CG-116) only closes runs of tasks that moved on. The stale record kept `running`, automerge held on "a run is in flight" for ten minutes, and the person edited the run record by hand. Rule: dispatching a review for a task with a review already running first closes the older run (kill the process, status `superseded`, cost recorded); and the reap loop walks every `running` record, not only the ones a task points at, closing any whose process is gone with the exit code it left.

## Acceptance criteria

- [ ] dispatching a second review closes the first as `superseded` and stops its process; a test with the fake harness.
- [ ] a `running` record whose pid is gone is closed on the next tick with a log line; a test seeds one.
- [ ] automerge is not held by a superseded or dead run.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T02:30:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:01:34+00:00 approved (web)
- 2026-09-05T03:05:55+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:58+00:00 approved (web)
