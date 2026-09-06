---
id: CG-282
title: The Mark done button on every in-review card sets status to done directly in the
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:user:context-garden/phase-04
created: '2026-09-05T23:58:16+00:00'
updated: '2026-09-06T00:20:01+00:00'
---

## Goal

Send it through a shared Scheduler.mark_done that uses _transition, label it as an escape hatch (e.g. 'Mark done without merging') with a confirm, and drop it from the review card's primary row.

## Context

Raised by the user persona review (Mark done). persona:user:context-garden/phase-04.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-271 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:20:01+00:00 pruned at approval (kickoff q2): subsumed by CG-292 (mark_done through _transition, labelled as an escape hatch with a confirm)
