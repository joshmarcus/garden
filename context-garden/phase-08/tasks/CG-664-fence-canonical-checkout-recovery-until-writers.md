---
id: CG-664
title: Fence canonical checkout recovery until writers stop
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-08/goals.md
- src/garden/canonical.py
- src/garden/scheduler/__init__.py
- tests/test_canonical.py
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T17:05:13+00:00'
---

## Goal

User value: retries cannot overlap a timed-out reconciliation writer and damage a shared checkout. Why now: the staff review's harmless probe and current exception path establish a concrete ownership gap. Size: hard. Dependencies: existing CG-406 checkout leases and process supervision. Terminate and reap owned descendants before releasing the lease; retain an actionable fenced state when cleanup cannot be confirmed.

## Context

Proposed at the context-garden/phase-07 retro. This closes a demonstrated data-integrity gap before users rely on opt-in canonical execution.

## Acceptance criteria

- [ ] On reconciliation timeout/cancellation, terminate and reap the owned command and descendants before releasing canonical checkout ownership; unrelated processes are unaffected.
- [ ] If cleanup cannot be confirmed, retain/quarantine the lease and present recoverable evidence. A retry cannot overlap a surviving writer; acknowledged shutdown permits normal recovery.
- [ ] Exercise the actual reconciliation/scheduler failure path with a harmless child writer, success control and uncertain-cleanup case. Preserve source, original failure and existing resource/deadline limits.

## Planning boundary

Retrospective draft in frozen Phase08; no implementation approval, runtime activation, private-data access, new workers or spending is implied. Address each outcome with meaningful observations; alternate evidence and reasoned criteria amendments are welcome. Preserve substantive findings and avoid process-only author rounds.
