---
id: CG-342
title: Reconcile Now CLI tests with the page-2 command
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scaffold.py
- src/garden/planner.py
- src/garden/cli/scaffold.py
- .claude/skills/garden-plan/SKILL.md
- .claude/skills/garden-operate/SKILL.md
- examples/garden.work.yaml
- docs/design.md
discovered_from: CG-215
created: '2026-09-06T14:04:52+00:00'
updated: '2026-09-06T14:04:53+00:00'
---

Current main imports `src/garden/cli/now2.py`, whose `garden now` command rejects `--page 1`, while `tests/test_now1.py::test_garden_now_prints_the_four_regions` still expects page 1 to succeed. Align the retained tests and intended CLI compatibility so the full suite passes on main.

## Provenance

Discovered by CG-215 (Onboarding skill and command: analyse an existing project and its environment to create a garden product, principles, setup config and a first phase) during run `20260906T135355Z-revise`.
## Log
- 2026-09-06T14:04:53+00:00 discovered by CG-215
