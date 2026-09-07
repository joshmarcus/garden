---
id: CG-370
title: Fix measured narrow-viewport overflow on Phase and Runs pages
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-07T04:57:52+00:00'
updated: '2026-09-07T04:58:19+00:00'
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
