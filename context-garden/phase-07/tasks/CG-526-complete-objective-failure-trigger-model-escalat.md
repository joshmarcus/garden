---
id: CG-526
title: Complete objective failure-trigger model escalation
status: done
product: context-garden
phase: phase-07
depends_on:
- id: CG-437
  after: merge
- id: CG-500
  after: merge
- id: CG-593
  after: merge
priority: 2
difficulty: hard
reading:
- docs/architecture.md
- docs/design.md
- docs/worker-protocol.md
- context-garden/phase-05/goals.md
- context-garden/phase-07/specs/enterprise-remote-environments.md
- context-garden/phase-05/specs/cost-aware-model-routing.md
- src/garden/scheduler/human.py
- src/garden/scheduler/poll.py
branch: garden/cg-526-complete-objective-failure-trigger-model-escalat
pr: https://github.com/joshmarcus/context-garden/pull/450
runner: remote
discovered_from: CG-505
attempts: 3
last_dispatched_at: '2026-09-11T01:40:20+00:00'
created: '2026-09-10T11:58:22+00:00'
updated: '2026-09-11T02:21:36+00:00'
file: src/garden/scheduler/human.py
error: CG-437 escalates only at substantive-revision thresholds; the routing specification's other objective
  failure triggers have no owning task.
---

Implement the remaining failure-driven model-routing policy from `phase-05/specs/cost-aware-model-routing.md`. Build on CG-437's durable substantive-revision thresholds without duplicating them: route eligible retries or revisions to a higher configured tier for objective implementation failures such as failed final verification, repeated unchanged attempts, unmet acceptance criteria, or missing expected changes. Preserve explicit model overrides and escalation floors; distinguish implementation failures from infrastructure, admission, stale-check, and unavailable-evidence conditions; record the triggering signal, prior/new tier and actual model; and add focused recovery and classification tests. Coordinate with CG-213/302 only at the OpenRouter adapter boundary.

## Provenance

Discovered by CG-505 (Audit and update all Garden specifications) during run `20260910T115405Z-revise`.
## Log
- 2026-09-10T11:58:22+00:00 discovered by CG-505


## Reviewed policy boundaries

