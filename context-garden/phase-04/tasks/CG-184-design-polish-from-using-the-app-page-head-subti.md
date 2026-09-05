---
id: CG-184
title: 'Design polish from using the app: page-head subtitles wrap too early, and other small layout nits'
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/base.html
- src/garden/web/templates/inbox.html
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
created: '2026-09-05T10:04:27+00:00'
updated: '2026-09-05T10:31:15+00:00'
---

## Goal

Small layout fixes the user noticed while using the web app on 2026-09-05. Each item is one change; keep the herbarium look and the plain copy.

## Items

1. **Page-head subtitles wrap too early.** On the Inbox, "Every item here is a decision only a person can make. Beyond that, the garden grows." breaks onto two lines on a wide screen because `.page-head p` has `max-width:62ch` and the left column is squeezed by the tools on the right. Let the subtitle use the width it has: the left column gets `flex:1; min-width:0`, the paragraph `max-width` rises to about 90ch, and `text-wrap:pretty` avoids a one-word second line. Apply to every page head, not only the Inbox.

(Further items the user reports before this task is taken are appended here, one per line, with the page and what they saw.)

## Acceptance criteria

- [ ] The Inbox subtitle is one line at 1280px and wider; page heads on Board, Trellis, task and run pages get the same rule.
- [ ] No page scrolls horizontally at 1000px; the page head stacks the tools under the title below that width.
- [ ] A test renders the Inbox and checks the page-head paragraph has no fixed 62ch cap.

## Log

- 2026-09-05T10:31:15+00:00 approved (web)
