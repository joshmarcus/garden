---
id: CG-667
title: Make command CI asynchronous and resource bounded
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-08/goals.md
- src/garden/ci_status.py
- src/garden/scheduler/__init__.py
- src/garden/run_supervisor.py
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T17:05:13+00:00'
---

## Goal

User value: a slow or noisy adapter cannot stall unrelated work or consume unbounded controller memory. Why now: queries run synchronously under the controller lock and output is capped only after buffering. Size: hard. Dependencies: existing command-CI exact-head contract and detached-work/process supervision. Consume bounded stdout and stderr, terminate owned processes on timeout or overflow, and accept results only for the unchanged source and provider policy.

## Context

Proposed at the context-garden/phase-07 retro. Enterprise adapter failures should remain isolated while exact-head merge protection stays intact.

## Acceptance criteria

- [ ] Move potentially slow command-CI execution outside the controller critical section with accounted, restart-recoverable work. A stalled adapter does not block unrelated collection or locked operator actions.
- [ ] Consume stdout/stderr with enforced memory/output bounds while the process runs; terminate owned descendants on timeout/overflow, preserve classified failure evidence and release capacity only after confirmed stop.
- [ ] Bind returned evidence to the original provider policy and evaluated source. Reject late results after a substantive source/policy change while preserving valid equivalent evidence; never waive a failed or missing check.
- [ ] Use deterministic stalled/noisy adapter cases and a successful control to demonstrate responsiveness, bounded output and safe restart/cleanup through actual scheduler entry points.

## Planning boundary

Retrospective draft in frozen Phase08; no implementation approval, runtime activation, private-data access, new workers or spending is implied. Address each outcome with meaningful observations; alternate evidence and reasoned criteria amendments are welcome. Preserve substantive findings and avoid process-only author rounds.
