---
id: CG-248
title: TUI's dispatch action ('d' key) also bypasses the approve gate on a draft
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/tui/app.py
- src/garden/web/actions/control.py
- src/garden/web/actions/tasks.py
- src/garden/scheduler/human.py
- src/garden/cli/planning.py
- src/garden/cli/state.py
- tests/test_web.py
- tests/test_tui.py
discovered_from: CG-238
created: '2026-09-05T23:28:25+00:00'
updated: '2026-09-06T00:24:04+00:00'
---

## Goal
Add the same status and active-run guard to the TUI's `action_dispatch` that the web "Dispatch now" path already got, so a draft task's placeholder brief cannot be dispatched from the TUI and a second 'd' press cannot double-dispatch.

## Context
`action_dispatch` in `src/garden/tui/app.py` calls `sched.dispatch(t, ...)` directly, with no status check and no active-run guard. A draft task's placeholder brief can be dispatched from the TUI the same way the web "Dispatch now" button used to, and a second press has the same double-dispatch race this task fixed for the web. This path wasn't one of that task's three named paths, so it was left alone; it needs the same treatment (hide/guard, or route through approve) for parity.

## Provenance
Discovered by CG-238 (Every path to ready or to a run goes through the approve gate: Dispatch now on a draft, the new-task form's approve-now, and garden take) during run `20260905T231202Z-work`.

## Acceptance criteria
- [ ] `action_dispatch` refuses to dispatch a task whose status is draft (either blocks the action or routes it through the approve gate first), matching the web guard in `src/garden/web/actions/control.py`.
- [ ] `action_dispatch` checks for an active run on the task before dispatching, so pressing 'd' twice in quick succession cannot start a second run.
- [ ] The 'd' keybinding either hides/disables on a draft task or the guard surfaces a clear message when refused, so the TUI's behavior matches the web page's.
- [ ] `tests/test_tui.py` gains a regression test asserting no dispatch occurs when the task is a draft or already has an active run.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:28:25+00:00 discovered by CG-238; deferred by the freeze
- 2026-09-06T00:18:31+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002114Z-edit) cost=$0.10
- 2026-09-06T00:24:04+00:00 approved (cli)
