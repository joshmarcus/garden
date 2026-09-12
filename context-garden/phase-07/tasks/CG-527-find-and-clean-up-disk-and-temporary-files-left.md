---
id: CG-527
title: Clean up abandoned worker branches, worktrees and temporary files
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-310
- CG-498
priority: 0
difficulty: hard
reading:
- src/garden/runner/local.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/resources.py
- src/garden/runs.py
- src/garden/config.py
- src/garden/gitops.py
branch: garden/cg-527-clean-up-abandoned-worker-branches-worktrees-and
pr: https://github.com/joshmarcus/context-garden/pull/444
attempts: 1
last_dispatched_at: '2026-09-10T14:56:44+00:00'
created: '2026-09-10T12:41:04+00:00'
updated: '2026-09-10T15:14:51+00:00'
---

## Goal

Find the disk and temporary files that Garden leaves behind on the controller machine and local workers, and fix their lifecycle cleanup so repeated work does not exhaust storage. This is a development task to investigate and implement cleanup behavior, not a request for an immediate operator cleanup.

## Context

The owner requested a task after the Windows disk backing the Garden WSL machine filled completely. WSL still reported ample virtual filesystem space; the controller became unavailable and a just-received run result had empty saved payload files. The responsible accumulation categories have not yet been established. Measure them before attributing the problem to Git branches or choosing deletion rules.

CG-310 already implements per-run temp cleanup and terminal-worktree cache retention; CG-498 owns obsolete worker-branch cleanup. Inspect those mechanisms and address the remaining gaps rather than duplicating their completed scope. Include abandoned setup/check/worker attempts, trial and auxiliary work, interrupted or crashed runs, worktree environments and caches, and Garden-generated scratch/output directories where evidence establishes leakage. Distinguish branch references, repository objects, worktrees, virtual environments, temporary data and retained run artifacts in the accounting.

## Acceptance criteria

- [ ] Produce a bounded storage inventory for the controller and local workers, with bytes by owned directory/category, lifecycle owner, eligibility for cleanup and retained reasons. Identify the actual paths and missing cleanup triggers behind material accumulation; do not infer causation from branch counts or directory age alone.
- [ ] Implement the missing normal-completion, cancellation, failed-setup, crash/restart and abandoned-attempt cleanup paths. Provide a bounded, idempotent way to sweep existing eligible leftovers with preview and configurable retention, using existing cleanup mechanisms where applicable.
- [ ] Protect active and queued runs, leases, checked-out or dirty worktrees, unmerged unique work, manual/external ownership, installed/rollback runtimes, and required result/transcript/recovery evidence. Recheck ownership and liveness immediately before removal; uncertain paths remain visible with a reason. Do not follow symlinks or reparse points outside the owned root.
- [ ] Report the free-space constraint that can actually prevent writes. Where supported, distinguish WSL guest free space from its Windows backing-volume free space; otherwise report unavailable host measurements explicitly. Keep platform-specific probes behind capability checks and do not resize or compact disks automatically as part of ordinary cleanup.
- [ ] Record what was reclaimed, bytes reclaimed, retained paths and reasons, and partial or failed deletions. Interrupted sweeps and retries must preserve durable evidence and must not turn missing or unwritten result data into successful completion.
- [ ] Verify meaningful lifecycle and concurrency cases using disposable fixtures, including repeated runs, failed setup, restart recovery, an active/dirty worktree, required evidence, foreign paths, symlink escapes and deletion failure. Use portable APIs/configurable paths for Linux, macOS and Windows through WSL; report any platform not exercised.

## Scope

Investigate and fix Garden-owned storage retention. Coordinate with existing branch cleanup and result-durability owners. This task does not authorize deletion of unrelated user files, live work, credentials, or the WSL virtual disk.

owner_request_key: owner-disk-temp-retention-20260910

## Owner clarification: branches and worktrees

The owner identifies accumulated worktrees as a major suspected contributor and explicitly requires cleanup of BOTH worker branches and worktrees. Make their combined lifecycle a primary part of this task. Measure disk use in worktrees and their virtual environments, build outputs and caches; inventory branch references and retained Git objects separately so branch counts do not stand in for disk measurements.

CG-498 supplies branch-cleanup primitives; investigate remaining retention or integration gaps and coordinate removal of eligible Garden-owned branches and worktrees, including existing backlog, ordinary workers, superseded attempts and trials. A branch being retained because a worktree still references it must be explained and resolved safely when that worktree is no longer needed. Preserve live, dirty, unmerged, externally owned and recovery-required work as specified above.

- [ ] Demonstrate that an eligible completed worker's branch AND worktree, including its generated environments/caches, can be reclaimed in the correct order; demonstrate that active, stacked, dirty and uniquely unmerged work remains protected. Report actual bytes reclaimed and the concrete reason for every retained branch/worktree.


