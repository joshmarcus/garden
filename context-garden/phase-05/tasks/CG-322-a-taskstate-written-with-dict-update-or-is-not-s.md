---
id: CG-322
title: A _TaskState written with dict.update or |= is not saved
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- context-garden/phase-05/specs/now-page.md
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
- src/garden/web/templates/base.html
- src/garden/web/templates/board.html
- src/garden/web/templates/costs.html
- src/garden/web/templates/herbarium.html
- src/garden/web/templates/runs.html
- src/garden/web/pages/costs.py
- src/garden/web/pages/board.py
- src/garden/web/pages/trellis.py
- src/garden/charts.py
- src/garden/events.py
- src/garden/plants.py
- src/garden/scheduler/queue.py
- src/garden/web/app.py
- src/garden/web/common.py
discovered_from: CG-308
created: '2026-09-06T03:36:56+00:00'
updated: '2026-09-06T03:36:56+00:00'
---

## Goal

`scheduler/state.py`'s `_TaskState` tracks dirty keys through `__setitem__`, `pop` and `setdefault`, so `st.update({...})` or `st |= {...}` changes the in-memory dict but `State.save()` never writes those keys. Either override `update` (and `__ior__`, `clear`) to mark keys written, or make the class refuse them with a clear error.

## Context

Found while writing the Now 1 tests: a merge-queue head set with `update` never reached state.json. No production code path uses `update` today, but the next one will lose a write silently.

## Provenance

Discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) during run `20260906T025753Z-work`.

## Log

- 2026-09-06T03:36:56+00:00 discovered by CG-308
