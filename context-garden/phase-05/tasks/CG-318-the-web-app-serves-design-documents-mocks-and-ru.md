---
id: CG-318
title: 'The web app serves design documents, mocks and run captures: /design/<file> for the product''s
  docs/design and a run page link to each capture'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/pages/runs.py
- src/garden/web/templates/run.html
- src/garden/web/templates/base.html
- src/garden/web/trust.py
- tests/test_web.py
created: '2026-09-06T02:15:43+00:00'
updated: '2026-09-06T02:15:43+00:00'
---

## Goal

Anything a worker renders for a person to look at is one click away in the web app. The product checkout's `docs/design/` is served read-only at `/design/<path>` (HTML mocks render as pages, markdown renders through the existing doc page, images inline), a task page lists the design files its PR adds or changes, and a run page links every capture recorded under the run (screenshots from CG-315's `ui` check, a mock a design task rendered). The nav gets a "Design" entry when the directory exists.

## Context

2026-09-06 02:20Z: the Now 1 design (CG-307) produced a 35 KB document and a static mock rendered from a real snapshot, and the owner could not open them: the operator sent the files through the chat, which the owner's client did not show, and the app has no way to serve a file from the product checkout. The stopgap was a `python -m http.server` on port 8766. With CG-315 adding screenshots to every UI review, the app must be the place to see them.

## Acceptance criteria

- [ ] `GET /design/<path>` serves files under the product checkout's `docs/design/` (and a worktree's, for an open PR, via `?ref=<branch>`), with HTML served as a page in a sandboxed iframe or a plain document, markdown through the doc renderer, and no path escapes (the trust module's path check); a test covers the escape and the three content types.
- [ ] The task page lists design files added or changed by the task's PR with links; the run page links each capture file recorded under the run directory (png, html, md).
- [ ] The nav shows "Design" when the product has a docs/design directory; the walkthrough captures /design once one exists.

## Log
- 2026-09-06T02:15:43+00:00 approved (cli)
