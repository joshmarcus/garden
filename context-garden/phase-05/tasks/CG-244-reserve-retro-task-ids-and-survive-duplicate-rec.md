---
id: CG-244
title: Reserve retro task IDs and survive duplicate records
status: failed
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
branch: garden/cg-244-reserve-retro-task-ids-and-survive-duplicate-rec
pr: https://github.com/joshmarcus/context-garden/pull/196
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: Running this phase's own retro can create colliding task IDs whose merge disables
  every page and tick, so postponing the fix would expose closure itself to the defect.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-06T01:58:54+00:00'
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-06T02:03:52+00:00'
---

## Goal

Reserve branch-filed IDs durably and atomically against all live task creators before writing retro drafts. Retain reservations across restart and define abandonment handling. Make duplicate IDs a surfaced validation failure that quarantines ambiguous tasks from dispatch while unrelated pages and ticks remain available. Test live creation between retro filing and PR merge.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: Running this phase's own retro can create colliding task IDs whose merge disables every page and tick, so postponing the fix would expose closure itself to the defect.

## Log

- 2026-09-05T23:15:10+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:58:00+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-05T23:59:48+00:00 approved by the retro reopen verdict
- 2026-09-06T00:01:27+00:00 dispatched work run 20260906T000113Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~5772 tokens)
- 2026-09-06T00:27:06+00:00 opened https://github.com/joshmarcus/context-garden/pull/196 (base main): Retro-filed task ids are now reserved durably and atomically in .garden/reservations.json (read by next_id and create_task under a shared lock) before the worktree drafts are written, so live creation between filing and merge never collides; and a duplicate id is quarantined out of dispatch and surfaced by validate/doctor/tick instead of raising and disabling every page and tick. cost=$7.75
- 2026-09-06T00:37:23+00:00 automated review: approve — Durable atomic id reservations and duplicate-id quarantine are implemented correctly, cover all live task creators, and are well tested (retro-vs-live-creation race, restart survival, abandonment reclaim, tick/validate/doctor surfacing); full suite and lint pass. cost=$0.81
- 2026-09-06T01:55:26+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/store.py); a rebase agent will resolve it
- 2026-09-06T01:58:54+00:00 dispatched rebase run 20260906T015853Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~6810 tokens)
- 2026-09-06T02:03:52+00:00 push failed: lease rejected on garden/cg-244-reserve-retro-task-ids-and-survive-duplicate-rec: expected origin at 163d31e2ab66, now at 99b4779f7fd8 cost=$0.47
