---
id: CG-457
title: Prevent remote queue-age timeouts from duplicating live work and losing run fences
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/runs.py
- src/garden/web/pages/api.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/fence.py
- tests/test_remote_worker.py
branch: garden/cg-457-prevent-remote-queue-age-timeouts-from-duplicati
pr: https://github.com/joshmarcus/context-garden/pull/352
runner: remote
discovered_from: CG-453
attempts: 1
last_dispatched_at: '2026-09-08T23:02:47+00:00'
created: '2026-09-08T23:01:16+00:00'
updated: '2026-09-09T01:11:32+00:00'
---

During the six-worker restoration, CG453 was queued at20:41UTC and claimed21:41UTC. The installed controller charged its unclaimed queue hour to worker elapsed timeout, timed out a live productive original at22:16UTC, and dispatched a duplicate that a second host claimed. The old host kept executing and returning heartbeats despite its terminal controller status. Operator receipts preserve both exact source bundles and output under /home/joshua/work/operator-test-tmp/cg453-duplicate-recovery-20260908; original and duplicate run IDs are20260908T204104Z-work and20260908T221655Z-work. Restoring the original actual execution age let its honest blocked result arrive, but finalization then failed because the duplicate had displaced the per-task fence manifest reference. This task owns the lifecycle repair, not the test-speed implementation of CG453.

## Acceptance criteria

- [ ] Unclaimed queue duration does not consume a remote model's execution timeout. Define and preserve queued, claimed, execution, lease, and final timestamps across delayed claim, reclaim, restart, and legacy records; preserve original historical timestamps rather than rewriting them to conceal accounting.
- [ ] A timeout or terminal transition accounts for or revokes the old generation before another generation can execute. Terminal or stale-generation heartbeats/results cannot extend leases or overwrite accepted evidence, and fresh active output/lease is handled according to a documented execution deadline policy.
- [ ] Every in-flight or interrupted-finalization run retains its own trusted fence reference outside worker-writable data. A later run or retry cannot overwrite, delete, or substitute the earlier run's authority. Preserve fail-closed behavior for genuinely missing or contradictory provenance.
- [ ] Regressions exercise long unclaimed wait followed by normal execution, actual running timeout, late heartbeat/result, duplicate prevention, restart/reap, and two generations with different manifests. Demonstrate complete source/results/usage preservation and no double accounting with recorded scheduler state transitions; do not accept a generic unrelated UI replay as proof.

## Log

- 2026-09-08T23:01:16+00:00 approved (owner-delegated recovery of actual duplicate execution incident)
- 2026-09-08T23:02:47+00:00 dispatched work run 20260908T230247Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15014 tokens)
- 2026-09-08T23:47:27+00:00 opened https://github.com/joshmarcus/context-garden/pull/352 (base main): Remote execution time now begins at first claim rather than queue entry, terminal generations reject late heartbeats/results, and every run retains its own trusted fence authority. Historical timestamps, claim generations, results, usage, and fail-closed provenance behavior are preserved. cost=$4.52
- 2026-09-09T00:32:58+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/352
- 2026-09-09T01:11:32+00:00 automated review could not start: CG-457 is done: #352 was merged at 00:32:58
