---
id: CG-478
title: Allow non-draft tasks to move into frozen phases
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler/human.py
- src/garden/scheduler/dispatch.py
- src/garden/store.py
- src/garden/web/actions/tasks.py
- tests/test_move.py
branch: garden/cg-478-allow-non-draft-tasks-to-move-into-frozen-phases
pr: https://github.com/joshmarcus/context-garden/pull/375
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T16:27:42+00:00'
created: '2026-09-09T12:52:35+00:00'
updated: '2026-09-09T17:06:11+00:00'
---

## Goal

Allow the user to move an existing non-draft task into a frozen phase without first converting it to a draft or temporarily unfreezing the destination. Freezing defers work; it should not discard the task's existing lifecycle state.

## Owner request

Feature: non-draft tasks can be moved into a frozen state. This follows moving the ready Spot task CG347 into frozen phase08. The current Scheduler.move rejects every non-draft task when the destination phase is already frozen.

## Acceptance criteria

- [ ] Allow moving non-draft tasks into an already frozen phase through the shared supported move operation, including CLI and web entry points. Remove the draft-only destination restriction rather than requiring an unfreeze/move/refreeze workaround.
- [ ] Preserve the task ID, lifecycle status, approval/review and failure history, round counts, source/branch/PR, dependencies, run records and useful artifacts. Moving into a frozen phase must not silently change ready/in-review/changes-requested work into a draft or reset its history.
- [ ] Keep the destination frozen throughout the move. Apply existing freeze gates to subsequent automatic work, including dispatch and relevant review/revise/rebase/merge paths. Moving alone must not create a freeze exception or resume work.
- [ ] Preserve safe active-run handling: retain the existing refusal or explicit safe deferral while a run or source writer is active. Do not kill a worker or discard active results merely to make the move succeed. Keep closed-phase and cross-product restrictions unless separately authorized.
- [ ] Show the preserved task status together with its frozen-phase hold clearly in the UI; explain why it will not run and keep the ordinary move history/event.
- [ ] Add proportionate regression coverage for a ready task and a PR-bearing non-draft task moved into a frozen phase, unchanged durable identity/history, refusal to start work afterward, and an active-run move refusal. Verify CLI/web use the same policy.

## Scope

Extend the existing phase-freeze and task-move implementation. Reuse Manual-mode lifecycle gating where applicable; do not create a second frozen-task status or alter the existing frozen phase08 or owner phase/task holds during implementation.

## Log

- 2026-09-09T12:52:35+00:00 approved (owner-requested non-draft moves into frozen phases, preserving lifecycle and active-work safety)
- 2026-09-09T13:20:42+00:00 dispatched work run 20260909T132042Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~18128 tokens)
- 2026-09-09T13:26:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:28:56+00:00 opened https://github.com/joshmarcus/context-garden/pull/375 (base main): Non-draft tasks can now move into frozen phases while retaining identity and lifecycle state; frozen-phase gates continue to prevent subsequent work. Verified focused move/freeze regressions (25 passed), lint, and source compilation on commit 0f2f6086. cost=$0.75
- 2026-09-09T13:31:35+00:00 automated review requested changes: The move and identity-preservation behavior works, but one automatic rebase path remains active for frozen tasks. cost=$0.32
- 2026-09-09T13:38:18+00:00 dispatched revise run 20260909T133818Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19140 tokens)
- 2026-09-09T13:44:40+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:47:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/375: Deferred stacked-child restacks now respect the shared frozen/closed phase gate, preserving the PR base and branch until unfreeze. Verified focused coordination and move coverage (39 passed), Ruff lint, and source compilation on commit a1d639e3. cost=$0.63
- 2026-09-09T15:01:12+00:00 automated review requested changes: Frozen tasks can still have stacked PRs automatically retargeted when the garden merges their parent, contradicting the claimed frozen hold. cost=$0.31
- 2026-09-09T15:04:15+00:00 dispatched revise run 20260909T150415Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19369 tokens)
- 2026-09-09T15:10:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:12:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/375: Frozen stacked children now retain their PR base and parent branch during parent automerge; restacking remains deferred until unfreeze. Verified with focused coordination and move tests (40 passed), Ruff, and source compilation. cost=$0.52
- 2026-09-09T15:20:57+00:00 automated review requested changes: Core move and stack-freeze behavior passes, but frozen PR tasks can still launch new automated work through two paths. cost=$0.58
- 2026-09-09T15:21:11+00:00 dispatched revise run 20260909T152111Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19855 tokens)
- 2026-09-09T15:27:26+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:31:31+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/375: Frozen PR tasks now retain CI failure facts while deferring detached CI analysis until unfreeze, and persona reviews share the frozen/closed dispatch gate and are hidden while held. Verified on commit 0059eab3 with focused tests (53 passed), Ruff, and source compilation. cost=$0.46
- 2026-09-09T15:40:49+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: add proportionate regression coverage; run `garden triage CG-478 --changes "<feedback>" to unblock`
- 2026-09-09T15:43:42+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T15:45:03+00:00 dispatched revise run 20260909T154503Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~20174 tokens)
- 2026-09-09T15:50:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:52:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/375: Frozen model-trial restarts now share the phase refusal before any destructive reset, and held task pages omit the trial action. Verified focused move/freeze/trial coverage (27 passed), broader extras/web coverage (validation receipt exit 0), Ruff, and source compilation. cost=$0.45
- 2026-09-09T15:52:32+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py, src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-09T15:52:32+00:00 dispatched rebase run 20260909T155232Z-rebase-2 via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2562 tokens)
- 2026-09-09T16:13:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/375: Rebased CG-478 onto origin/main and resolved scheduler conflicts while preserving both main and branch behavior. cost=$0.02
- 2026-09-09T16:16:15+00:00 automated review requested changes: Moving ready and PR-bearing tasks into frozen phases preserves durable state, and automatic dispatch/restack/merge paths are held. However, direct automated-review requests mutate held task state before being refused. cost=$0.34
- 2026-09-09T16:16:28+00:00 dispatched revise run 20260909T161627Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~20390 tokens)
- 2026-09-09T16:20:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T16:23:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/375: Frozen PR review requests now preserve review counters and needs-human state before refusal. Verified focused move and review-cap tests, Ruff, and source compilation. cost=$0.51
- 2026-09-09T16:27:24+00:00 automated review requested changes: Frozen-phase moves and scheduler holds work, but the task page mislabels closed-phase holds as frozen. cost=$0.59
- 2026-09-09T16:27:42+00:00 dispatched revise run 20260909T162740Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~20590 tokens)
- 2026-09-09T16:33:42+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T16:39:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/375: Closed phases now display “Held by closed phase,” while frozen holds retain their frozen label. Verified 74 focused tests, Ruff, and source compilation on commit 2d3d2f56. cost=$0.31
- 2026-09-09T17:04:24+00:00 automated review: approve — Non-draft tasks can move into frozen phases without resetting durable state, while automatic work remains held. Frozen and closed phase holds are labeled accurately in the task UI. cost=$0.67
- 2026-09-09T17:06:11+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/375
