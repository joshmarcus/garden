---
id: CG-385
title: Recover cache-limited admission through bounded reclaim and a fresh headroom check
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-383
priority: 0
order: 6
difficulty: hard
reading:
- src/garden/scheduler/resources.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/checkruns.py
- tests/scheduler/test_resources.py
- docs/validation/cg383/README.md
branch: garden/cg-385-recover-cache-limited-admission-through-bounded
pr: https://github.com/joshmarcus/context-garden/pull/294
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T23:51:38+00:00'
created: '2026-09-07T14:44:22+00:00'
updated: '2026-09-09T00:43:43+00:00'
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
- 2026-09-07T16:25:19+00:00 triage: changes requested by hand: - **automated review** blocking (`src/garden/resource_reclaim.py`:58): The helper can reclaim a substituted cgroup befor
- 2026-09-07T17:01:33+00:00 dispatched revise run 20260907T170131Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18852 tokens)
- 2026-09-07T17:25:44+00:00 preserved uncommitted worktree changes from run 20260907T170131Z-revise outside the PR: `git stash apply abcedca4af1e06104a264d0f5f9ef4c9137b4589` in /home/joshua/work/worktrees/CG-385 (garden:CG-385:20260907T170131Z-revise:reap)
- 2026-09-07T17:28:12+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/294: Automatic worker and review scheduling now starts one serialized bounded reclaim when cgroup headroom is the sole gate, while descriptor-pinned identity checks prevent reclaiming a substituted target. Real capped disk-cache and served-history evidence demonstrate fresh-headroom recovery and responsive operator surfaces. cost=$3.14
- 2026-09-07T17:33:02+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: focused regressions ; run `garden triage CG-385 --changes "<feedback>" to unblock`
- 2026-09-07T17:38:18+00:00 triage: changes requested by hand: Operator disposition under delegated owner authority: no human action is needed. Prior code defects are accepted as repa
- 2026-09-07T17:38:18+00:00 Operator narrowed repeated-review evidence stop to actual served reclaim behavior; source-equivalent validation-only commit is not itself a code defect. Restored concrete pending feedback and cleared human stop.
- 2026-09-07T17:55:51+00:00 dispatched revise run 20260907T175548Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18287 tokens)
- 2026-09-07T18:17:13+00:00 preserved uncommitted worktree changes from run 20260907T175548Z-revise outside the PR: `git stash apply ce836ad578be5f49b53056b742dff6097e1e737a` in /home/joshua/work/worktrees/CG-385 (garden:CG-385:20260907T175548Z-revise:reap)
- 2026-09-07T18:26:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/294: Added a bounded disposable served journey proving partial real reclaim remains fail-closed, subsequent real reclaim restores headroom, and a fresh normal tick admits one supervised worker while HTTP stays responsive. Corrected the retained-history report documentation so synthetic diagnostic states are not represented as real reclaim or loaded execution. cost=$1.24
- 2026-09-07T18:37:35+00:00 check did not run (20260907T182703Z-check): idle 20 min (no output or file change); will retry
- 2026-09-07T18:38:48+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:40:02+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:41:12+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:42:25+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:43:37+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:44:55+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:46:19+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:47:50+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:49:01+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:50:12+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:51:24+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:52:36+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:53:49+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:55:01+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:56:15+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:57:29+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T18:59:00+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:00:41+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:03:31+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:05:26+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:07:12+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:08:56+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:10:18+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:11:40+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:12:59+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:14:23+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:15:43+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:17:04+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:18:25+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:19:45+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:21:06+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:22:26+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:23:42+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:24:57+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:26:12+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:27:28+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:28:43+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:30:15+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:31:44+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:33:33+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:35:08+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:36:41+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:38:11+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:39:40+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:40:57+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:42:13+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:43:28+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:44:43+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:46:03+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:47:17+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:48:42+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:50:04+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:51:32+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:52:59+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:54:31+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:55:52+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:57:16+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T19:58:50+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:00:45+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:02:12+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:04:02+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:06:51+00:00 Operator-owned environment recovery: preserved failed check evidence and continuation, granted one admission-controlled check retry; no implementation restart or assumed pass. Prevention CG-393/386.
- 2026-09-07T20:06:52+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); will retry
- 2026-09-07T20:08:20+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); will retry
- 2026-09-07T20:09:43+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); will retry
- 2026-09-07T20:11:04+00:00 check did not run (20260907T183736Z-check): idle 22 min (no output or file change); will retry
- 2026-09-07T20:12:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:13:55+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:15:22+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:17:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:18:42+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:20:31+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:22:08+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:23:49+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:25:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:27:26+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:29:05+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:30:41+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:32:16+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:33:34+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:34:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:35:58+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:37:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:38:22+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:39:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:40:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:42:00+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:43:13+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:44:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:45:52+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:47:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:48:16+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:49:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:50:38+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:51:49+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:53:09+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:54:29+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:55:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:57:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T20:58:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:00:29+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:01:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:03:22+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:04:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:06:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:07:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:08:52+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:10:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:11:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:12:48+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:14:00+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:15:13+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:16:25+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:17:41+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:18:57+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:20:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:21:28+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:22:40+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:23:53+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:25:05+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:26:18+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:27:31+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:28:45+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:30:00+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:31:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:31:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:32:13+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:33:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:34:59+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:36:23+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:37:44+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:39:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:41:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:44:06+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:46:43+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:48:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:50:13+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:52:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:54:31+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:56:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T21:58:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:01:08+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:03:09+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:04:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:05:50+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:07:06+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:08:35+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:10:08+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:11:37+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:13:06+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:14:35+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:16:07+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:17:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:19:09+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:20:45+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:21:59+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:23:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:24:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:25:37+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:26:53+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:29:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:30:29+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:31:54+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:34:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:35:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:37:37+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:39:23+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:41:37+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:43:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:46:09+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:48:21+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:50:07+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:51:42+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:53:20+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:55:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:56:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T22:58:44+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:00:24+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:02:17+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:06:25+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:09:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:11:50+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:14:29+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:17:24+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:19:35+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:21:38+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:23:23+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:25:11+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:26:55+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:29:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:31:41+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:33:34+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:35:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:36:52+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:38:30+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:40:07+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:41:42+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:43:43+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:46:16+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:50:01+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:52:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:55:09+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:56:58+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-07T23:58:42+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T00:00:36+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T00:03:17+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:14:50+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:14:53+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:16:05+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:17:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:19:36+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:21:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:23:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:24:59+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:26:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:28:25+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:30:16+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:32:00+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:33:37+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:35:11+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:36:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:39:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:40:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:42:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:44:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:45:52+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:47:31+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:49:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:50:51+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:52:55+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:54:45+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:56:40+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:58:34+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T02:59:43+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:00:52+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:02:05+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:03:29+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:08:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:10:08+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:28:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:28:15+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:29:28+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:30:40+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T03:31:51+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T08:54:55+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T08:54:58+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T08:56:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T08:57:26+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T08:58:36+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T08:59:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:00:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:02:09+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:03:20+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:04:40+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:05:52+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:07:02+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:08:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:09:34+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:10:48+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:12:05+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:14:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:15:50+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:17:31+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:18:47+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:21:50+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:23:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:24:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:25:24+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:26:34+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:27:44+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:28:54+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:30:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:31:19+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:32:38+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:33:53+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:35:13+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:36:28+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:37:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:38:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:40:06+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:41:16+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:42:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:44:38+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:45:51+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:47:02+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:48:17+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:49:30+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:50:42+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:51:59+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:53:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:54:30+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:55:42+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:56:51+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:58:00+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T09:59:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:00:19+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:01:29+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:02:40+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:03:58+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:05:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:06:21+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:07:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:08:42+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:09:53+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:11:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:12:19+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:13:35+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:14:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:15:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:17:21+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:19:09+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:21:11+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:23:15+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:25:13+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:27:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:29:12+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:31:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:33:08+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:35:05+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:37:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:39:07+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:40:19+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:41:38+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:42:53+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:44:10+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:45:43+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:47:07+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:48:22+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:49:36+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:50:46+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:52:01+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:53:16+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:54:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:55:48+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:57:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:58:18+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T10:59:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:00:48+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:02:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:03:19+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:04:29+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:05:41+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:06:51+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:07:59+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:09:49+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:11:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:13:22+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:15:18+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:17:23+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:19:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:21:05+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:22:52+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:24:53+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:26:48+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:28:45+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:30:44+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:32:44+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:34:43+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:36:37+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:38:30+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:40:25+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:42:20+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:44:17+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:46:11+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:48:20+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:50:16+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:52:00+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:53:15+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:53:21+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:54:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:56:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:58:03+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T11:59:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:01:04+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:02:38+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:04:32+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:06:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:08:34+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:10:27+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:12:14+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:13:58+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:15:50+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:17:33+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:20:43+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:22:37+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:23:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:25:57+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:27:07+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:28:45+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:29:56+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:31:07+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:32:20+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:33:31+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:34:50+00:00 check did not run (20260907T201104Z-check): idle 115 min (no output or file change); retry also failed; needs human
- 2026-09-08T12:35:50+00:00 triage: changes requested by hand: Operator audit: actual old CI fails architecture-map registration for resource_reclaim.py; repair this substantive check
- 2026-09-08T12:35:50+00:00 Delegated operator Inbox review: preserved PR/worktree and queued one concrete continuation within current 4 AWS + 1 local limits.
- 2026-09-08T12:50:26+00:00 automated review: request_changes — Bounded reclaim remains fail-closed and ordinary admission gates control the eventual launch; focused tests, disposable workload evidence, UI captures, and exact-head CI pass. The PR description is stale, so the supplied rewrite updates its verification to the reviewed head. cost=$0.81
- 2026-09-08T22:54:35+00:00 dispatched revise run 20260908T225432Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~29722 tokens)
- 2026-09-08T22:59:00+00:00 preserved uncommitted worktree changes from run 20260908T225432Z-revise outside the PR: `git stash apply 84e660bafd3ff33ec4ff765d0ef18264f1ca2914` in /home/joshua/work/worktrees/CG-385 (garden:CG-385:20260908T225432Z-revise:reap)
- 2026-09-08T23:00:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/294: Registered the bounded cgroup reclaim helper in the architecture module map, resolving the substantive old-CI documentation failure without changing runtime admission behavior or production caps. Committed as 4704288bd94be661892d08f1cf39a24ec5da6ae6. cost=$0.92
- 2026-09-08T23:00:58+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/observe.py, src/garden/scheduler/resources.py, src/garden/web/templates/base.html); a rebase agent will resolve it
- 2026-09-08T23:05:13+00:00 automated review: request_changes — The reclaim implementation passes lint and 25 focused tests, but required reviewed-head evidence is missing: the replay never exercises reclaim and exact-head CI is not reported. The branch must also be reconciled with current main. cost=$0.53
- 2026-09-08T23:14:28+00:00 dispatched rebase run 20260908T231425Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8945 tokens)
- 2026-09-08T23:16:52+00:00 preserved uncommitted worktree changes from run 20260908T231425Z-rebase outside the PR: `git stash apply 93205cae564b722e9b464e7c87425229e48ffc71` in /home/joshua/work/worktrees/CG-385 (garden:CG-385:20260908T231425Z-rebase:reap)
- 2026-09-08T23:18:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/294: Rebased onto origin/main and resolved only the marked conflicts. cost=$0.02
- 2026-09-08T23:32:38+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: explain the actual r; run `garden triage CG-385 --changes "<feedback>" to unblock`

