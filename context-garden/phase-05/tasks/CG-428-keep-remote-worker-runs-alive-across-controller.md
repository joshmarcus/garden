---
id: CG-428
title: Keep remote worker runs alive across controller redeploys
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/remote_worker.py
- src/garden/runner/remote.py
- src/garden/managed_worker.py
- src/garden/runs.py
- tests/test_remote_worker.py
- tests/test_managed_worker.py
- docs/worker-protocol.md
branch: garden/cg-428-keep-remote-worker-runs-alive-across-controller
pr: https://github.com/joshmarcus/context-garden/pull/334
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T03:22:28+00:00'
created: '2026-09-08T12:43:50+00:00'
updated: '2026-09-09T09:42:43+00:00'
---

## Goal

A normal controller redeploy should preserve productive remote jobs and their transcripts/results. Operators should not have to wait for every remote model session to finish before restarting the controller.

## Context and provenance

Owner explicitly requested this ticket on 2026-09-08 while deploying v0.3.0rc4. Inspection of deployed v0.3.0rc3 found `_LeaseHeartbeat._run` permanently records its first request exception and `ensure_current` later fails the run; transcript and finish posts can also fail across a controller disconnect. Four active AWS jobs therefore require a drain before today's restart. Preserve the single-controller model and existing identity/provenance fences.

## Acceptance criteria

- [ ] Transient connection refusal, timeout and retryable server errors during an ordinary controller stop/start are retried within a documented bounded recovery/lease window; active model/check subprocess work is preserved when authority is still valid.
- [ ] Authentication rejection, explicit cancellation/revocation, confirmed lease replacement and exhausted recovery deadlines remain terminal. Never silently renew a stale worker's authority, extend the AWS host deadline, or allow competing owners to publish.
- [ ] Transcript chunks and pending finish/result uploads survive reconnects with ordering and idempotency: no lost completed output, duplicate result collection, duplicate PR/branch publication or duplicate work execution after controller restart.
- [ ] The controller reconciles resumed and genuinely expired leases consistently from durable state; the UI distinguishes reconnecting/redeploy recovery from failed or dead workers and explains the remaining bounded wait.
- [ ] Deterministic focused regressions cover heartbeat, stream upload, finish acknowledgement loss, lease expiry/reassignment and explicit rejection. A separately bounded disposable controller stop/start journey demonstrates a real active job completing exactly once. Any stress/load experiments stay opt-in and out of normal tests/CI.
- [ ] Document deployment compatibility and recovery limits, with exact-head CI and current-source evidence before rollout. The owner has requested filing this task; do not alter today's running worker protocol as part of ticket creation.

## Log

- 2026-09-08T12:43:50+00:00 Filed at owner request after redeploy drain exposed first-transient-heartbeat failure; draft for planned implementation.
- 2026-09-08T14:07:31+00:00 approved (web)
- 2026-09-08T15:42:33+00:00 dispatched work run 20260908T154233Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16810 tokens)
- 2026-09-08T16:23:54+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$4.97
- 2026-09-08T16:24:20+00:00 dispatched revise run 20260908T162420Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17057 tokens)
- 2026-09-08T16:54:17+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$3.04
- 2026-09-08T16:55:51+00:00 dispatched revise run 20260908T165550Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17138 tokens)
- 2026-09-08T17:26:42+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$2.14
- 2026-09-08T17:27:34+00:00 dispatched revise run 20260908T172731Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17218 tokens)
- 2026-09-08T17:51:25+00:00 pre-PR checks failed (ui, UI captures, PR description); no PR opened yet; revise run will fix cost=$1.79
- 2026-09-08T17:54:10+00:00 dispatched revise run 20260908T175410Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17323 tokens)
- 2026-09-08T18:31:21+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$1.89
- 2026-09-08T19:09:12+00:00 dispatched revise run 20260908T190911Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18657 tokens)
- 2026-09-08T19:20:37+00:00 opened https://github.com/joshmarcus/context-garden/pull/334 (base main): Remote worker recovery now preserves active work, ordered transcripts, and idempotent completion across bounded controller outages. The revision also makes remote UI checks execute from the candidate checkout, preventing controller-local PYTHONPATH failures during rolling deployments. cost=$1.52
- 2026-09-08T19:21:48+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/remote_worker.py); a rebase agent will resolve it
- 2026-09-08T19:21:58+00:00 dispatched rebase run 20260908T192158Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~5027 tokens)
- 2026-09-08T19:27:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/334: Rebased onto origin/main and resolved the remote_worker.py conflict while preserving both sides. cost=$0.02
- 2026-09-08T19:47:35+00:00 automated review requested changes: The implementation is broadly sound, but worker-side retry expires after recovery_seconds while controller authority lasts lease_seconds + recovery_seconds. With defaults, productive work stops after 300 seconds even though the documented durable lease remains valid for 420 seconds. cost=$0.57
- 2026-09-08T19:48:03+00:00 dispatched revise run 20260908T194803Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19795 tokens)
- 2026-09-08T20:16:48+00:00 revision failed: worker idle 20 min (no output or file change)
- 2026-09-08T21:34:35+00:00 Delegated Input sweep restored final predeadline source checkpoint f9d4a562011b and retained complete failed-run feedback; operator owns continuation.


