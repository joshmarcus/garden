---
id: CG-535
title: Preserve maintenance requests across stale scheduler reads
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/budget.py
- src/garden/scheduler/state.py
- src/garden/scheduler/__init__.py
- docs/architecture.md
branch: garden/cg-535-preserve-maintenance-requests-across-stale-sched
pr: https://github.com/joshmarcus/context-garden/pull/441
discovered_from: retro:context-garden/phase-05
freeze_exception: true
freeze_exception_reason: A supposedly safe installation pause can disappear through observation, allowing
  scheduling to resume across a maintenance boundary.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T13:21:19+00:00'
created: '2026-09-10T13:10:36+00:00'
updated: '2026-09-10T13:40:08+00:00'
---

## Goal

Make maintenance inspection observational and reserve creation or modification of its durable entry for explicit state changes. Reproduce the stale tick reading absent maintenance, concurrent pause request and stale save sequence. Preserve ordinary pause state, quiescence and resume semantics.

## Context

Filed by the context-garden/phase-05 retro `reopen` verdict: it must land before the phase can close. Reason: A supposedly safe installation pause can disappear through observation, allowing scheduling to resume across a maintenance boundary.

## Acceptance criteria

- [ ] Reading absent maintenance state does not dirty a key or create a subsequently persisted maintenance entry.
- [ ] A concurrent maintenance-pause request survives a stale tick's later save.
- [ ] A subsequent tick observes the preserved request and follows the existing quiescence behavior.
- [ ] Explicit request, quiesce and resume actions remain persistent and focused concurrent-control regressions pass.

## Log

- 2026-09-10T13:10:36+00:00 filed by the context-garden/phase-05 retro reopen verdict (blocking)
- 2026-09-10T13:16:43+00:00 approved by the retro reopen verdict
- 2026-09-10T13:21:19+00:00 dispatched work run 20260910T132116Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~20926 tokens)
- 2026-09-10T13:23:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:25:16+00:00 opened https://github.com/joshmarcus/context-garden/pull/441 (base main): Maintenance reads are now observational, so a stale scheduler save preserves a concurrently requested maintenance pause. Focused scheduler/state tests (66 passed) and Ruff lint passed on commit 7db2a960. cost=$0.26
- 2026-09-10T13:26:45+00:00 automated review: approve — Absent maintenance reads are now observational, preventing stale scheduler saves from overwriting concurrent pause requests while preserving request, quiesce, and resume behavior. cost=$0.31
- 2026-09-10T13:40:08+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/441
