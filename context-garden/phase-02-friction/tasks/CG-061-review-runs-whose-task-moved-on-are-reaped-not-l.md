---
id: CG-061
title: Review runs whose task moved on are reaped, not left running forever
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- context-garden/phase-01-bootstrap/specs/scheduler.md
created: '2026-09-04T18:16:39+00:00'
updated: '2026-09-04T18:41:38+00:00'
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
