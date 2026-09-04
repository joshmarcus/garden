---
id: CG-091
title: State.save()'s file replacement is not atomic for concurrent readers
status: draft
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
updated: '2026-09-04T19:55:45+00:00'
---

`State.save()` in `src/garden/scheduler.py` does `self.path.write_text(...)`, which truncates the file before writing the new content. A concurrent `State.__init__` (e.g. from the web UI or an overlapping scheduler tick) reading the file mid-write can see a truncated/partial JSON payload, hit `JSONDecodeError`, and silently fall back to `{}` — losing all in-memory state for that reader, which is especially bad for in-flight trial metadata. Fix by writing to a temp file in the same directory and `os.replace()`'ing it into place (or by having readers take the same flock).

## Provenance

Discovered by CG-082 (Separate GARDEN_ROOT (guard) from the check-command venv path variable) during run `20260904T195040Z-revise`.

## Log

- 2026-09-04T19:55:45+00:00 discovered by CG-082
