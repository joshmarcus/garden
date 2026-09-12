---
id: CG-587
title: Break the runs and hosts package import cycle
status: cancelled
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/personas.py
- src/garden/scheduler/persona.py
- src/garden/scheduler/retro.py
- src/garden/model.py
- src/garden/runs.py
- src/garden/config.py
discovered_from: CG-531
created: '2026-09-10T15:10:43+00:00'
updated: '2026-09-10T15:34:09+00:00'
file: src/garden/runs.py
error: 'ImportError: cannot import name ''RunStore'' from partially initialized module ''garden.runs'''
---

Restore pytest collection by preventing `garden.runs` importing `garden.hosts.locking` from executing `garden.hosts.__init__`, which imports `drain` and re-imports `RunStore`.

## Provenance

Discovered by CG-531 (Add an ontologist persona for precise and extensible data models) during run `20260910T150651Z-work`.
## Log
- 2026-09-10T15:10:43+00:00 discovered by CG-531

## Duplicate disposition

This finding is preserved as discovery evidence from CG-531. The already-approved CG-585 owns this exact main runs/hosts import cycle, clean-process regression and retained RunStore locking guarantees. Follow CG-585 to its actual accepted merge; do not launch a second implementation or treat this cancellation as proof the failure is fixed.
- 2026-09-10T15:34:09+00:00 Duplicate of CG-585, the already-approved owner of the same main runs/hosts import cycle; original discovery preserved.
