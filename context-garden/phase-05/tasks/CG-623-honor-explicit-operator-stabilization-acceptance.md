---
id: CG-623
title: Honor explicit operator stabilization acceptance without rewriting measured evidence
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-537
priority: 0
difficulty: hard
reading:
- src/garden/stabilization.py
- src/garden/scheduler/human.py
- tests/test_stabilization.py
branch: garden/cg-623-honor-explicit-operator-stabilization-acceptance
pr: https://github.com/joshmarcus/context-garden/pull/489
runner: local
discovered_from: 'operator: actual Phase05 closure refusal after CG537 acceptance'
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-11T11:31:46+00:00'
created: '2026-09-11T10:31:23+00:00'
updated: '2026-09-11T11:50:38+00:00'
---

## Goal

Make native phase closure honor an explicit, accountable operator acceptance of stabilization limitations while keeping measured PASS/FAIL/UNPROVEN evidence unchanged. The current gate only accepts a fully populated current-build mechanical report and has no way to represent an owner-authorized acceptance decision. Implement the smallest portable supported command/API and closure-gate integration; do not close the live phase or edit its evidence from the worker.

## Actual diagnosis and authority

On September11 the owner instructed: "Please review all human actions for me, approve tasks, etc". The delegated operator accepted the independently reviewed Phase05 target/coverage/latency/current-policy limitations through native question20260910T172433Z-work-q0 at10:11:15UTC. Final context PR5 https://github.com/joshmarcus/garden/pull/5 was independently approved at d0d81f0bd7bd8e0a758d0175ce10c561b9f93925 and merged at499807fd8d561fb80378c089d356f6a8e49beaa8. All24 original reports were preserved,101 actual RC21 ordinary ticks were observed, CG537 completed through supported external-PR merge/source verification. The subsequent native retro_decide(close_with_followups) refused before closure.

Installed RC21 e38b8404175e9b3a9ffcddb41251db3ac2d6f611 stabilization.gate unconditionally requires five PASS outcomes bound to running_build_sha, seven recovery exercises, interaction evidence and4hours/10tasks. This live garden has no stabilization-evidence.json sidecar. The refusal correctly reports absent data, but cannot honor the actual accepted policy and earlier owner instruction not to rerun an arbitrary/fixed stabilization window. Do not fabricate or reconstruct missing mechanical evidence. A first-class explicit acceptance is distinct from a claim those tests or targets passed. The new acceptance must require an operator action and carry source/authority/rationale/scope provenance. Generic task completion, a version bump, a worker's output or an arbitrary answered question must never create an acceptance automatically.

## Acceptance criteria

- [ ] Provide a supported explicit operator command/API to record an acceptance decision for one phase and identified build with nonempty authority, rationale and evidence/source references, accountable actor and timestamp. Record human_owner versus delegated_operator truthfully; automation/unknown actors cannot invent owner authority. No acceptance is created merely by dispatch, merging, answering an unrelated question or worker claims.
- [ ] The gate may recognize only a structurally valid acceptance matching its exact phase and identified build. Missing, malformed, stale, wrong-phase/build or unauthorized acceptance remains refused under the existing measured-evidence path. Do not remove the stabilization spec, bypass the gate with force, monkeypatch the runtime, directly set the phase closed or relabel incomplete outcomes PASS. Bind an explicit build supplied to the command consistently with gate evaluation, with safe defaults and truthful reporting.
- [ ] Preserve existing sidecar samples, outcomes, failures, interventions and historical reports byte-for-byte when acceptance is recorded or superseded; use a separate durable record or equivalent non-destructive storage. Expose the accepted-with-limitations disposition and its provenance distinctly from measured success in the existing report/CLI read path. Later acceptance changes retain prior decisions, and a changed build does not silently inherit acceptance.
- [ ] Cover the explicit command/API through the real native phase-close/retro-decision path using disposable fixtures: accepted limitations can permit closure after all ordinary open-task/retro-blocker gates pass; acceptance cannot skip unfinished work, wrong build/phase, malformed authority or existing worker/operator trust boundaries. Keep the default measured gate behavior unchanged. Focused portable tests, Ruff, exact-head CI and independent review remain required; report Linux/macOS/Windows-through-WSL coverage honestly.

