---
id: CG-358
title: Keep incident control actions responsive and retry-safe during web overload
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading: []
branch: garden/cg-358-keep-incident-control-actions-responsive-and-ret
attempts: 1
last_dispatched_at: '2026-09-06T19:40:17+00:00'
created: '2026-09-06T19:13:47+00:00'
updated: '2026-09-06T19:40:17+00:00'
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
