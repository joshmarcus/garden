---
id: CG-471
title: Make stale check recovery one guarded atomic action
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/human.py
- src/garden/inbox.py
- src/garden/web/actions/tasks.py
- tests/scheduler/test_human.py
branch: garden/cg-471-make-stale-check-recovery-one-guarded-atomic-act
pr: https://github.com/joshmarcus/context-garden/pull/372
attempts: 1
last_dispatched_at: '2026-09-09T14:53:32+00:00'
created: '2026-09-09T11:12:25+00:00'
updated: '2026-09-09T15:05:24+00:00'
---

## Goal

Make recovery from an exhausted or stale check continuation one guarded action. The action must reconcile the terminal `check_run` pointer and the task stop together, then resume to the correct pipeline state without the next terminal audit recreating the same Inbox card.

## Observed friction

The 2026-09-09 11:00 UTC Inbox sweep found `check_did_not_run` cards on CG-406 (`20260909T025423Z-check`), CG-437 (`20260909T033806Z-check`) and CG-434 (`20260909T044820Z-check`). A plain `garden resume` cleared `needs_human`, but left each collected terminal `check_run` pointer. The next audit recreated the same stop. The operator had to run `garden recover-check` and then choose resume or retry. CG-406 and CG-437 had fresh exact-head GitHub CI success and correctly resumed without implementation retries; CG-434 had genuine current CI failure plus preserved substantive feedback and correctly continued its existing branch after pointer recovery.

CG-374 broadly routed routine recovery to operator actions, but its own history shows repeated `check did not run` cards and does not provide this atomic stale-pointer disposition. CG-438 owns review-continuation lifecycle, not check resumption semantics.

## Acceptance criteria

- [ ] The Inbox, CLI and web expose one guarded action for a terminal `check_did_not_run` stop that clears or reconciles the exact stale `check_run` pointer and the matching `needs_human` stop atomically under scheduler/tick locking.
- [ ] Recovery chooses the correct continuation from durable evidence: resume without an implementation run only when there is nothing actionable; retain substantive pending feedback and current source/check failures for an existing-branch retry; keep a genuinely live check and its continuation untouched.
- [ ] A later tick or terminal audit cannot recreate the same stop from the recovered terminal pointer. Repeated invocation is safe and does not erase original run/result/error files, source identity, review provenance or current runs.
- [ ] The card explains whether it will resume pipeline progression or continue an existing revision. Do not present a plain `resume` action that is known to leave the terminal pointer behind.
- [ ] Focused regressions cover CG-406/CG-437-style exact-head-green recovery, CG-434-style substantive failure retention, a live check, mismatched/newer pointers, concurrent tick/action ordering and repeated invocation.

## Log

