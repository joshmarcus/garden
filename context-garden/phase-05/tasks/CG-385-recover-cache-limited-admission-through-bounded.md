---
id: CG-385
title: Recover cache-limited admission through bounded reclaim and a fresh headroom check
status: running
product: context-garden
phase: phase-05
depends_on:
- CG-383
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/resources.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/checkruns.py
- tests/scheduler/test_resources.py
- docs/validation/cg383/README.md
branch: garden/cg-385-recover-cache-limited-admission-through-bounded
attempts: 1
last_dispatched_at: '2026-09-07T15:17:03+00:00'
created: '2026-09-07T14:44:22+00:00'
updated: '2026-09-07T15:17:03+00:00'
---

## Goal

Unblock cache-limited worker admission using the CG383 calibration without weakening the memory ceiling, reserve, pressure safeguards or shared-slot cap.

## Evidence

CG383/PR293 merged d14afc5. Matched disk/tmpfs fixtures show disk inactive_file can be reclaimed while tmpfs shmem cannot be counted as available memory with swap disabled. The production controller previously stopped at roughly 3.7GiB usage dominated by file cache despite host headroom and zero memory pressure. Calibration is complete; the deployed admission policy is unchanged.

## Acceptance criteria

- [ ] Only consider a bounded best-effort reclaim when actual limiting controller/execution cgroup headroom is the remaining admission gate. Preserve host/temp/slot/pressure checks and hard/soft memory limits; never treat all file memory, shmem, or requested reclaim bytes as available memory.
- [ ] Perform potentially blocking kernel reclaim outside the scheduler/web transaction with bounded requests, timeout/cooldown, no duplicate helper and existing resource supervision. Record before/after actual headroom and errors; do not block web requests while waiting.
- [ ] Admit only after fresh normal headroom and all ordinary gates pass under the admission lock. Failure, partial reclaim, stale/missing readings, concurrent growth, unavailable delegation and changed cgroup identity preserve the stop. No production cache deletion or ad-hoc cap bypass.
- [ ] Focused regressions cover those cases and worker/reviewer/check contention; disposable capped workload records real launch high water, memory.stat including shmem/inactive_file, PSI/event deltas and route latency. Preserve original reports and label synthetic versus real workload accurately.
- [ ] Explain the actual recovery/remaining gate in UI/observe output, with rate-limited diagnostics. Self-review and exact-head CI precede deployment; a calibration-only outcome is insufficient for this implementation task.

## Link

CG380 profiles broader controller cost; CG382 addresses repeated request scans. This task owns the actual admission repair, not another unconstrained investigation.

## Log

- 2026-09-07T14:44:23+00:00 Operator fast-forward follow-up: evidence-supported implementation remains necessary after CG383 calibration. No worker dispatched during maintenance.
- 2026-09-07T15:17:03+00:00 dispatched work run 20260907T151701Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16086 tokens)
