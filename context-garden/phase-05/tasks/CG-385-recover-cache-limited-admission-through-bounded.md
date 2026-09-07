---
id: CG-385
title: Recover cache-limited admission through bounded reclaim and a fresh headroom check
status: changes_requested
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
pr: https://github.com/joshmarcus/context-garden/pull/294
attempts: 1
last_dispatched_at: '2026-09-07T15:17:03+00:00'
created: '2026-09-07T14:44:22+00:00'
updated: '2026-09-07T16:15:34+00:00'
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
- 2026-09-07T15:51:22+00:00 preserved uncommitted worktree changes from run 20260907T151701Z-work outside the PR: `git stash apply 35021ba8ee232ca3816fd5a8c145102d6c111aaf` in /home/joshua/work/worktrees/CG-385 (garden:CG-385:20260907T151701Z-work:reap)
- 2026-09-07T16:08:46+00:00 opened https://github.com/joshmarcus/context-garden/pull/294 (base main): Cache-limited local admission can now launch one bounded, timed cgroup reclaim helper while preserving every ordinary admission gate. Launches remain stopped until a later locked admission check observes fresh headroom, and operator surfaces report the measured result or error. cost=$4.52
- 2026-09-07T16:14:54+00:00 automated review requested changes: Reclaim remains fail-closed for admission, but cgroup identity is checked too late to prevent reclaiming a substituted target. The required served scalability evidence is also incomplete. cost=$0.68

## Blocking direct operator review, 2026-09-07

1. P1: Ordinary automatic scheduling never starts eligible reclaim. scheduler/resources.py:383-386 only calls _start_reclaim_if_eligible from _admit_local_launch. dispatch.py:105-106 and review_slots_free instead stop at local_slots_free==0 first; the tick's refresh_resource_pressure only records status. A disposable normal sched.tick with the existing cache-limited fixture records pressure but makes zero reclaim attempts. Repair the normal scheduling entry point under the admission lock, retaining side-effect-free readers and fresh admission checks. Cover ready workers AND queued reviews across ticks, including successful recovery.

2. P1: Reclaim-state reads mutate shared files without serialization. resource_status -> _reclaim_description -> _reclaim_state can be called by concurrent web readers and scheduler writers. _write_reclaim_state uses one PID-based temporary filename, so concurrent same-process publications collide and one os.replace raises FileNotFoundError. The deterministic two-thread reproduction fails. Make read paths side-effect free, serialize state reconciliation/helper ownership, and use unique atomic temporary files. Verify reads cannot clobber a newer helper, spawn duplicates or return500.

3. P1 evidence gap: The retained-history workload records ~155MiB peak under1536MiB memory.high, does not create cache-limited admission and never invokes real reclaim. It cannot show that CG385 resolves this incident. Retain that useful responsiveness evidence, but add a disposable bounded disk-cache workload that crosses the configured admission reserve, triggers recovery through the normal tick, verifies real headroom before/after and then admits one real supervised task. Record concurrent-growth/failure behavior and route responsiveness. No production cache experiment or relaxed cap.

Reproductions: test_operator_review.py uses the PR's existing tests.conftest and _cache_limited fixture; run with PYTHONPATH=<PR>:<PR>/src. Both asserted regressions fail on the reviewed head in0.33s,61.7MiB peak/noSwap underCPU200%/MemoryMax1GiB. The first initial harness invocation lacked the root fixtures; that setup error was corrected before the two real failures were recorded. These tests do not change production state.
- 2026-09-07T16:15:34+00:00 Owner-requested operator review of11064356 found two reproduced blockers and missing real-reclaim acceptance evidence. Do not merge this head; preserve active automated review, address the inline findings in the next revision. Source checkout unchanged.
