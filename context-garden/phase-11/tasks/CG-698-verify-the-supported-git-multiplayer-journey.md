---
id: CG-698
title: Verify the supported Git multiplayer journey
status: draft
product: context-garden
phase: phase-11
depends_on:
- CG-695
priority: 2
difficulty: hard
reading:
- context-garden/phase-11/goals.md
- tests/test_multiplayer_workflow.py
- tests/test_git_coordination.py
- src/garden/migration.py
- src/garden/multiplayer_client.py
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:11:17+00:00'
---

## Goal

User value: confidence that normal migration, startup and two independent schedulers work together. Why now: CG-640's headline journeys still inject HTTP/SQLite authority. Size: hard. Dependencies: Git migration repair and delivered CG-631 through CG-640. Use independent roots and a disposable bare remote through supported configuration and scheduler entry points, covering contention, restart, partition, late results, acknowledged handoff and phase closure.

## Context

Proposed at the context-garden/phase-10 retro. A bounded integrated journey connects strong protocol tests to the product users actually start.

## Acceptance criteria

- [ ] Exercise two independent local installations and a disposable Git remote through supported configuration and actual scheduler entry points, covering startup/ownership, contention, acknowledged handoff, recovery and phase operations.
- [ ] Demonstrate both rejection during unresolved or stale authority and successful progress after legitimate resolution without injecting the obsolete coordinator or weakening production permission guards.
- [ ] Label retained HTTP/SQLite tests as legacy compatibility evidence and distinguish source-level checks from the supported Git acceptance journey; reuse existing boundary tests instead of duplicating their assertions.

## Planning boundary

Frozen Phase11 retrospective draft. No implementation approval, production activation, extra worker capacity, spending or deadline extension is implied. Address every intended outcome substantively; alternate evidence and justified criteria amendments are welcome. Retain material failures and avoid cosmetic or mechanical-rebase rejection rounds.
