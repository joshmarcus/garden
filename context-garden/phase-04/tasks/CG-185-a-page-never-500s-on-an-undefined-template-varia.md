---
id: CG-185
title: 'A page never 500s on an undefined template variable: tojson gets a value on every path, and a
  template error renders as a flash, not a traceback'
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/inbox.html
- src/garden/web/templates/task.html
- src/garden/web/templates/trials.html
- src/garden/web/trust.py
branch: garden/cg-185-a-page-never-500s-on-an-undefined-template-varia
attempts: 1
last_dispatched_at: '2026-09-05T12:17:19+00:00'
created: '2026-09-05T10:17:58+00:00'
updated: '2026-09-05T12:17:19+00:00'
---

## Goal

No page returns a 500 because a template serialised a variable that was not in its context. Every `tojson` use has a value on every render path, the Jinja environment is strict about undefined names in tests, and if a template still raises at runtime the user sees the flash-message error the app already has for actions, with the traceback in the log.

## Context

At 10:12:19 on 2026-09-05 the web UI returned "Internal Server Error" to the user; the journal shows `TypeError: Object of type Undefined is not JSON serializable` raised from a template render (through `web/trust.py`'s origin middleware). The three `tojson` uses are `trials.html` (`harnesses`), `task.html` (the trial form's `data-harnesses`) and `inbox.html` (`phases_by_product`, added by CG-157); the request path was not captured because the access log is not in the journal. The page rendered normally a minute later, so the missing value depends on state (a task with no harness list, or an inbox render path that skips the friction form's context).

## Acceptance criteria

- [ ] The template environment used by tests runs with `undefined=StrictUndefined`, and every page in the walkthrough renders under it with representative data (a task without trials, an inbox with no products, an empty trials page).
- [ ] Each `tojson` site gets its value from the page's context on every path, with an explicit empty default.
- [ ] A template exception at runtime renders the error as a flash on a 500 page that keeps the header and navigation, and logs the traceback with the request path.
- [ ] Uvicorn's access log reaches the journal (or the serve log) so the next 500 can be tied to its request.

## Log

- 2026-09-05T10:31:15+00:00 approved (web)
- 2026-09-05T12:17:19+00:00 dispatched work run 20260905T121711Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~15626 tokens)
