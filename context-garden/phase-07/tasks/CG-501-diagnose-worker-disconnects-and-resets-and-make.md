---
id: CG-501
title: Diagnose worker disconnects and resets and make recovery resilient
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/remote_worker.py
- src/garden/managed_worker.py
- src/garden/runner/remote.py
- src/garden/runs.py
- docs/worker-protocol.md
branch: garden/cg-501-diagnose-worker-disconnects-and-resets-and-make
pr: https://github.com/joshmarcus/context-garden/pull/414
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T18:50:35+00:00'
created: '2026-09-10T02:35:56+00:00'
updated: '2026-09-10T19:14:26+00:00'
---

## Goal

Make worker disconnects, connection resets and daemon restarts diagnosable, explain their cause to the operator, and recover transient failures without losing work or duplicating execution.

## Context

Owner request: better observability around worker disconnects/resets, better resilience, and knowledge of the cause. Diagnose the observed failures as part of this task; instrumentation alone is not the deliverable.

On September 10 the renewed workers exhibited repeated idle POST /api/runs/claim HTTP502 Bad Gateway errors followed by daemon exits and service restarts. A bounded audit recorded 38 restarts across six hosts; those samples were idle and do not prove that all other incidents were idle. No 401/403 was observed. An earlier timeout classifier accidentally matched source text timeout=60 rather than an actual timeout. Proxy/tailnet/WSL origin is a hypothesis, not an established cause. The separate fresh-WSL-command launch hangs are not proven to be the same failure.

CG491 / PR394 contains the merged idle-claim retry/idempotency fix; RC16 deployment does not contain it. Read current source and runtime facts before claiming this is still an unfixed source defect. Reuse its recovery rather than duplicating it. Coordinate with CG499 worker inventory/Now/API, CG494 scheduler health and CG423 lifecycle ownership. This task owns detailed incident evidence, cross-component cause attribution and remaining resilience gaps.

## Acceptance criteria

- [ ] Investigate the observed idle-claim 502/reset/restart incident with bounded, sanitized controller, worker, transport and supervisor evidence. Produce a linked incident report stating the failure chain, observed trigger, confirmed root cause(s), impact and concrete corrective actions. Separate confirmed facts from hypotheses; if upstream evidence cannot establish a cause, explicitly report unknown with the precise missing evidence and an implemented capture path for the next recurrence, never fabricate a cause.
- [ ] Persist structured lifecycle and transport events with UTC timestamps, stable worker/process-generation identity, request correlation, operation, endpoint class, HTTP status or actual exception, exit reason and restart count, reconnect attempts/backoff and recovery outcome. Distinguish planned shutdown/expiry, process crash, network or proxy failure, authentication failure, controller unavailability and unknown causes. Keep worker contact independent of task leases and preserve useful bounded history across restarts.
- [ ] Correlate both ends of a failed operation and report whether work was idle, queued, executing, returning a result or recovering. Distinguish network loss from daemon reset and host termination; show last healthy contact, duration, affected task/run and whether execution or result delivery was interrupted. Integrate incident summaries/details with CG499 and a safe diagnostic API/export instead of building a second worker dashboard. Notify on meaningful failure or recovery, deduplicating repeated identical events.
- [ ] Recover transient claim, heartbeat and result-return failures with bounded timeouts and classified retries/backoff with jitter, using existing protocol idempotency and fencing. Avoid crash/restart storms and silent permanent retry loops; surface persistent or authentication failures with a concrete operator action. Preserve active source/results and durable pending delivery across process restart; never replay accepted execution or let an expired generation overwrite current results. Preserve configured resource, lease and absolute host-deadline limits.
- [ ] Use a disposable controller/worker journey to inject 502/503, actual connection reset/refusal/timeout, controller restart, worker process restart during execution and result delivery, and permanent auth failure. Demonstrate correlated diagnostic evidence, bounded recovery, truthful cause/unknown classification, no duplicate execution and successful eventual result delivery where recovery is possible. Include idle workers and expected deadline termination. Do not inject faults into the live fleet or count exception text in source code as a real incident.
- [ ] Keep diagnostics bounded, rate-limited and secret-safe: redact bearer/enrollment/model/cloud credentials, sensitive request bodies and raw private transcripts; avoid synchronous cloud/SSH fan-out on UI requests. Use portable APIs and configurable paths on Linux, macOS and Windows through WSL, isolating optional systemd/platform collectors behind capability checks. Report which platforms and actual runtime versions were tested.

## Scope boundaries

Adding this task does not authorize a live fleet restart, replacement, new cloud spending, deadline extension or immutable-runtime hotpatch. Route any required deployment through existing validated release procedures. Preserve original failure evidence and report source fix versus installed runtime separately.

## Log

