---
id: CG-464
title: Merge clean approved heads without redundant latest-base rebuild
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/config.py
- src/garden/scheduler/rebase.py
- src/garden/github.py
- tests/test_automerge.py
- tests/test_store.py
branch: codex/merge-clean-reviewed-head
pr: https://github.com/joshmarcus/context-garden/pull/358
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T11:22:08+00:00'
created: '2026-09-09T02:50:41+00:00'
updated: '2026-09-09T14:02:31+00:00'
---

## Goal

Merge approved pull requests with passing CI on their current reviewed commit when they remain conflict-free, without requiring a rebase and another build solely because main advanced.

## Context

The owner explicitly authorized this policy on September 9 and requested an implementation PR. PR346 was approved, exact-head CI was green and GitHub reported CLEAN/MERGEABLE, but the current queue required a latest-base rebase and another full build. Keep merges sequential as the owner explicitly clarified: after each completed merge, recompute the next PR against the updated base so new conflicts cannot be ignored. CG396 owns pluggable exact-head CI receipts; this task owns the optional current-base requirement and does not duplicate that work.

## Acceptance criteria

- [ ] When the owner-selected policy permits it, an approved PR with current-head passing CI and a fresh conflict-free GitHub assessment merges without rebasing or launching another validation round merely because main advanced.
- [ ] Merge processing remains sequential. After a prior merge, the next candidate is checked against the updated base; pending or unknown mergeability waits and a newly conflicting candidate is routed through existing conflict recovery.
- [ ] Actual failing or pending CI, stale review/head identity, substantive review rejection, dependency or human stops and atomic head guards retain their protection; a concurrent head change cannot merge unreviewed source.
- [ ] Preserve an explicit configurable option for installations requiring current-base validation, document both behaviors and verify focused positive and refusal paths. The current owner's intended configuration uses the clean-head policy.

## Implementation scope

Use the existing merge queue and GitHub mechanisms. A github.automerge_require_current_base setting with a product-level override is appropriate if consistent with configuration conventions. Preserve existing default compatibility if useful and configure this garden explicitly after the new release is deployed. Do not hot-patch the installed RC9 runtime or manually merge ordinary feature PRs to claim Garden throughput.

## Log

- 2026-09-09T02:50:42+00:00 approved (owner clean-head merge policy and explicit sequential-merge clarification)
- 2026-09-09T02:50:42+00:00 Operator-owned implementation by capture_policy_sol in isolated existing source; no duplicate scheduler author.
- 2026-09-09T02:50:43+00:00 dispatched work run 20260909T025043Z-work via manual [human] (fresh session, base main, ~19876 tokens)
- 2026-09-09T03:13:27+00:00 external PR attached at codex/merge-clean-reviewed-head; existing CI is SUCCESS
- 2026-09-09T03:40:56+00:00 automated review: approve — The clean-head policy is configurable and preserves sequential processing, exact-head approval/CI checks, conflict handling, and atomic merge guards. cost=$0.42
- 2026-09-09T03:44:21+00:00 Operator held only automatic merge for the confirmed same-patch conflict-rebase review-head lineage defect. Current PR358 is being corrected in an isolated checkout; live read-only reviews and all existing results remain preserved. See cg464-known-lineage-bug-automerge-hold.json for exact prior setting and restore gate.
- 2026-09-09T04:04:49+00:00 Published reviewed approval-lineage correction 433aebc481eb8968d63b40bbfaa2a3375b87dc9f; original review evidence preserved, one exact-head review queued. Autocomplete remains held until corrected-head validation completes.
- 2026-09-09T04:09:34+00:00 automated review:  —
- 2026-09-09T10:38:46+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-09T10:38:48+00:00 dispatched rebase run 20260909T103848Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1396 tokens)
- 2026-09-09T10:42:25+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/358: Rebased onto origin/main and resolved the poll.py automerge validation conflict while preserving both provider validation and clean-head policy behavior. cost=$0.02
- 2026-09-09T10:45:04+00:00 automated review requested changes: The core clean-head queue behavior is implemented, but its CI gate is incompatible with command-based exact-head validation. cost=$0.50
- 2026-09-09T10:45:12+00:00 dispatched revise run 20260909T104512Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21052 tokens)
- 2026-09-09T10:48:35+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T10:49:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/358: Fixed clean-head automerge so command-provider exact-head validation is authoritative even when GitHub checks are empty. Committed as c935ec025793febdf327a483123a04a465b07c9a; 97 focused tests and Ruff passed. cost=$0.57
- 2026-09-09T10:52:23+00:00 automated review: approve — The configurable clean-head merge path meets the requested policy while retaining the current-base default and existing safety gates. cost=$0.36
- 2026-09-09T11:22:05+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/rebase.py); a rebase agent will resolve it
- 2026-09-09T11:22:08+00:00 dispatched rebase run 20260909T112207Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1849 tokens)
- 2026-09-09T11:26:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/358: Rebased onto origin/main and resolved the rebase.py conflict preserving both sides' behavior cost=$0.01
- 2026-09-09T11:28:57+00:00 automated review: approve — The configurable clean-head merge path meets the requested policy while preserving sequential processing and existing safety gates. cost=$0.38
- 2026-09-09T13:50:49+00:00 operator restored prior absent automerge setting: native lineage correction, exact-head CI and independent peer review verified on afd16e1b; normal Garden merger owns completion
- 2026-09-09T14:00:39+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T14:02:31+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/358
