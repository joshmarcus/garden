---
id: CG-358
title: Keep incident control actions responsive and retry-safe during web overload
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading: []
branch: garden/cg-358-keep-incident-control-actions-responsive-and-ret
pr: https://github.com/joshmarcus/context-garden/pull/239
attempts: 1
last_dispatched_at: '2026-09-07T03:40:33+00:00'
created: '2026-09-06T19:13:47+00:00'
updated: '2026-09-07T09:13:19+00:00'
---

## Goal

Keep recovery controls usable during overloaded page rendering and make timed-out mutations safe to reconcile without duplicate launches.

## Context

2026-09-06 web incident: dynamic requests repeatedly scanned history and saturated request threads. Priority CG-357 dispatch itself took minutes; HTTP clients timed out while task_action continued. Restart interrupted a no-PID startup and left setup children. Operator inspected Python stacks and run files to distinguish queued/startup/live states before retrying. See context-garden/docs/incidents/2026-09-06-web-responsiveness-retro.md. CG-357 repairs the measured read amplification; this task protects recovery controls from a future expensive read path. CG-338 owns resource admission and CG-355 owns updater lifecycle.

## Acceptance criteria

- [ ] Under a reproducibly slow/overloaded read path, pause, health/status and bounded recovery launch remain available within documented latency bounds using an isolated control path or equivalent bounded design; no expensive full-history dependency in liveness checks.
- [ ] Mutation requests expose durable operation/run identity and meaningful requested/preparing/running/finished states. Retrying after client timeout cannot create duplicate work; concurrency tests cover an original request that continues after disconnect.
- [ ] Restart during preparation preserves work and reconciles orphaned setup exactly once. A no-PID preparing record never counts as confirmed live work; escaped descendants are accounted for with CG-338.
- [ ] Integration validation overloads a disposable served app, times out/retries a mutation and restarts during preparation; verifies responsiveness, exactly one worker, preserved state and unchanged resource caps. No fault injection on live garden.

## Counterfactual

A responsive, durable recovery action would have started CG-357 promptly and avoided manual stack inspection and ambiguous restart/retry handling, shortening the outage even before a full history-index fix existed.

## Log

- 2026-09-06T19:40:17+00:00 dispatched work run 20260906T193955Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~8672 tokens)

20:13 operator-race evidence: between observation and retry, automatic dispatch started CG-338 revision201038; retry cancelled the just-started worker. Preserve expected-run identity on control actions (optimistic precondition / compare-and-act); reject a stale retry rather than silently cancelling a newer run. This counterfactual prevents observation/action races even when the HTTP response is healthy. Dirty work was preserved in operator-test-tmp/CG338-retry-race-2013.patch and task requeued.
- 2026-09-06T20:28:59+00:00 opened https://github.com/joshmarcus/context-garden/pull/239 (base main): Incident controls now remain responsive independently of expensive task/history reads, while recovery launches expose durable lifecycle identity and deduplicate retries. Interrupted preparation is reconciled once, including setup children that survive a server restart. cost=$7.00
- 2026-09-06T20:37:21+00:00 automated review requested changes: Health and pause use a bounded read path, and preparation records improve restart reconciliation. However, recovery dispatch remains synchronous without a client-visible idempotency identity, the claimed integration scenario is only an in-process unit simulation, and the PR includes an unrelated runtime snapshot. cost=$0.45
- 2026-09-06T20:47:05+00:00 dispatched revise run 20260906T204704Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9881 tokens)
- 2026-09-06T21:15:13+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/239: Incident controls now remain responsive when ordinary ASGI request workers are exhausted. Recovery launches return a durable identity before preparation, safely replay client keys, reject stale observations, and resume the same preparation record after server restart without duplicating setup or workers. cost=$5.41
- 2026-09-06T21:15:18+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py); a rebase agent will resolve it
- 2026-09-07T01:22:51+00:00 dispatched rebase run 20260907T012250Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8318 tokens)
- 2026-09-07T01:26:32+00:00 preserved uncommitted worktree changes from run 20260907T012250Z-rebase outside the PR: `git stash apply 10ae391b5581c804d5983439206a2678dcdb71c9` in /home/joshua/work/worktrees/CG-358 (garden:CG-358:20260907T012250Z-rebase:reap)
- 2026-09-07T01:27:43+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/239: Rebased CG-358 onto origin/main and resolved all rebase conflicts while preserving both sides and the pre-existing snapshot change cost=$0.04
- 2026-09-07T02:19:38+00:00 triage: changes requested by hand: PR239 exact-head CI34073026576 failed two concrete cases: tests/scheduler/test_restart.py::test_restart_reconciles_a_no_
- 2026-09-07T02:20:16+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-358`) or send it back (`garden triage CG-358 --changes "..."`)
- 2026-09-07T02:25:06+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T03:40:33+00:00 dispatched revise run 20260907T034031Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10472 tokens)
- 2026-09-07T03:50:35+00:00 preserved uncommitted worktree changes from run 20260907T034031Z-revise outside the PR: `git stash apply a12fff38e9dda706e8a246c029cb8c5391dea1ec` in /home/joshua/work/worktrees/CG-358 (garden:CG-358:20260907T034031Z-revise:reap)
- 2026-09-07T04:00:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/239: Reconciled interrupted preparation by indexing requested and preparing runs as active reservations, while retaining the idempotency-key distinction that preserves replayable recovery work. The disposable served-app integration now uses the active Python interpreter and exact-head CI passes. cost=$1.10
- 2026-09-07T04:07:19+00:00 stalled: review finding repeated after a revise round: ui captures not read for: board, board-list, config, events, herbarium, inbox, n; run `garden triage CG-358 --changes "<feedback>" to unblock`
- 2026-09-07T09:13:18+00:00 triage: changes requested by hand: All functional criteria were accepted; the remaining blanket missing-images stop was environmental. CG326/370 capture fi
- 2026-09-07T09:13:19+00:00 re-enabled by hand; revise run will follow
