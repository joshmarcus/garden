---
id: CG-134
title: 'garden walkthrough: render the live web app''s pages for the retro and the persona reviews'
status: running
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: medium
reading:
- src/garden/cli.py
- src/garden/web/app.py
- personas/designer.md
branch: garden/cg-134-garden-walkthrough-render-the-live-web-app-s-pag
attempts: 1
last_dispatched_at: '2026-09-05T03:57:23+00:00'
created: '2026-09-05T00:37:32+00:00'
updated: '2026-09-05T03:57:23+00:00'
---

## Goal

`garden walkthrough product/phase` renders the live garden's web pages, in the order a person uses them, to screenshots and HTML under `<phase>/docs/walkthrough/<date>/` with an `index.md` that says what each page is for and what to look at, so a persona review can judge the real UI and a person can follow it as a QA script.

## Context

Asked at the freeze of the first live run. Persona reviews read code, PR bodies and task files and never see a page; the designer, usability-expert and user personas need the rendered app. Pages: Inbox, Board (columns and list), Trellis, a task page with runs and the live log, a run page (transcript, brief, final message), the phase page, the Herbarium and a closed phase's header, Config, Trials, Events. Use Playwright's Chromium (present in the cache on the home machine; a work machine may need `playwright install chromium`) with a fallback to HTML-only when no browser is available. The index lists each page with its purpose, one line on what to look at, and the screenshot. The persona review brief adds the newest walkthrough directory to its reading when one exists. Keep the copy plain; the herbarium look is the app's, not the walkthrough's.

## Acceptance criteria

- [ ] the command writes screenshots (or HTML only, with a note) and `index.md` for every page above against a running or test-client app.
- [ ] `garden persona-review product/phase` includes the newest walkthrough in the brief when present; a test checks the brief.
- [ ] README documents the command and the browser requirement.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T00:40:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03; done by hand for this retro
- 2026-09-05T03:01:10+00:00 approved (web)
- 2026-09-05T03:05:55+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:57+00:00 approved (web)
- 2026-09-05T03:57:23+00:00 dispatched work run 20260905T035715Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4389 tokens)
