---
id: CG-473
title: Reserve a task in Manual mode from automatic actions
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- context-garden/product.md
- docs/architecture.md
- docs/design.md
- docs/worker-protocol.md
branch: garden/cg-473-reserve-a-task-in-manual-mode-from-automatic-act
pr: https://github.com/joshmarcus/context-garden/pull/368
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T15:39:35+00:00'
created: '2026-09-09T11:13:16+00:00'
updated: '2026-09-09T15:55:13+00:00'
---

## Goal

Let an operator or person mark a task as **Manual** so Garden observes it but does not perform automatic lifecycle actions while someone resolves it directly.

`runner: manual` is not this mode: it selects a manual authoring route, but the scheduler can still revise, review, rebase, merge, recover, or otherwise advance the task automatically. Manual mode is an explicit reservation across the whole task lifecycle.

## Acceptance criteria

- [ ] Add a visible, compact Manual mode and guarded action on the task page and in appropriate Inbox/task controls. Record who reserved it (`operator` or a human owner) and an optional short note with durable history.
- [ ] Once Manual mode is active, suppress new automatic work, revision, review/persona, check/recovery dispatch, rebase, and merge actions for that task. Read-only polling, status display, logs, PR/check observation, and evidence inspection continue.
- [ ] Enabling Manual mode never kills, cancels, supersedes, or steals an active run. Show the active work honestly and apply the reservation at the safe lifecycle boundary; require an explicit separately guarded stop/cancel action if interruption is desired.
- [ ] Provide an explicit **Return to automation** action that checks current task/run/PR/head state under the scheduler lock, refuses stale or unsafe requests, preserves source/history/results, and resumes through the normal supported state rather than inventing approval or rerunning completed work.
- [ ] Manual mode composes with existing task-specific automerge opt-outs, phase holds, freezes, dependency blocks, troubled-task investigations, runner selection, and ownership. Entering or leaving Manual mode must not clear or overwrite any separate hold, approval, review finding, runner setting, or automerge policy.
- [ ] CLI/API and web actions share the authoritative transition, are retry-safe, and expose an accessible state/action in narrow and desktop task UI. Tests cover active work, stale concurrent actions, all suppressed lifecycle modes, direct observation while reserved, and safe return.

## Scope

Build on existing ownership, Inbox action, task transition, and operator-investigation patterns (including CG-410, CG-414, and CG-437). Keep execution routing (`runner`) separate from the new lifecycle reservation. Do not implement a general permissions system or change unrelated holds.

## Log