- 2026-09-09T11:00:00+00:00 filed from owner-requested full Inbox sweep after reproducing the resume-to-repeat-stop behavior on CG-406, CG-437 and CG-434.
- 2026-09-09T11:13:04+00:00 approved (cli)
- 2026-09-09T11:45:04+00:00 dispatched work run 20260909T114500Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~22647 tokens)
- 2026-09-09T11:52:38+00:00 preserved uncommitted worktree changes from run 20260909T114500Z-work outside the PR: `git stash apply ee1e1d8f37ffb1cafc1030d02520ec3413680ee0` in /home/joshua/work/worktrees/CG-471 (garden:CG-471:20260909T114500Z-work:reap)
- 2026-09-09T11:52:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:54:10+00:00 opened https://github.com/joshmarcus/context-garden/pull/372 (base main): Terminal check-stop recovery now uses the scheduler tick lock, reconciles only the matching terminal pointer and stop, preserves actionable feedback for revisions, and exposes the guarded action without unsafe resume/retry paths. Focused decision and web tests passed (134), and Ruff is clean. cost=$1.07
- 2026-09-09T11:56:43+00:00 automated review requested changes: The recovery works for the synthetic stale-pointer shape, but leaves ordinary `check_did_not_run` cards permanently stopped. cost=$0.44
- 2026-09-09T11:56:58+00:00 dispatched revise run 20260909T115655Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~23868 tokens)
- 2026-09-09T12:01:38+00:00 preserved uncommitted worktree changes from run 20260909T115655Z-revise outside the PR: `git stash apply 922506badc539c4e674769169bb4d90ce2b0845e` in /home/joshua/work/worktrees/CG-471 (garden:CG-471:20260909T115655Z-revise:reap)
- 2026-09-09T12:01:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:03:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/372: Recovered ordinary parked check stops by resolving the terminal run recorded in the durable stop when no newer check pointer exists. Verified focused decision, reap, and web suites plus Ruff. cost=$0.44
- 2026-09-09T12:05:56+00:00 automated review requested changes: Recovery correctly handles tested terminal and running cases, but can erase a genuinely active check during its requested/preparing lifecycle. cost=$0.55
- 2026-09-09T12:06:24+00:00 dispatched revise run 20260909T120621Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~23889 tokens)
- 2026-09-09T12:09:23+00:00 preserved uncommitted worktree changes from run 20260909T120621Z-revise outside the PR: `git stash apply a34c923bd2c789b0e5c602b3a0138b8e51b71b1a` in /home/joshua/work/worktrees/CG-471 (garden:CG-471:20260909T120621Z-revise:reap)
- 2026-09-09T12:09:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:09:26+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:09:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/372: Recovery now treats requested, preparing, and running check records as active, preserving their stop and continuation until terminal. Focused decision, web, and human-action tests passed; Ruff is clean. cost=$0.48
- 2026-09-09T12:13:27+00:00 automated review requested changes: The active requested/preparing lifecycle fix works and focused tests pass, but recovery can still erase a mismatched newer parked-check continuation. cost=$0.42
- 2026-09-09T12:14:16+00:00 dispatched revise run 20260909T121413Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~24614 tokens)
- 2026-09-09T12:16:37+00:00 preserved uncommitted worktree changes from run 20260909T121413Z-revise outside the PR: `git stash apply fc9a5a05d5e8431bd8a41c439cfbfd2753622b6d` in /home/joshua/work/worktrees/CG-471 (garden:CG-471:20260909T121413Z-revise:reap)
- 2026-09-09T12:16:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:17:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/372: Recovery now refuses to clear a recovery_check that points to a newer parked run than the terminal needs_human stop, preserving both records. Added a focused regression for the no-check_run newer parked-pointer shape; focused decision/web/human tests and Ruff passed. cost=$0.32
- 2026-09-09T12:20:37+00:00 automated review: approve — The guarded recovery correctly reconciles matching terminal check state, preserves newer or live continuations, and selects pipeline resume versus existing-branch revision from durable actionable evidence. cost=$0.49
- 2026-09-09T14:21:30+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_decisions.py); a rebase agent will resolve it
- 2026-09-09T14:30:11+00:00 dispatched rebase run 20260909T143007Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2592 tokens)
- 2026-09-09T14:31:12+00:00 preserved uncommitted worktree changes from run 20260909T143007Z-rebase outside the PR: `git stash apply ed9d3792c47bc53615ef8a338c06c012f3099f92` in /home/joshua/work/worktrees/CG-471 (garden:CG-471:20260909T143007Z-rebase:reap)
- 2026-09-09T14:33:48+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.01
- 2026-09-09T14:53:32+00:00 dispatched revise run 20260909T145328Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~24784 tokens)
- 2026-09-09T14:57:23+00:00 preserved uncommitted worktree changes from run 20260909T145328Z-revise outside the PR: `git stash apply 6176fd3671b04acb008d99c1337903044e7af163` in /home/joshua/work/worktrees/CG-471 (garden:CG-471:20260909T145328Z-revise:reap)
- 2026-09-09T14:57:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:58:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/372: Resolved the reported Ruff import-order failure in committed b38b29b06. Focused decision, human-action, and guarded Inbox recovery tests pass; required Ruff lint is clean. cost=$0.34
- 2026-09-09T15:03:47+00:00 automated review: approve — The guarded recovery correctly reconciles matching terminal check state, preserves live or newer continuations, and chooses pipeline progression versus existing-branch revision from durable actionable evidence. cost=$0.39
- 2026-09-09T15:05:24+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/372
