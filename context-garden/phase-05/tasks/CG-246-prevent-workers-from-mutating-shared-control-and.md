---
id: CG-246
title: Prevent workers from mutating shared control and harness state
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The reported remaining write paths can forge approval evidence or execute code
  in later operator sessions, undermining the phase's trust guarantees even after git and reload fixes.
retro_blocking: true
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:59:48+00:00'
---

## Goal

Provide per-worker harness configuration containing only required authentication material instead of writable operator config directories. Enforce write separation for live task files, scheduler state, sibling run outputs and audit evidence, including shell redirects; place work directories outside control storage. If recovery restores state, preserve scheduler-owned concurrent updates rather than overwriting the whole snapshot. Demonstrate that a worker cannot plant operator-session hooks, forge sibling approvals or replace another run's completion evidence.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The reported remaining write paths can forge approval evidence or execute code in later operator sessions, undermining the phase's trust guarantees even after git and reload fixes.

## Log

- 2026-09-05T23:15:10+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:58:00+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-05T23:59:48+00:00 approved by the retro reopen verdict
