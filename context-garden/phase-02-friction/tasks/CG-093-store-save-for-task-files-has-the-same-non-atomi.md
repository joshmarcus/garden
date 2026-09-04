---
id: CG-093
title: Store.save() for task files has the same non-atomic write_text pattern
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
branch: garden/cg-093-store-save-for-task-files-has-the-same-non-atomi
pr: https://github.com/joshmarcus/context-garden/pull/46
discovered_from: CG-091
attempts: 2
last_dispatched_at: '2026-09-04T21:11:09+00:00'
created: '2026-09-04T20:59:56+00:00'
updated: '2026-09-04T21:18:58+00:00'
---

`Store.save()` in `src/garden/store.py` does `task.path.write_text(task.render())`, the same truncate-before-write pattern this task fixed in `State.save()`. A concurrent reader of a task file (e.g. the web UI or another scheduler tick calling `Store._load_task`) could in principle observe a truncated task markdown file and fail to parse it. Worth the same temp-file + os.replace() treatment if it's judged in scope, but it's a different code path (task frontmatter files, not state.json) and wasn't part of this task's brief.

## Provenance

Discovered by CG-091 (State.save()'s file replacement is not atomic for concurrent readers) during run `20260904T205551Z-work`.

## Log

- 2026-09-04T20:59:56+00:00 discovered by CG-091
- 2026-09-04T21:00:32+00:00 approved (web)
- 2026-09-04T21:06:47+00:00 dispatched work run 20260904T210647Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8494 tokens)
- 2026-09-04T21:11:07+00:00 no active run found; back to ready
- 2026-09-04T21:11:09+00:00 dispatched work run 20260904T211109Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8684 tokens)
- 2026-09-04T21:14:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/46 (base main): Store.save() already had the atomic temp-file + os.replace() fix committed on this branch from a prior interrupted run of this same task; verified the change matches the task, all 221 tests pass, and lint is clean. No new commits were needed. cost=$0.57
- 2026-09-04T21:15:15+00:00 automated review: approve — Store.save() now writes task files atomically via a temp-file + os.replace() helper mirroring the CG-091 fix, with tests covering content, no leftover temp files, and the failure path. Diff is minimal, correct, and in scope. cost=$0.33
- 2026-09-04T21:18:58+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/46
