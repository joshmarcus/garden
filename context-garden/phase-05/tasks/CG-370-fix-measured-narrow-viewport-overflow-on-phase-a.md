---
id: CG-370
title: Fix measured narrow-viewport overflow on Phase and Runs pages
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-370-fix-measured-narrow-viewport-overflow-on-phase-a
pr: https://github.com/joshmarcus/context-garden/pull/267
attempts: 1
last_dispatched_at: '2026-09-07T05:33:58+00:00'
created: '2026-09-07T04:57:52+00:00'
updated: '2026-09-07T06:20:16+00:00'
---

## Goal

Remove unintended horizontal overflow on Phase and Runs at390 CSS pixels while retaining readable, usable content.

## Evidence

Real bounded Chromium capture against CG326 head1b4c4c9 measured Phase clientWidth390/scrollWidth898 and Runs390/646, both light/dark. Other narrow pages measured390/390. Evidence: /home/joshua/work/operator-test-tmp/cg326-effective-runtime-20260907T0455/stdout.log and source-head.txt. Browser successfully generated50PNG artifacts; missing page narrow images reflect fail-closed viewport assertions, not missing browser libraries. CG326 owns Now2 frame-load/capture mechanics. Verify on currentmain before changing; distinguish pre-existing layout bugs from harness behavior.

## Acceptance criteria

- [ ] Reproduce Phase/ Runs overflow in a disposable served current-main garden at390px; identify actual overflowing elements. If already fixed, record exact correcting commit and fresh evidence instead of duplicating work.
- [ ] Fix unintended document-level overflow in both themes without hiding required data or controls; long identifiers/tables remain navigable and usable. Preserve desktop behavior and intentional internal scroll regions.
- [ ] Real browser verifies document clientWidth/scrollWidth and relevant control behavior, retains current-head light/dark390px screenshots plus desktop smoke evidence. Do not weaken or skip capture assertions.
- [ ] Focused checks bounded/serial and exact-head GitHubCI; internal self-review and fixes. No production edits/fault injection.

## Log
## Goal

One or two sentences.

## Context

What the agent needs to know that is not in the reading list.

## Acceptance criteria

- [ ] ...

## Out of scope

- ...
- 2026-09-07T05:33:58+00:00 dispatched work run 20260907T053326Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9132 tokens)
- 2026-09-07T05:58:00+00:00 preserved uncommitted worktree changes from run 20260907T053326Z-work outside the PR: `git stash apply 126ea87e35557cdab216057b53d7536c582d5987` in /home/joshua/work/worktrees/CG-370 (garden:CG-370:20260907T053326Z-work:reap)
- 2026-09-07T06:01:08+00:00 opened https://github.com/joshmarcus/context-garden/pull/267 (base main): Phase and Runs no longer widen the document at 390px; their intentionally wide tables remain usable through their existing internal horizontal scroll areas. The final commit 5057cba passed exact-head GitHub CI. cost=$2.83
- 2026-09-07T06:05:08+00:00 description rewritten by the reviewer cost=$0.79
- 2026-09-07T06:11:49+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T06:18:39+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T06:20:16+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/267
