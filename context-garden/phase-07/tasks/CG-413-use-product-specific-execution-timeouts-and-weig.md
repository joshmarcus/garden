---
id: CG-413
title: Use product-specific execution timeouts and weighted resource admission
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-413-use-product-specific-execution-timeouts-and-weig
pr: https://github.com/joshmarcus/context-garden/pull/324
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T12:57:05+00:00'
created: '2026-09-07T20:05:53+00:00'
updated: '2026-09-09T13:24:52+00:00'
---

## Goal

Use product-specific execution timeouts and weighted resource admission. Recheck current implementation before choosing the smallest compatible change.

## Acceptance criteria

- [ ] Resolve per-product execution timeouts with backwards-compatible defaults across worker, revision and relevant runner paths; keep check timeout semantics distinct.
- [ ] Define validated per-product resource weights or reservations, including units and inheritance. Admit cheap work alongside heavy work when measured capacity permits, without lowering host reserves or bypassing hard caps.
- [ ] Account atomically for all admitted work and release reservations on terminal/recovered runs. Count heavy checks on their executing host and retain one active task per machine in in-place mode.
- [ ] Demonstrate two products with different time budgets and weights, starvation protection and restart reconciliation. Reuse shared resource admission and CG-405 remote integration rather than parallel accounting.

## Provenance and scope

Owner-provided additional gap F5, 2026-09-07. Generic requirements only. This task remains a phase-07 draft and does not authorize new access, deployment or external notifications. Refer to the shared spec, not the private environment survey.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T15:46:53+00:00 dispatched work run 20260908T154653Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~9277 tokens)
- 2026-09-08T16:21:16+00:00 opened https://github.com/joshmarcus/context-garden/pull/324 (base main): Added per-product execution budgets and durable weighted capacity reservations across local and remote execution. Admission supports bounded first-fit scheduling, restart reconciliation, host-specific accounting, and keeps check timeouts independent. cost=$4.36
- 2026-09-08T16:33:34+00:00 check did not run (20260908T163213Z-check): idle 22 min (no output or file change); will retry
- 2026-09-08T16:35:45+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:38:05+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:39:56+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:41:39+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:43:40+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:45:11+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:46:56+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:48:55+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:50:18+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:51:41+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:53:01+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:54:19+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:55:37+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:57:05+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T16:58:29+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:01:05+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:02:25+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:04:03+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:05:21+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:06:50+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:08:08+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:09:25+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human
- 2026-09-08T17:10:44+00:00 check did not run (20260908T163334Z-check): idle 24 min (no output or file change); retry also failed; needs human


## Operator replay recovery 2026-09-08T17:12:01.153329+00:00

