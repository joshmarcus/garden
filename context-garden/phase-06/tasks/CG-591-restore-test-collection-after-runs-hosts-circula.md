---
id: CG-591
title: Restore test collection after runs-hosts circular import
status: cancelled
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/inbox.py
- src/garden/web/pages/inbox.py
- src/garden/web/pages/task.py
- src/garden/scheduler/human.py
discovered_from: CG-540
created: '2026-09-10T15:46:42+00:00'
updated: '2026-09-10T16:02:27+00:00'
file: src/garden/hosts/__init__.py
error: 'ImportError: cannot import name RunStore from partially initialized module garden.runs'
---

Break the circular import that prevents pytest collection: `garden.runs` imports `garden.hosts.locking`, package initialization imports `hosts.drain`, and `hosts.drain` imports `RunStore` from the partially initialized `garden.runs` module.

## Provenance

Discovered by CG-540 (Reconcile deferred notices and attention ownership) during run `20260910T153920Z-work`.
## Log
- 2026-09-10T15:46:42+00:00 discovered by CG-540

## Duplicate disposition

The original discovery is preserved. CG-585 owns this exact import cycle and has already merged as51241517dbccc79a3bd3a69effbcfb1485bd133d, with post-merge main CI34497515251 passing. The discovering task should rebase onto that accepted repair and validate its distinct changes. Do not launch a duplicate implementation or erase the original failed collection evidence.
- 2026-09-10T16:02:27+00:00 Duplicate of completed CG-585 import repair; original discovery preserved and accepted main CI verified.