## Scope and ownership

This is a new P0 Phase05 closing correction under the owner's delegated human-action review, distinct from completed CG341(mechanical recorder),375(actor accounting),369(fixture scope) and537(editorial closing account). Root owns any actual acceptance recording, final native closure and later stable release from accepted source. The worker must only implement and verify in its isolated native checkout. No new persona/security verifier, live canary, artificial task count, fixed soak, new fleet resource, deadline extension or bulk cleanup. Preserve CG506 storage/S3 deferral, frozen Phase08, cancelled533 blocked report, Herdr withdrawal, all current work and the same six-host80USDcap/September11 11:36:42UTCdeadline.
## Log
- 2026-09-11T10:31:24+00:00 approved (delegated operator: owner all-human-actions review; actual native closure refuses accepted policy)
- 2026-09-11T10:32:09+00:00 dispatched work run 20260911T103209Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2606 tokens)
- 2026-09-11T10:38:33+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T10:40:00+00:00 opened https://github.com/joshmarcus/context-garden/pull/489 (base main): Added explicit operator acceptance of stabilization limitations for an exact phase/build without altering measured evidence. Focused stabilization tests pass (22 passed), Ruff passes, and commit cf7f1ecb contains the complete change; exact-head CI and independent review remain merge-gate responsibilities. cost=$1.02
- 2026-09-11T10:41:30+00:00 automated review requested changes: Acceptance recording, gate behavior, evidence preservation, and native closure integration work as intended, but closing-review identity does not reliably change when an acceptance is superseded. cost=$0.28
- 2026-09-11T10:41:39+00:00 dispatched revise run 20260911T104139Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2856 tokens)
- 2026-09-11T10:44:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T10:45:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/489: Closing-review identity now uses a deterministic digest of the complete matching acceptance decision, ensuring same-second superseding decisions invalidate stale preparation. Committed as 577c17f2; 23 stabilization tests and 2 adjacent retro tests passed, and Ruff is clean. cost=$0.55
- 2026-09-11T10:46:59+00:00 automated review: approve — The implementation meets the source-owned requirements; exact-head CI remains pending and is independently merge-gated. cost=$0.20
- 2026-09-11T10:53:42+00:00 CI failure
- 2026-09-11T10:53:51+00:00 dispatched revise run 20260911T105351Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2874 tokens)
- 2026-09-11T11:14:57+00:00 worker asks: Can you provide the failed pytest node and traceback from GitHub Actions run 34590658657, or rerun that exact-head push CI so the actionable failure is visible? cost=$1.89
- 2026-09-11T11:31:46+00:00 dispatched resume run 20260911T113146Z-resume via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2676 tokens)
- 2026-09-11T11:35:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/489: Fixed the failing same-second stabilization acceptance test fixture without weakening production prerequisite or owner-approval gates. Committed as 81fb8f98; 23 stabilization tests, 2 adjacent retro tests, Ruff, diff checks, and conflict-marker inspection passed on Linux. cost=$0.52

- 2026-09-11T11:40:22.729682+00:00 delegated operator: route subsequent work/check/review admission through the existing local runner after authenticated AWS verification that all six deadline-limited workers terminated. Preserve the original remote review and its failure/recovery accounting; no extra fleet authority inferred.
- 2026-09-11T11:43:55+00:00 automatic review recovery 1/2 queued for the current head: Authenticated AWS verification shows the original worker terminated at the effective owner11:36:42UTC deadline without an authenticated review final. Continue the same exact-head review on existing local capacity; preserve original partial transcript and unknown cost.
- 2026-09-11T11:47:33+00:00 automated review: approve — Explicit stabilization acceptance is correctly recorded and honored without altering measured evidence or bypassing ordinary closure gates. cost=$0.22
- 2026-09-11T11:48:59+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T11:50:38+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/489
