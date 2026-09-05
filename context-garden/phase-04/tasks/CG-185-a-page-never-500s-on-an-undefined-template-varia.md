---
id: CG-185
title: 'A page never 500s on an undefined template variable: tojson gets a value on every path, and a
  template error renders as a flash, not a traceback'
status: done
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
pr: https://github.com/joshmarcus/context-garden/pull/147
attempts: 2
last_dispatched_at: '2026-09-05T13:14:43+00:00'
created: '2026-09-05T10:17:58+00:00'
updated: '2026-09-05T14:01:07+00:00'
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
- 2026-09-05T12:47:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/147 (base main): Made undefined template variables fail loud in a strict Jinja environment used by both tests and production, fixed the sparse dict/state/event access patterns that would have regressed under it, hardened every tojson site with explicit defaults, added a flash-based 500 page with traceback+path logging, and fixed garden serve's uvicorn access log being silenced. cost=$6.29
- 2026-09-05T12:52:48+00:00 automated review requested changes: Under the new StrictUndefined env, the Inbox raises while rendering any pending duplicate/obsolete decision: those items (inbox.py:315-327) never set kind_blurb/evidence/discuss, but inbox.html lines 31-34 read them unguarded for every group=='attention' item, so the page now shows a 500 flash where it used to render — the exact failure this task exists to prevent. The author's own it.get('decision') guard on line 53 shows these items were known; the what-block accesses were missed, and no test renders the Inbox HTML with a pending decision. cost=$1.51
- 2026-09-05T13:00:57+00:00 dispatched revise run 20260905T130057Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~16902 tokens)
- 2026-09-05T13:06:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/147: Fixed the Inbox template's unguarded kind_blurb/evidence/discuss reads on pending duplicate/cancel decisions (the reviewer's blocking finding), guarding them with it.get(...) like the existing it.get('decision') check, and added a test rendering the Inbox with a pending decision under the strict template env. Full suite (607 passed) and ruff pass. cost=$0.83
- 2026-09-05T13:11:26+00:00 automated review: approve — All four acceptance criteria are met and tested: StrictUndefined env for tests+prod, all three tojson sites defaulted, a template-error flash page with traceback+path logging, and the uvicorn access log restored. Prior blocking finding is fixed and covered; full suite (607) and ruff pass. cost=$1.12
- 2026-09-05T13:11:31+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/app.py); a rebase agent will resolve it
- 2026-09-05T13:13:11+00:00 dispatched rebase run 20260905T131311Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~2979 tokens)
- 2026-09-05T13:14:19+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:14:43+00:00 dispatched work run 20260905T131443Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~17056 tokens)
- 2026-09-05T13:16:00+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:01:07+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/147
