---
id: CG-171
title: garden new-task does not check a frozen phase either
status: draft
product: context-garden
phase: phase-03
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- src/garden/model.py
- src/garden/cli.py
discovered_from: CG-161
created: '2026-09-05T04:21:17+00:00'
updated: '2026-09-05T04:21:17+00:00'
---

`garden new-task` (src/garden/cli.py, ~line 173) checks `ph.closed` but not `ph.frozen`, the same gap CG-161 fixed for `garden plan`/web `plan_phase`. A new manually-created task can materialize as a draft during a freeze. Low risk since the resulting draft still can't be approved without a freeze exception (or none exists to grant, same as planning), but for parity it could be blocked the same way. Out of scope for CG-161, which was scoped explicitly to plan_phase/garden plan.

## Provenance

Discovered by CG-161 (garden plan does not check a frozen phase (only closed)) during run `20260905T041549Z-work`.

## Log

- 2026-09-05T04:21:17+00:00 discovered by CG-161
