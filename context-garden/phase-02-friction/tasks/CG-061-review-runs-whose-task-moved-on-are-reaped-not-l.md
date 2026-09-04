---
id: CG-061
title: Review runs whose task moved on are reaped, not left running forever
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- context-garden/phase-01-bootstrap/specs/scheduler.md
branch: garden/cg-061-review-runs-whose-task-moved-on-are-reaped-not-l
pr: https://github.com/joshmarcus/context-garden/pull/47
attempts: 1
last_dispatched_at: '2026-09-04T21:14:13+00:00'
created: '2026-09-04T18:16:39+00:00'
updated: '2026-09-04T21:20:31+00:00'
---

## Goal

A review, persona or comparison run whose task has already moved on is reaped when it finishes, so the run record and the "Running now" list do not show it as running forever.

## Context

At the cut-over of the first live run, four review runs (CG-010, CG-032, CG-038, CG-055) had exit codes on disk and no process, yet their `run.json` said `running` and the Inbox listed them as workers for half an hour. Each task had transitioned (merged, sent back, re-reviewed) before the tick that would have read the verdict, and the reap only looks at `state[task].review_run`, which by then pointed elsewhere or at nothing. The tick should also sweep every run marked `running` whose `exit_code` exists or whose pid is gone, regardless of task state: record usage and cost, mark it `done` or `failed` with a note, and post the verdict only if the task is still where it was. They were closed by hand at the cut-over.

## Acceptance criteria

- [ ] a finished run that no task state points at is closed on the next tick with its usage recorded.
- [ ] "Running now" and `garden runs` never show a run whose process is gone and exit code is written.
- [ ] a test: start a review run, transition the task away, finish the run, tick, assert the record is closed.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T20:55:50+00:00 dispatched work run 20260904T205550Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3003 tokens)
- 2026-09-04T21:04:43+00:00 pre-PR checks failed (tests); no PR opened yet; revise run will fix cost=$4.35
- 2026-09-04T21:04:43+00:00 dispatched revise run 20260904T210443Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~3690 tokens)
- 2026-09-04T21:11:07+00:00 revision failed: no GARDEN_RESULT in worker output (see final.md)
- 2026-09-04T21:13:24+00:00 reset to ready by hand
- 2026-09-04T21:14:13+00:00 dispatched work run 20260904T211412Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3143 tokens)
- 2026-09-04T21:17:22+00:00 discovered work filed: CG-105
- 2026-09-04T21:17:51+00:00 opened https://github.com/joshmarcus/context-garden/pull/47 (base main): Verified and confirmed the existing commit (reap_orphaned sweep for review/persona/compare runs whose task moved on) is correct and complete: added test passes, full suite passes 219/3 skipped with GARDEN_ROOT unset, lint clean. No further code changes were needed. cost=$1.28
- 2026-09-04T21:20:31+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/47