- 2026-09-10T03:08:55+00:00 approved (delegated operator reviewed owner-requested draft during Inbox sweep)
- 2026-09-10T04:00:15+00:00 dispatched work run 20260910T040012Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17920 tokens)
- 2026-09-10T04:18:21+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:19:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/414 (base main): Diagnosed the observed restart chain, added correlated bounded diagnostics and finite recovery behavior, and made result delivery durable across daemon restarts. Verified committed head ea6076e115c02ead701af6fe8bd58d99c47754c3 with 98 focused tests and full requested Ruff lint. cost=$2.41
- 2026-09-10T04:23:10+00:00 automated review requested changes: The core recovery and diagnostics paths remain incomplete: pending-result replay can cause restart storms, controller diagnostics omit failed requests, and event storage is not byte-bounded. cost=$0.46
- 2026-09-10T04:40:21+00:00 dispatched revise run 20260910T044018Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19608 tokens)
- 2026-09-10T04:53:19+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:54:43+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Hardened pending-result recovery against restart loops, enforced byte and record bounds with sanitized correlation fields, and captured both successful and rejected controller operations with deduplicated failure/recovery notices. Verified the final source with 102 focused tests and current-head Ruff lint; the worktree is clean. cost=$2.75
- 2026-09-10T04:58:32+00:00 automated review requested changes: Focused tests and lint pass, but two required recovery/diagnostic behaviors remain incomplete: daemon restart during execution cannot resume result collection, and controller events lose worker identity for heartbeat/result requests. cost=$0.53
- 2026-09-10T04:58:56+00:00 dispatched revise run 20260910T045851Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20008 tokens)
- 2026-09-10T05:08:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T05:09:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Added durable active-execution handoff so a replacement managed-worker daemon can resume lease renewal, collect a surviving supervisor, and deliver its result without replaying execution. Controller diagnostics now preserve validated worker identity across heartbeat/result operations; 104 focused tests and full requested Ruff lint passed at committed head d8c63cf3e39928bb3b77a8e8f1f577b525579a2a. cost=$2.11
- 2026-09-10T05:11:09+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/api.py); a rebase agent will resolve it
- 2026-09-10T05:16:51+00:00 dispatched rebase run 20260910T051649Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2638 tokens)
- 2026-09-10T05:20:13+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.01
- 2026-09-10T05:41:46+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T05:58:48+00:00 dispatched revise run 20260910T055845Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19910 tokens)
- 2026-09-10T06:06:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T06:08:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Recovered supervisor publication failures now transfer completed work safely to either quarantine or durable pending delivery without daemon restart loops or execution replay. Merged current main while preserving exact-source validation receipts, and verified committed head 0de0db295a4d70c8653e1e9236409037c977e7e9 with 112 focused tests and repository-wide Ruff. cost=$1.26
- 2026-09-10T06:11:50+00:00 automated review requested changes: Managed model executions survive daemon replacement, but remote check executions do not persist an active-claim handoff and therefore cannot be recovered after a worker daemon restart. cost=$0.59
- 2026-09-10T06:26:42+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T06:26:56+00:00 dispatched revise run 20260910T062652Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20480 tokens)
- 2026-09-10T06:33:45+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T06:34:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Remote check supervisors now persist the same durable active-claim handoff as harness executions, allowing a replacement daemon to renew the lease, collect checks.json, and deliver the fenced result without replay. Verified current head d930c6d274061ff06790a293b37e1de7b6c51185 with focused restart/integration and architecture tests plus repository-wide Ruff; full CI remains the controller-owned merge gate for this local WSL run. cost=$1.19
- 2026-09-10T10:50:03+00:00 automated review requested changes: Diagnostics and restart handoff are substantially covered, but recovered executions are not safely terminated when their lease or absolute execution deadline expires. cost=$0.59
- 2026-09-10T10:57:58+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T11:42:59+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T11:47:06+00:00 dispatched revise run 20260910T114702Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20878 tokens)
- 2026-09-10T11:55:20+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:56:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Recovered supervisors are now terminated and quarantined when lease authority becomes terminal, preserving fixed execution deadlines without replay or restart loops. Verified with 114 focused remote/managed-worker tests, a real-process deadline regression, and repository-wide Ruff on Linux WSL2 with Python 3.14.4. cost=$1.32
- 2026-09-10T11:59:46+00:00 automated review requested changes: Recovery and diagnostics are substantially covered, but stale active-claim state can mistake a reused PID for the original supervisor and terminate an unrelated process. cost=$0.54
- 2026-09-10T13:25:03+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T13:27:13+00:00 dispatched revise run 20260910T132710Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20948 tokens)
- 2026-09-10T13:35:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:36:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Persisted and verified supervisor process-birth identity during daemon recovery, preventing reused PIDs from receiving signals or causing execution replay. Committed head 9782e749b278ca040fd259140506ce2ff823e13c passes 95 focused remote-worker tests and repository-wide Ruff. cost=$1.25
- 2026-09-10T13:36:54+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/remote_worker.py); a rebase agent will resolve it
- 2026-09-10T13:40:30+00:00 dispatched rebase run 20260910T134029Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3992 tokens)
- 2026-09-10T13:48:24+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.06
- 2026-09-10T14:02:18+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:12:41+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T14:15:50+00:00 dispatched revise run 20260910T141547Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22149 tokens)
- 2026-09-10T14:22:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:23:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Recovered executions now enforce their persisted absolute deadline locally even while the controller is unreachable, terminating only an identity-verified supervisor and quarantining the claim without replay. Fixed all five reported Ruff errors and verified committed head 0311b4e21374a3a84730bab835fadda9aee2a070 with 96 focused remote-worker tests and repository-wide Ruff. cost=$0.78
- 2026-09-10T14:27:34+00:00 automated review requested changes: Recovery and diagnostics are well covered, but the macOS supervisor identity fallback can still mistake a rapidly reused PID for the original process and signal unrelated work. cost=$0.57
- 2026-09-10T14:31:07+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:32:44+00:00 dispatched revise run 20260910T143240Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21852 tokens)
- 2026-09-10T14:36:14+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:37:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Replaced the unsafe second-resolution macOS ps fallback with fail-closed recovery: unfinished handoffs without a strong process identity are quarantined without signalling or replay, while Linux retains boot-ID/start-tick fencing and deadline enforcement. Committed head 887a4c74da96510a088db329ea1b0edf4ff70bfa passed 98 focused remote-worker tests and repository-wide Ruff on Linux WSL2 with Python 3.14.4; native macOS was not tested. cost=$0.61
- 2026-09-10T14:37:45+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/api.py); a rebase agent will resolve it
- 2026-09-10T14:41:46+00:00 dispatched rebase run 20260910T144145Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~4731 tokens)
- 2026-09-10T14:44:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Rebased all 17 commits and preserved locked run persistence, conflict handling, diagnostic imports, and heartbeat event logging. cost=$0.01
- 2026-09-10T14:45:21+00:00 CI failure
- 2026-09-10T15:48:16+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T16:29:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T16:30:46+00:00 dispatched revise run 20260910T163043Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22405 tokens)
- 2026-09-10T16:35:19+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:36:36+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Rebased onto accepted main, retaining its import/locking repair, and classified GET /api/worker-diagnostics as an operator-read route. Verified committed head be19210f0eb7190ab01cd183e9227b8cdc10746a with current-head startup/export tests, 119 focused recovery tests, and repository-wide Ruff. cost=$0.61
- 2026-09-10T16:42:47+00:00 automated review requested changes: Managed-worker recovery and diagnostics are well covered, and focused suites pass, but the documented standalone `garden worker` path still bypasses the new recovery lifecycle. cost=$0.82
- 2026-09-10T16:51:21+00:00 triage: changes requested by hand: Preserve the now-correct diagnostic route and the managed-daemon recovery behavior; both exact-head CI runs34503033965/3
- 2026-09-10T16:53:13+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T17:04:13+00:00 dispatched revise run 20260910T170409Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22890 tokens)
- 2026-09-10T17:11:30+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:12:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Closed the standalone worker recovery gap by sharing durable lifecycle initialization and claim retry behavior with the managed daemon, then recovering active claims and pending results before requesting new work. Verified committed head b67098f586f4101ba56ea6aca70610d40f2c826f with 120 focused tests and repository-wide Ruff lint. cost=$1.44
- 2026-09-10T17:16:23+00:00 automated review requested changes: Diagnostics and recovery coverage are substantial, but execution launch is not crash-atomic and can still permit duplicate work. cost=$0.75
- 2026-09-10T17:31:41+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T17:31:41+00:00 delegated operator routed next correction to existing renewed remote fleet after owner reported idle workers; existing scope, review/CI gates and fleet limits preserved
- 2026-09-10T17:35:17+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T17:38:18+00:00 dispatched revise run 20260910T173818Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22914 tokens)
- 2026-09-10T17:50:39+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:52:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Made remote harness and check launch crash-atomic with a parent/supervisor gate released only after the PID/birth-fenced active claim is fsynced. Verified committed head f002c1c3 with 106 focused remote-worker tests and repository-wide Ruff lint on Linux with Python 3.12. cost=$2.31
- 2026-09-10T17:52:27+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/remote_worker.py); a rebase agent will resolve it
- 2026-09-10T17:52:33+00:00 dispatched rebase run 20260910T175233Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~5872 tokens)
- 2026-09-10T17:57:07+00:00 automated review: request_changes — The durable launch gate prevents duplicate execution, but a daemon crash can still start a harness with an empty or truncated brief. cost=$0.80
- 2026-09-10T18:02:51+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.06
- 2026-09-10T18:34:37+00:00 pre-PR checks failed (lint) (rebase onto `main` did not apply cleanly); revise run will fix before the PR is updated
- 2026-09-10T18:49:00+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T18:50:35+00:00 dispatched revise run 20260910T185034Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23940 tokens)
- 2026-09-10T18:58:03+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:59:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/414: Rebased the existing recovery work onto accepted main repair dc84676e and made remote harness input crash-atomic by durably staging the complete brief before launch-gate release. Committed head 61e8f291 passed 107 remote-worker tests, 34 managed-worker/execution-sandbox tests, five current-head launch/input regressions, and repository-wide Ruff. cost=$1.15
- 2026-09-10T19:05:32+00:00 automated review: approve — The current revision closes the launch/input crash window and provides bounded correlated diagnostics, durable fenced recovery, and a truthful incident analysis. No blocking defects found. cost=$1.15
- 2026-09-10T19:08:22+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T19:14:26+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/414
