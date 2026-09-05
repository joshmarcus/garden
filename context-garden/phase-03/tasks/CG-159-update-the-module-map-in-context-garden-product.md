---
id: CG-159
title: Update the module map in context-garden/product.md for the scheduler and web packages
status: cancelled
product: context-garden
phase: phase-03
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- tests/test_scheduler.py
- tests/fake_claude.py
- docs/architecture.md
discovered_from: CG-137
created: '2026-09-05T03:36:08+00:00'
updated: '2026-09-05T03:44:11+00:00'
---

## Goal

CG-137 split `src/garden/scheduler.py` into the package `src/garden/scheduler/` (one mixin per tick phase) and `src/garden/web/app.py` into `web/app.py`, `web/common.py`, `web/pages/` and `web/actions/`. The layout list in `context-garden/product.md` still names `scheduler.py` and `web/app.py`. Update it to match the module map in `docs/architecture.md` of the context-garden repo.

## Context

The product overview lives in the driving garden (joshmarcus/garden), so a product worktree cannot edit it.

## Provenance

Discovered by CG-137 (Split the scheduler by tick phase and the web actions into a registry so features stop colliding) during run `20260905T032209Z-work`.

## Log

- 2026-09-05T03:36:08+00:00 discovered by CG-137
- 2026-09-05T03:44:11+00:00 done by hand in the garden repo: context-garden/product.md layout now names scheduler/, web/pages, web/actions and tests/scheduler (a product worktree cannot edit this file)
