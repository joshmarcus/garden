---
id: CG-281
title: Dispatch now on a draft and the New task form's approve-now both skip the approv
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-05T23:58:16+00:00'
updated: '2026-09-05T23:58:16+00:00'
discovered_from: persona:user:context-garden/phase-04
---

## Goal

Route the dispatch web action for a draft and the form's ready status through Scheduler.approve (brief_gaps), and hide Dispatch now on a draft whose card shows a gap; close garden take the same way.

## Context

Raised by the user persona review (brief gate). persona:user:context-garden/phase-04.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-270 (renumbered by the operator: two reconcile runs drew ids from one counter)
