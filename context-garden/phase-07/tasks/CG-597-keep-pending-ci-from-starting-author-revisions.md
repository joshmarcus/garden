---
id: CG-597
title: Keep pending CI from starting author revisions
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-593
- CG-526
kind: bug
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/review.py
- src/garden/review.py
- src/garden/checks.py
branch: garden/cg-597-keep-pending-ci-from-starting-author-revisions
pr: https://github.com/joshmarcus/context-garden/pull/474
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T19:20:10+00:00'
created: '2026-09-10T18:38:41+00:00'
updated: '2026-09-11T03:02:48+00:00'
---

## Goal

Keep pending external validation as an explicit wait, without starting an author revision or requiring another review merely because CI finished after a source review.

## Observed incident

CG593 review180843 at5116fda1694233fdce685d385380d58ffe8f47db found no code defect and121focused passes, but returned request_changes solely because fullCI34512343465/34512347835 was still running. That automatically dispatched redundant revision181243; both realCI jobs passed18:16 on unchangedsource, but the extra revision repeated fullvalidation and cost0.6708492USD before its authenticated completion18:27. Original review, failures, results and usage remain evidence. The operator independently reviewed the complete four-file diff and merged the unchanged approved/green repair18:30. This task corrects the future workflow, not those historical records.

## Acceptance criteria

- [ ] Represent a pending source-bound external gate separately from an actionable implementation/review defect. A reviewer can approve the inspected source while CI remains an independent merge gate; a not-yet-completed validation requirement must not by itself consume an author attempt, revision or escalation.
- [ ] Coordinate reviewer-result ingestion and normal CI state across timing races: CI pending before/after review, CI later success/failure/unavailable, changed head and stale receipts. Real code defects still require correction even if CI is pending; actual failed CI remains actionable through CG500. Never infer approval or waive an unrelated unmet criterion from a green check.
- [ ] Once the same reviewed source's sole pending external gate passes, proceed through ordinary accepted-source merge eligibility without a second review merely for count/timing. Preserve source-bound approvals, independent review, configured policy and all original findings/history. Use typed provenance/requirement classification rather than broad substring rules that could erase a real defect.
- [ ] Keep UI/CLI status and next actions truthful: waiting for named CI/evidence, actual unavailable infrastructure, real implementation changes, or merge eligibility. No request to edit code that is already accepted and unchanged; no stale human decision after the gate resolves.
- [ ] Add deterministic paired regressions for CI-only waiting versus a real code finding, pending-to-green/red, head changes, and review/check arrival order. Preserve CG526's failure classification, unknown pricing and actual attempt accounting. Verify the same frozen acceptance requirement is not automatically treated as a pre-review failure when it describes final merge readiness.

## Scope

Build on CG396 exact-head checks, CG500 CI revision routing, CG474 feedback preservation and CG526 objective classification. This is distinct from CG594 reference-driven brief composition. Keep the current review/CI protections and models; do not rerun the live phase retrospective or rewrite original observations.

owner_request_key: pending-ci-is-wait-not-author-revision-20260910

## Log

- 2026-09-10T18:39:34+00:00 approved (delegated operator observed CI-only author loop; preserve actual review/CI gates)
- 2026-09-10T18:41:02+00:00 dispatched work run 20260910T184102Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-526-complete-objective-failure-trigger-model-escalat stacked on CG-526, ~17494 tokens)
- 2026-09-10T18:48:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:50:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/474 (base garden/cg-526-complete-objective-failure-trigger-model-escalat): Separated pending external CI from source review so accepted, unchanged source waits at the merge gate without consuming another review or author revision. Verified review/CI timing, pending-to-green merge, red-CI routing, stale heads/receipts, and implementation-failure accounting with 214 focused tests; Ruff passed. cost=$2.33
- 2026-09-10T18:54:54+00:00 automated review: approve — Pending exact-head CI is cleanly separated from source-review defects while existing merge, stale-head, and failed-CI gates remain enforced. cost=$0.91
- 2026-09-10T19:01:10+00:00 CI failure
- 2026-09-10T19:01:41+00:00 dispatched revise run 20260910T190141Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-526-complete-objective-failure-trigger-model-escalat, ~18850 tokens)
- 2026-09-10T19:08:26+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:10:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/474: Updated the fake reviewer to classify unmet criteria as implementation failures, restoring the expected escalation behavior while preserving conservative handling of legacy reviews. Verified 373 affected tests pass and Ruff is clean at fe60957b2ab28a08990a522b1ec7de1db8dfcbfa. cost=$1.05
- 2026-09-10T19:10:23+00:00 PR conflicts with garden/cg-526-complete-objective-failure-trigger-model-escalat; rebase onto garden/cg-526-complete-objective-failure-trigger-model-escalat conflicts (src/garden/scheduler/poll.py, tests/scheduler/test_feedback_handoff.py); a rebase agent will resolve it
- 2026-09-10T19:10:31+00:00 dispatched rebase run 20260910T191031Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base garden/cg-526-complete-objective-failure-trigger-model-escalat, conflict only; easy tier, ~2089 tokens)
- 2026-09-10T19:15:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/474: Resolved CI identity, rerun handling, regression-test, and fake-review classification conflicts; rebase completed cleanly. cost=$0.02
- 2026-09-10T19:19:54+00:00 automated review requested changes: Pending CI is separated from initial source-review dispatch and merge remains exact-head gated, but pending-gate findings can still suppress a later actionable author revision through stall detection. cost=$0.65
- 2026-09-10T19:20:10+00:00 dispatched revise run 20260910T192010Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-526-complete-objective-failure-trigger-model-escalat, ~19855 tokens)
- 2026-09-10T19:23:41+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:25:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/474: Excluded typed pending external gates from repeated-finding stall detection and added a regression proving a repeated pending gate cannot suppress a new implementation defect. Verified 189 focused tests and repository-wide Ruff lint pass at cc3e9dba43c29fcf4c3230ec00cdb60bc5d276cd. cost=$0.65
- 2026-09-10T19:29:00+00:00 automated review: approve — Pending exact-head CI is correctly separated from actionable review defects, while stale-head, failed-CI, implementation-feedback, and merge gates remain enforced. cost=$0.48
- 2026-09-11T02:21:40+00:00 parent CG-526 merged; rebased onto main and retargeted the PR
- 2026-09-11T02:39:12+00:00 automated review: approve — Pending exact-head CI is separated from actionable review defects while merge, stale-head, failed-CI, and implementation-finding protections remain intact. cost=$0.73
- 2026-09-11T02:56:00+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T03:02:48+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/474
