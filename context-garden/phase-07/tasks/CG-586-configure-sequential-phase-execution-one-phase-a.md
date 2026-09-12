---
id: CG-586
title: Configure sequential phase execution, one phase at a time
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/config.py
- src/garden/scheduler/dispatch.py
- src/garden/store.py
branch: garden/cg-586-configure-sequential-phase-execution-one-phase-a
pr: https://github.com/joshmarcus/context-garden/pull/473
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T21:08:00+00:00'
created: '2026-09-10T15:06:29+00:00'
updated: '2026-09-10T21:57:35+00:00'
---

## Goal

Let the owner configure Garden to work through a product's phases sequentially, working on one phase at a time rather than dispatching work across several open phases.

## Context

Owner request: "configuration for sequential phases (work on one at a time)". Add an explicit scheduling option alongside the existing concurrent-phase behavior. This is phase concurrency, not a limit of one task or one worker: eligible tasks within the selected phase may still run in parallel under existing resource limits. Filing this task does not change the live scheduler's configuration.

## Acceptance criteria

- [ ] Provide a persistent, validated setting for sequential versus concurrent phase execution. Make its scope and effective value clear in supported configuration surfaces and documentation; use the shared configuration boundary rather than separate UI/CLI policy. Preserve existing installations' scheduling behavior until the option is enabled.
- [ ] In sequential mode, choose the earliest open phase in the product's configured phase order and admit new work only for that phase. Later phases become eligible only after the current phase is actually closed, including required closing review and outstanding blockers; an empty ready queue or all implementation tasks merged is not itself phase closure. Respect existing phase freezes, owner decisions and task dependencies.
- [ ] Apply the same decision consistently to local and remote dispatch, revisions, reviews and other phase-owned model work. Keep collection, lease renewal, final publication and recovery for already active work available. Normal task parallelism and existing resource caps still apply within the current phase.
- [ ] Explain the current phase and why later-phase tasks are waiting in queue/status views. If the phase is blocked, frozen, awaiting owner input or depends on later-phase work, surface an actionable reason without silently skipping the phase, weakening dependencies or changing the setting. Avoid introducing a second independent phase-order mechanism.
- [ ] Define safe enable/disable and phase-reopen behavior. Preserve already running work and its source/results when the setting changes; stop new admission from other phases and let existing work finish, making that transition visible. Reopening an earlier phase must update new-admission eligibility predictably without cancelling later-phase work already in flight.
- [ ] Add proportionate deterministic coverage for concurrent behavior, sequential phase selection and advancement, closing-review blockers, reopening, cross-phase dependency waits, local/remote consistency and configuration changes with work in flight. Use portable APIs for Linux, macOS and Windows through WSL and report environments actually tested.

owner_request_key: owner-sequential-phase-configuration-20260910

## Log

- 2026-09-10T15:34:09+00:00 approved (delegated operator; full Inbox brief review of owner-requested sequential phase configuration)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:39:55+00:00 dispatched work run 20260910T173951Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~13363 tokens)
- 2026-09-10T17:52:08+00:00 discovered work filed: CG-596
- 2026-09-10T17:52:08+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:57:09+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$3.75
- 2026-09-10T18:34:41+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/473 (base main): Added validated global/product-scoped phase_execution configuration with a backward-compatible concurrent default and sequential earliest-open-phase admission. Verified phase advancement, reopening, freezes, cross-phase dependencies, queued/direct model routes, in-flight preservation, configuration surfaces, and status explanations on Linux with Python 3.12.
- 2026-09-10T18:34:43+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:45:32+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/task.py); a rebase agent will resolve it
- 2026-09-10T18:45:32+00:00 dispatched rebase run 20260910T184532Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1702 tokens)
- 2026-09-10T18:50:11+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.01
- 2026-09-10T18:50:35+00:00 dispatched revise run 20260910T185035Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14301 tokens)
- 2026-09-10T18:54:48+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:56:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/473: Removed the unused phase_refusal import introduced during conflict resolution and committed the fix as 3507a5b8. Verified the sequential-phase suite (4 passed), repository-wide Ruff lint, diff integrity, and absence of conflict markers on Linux with Python 3.12. cost=$0.43
- 2026-09-10T19:04:01+00:00 automated review requested changes: Sequential admission is broadly implemented, but an in-progress retro can still launch new model work from a no-longer-selected phase after configuration changes or phase reopening. cost=$0.50
- 2026-09-10T19:04:28+00:00 dispatched revise run 20260910T190428Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14635 tokens)
- 2026-09-10T19:08:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:09:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/473: Retro reconciliation now rechecks its owning product and phase before launching new model work, preserves deferred retro state, and retries after the selected phase advances. Verified on Linux with Python 3.12: 36 retro tests passed, 7 combined sequential-phase/retro tests passed, and repository Ruff lint passed. cost=$0.63
- 2026-09-10T19:14:19+00:00 automated review requested changes: Sequential phase admission is broadly implemented, but trial comparison can still start from a no-longer-selected phase. The branch also contains unrelated completion-provenance UI and fake-provider commits absent from main. cost=$0.41
- 2026-09-10T19:33:19+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T19:42:20+00:00 dispatched revise run 20260910T194220Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15690 tokens)
- 2026-09-10T20:00:39+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:01:56+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/473: Sequential phase admission now also gates trial comparison launches after contenders finish, preserving a visible retryable state until the phase becomes eligible. Verified committed head 328b8a4c on Linux/Python 3.12 with focused regressions, the full ordinary pytest suite, Ruff lint, and diff integrity checks. cost=$2.37
- 2026-09-10T20:04:14+00:00 automated review requested changes: Sequential phase admission works across the reviewed dispatch paths, including deferred trial comparisons and retros. One blocking UI statement contradicts the implemented and required in-flight publication behavior. cost=$0.54
- 2026-09-10T20:06:53+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T20:08:08+00:00 dispatched revise run 20260910T200808Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15752 tokens)
- 2026-09-10T20:11:54+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:13:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/473: Task-page phase holds now distinguish sequential admission from closed/frozen restrictions: sequential mode blocks new model work while explicitly allowing in-flight work to finish and publish. Verified committed head de150a7f on Linux/Python 3.12 with 83 focused tests, repository-wide Ruff lint, and diff integrity checks. cost=$0.68
- 2026-09-10T20:15:55+00:00 automated review requested changes: Sequential phase gating is broadly implemented, but fresh investigation-agent runs can still start for a later, non-selected phase. cost=$0.41
- 2026-09-10T20:46:37+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T21:07:30+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T21:08:00+00:00 dispatched revise run 20260910T210759Z-revise-3 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16084 tokens)
- 2026-09-10T21:11:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T21:12:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/473: Sequential phase admission now gates fresh investigation-agent runs while preserving pending state for retry after phase advancement. Verified committed head 1449d55f on Linux/Python 3.12 with 9 focused tests, repository-wide Ruff lint, diff integrity, and conflict-marker checks. cost=$0.57
- 2026-09-10T21:41:31+00:00 automated review: approve — Sequential phase admission is consistently applied across dispatch, investigation, review, trial, persona, kickoff, retro, and status paths while preserving active work. cost=$0.61
- 2026-09-10T21:45:15+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T21:57:35+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/473
