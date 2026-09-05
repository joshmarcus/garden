---
id: CG-134
title: 'garden walkthrough: render the live web app''s pages for the retro and the persona reviews'
status: done
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
pr: https://github.com/joshmarcus/context-garden/pull/103
attempts: 1
last_dispatched_at: '2026-09-05T04:08:48+00:00'
created: '2026-09-05T00:37:32+00:00'
updated: '2026-09-05T04:36:56+00:00'
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
- 2026-09-05T04:07:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/103 (base main): Added `garden walkthrough product/phase`, which renders every web page to screenshots, HTML and plain text with an index.md describing each page, and made the phase persona review inline the newest walkthrough. Screenshots use an optional Playwright/Chromium extra and fall back to HTML+text with a note when no browser is present. cost=$3.97
- 2026-09-05T04:08:44+00:00 CI failure
- 2026-09-05T04:08:48+00:00 dispatched revise run 20260905T040848Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~5648 tokens)
- 2026-09-05T04:17:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/103: Fixed the CI F821 failure by merging main (which introduced the in-process runner and removed the wait_for_runs helper) and dropping the obsolete wait_for_runs calls from the walkthrough and retro tests, since dispatch now finishes workers synchronously. ruff and the full test suite pass. cost=$1.86
- 2026-09-05T04:25:58+00:00 automated review: approve — Adds `garden walkthrough` rendering every web page to HTML/text/screenshot with an index.md, and inlines the newest capture into the phase persona brief. All three acceptance criteria met and tested; code, scope, and description are clean. cost=$0.72
- 2026-09-05T04:36:56+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/103