## Preserved-work continuation after restored capacity

Capacity is restored. The preserved latest source f9d4a562011bb9ec8585bfcb43bd72f34a6aad6f is now published on the existing task branch. Continue it, not a fresh implementation. Before test execution, integrate current origin/main (currently93681f4e74bd63996960057219a86c3e83296ed2) containing merged CG446; retain all substantive task changes and full original review feedback. Ordinary validation remains120seconds/test and900seconds/suite. Focus first on the remaining task-specific outcomes, never rerun the old hanging full suite unchanged. This continuation follows the original host loss and does not count that loss as a source failure.
- 2026-09-08T21:56:39+00:00 re-enabled by hand; revise run will follow
- 2026-09-08T21:58:00+00:00 dispatched revise run 20260908T215800Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20353 tokens)
- 2026-09-08T22:36:56+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/334: Remote workers now retry through the controller's full lease-plus-recovery window, with deterministic boundary coverage and a real disposable controller stop/start journey proving exactly-once completion. The branch is integrated with current origin/main and includes durable interaction evidence plus the existing reconnecting-state captures. cost=$4.27
- 2026-09-08T22:44:33+00:00 automated review produced no verdict (failed) cost=$0.55
- 2026-09-08T22:57:42+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/remote_worker.py); a rebase agent will resolve it
- 2026-09-08T22:57:54+00:00 dispatched rebase run 20260908T225754Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2313 tokens)
- 2026-09-08T23:21:13+00:00 check did not run (20260908T230045Z-check-2): idle 20 min (no output or file change); will retry
- 2026-09-08T23:47:15+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit 046cb5b709d6, not because of this branch; waiting for the base to go green, no revise round cost=$0.03
- 2026-09-08T23:50:59+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit 6fb64db88743, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-09T00:16:01+00:00 triage: changes requested by hand: Operator investigation: the current base_broken stop is not proof that main fails. The actual base-probe234907 has contr
- 2026-09-09T00:16:59+00:00 dispatched revise run 20260909T001659Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22048 tokens)
- 2026-09-09T00:22:36+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/334: Removed the unused Callable import and ctx assignment while preserving the completed remote recovery implementation. Exact-head focused lifecycle regressions and repository lint pass on d3a8cc57a6ab800d392e1c1d527cfbc201b169de. cost=$0.61
- 2026-09-09T00:29:04+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-09T00:29:23+00:00 dispatched rebase run 20260909T002923Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2698 tokens)
- 2026-09-09T00:35:52+00:00 pre-PR checks failed (UI captures); revise run will fix before the PR is updated cost=$0.02
- 2026-09-09T00:36:25+00:00 dispatched revise run 20260909T003625Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20206 tokens)
- 2026-09-09T00:52:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/334: Integrated current main and completed the remote-recovery revision. Generated UI checks remain host-portable, recovery tests match durable lease semantics, four reconnecting-state PNGs were refreshed, and the disposable restart journey completed exactly once. cost=$1.08
- 2026-09-09T01:03:59+00:00 automated review requested changes: Focused lifecycle tests and lint pass, but terminal lease loss leaves old subprocesses executing and exact-head CI has two regressions in generated UI-check provenance. cost=$0.80
- 2026-09-09T01:04:19+00:00 dispatched revise run 20260909T010419Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23149 tokens)
- 2026-09-09T01:16:22+00:00 revision failed: remote worker finished without pushing commits
- 2026-09-09T02:39:46+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/334 (pr_number 334 -> 334)
- 2026-09-09T02:42:22+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/checkruns.py, tests/test_walkthrough.py); a rebase agent will resolve it
- 2026-09-09T02:53:21+00:00 dispatched rebase run 20260909T025321Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3232 tokens)
- 2026-09-09T03:22:12+00:00 rebase conflict run 20260909T025321Z-rebase did not finish: worker idle 21 min (no output or file change); will retry
- 2026-09-09T03:22:12+00:00 rebase conflict run 20260909T025321Z-rebase did not finish: worker idle 21 min (no output or file change); will retry
- 2026-09-09T03:22:28+00:00 dispatched rebase run 20260909T032228Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3350 tokens)
- 2026-09-09T03:36:50+00:00 automated review: approve — Remote work survives bounded controller outages while stale, revoked, expired, and replaced generations remain fenced. Transcript and finish replay are durable and idempotent, and reconnecting state is surfaced clearly. cost=$0.59
- 2026-09-09T04:00:58+00:00 check did not run (20260909T034055Z-check): idle 20 min (no output or file change); will retry
- 2026-09-09T04:12:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/334: Rebased onto origin/main and resolved all conflicts while preserving main's current reviewer-chosen UI evidence behavior. cost=$0.02
- 2026-09-09T04:13:59+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T04:33:29+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T04:43:25+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T05:01:09+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T05:02:12+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T05:09:51+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/334
- 2026-09-09T09:42:43+00:00 automated review could not start: CG-428 is done: #334 was merged at 05:09:51
