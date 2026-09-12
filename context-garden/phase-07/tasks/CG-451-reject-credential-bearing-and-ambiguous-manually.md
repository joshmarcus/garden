---
id: CG-451
title: Reject credential-bearing and ambiguous manually adopted PR URLs
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-395
priority: 1
difficulty: medium
reading:
- src/garden/github.py
- src/garden/cli/loop.py
- src/garden/scheduler/dispatch.py
- tests/test_cli.py
branch: garden/cg-451-reject-credential-bearing-and-ambiguous-manually
pr: https://github.com/joshmarcus/context-garden/pull/341
runner: remote
discovered_from: Owner criteria/enterprise review audit2026-09-08
attempts: 1
last_dispatched_at: '2026-09-09T01:45:41+00:00'
created: '2026-09-08T19:24:46+00:00'
updated: '2026-09-09T03:41:10+00:00'
---

## Goal

Prevent manual PR adoption from persisting a raw secret-bearing or ambiguous URL.

Sol audited mergedPR307/head669f519a: pull_request_number returns7 for https://user:secret@forge-one.test/Team/Repo/pull/7?token=synthetic#x. These are synthetic strings, not credentials. garden take passes the raw external_pr to dispatch, which stores task.pr.

## Acceptance criteria

- [ ] Reject PR URLs containing userinfo/passwords, query strings, fragments or ambiguous unsupported URL components before storing task/run state.
- [ ] Ordinary valid configured enterprise and public PR URLs preserve canonical host/repository identity and case policy.
- [ ] Parser and CLI adoption regressions use synthetic values and prove rejected URLs create no secret-bearing task/run link.

## Log

- 2026-09-08T19:24:46+00:00 approved (owner-delegated-hourly-audit)
- 2026-09-08T19:26:13+00:00 dispatched work run 20260908T192612Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~10345 tokens)
- 2026-09-08T19:34:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/341 (base main): Manual PR adoption now rejects credential-bearing and decorated URLs before provider lookup or state persistence, with a dispatch-level guard against bypasses. Parser and CLI regressions cover synthetic unsafe values plus enterprise/public case-preserving URLs. cost=$0.54


## Delegated Input CI audit

Delegated Input CI audit at 2026-09-08T21:39:00.619967+00:00 for current head 624486d7bae61f49aa5f42f3701b835111ae248e:
test	UNKNOWN STEP	2026-09-08T19:43:06.8857314Z E                   RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2542941Z E                   RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2552616Z FAILED tests/scheduler/test_human.py::test_external_open_pr_uses_claimed_identity_and_review_without_managed_worktree - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2553964Z FAILED tests/scheduler/test_human.py::test_external_claim_persists_actual_identity_before_finish - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2555102Z FAILED tests/scheduler/test_human.py::test_external_completion_pr_lookup_failure_is_audited[GitHubError] - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2556225Z FAILED tests/scheduler/test_human.py::test_external_completion_pr_lookup_failure_is_audited[KeyError] - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2557792Z FAILED tests/scheduler/test_human.py::test_external_merged_pr_completes_without_rechecks_after_final_base_verification - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2559070Z FAILED tests/scheduler/test_human.py::test_external_merged_pr_restacks_its_child - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2560150Z FAILED tests/scheduler/test_human.py::test_external_stacked_merged_pr_is_not_completed_until_it_reaches_final_base - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2561301Z FAILED tests/scheduler/test_human.py::test_external_completion_git_guard_violation_is_refused_and_failed - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2562435Z FAILED tests/test_stabilization.py::test_sample_excludes_a_completed_merged_external_pr_from_unattended_work - RuntimeError: external PR must be a GitHub URL for this repository
test	UNKNOWN STEP	2026-09-08T19:43:07.2563549Z 9 failed, 1712 passed, 3 skipped, 4 deselected, 2 warnings in 485.11s (0:08:05)
Original full diagnostics: /home/joshua/work/operator-test-tmp/input-sweep-20260908T2125/pr-341-ci-34269733651.log.
The nine exact-head failures reject valid synthetic external PR fixtures at the new URL guard. Preserve the credential/host protection and repair valid supported identity/fixture handling. Retain every existing review finding; this note supplements it. Use bounded focused same-environment verification rather than repeating the unchanged full suite.
- 2026-09-09T00:29:19+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_github_hosts.py); a rebase agent will resolve it
- 2026-09-09T00:29:24+00:00 dispatched rebase run 20260909T002924Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~4827 tokens)
- 2026-09-09T00:32:27+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/341: Rebased onto origin/main and resolved the test_github_hosts.py conflict while preserving both sides. cost=$0.01
- 2026-09-09T01:44:43+00:00 automated review requested changes: The URL parser and CLI regressions satisfy the frozen criteria, but the dispatch-level guard breaks nine established external-PR lifecycle tests by rejecting valid provider-supplied PR identities. Repair the compatibility boundary and rerun the affected scheduler tests. cost=$0.34
- 2026-09-09T01:45:41+00:00 dispatched revise run 20260909T014538Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~13088 tokens)
- 2026-09-09T01:54:13+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/341: Preserved strict CLI validation for manually entered PR URLs while allowing safe provider-returned identities with verified PR numbers at dispatch. Unsafe provider identities are rejected before task or run persistence. cost=$0.52
- 2026-09-09T02:22:58+00:00 automated review: approve — Unsafe manually supplied and provider-returned PR URLs are rejected before persistence, while valid public, enterprise, and opaque provider identities remain supported. cost=$0.24
- 2026-09-09T02:23:18+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T02:35:42+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/341
- 2026-09-09T03:41:10+00:00 automated review could not start: CG-451 is done: #341 was merged at 02:35:42
