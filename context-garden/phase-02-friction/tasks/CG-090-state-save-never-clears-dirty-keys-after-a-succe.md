---
id: CG-090
title: State.save() never clears dirty keys after a successful write
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
discovered_from: CG-082
created: '2026-09-04T19:55:45+00:00'
updated: '2026-09-04T20:16:13+00:00'
---

In `src/garden/scheduler.py`, `_TaskState` (from CG-053) marks keys dirty on write/mutation-prone read, and `State.save()` merges only dirty keys into the on-disk file — but never clears the in-memory dirty set after a successful save. Every subsequent `save()` call re-writes all previously-dirty keys with their current in-memory values, which can silently clobber a concurrent writer's later update to the same key. Needs a fix in `State.save()` to clear each `_TaskState`'s dirty set (or just the keys it wrote) after the write succeeds.

## Provenance

Discovered by CG-082 (Separate GARDEN_ROOT (guard) from the check-command venv path variable) during run `20260904T195040Z-revise`.

## Log

- 2026-09-04T19:55:45+00:00 discovered by CG-082
- 2026-09-04T20:16:13+00:00 approved (web)
