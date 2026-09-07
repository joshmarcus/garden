---
id: CG-319
title: Keep Now 1 as Now, retire Now 2, and place Now after Inbox
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-308
- CG-309
priority: 2
order: 2
difficulty: medium
reading:
- context-garden/phase-05/specs/now-page.md
- src/garden/web/app.py
- src/garden/web/templates/base.html
- tests/test_web.py
created: '2026-09-06T02:40:45+00:00'
updated: '2026-09-07T15:52:11+00:00'
---

## Goal

Keep the existing Now 1 design as the single Now page at `/now`. Drop Now 2 entirely as an application implementation; do not combine its design into the retained page. Rename visible Now 1 labels to Now and place Now immediately after Inbox in the top navigation bar.

## Context

Explicit owner decision on2026-09-07 supersedes the previous operator-proposed combination and the requirement for a side-by-side selection study. The design choice is settled: retain Now 1. Owner explicitly moved this task into phase05 and authorized implementation on2026-09-07. Other phase06 holds and current resource containment remain unchanged.

## Acceptance criteria

- [ ] `/now` serves the existing Now 1 design and interactions under the visible name Now. No user-facing navigation, heading or selector labels it Now 1 or offers Now 2.
- [ ] The top navigation order places Now immediately after Inbox. Any other navigation consistently links to the one canonical `/now` page without duplicate variants.
- [ ] Retire the Now 2 application templates, exclusive helpers and serving implementation. Redirect legacy `/now1` and `/now2` bookmarks to `/now`; redirects do not retain a second page implementation. Preserve shared production metrics, necessary coverage and historical incident/review evidence rather than deleting them solely because filenames mention a variant.
- [ ] Update applicable design documentation, walkthrough/capture targets, links and tests for the retained Now page and legacy redirects. Verify the actual Inbox -> Now navigation, core Now 1 interactions and responsive behavior in the running app; focused checks and exact-head CI pass without unrelated redesign.

## Log

- 2026-09-06T13:20:32+00:00 approved (cli)
- 2026-09-06T13:45:05+00:00 Owner-directed feature deferral until phase-05 stabilization is demonstrated. Preserve existing branch and PR; no further implementation or merge before the gate passes.
- 2026-09-06T13:45:07+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-07T02:16:25+00:00 Owner chose Now1 exclusively: remove Now2, rename Now1 to Now, and place it after Inbox in the top navigation. Replaces prior operator combination decision. Remains phase06 draft under freeze.
- 2026-09-07T15:52:11+00:00 moved from context-garden/phase-06 to context-garden/phase-05
- 2026-09-07T15:52:11+00:00 Owner explicitly requested phase05 promotion and unfreeze; implement the settled Now1-only design.
- 2026-09-07T15:52:11+00:00 approved (owner-phase05-promotion)
