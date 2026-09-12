---
id: CG-584
title: Preserve worker completion across standalone scheduler writes
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/web/pages/api.py
- src/garden/runs.py
- src/garden/scheduler/__init__.py
- src/garden/scheduler/reap.py
- src/garden/remote_worker.py
- context-garden/docs/incidents/worker-finish-stale-run-2026-09-10.md
branch: garden/cg-584-preserve-worker-completion-across-standalone-sch
pr: https://github.com/joshmarcus/context-garden/pull/443
runner: remote
freeze_exception: true
freeze_exception_reason: Authenticated completed source can lose its durable completion identity under
  the deployed split topology; preserve recovery and source integrity before closure.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T14:03:13+00:00'
created: '2026-09-10T13:46:55+00:00'
updated: '2026-09-10T14:27:37+00:00'
---

## Goal

Prevent an authenticated worker completion from losing its source-publication, final-receipt or lease metadata when the standalone scheduler saves an older Run. Make the worker claim/heartbeat/finish and scheduler run lifecycle share a process-safe mutation contract in both embedded and split controller topologies, preserving completed source/results and exactly-once promotion.

## Context

CG-516 supplied a concrete failure: authenticated finish HTTP200 and run_finished done at13:19:34, followed at13:19:36 by a stale watch save that cleared pushed_head/final_received_at and reported no commits pushed. The exact committed revision already existed on the origin staging ref and its worker/controller final bytes matched. RC16 is installed; source inspection finds the process-local API guard still present in published but undeployed RC17. This is independent of the disk-full incident.

## Acceptance criteria

- [ ] Establish process-safe serialization or an equally strong atomic merge/CAS contract for claim, heartbeat, finish and scheduler lifecycle mutations. Reload and validate the exact run/lease/source identity at the protected mutation boundary; a threading.Lock in one process is insufficient. Define lock ordering and avoid holding the global scheduler lock across heavy upload, model or provider work.
- [ ] A stale watch observation cannot erase newer pushed_head, final_received_at, claim history, lease/recovery state or completion records. Preserve fencing, deadlines, replay rejection and correct treatment of expired/superseded claims; never recover by fabricating fields or dropping old failures.
- [ ] Deterministically interleave a stale standalone-watch read with a real authenticated finish from another process, then save/reap. Verify the published source and final receipt survive, the original result/usage remain intact, the staging commit is promoted once and the task receives normal exact-head CI/review. Cover heartbeat/claim races and retry/restart boundaries proportionately.
- [ ] Existing embedded-controller and split-controller worker protocol behavior remains compatible with currently deployed workers. Invalid or stale updates fail closed, ordinary requests stay bounded, and result collection is not blocked merely by a scheduling pause.
- [ ] Use the existing portable locking/record APIs for Linux, macOS and Windows through WSL, exercise platform-sensitive behavior with supported alternatives, and report untested environments. Preserve resource caps and active source/results; no live-cloud canary or fleet spending is required.

## Ownership

Coordinate existing CG-497 answer serialization, CG-488/535 durable control-state protection and CG-487 result finalization without duplicating them. This task owns the demonstrated shared Run mutation defect and regression. The final closing account must include the actual repair and post-reopen evidence.

owner_request_key: operator-stale-run-worker-finish-20260910

## Log

- 2026-09-10T13:46:55+00:00 approved (delegated operator; independently confirmed completion race)
- 2026-09-10T13:47:19+00:00 dispatched work run 20260910T134719Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22233 tokens)
- 2026-09-10T13:57:46+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:59:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/443 (base main): Added process-safe, atomic Run persistence that preserves newer authenticated lease and completion metadata across stale scheduler saves, rejects obsolete claim generations, and refreshes remote records before scheduler finalization. Committed as c108eea6; focused tests and repository-wide lint pass. cost=$2.27
- 2026-09-10T14:02:57+00:00 automated review requested changes: The cross-process record lock is sound, but the finish transaction is not atomic and stale lifecycle writes remain lossy. cost=$0.40
- 2026-09-10T14:03:13+00:00 dispatched revise run 20260910T140313Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23675 tokens)
- 2026-09-10T14:15:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:16:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/443: Committed e82422e6, making authenticated heartbeat/finish publication and completion signaling one process-safe transaction and replacing selective stale-state preservation with whole-record three-way merging and generation fencing. Verified 97 focused tests, an exact-final-source 19-test targeted rerun, repository-wide Ruff lint, and clean diff/conflict checks. cost=$2.34
- 2026-09-10T14:20:49+00:00 automated review: approve — The revision preserves authenticated worker completion across stale standalone scheduler writes while fencing obsolete claim generations and retaining normal promotion/check/review behavior. cost=$0.61
- 2026-09-10T14:26:10+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T14:27:37+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/443
