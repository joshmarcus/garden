---
id: CG-599
title: Bound cleanup so historical branch scans do not stall scheduling and collection
status: done
product: context-garden
phase: phase-05
depends_on: []
kind: bug
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/__init__.py
- src/garden/gitops.py
branch: garden/cg-599-bound-cleanup-so-historical-branch-scans-do-not
pr: https://github.com/joshmarcus/context-garden/pull/477
runner: remote
discovered_from: CG-527
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T21:45:39+00:00'
created: '2026-09-10T21:44:58+00:00'
updated: '2026-09-10T22:50:52+00:00'
---

## Goal

Keep automatic branch and storage cleanup from monopolizing the shared controller lock and delaying result collection, subsequent dispatch and operator actions. Repair the demonstrated RC19 regression through normal versioned source and review. Preserve cleanup ownership and data-loss protections.

## Reproduction and evidence

Exact RC19 70ae9179ae6e2af865aef5a8cecca90460328c4d, controller watch PID1266403, ordinary dispatch resumed21:26:53UTC. Five real remote runs were queued21:27:20–22 and all five were claimed by distinct workers21:27:20–27. Four returned authenticated finals21:28:45–21:30:35, but scheduler collection did not happen until21:41:19–30 after one guarded SIGINT interrupted only a read-only ls-remote scan. The reviewed ingress installer and operator task registration also waited for tick.lock. Worker protocol operations themselves continued: preserve this corrected distinction and the original mistaken inference as superseded. The scheduler subprocess repeatedly runs git ls-remote --heads origin refs/heads/<one historical task branch>, cycling across the roughly600-task live history. Read-only snapshots and original deployment/results remain under operator-test-tmp/rc19-deploy-20260910; no process or installed source has been modified to hide the problem.

scheduler._tick_body unconditionally calls storage sweep then branch sweep under _controller_lock. storage_inventory first calls branch_cleanup_inventory; sweep_worker_branches calls it again, and _branch_delete_recheck calls it again for each candidate. classify_branches loops recorded provenance and performs a separate remote query per branch before cheap active/protected checks. The new shared lock required by CG584 correctly prevents races, but this unbounded network fanout starves normal scheduler progress. branches.cleanup_limit=0 still builds the full inventory, so it is not a working operational disable.

## Acceptance criteria

- [ ] Reproduce the number of remote operations and shared-lock starvation deterministically with a representative large historical provenance fixture. Preserve live timing as failure evidence, and distinguish queued jobs from real claimed/running work.
- [ ] Make automatic cleanup bounded in remote requests and elapsed work, proportionate to repositories or a configured per-pass budget rather than all historical branches times candidates. Use current remote authority for deletion; a missing, failed, stale or truncated inventory must conservatively preserve data. Batch remote observations or equivalent bounded design may be used. Eliminate redundant full-inventory scans during immediate candidate rechecks while retaining fresh ownership/head/PR checks and compare-and-swap deletion.
- [ ] Ensure native result collection, subsequent dispatch and operator actions progress without an unbounded cleanup scan. Preserve independently functioning worker claims, heartbeat and authenticated finish, the CG584 cross-process Run mutation lock and its two-process regression; do not remove locks or invent completion metadata. Keep automatic ordinary dispatch running and keep eventual cleanup possible.
- [ ] Provide an effective supported way to disable automatic cleanup for recovery, checked BEFORE expensive inventory or deletion; do not use fake remotes or alter Git/provider credentials. Exercise disabled behavior and enabled bounded behavior without live deletion or new cloud spending.
- [ ] Retain protections for active, queued, manual/external, open-PR, stacked-base, uncertain, unmerged, changed-head and symlink/foreign work; preserve legacy run evidence and worker/result files. No broad cleanup is authorized by this repair.
- [ ] Run focused scheduler, branch cleanup, storage cleanup and cross-process protocol tests plus Ruff sequentially, obtain independent review and actual exact-head CI, and report exact tested source and untested platforms. Support Linux, macOS and Windows through WSL with capability checks where needed. Do not hotpatch installed RC19 or publish/deploy from this worker; root owns reviewed release activation.

## Closing account

This is a new observed rollout blocker distinct from the already-merged CG598 metrics aggregation repair and CG593 main CI correction. CG537 must record this failure and the accepted correction before recommending closure. Do not edit its manual worktree, cancel its reservation, or alter original retro reports.

owner_request_key: rc19-cleanup-starves-worker-protocol-20260910

## Log

- 2026-09-10T21:44:59+00:00 approved (delegated operator: actual RC19 shared-lock cleanup starvation)
- 2026-09-10T21:45:39+00:00 dispatched work run 20260910T214539Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16216 tokens)
- 2026-09-10T22:20:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T22:26:33+00:00 opened https://github.com/joshmarcus/context-garden/pull/477 (base main): Bound automatic cleanup to one time-limited remote snapshot per repository, removed historical branch rescans from candidate rechecks, and made zero cleanup limits effective before inventory. Exact head 8df02641 passed 84 focused tests and Ruff and received independent approval. cost=$1.59
- 2026-09-10T22:43:19+00:00 Manual mode reserved by operator: Preserve recovered CI-pending review; operator independently reviews exact green head for merge without another author revision.
- 2026-09-10T22:50:14+00:00 returned from Manual mode to automation
- 2026-09-10T22:50:27+00:00 automated review requested changes: The cleanup implementation is bounded and conservative, but required exact-head CI is still pending. cost=$0.51
- 2026-09-10T22:50:52+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/477
