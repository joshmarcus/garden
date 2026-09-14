---
id: CG-701
title: Run retrospectives without reopening closed phases
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 3
difficulty: medium
reading:
- context-garden/phase-11/goals.md
- src/garden/scheduler/retro.py
- src/garden/model.py
- tests/test_retro.py
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:11:17+00:00'
---

## Goal

User value: learn from released work while its completion status stays accurate. Why now: this retrospective required temporary reopening. Size: medium. Dependencies: existing phase-owner authorization and CG-684's publication-policy preservation. Permit an authorized retrospective claim on a closed phase, suppress implementation dispatch and retain draft follow-ups in the frozen destination.

## Context

Proposed at the context-garden/phase-10 retro. Reflection should not implicitly authorize another implementation cycle.

## Acceptance criteria

- [ ] Allow an explicitly authorized retrospective on a closed phase while preserving its closure metadata and denying implementation dispatch; reopening implementation remains a separate intentional action.
- [ ] Retain phase-operation authority, maintenance/resource guards, durable duplicate-request prevention and normal report/reconciliation behavior across retries and restarts.
- [ ] Exercise the actual closed-phase start/reconciliation path with a frozen destination and draft follow-ups, coordinating with CG-684's existing policy-preservation work without reopening the phase merely to gather evidence.

## Planning boundary

Frozen Phase11 retrospective draft. No implementation approval, production activation, extra worker capacity, spending or deadline extension is implied. Address every intended outcome substantively; alternate evidence and justified criteria amendments are welcome. Retain material failures and avoid cosmetic or mechanical-rebase rejection rounds.