## Measured cleanup evidence, September 10

The read-only inventory found 46 GiB under the worktree root, including per-task scratch homes, 11 GiB of operator scratch data, and 12 GiB of retained Garden run/state data. The worktree-root figure must not be described as Git branch storage.

A guarded cleanup removed six clean worktrees whose heads were reachable from main and 265 disposable browser/package cache directories belonging to completed tasks whose corresponding worktrees were already absent. It reclaimed 35,017,486,336 bytes (32.6 GiB) inside WSL. Source branch references, active/unfinished worktrees, dirty or uniquely unmerged work, separately owned CG-423, installed runtimes, saved reports/transcripts and recovery payloads were preserved. Exact candidates, retained reasons and results are in /home/joshua/work/operator-test-tmp/side-disk-cleanup-20260910/{plan.json,result.json}; this is measured operator evidence, not proof that the automatic lifecycle fix is implemented.

Thirty-one orphan browser caches were each about 656 MiB; their newest download-link records were from September 7. Per-task pip caches continued accumulating across completed tasks. Current product setup already supplies a shared PLAYWRIGHT_BROWSERS_PATH, so investigate its effective propagation before adding another setting or claiming current browser downloads still duplicate. The clear lifecycle gap is that deleting a Git worktree does not necessarily reclaim the adjacent .garden-home-<task> caches.

- [ ] Include adjacent isolated worker homes, trial/probe/check homes and their disposable caches in lifecycle accounting and bounded cleanup; do not remove private model sessions or required evidence merely because the worktree disappeared. Exercise the exact orphan-home case with a completed task and no remaining Git worktree.
- [ ] Bound future cache growth with explicit ownership, size/age limits and safe reuse or retirement. Keep cleanup incremental so a large existing backlog does not monopolize a scheduler tick. A repeated completed-task workload must reach a measured storage plateau under the selected retention policy.

Coordinate with the separate owner-selected 20 GiB physical-disk admission task. This task supplies reclamation and retention; that task prevents new work or large materialization from exhausting required backing storage.

storage-measurement-20260910-side

## Log

- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T13:40:36+00:00 dispatched work run 20260910T134031Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20285 tokens)
- 2026-09-10T14:01:41+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:03:00+00:00 opened https://github.com/joshmarcus/context-garden/pull/444 (base main): Implemented bounded, idempotent storage inventory and cleanup for worktrees, run temp directories, worktree caches, and adjacent isolated worker homes. Verified lifecycle protection, orphan cleanup, worktree-before-branch ordering, durable audits, byte accounting, symlink safety, deletion failures, and bounded repeated cleanup with 108 focused tests; required Ruff lint passed. cost=$4.67
- 2026-09-10T14:05:26+00:00 automated review requested changes: Cleanup can escape its owned root through an intermediate symlink, and deletion evidence is not crash-durable. cost=$0.50
- 2026-09-10T14:10:39+00:00 dispatched revise run 20260910T141036Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21367 tokens)
- 2026-09-10T14:16:55+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:18:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/444: Hardened storage cleanup against intermediate symlink/reparse-point escapes and made destructive sweep evidence crash-durable with pre-operation receipts, per-operation updates, and restart reconciliation. Committed as 2906b441; 9 focused tests and required Ruff lint passed. cost=$0.84
- 2026-09-10T14:20:56+00:00 automated review requested changes: The guarded deletion and crash-durable receipts are improved, but abandoned nonstandard worktrees remain permanently ineligible for cleanup. cost=$0.65
- 2026-09-10T14:21:17+00:00 dispatched revise run 20260910T142114Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21759 tokens)
- 2026-09-10T14:28:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:30:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/444: Saved run paths and branches now identify nonstandard abandoned worktrees, including failed ordinary attempts and trials. Cleanup retains active, external, dirty, or uniquely unmerged work and reclaims eligible managed attempts; committed as 03d807e0. cost=$1.40
- 2026-09-10T14:32:31+00:00 automated review requested changes: Cleanup coverage and ownership protections are strong, but destructive-operation evidence is still not crash-durable. cost=$0.35
- 2026-09-10T14:49:49+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:56:44+00:00 dispatched revise run 20260910T145641Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22259 tokens)
- 2026-09-10T15:02:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:04:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/444: Committed b7dc7942, closing the destructive cleanup crash window with fsynced pending-operation records and conservative restart reconciliation. Current-head focused storage/architecture tests passed (11 tests), and required Ruff lint passed. cost=$0.91
- 2026-09-10T15:06:40+00:00 automated review: approve — Cleanup is bounded, conservative, crash-audited, and integrates worktree removal before existing branch reclamation while preserving uncertain or live storage. cost=$0.49
- 2026-09-10T15:14:51+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/444
