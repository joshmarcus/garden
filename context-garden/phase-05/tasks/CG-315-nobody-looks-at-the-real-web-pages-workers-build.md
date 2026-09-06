---
id: CG-315
title: 'UI changes are reviewed against rendered pages: a template or style change captures the affected
  pages as screenshots at two widths, the reviewer and the personas read them, and the walkthrough uses
  the same capture'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/walkthrough.py
- src/garden/checks.py
- src/garden/checkrun.py
- src/garden/review.py
- src/garden/scheduler/review.py
- src/garden/web/app.py
- tests/test_web.py
- docs/worker-protocol.md
branch: garden/cg-315-ui-changes-are-reviewed-against-rendered-pages-a
attempts: 1
last_dispatched_at: '2026-09-06T02:47:20+00:00'
created: '2026-09-06T02:10:34+00:00'
updated: '2026-09-06T02:47:20+00:00'
---

## Goal

A change to a template, a stylesheet or a page route is judged on what a person would see. The pre-PR checks render every page the diff touches (and the Inbox, Board, task page and Now pages always) against a seeded fake garden in a headless browser at 1280 and 390 wide, light and dark, and attach the screenshots to the run; the review brief includes them so the reviewer (a model that can read images) checks layout, overlap, wrapping and empty states, and says so per page; the persona phase reviews read the same captures. `garden walkthrough` is built on the same renderer, so the retro's walkthrough and the PR captures are one mechanism.

## Context

Owner's friction, 2026-09-06 02:10Z: "we're not actually looking at the real webpages and observing UI issues, even during review." Evidence from the same night: the Inbox decision card shipped with its text column collapsed to one word per line and the action buttons drawn over the evidence list (CG-312); the task page a notification links to shows no decision card (CG-311); no phase-04 walkthrough was captured, so four personas reviewed pages they never saw. The worker environment has no browser (friction from CG-208, CG-214, CG-224), and the walkthrough renders server-side HTML without layout. The product's setup block owns the dependency (a headless Chromium through Playwright, or an equivalent the setup can install without hand steps); the garden records the captures under the run and links them from the run page.

## Acceptance criteria

- [ ] A check named `ui` runs when the diff touches `src/garden/web/**` or a template: it starts the app against a seeded fake garden (the walkthrough's), captures each affected page and the four core pages at 1280 and 390, light and dark, as PNG under the run directory, and links them on the run page; it does not run for diffs that touch no UI file.
- [ ] The review brief for such a PR embeds the captures (paths the reviewer can Read as images) and the reviewer's verdict names each page it looked at; a review that did not read the captures is a mechanical `request_changes` (the GARDEN_REVIEW block carries `pages_seen`).
- [ ] Persona phase reviews and `garden walkthrough` use the same renderer and the same seeded garden; the phase-05 walkthrough is captured by the retro before the personas run (CG-253 wires the ordering, this task provides the capture).
- [ ] The product setup installs the browser without hand steps and `garden doctor` reports whether it is present; a machine without it degrades to HTML-only capture with a warning, never a silent skip.
- [ ] Tests: a template change triggers the `ui` check and produces the expected files; a non-UI change does not; the review brief builder includes the capture paths.

## Log
- 2026-09-06T02:10:34+00:00 approved (cli)
- 2026-09-06T02:47:20+00:00 dispatched work run 20260906T024657Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19890 tokens)
