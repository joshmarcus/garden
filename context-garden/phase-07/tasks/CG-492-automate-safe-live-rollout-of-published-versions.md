---
id: CG-492
title: Automate safe live rollout of published versions to the worker fleet
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/upgrade.py
- src/garden/managed_worker.py
- src/garden/remote_worker.py
- src/garden/hosts/core.py
- src/garden/hosts/models.py
- src/garden/scheduler/upgrades.py
- tests/test_upgrade.py
- tests/test_managed_worker.py
branch: garden/cg-492-automate-safe-live-rollout-of-published-versions
pr: https://github.com/joshmarcus/context-garden/pull/492
runner: remote
attempts: 1
last_dispatched_at: '2026-09-11T14:50:41+00:00'
created: '2026-09-09T17:29:36+00:00'
updated: '2026-09-11T15:06:33+00:00'
---

## Goal

Turn the repeated operator rollout procedure into a supported, resumable Garden operation that installs one already-published immutable Garden version across the existing managed worker fleet and proves each worker healthy at that exact source before declaring success.

This task automates rollout to workers that already exist. It does not publish releases, create or replace hosts, enlarge the fleet, extend deadlines or budgets, widen credentials, or authorize a frozen phase to dispatch.

## Required behavior

- Accept an immutable published version plus its expected source commit and verified source manifest. Refuse mutable, mismatched, unverified, or partially specified candidates.
- Inventory the configured existing workers and persist a rollout plan before mutation. Preserve host identities, resource caps, aggregate budget, absolute owner deadlines, enrollment and secret boundaries, controller rollback runtime, and the prior worker runtime as rollback.
- Advance workers sequentially or through an explicitly bounded safe batch. Wait for an actual idle or accounted drain boundary, preserving active jobs, claim generations, worktrees, source, transcripts, results and pending collection. If a worker becomes busy after the plan was read, defer it and reconcile again rather than interrupting it.
- Install into a new versioned runtime and verify the package version, direct-url commit, source manifest/hash set, executable and required tool environment before switching the service.
- Apply the exact intended service configuration and ownership. Verify unit source, environment/config path, owner and group, file modes, executable path, advertised source head, unit freeze/thaw state, PID identity and readiness. Do not accept a stale PID, a daemon left frozen, an old unit definition, or a process that merely exists.
- Require stable live health after activation: repeated authenticated claim/heartbeat/finish compatibility probes or an equivalent non-destructive protocol journey, expected source/version reporting, and no restart loop or immediate resource failure. Mark a worker complete only after the stability window passes.
- Persist every per-worker transition, observation and receipt durably so an interrupted controller or operator can resume without reinstalling completed workers or forgetting a failed/deferred worker.
- On failure, stop advancing the rollout. Roll back the affected idle worker when the previous runtime is intact and rollback is safe; otherwise leave it fenced and report the exact recovery action. Never roll back or restart a worker that acquired live work after the last idle check.

## Acceptance criteria

- [ ] A supported command or API plans, starts, inspects, resumes and safely aborts a rollout of an immutable published version to the configured existing worker fleet. Repeating the same operation is idempotent; conflicting rollout identities are rejected.
- [ ] Durable per-worker state covers planned, waiting-for-idle, draining, staged, verified, activated, health-checking, complete, deferred, failed and rolled-back outcomes with timestamps and exact version/source identity.
- [ ] Activation is guarded by a fresh idle/claim check and preserves all active job, branch, source, transcript, result and collection state. A claim arriving between observation and mutation causes deferral.
- [ ] Staging and post-switch verification prove exact package/runtime/direct-url/source-manifest identity plus service config path, owner/group/mode, source-head advertisement, unit freeze state, PID identity and readiness.
- [ ] Success requires a bounded stable live-health window and protocol compatibility evidence. A single process check or one transient HTTP success is insufficient.
- [ ] Failure handling is sequential and resumable: later workers remain untouched, completed receipts remain valid, rollback uses the retained prior runtime only at a safe idle boundary, and a newly busy worker is deferred.
- [ ] Deterministic fixtures cover interrupted resume, stale PID reuse, wrong source hash with correct version text, wrong unit owner or mode, stale source-head environment, frozen-but-running unit, readiness timeout, restart loop after initial success, claim race at the drain boundary, partial-fleet failure and rollback failure. Add a bounded disposable-worker journey for the supported live protocol without consuming production work.
- [ ] Documentation explains release prerequisites, operator-visible progress, abort/resume/rollback semantics, retained evidence and the invariants for host identities, deadlines, budgets, resource caps and secrets.

