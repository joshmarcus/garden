---
id: CG-491
title: Recover idle worker claims after transient or lost claim responses
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/managed_worker.py
- src/garden/web/app.py
- src/garden/runs.py
- tests/test_managed_worker.py
- tests/test_web.py
branch: garden/cg-491-recover-idle-worker-claims-after-transient-or-lo
pr: https://github.com/joshmarcus/context-garden/pull/394
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T17:41:37+00:00'
created: '2026-09-09T17:19:34+00:00'
updated: '2026-09-10T01:12:52+00:00'
---

## Goal

Make managed workers tolerate transient failures while requesting idle work, including the ambiguous case where the controller commits a claim but the successful response is lost. A worker must recover without exiting, stranding the new claim until lease expiry, or executing a duplicate generation.

This is the idle `POST /api/runs/claim` path. CG-428 owns active-run heartbeat transport retry. Preserve its scope and behavior. Implement this as a normal versioned source change; do not hotpatch RC13 or alter the active rollout.

## Reproduction

During the RC13 rollout a managed worker received HTTP 502 from `POST /api/runs/claim` before any child process started. The unhandled `WorkerClient.post` error terminated the worker. A response can also be lost after the controller has already allocated the run, so blindly repeating the current claim request can create a second allocation while the first remains leased.

## Acceptance criteria

- [ ] Retry transient idle claim transport failures with a bounded delay/backoff and keep the managed worker alive. Permanent authentication, validation, and other non-transient responses remain visible failures.
- [ ] Give retries of one logical claim request a stable idempotency identity. If the controller committed the first request but its response was lost, replay returns that same allocation instead of claiming another task or generation.
- [ ] Fence stale, expired, mismatched-host, and mismatched-generation claim identities. Recovery must not authorize duplicate execution, revive an obsolete lease, or let one worker consume another worker's claim.
- [ ] Add a deterministic end-to-end regression that commits a claim, drops the first successful response, retries it, and proves exactly one run generation is allocated and executed. Also cover a transient failure before allocation and the relevant permanent-error behavior.
- [ ] Preserve active-run heartbeat semantics owned by CG-428, existing capacity and harness filtering, lease recovery, terminal collection, and current worker resource limits. Document the request identity and replay lifetime narrowly enough for operators to diagnose it.

## Log

- 2026-09-09T17:19:34+00:00 approved (operator follow-up from reproduced RC13 idle claim HTTP 502; versioned source fix only, distinct from CG-428 active heartbeat retries)
- 2026-09-09T17:20:25+00:00 dispatched work run 20260909T172025Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18955 tokens)
- 2026-09-09T17:32:11+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T17:34:19+00:00 opened https://github.com/joshmarcus/context-garden/pull/394 (base main): Managed workers now survive transient idle-claim failures using capped exponential backoff and stable request identities. The controller durably replays an ambiguously lost successful claim only while its exact host-bound lease generation remains recoverable; focused worker/web tests and lint pass at commit 894a2d02. cost=$1.95
- 2026-09-09T17:36:14+00:00 CI failure
- 2026-09-09T17:41:21+00:00 automated review: approve — Idle claim retries, durable idempotent replay, and lease-generation fencing satisfy the requested recovery behavior without altering heartbeat handling. cost=$0.32
- 2026-09-09T17:41:37+00:00 dispatched revise run 20260909T174137Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19571 tokens)
- 2026-09-09T17:54:34+00:00 worker found no change to make: The failing checks are duplicate CI infrastructure failures, not failures caused by the branch diff, so no source amendment is justified.; reconciling with checks and a fresh review
- 2026-09-09T17:56:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/394: The existing implementation is correct and fully committed. Both reported CI checks failed in GitHub's Playwright dependency-install step before lint or pytest ran; local current-head validation passed 2,077 ordinary tests and Ruff. cost=$1.13
- 2026-09-09T18:00:35+00:00 automated review: approve — Idle claim retries and durable, generation-fenced replay satisfy the requested recovery behavior without changing heartbeat handling. cost=$0.28
- 2026-09-10T00:54:20+00:00 renewed-fleet diagnostic: all six RC16 daemons remained active but accumulated 38 idle-claim HTTP 502 exits/restarts; no authentication failure or sampled active-child interruption. This is CG-491's exact scope, and its fix is absent from RC16. Preserve PR394's current head and recover its infrastructure-failed exact-head CI through the normal flow. Evidence: `context-garden/docs/incidents/idle-claim-502-restarts-20260910.md` and `/home/joshua/work/operator-test-tmp/aws-renew-20260909/cg491-idle-claim-restart-addendum.json`.
- 2026-09-10T01:00:29+00:00 exact CI diagnosis: both failed runs stopped before lint/pytest because the Google Chrome apt index returned a hash-sum mismatch during Playwright dependency installation. The current head remained `894a2d027fc2c5792b7724b9c7e6c8d9e51eacd4`; both failed jobs were re-run without a source change.
- 2026-09-10T01:11:24+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T01:12:52+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/394
