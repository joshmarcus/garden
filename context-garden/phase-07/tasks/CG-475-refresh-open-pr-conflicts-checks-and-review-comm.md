---
id: CG-475
title: Refresh open PR conflicts, checks, and review comments
status: done
product: context-garden
phase: phase-07
depends_on:
- id: CG-472
  after: merge
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/rebase.py
- src/garden/github.py
- src/garden/web/pages/board.py
- src/garden/web/templates/_board.html
- src/garden/config.py
branch: garden/cg-475-refresh-open-pr-conflicts-checks-and-review-comm
pr: https://github.com/joshmarcus/context-garden/pull/371
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T15:30:17+00:00'
created: '2026-09-09T11:15:32+00:00'
updated: '2026-09-09T15:47:52+00:00'
---

## Goal

Extend the existing PR polling and the board's new PRs tab so open pull requests stay current for check/validation status, GitHub mergeability and conflicts, and incremental new review comments without creating a second independent poller.

## Existing coverage

Garden already polls task-linked PRs in active review states. That path refreshes the PR check rollup and failed checks, reads GitHub mergeability independently of CI, fetches review feedback incrementally, deduplicates ignored feedback, and routes actionable conflicts, failures, and trusted comments through the normal task workflow. Preserve and reuse it.

## Acceptance criteria

- [ ] Reuse or factor the existing repository/GitHub polling path to refresh the open PR records shown by CG-472. Cover open unlinked PRs as observation records and avoid a competing timer, duplicate GitHub fetch, or separate source of truth.
- [ ] Refresh configured CI/check or validation-provider state following CG-467. Do not assume GitHub Actions exists, and preserve pending, failure, success, unavailable, permission, and unknown states honestly.
- [ ] Refresh GitHub mergeability/conflict metadata as its own fact. Never infer “no conflict” from green CI or stale local data, and bind any actionable transition or display to the current PR head.
- [ ] Fetch new review comments incrementally with a durable cursor or equivalent identity-based deduplication. Backoff, rate limits, transient errors, restarts, and repeated pages must not lose a comment or create repeated actions.
- [ ] For an automatic Garden task, route a current actionable conflict, configured validation failure, or trusted review comment through the existing normal workflow and its revision, review, budget, head-freshness, and attempt limits. Do not bypass existing trust or approval rules.
- [ ] For unlinked PRs, display refreshed facts without inventing a Garden task or automatically changing source. For tasks reserved in Manual mode by CG-473, polling and display remain read-only: record visible facts while suppressing automatic revise, review, rebase, recovery, and merge actions.
- [ ] Scope polling to open PRs in the selected/configured product repository, stop tracking closed entries in the default CG-472 view, and preserve repository and enterprise-host credential boundaries. Surface fetch errors and stale timestamps without turning them into empty or successful state.
- [ ] Add focused deterministic tests for linked and unlinked PR refresh, head changes, conflicts distinct from CI, incremental comment deduplication across restarts, configured non-Actions validation, backoff/rate limiting, Manual-mode observation without action, and recovery after a transient fetch failure.

## Scope

Extend the current scheduler/GitHub abstraction and CG-472 data flow. Do not build a generic webhook service, a second dashboard, a new CI provider framework, or broad PR management for unlinked pull requests.

## Log

