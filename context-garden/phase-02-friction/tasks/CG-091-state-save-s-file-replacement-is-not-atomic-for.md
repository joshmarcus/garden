---
id: CG-091
title: State.save()'s file replacement is not atomic for concurrent readers
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
branch: garden/cg-091-state-save-s-file-replacement-is-not-atomic-for
pr: https://github.com/joshmarcus/context-garden/pull/45
discovered_from: CG-082
attempts: 1
last_dispatched_at: '2026-09-04T21:11:09+00:00'
created: '2026-09-04T19:55:45+00:00'
updated: '2026-09-04T21:18:57+00:00'
---

`State.save()` in `src/garden/scheduler.py` does `self.path.write_text(...)`, which truncates the file before writing the new content. A concurrent `State.__init__` (e.g. from the web UI or an overlapping scheduler tick) reading the file mid-write can see a truncated/partial JSON payload, hit `JSONDecodeError`, and silently fall back to `{}` — losing all in-memory state for that reader, which is especially bad for in-flight trial metadata. Fix by writing to a temp file in the same directory and `os.replace()`'ing it into place (or by having readers take the same flock).

## Provenance

Discovered by CG-082 (Separate GARDEN_ROOT (guard) from the check-command venv path variable) during run `20260904T195040Z-revise`.

## Log

- 2026-09-04T19:55:45+00:00 discovered by CG-082
- 2026-09-04T20:16:16+00:00 approved (web)
- 2026-09-04T20:55:51+00:00 dispatched work run 20260904T205551Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8506 tokens)
- 2026-09-04T20:59:56+00:00 discovered work filed: CG-093
- 2026-09-04T20:59:57+00:00 pre-PR checks failed (tests, lint); no PR opened yet; revise run will fix cost=$1.89
- 2026-09-04T20:59:58+00:00 dispatched revise run 20260904T205958Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8750 tokens)
- 2026-09-04T21:05:43+00:00 worker blocked: State.save() atomicity fix (commit 6937f02) is correct and complete; pytest (220 passed) and ruff are clean when run without the poisoned GARDEN_ROOT. The pre-PR check failure is unrelated to this diff: it's caused by the orchestrating garden's checks.pre_pr command for this product still referencing $GARDEN_ROOT for the venv path, which CG-082 made a guaranteed-nonexistent sentinel for check subprocesses. cost=$1.96
- 2026-09-04T21:10:52+00:00 reset to ready by hand
- 2026-09-04T21:11:09+00:00 dispatched work run 20260904T211108Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8755 tokens)
- 2026-09-04T21:13:11+00:00 discovered work filed: CG-103
- 2026-09-04T21:13:39+00:00 opened https://github.com/joshmarcus/context-garden/pull/45 (base main): State.save() in scheduler.py now writes state.json atomically: content goes to a per-PID temp file in the same directory, then os.replace() swaps it into place, so a concurrent State.__init__ reader can never observe a truncated file. Added tests covering no-leftover-temp-files and a concurrent-reader race via monkeypatched os.replace. cost=$0.58
- 2026-09-04T21:15:14+00:00 automated review: approve — State.save() now writes to a same-directory per-PID temp file and os.replace()s it into place, closing the truncation window for lock-free readers; well-tested and lint/tests clean. cost=$0.34
- 2026-09-04T21:18:57+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/45