## Relationship to existing work

Reuse the host lifecycle, managed-worker protocol, upgrade validation and durable scheduler state already present. CG-428 covers active remote runs across controller outages; preserve those guarantees. CG-423 covers fleet provisioning/bootstrap. This task owns version rollout orchestration for an existing fleet and must not duplicate host creation or release publication.

## Log

- 2026-09-09T17:29:36+00:00 owner requested and approved task registration for phase08; phase08 remains frozen, no freeze exception is granted, and dispatch waits for explicit phase release
- 2026-09-11T14:03:48+00:00 moved from context-garden/phase-08 to context-garden/phase-07
- 2026-09-11T14:04:30+00:00 dispatched work run 20260911T140430Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2639 tokens)
- 2026-09-11T14:13:40+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T14:15:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/492 (base main): Added a supported durable API and bounded command transport for safely rolling an immutable published Garden version across existing workers. Verified 22 rollout tests, 63 adjacent upgrade/managed-worker tests, Ruff lint, Python compilation, clean diff, and a clean committed worktree. cost=$1.28
- 2026-09-11T14:18:01+00:00 automated review requested changes: The rollout covers the intended safety checks, but resumability and crash durability remain incomplete. cost=$0.29
- 2026-09-11T14:18:12+00:00 dispatched revise run 20260911T141812Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2919 tokens)
- 2026-09-11T14:23:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T14:24:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/492: Fixed rollout crash resumability and journal durability in commit b4c4ce5f. Verified 67 focused rollout, upgrade, and managed-worker tests plus clean Ruff lint; the committed worktree is clean. cost=$0.62
- 2026-09-11T14:27:36+00:00 automated review requested changes: The phase-resume and fsync fixes work, but activation is still not crash-safe across a lost backend response. cost=$0.22
- 2026-09-11T14:27:47+00:00 dispatched revise run 20260911T142746Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2932 tokens)
- 2026-09-11T14:32:55+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T14:34:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/492: Made rollout mutations crash-safe by durably recording stable action IDs before stage, activation, rollback, and fencing calls, with replay-safe backend semantics. Verified 26 rollout tests, 42 adjacent upgrade/managed-worker tests, Ruff, Python compilation, whitespace checks, and a clean committed worktree. cost=$0.46
- 2026-09-11T14:37:07+00:00 automated review requested changes: Mutation replay remains incomplete: an interrupted rollback or fence cannot be resumed despite its durable action ID. Exact-head CI is also pending. cost=$0.22
- 2026-09-11T14:42:45+00:00 triage: changes requested by hand: Delegated operator reviewed the actual143437 findings and the2-round top-difficulty stop. Continue one bounded correctio
- 2026-09-11T14:43:54+00:00 dispatched revise run 20260911T144353Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2944 tokens)
- 2026-09-11T14:47:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T14:49:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/492: Made interrupted rollback and fence operations resumable from durable pending-recovery records without repeating destructive mutations or advancing later workers. Verified commit 2c647c3e with 70 focused rollout/upgrade/managed-worker tests, Ruff lint, Python compilation, whitespace checks, conflict-marker inspection, and a clean committed worktree. cost=$0.49
- 2026-09-11T14:50:31+00:00 automated review requested changes: Recovery replay is fixed, but activation verification can accept a runtime that was never staged or verified. cost=$0.26
- 2026-09-11T14:50:41+00:00 dispatched revise run 20260911T145040Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2957 tokens)
- 2026-09-11T14:54:28+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T14:55:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/492: Bound post-switch verification to the durable staged runtime and executable attestation, preventing an unstaged runtime from reaching healthy/complete. Verified commit 6d8dd1e6 with 72 rollout, upgrade, and managed-worker tests, clean Ruff lint, Python compilation, whitespace checks, and a clean worktree. cost=$0.35
- 2026-09-11T14:58:36+00:00 automated review: approve — The rollout implementation satisfies the frozen contract, including crash-safe mutation replay and exact binding of activation evidence to the staged runtime. Exact-head CI remains pending and is independently enforced before merge. cost=$0.26
- 2026-09-11T15:06:33+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/492