## Operator bounded validation disposition 2026-09-08T23:50:16.661542+00:00

Operator-owned investigation result: current83acd1d retains substantive admission-path changes since the old d7ca76b evidence, so source equivalence alone does not close the affected-flow gap. Current controller GitHub state reports exact-head CI SUCCESS, superseding the reviewer missing-CI statement; verify that authoritative receipt instead of launching another full suite. Grant exactly one precise remote evidence revision with the full current review below. Preserve the passing26focusedtests and implemented bounded-reclaim repair. Run only the existing opt-in tests/scheduler/test_resources.py::test_real_disk_cache_reclaim_recovers_normal_tick_admission in a NEW DISPOSABLE DELEGATED CAPPED scope (CPU200%,MemoryHigh1536MiB/Max2GiB,Swap0,RuntimeMax120s; CG385_REAL_REPORT points outside tracked source), plus the smallest actual served diagnostic/loaded-workload verification needed by the frozen criteria. The test intentionally writes600MiB private disk cache and192MiB temporary anonymous memory; do not run it in a production daemon/controller cgroup, change live reserve/caps, delete production cache, start extra hosts, or run an unrelated stress suite. Preserve measured partial/failure, true kernel reclaim, fresh locked admission, actual HTTP bodies/statuses, memory.stat/PSI/events/highwater and clean private-file/helper shutdown. Label synthetic history separately. If a separate delegated scope is unavailable, stop with that exact operator prerequisite and retained source; do not substitute a generic lifecycle replay or another implementation rewrite. Keep per-test120s and suite900s hard bounds. Update PR verification from the actual result.
- 2026-09-08T23:50:17+00:00 triage: changes requested by hand: Operator-owned investigation result: current83acd1d retains substantive admission-path changes since the old d7ca76b evi
- 2026-09-08T23:51:38+00:00 dispatched revise run 20260908T235138Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~33848 tokens)
- 2026-09-08T23:54:13+00:00 worker asks: Can you provide a new disposable delegated scope with CPUQuota=200%, MemoryHigh=1536MiB, MemoryMax=2GiB, MemorySwapMax=0, and RuntimeMaxSec=120s for the single authorized CG-385 evidence run? cost=$0.42
- 2026-09-09T00:43:43+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/294
