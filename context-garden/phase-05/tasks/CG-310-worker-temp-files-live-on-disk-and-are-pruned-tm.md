---
id: CG-310
title: 'Worker temp files live on disk and are pruned: TMPDIR under the work root, per-run cleanup at
  reap, and a sweep of finished tasks'' worktree venvs and caches'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/runner/local.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/reap.py
- src/garden/checkrun.py
- src/garden/config.py
- examples/garden.work.yaml
- docs/worker-protocol.md
branch: garden/cg-310-worker-temp-files-live-on-disk-and-are-pruned-tm
pr: https://github.com/joshmarcus/context-garden/pull/209
attempts: 1
last_dispatched_at: '2026-09-06T02:39:04+00:00'
created: '2026-09-06T01:45:39+00:00'
updated: '2026-09-06T03:08:02+00:00'
---

## Goal

A garden running for a day does not fill the machine's temp space. Every worker, check and setup run gets `TMPDIR` under the garden's work root on disk (`<work>/tmp/<run id>`), the directory is removed when the run is reaped, and a periodic sweep (each tick, cheap) removes the `.venv`, `.pytest_cache` and `__pycache__` of worktrees whose task is done or cancelled, and the worktree itself after a configurable age. `garden doctor` reports free space on the work root and on `/tmp` and warns under a threshold.

## Context

2026-09-06 01:10Z: `/tmp` on the operator's WSL machine is a 3.9 GB RAM-backed tmpfs. Pytest temp directories from hundreds of check runs, a worker's own `/tmp/cg291-pytest` (334 MB), stale trial venvs (`/tmp/cg030venv`, 111 MB) and the scratch directories Claude Code keeps per worker session filled it while 11 GB of a 1 TB disk were in use. Every process that opens a file under `/tmp` then failed with ENOSPC, including the operator's own shell, and the owner had to clear it by hand. The root cause is that nothing routes worker temp to disk or prunes it; the fix belongs to the runner and the reaper, not to the operator.

## Acceptance criteria

- [ ] `LocalRunner.start`, check runs and setup runs export `TMPDIR` (and `PYTEST_DEBUG_TEMPROOT`) as `<work root>/tmp/<run id>`, created before the process starts and removed at reap; a test asserts the env and the cleanup with the fake harness.
- [ ] A tick-time sweep removes `.venv`, `.pytest_cache` and `__pycache__` under worktrees whose task is `done` or `cancelled`, and removes such a worktree entirely after `worktrees.keep_days` (default 2); a test creates a done task's worktree with a venv and sees it pruned.
- [ ] `garden doctor` prints free space for the work root and `/tmp` and warns below `doctor.min_free_mb` (default 2048); the operate skill names the check.
- [ ] Nothing a running run uses is removed: the sweep skips any worktree with an active run, and the test covers it.

## Log

- 2026-09-06T01:45:39+00:00 approved (cli)
- 2026-09-06T02:39:04+00:00 dispatched work run 20260906T023849Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~21460 tokens)
- 2026-09-06T03:01:57+00:00 opened https://github.com/joshmarcus/context-garden/pull/209 (base main): Worker, setup, and check temporary files now use disk-backed per-run directories under the work root and are cleaned after reap. Terminal worktree caches are pruned conservatively, aged worktrees are removed, and doctor reports free space. cost=$2.16
- 2026-09-06T03:05:47+00:00 description rewritten by the reviewer cost=$0.33
- 2026-09-06T03:05:59+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-06T03:08:02+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/209
