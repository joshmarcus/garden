---
id: CG-122
title: Extend the flash-message pattern to friction-report and phase/global actions
status: running
product: context-garden
phase: phase-02-friction
depends_on:
- CG-086
priority: 3
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/task.html
branch: garden/cg-122-extend-the-flash-message-pattern-to-friction-rep
discovered_from: CG-086
attempts: 1
last_dispatched_at: '2026-09-04T23:31:10+00:00'
created: '2026-09-04T23:03:17+00:00'
updated: '2026-09-04T23:31:10+00:00'
---

task_action() now flashes scheduler errors instead of 500ing, but /friction-report, /phases/{p}/{ph}/approve-all, /phases/{p}/{ph}/persona, /phases/{p}/{ph}/plan, /pause, /resume and /upgrade still let exceptions propagate to a blank error page. None of them are the reported failure path, but they share the same shape of risk. The flash helper (_flash_url in web/app.py) and the base.html banner already exist and can be reused directly.

## Provenance

Discovered by CG-086 (Web actions report failures as messages, never as a 500) during run `20260904T225523Z-work`.

## Log

- 2026-09-04T23:03:17+00:00 discovered by CG-086
- 2026-09-04T23:14:01+00:00 approved
- 2026-09-04T23:14:01+00:00 priority 2 -> 3
- 2026-09-04T23:31:10+00:00 dispatched work run 20260904T233102Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-086-web-actions-report-failures-as-messages-never-as stacked on CG-086, ~5900 tokens)
