---
id: CG-500
title: Route approved PRs with failed CI back to revision
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/human.py
- tests/scheduler/test_poll.py
branch: garden/cg-500-route-approved-prs-with-failed-ci-back-to-revisi
pr: https://github.com/joshmarcus/context-garden/pull/410
discovered_from: CG-411
attempts: 1
last_dispatched_at: '2026-09-10T03:50:36+00:00'
created: '2026-09-10T02:28:04+00:00'
updated: '2026-09-10T04:18:33+00:00'
---

## Goal

Automatically route a reviewed PR with failing current-head CI back to a bounded revision or diagnosed infrastructure recovery instead of leaving it idle in review or appearing merge eligible.

## Context

Owner request September 10: if something is approved for review but CI fails, send it back to revise. CG411 / PR321 at 2aad2515ebbfb9c14881de9101e895b1e7b7372f had an approving native review and two failed CI runs (34425178450, 34425175957), no pending feedback and no active run. It sat in review until operator triage supplied the failing completed-merged external-PR fixture regression. CG417 demonstrates repeated pre-test infrastructure failure. Coordinate with CG474 feedback composition and CG396/CG434 exact-source CI evidence; this issue owns automatic transition and truthful eligibility, not another CI provider.

## Acceptance criteria

- [ ] On a new terminal failure of applicable current-head CI, obtain actionable failure evidence, preserve all applicable review feedback and queue one bounded revision of the existing branch even if the latest review approved it. Do not require a human to discover the idle state.
- [ ] Distinguish code/test failures from infrastructure or unavailable-check failures. Use a specific bounded retry/recovery for genuinely transient infrastructure; repeated setup failure must reach actionable diagnosis, never an unlimited rerun or invented code defect.
- [ ] Deduplicate by current source and check attempt/failure identity across repeated polls and controller restarts. Respect active writers, manual reservations, explicit holds and revision limits, with a visible actionable reason when continuation cannot be admitted.
- [ ] Remove failed-head PRs from merge eligibility and show the actual next state/reason in task, Inbox and merge-queue views. Preserve exact-head passing CI, approval, conflict and atomic-head checks before eventual merge.
- [ ] Verify approval-before-failure, failure-before-approval, pending-to-failure, stale head, duplicate polls/restart, repeated infrastructure error, protected manual work and successful revise/check/review progression. The actual worker brief includes full relevant CI evidence and applicable review findings. Keep APIs and paths portable on Linux, macOS and Windows through WSL; report untested platforms.

## Log

- 2026-09-10T02:34:12+00:00 approved (owner requested draft review and readiness; operator verified brief)
- 2026-09-10T02:51:43+00:00 dispatched work run 20260910T025140Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16186 tokens)
- 2026-09-10T02:57:30+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T02:58:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/410 (base main): Terminal current-head CI failures now bypass the unchanged-PR timestamp shortcut, retain actionable failed-check evidence, leave the merge queue, and route to one bounded revision. Verified with the complete scheduler suite (339 passed, 1 skipped), Ruff, and git diff checks; committed as a1522da4. cost=$1.03
- 2026-09-10T03:01:04+00:00 automated review: approve — Terminal current-head CI failures now bypass the unchanged-PR timestamp shortcut, are deduplicated by stable failure identity, and route approved merge candidates back to revision with actionable CI feedback. cost=$0.45
- 2026-09-10T03:09:39+00:00 triage: changes requested by hand: Exact run34431457686 fails two relevant regressions: test_red_ci_holds_the_merge_with_reason_on_the_task expects IN_REVI
- 2026-09-10T03:50:36+00:00 dispatched revise run 20260910T035033Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17108 tokens)
- 2026-09-10T03:56:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:57:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/410: Fixed flaky CI retry sequencing so the bounded retry is not consumed during the same scheduler tick and a subsequent genuine failure routes to revision. Updated the obsolete red-CI merge test and committed the result as 8be214eb; affected suites passed with 424 passed/1 skipped, final-head regressions passed 4/4, and Ruff passed. cost=$0.67
- 2026-09-10T04:00:01+00:00 automated review: approve — Failed current-head CI now exits merge eligibility and routes approved PRs through bounded revision or CI recovery, with stable deduplication and actionable evidence. cost=$0.34
- 2026-09-10T04:15:48+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T04:18:33+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/410
