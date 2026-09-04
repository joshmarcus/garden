---
id: CG-093
title: Store.save() for task files has the same non-atomic write_text pattern
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
discovered_from: CG-091
created: '2026-09-04T20:59:56+00:00'
updated: '2026-09-04T21:00:32+00:00'
---

`Store.save()` in `src/garden/store.py` does `task.path.write_text(task.render())`, the same truncate-before-write pattern this task fixed in `State.save()`. A concurrent reader of a task file (e.g. the web UI or another scheduler tick calling `Store._load_task`) could in principle observe a truncated task markdown file and fail to parse it. Worth the same temp-file + os.replace() treatment if it's judged in scope, but it's a different code path (task frontmatter files, not state.json) and wasn't part of this task's brief.

## Provenance

Discovered by CG-091 (State.save()'s file replacement is not atomic for concurrent readers) during run `20260904T205551Z-work`.

## Log

- 2026-09-04T20:59:56+00:00 discovered by CG-091
- 2026-09-04T21:00:32+00:00 approved (web)
