---
id: CG-322
title: A _TaskState written with dict.update or |= is not saved
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/state.py
- tests/test_state.py
discovered_from: CG-308
created: '2026-09-06T03:36:56+00:00'
updated: '2026-09-06T13:20:31+00:00'
---

## Goal

`scheduler/state.py`'s `_TaskState` tracks dirty keys through `__setitem__`, `pop` and `setdefault`, so `st.update({...})` or `st |= {...}` changes the in-memory dict but `State.save()` never writes those keys. Either override `update` (and `__ior__`, `clear`) to mark keys written, or make the class refuse them with a clear error.

## Context

Found while writing the Now 1 tests: a merge-queue head set with `update` never reached state.json. No production code path uses `update` today, but the next one will lose a write silently.

## Provenance

Discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) during run `20260906T025753Z-work`.

## Log

- 2026-09-06T03:36:56+00:00 discovered by CG-308

## Acceptance criteria

- [ ] All supported dict mutators persist their changes through State.save and retain concurrent disjoint updates; regression tests cover update, |= and deletion via clear. Unsupported mutators fail explicitly rather than silently losing writes.
- 2026-09-06T13:20:31+00:00 approved (cli)
