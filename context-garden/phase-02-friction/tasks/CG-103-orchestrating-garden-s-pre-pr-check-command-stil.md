---
id: CG-103
title: Orchestrating garden's pre-PR check command still resolves venv/tool paths via $GARDEN_ROOT for
  this product
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
discovered_from: CG-091
created: '2026-09-04T21:13:11+00:00'
updated: '2026-09-04T21:16:02+00:00'
---

CG-082 made `GARDEN_ROOT` a guaranteed-nonexistent sentinel for the environment passed to worker subprocesses (to stop workers from mutating the live garden). But the garden's own `checks.pre_pr` command configuration for the context-garden product still appears to reference `$GARDEN_ROOT` to locate the venv/tool path used to run pre-PR checks, so pre-PR checks fail immediately for every task in this product regardless of the actual diff. Fix: point the pre-PR check command at a fixed, known-good path (e.g. the product repo's own `.venv`) instead of `$GARDEN_ROOT`. This affected CG-091's first two dispatch rounds even though the code fix itself was correct both times.

## Provenance

Discovered by CG-091 (State.save()'s file replacement is not atomic for concurrent readers) during run `20260904T211108Z-work`.

## Log

- 2026-09-04T21:13:11+00:00 discovered by CG-091
- 2026-09-04T21:16:02+00:00 obsolete: the live garden.yaml already uses $GARDEN_EXEC_ROOT; the remaining piece (tests immune to GARDEN_ROOT) is CG-098/CG-101
