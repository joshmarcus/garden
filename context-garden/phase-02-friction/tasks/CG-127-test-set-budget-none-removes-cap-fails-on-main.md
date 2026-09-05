---
id: CG-127
title: test_set_budget_none_removes_cap fails on main
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/config.py
branch: garden/cg-127-test-set-budget-none-removes-cap-fails-on-main
pr: https://github.com/joshmarcus/context-garden/pull/89
discovered_from: CG-074
attempts: 1
last_dispatched_at: '2026-09-05T00:08:37+00:00'
created: '2026-09-05T00:04:19+00:00'
updated: '2026-09-05T00:17:10+00:00'
---

`tests/test_coordination.py::test_set_budget_none_removes_cap` fails on unmodified origin/main (4d3199b) with `assert 0 == 2` on the second tick after `sched.retry(t)` — looks like retry() routes a task with an open PR into the revise/CHANGES_REQUESTED path instead of a fresh dispatch, and the second tick's revise dispatch isn't happening as the test expects. Unrelated to CG-074; worth a dedicated task.

## Provenance

Discovered by CG-074 (Reviews do not consume worker slots) during run `20260904T235956Z-revise`.

## Log

- 2026-09-05T00:04:19+00:00 discovered by CG-074
- 2026-09-05T00:07:57+00:00 approved (web)
- 2026-09-05T00:07:57+00:00 priority 2 -> 0 (web)
- 2026-09-05T00:08:37+00:00 dispatched work run 20260905T000828Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4714 tokens)
- 2026-09-05T00:14:16+00:00 opened https://github.com/joshmarcus/context-garden/pull/89 (base main): retry() reset a RUNNING task to READY without cancelling its active run; a finished-but-unreaped run stayed 'running' and held a max_parallel slot, so the freshly-readied task never dispatched. Extracted cancel()'s kill-and-mark logic into _cancel_active_run() and called it from retry()'s reset path. cost=$1.34
- 2026-09-05T00:15:42+00:00 automated review: approve — Small, correct fix: retry() on a still-RUNNING task now cancels its unreaped run so the freed slot lets dispatch proceed, extracting cancel()'s logic into a shared _cancel_active_run() helper. Tests and lint pass; PR description is clear and scar-free. cost=$0.37
- 2026-09-05T00:17:10+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/89
