---
id: CG-254
title: redispatch kills the superseded worker, and pin runs the canary, installs and restarts after a
  tick
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: medium
reading:
- src/garden/runs.py
- src/garden/gitops.py
- src/garden/harness.py
- tests/test_cli.py
harness: codex
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:10+00:00'
updated: '2026-09-06T00:50:43+00:00'
---

## Goal

**User value:** the two recurring operator hand sequences become one command each; re-dispatching from codex to fable left two workers in one worktree and cost $4.34 for a run with no PR.

**Why now:** both were done by hand several times this phase and each is a known failure mode.

**Size:** medium. **Depends on:** CG-180, CG-198 (merged).

## Context

Proposed at the context-garden/phase-04 retro. Operator hand steps are the operator-spend goal in another form.

## Acceptance criteria

- [ ] `garden redispatch <task_id>` kills any run still active for that task (via `Run.kill`/`RunStore.active` in `src/garden/runs.py`) before starting the new one, so switching harnesses mid-task never leaves two workers in one worktree — proven by `tests/test_scheduler.py::test_redispatch_kills_active_run`.
- [ ] `garden redispatch` reuses the task's existing worktree and branch instead of the hand sequence of killing a worker and then calling `dispatch --force`, following the same dispatch path as `src/garden/cli.py`'s `dispatch` command.
- [ ] `garden pin <sha>` runs a canary check against the new commit and refuses to install if the canary fails.
- [ ] `garden pin <sha>` installs the new commit and restarts the scheduler only after the in-flight tick finishes, never mid-tick — proven by `tests/test_cli.py::test_pin_waits_for_tick_before_restart`.
- [ ] Both commands appear in the CLI help text alongside the existing `dispatch`/`doctor` commands in `src/garden/cli.py`.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-243 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:24:19+00:00 integrated 1 suggestion(s) (run 20260906T002109Z-edit) cost=$0.35
- 2026-09-06T00:50:43+00:00 approved (cli)
