---
id: CG-248
title: TUI's dispatch action ('d' key) also bypasses the approve gate on a draft
status: draft
product: context-garden
phase: phase-05
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
updated: '2026-09-06T00:18:31+00:00'
---

src/garden/tui/app.py's `action_dispatch` calls `sched.dispatch(t, ...)` directly with no status check and no active-run guard, so a draft task's placeholder brief can be dispatched from the TUI the same way the web "Dispatch now" button used to, and a second press has the same double-dispatch race this task fixed for the web. Not one of this task's three named paths, so left alone; worth the same treatment (hide/guard, or route through approve) for parity.

## Provenance

Discovered by CG-238 (Every path to ready or to a run goes through the approve gate: Dispatch now on a draft, the new-task form's approve-now, and garden take) during run `20260905T231202Z-work`.

## Log

- 2026-09-05T23:28:25+00:00 discovered by CG-238; deferred by the freeze
- 2026-09-06T00:18:31+00:00 moved from context-garden/phase-04 to context-garden/phase-05