- 2026-09-09T11:15:32+00:00 approved (owner-requested open PR status/conflict/comment polling; preserves existing linked-task poller and Manual-mode read-only behavior)
- 2026-09-09T11:32:14+00:00 dispatched work run 20260909T113214Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14392 tokens)
- 2026-09-09T11:46:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:47:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/371 (base main): Open PR facts now refresh through the scheduler's existing polling phase and persist for the Board, avoiding page-driven GitHub polling and duplicate linked-PR fetches. Verified focused scheduler, web, GitHub transport, restart, deduplication, Manual-mode, backoff, and recovery coverage plus repository-wide lint. cost=$3.41
- 2026-09-09T12:03:28+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/github.py, src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-09T12:03:31+00:00 dispatched rebase run 20260909T120331Z-rebase-2 via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1666 tokens)
- 2026-09-09T12:04:38+00:00 automated review: request_changes — The scheduler/Board integration is coherent, but REST-based feedback polling is not paginated and can permanently omit actionable comments. cost=$0.50
- 2026-09-09T12:07:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: Resolved the two rebase conflicts while preserving open-PR polling, CI safeguards, feedback deduplication, and commit metadata. cost=$0.02
- 2026-09-09T12:17:38+00:00 operator current-head CI diagnosis added to pending feedback while active review ownership was preserved
- 2026-09-09T12:22:06+00:00 automated review requested changes: The scheduler/Board integration is coherent, but token-only REST feedback polling can permanently omit actionable comments beyond the first page. cost=$0.35
- 2026-09-09T12:22:18+00:00 dispatched revise run 20260909T122218Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15727 tokens)
- 2026-09-09T12:27:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:28:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: REST feedback polling now paginates all three comment/review collections, so actionable feedback after the first 100 records is observed and remains covered by durable identity deduplication. The canary MemoryGitHub open-PR observation now advances pending check latency like the production-enriched path; focused scheduler, Board, GitHub, and canary tests passed at 99045a5692236a9fa3cbd1f4f5d85ccf04548417, and repository-wide Ruff lint passed. cost=$0.83
- 2026-09-09T12:32:40+00:00 automated review requested changes: The scheduler-owned observation flow and feedback pagination are coherent, but REST-authenticated repositories still lose required conflict and check-error states. cost=$0.47
- 2026-09-09T12:32:51+00:00 dispatched revise run 20260909T123251Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16148 tokens)
- 2026-09-09T12:36:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:38:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: REST-backed PR polling now preserves explicit GitHub conflicts and check-rollup permission/unavailable failures instead of presenting unknown or empty states. Verified commit e1a09dcf822c3ac5f13e2b9527a61d77277029a5 with 201 focused tests and repository-wide Ruff lint. cost=$0.59
- 2026-09-09T12:42:44+00:00 automated review requested changes: The shared scheduler observation flow is coherent, but initial feedback migration and REST check pagination can cause incorrect actions or status. cost=$0.60
- 2026-09-09T12:43:42+00:00 dispatched revise run 20260909T124341Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16429 tokens)
- 2026-09-09T13:20:14+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:21:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: REST-backed PR observations now aggregate every check-run page, and upgraded linked PRs seed historical feedback identities from their established cursor without repeating actions. Verified 90 focused scheduler/GitHub tests and repository-wide Ruff lint at commit 8d52046a0aed294a40ac833838f9d1f5c5f76ff4. cost=$0.70
- 2026-09-09T13:26:05+00:00 automated review requested changes: The shared observation path, pagination, deduplication, REST state handling, and Board integration are otherwise coherent, but rate-limit backoff is bypassed for linked PRs. cost=$0.39
- 2026-09-09T13:29:10+00:00 dispatched revise run 20260909T132910Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16535 tokens)
- 2026-09-09T13:38:01+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:39:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: Linked PR polling now honors repository refresh failures and rate-limit backoff without issuing fallback per-task GitHub requests. Focused scheduler polling tests, broader GitHub/Board suites, diff checks, and repository-wide Ruff lint passed at e83b18a54d5e1075e1c4c42e55ce076db9f964e0. cost=$0.64
- 2026-09-09T13:44:34+00:00 automated review requested changes: The shared polling path and focused coverage are coherent, but REST PR-detail failures are incorrectly presented as successful refreshes and can erase current-head conflict metadata. cost=$0.40
- 2026-09-09T13:46:19+00:00 dispatched revise run 20260909T134619Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16885 tokens)
- 2026-09-09T13:51:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:00:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: REST PR-detail failures now mark repository observations stale and preserve the prior snapshot instead of persisting an incomplete successful refresh. Verified commit a115af615793e9d7bb4c7d642a3bc0f6e2eefb17 with 92 focused GitHub/scheduler tests and repository-wide Ruff lint. cost=$0.63
- 2026-09-09T14:03:47+00:00 CI failure
- 2026-09-09T14:05:33+00:00 dispatched revise run 20260909T140533Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16715 tokens)
- 2026-09-09T14:39:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:52:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: Fixed the full-suite CI regression by allowing configured CI analysis to reconsider the same-head failure after a flaky rerun, while retaining obsolete-head guards and the one-rerun limit. Verified commit 87786c84d487104d44c36b7dd53d3753e619f2a3 with the full ordinary suite (1910 passed, 4 skipped, 4 stress tests deselected), focused regression coverage (23 passed), and repository-wide Ruff lint. cost=$1.33
- 2026-09-09T15:00:05+00:00 automated review requested changes: The shared scheduler observation flow is coherent, but REST-backed status validation is not actually refreshed. cost=$0.52
- 2026-09-09T15:02:44+00:00 dispatched revise run 20260909T150244Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17372 tokens)
- 2026-09-09T15:10:44+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:12:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: REST-backed PR polling now combines commit status contexts with check runs for the current head, so configured non-Actions validation is refreshed honestly. Verified at commit 6842dd1a with 121 focused GitHub/scheduler tests, repository-wide Ruff lint, and a clean final diff. cost=$0.58
- 2026-09-09T15:19:43+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: refresh configured ci/check or validat; run `garden triage CG-475 --changes "<feedback>" to unblock`
- 2026-09-09T15:29:02+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T15:29:06+00:00 priority 2 -> 1 (web)
- 2026-09-09T15:30:17+00:00 dispatched revise run 20260909T153017Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17718 tokens)
- 2026-09-09T15:35:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:39:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/371: REST polling now fetches check runs and commit statuses independently, preserving accessible configured validation results when the other GitHub endpoint is forbidden or unavailable. Committed as 0aba7db8; 95 focused tests passed and repository-wide Ruff lint is clean. cost=$0.56
- 2026-09-09T15:43:22+00:00 automated review: approve — The shared scheduler-owned observation flow correctly refreshes linked and unlinked open PR facts while preserving head-bound actions, Manual-mode read-only behavior, durable feedback deduplication, and explicit provider/error states. cost=$0.43
- 2026-09-09T15:46:13+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T15:47:52+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/371
