---
id: CG-243
title: Preserve task actions across concurrent ticks and moves
status: in_review
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
branch: garden/cg-243-preserve-task-actions-across-concurrent-ticks-an
pr: https://github.com/joshmarcus/context-garden/pull/194
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The action/tick split can silently discard user decisions and can turn a routine
  move into duplicate IDs that stop the entire garden.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-06T00:01:13+00:00'
created: '2026-09-05T23:15:09+00:00'
updated: '2026-09-06T00:22:40+00:00'
---

## Goal

Add concurrency control for task-file saves and moves, using a revision token or a lock with explicit merge/conflict semantics rather than trusting coarse timestamps. Reapply only intended fields and prevent stale saves from recreating a moved task. Test cancellation, priority and log edits interleaved with a tick, plus a move during transition; maintain the responsive action requirement.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The action/tick split can silently discard user decisions and can turn a routine move into duplicate IDs that stop the entire garden.

## Log

- 2026-09-05T23:15:09+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:57:59+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-05T23:59:48+00:00 approved by the retro reopen verdict
- 2026-09-06T00:01:13+00:00 dispatched work run 20260906T000059Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~5769 tokens)
- 2026-09-06T00:22:40+00:00 opened https://github.com/joshmarcus/context-garden/pull/194 (base main): Task-file saves now merge under a lock, reapplying only the fields a writer changed onto the current on-disk file, and a save whose file a concurrent move deleted is dropped rather than recreating a duplicate id. Adds tests for cancellation/priority/log edits interleaved with a tick and a move during a transition. cost=$4.74
