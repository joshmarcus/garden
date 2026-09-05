---
id: CG-244
title: Reserve retro task IDs and survive duplicate records
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: Running this phase's own retro can create colliding task IDs whose merge disables
  every page and tick, so postponing the fix would expose closure itself to the defect.
retro_blocking: true
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:58:00+00:00'
---

## Goal

Reserve branch-filed IDs durably and atomically against all live task creators before writing retro drafts. Retain reservations across restart and define abandonment handling. Make duplicate IDs a surfaced validation failure that quarantines ambiguous tasks from dispatch while unrelated pages and ticks remain available. Test live creation between retro filing and PR merge.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: Running this phase's own retro can create colliding task IDs whose merge disables every page and tick, so postponing the fix would expose closure itself to the defect.

## Log

- 2026-09-05T23:15:10+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:58:00+00:00 moved from context-garden/phase-04 to context-garden/phase-05
