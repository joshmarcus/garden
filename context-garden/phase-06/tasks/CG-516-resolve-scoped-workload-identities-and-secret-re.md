---
id: CG-516
title: Resolve scoped workload identities and secret references at the execution boundary
status: done
product: context-garden
phase: phase-06
depends_on:
- CG-399
- CG-401
- CG-415
priority: 1
difficulty: hard
reading:
- src/garden/config.py
- src/garden/runner/base.py
- src/garden/remote_worker.py
- src/garden/managed_worker.py
- docs/worker-protocol.md
- context-garden/phase-06/specs/context-garden-stripe-environment.md
branch: garden/cg-516-resolve-scoped-workload-identities-and-secret-re
pr: https://github.com/joshmarcus/context-garden/pull/429
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T17:19:09+00:00'
created: '2026-09-10T11:18:51+00:00'
updated: '2026-09-10T17:25:13+00:00'
---

## Goal

Resolve logical credential references into least-privilege workload authority only at the operation boundary. Support short-lived identity providers without copying a human profile, distinguish automation from human identity in audit records, and fail closed when scope, audience, membership, renewal or revocation requirements are not satisfied.

## Context

CG-401 safely maps approved tool configuration and CG-399 keeps physical identities out of shared records. CG-400 was cancelled at the owner's request and must not be revived wholesale. This task is the smaller executable resolver contract needed by enterprise source, package, tool and worker operations.

This new scope is authorized by the owner's request to turn the enterprise environment specification into deduplicated Phase 06 work. It owns runtime resolution and enforcement only; it does not restore CG-400's policy-definition exercise or make deployment-specific identity decisions.

## Acceptance criteria

- [ ] Add a trusted resolver interface receiving a logical reference, operation, audience, run identity and requested lifetime; return only bounded authority plus non-secret issuer/expiry metadata.
- [ ] Permit provider adapters from trusted local configuration with explicit capabilities and versioning. Task text, worker output and repository files cannot register providers or request broader scopes.
- [ ] Pass resolved authority only to the named subprocess or protocol request. Never persist or emit credential values in claims, briefs, transcripts, notifications, diagnostics or committed configuration.
- [ ] Handle expiry, renewal, revocation, missing membership and unavailable providers as actionable environment failures without consuming an author revision or falling back to ambient credentials.
- [ ] Use synthetic identity providers to verify audience/scope mismatch, short lifetime, renewal, revocation, concurrent runs, redaction and local/remote equivalence on supported platforms.

enterprise_capability_key: enterprise-workload-identity-resolver

## Log

- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:39:34+00:00 dispatched work run 20260910T113934Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18797 tokens)
- 2026-09-10T11:52:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:53:33+00:00 opened https://github.com/joshmarcus/context-garden/pull/429 (base main): Added a trusted, versioned workload identity resolver with bounded operation/audience/scope/lifetime policies, metadata-only audit identity, ephemeral subprocess/header delivery, renewal and fail-closed validation. Verified with 82 focused workload-identity and runner tests plus clean project lint. cost=$0.94
- 2026-09-10T11:56:43+00:00 automated review requested changes: The resolver is well-tested in isolation, but it is not connected to any execution boundary, so the requested runtime enforcement and environment-failure handling are not implemented. cost=$0.31
- 2026-09-10T12:52:01+00:00 dispatched revise run 20260910T125201Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20064 tokens)
- 2026-09-10T13:06:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:07:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/429: Connected trusted workload identity resolution to local and managed-remote worker execution boundaries, enforced named targets, isolated credentials from setup, and routed resolution failures through environment-error recovery without consuming author attempts. Verified commit 6949a220 with 106 focused tests and clean project lint. cost=$2.35
- 2026-09-10T13:12:08+00:00 automated review requested changes: Execution-boundary resolution is now integrated, but credential values are not redacted from worker output before persistence or remote transcript upload. cost=$0.69
- 2026-09-10T13:12:31+00:00 dispatched revise run 20260910T131231Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20379 tokens)
- 2026-09-10T13:19:35+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:19:36+00:00 revision failed: remote worker finished without pushing commits
- 2026-09-10T13:45:21+00:00 triage: marked ready for review (Recovered the exact original worker commit06bcf53e by verified fast-forward from its already-publish)
- 2026-09-10T13:49:45+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: pass resolved authority only to the na; run `garden triage CG-516 --changes "<feedback>" to unblock`
- 2026-09-10T14:02:20+00:00 triage: changes requested by hand: Continue from the recovered published commit06bcf53e; do not repeat the publication repair or discard its code. The actu
- 2026-09-10T14:05:37+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:06:44+00:00 dispatched revise run 20260910T140644Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21371 tokens)
- 2026-09-10T14:59:08+00:00 revision failed: worker idle 20 min (no output or file change)
- 2026-09-10T15:21:22+00:00 triage: marked ready for review (Recovered the exact existing worker commit762c59cd by verified non-force fast-forward of PR429 from0)
- 2026-09-10T15:22:15+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-10T15:22:22+00:00 dispatched rebase run 20260910T152222Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2059 tokens)
- 2026-09-10T15:26:08+00:00 pre-PR checks failed (lint, syntax); revise run will fix before the PR is updated cost=$0.02
- 2026-09-10T15:34:11+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T15:34:27+00:00 dispatched revise run 20260910T153426Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20727 tokens)
- 2026-09-10T15:37:50+00:00 worker blocked: Committed the bounded Popen environment correction at d564f36d. Python compilation and full Ruff lint pass; direct execution of the supervisor workload-identity integration test passes, but ordinary pytest collection is blocked by an unrelated circular import in the rebased head. cost=$0.62
- 2026-09-10T15:55:37+00:00 triage: marked ready for review (Preserved exact blocked-run source d564f36dae29656c875cd740f7cb18330dec2f19 by guarded non-force fas)
- 2026-09-10T15:56:45+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/config.py); a rebase agent will resolve it
- 2026-09-10T15:56:50+00:00 dispatched rebase run 20260910T155649Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2351 tokens)
- 2026-09-10T15:59:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/429: Rebased onto origin/main and resolved the config conflict by preserving both sides' executable keys. cost=$0.01
- 2026-09-10T16:03:31+00:00 automated review requested changes: Managed-remote credential handling still persists raw worker output before redaction, and the focused identity/remote-worker suite fails. cost=$0.47
- 2026-09-10T16:06:49+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T16:29:49+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T16:30:43+00:00 dispatched revise run 20260910T163042Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21739 tokens)
- 2026-09-10T16:52:52+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:54:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/429: Committed f046dc93, moving managed-remote identity resolution into the streaming supervisor so stdout, stderr, final output, transcripts, and finish payloads contain only redacted authority. The focused identity/remote-worker suite passed 118 tests and full Ruff lint passed. cost=$2.55
- 2026-09-10T16:58:24+00:00 automated review: approve — Scoped workload authority is resolved from trusted host configuration at local and managed-remote execution boundaries, with fail-closed lifecycle enforcement and redaction before persistence or upload. cost=$0.48
- 2026-09-10T17:06:41+00:00 triage: changes requested by hand: Preserve the independently approved scoped-authority resolution, lifecycle enforcement and pre-persistence redaction (11
- 2026-09-10T17:09:17+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T17:10:25+00:00 dispatched revise run 20260910T171024Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21608 tokens)
- 2026-09-10T17:17:41+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:18:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/429: Committed 59f666c8 to correct supervisor output-channel ownership while preserving parallel model sessions, serialized heavy validation, and pre-persistence credential redaction. The combined runner, workload-identity, and remote-worker suite passed 173 tests, and full project Ruff lint passed. cost=$1.11
- 2026-09-10T17:19:05+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/config.py); a rebase agent will resolve it
- 2026-09-10T17:19:09+00:00 dispatched rebase run 20260910T171909Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3158 tokens)
- 2026-09-10T17:25:08+00:00 pre-PR checks failed (lint) (still failing after a rebase onto `main`); revise run will fix before the PR is updated cost=$0.03
- 2026-09-10T17:25:13+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/429
