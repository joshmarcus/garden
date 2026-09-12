---
id: CG-534
title: Refuse destructive recovery from corrupt scheduler state
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/state.py
- src/garden/scheduler/__init__.py
- src/garden/scheduler/budget.py
- docs/architecture.md
branch: garden/cg-534-refuse-destructive-recovery-from-corrupt-schedul
pr: https://github.com/joshmarcus/context-garden/pull/442
discovered_from: retro:context-garden/phase-05
freeze_exception: true
freeze_exception_reason: Silent durable-state loss can remove safety controls and recovery intent, directly
  contradicting dependable operation.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T13:17:03+00:00'
created: '2026-09-10T13:10:36+00:00'
updated: '2026-09-10T13:57:54+00:00'
---

## Goal

Preserve malformed state bytes and fail closed for scheduling mutations instead of replacing corrupt JSON with an empty side-store. Cover initial loading and locked save-time rereads, including other state-writing recovery paths. Provide an actionable diagnosis and a deliberate recovery route without silently losing pauses, leases or continuation intent.

## Context

Filed by the context-garden/phase-05 retro `reopen` verdict: it must land before the phase can close. Reason: Silent durable-state loss can remove safety controls and recovery intent, directly contradicting dependable operation.

## Acceptance criteria

- [ ] Loading malformed existing state preserves its bytes and reports corruption instead of presenting an empty healthy store.
- [ ] If state becomes malformed between load and save, the mutation refuses to overwrite it and preserves the caller's pending changes for deliberate recovery.
- [ ] Scheduling and control mutations cannot proceed as if missing controls were defaults after a corruption diagnosis.
- [ ] Focused regressions cover initial corruption, save-time corruption and valid concurrent dirty-key merging without modifying live state.

## Log

- 2026-09-10T13:10:36+00:00 filed by the context-garden/phase-05 retro reopen verdict (blocking)
- 2026-09-10T13:16:43+00:00 approved by the retro reopen verdict
- 2026-09-10T13:17:03+00:00 dispatched work run 20260910T131702Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20935 tokens)
- 2026-09-10T13:25:11+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:26:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/442 (base main): Scheduler state loading, locked saves, and fence recovery now refuse malformed state without overwriting its bytes, while retaining pending in-memory mutations for deliberate recovery. Verified with 130 focused state, dispatch, and fence tests plus repository-wide Ruff lint. cost=$1.11
- 2026-09-10T13:29:36+00:00 automated review: approve — Corrupt scheduler state now fails closed across initial load, locked save rereads, and fence restoration while preserving disk bytes and pending mutations. cost=$0.39
- 2026-09-10T13:57:54+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/442
