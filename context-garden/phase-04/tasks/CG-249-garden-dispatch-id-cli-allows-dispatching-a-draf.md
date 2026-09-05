---
id: CG-249
title: '`garden dispatch <id>` (CLI) allows dispatching a draft directly'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/web/actions/control.py
- src/garden/web/actions/tasks.py
- src/garden/scheduler/human.py
- src/garden/cli/planning.py
- src/garden/cli/state.py
- tests/test_web.py
- tests/test_cli.py
discovered_from: CG-238
created: '2026-09-05T23:28:25+00:00'
updated: '2026-09-05T23:28:25+00:00'
---

cli/loop.py's `dispatch` command permits `mode == "work"` on a task in DRAFT status without `--force`, and never checks brief_gaps -- the same underlying gap CG-238 closed for the web button and `garden take`, just via a different CLI command. Not named in this task's three call sites; consider requiring approval first or running brief_gaps before allowing a draft to dispatch.

## Provenance

Discovered by CG-238 (Every path to ready or to a run goes through the approve gate: Dispatch now on a draft, the new-task form's approve-now, and garden take) during run `20260905T231202Z-work`.

## Log

- 2026-09-05T23:28:25+00:00 discovered by CG-238; deferred by the freeze
