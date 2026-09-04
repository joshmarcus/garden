---
id: CG-110
title: CG-107 duplicates CG-092
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/runner/local.py
- src/garden/runner/ssh.py
- src/garden/brief.py
- src/garden/config.py
- examples/garden.work.yaml
discovered_from: CG-092
created: '2026-09-04T21:26:44+00:00'
updated: '2026-09-04T21:29:27+00:00'
---

The garden repo has task CG-107 ('Driving garden config should adopt the setup block for context-garden'), discovered_from CG-081 on a later revise run, describing the same change CG-092 asked for. Once CG-092's change is confirmed merged/applied, CG-107 should probably be closed as a duplicate to avoid a second worker redoing this.

## Provenance

Discovered by CG-092 (Remove venv install lines from the context-garden garden config and product overview) during run `20260904T212102Z-resume`.

## Log

- 2026-09-04T21:26:44+00:00 discovered by CG-092
- 2026-09-04T21:29:27+00:00 handled: CG-107 was cancelled as a duplicate of CG-092 at 21:25; this note-task has nothing left to do
