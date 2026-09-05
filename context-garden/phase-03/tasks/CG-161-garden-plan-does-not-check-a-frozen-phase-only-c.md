---
id: CG-161
title: garden plan does not check a frozen phase (only closed)
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-148
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- src/garden/model.py
- src/garden/cli.py
discovered_from: CG-148
created: '2026-09-05T03:55:13+00:00'
updated: '2026-09-05T03:57:42+00:00'
---

## Goal

`plan_phase` (web) and `garden plan` only refuse a closed phase; a frozen phase still accepts new planner-created drafts. Drafts still can't be approved without a freeze exception, so this is low-risk, but for full parity with the freeze's intent (no new work materializing during a freeze) planning could also be blocked, or explicitly documented as allowed.

## Context

Noticed while implementing CG-148; left out to keep that task's scope to approve/dispatch/discovered-work as specified in its acceptance criteria.

## Provenance

Discovered by CG-148 (A frozen or closed phase refuses approvals and dispatch; a freeze is a phase state, not a note) during run `20260905T033732Z-work`.

## Log

- 2026-09-05T03:55:13+00:00 discovered by CG-148
- 2026-09-05T03:57:42+00:00 approved (web)
