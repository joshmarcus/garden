---
id: CG-396
title: Use pluggable exact-head CI status for review and merge eligibility
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-395
priority: 0
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an
pr: https://github.com/joshmarcus/context-garden/pull/343
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T14:52:59+00:00'
created: '2026-09-07T19:56:15+00:00'
updated: '2026-09-10T15:10:53+00:00'
---

## Goal

Add a bounded status-provider contract distinct from existing failure-log analyzers. Resolve status for repository, PR and exact head even if PR metadata is unchanged.

## Acceptance criteria

- [ ] Return state, queried SHA, stale, exists_for_sha, evidence URL and failures; stale, missing, mismatched, unknown, timeout and malformed responses never qualify as green.
- [ ] Refresh after head changes and external CI completion without relying solely on PR updated_at; bind review and merge eligibility to the current head.
- [ ] Show exact-head freshness and absence on task pages and metrics; retain existing GitHub behavior and analyzer hooks. Test delayed status, old green, unavailable provider and recovery.

**Owner-requested AWS validation provider (2026-09-08)**

The owner wants external workers to run the full ordinary test suite on their AWS host instead of pushing to GitHub Actions solely to run it. Integrate this into the existing status-provider contract rather than adding a parallel gate.

- [ ] Supply a worker-check status provider backed by Garden-owned durable check results, bound to exact source SHA, command/selection, exit status and log location. An author's prose alone cannot manufacture a pass. Rebase or changed source invalidates prior success.
- [ ] Under explicit product policy, successful AWS-host ordinary-suite verification satisfies final validation, review and merge eligibility without requiring a duplicate GitHub Actions full-suite run. Update author/reviewer briefs and UI/status explanations consistently; preserve GitHub-backed behavior for other policies.
- [ ] Keep local resource-constrained workers on focused suites. AWS ordinary suites exclude stress unless a separate bounded experiment explicitly opts in. Integrate the supervised remote validation repair tracked by CG-429 and retain real test failures.
- [ ] Verify a real remote ordinary-suite result flowing into current-head eligibility, plus stale/absent/failure/mismatched-head cases. Adjust routine GitHub workflow selection for this policy without disabling unrelated safeguards or hiding a failed required check.

- [ ] Remote workers do not each poll unauthenticated GitHub Actions. Centralize any remaining required status reads through the authenticated controller, coalesce/cache by repository and SHA, respect rate-limit/reset responses, and return pending/unavailable clearly without wasting implementation rounds. Preserve completed work when external status alone is unavailable.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G4. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T12:51:04+00:00 Owner requested AWS-host full ordinary suites as the gate instead of duplicate GitHub full-suite runs; integrated into existing unstarted status-provider scope. CG429 owns remote supervisor environment repair.
- 2026-09-08T12:54:44+00:00 Owner reports widespread GitHub rate limits; confirmed CG411 HTTP403 public Actions limit while useful implementation remained committed. Centralized bounded status access and saved-work recovery added to the same provider scope.
- 2026-09-08T13:49:53+00:00 dispatched work run 20260908T134953Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-395-support-explicit-github-enterprise-hosts-across stacked on CG-395, ~10167 tokens)
- 2026-09-08T15:33:22+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$6.46
- 2026-09-08T15:33:46+00:00 dispatched revise run 20260908T153346Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-395-support-explicit-github-enterprise-hosts-across, ~10379 tokens)


## Operator approved-policy recovery, 2026-09-08T1529