Both replay attempts expired before host claim and performed no check. Original records are preserved. Recover the required check and review on the controller through normal one-slot admission, with actual affected scheduling/timeout outcome verification; a generic replay alone does not establish those outcomes. CG431/436/438 own permanent routing, semantic selection and continuation repairs.
- 2026-09-08T17:34:57+00:00 review validation scope expansion: weighted in-place remote claim — The changed claim endpoint forces capacity to one before comparing weighted reservations, creating a permanent admission failure for heavier products.
- 2026-09-08T17:34:58+00:00 automated review requested changes: Weighted admission works in focused tests, but in-place hosts permanently reject runs whose product weight exceeds one. The saved served replay covers generic reap/retry behavior, not the required affected timeout/admission journey. cost=$0.30
- 2026-09-09T01:52:56+00:00 Operator restored queued author to remote after current-source check routing inspection: no generated capture pages or controller-owned spec paths. Full substantive feedback preserved; current owner proportional-validation policy appended. No active run or cap changed.
- 2026-09-09T02:17:25+00:00 dispatched revise run 20260909T021725Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~13363 tokens)
- 2026-09-09T02:54:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T03:15:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/324: Separated the in-place one-run fence from weighted capacity comparison, so an idle in-place host can claim a weight-2 product while still rejecting concurrent work until release. Verified the committed behavior with the full remote-worker suite (27 passed), focused scheduler resource and in-place tests (20 passed), and Ruff. cost=$0.61
- 2026-09-09T03:16:03+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py, src/garden/scheduler/reap.py, src/garden/scheduler/resources.py, src/garden/scheduler/review.py, tests/scheduler/test_resources.py, tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-09T03:17:29+00:00 dispatched rebase run 20260909T031729Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3104 tokens)
- 2026-09-09T03:43:39+00:00 pre-PR checks failed (lint, syntax); revise run will fix before the PR is updated cost=$0.02
- 2026-09-09T03:45:18+00:00 dispatched revise run 20260909T034518Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15817 tokens)
- 2026-09-09T03:50:20+00:00 automated review: request_changes — The rebased head contains syntax errors in core scheduler modules and cannot run or be tested. cost=$0.16
- 2026-09-09T03:53:08+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T03:59:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/324: Repaired malformed conflict resolution in weighted dispatch and review metadata, restored starvation-tracking scope, and fixed import ordering. Verified commit f4c5092d with 75 passed and 1 skipped focused tests, clean Ruff, Python compilation, and git diff checks. cost=$0.45
- 2026-09-09T04:04:04+00:00 automated review requested changes: Weighted admission tests pass, but product-specific execution budgets are not consistently enforced across remote and local/SSH paths. cost=$0.45
- 2026-09-09T04:04:26+00:00 dispatched revise run 20260909T040426Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15018 tokens)
- 2026-09-09T04:09:35+00:00 revision failed: worker exited 1: {'message': "You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 15th, 2026 2:14 AM."}
- 2026-09-09T09:45:24+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T09:45:44+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-413`) or send it back (`garden triage CG-413 --changes "..."`)
- 2026-09-09T11:04:10+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T11:05:20+00:00 dispatched revise run 20260909T110520Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15254 tokens)
- 2026-09-09T11:14:41+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:17:27+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/324: Remote controller deadlines now use each run's snapshotted product execution budget with legacy and check-mode fallbacks, while local and SSH launchers preserve fractional timeout minutes. Verified commit 8f51303d with the affected remote-worker, runner, and weighted-resource suites plus clean Ruff and compilation checks. cost=$1.31
- 2026-09-09T11:17:41+00:00 PR conflicts with main; rebase onto main conflicts (docs/architecture.md, src/garden/config.py, src/garden/remote_worker.py, src/garden/web/pages/api.py, tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-09T11:17:49+00:00 dispatched rebase run 20260909T111748Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3820 tokens)
- 2026-09-09T11:21:51+00:00 automated review: request_changes — Weighted admission and product-specific budgets otherwise pass focused verification, but legacy remote check runs incorrectly receive a product execution timeout. cost=$0.52
- 2026-09-09T11:24:46+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/324: Rebased CG-413 onto origin/main and resolved all conflicts. cost=$0.03
- 2026-09-09T11:28:59+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: resolve per-product execution timeouts; run `garden triage CG-413 --changes "<feedback>" to unblock`
- 2026-09-09T12:44:33+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T12:44:57+00:00 dispatched revise run 20260909T124457Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16569 tokens)
- 2026-09-09T12:54:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:55:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/324: Fixed all three blocking edge cases and committed them as c8fb2085. Focused resource, remote-worker, persona, kickoff, and retro suites passed (181 passed, 1 skipped); Ruff, compileall, diff checks, and conflict-marker checks were clean. cost=$1.24
- 2026-09-09T12:55:44+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/checkruns.py); a rebase agent will resolve it
- 2026-09-09T12:57:05+00:00 dispatched rebase run 20260909T125704Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3768 tokens)
- 2026-09-09T13:01:57+00:00 automated review: approve — Product-specific execution budgets and weighted admission satisfy the frozen criteria, including distinct check semantics, starvation protection, restart accounting, and in-place exclusivity. cost=$0.51
- 2026-09-09T13:05:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/324: Rebased CG-413 onto origin/main and resolved all conflicts. cost=$0.02
- 2026-09-09T13:20:14+00:00 automated review: approve — Product-specific execution budgets and weighted admission meet the frozen criteria, including independent check timeouts, bounded starvation protection, restart accounting, and in-place exclusivity. cost=$0.51
- 2026-09-09T13:21:47+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T13:24:52+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/324
