---
id: CG-122
title: Extend the flash-message pattern to friction-report and phase/global actions
status: in_review
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
pr: https://github.com/joshmarcus/context-garden/pull/87
discovered_from: CG-086
attempts: 1
last_dispatched_at: '2026-09-04T23:31:10+00:00'
created: '2026-09-04T23:03:17+00:00'
updated: '2026-09-04T23:37:30+00:00'
---

task_action() now flashes scheduler errors instead of 500ing, but /friction-report, /phases/{p}/{ph}/approve-all, /phases/{p}/{ph}/persona, /phases/{p}/{ph}/plan, /pause, /resume and /upgrade still let exceptions propagate to a blank error page. None of them are the reported failure path, but they share the same shape of risk. The flash helper (_flash_url in web/app.py) and the base.html banner already exist and can be reused directly.

## Provenance

Discovered by CG-086 (Web actions report failures as messages, never as a 500) during run `20260904T225523Z-work`.

## Log

- 2026-09-04T23:03:17+00:00 discovered by CG-086
- 2026-09-04T23:14:01+00:00 approved
- 2026-09-04T23:14:01+00:00 priority 2 -> 3
- 2026-09-04T23:31:10+00:00 dispatched work run 20260904T233102Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-086-web-actions-report-failures-as-messages-never-as stacked on CG-086, ~5900 tokens)
- 2026-09-04T23:36:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/87 (base garden/cg-086-web-actions-report-failures-as-messages-never-as): Extended the flash-message pattern from task_action to /friction-report, /phases/{p}/{ph}/approve-all, /persona, /plan, /pause, /resume and /upgrade — each now catches RuntimeError/GitError/GitHubError and generic exceptions and flashes a message via the existing _flash_url helper instead of 500ing. persona and plan also 404 (instead of raising KeyError) on an unknown product/phase. Added tests covering the new flash and 404 paths; full suite (293 tests) and ruff pass. cost=$2.25
- 2026-09-04T23:37:30+00:00 automated review: approve — Faithfully extends the CG-086 flash-message pattern to all seven remaining POST routes with matching three-tier error handling, plus sensible 404s for unknown phases; tests and ruff pass. cost=$0.49