Reuse CG-437 substantive-revision floors and CG-500 terminal-CI-failure handling. Define the exact objective signals, transition/threshold and precedence before implementing remaining triggers; preserve explicit model choices and never lower an established floor. Deduplicate a failed attempt or CI identity across polls/restarts and persist the signal, prior/new tier and resolved model. Infrastructure, admission, stale observations and unavailable optional evidence are not implementation failures. Keep provider-independent work independent; any OpenRouter-specific adapter change must use the accepted CG-213/302 contract after those owners land.
- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T15:32:00+00:00 dispatched work run 20260910T153156Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22190 tokens)
- 2026-09-10T15:39:04+00:00 discovered work filed: CG-590
- 2026-09-10T15:39:04+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:40:32+00:00 opened https://github.com/joshmarcus/context-garden/pull/450 (base main): Implemented and committed durable objective-failure model escalation across worker retries, pre-PR verification, CI, automated review, and unchanged-attempt handling. Ruff and Python compilation passed; focused pytest collection was blocked by an existing circular import in the checkout. cost=$1.51
- 2026-09-10T15:41:51+00:00 CI failure
- 2026-09-10T15:44:30+00:00 dispatched revise run 20260910T154426Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~23467 tokens)
- 2026-09-10T15:56:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:58:05+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Exact-status CI failures now escalate provider-independently after usable analysis, with authoritative failure identities retained across holds, reruns, polls, and restarts. Fixed the CI circular import and verified committed head 1b9a3cb336526ad450c02a8a9c9efd61239b8f2a with 211 focused tests and clean Ruff. cost=$2.77
- 2026-09-10T15:58:14+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/hosts/locking.py, src/garden/locking.py); a rebase agent will resolve it
- 2026-09-10T15:59:44+00:00 dispatched rebase run 20260910T155943Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2026 tokens)
- 2026-09-10T16:02:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Rebased onto origin/main and resolved conflicts in both locking modules; worktree is clean. cost=$0.01
- 2026-09-10T16:06:23+00:00 automated review: approve — Objective implementation failures now escalate model tiers durably while preserving explicit models, escalation floors, and infrastructure/stale-result exclusions. cost=$0.71
- 2026-09-10T16:31:23+00:00 triage: changes requested by hand: The current head has independent functional approval, but actual push CI34499374358 failed2 tests with2542 passing. Pres
- 2026-09-10T16:51:44+00:00 dispatched revise run 20260910T165140Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~23665 tokens)
- 2026-09-10T16:58:30+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:59:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Reconciled the two failed CI tests with the intended objective-failure policy: unmet criteria and blocking implementation findings escalate medium/sonnet work to hard/opus, while original run history remains attributed to medium/sonnet and current task metrics use the effective hard tier. Committed as 517b1a07; 508 affected tests passed with 1 skipped, exact-head regression nodes passed, and Ruff is clean. cost=$1.08
- 2026-09-10T17:05:16+00:00 automated review requested changes: Automated-review escalation treats every blocking finding as an implementation failure, including infrastructure or unavailable-evidence blockers that the task explicitly excludes. cost=$0.94
- 2026-09-10T17:09:15+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T17:19:13+00:00 dispatched revise run 20260910T171910Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~24265 tokens)
- 2026-09-10T17:28:32+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:29:46+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Closed the automated-review classification gap by requiring typed failure categories and escalating only objective implementation failures. Committed as 6add4399; 281 focused tests passed, 9 exact-head regression cases passed, and Ruff is clean. cost=$2.54
- 2026-09-10T17:41:32+00:00 automated review requested changes: Objective-failure classification is substantially implemented, but current head fails an applicable end-to-end escalation test and contradicts the PR's passing-test claim. cost=$0.70
- 2026-09-10T18:46:00+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T18:56:56+00:00 dispatched revise run 20260910T185652Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~24403 tokens)
- 2026-09-10T18:59:37+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:01:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Rebased onto the accepted CG-593 repair and corrected the fake review producer so unmet implementation criteria carry the typed implementation category and trigger the durable escalation path. Verified 329 focused tests, then reran the exact failing regression and Ruff successfully at committed head 04efed90b544e51ee89a8c01478cb2c0d5f42f39. cost=$0.75
- 2026-09-10T19:04:00+00:00 automated review requested changes: Most objective-failure routing is correctly implemented and the focused suite passes, but repeated infrastructure or unavailable-evidence review blockers can still escalate the author model through the generic stall path. cost=$0.76
- 2026-09-10T19:33:16+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T19:58:54+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T19:59:36+00:00 dispatched revise run 20260910T195936Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24587 tokens)
- 2026-09-10T20:05:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:06:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Repeated automated-review stalls now preserve typed failure eligibility: infrastructure, admission, and unavailable-evidence blockers still stall for human attention but do not escalate the author model, while repeated implementation failures retain escalation. Committed as 621ad20c; 236 focused tests passed and Ruff is clean. cost=$1.04
- 2026-09-10T20:10:34+00:00 automated review requested changes: Typed review classification is improved, but an infrastructure-driven revision that correctly leaves the source unchanged still escalates the model through generic no-change stall handling. cost=$0.36
- 2026-09-10T20:46:34+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T20:47:28+00:00 dispatched revise run 20260910T204728Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24942 tokens)
- 2026-09-10T20:55:35+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:56:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Preserved originating automated-review failure eligibility through revise dispatch and unchanged-result stall handling. Verified that infrastructure feedback stalls without model escalation while implementation feedback still records repeated_unchanged_attempt; 231 broader focused tests and 161 final review/handoff tests passed, and Ruff is clean. cost=$1.64
- 2026-09-10T20:59:14+00:00 automated review requested changes: Typed review and unchanged-revision routing are substantially correct, but two objective-failure classification paths remain incomplete. cost=$0.73
- 2026-09-10T21:57:05+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T21:57:37+00:00 dispatched revise run 20260910T215737Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25454 tokens)
- 2026-09-10T22:26:33+00:00 revision failed: worker idle 22 min (no output or file change)
- 2026-09-10T22:58:57+00:00 dispatched work run 20260910T225857Z-work via manual [human] (fresh session, base main, ~24571 tokens)
- 2026-09-10T22:58:58+00:00 external PR attached at garden/cg-526-complete-objective-failure-trigger-model-escalat; existing CI is PENDING
- 2026-09-10T23:19:52+00:00 automated review requested changes: Most escalation paths are correctly typed and durable, but a classified infrastructure or unavailable-evidence pre-PR failure can still escalate the implementation tier. cost=$0.58
- 2026-09-10T23:43:45+00:00 triage: changes requested by hand: One bounded correction for the new typed-error finding: candidate infrastructure/admission/unavailable-evidence failures
- 2026-09-10T23:47:43+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T23:48:12+00:00 dispatched revise run 20260910T234812Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25556 tokens)
- 2026-09-11T00:01:34+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T00:12:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/450: Preserved typed pre-PR failure classifications through clean-base probes while retaining legacy untyped escalation behavior. Committed as 144cf521; 50 focused scheduler tests passed before the expanded 5-case regression passed, and Ruff is clean. cost=$0.64
- 2026-09-11T00:24:20+00:00 automated review requested changes: Objective-failure escalation is broadly implemented and its focused tests pass, but cancelled GitHub Actions runs are incorrectly attributed to the implementation and can trigger model escalation. cost=$0.68
- 2026-09-11T00:44:41+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-11T00:45:11+00:00 dispatched revise run 20260911T004510Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25862 tokens)
- 2026-09-11T01:09:46+00:00 revision failed: worker idle 21 min (no output or file change)
- 2026-09-11T01:40:20+00:00 dispatched work run 20260911T014019Z-work via manual [human] (fresh session, base main, ~25132 tokens)
- 2026-09-11T01:40:21+00:00 external PR attached at garden/cg-526-complete-objective-failure-trigger-model-escalat; existing CI is SUCCESS
- 2026-09-11T02:04:58+00:00 automated review: approve — Objective implementation failures now escalate durably while explicit models, escalation floors, and non-implementation classifications remain protected. cost=$0.85
- 2026-09-11T02:08:44+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T02:21:36+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/450
