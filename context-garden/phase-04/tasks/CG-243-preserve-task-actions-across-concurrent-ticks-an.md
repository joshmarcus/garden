---
id: CG-243
title: Preserve task actions across concurrent ticks and moves
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The action/tick split can silently discard user decisions and can turn a routine
  move into duplicate IDs that stop the entire garden.
retro_blocking: true
created: '2026-09-05T23:15:09+00:00'
updated: '2026-09-05T23:15:09+00:00'
---

## Goal

Add concurrency control for task-file saves and moves, using a revision token or a lock with explicit merge/conflict semantics rather than trusting coarse timestamps. Reapply only intended fields and prevent stale saves from recreating a moved task. Test cancellation, priority and log edits interleaved with a tick, plus a move during transition; maintain the responsive action requirement.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The action/tick split can silently discard user decisions and can turn a routine move into duplicate IDs that stop the entire garden.

## Log

- 2026-09-05T23:15:09+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
