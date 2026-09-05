---
id: CG-192
title: garden.yaml is re-read each tick when it changes, and the Config page says which keys are live
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-03
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T10:31:17+00:00'
---

## Goal

**User value:** editing garden.yaml takes effect within one tick with the changed keys logged; the Config page names what is live so nobody restarts to be safe.

**Why now:** this was a phase-03 goal and definition-of-done item that did not ship and has no task in any phase; six of seven personas flagged it.

**Size:** medium. **Depends on:** nothing. Reload in Store.invalidate on mtime change, Scheduler reads store.config per tick, one test that a max_parallel change between two ticks is honoured.

## Context

Proposed at the context-garden/phase-03 retro. A promised item with no owner is the one thing every reviewer called out; it is small and unblocks unattended operation.

## Log

- 2026-09-05T10:31:17+00:00 approved (web)