The operator preserved this worker checkout and applied only already-approved CG426 stress opt-in hunks because this old/stacked branch predated them. Retain the policy in the final source and verify the ordinary selection. Preservation receipts are under /var/lib/garden-worker/operator-preservation/CG-396-stress-policy-20260908T1527 on its worker host. The current-policy propagation repair is CG-434.
- 2026-09-08T16:58:26+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$9.59
- 2026-09-08T17:01:22+00:00 dispatched revise run 20260908T170122Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-395-support-explicit-github-enterprise-hosts-across, ~10654 tokens)
- 2026-09-08T17:28:59+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$2.32
- 2026-09-08T17:30:18+00:00 dispatched revise run 20260908T173015Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-395-support-explicit-github-enterprise-hosts-across, ~10751 tokens)
- 2026-09-08T18:09:58+00:00 check did not run (20260908T174940Z-check): idle 20 min (no output or file change); will retry
- 2026-09-08T18:16:37+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$1.56
- 2026-09-08T19:09:13+00:00 dispatched revise run 20260908T190913Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-395-support-explicit-github-enterprise-hosts-across, ~12147 tokens)
- 2026-09-08T19:30:45+00:00 parent CG-395 merged; rebase onto main conflicts; the next run must resolve it
- 2026-09-08T19:30:45+00:00 parent CG-395 merged; rebase conflicts; a rebase agent will resolve it cost=$2.03
- 2026-09-08T19:31:13+00:00 dispatched rebase run 20260908T193113Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2195 tokens)
- 2026-09-08T19:38:58+00:00 pre-PR checks failed (lint, syntax, PR description); no PR opened yet; revise run will fix cost=$0.01
- 2026-09-08T19:39:28+00:00 dispatched revise run 20260908T193927Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17850 tokens)
- 2026-09-08T19:49:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/343 (base main): Repaired the rebase-damaged metrics return while preserving existing totals and exact-head CI aggregation. Added regression coverage and confirmed the complete CG-396 focused suite, current-head tests, syntax, and lint pass. cost=$1.41
- 2026-09-08T20:16:49+00:00 automated review produced no verdict (idle 20 min (no output or file change))
- 2026-09-08T21:25:00+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/validation.py); a rebase agent will resolve it
- 2026-09-08T21:49:26+00:00 dispatched rebase run 20260908T214926Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2998 tokens)
- 2026-09-08T21:53:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Rebase completed successfully with both conflict resolutions applied. cost=$0.01
- 2026-09-08T22:06:35+00:00 automated review requested changes: The exact-head provider foundation is present, but four acceptance outcomes remain materially incomplete: state head refresh can be skipped, worker receipts do not validate selection or retain logs, GitHub reads are neither cached nor rate-limit-aware, and no real remote result or served replay is available for the reviewed head. cost=$0.50
- 2026-09-08T22:06:59+00:00 dispatched revise run 20260908T220659Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~13946 tokens)
- 2026-09-08T23:36:09+00:00 Operator preserved original queue timestamp and aligned temporary execution-age accounting with the independently verified claim; bound live remote processes and unexpired lease retained, without claiming fresh buffered output or functional success. CG457 owns the permanent lifecycle fix.
- 2026-09-09T00:51:08+00:00 revision failed: worker timed out
- 2026-09-09T01:55:06+00:00 triage: changes requested by hand: Owner-delegated precise preserved-source integration 20260909T0153. One bounded continuation, preserving the completed i
- 2026-09-09T01:56:40+00:00 dispatched revise run 20260909T015640Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22400 tokens)
- 2026-09-09T02:22:55+00:00 revision failed: worker idle 21 min (no output or file change)
- 2026-09-09T09:44:55+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T09:47:33+00:00 dispatched revise run 20260909T094731Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16551 tokens)


## Current main integration: enterprise validation policy

Owner feature CG467 / PR365 merged main at ece25c70bc5469fd7fa7b3aefec34bd89acffff2 while this preserved CG396 continuation was running. It adds per-product validation policy and worker tooling that do not assume GitHub Actions is available. Continue the existing CG396 source; integrate its pluggable status-provider contract with that existing policy and exact-head receipt behavior when reconciling latest main, rather than creating a competing configuration or duplicating CG467. Preserve real failures, source attribution, and current review/merge guards. This note does not interrupt or restart the active worker and does not clear any substantive review finding.
- 2026-09-09T10:59:32+00:00 discovered work filed: CG-469
- 2026-09-09T10:59:32+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:35:18+00:00 check did not run (20260909T105941Z-check): timed out; will retry
- 2026-09-09T12:36:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Implemented exact-head refresh, authoritative transported validation evidence, and controller-side GitHub status caching/rate-limit recovery. Current head 990d5a14 passed 66 focused tests and Ruff; the single full-suite attempt had 1724 passes and four supervisor-environment failures, with the one genuine contract mismatch fixed afterward. cost=$4.23
- 2026-09-09T12:37:03+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/brief.py, src/garden/scheduler/poll.py, src/garden/scheduler/review.py, tests/scheduler/test_poll.py); a rebase agent will resolve it
- 2026-09-09T12:37:06+00:00 dispatched rebase run 20260909T123706Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~7335 tokens)
- 2026-09-09T12:44:44+00:00 pre-PR checks failed (lint, syntax); revise run will fix before the PR is updated cost=$0.05
- 2026-09-09T13:03:43+00:00 dispatched revise run 20260909T130342Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16033 tokens)
- 2026-09-09T13:20:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:21:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Repaired the rebase-introduced syntax and lint failures and aligned the automerge fixture with command-backed validation policy. Commit 6bde2991 passed 53 focused tests, repository-wide Ruff, Python compilation, and diff/conflict checks. cost=$0.56
- 2026-09-09T13:26:03+00:00 automated review requested changes: The exact-head foundation works in focused tests, but GitHub status-context compatibility and per-product validation-policy integration remain incomplete. cost=$0.62
- 2026-09-09T13:27:42+00:00 dispatched revise run 20260909T132742Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16529 tokens)
- 2026-09-09T13:56:47+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:00:44+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Exact-head GitHub polling now combines Check Runs with commit status contexts, while per-product command validation consistently uses Garden-owned exact-head worker receipts for ingestion, review, and merge eligibility. Verified commit e63cd386 with 573 focused tests passing, 1 skipped, 4 stress tests deselected, and repository-wide Ruff clean. cost=$2.20
- 2026-09-09T14:03:58+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-09T14:04:09+00:00 dispatched rebase run 20260909T140408Z-rebase-2 via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3779 tokens)
- 2026-09-09T14:06:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Rebased onto origin/main and preserved both exact-head CI checks and pluggable status-provider behavior. cost=$0.01
- 2026-09-09T14:15:20+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/github.py); a rebase agent will resolve it
- 2026-09-09T14:20:16+00:00 dispatched rebase run 20260909T142016Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3910 tokens)
- 2026-09-09T14:23:48+00:00 automated review: request_changes — The exact-head provider and policy integration are broadly implemented, but worker-check eligibility can select an older receipt instead of the latest attempt. cost=$0.52
- 2026-09-09T14:47:56+00:00 check did not run (20260909T142701Z-check): idle 21 min (no output or file change); will retry
- 2026-09-09T14:54:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Rebased CG-396 onto origin/main and resolved the github.py conflict. cost=$0.01
- 2026-09-09T14:57:23+00:00 CI failure
- 2026-09-09T15:20:56+00:00 automated review:  —
- 2026-09-09T15:21:11+00:00 dispatched revise run 20260909T152110Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16568 tokens)
- 2026-09-09T16:46:08+00:00 revision failed: worker idle 83 min (no output or file change)
- 2026-09-09T17:25:14+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T17:32:32+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T17:35:09+00:00 dispatched revise run 20260909T173509Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16758 tokens)
- 2026-09-09T17:36:23+00:00 environment stop (materialization): the worker could not prepare an isolated checkout; branch not blamed and attempt not counted; feedback restored, will retry the revise round
- 2026-09-09T17:53:02+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T17:55:22+00:00 dispatched revise run 20260909T175522Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16869 tokens)
- 2026-09-09T18:26:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T18:29:38+00:00 check did not run (20260909T182641Z-check): check execution did not complete

