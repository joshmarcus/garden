---
id: CG-487
title: Collect terminal remote results after task completion
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/reap.py
- src/garden/runner/remote.py
- src/garden/runs.py
- tests/scheduler/test_dead_runs.py
branch: codex/collect-terminal-remote-results
pr: https://github.com/joshmarcus/context-garden/pull/388
attempts: 1
last_dispatched_at: '2026-09-09T19:27:37+00:00'
created: '2026-09-09T15:34:06+00:00'
updated: '2026-09-09T19:43:57+00:00'
---

## Goal

Close a remote run whose accepted result arrived after its task already became terminal,
without reopening the task or repeating publication, verification, review, or approval.

## Context

CG-432 run `20260909T010011Z-revise` has an accepted generation, exact pushed head,
`remote_result.json`, `final.md`, and exit code 0, but its run record remains `running` after
PR 337 merged the same head and marked the task done. Normal worker reaping visits only
running tasks, while the dangling-run sweep skips every remote runner. The Now page therefore
shows a historical result as current work and active-run accounting can retain it indefinitely.

Use the existing runner collection and event shapes. A terminal task is authoritative: this
cleanup only records the already accepted remote result and closes its run. Do not call normal
`finalize`, which can push, schedule checks/reviews, or transition the task. Require an exit
code or accepted remote result and the same immutable generation ownership used by the finish
endpoint. A stale or partial result must fail closed.

## Acceptance criteria

- [ ] The dangling sweep collects a completed remote run after its task is already terminal,
  persists result, usage, cost, model, error, exit code and `finished_at`, and emits exactly one
  terminal `run_finished` event.
- [ ] Collection never changes the terminal task, task state, branch, PR, approval, check or
  review ownership, and never invokes the normal publish/finalize path.
- [ ] Repeated sweeps are idempotent. An active current generation, a remote record without
  accepted completion output, and a stale or mismatched result remain untouched.
- [ ] Focused tests cover a task merged before remote finish collection, failed or cancelled
  terminal tasks, exact generation/result ownership, and repeated sweeps.

## Out of scope

- Reopening terminal tasks, re-running checks or review, pushing branches, merging PRs, or
  changing remote admission and lease semantics.
- Applying an operator-specific CG-432 metadata edit before this source passes independent
  review and is installed through the normal versioned release process.

## Log

- 2026-09-09T15:36:58+00:00 approved (cli)
- 2026-09-09T15:37:02+00:00 dispatched work run 20260909T153658Z-work via manual [human] (fresh session, base main, ~15176 tokens)
- 2026-09-09T15:51:00+00:00 external PR attached at codex/collect-terminal-remote-results; existing CI is PENDING
- 2026-09-09T16:02:55+00:00 automated review: approve — Terminal remote results are safely collected without re-entering task finalization, and stale, partial, owned, or nonterminal runs remain untouched. cost=$0.27
- 2026-09-09T17:54:32+00:00 automated review requested changes: Valid accepted remote completions are collected idempotently without changing terminal task/state ownership. However, a partial exit-code file is treated as a completed failed run instead of remaining untouched. cost=$0.39
- 2026-09-09T19:27:37+00:00 dispatched revise run 20260909T192732Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17021 tokens)
- 2026-09-09T19:29:58+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T19:31:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/388: Terminal remote collection now requires a non-empty, valid integer exit code, preventing partial completion files from closing runs as failed. Verified 61 focused scheduler tests pass and repository-wide Ruff is clean; no typechecker is configured. cost=$0.37
- 2026-09-09T19:33:46+00:00 automated review: approve — Terminal remote completions are collected idempotently without re-entering task finalization or changing terminal task ownership. Partial, malformed, stale-generation, owned, and nonterminal cases remain untouched. cost=$0.31
- 2026-09-09T19:42:24+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T19:43:57+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/388