- 2026-09-09T11:13:16+00:00 approved (owner)
- 2026-09-09T11:13:37+00:00 dispatched work run 20260909T111337Z-work-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15433 tokens)
- 2026-09-09T11:31:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:33:24+00:00 opened https://github.com/joshmarcus/context-garden/pull/368 (base main): Added a durable, lock-serialized Manual mode reservation that preserves active work, suppresses new automatic lifecycle actions, continues observation, and returns safely through existing lifecycle state. Verified focused scheduler, CLI, and web behavior plus final lint on commit 1adf43c2. cost=$4.32
- 2026-09-09T11:39:43+00:00 automated review requested changes: Manual mode does not correctly settle active work at its safe boundary. Finished worker runs remain permanently active, and active review/edit results can still advance or mutate the task while reserved. cost=$0.34
- 2026-09-09T11:39:58+00:00 dispatched revise run 20260909T113958Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16790 tokens)
- 2026-09-09T11:51:18+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:52:46+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Fixed Manual mode safe-boundary handling so active worker, review, persona, edit, and check runs can finish and release capacity while their state-changing continuations remain parked. Verified guarded return resumes those continuations through normal scheduler paths; 275 affected tests and a final 132-test lifecycle selection passed, with Ruff and git diff checks clean on commit 322db8b5. cost=$1.80
- 2026-09-09T11:55:28+00:00 automated review requested changes: Manual mode still permits two automatic lifecycle mutations during observation/cleanup, so the reservation is not comprehensive. cost=$0.58
- 2026-09-09T11:55:41+00:00 dispatched revise run 20260909T115540Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16974 tokens)
- 2026-09-09T12:01:40+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:03:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Manual mode now observes terminal PR and dead-run conditions without applying lifecycle mutations. Guarded return resumes the existing merge/close or retry/failure path; committed as c6db17d5 after 234 scheduler tests passed and Ruff completed cleanly. cost=$1.01
- 2026-09-09T12:05:58+00:00 automated review requested changes: Manual mode still fails to reserve active model trials at their safe boundary. cost=$0.39
- 2026-09-09T12:06:25+00:00 dispatched revise run 20260909T120624Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17231 tokens)
- 2026-09-09T12:13:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:15:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Manual mode now safely reserves model trials: active contenders are not timed out, terminal results are collected without lifecycle advancement, and guarded return resumes the normal comparison path. Committed as 8e5e362f; focused scheduler tests and Ruff passed. cost=$1.45
- 2026-09-09T12:18:01+00:00 automated review requested changes: Manual-mode lifecycle parking works in the tested paths, but starting a replacement model trial can still mutate a reserved task. cost=$0.46
- 2026-09-09T12:18:16+00:00 dispatched revise run 20260909T121815Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17282 tokens)
- 2026-09-09T12:22:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:23:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Model-trial startup now rejects Manual-reserved tasks before validation, dispatch, or destructive --again cleanup. Focused Manual lifecycle and trial suites passed (107 tests total), Ruff passed, and the final diff checks were clean on commit 052c78ad. cost=$0.43
- 2026-09-09T12:27:23+00:00 automated review requested changes: Manual-mode lifecycle parking is broadly implemented and the focused suite passes, but Return to automation does not validate all required stale state. cost=$0.88
- 2026-09-09T12:27:40+00:00 dispatched revise run 20260909T122740Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17589 tokens)
- 2026-09-09T12:36:44+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:38:13+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Return to automation now compares the observed task status, PR URL/number/state, and head under the scheduler lock before clearing Manual mode. Committed as 842e33f1; 219 focused lifecycle/web tests and 67 CLI tests passed, and Ruff is clean. cost=$1.51
- 2026-09-09T12:42:42+00:00 automated review requested changes: Manual-mode polling advances PR-processing watermarks, causing changes observed while reserved to be skipped after returning to automation. cost=$0.62
- 2026-09-09T12:43:41+00:00 dispatched revise run 20260909T124341Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18109 tokens)
- 2026-09-09T12:49:50+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:54:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Manual-mode polling now preserves PR lifecycle-processing cursors while recording a separate observation snapshot, so feedback and draft/head changes observed during reservation are processed normally after return. Committed as 29b740c4; 297 focused tests passed, Ruff passed, and the final diff check was clean. cost=$0.98
- 2026-09-09T12:59:29+00:00 automated review requested changes: Manual-mode lifecycle parking is broadly implemented, but the web return action cannot resume automation after an observed PR head change. cost=$0.53
- 2026-09-09T12:59:41+00:00 dispatched revise run 20260909T125941Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18303 tokens)
- 2026-09-09T13:21:48+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:23:25+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: The task page now uses the authoritative scheduler guard, allowing Return to automation after a PR head change observed during Manual mode. Commit f057af17 passed 204 focused web and scheduler tests, Ruff, and diff checks. cost=$0.81
- 2026-09-09T13:23:36+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-09T13:23:45+00:00 dispatched rebase run 20260909T132345Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3277 tokens)
- 2026-09-09T13:28:53+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Rebased onto origin/main and resolved the review lifecycle conflict while preserving Manual-mode guards and recovery behavior. cost=$0.01
- 2026-09-09T13:32:50+00:00 automated review: approve — Manual mode now consistently parks automatic lifecycle mutations while preserving observation and safely resumes existing continuations. cost=$0.88
- 2026-09-09T14:04:04+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/rebase.py); a rebase agent will resolve it
- 2026-09-09T14:05:32+00:00 dispatched rebase run 20260909T140532Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3468 tokens)
- 2026-09-09T14:21:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Rebased onto origin/main and resolved the rebase.py conflict, preserving the Manual-mode guard and updated main-branch documentation. cost=$0.01
- 2026-09-09T14:27:17+00:00 CI failure
- 2026-09-09T14:54:55+00:00 dispatched revise run 20260909T145454Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18799 tokens)
- 2026-09-09T15:03:47+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:08:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Restored automatic-review failure recovery while preserving Manual-mode parking, committed as 4ce4163b. The four reported recovery cases and broader affected modules pass (179 tests), Ruff is clean, and the final diff check passes. cost=$0.63
- 2026-09-09T15:08:59+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/__init__.py); a rebase agent will resolve it
- 2026-09-09T15:09:06+00:00 dispatched rebase run 20260909T150901Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3832 tokens)
- 2026-09-09T15:17:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Rebased onto origin/main and resolved the scheduler lock conflict in src/garden/scheduler/__init__.py, preserving Manual-mode locking and existing tick_lock callers. cost=$0.02
- 2026-09-09T15:24:51+00:00 automated review: approve — Manual mode consistently parks automatic lifecycle mutations while preserving observation and completed-run continuations for safe return to automation. cost=$0.73
- 2026-09-09T15:30:10+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T15:31:43+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_web.py); a rebase agent will resolve it
- 2026-09-09T15:39:35+00:00 dispatched rebase run 20260909T153935Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~4057 tokens)
- 2026-09-09T15:44:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/368: Rebased onto origin/main and resolved all web action, page, template, and test conflicts without unrelated changes. cost=$0.02
- 2026-09-09T15:49:00+00:00 automated review: approve — Manual mode consistently parks automatic lifecycle mutations while preserving observation, active work, and existing state for guarded resumption. cost=$0.88
- 2026-09-09T15:53:38+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T15:55:13+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/368
