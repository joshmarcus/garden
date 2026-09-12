---
id: CG-483
title: Keep generated worker context out of tracked source files
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/snapshot.py
- tests/scheduler/test_reap.py
branch: codex/keep-generated-context-out-of-source
pr: https://github.com/joshmarcus/context-garden/pull/383
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T14:51:19+00:00'
created: '2026-09-09T14:51:17+00:00'
updated: '2026-09-09T15:21:39+00:00'
---

## Goal

Stop scheduler-generated live snapshots from dirtying tracked checkout files and interfering with worker rebases, commits, or recovery.

## Evidence

CG349 rebase20260909T144010Z began with git refusing unstaged docs/design/snapshot.json. Scheduler.dispatch calls write_snapshot after preparing a local worktree, including rebase mode; snapshot.py overwrites this tracked file. The worker correctly stashed/restored it and normal reap preserved it again. Owner reported the quoted restoration and requested root-cause repair.

## Acceptance criteria

- [ ] Generate live context in a run-scoped artifact outside tracked project source; never overwrite a project's existing docs/design/snapshot.json or other source file.
- [ ] Keep appropriate worker context available with an explicit brief reference while preserving current redaction and provenance. Do not inject unnecessary context into conflict-only rebases.
- [ ] Prove dispatch with an existing tracked snapshot leaves its bytes, index and git status unchanged, and that a rebase does not require stashing scheduler-generated source changes.
- [ ] Preserve existing worktrees, original snapshot contents, run artifacts and active workers. Correct source through a reviewed PR and validated release, not an installed-runtime patch.

## Log

- 2026-09-09T14:51:17+00:00 approved (owner-reported shared checkout corruption during root-cause repair)
- 2026-09-09T14:51:19+00:00 dispatched work run 20260909T145119Z-work via manual [human] (fresh session, base main, ~15690 tokens)
- 2026-09-09T15:21:39+00:00 external PR merged and verified on main
