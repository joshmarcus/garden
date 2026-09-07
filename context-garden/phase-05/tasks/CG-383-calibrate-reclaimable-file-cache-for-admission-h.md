---
id: CG-383
title: Calibrate reclaimable file cache for admission headroom
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/config.py
branch: garden/cg-383-calibrate-reclaimable-file-cache-for-admission-h
pr: https://github.com/joshmarcus/context-garden/pull/293
discovered_from: CG-380
last_dispatched_at: '2026-09-07T13:41:13+00:00'
created: '2026-09-07T13:02:16+00:00'
updated: '2026-09-07T14:27:17+00:00'
file: src/garden/scheduler/resources.py
error: The admission sensor counts all memory.current against memory.high; the operator sample had about
  2,198MiB file cache, 5,621MiB host MemAvailable and zero pressure/events but reported only 550MiB cgroup
  headroom.
---

In a disposable cgroup with the existing hard memory cap and reserve, populate file cache, record memory.stat working-set fields and PSI/events, issue bounded memory.reclaim, and measure reclaimed bytes plus a one-slot launch high-water mark. Use the result to decide whether a guarded reclaimable-cache allowance is safe without weakening hard caps, pressure/OOM safeguards, or the owner-configured shared-slot cap.

## Provenance

Discovered by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`.
## Log
- 2026-09-07T13:02:16+00:00 discovered by CG-380
- 2026-09-07T13:03:31+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:04:53+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:06:07+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:07:21+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:08:35+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:09:48+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:03+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:29+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:39+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:12:55+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:14:13+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:15:32+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:16:55+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:18:20+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`

## Acceptance criteria

- [ ] Measure the proposed mechanism on a disposable bounded fixture with exact build, commands and resource deltas.
- [ ] Preserve hard caps, pressure safeguards and data freshness; no production cache deletion or fault injection.
- [ ] Report justified fix or evidence-backed disposition, with focused regression checks and exact-head CI for code changes. Self-review and fix findings.
- 2026-09-07T13:19:25+00:00 approved (operator-incident-followup)
- 2026-09-07T13:19:45+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:21:10+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:22:36+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:24:01+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:25:27+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:26:42+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:27:57+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:29:10+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:30:25+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:31:40+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:32:56+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:34:12+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:35:29+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:36:59+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:41:13+00:00 dispatched work run 20260907T134111Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~16441 tokens)
- 2026-09-07T13:56:40+00:00 preserved uncommitted worktree changes from run 20260907T134111Z-work outside the PR: `git stash apply a7be75584c06626c6a01459ceab816debea5f690` in /home/joshua/work/worktrees/CG-383 (garden:CG-383:20260907T134111Z-work:reap)
- 2026-09-07T13:56:40+00:00 worker asks: May I temporarily stash the pre-existing unrelated docs/design/snapshot.json modification solely to run scripts/check_ci.py on commit 4c5a956, then restore it unchanged? cost=$1.15

## Operator answer and continuation

Owner delegates routine preservation. Yes: temporarily stash the unrelated docs/design/snapshot.json solely for exact-head CI validation, keep its named stash/hash, and restore it unchanged afterward. Scheduler already salvaged the dirty snapshot as a7be75584c06626c6a01459ceab816debea5f690; inspect current state before stashing again. Preserve implementation commit4c5a956 and continue validation/review, not a fresh implementation. Do not discard or commit the snapshot to this PR, alter production cache/caps, or repeat already-passing validation without cause.
- 2026-09-07T14:02:44+00:00 reset to ready by hand
- 2026-09-07T14:27:15+00:00 Operator fast-forward: calibration PR293 merged d14afc5 after exact CI and self-review; production admission policy remains a follow-up.
- 2026-09-07T14:27:17+00:00 Operator fast-forward: GitHub merge verified d14afc5310bf426af4d283ca8174c21219c58260; exact-head CI and operator self-review passed. Not yet deployed.
