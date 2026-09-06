---
id: CG-344
title: Keep fence bookkeeping memory bounded as run history grows
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 7
difficulty: hard
reading: []
branch: garden/cg-344-keep-fence-bookkeeping-memory-bounded-as-run-his
pr: https://github.com/joshmarcus/context-garden/pull/232
attempts: 1
last_dispatched_at: '2026-09-06T15:03:57+00:00'
created: '2026-09-06T15:03:02+00:00'
updated: '2026-09-06T17:02:27+00:00'
---

## Goal

Fence bookkeeping must preserve isolation guarantees without making scheduler and CLI memory grow in proportion to repeated copies of the entire run history.

## Evidence

2026-09-06 15:00Z after Josh rebooted from a host memory lockup: .garden/state.json is 102MiB; 91.1MiB consists of large repeated fence_guard_manifest strings, with several task values about 3.4 million characters each. The server loads and writes state, and CLI actions instantiate it too. Before reboot the garden cgroup had peaked at 6.5GiB; overlapping full pytest suites and RAM-backed temporary files are additional contributors. No OOM-killer event was found in the retained previous-boot kernel log, so do not claim the manifest alone caused the host lockup. CG-338 covers resource admission; this task fixes the specific bookkeeping amplification.

## Acceptance criteria

- [ ] Snapshot attribution and restoration retain the current fence guarantees while large immutable manifests are stored/referenced without duplicating all content into each state value; prove this with existing isolation tests plus representative history-growth tests.
- [ ] Completed-run metadata retention cannot inflate routine status/actions/ticks indefinitely; preserve auditability, recovery, accounting and concurrently active fences. Migration from existing large state is safe and does not edit live state concurrently with a tick.
- [ ] Report before/after serialized state size, peak memory of a representative status action and tick, and history-size scaling. The fix must not simply remove or disable fence protections.

## Log

- 2026-09-06T15:03:02+00:00 approved (cli)
- 2026-09-06T15:03:57+00:00 dispatched work run 20260906T150332Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~8259 tokens)
- 2026-09-06T15:21:54+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit a63946ec2545, not because of this branch; waiting for the base to go green, no revise round cost=$2.20
- 2026-09-06T16:17:29+00:00 base branch `main` recovered (moved to f1ddcdcced39); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-06T16:17:32+00:00 opened https://github.com/joshmarcus/context-garden/pull/232 (base main): Fence bookkeeping now scales with concurrently active runs instead of completed history. Legacy inline manifests are safely compacted, active fence restoration remains intact, and active-run discovery no longer materializes all historical run records.
- 2026-09-06T16:17:32+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-06T16:38:30+00:00 automated review requested changes: The bounded-bookkeeping direction and scaling tests are sound, but the new manifest lookup weakens the fence’s tamper guarantee and the branch includes a large unrelated snapshot update. cost=$0.56
- 2026-09-06T17:02:27+00:00 Owner fast-forward: directly repaired and self-reviewed f7b2646; 182 targeted tests and full GitHub CI passed; PR 232 verified merged at bda4911f5a9854212298294ef957813f5b1c016d.
