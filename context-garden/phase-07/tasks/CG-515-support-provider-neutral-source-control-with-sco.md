---
id: CG-515
title: Support provider-neutral source control with scoped certificate and proxy policy
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-395
- CG-396
- CG-467
priority: 1
difficulty: hard
reading:
- src/garden/github.py
- src/garden/config.py
- src/garden/checks.py
- src/garden/scheduler/poll.py
- docs/architecture.md
- context-garden/phase-06/specs/context-garden-stripe-environment.md
branch: garden/cg-515-support-provider-neutral-source-control-with-sco
pr: https://github.com/joshmarcus/context-garden/pull/427
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T17:04:09+00:00'
created: '2026-09-10T11:18:51+00:00'
updated: '2026-09-10T17:20:22+00:00'
---

## Goal

Define a provider-neutral source-control boundary for repository discovery, change requests, reviews, links and exact-source status while preserving the existing GitHub and GitHub Enterprise behavior. Apply endpoint-scoped certificate-authority and outbound-proxy policy through supported clients without disabling certificate verification or leaking authorization across endpoints.

## Context

CG-395 and CG-447 normalize explicit GitHub Enterprise identities, and CG-396/CG-467 separate validation policy from GitHub Actions. The remaining contract still assumes GitHub-shaped change requests and does not provide one safe connection-policy path for source and CI clients. Use synthetic services only.

## Acceptance criteria

- [ ] Introduce a narrow provider interface for repository identity, branch discovery, change-request metadata, reviews, links and exact-head status; retain the existing GitHub adapter without changing its safety gates.
- [ ] Configure web/API endpoints, credential references, certificate-authority bundles and proxies per product and operation. Reject mismatched authorities, unsafe redirects, invalid bundles and attempts to disable verification.
- [ ] Keep authentication failure, certificate failure, proxy failure, unavailable provider and unsupported operation distinct in diagnostics; never print credentials, private endpoints or proxy authorization.
- [ ] Preserve exact-head evidence, fresh conflict checks, atomic head guards, protected paths and external branch ownership across adapters. Unsupported merge/review capabilities fail closed.
- [ ] Exercise two synthetic providers with non-default base branches, stale heads, endpoint mismatch, redirect, proxy and custom-CA fixtures. No test contacts private infrastructure; existing GitHub behavior and lint remain clean.

enterprise_capability_key: enterprise-source-provider-network-trust

## Log

- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:37:04+00:00 dispatched work run 20260910T113703Z-work-3 via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an stacked on CG-396, ~16099 tokens)
- 2026-09-10T11:49:21+00:00 discovered work filed: CG-525
- 2026-09-10T11:49:21+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:50:42+00:00 opened https://github.com/joshmarcus/context-garden/pull/427 (base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an): Added a provider-neutral source-control contract and endpoint-scoped trust policy, retaining the GitHub/GHE adapter and scheduler safety gates. Verified 121 focused source-control/GitHub tests pass and `.venv/bin/ruff check src tests scripts` is clean. cost=$1.85
- 2026-09-10T11:55:15+00:00 automated review requested changes: The provider-neutral boundary and scoped transport policy are not wired through the operational scheduler path. Non-GitHub adapters are rejected, configured trust can be bypassed by `gh`, and new source-control routes skip the checkout identity guard. cost=$0.38
- 2026-09-10T11:55:40+00:00 dispatched revise run 20260910T115540Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an, ~17630 tokens)
- 2026-09-10T12:51:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T12:54:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/427: Wired provider factories through operational scheduler source-control routes, applied provider-neutral repository/link identity checks, preserved exact-head merge guards, and prevented scoped GitHub routes from falling back to ambient gh credentials. Verified 139 focused tests before the final authority fix, 16 current-head source-control tests afterward, and `.venv/bin/ruff check src tests scripts` clean on commit 5f3d34fe. cost=$3.32
- 2026-09-10T12:57:47+00:00 automated review requested changes: Provider-neutral routing and scheduler safety integration are substantially present, but invalid CA bundles are not actually rejected. cost=$0.43
- 2026-09-10T12:58:22+00:00 dispatched revise run 20260910T125822Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an, ~17335 tokens)
- 2026-09-10T13:05:58+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:07:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/427: Scoped CA bundles are now fully parsed during ConnectionPolicy construction, with malformed certificates and non-certificate content rejected before any request. Verified 20 focused source-control tests and repository-wide Ruff lint on committed head d1ae5ac0a1df7f24e049acaacf180de53cd37560. cost=$0.64
- 2026-09-10T13:10:43+00:00 automated review requested changes: The provider boundary and CA validation are substantially implemented, but legacy per-product GitHub trust settings can still be bypassed through ambient `gh`. cost=$0.42
- 2026-09-10T13:25:05+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T13:25:39+00:00 dispatched revise run 20260910T132539Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an, ~17898 tokens)
- 2026-09-10T13:37:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:39:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/427: Legacy products.<name>.github routes now use the scoped HTTP client whenever a credential reference, CA bundle, or proxy is configured, preventing ambient gh from bypassing endpoint policy. Verified 24 focused source-control tests and repository-wide Ruff lint on committed head 0d9f83ce90a132596d5268cabfafd6da7591478d. cost=$0.55
- 2026-09-10T13:42:58+00:00 automated review requested changes: The provider boundary is substantially implemented, but the REST error rewrite regresses GitHub rate-limit and authentication diagnostics. cost=$0.59
- 2026-09-10T15:09:37+00:00 stack parent CG-396 merging; retargeted this PR to main before the parent branch is deleted
- 2026-09-10T15:10:56+00:00 parent CG-396 merged; rebase onto main conflicts (src/garden/brief.py, src/garden/ci_status.py, src/garden/events.py, src/garden/scheduler/poll.py, src/garden/scheduler/reap.py, src/garden/scheduler/review.py, src/garden/web/templates/task.html, tests/scheduler/test_poll.py, tests/test_ci_status.py, tests/test_web.py); a rebase agent will resolve it
- 2026-09-10T15:16:15+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T15:17:20+00:00 dispatched rebase run 20260910T151720Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~9821 tokens)
- 2026-09-10T15:27:27+00:00 pre-PR checks failed (lint, syntax); revise run will fix before the PR is updated cost=$0.12
- 2026-09-10T15:27:42+00:00 dispatched revise run 20260910T152741Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19625 tokens)
- 2026-09-10T15:33:05+00:00 worker blocked: Committed the pre-PR syntax and lint repairs as 2929414b; `.venv/bin/ruff check src tests scripts` passes and `tests/test_source_control.py` passes 24/24. Broader focused validation found 60 substantive rebase regressions, so the branch is not safe to declare done. cost=$1.13
- 2026-09-10T15:55:39+00:00 triage: changes requested by hand: The previous bounded revision correctly returned BLOCKED: partial commit2929414b0ed776d31c4968e2af367561a1120cec made sy
- 2026-09-10T16:06:47+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T16:29:48+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T16:30:42+00:00 dispatched revise run 20260910T163042Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19181 tokens)
- 2026-09-10T16:51:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:52:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/427: Rebased only the provider-neutral source-control commits onto accepted current main, restored accepted receipt/status/locking behavior, and fixed GitHub REST rate-limit and authentication classification. Verified 625 affected tests, an additional 61 final-content poll/source-control tests, repository-wide Ruff lint, clean conflict-marker inspection, and a clean worktree. cost=$5.54
- 2026-09-10T16:55:38+00:00 automated review requested changes: The provider-neutral contract is incomplete for the operational polling path, so a conforming non-GitHub adapter fails after feedback cursors are established. cost=$0.42
- 2026-09-10T17:03:38+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T17:04:09+00:00 dispatched revise run 20260910T170408Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19231 tokens)
- 2026-09-10T17:10:13+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:11:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/427: Completed the provider-neutral scheduler contract on commit 69b32554. Both synthetic adapters now exercise first and incremental polling plus guarded branch/stack cleanup; 88 focused tests and repository-wide Ruff lint passed. cost=$0.98
- 2026-09-10T17:15:09+00:00 automated review: approve — The provider-neutral source-control boundary, scoped transport policy, and operational polling/cleanup integration satisfy the requested outcomes without weakening scheduler safety gates. cost=$0.60
- 2026-09-10T17:17:18+00:00 moved from context-garden/phase-06 to context-garden/phase-07
- 2026-09-10T17:20:22+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/427
