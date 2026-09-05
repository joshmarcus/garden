---
id: CG-239
title: resolve_reading refuses absolute and parent paths, and the fence hashes the clone's git config
  and hooks
status: in_review
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/brief.py
- src/garden/scheduler/fence.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/reap.py
- src/garden/gitops.py
- tests/test_brief.py
- tests/scheduler/test_dispatch.py
branch: garden/cg-239-resolve-reading-refuses-absolute-and-parent-path
pr: https://github.com/joshmarcus/context-garden/pull/193
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: Goal 3 claims trust matches the mechanism and the phase runs overnight with automerge
  on for itself; the security persona verified on git 2.53 that a worker can execute code in the scheduler
  with the operator's credentials, and that a worker-filed task can inline the gh token into the next
  brief.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-05T23:45:29+00:00'
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:54:09+00:00'
---

## Goal

In resolve_reading refuse absolute paths and any resolved path not under its base, and report it in brief_gaps. At dispatch hash the clone's .git/config, its hooks directory, the worktree's .git file and .git/worktrees/<id>/, and at reap refuse to run any git in that clone if they changed. Run scheduler-side git with core.hooksPath pointed at an empty directory and core.fsmonitor=false via GIT_CONFIG_COUNT in the one gitops.git wrapper. Tests: a worktree config write is attributed and blocks git at reap; a ../ reading entry is a gap.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: Goal 3 claims trust matches the mechanism and the phase runs overnight with automerge on for itself; the security persona verified on git 2.53 that a worker can execute code in the scheduler with the operator's credentials, and that a worker-filed task can inline the gh token into the next brief.

## Acceptance criteria

- [ ] `resolve_reading` refuses an absolute path and any path that resolves outside its base, and reports each as a brief gap.
- [ ] At dispatch the fence hashes the clone's `.git/config`, its hooks directory, the worktree's `.git` file and `.git/worktrees/<id>/`; at reap, a change blocks every scheduler-side git command in that clone and is attributed on the task.
- [ ] Scheduler-side git runs with `core.hooksPath` at an empty directory and `core.fsmonitor=false` through `GIT_CONFIG_COUNT` in the one `gitops.git` wrapper.
- [ ] Tests: a worktree config write is attributed and blocks git at reap; a `../` reading entry is a gap; an absolute reading entry is a gap.

## Log

- 2026-09-05T23:05:56+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:10:30+00:00 approved (cli)
- 2026-09-05T23:12:33+00:00 dispatched work run 20260905T231218Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5584 tokens)
- 2026-09-05T23:40:40+00:00 opened https://github.com/joshmarcus/context-garden/pull/193 (base main): resolve_reading now refuses absolute/parent-escaping reading paths (reported as brief gaps), and the fence hash-checks a clone's .git/config, hooks dir, and worktree git-admin files at dispatch, blocking every scheduler-side git command in that clone at reap if they change; gitops.git now forces core.hooksPath/core.fsmonitor off via GIT_CONFIG_COUNT. cost=$4.15
- 2026-09-05T23:45:10+00:00 automated review requested changes: The reading-path fix and git-guard scaffolding work and are tested, but the hooksPath mitigation uses a shared, predictable, worker-writable temp directory that reopens the same hook-planting attack the task exists to close, and a fourth raw git subprocess call (path_at) bypasses both the block and the forced env. cost=$0.71
- 2026-09-05T23:45:29+00:00 dispatched revise run 20260905T234529Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~23897 tokens)
- 2026-09-05T23:54:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/193: Fixed both blocking review findings: core.hooksPath now points at a freshly created, unpredictable directory that is torn down immediately after each git call instead of a shared, worker-writable path, and path_at() now runs through the git() wrapper so it respects a blocked clone and the forced hooksPath/fsmonitor env like every other call site. cost=$0.86
