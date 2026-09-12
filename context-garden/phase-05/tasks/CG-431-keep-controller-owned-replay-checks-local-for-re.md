---
id: CG-431
title: Keep controller-owned replay checks local for remote-authored tasks
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 1
difficulty: medium
reading:
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/review.py
- src/garden/runner/remote.py
- src/garden/web/pages/api.py
- tests/test_review.py
- tests/test_runners.py
branch: garden/cg-431-keep-controller-owned-replay-checks-local-for-re
pr: https://github.com/joshmarcus/context-garden/pull/320
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T15:21:44+00:00'
created: '2026-09-08T14:59:03+00:00'
updated: '2026-09-08T16:03:28+00:00'
---

## Goal

Choose the check execution backend from the check's actual inputs and ownership. Remote implementation must not send a controller-owned replay command to an unrelated AWS filesystem.

## Repeated production evidence

On rc5, CG409, CG401 and CG412 interaction_replay checks inherited Task.runner=remote. Their literal commands reference /home/joshua/garden/.venv/bin/python3, a controller /home/joshua/work/worktrees/CG-N source checkout and .garden/interaction-replays output directory. The AWS worker cannot use those paths. Several unclaimed checks were then declared idle from old worktree activity and created needs-human stops. CG409/401 were recovered through supported local replay/review routing; CG412's already queued check is preserved, with future retry/review routed locally. Original source, runs and failures are retained.

## Acceptance criteria

- [ ] Controller-owned replay commands use the controller's normal local admission even when their authoring task is remote; record actual backend and provenance.
- [ ] Portable checks and AWS full ordinary suites remain eligible for remote execution. Do not copy controller credentials/paths into a worker or silently treat an unexecuted check as passed.
- [ ] Retries preserve correct check-backend ownership and continuation identity, without changing the implementation task's permanent runner or duplicating active work.
- [ ] Add focused scheduler/runner regressions for a remote-authored task with controller-owned replay, a genuinely portable remote check, and a retry after an environmental failure.
- [ ] Coordinate the observed stale-worktree/unclaimed-check age issue with existing CG393 and collected-check idempotency with CG386. Reuse their work rather than bundling unrelated implementations.

## Context

Owner delegates clearing human-input stops and requires meaningful outcome verification, with metadata alone advisory. This is a routing defect that prevented real execution, not grounds to invent evidence. Evidence: /home/joshua/work/operator-test-tmp/human-input-20260908T1405 and heartbeat-20260908T1454. Current controller rc5 remains pinned; this task does not authorize a new release deployment or live-task interruption.

## Log

- 2026-09-08T15:01:58+00:00 approved (operator-repeated-check-routing-recovery)
- 2026-09-08T15:21:44+00:00 dispatched work run 20260908T152144Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16286 tokens)
- 2026-09-08T15:46:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/320 (base main): Controller-owned interaction replay checks now dispatch locally for remote-authored tasks, while portable checks remain remote-capable. Check backend/provenance persists through automatic and delegated retries. cost=$1.32
- 2026-09-08T16:01:41+00:00 automated review: approve — Controller-owned replay checks are correctly routed locally while portable checks retain remote eligibility, and backend ownership survives automatic and delegated recovery. Focused regressions, adjacent suites, lint, and disposable served interaction passed at the reviewed head. cost=$0.48
- 2026-09-08T16:02:10+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-08T16:03:28+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/320
