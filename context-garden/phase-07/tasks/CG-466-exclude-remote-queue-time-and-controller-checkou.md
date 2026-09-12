---
id: CG-466
title: Exclude remote queue time and controller checkouts from idle timeouts
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/runs.py
- src/garden/scheduler/reap.py
- src/garden/remote_worker.py
- tests/test_remote_worker.py
- tests/scheduler/test_reap.py
- docs/worker-protocol.md
branch: garden/cg-466-exclude-remote-queue-time-and-controller-checkou
pr: https://github.com/joshmarcus/context-garden/pull/363
runner: remote
discovered_from: CG-457
attempts: 1
last_dispatched_at: '2026-09-09T14:31:33+00:00'
created: '2026-09-09T03:25:44+00:00'
updated: '2026-09-09T15:17:14+00:00'
---

## Goal

Repair the remaining remote idle-time accounting path from CG457 so queued time and unrelated controller checkout mtimes cannot prematurely time out a valid remote model/check execution.

## Context

Provenance marker: CG406-025423-post-RC9-idle. This is a precise follow-up to merged/deployed CG457, separate from CG428's confirmed transient HTTP502 retry behavior. Do not duplicate either task's existing implementation.

Actual post-RC9 CG406 check 20260909T025423Z-check was queued/started at2026-09-09T02:54:23.460772Z and first claimed/execution_started at03:01:49.832611Z. No controller stdout.json or stderr.log was ever created. The record still points worktree at /home/joshua/work/worktrees/CG-406, which is the controller checkout, not the independent host's checkout. A later host5 generation was claimed03:12:34 with a valid600-second lease through03:22:34. Nonetheless the controller timed it out at03:14:27 with idle20min, after only12m37s since first actual claim. Its original timeout/result/no-results evidence and task attention stop remain retained.

Installed RC9 runs.idle_minutes clamps the latest measured local mtime to started_at, while execution_minutes correctly uses execution_started_at or claimed_at. Scheduler._finished_or_timed_out applies idle_minutes to remote checks as well. This makes queue time and an unrelated controller worktree look like remote execution silence. Source and event receipts are in /home/joshua/work/operator-test-tmp/input-sweep-20260908T2125/cg406-post-rc9-idle-proof.json.

## Acceptance criteria

- [ ] Remote idle accounting excludes unclaimed queue duration. Use the actual execution-start marker with a documented claimed_at compatibility fallback; preserve original queued/started/claim/generation timestamps across reload, reclaim and legacy records. The observed CG406 run cannot reach20 execution-idle minutes at03:14:27.
- [ ] Independent remote execution does not use the controller checkout's mtime as evidence of remote progress or silence. Define proportionate behavior for a remote check with no streamed output, a valid active lease, and genuinely idle remote work; preserve bounded execution deadlines and existing safe local idle accounting. Do not conceal failures by treating every claimed record as productive forever.
- [ ] Focused regressions exercise long queue then first claim, stale controller worktree, no remote output, legacy/reclaimed records, a real execution-idle expiry and unchanged overall execution deadline. Record actual scheduler timeout decisions with controlled time; no broad application replay, load matrix or stress suite is required.
- [ ] Preserve the original CG406 timeout, source and durable run evidence. This implementation does not clear its live stop, invent a passing check, rewrite an expired generation, or dispatch a blind retry. After a versioned fix is deployed, the operator may perform one guarded actual resumption of the required current-source check.

## Out of scope

Transport reconnect/retry remains CG428's owner. Do not hotpatch runtime packages, change host/global/local/reviewer caps or AWS deadlines, disable idle enforcement globally, or rerun unrelated author work.

## Log

- 2026-09-09T03:25:44+00:00 approved (delegated-operator-proven-remote-idle-followup)
- 2026-09-09T03:49:13+00:00 dispatched work run 20260909T034913Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15127 tokens)
- 2026-09-09T04:01:14+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T04:04:09+00:00 opened https://github.com/joshmarcus/context-garden/pull/363 (base main): Remote idle accounting now begins at first execution claim, ignores controller-checkout mtimes, and still expires genuinely silent remote work while preserving overall deadlines. Focused remote-worker/reap suites passed 85 tests and Ruff passed at commit 0417c578. cost=$1.71
- 2026-09-09T04:09:36+00:00 automated review:  —
- 2026-09-09T05:11:14+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/api.py); a rebase agent will resolve it
- 2026-09-09T09:42:45+00:00 dispatched rebase run 20260909T094245Z-rebase-2 via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1576 tokens)
- 2026-09-09T09:45:25+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/363: Rebased CG-466 onto origin/main and resolved the api.py conflict. cost=$0.01
- 2026-09-09T09:48:45+00:00 automated review requested changes: The remote accounting logic appears sound, but the new legacy-reclaim regression fails deterministically, so the focused suite is not green. cost=$0.40
- 2026-09-09T09:52:34+00:00 dispatched revise run 20260909T095234Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16145 tokens)
- 2026-09-09T09:57:52+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T09:59:24+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/363: Fixed the deterministic legacy reclaim regression by expiring recovery_expires_at alongside lease_expires_at, so the test exercises a genuinely reclaimable record. The affected remote-worker/reap suites completed successfully, the specific reported regression passed, and Ruff passed at committed head 5ccc6866. cost=$0.43
- 2026-09-09T10:03:22+00:00 automated review: approve — Remote idle accounting correctly excludes queue time and controller-checkout mtimes while retaining bounded idle and execution deadlines. cost=$0.26
- 2026-09-09T14:28:27+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T14:31:33+00:00 dispatched revise run 20260909T143132Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16861 tokens)
- 2026-09-09T15:02:30+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:06:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/363: Merged current main to incorporate the decision-before-waiting-status correction while preserving the remote idle-accounting implementation. At merged head 3ce96931, 121 focused remote-worker/reap/decision tests passed, the full ordinary suite exited 0, and Ruff passed. cost=$1.44
- 2026-09-09T15:12:22+00:00 automated review: approve — Remote idle accounting correctly excludes queue time and controller-checkout mtimes while retaining genuine idle expiry and the independent execution deadline. cost=$0.39
- 2026-09-09T15:15:29+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T15:17:14+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/363
