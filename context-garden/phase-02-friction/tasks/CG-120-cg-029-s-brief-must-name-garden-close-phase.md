---
id: CG-120
title: CG-029's brief must name `garden close-phase`
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/base.html
- src/garden/web/templates/phase.html
- src/garden/store.py
- src/garden/model.py
- src/garden/cli.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
discovered_from: CG-078
created: '2026-09-04T22:59:04+00:00'
updated: '2026-09-04T23:14:00+00:00'
---

CG-078's acceptance criteria include "CG-029's brief names the command", but CG-029 is a scheduler-owned task file in the garden repo, out of reach of a tool-repo worker. Edit CG-029's body so its closing step runs `garden close-phase <product/phase>` (added in CG-078).

## Provenance

Discovered by CG-078 (Closed phases leave the rail and live in a browsable herbarium) during run `20260904T224340Z-work`.

## Log

- 2026-09-04T22:59:04+00:00 discovered by CG-078
- 2026-09-04T23:14:00+00:00 folded into CG-029, which now names garden close-phase
