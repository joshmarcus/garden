---
id: CG-590
title: Remove runs and hosts package circular import
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: easy
reading:
- docs/architecture.md
- docs/design.md
- docs/worker-protocol.md
- context-garden/phase-05/goals.md
- context-garden/phase-07/specs/enterprise-remote-environments.md
- context-garden/phase-05/specs/cost-aware-model-routing.md
- src/garden/scheduler/human.py
- src/garden/scheduler/poll.py
discovered_from: CG-526
created: '2026-09-10T15:39:04+00:00'
updated: '2026-09-10T16:02:26+00:00'
file: src/garden/hosts/__init__.py
error: 'ImportError: cannot import name ''RunStore'' from partially initialized module ''garden.runs'''
---

Focused pytest collection fails before tests run because importing `garden.runs` loads `garden.hosts.__init__`, which eagerly imports `drain`, which imports `RunStore` from the still-partially initialized `garden.runs`. Make the hosts package initialization acyclic so ordinary scheduler tests can collect.

## Provenance

Discovered by CG-526 (Complete objective failure-trigger model escalation) during run `20260910T153156Z-work`.
## Log
- 2026-09-10T15:39:04+00:00 discovered by CG-526

## Duplicate disposition

The original discovery is preserved. CG-585 owns this exact import cycle and has already merged as51241517dbccc79a3bd3a69effbcfb1485bd133d, with post-merge main CI34497515251 passing. The discovering task should rebase onto that accepted repair and validate its distinct changes. Do not launch a duplicate implementation or erase the original failed collection evidence.
- 2026-09-10T16:02:26+00:00 Duplicate of completed CG-585 import repair; original discovery preserved and accepted main CI verified.
