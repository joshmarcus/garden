---
id: CG-404
title: Add command-backed host acquisition readiness and warm reuse to the shared lifecycle
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-399
- CG-345
priority: 1
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-404-add-command-backed-host-acquisition-readiness-an
pr: https://github.com/joshmarcus/context-garden/pull/316
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T01:54:50+00:00'
created: '2026-09-07T19:56:17+00:00'
updated: '2026-09-09T04:11:19+00:00'
---

## Goal

Extend the shared provider/environment contracts with a vendor-neutral command-backed host adapter; do not create a second EC2-specific lifecycle.

## Acceptance criteria

- [ ] Acquire, read-only readiness and release are bounded asynchronous operations with durable state, maximum hosts and TTL; repeated ticks/restarts do not duplicate acquisition.
- [ ] Prefer compatible warmed hosts only after the previous process is terminal and checkout reconciliation succeeds. Verify configured workspace, revision, provisioning completion, harness login and a bounded non-mutating smoke probe.
- [ ] Readiness/provisioning failure is an environment stop without consuming a task attempt; support recovery, cancellation, orphan inspection and explicit retirement.
- [ ] Verify wrapper transport passes argv, stdin, exit codes and output faithfully. All dispatch originates at the controller; do not require host-to-host SSH. Preserve logical aliases.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G2 delta over phase-05 lifecycle. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T13:52:47+00:00 dispatched work run 20260908T135247Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~9296 tokens)
- 2026-09-08T14:49:27+00:00 opened https://github.com/joshmarcus/context-garden/pull/316 (base main): Added a vendor-neutral, controller-side command host adapter with bounded byte-faithful transport, durable acquisition state, readiness gating, warm reuse, TTL retirement, cancellation, orphan inspection, and explicit release/retirement. Documented the wrapper protocol and shared lifecycle integration. cost=$3.00
- 2026-09-08T14:58:15+00:00 automated review requested changes: Focused checks pass, but warm reuse, absolute TTL enforcement, and readiness failure handling do not meet the lifecycle criteria. cost=$0.26
- 2026-09-08T14:58:26+00:00 dispatched revise run 20260908T145826Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~10331 tokens)
- 2026-09-08T15:43:44+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/316: Warm host leases now preserve their original acquisition timestamp across releases and reuse, stopped hosts restart automatically only after the previous run is terminal, and readiness wrapper failures become durable recoverable environment stops. Added regressions for release-to-reuse, immutable TTL enforcement, terminality gating, and provider/invalid-JSON recovery. cost=$2.67
- 2026-09-08T15:54:34+00:00 review validation scope expansion: Duplicate pre-dispatch acquisition probe — Inspection showed an unreleased lease with an empty run_id remains eligible, directly risking duplicate dispatch.
- 2026-09-08T15:54:34+00:00 review validation scope expansion: Malformed acquisition response probe — The command adapter accesses value.get before validating the JSON value is an object, exposing an untested provisioning failure path.
- 2026-09-08T15:54:36+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: acquire, read-only r; run `garden triage CG-404 --changes "<feedback>" to unblock`
- 2026-09-08T16:05:24+00:00 triage: changes requested by hand: The repeated stop includes two concrete bugs. Preserve the implementation; make unbound acquired leases atomic/exclusive
- 2026-09-08T16:21:36+00:00 dispatched revise run 20260908T162136Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~10692 tokens)
- 2026-09-08T16:50:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/316: Made command-backed host acquisition exclusive across controller instances with durable, expiring pre-attach reservations, and converted wrong-shaped acquisition responses into recoverable environment stops. Added targeted regressions for duplicate acquisition, cancellation and stale recovery, plus list/null/scalar payload recovery. cost=$2.16
- 2026-09-08T16:54:17+00:00 review validation scope expansion: Duplicate pre-dispatch acquisition probe — The revised exclusivity test is sequential, while the claimed cross-controller guarantee requires overlapping acquisition; a controlled concurrent probe demonstrated two acquire calls.
- 2026-09-08T16:54:19+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: acquire, read-only r; run `garden triage CG-404 --changes "<feedback>" to unblock`
- 2026-09-08T17:13:19+00:00 re-enabled by hand; revise run will follow
- 2026-09-08T17:18:21+00:00 dispatched revise run 20260908T171818Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~10487 tokens)
- 2026-09-08T17:55:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/316: Serialized command-backed host acquisition across overlapping controller instances and added a controlled concurrent regression proving only one acquire call occurs. The focused host lifecycle suite and repository-wide lint pass on commit 6420cb9d8bb16f314820715c3058cc7b50601f87. cost=$1.91
- 2026-09-08T18:31:27+00:00 automated review produced no verdict (idle 38 min (no output or file change))
- 2026-09-08T19:23:55+00:00 Operator verified deployment-era interrupted check/review, preserved failed record, queued exactly one current-head replay/review through current controller runtime; no implementation retry.
- 2026-09-08T21:00:23+00:00 review validation scope expansion: Malformed inspect response probe — Inspection of the command protocol revealed that discover iterates the response without validating it is a list, which directly affects the readiness/provisioning failure criterion.
- 2026-09-08T21:00:25+00:00 automated review requested changes: The overlapping-controller acquisition race is fixed and the focused 29-test suite passes. However, a wrong-shaped inspect response bypasses environment-stop handling, leaving a provisioning failure path unrecoverable under the lifecycle contract. cost=$0.45
- 2026-09-09T01:53:02+00:00 Operator restored queued author to remote after current-source check routing inspection: no generated capture pages or controller-owned spec paths. Full substantive feedback preserved; current owner proportional-validation policy appended. No active run or cap changed.
- 2026-09-09T01:54:50+00:00 dispatched revise run 20260909T015450Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~13559 tokens)
- 2026-09-09T02:16:41+00:00 review pre-flight advisory: omitted optional items: No conflict markers remain
- 2026-09-09T02:29:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/316: Validated command-backed inspect responses before decoding and added recovery coverage for null, object, scalar, and malformed-row responses. The focused lifecycle suite and repository lint pass at committed HEAD. cost=$0.61
- 2026-09-09T02:53:02+00:00 automatic review recovery 1/2 queued for the current head: idle 20 min (no output or file change)
- 2026-09-09T03:22:13+00:00 automatic review recovery 2/2 queued for the current head: idle 20 min (no output or file change)
- 2026-09-09T03:43:39+00:00 automated review: approve — The command-backed lifecycle meets the frozen criteria, including the corrected malformed-inspection recovery path and serialized cross-controller acquisition. cost=$0.42
- 2026-09-09T03:49:01+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T04:01:36+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T04:04:03+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T04:11:06+00:00 automated review:  —
- 2026-09-09T04:11:19+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/316
