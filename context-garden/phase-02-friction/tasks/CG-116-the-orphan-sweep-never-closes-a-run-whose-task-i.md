---
id: CG-116
title: The orphan sweep never closes a run whose task is still running
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler.py
- tests/test_scheduler.py
branch: garden/cg-116-the-orphan-sweep-never-closes-a-run-whose-task-i
pr: https://github.com/joshmarcus/context-garden/pull/59
attempts: 1
last_dispatched_at: '2026-09-04T22:06:11+00:00'
created: '2026-09-04T21:56:41+00:00'
updated: '2026-09-04T22:18:35+00:00'
---

## Goal

The orphan sweep (CG-061) closes only review, persona and comparison runs whose task has genuinely moved on. A work, revise or resume run of a task that is still `running` is reaped by the normal path, with its result read, never swept.

## Context

Found on the first live run, twenty minutes after #47 went live. CG-098 (stacked on CG-090) was on a revise round; its worker finished at 21:54 with "no code changes required; the branch already satisfies the criteria" and a $3.35 cost. In the same tick the sweep closed that run with `error: "closed by orphan sweep: task moved on before this run's verdict was read"` and `orphaned: true`, before the reap read the result. The next tick found the task `running` with no active run and sent it back to `ready` ("no active run found"), which would have re-dispatched fresh work on a branch that already has PR #54. The person put it back to `in_review` by hand. The code shows why: `reap_orphaned` runs after the task reaps in the same tick and closes any run that `_finished_or_timed_out` says is finished and that no reap claimed above it, so a run that finishes between its task's reap and the sweep within one tick is swept on the spot. Fix the ordering or the condition: it should consider only runs with `mode` in (review, persona, compare), and only when the task's status is one where no verdict can be applied (done, cancelled, failed, or a PR that is closed or merged); a task in `running`, `changes_requested` or `in_review` with a finished run of its own is never an orphan. Write the rule next to the sweep and make the "no active run found" path record what happened to the run it expected, so the next time a run disappears the log says who closed it.

## Acceptance criteria

- [ ] a finished revise run of a `running` task is reaped normally; a test reproduces the CG-098 timing (run finishes in the same tick as the sweep).
- [ ] the sweep touches only review/persona/compare runs of tasks that have moved on; a test for each mode.
- [ ] "no active run found" logs the run id and its closer.

## Log

- 2026-09-04T22:06:11+00:00 dispatched work run 20260904T220610Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~6589 tokens)
- 2026-09-04T22:15:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/59 (base main): Scoped the orphan sweep to review/persona/compare runs whose task can no longer receive a verdict (terminal/failed/PR closed or merged), so a work/revise/resume run finishing in the same tick as the sweep is reaped normally instead of swept; also made the 'no active run found' reset log the run id and its closer. cost=$3.25
- 2026-09-04T22:18:35+00:00 automated review: approve — The sweep is correctly scoped to review/persona/compare runs of tasks whose verdict is moot, so a same-tick revise finish is reaped normally; all three acceptance criteria are met with per-mode tests, full suite (291 passed) and ruff are green. cost=$0.61
