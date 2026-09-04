---
id: CG-121
title: Planner and friction reports can still create tasks in a closed phase
status: ready
product: context-garden
phase: phase-02-friction
depends_on:
- CG-078
priority: 3
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/base.html
- src/garden/web/templates/phase.html
- src/garden/store.py
- src/garden/model.py
- src/garden/cli.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-121-planner-and-friction-reports-can-still-create-ta
discovered_from: CG-078
last_dispatched_at: '2026-09-04T23:29:32+00:00'
created: '2026-09-04T22:59:04+00:00'
updated: '2026-09-04T23:35:51+00:00'
---

CG-078 guards `new-task` and the scheduler, per the spec. `garden plan`/`import_plan`, the web plan form and friction draft-task creation can still write tasks into a closed phase (the phase page for a closed phase no longer offers the forms, but the CLI paths remain). Decide whether those paths should refuse or implicitly reopen.

## Provenance

Discovered by CG-078 (Closed phases leave the rail and live in a browsable herbarium) during run `20260904T224340Z-work`.

## Log

- 2026-09-04T22:59:04+00:00 discovered by CG-078
- 2026-09-04T23:14:00+00:00 approved
- 2026-09-04T23:14:00+00:00 priority 2 -> 3
- 2026-09-04T23:29:32+00:00 dispatched work run 20260904T232924Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~14952 tokens)
- 2026-09-04T23:35:29+00:00 worker blocked: CG-121 asks to guard garden plan/import_plan and friction draft-task creation the same way CG-078 guards new-task, but CG-078 (Phase.closed, store.set_phase_closed, close-phase/reopen-phase, the new-task guard) is not merged to main yet — its PR #73 is still open — so none of the APIs this task needs to build on exist in the checkout. cost=$2.78
- 2026-09-04T23:35:51+00:00 reset to ready by hand
