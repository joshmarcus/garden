---
id: CG-102
title: State.save() in scheduler.py still not atomic
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
discovered_from: CG-093
created: '2026-09-04T21:11:00+00:00'
updated: '2026-09-04T21:12:57+00:00'
---

CG-093's brief says CG-091 already fixed the write_text()-truncation pattern in `State.save()` (scheduler.py), but on this branch's main, `State.save()` (scheduler.py:173) still does a plain `self.path.write_text(...)`. Either CG-091's PR hasn't merged yet, or its fix covered only the concurrent-writer flock/merge logic and not the on-disk atomicity of the final write. Worth re-checking CG-091's status/scope.

## Provenance

Discovered by CG-093 (Store.save() for task files has the same non-atomic write_text pattern) during run `20260904T210647Z-work`.

## Log

- 2026-09-04T21:11:00+00:00 discovered by CG-093
- 2026-09-04T21:12:57+00:00 cancelled (web)