worker materialization failed during checkout: Command '['git', 'checkout', '-B', '', 'origin/']' returned non-zero exit status 128.; preserved at /var/lib/garden-worker/work/preserved-materializations/CG-396/20260909T182641Z-check-9933cde54c10; will retry
- 2026-09-09T18:51:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Worker-check eligibility now orders durable receipts by supervised execution time and fails closed on a malformed latest exact-head attempt instead of falling back to older green evidence. Verified with 175 focused tests after the final change, an earlier 288-test affected suite, repository-wide Ruff, and git diff checks; committed as 665c284e. cost=$1.31
- 2026-09-09T18:51:20+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py, tests/scheduler/test_poll.py); a rebase agent will resolve it
- 2026-09-09T18:51:22+00:00 dispatched rebase run 20260909T185121Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~4830 tokens)
- 2026-09-09T18:53:45+00:00 automated review: request_changes — Focused tests pass, but malformed newest worker-check evidence can either fall back to an older green receipt or raise an exception instead of failing closed. cost=$0.31
- 2026-09-09T18:57:33+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.05
- 2026-09-10T02:07:59+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T13:54:09+00:00 triage: changes requested by hand: The recorded conditional deferral is now satisfied: CG-434/PR327 merged into main at2026-09-10T05:22:49Z (merge a2a4a528
- 2026-09-10T13:55:24+00:00 dispatched revise run 20260910T135524Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18038 tokens)
- 2026-09-10T14:14:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:15:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Reconciled PR 343 with current main and CG-434, then fixed newest malformed exact-head receipts so missing-command and non-object evidence cannot fall back to an older green result. Current head 7a367715 passed 352 affected tests, targeted GitHub/UI coverage, repository-wide Ruff, and diff/conflict checks. cost=$3.45
- 2026-09-10T14:19:33+00:00 automated review requested changes: Worker receipts now fail closed as intended, but exact-head GitHub status remains incomplete for repositories with more than 100 checks or status contexts. cost=$0.37
- 2026-09-10T14:31:06+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:31:28+00:00 dispatched revise run 20260910T143128Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18413 tokens)
- 2026-09-10T14:36:09+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:37:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Paginated both authenticated gh exact-head status endpoints and fail closed when pagination is incomplete or malformed. Commit 4982fb23 passed all 87 tests in tests/test_github_hosts.py and repository-wide Ruff. cost=$0.64
- 2026-09-10T14:40:19+00:00 automated review requested changes: The provider integration is broadly covered, but the REST-backed GitHub status path can incorrectly report green from incomplete evidence. cost=$0.32
- 2026-09-10T14:49:48+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:52:45+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T14:52:59+00:00 dispatched revise run 20260910T145259Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18799 tokens)
- 2026-09-10T14:57:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:59:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/343: Committed c0207b27, aligning REST exact-head status completeness with the gh-backed path. Verified 91 GitHub-provider tests pass, repository-wide Ruff is clean, affected files compile, and the committed diff has no whitespace errors. cost=$0.80
- 2026-09-10T15:04:05+00:00 automated review: approve — Exact-head GitHub and durable worker-check providers fail closed and correctly gate review and merge eligibility under per-product policy. cost=$0.67
- 2026-09-10T15:09:22+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T15:10:53+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/343
