---
id: CG-090
title: State.save() never clears dirty keys after a successful write
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
branch: garden/cg-090-state-save-never-clears-dirty-keys-after-a-succe
discovered_from: CG-082
attempts: 1
last_dispatched_at: '2026-09-04T21:24:18+00:00'
created: '2026-09-04T19:55:45+00:00'
updated: '2026-09-04T21:24:18+00:00'
---

In `src/garden/scheduler.py`, `_TaskState` (from CG-053) marks keys dirty on write/mutation-prone read, and `State.save()` merges only dirty keys into the on-disk file — but never clears the in-memory dirty set after a successful save. Every subsequent `save()` call re-writes all previously-dirty keys with their current in-memory values, which can silently clobber a concurrent writer's later update to the same key. Needs a fix in `State.save()` to clear each `_TaskState`'s dirty set (or just the keys it wrote) after the write succeeds.

## Provenance

Discovered by CG-082 (Separate GARDEN_ROOT (guard) from the check-command venv path variable) during run `20260904T195040Z-revise`.

## Log

- 2026-09-04T19:55:45+00:00 discovered by CG-082
- 2026-09-04T20:16:13+00:00 approved (web)
- 2026-09-04T20:55:51+00:00 dispatched work run 20260904T205550Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8496 tokens)
- 2026-09-04T20:58:55+00:00 pre-PR checks failed (tests, lint); no PR opened yet; revise run will fix cost=$1.24
- 2026-09-04T20:58:56+00:00 dispatched revise run 20260904T205855Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8723 tokens)
- 2026-09-04T21:03:37+00:00 discovered work filed: CG-097
- 2026-09-04T21:03:39+00:00 pre-PR checks failed (tests); no PR opened yet; revise run will fix cost=$1.30
- 2026-09-04T21:05:43+00:00 dispatched revise run 20260904T210543Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~9261 tokens)
- 2026-09-04T21:10:52+00:00 discovered work filed: CG-101
- 2026-09-04T21:11:00+00:00 pre-PR checks failed (tests); no PR opened yet; revise run will fix cost=$1.39
- 2026-09-04T21:19:42+00:00 reset to ready by hand
- 2026-09-04T21:24:18+00:00 dispatched work run 20260904T212417Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8723 tokens)
