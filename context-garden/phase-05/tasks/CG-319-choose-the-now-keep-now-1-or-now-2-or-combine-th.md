---
id: CG-319
title: Keep Now 1 as Now, retire Now 2, and place Now after Inbox
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-308
- CG-309
priority: 0
order: 2
difficulty: hard
reading:
- context-garden/phase-05/specs/now-page.md
- src/garden/web/app.py
- src/garden/web/templates/base.html
- tests/test_web.py
branch: garden/cg-319-keep-now-1-as-now-retire-now-2-and-place-now-aft
pr: https://github.com/joshmarcus/context-garden/pull/305
attempts: 1
last_dispatched_at: '2026-09-08T12:14:49+00:00'
created: '2026-09-06T02:40:45+00:00'
updated: '2026-09-08T12:19:51+00:00'
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
- 2026-09-08T10:48:21+00:00 priority 2 -> 0 (web)
- 2026-09-08T10:48:25+00:00 difficulty medium -> hard (web)
- 2026-09-08T11:20:00+00:00 dispatched work run 20260908T111955Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~14756 tokens)
- 2026-09-08T11:48:11+00:00 preserved uncommitted worktree changes from run 20260908T111955Z-work outside the PR: `git stash apply 3a22a35127c9a369c7dcc6a3745261d968fffa24` in /home/joshua/work/worktrees/CG-319 (garden:CG-319:20260908T111955Z-work:reap)
- 2026-09-08T11:50:12+00:00 opened https://github.com/joshmarcus/context-garden/pull/305 (base main): The retained Now 1 experience is now the single canonical `/now` page, placed immediately after Inbox, while `/now1` and `/now2` permanently redirect to it. The executable Now 2 implementation was removed, documentation and walkthrough targets were updated, responsive evidence was captured, and exact-head CI passed. cost=$7.66
- 2026-09-08T12:13:57+00:00 automated review requested changes: The application correctly consolidates Now at `/now`, but the retained design mock and its template still present the retired two-page navigation. Update and regenerate those applicable design artifacts before merge. cost=$1.38
- 2026-09-08T12:14:49+00:00 dispatched revise run 20260908T121447Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16095 tokens)
- 2026-09-08T12:19:51+00:00 marked done without merging (web)
