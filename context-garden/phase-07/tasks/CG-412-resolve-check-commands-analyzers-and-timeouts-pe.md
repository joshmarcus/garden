---
id: CG-412
title: Resolve check commands analyzers and timeouts per product
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-412-resolve-check-commands-analyzers-and-timeouts-pe
pr: https://github.com/joshmarcus/context-garden/pull/317
runner: remote
attempts: 1
last_dispatched_at: '2026-09-11T10:55:09+00:00'
created: '2026-09-07T20:05:52+00:00'
updated: '2026-09-11T11:15:06+00:00'
---

## Goal

Resolve check commands analyzers and timeouts per product. Recheck current implementation before choosing the smallest compatible change.

## Acceptance criteria

- [ ] Provide product overrides for pre-PR checks, CI analyzers and check timeout, with documented inheritance and explicit empty-list semantics.
- [ ] Use one resolver in synchronous and detached checks, CI failure analysis, base probes and check continuations; preserve product setup environment and per-check overrides.
- [ ] Persist effective settings for an in-flight run so another product or later config edit cannot silently change its validation contract.
- [ ] Validate a lightweight document product beside a heavyweight compiled product without shell product switches. Integrate shared configuration metadata/locks from CG-349 when available.

## Provenance and scope

Owner-provided additional gap F4, 2026-09-07. Generic requirements only. This task remains a phase-07 draft and does not authorize new access, deployment or external notifications. Refer to the shared spec, not the private environment survey.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T13:52:48+00:00 dispatched work run 20260908T135248Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9191 tokens)
- 2026-09-08T14:54:30+00:00 opened https://github.com/joshmarcus/context-garden/pull/317 (base main): Added product-level check, CI analyzer, and timeout overrides with explicit empty-list semantics. Check contracts now flow through one resolver and are snapshotted for detached checks and continuations. cost=$3.04
- 2026-09-08T15:46:39+00:00 automated review produced no verdict (idle 58 min (no output or file change))
- 2026-09-08T16:05:21+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/checkruns.py); a rebase agent will resolve it
- 2026-09-08T16:12:10+00:00 dispatched rebase run 20260908T161210Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~955 tokens)
- 2026-09-08T16:28:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/317: Rebased onto origin/main and resolved the checkruns.py conflict preserving both product check settings and execution metadata. cost=$0.02
- 2026-09-08T16:46:56+00:00 automated review produced no verdict (idle 23 min (no output or file change))
- 2026-09-08T19:23:55+00:00 Operator verified deployment-era interrupted check/review, preserved failed record, queued exactly one current-head replay/review through current controller runtime; no implementation retry.
- 2026-09-08T21:14:30+00:00 automated review requested changes: Product-level contracts are largely implemented and focused validation passes, but the shared resolver contaminates CI analyzer specs with required pre-PR checks. The required served-interaction evidence is also unavailable at the supplied path. cost=$0.30
- 2026-09-09T01:53:00+00:00 Operator restored queued author to remote after current-source check routing inspection: no generated capture pages or controller-owned spec paths. Full substantive feedback preserved; current owner proportional-validation policy appended. No active run or cap changed.
- 2026-09-09T02:02:20+00:00 dispatched revise run 20260909T020220Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~12805 tokens)
- 2026-09-09T02:30:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/317: CI analyzer resolution no longer appends required pre-PR checks. Product-specific check contracts, detached continuation snapshots, and environment overrides remain covered by focused tests. cost=$0.40
- 2026-09-09T03:01:55+00:00 automated review: approve — Product-specific check contracts are correctly resolved, isolated by stage, and persisted across detached continuations and configuration changes. cost=$0.33
- 2026-09-09T03:52:01+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T04:01:07+00:00 CI failure
- 2026-09-09T04:01:37+00:00 dispatched revise run 20260909T040137Z-revise-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~12948 tokens)
- 2026-09-09T04:02:45+00:00 automated review: approve — Product-specific pre-PR checks, CI analyzers, environments, and timeouts are resolved independently and persisted across continuations and configuration changes. cost=$0.26
- 2026-09-09T04:09:34+00:00 revision failed: worker exited 1: {'message': "You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 15th, 2026 2:14 AM."}
- 2026-09-09T09:45:17+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T09:45:44+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-412`) or send it back (`garden triage CG-412 --changes "..."`)
- 2026-09-09T09:47:00+00:00 cancelled (web)
- 2026-09-11T10:11:14+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/317 (garden/cg-412-resolve-check-commands-analyzers-and-timeouts-pe@7313228e6bdcbc8e280289a8aa842991c933b37d, pr_number 317 -> 317)
- 2026-09-11T10:11:15+00:00 Reactivated by delegated operator under owner all-human-actions review authority September11 10:07UTC; adopt actual PR317 head7313228e6bdc and return to normal rebase/CI/review. Preserve original cancellation, failures, reviews and source; no fresh author attempt or allowance.
- 2026-09-11T10:12:19+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/config.py, src/garden/scheduler/checkruns.py, src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-11T10:12:21+00:00 dispatched rebase run 20260911T101220Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2167 tokens)
- 2026-09-11T10:16:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/317: Rebased CG-412 onto origin/main and resolved all conflicts while preserving product check settings, snapshots, staging, and validation behavior. cost=$0.03
- 2026-09-11T10:18:49+00:00 difficulty medium -> hard after unmet_acceptance_criteria: Base probes do not preserve the intended split between the failed subset executed by the probe and the full suite retained for a later rebase recheck.; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-11T10:18:49+00:00 automated review requested changes: Base probes do not preserve the intended split between the failed subset executed by the probe and the full suite retained for a later rebase recheck. cost=$0.28
- 2026-09-11T10:22:21+00:00 triage: changes requested by hand: Delegated operator all-human-actions review: the current independent reviewer reproduced a real failing regression at he
- 2026-09-11T10:22:55+00:00 dispatched revise run 20260911T102255Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2849 tokens)
- 2026-09-11T10:25:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T10:26:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/317: Corrected check payload precedence so call-specific base-probe specs execute without replacing the full persisted validation contract. Verified the regression, related product and continuation behavior, and lint on commit bf9525f4. cost=$0.44
- 2026-09-11T10:30:43+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: use one resolver in synchronous and de; run `garden triage CG-412 --changes "<feedback>" to unblock`
- 2026-09-11T10:33:38+00:00 triage: changes requested by hand: Delegated operator review of the10:30 stall: the prior payload-precedence defect is corrected and the reviewer passed119
- 2026-09-11T10:34:46+00:00 dispatched revise run 20260911T103446Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2860 tokens)
- 2026-09-11T10:38:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T10:40:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/317: Base-probe failure handling now selects failed checks from the persisted in-flight contract and preserves the original full suite, environment, and timeout for later rebase checks. Legacy continuations without a snapshot retain a documented live-config fallback; committed as 963b64c1. cost=$0.49
- 2026-09-11T10:42:51+00:00 automated review: approve — Product-specific check contracts are correctly resolved and snapshotted through detached checks, base probes, retries, and rebase rechecks. Exact-head CI remains pending as an independently enforced merge gate. cost=$0.46
- 2026-09-11T10:51:01+00:00 CI failure
- 2026-09-11T10:54:59+00:00 triage: changes requested by hand: Delegated operator diagnosed the exact-head real CI failures despite the remote analyzer's authentication error. Both CI
- 2026-09-11T10:55:09+00:00 dispatched revise run 20260911T105509Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2875 tokens)
- 2026-09-11T10:57:36+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T10:59:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/317: Updated the two worker-CI scheduler test doubles to inherit ReapMixin, preserving the production check-settings resolver and the existing publishing-policy and non-duplication assertions. Verified 131 focused tests and lint; exact-head CI remains the scheduler-enforced merge gate after push. cost=$0.28
- 2026-09-11T11:01:40+00:00 automated review: approve — Product-specific check contracts are correctly resolved, isolated by stage, and snapshotted across detached checks, base probes, retries, and rebase rechecks. Exact-head CI remains pending as an independently enforced merge gate. cost=$0.29
- 2026-09-11T11:13:28+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T11:15:06+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/317
