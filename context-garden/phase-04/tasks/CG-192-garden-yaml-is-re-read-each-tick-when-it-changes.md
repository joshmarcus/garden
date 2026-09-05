---
id: CG-192
title: garden.yaml is re-read each tick when it changes, and the Config page says which keys are live
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
branch: garden/cg-192-garden-yaml-is-re-read-each-tick-when-it-changes
pr: https://github.com/joshmarcus/context-garden/pull/148
discovered_from: retro:context-garden/phase-03
attempts: 1
last_dispatched_at: '2026-09-05T12:34:08+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T13:16:02+00:00'
---

## Goal

**User value:** editing garden.yaml takes effect within one tick with the changed keys logged; the Config page names what is live so nobody restarts to be safe.

**Why now:** this was a phase-03 goal and definition-of-done item that did not ship and has no task in any phase; six of seven personas flagged it.

**Size:** medium. **Depends on:** nothing. Reload in Store.invalidate on mtime change, Scheduler reads store.config per tick, one test that a max_parallel change between two ticks is honoured.

## Context

Proposed at the context-garden/phase-03 retro. A promised item with no owner is the one thing every reviewer called out; it is small and unblocks unattended operation.

## Log

- 2026-09-05T10:31:17+00:00 approved (web)
- 2026-09-05T12:34:08+00:00 dispatched work run 20260905T123359Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4358 tokens)
- 2026-09-05T12:47:41+00:00 opened https://github.com/joshmarcus/context-garden/pull/148 (base main): garden.yaml (and its env/local overlays) is re-read in Store.invalidate on an mtime change, the scheduler picks up the reloaded config each tick and logs the changed keys, and the Config page names the live keys versus the RESTART_KEYS that still need a restart. cost=$4.42
- 2026-09-05T12:49:29+00:00 automated review: approve — Meets all four acceptance criteria with tests; Store reloads garden.yaml on mtime change, the scheduler re-reads store.config each tick via self.cfg, and the Config page names live vs RESTART_KEYS. Scope clean, docs updated, targeted tests and ruff pass. cost=$0.72
- 2026-09-05T13:16:02+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/148
