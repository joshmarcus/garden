---
id: CG-297
title: The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal
  exit
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading: []
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-05T23:58:19+00:00'
discovered_from: retro:context-garden/phase-04
---

## Goal

Render the text capture with an HTML parser that drops hidden panels and never prints attribute values (a '->' in a title showed as 'tasks">Plan phase'). Separately, a pre-PR check that exits on SIGTERM under machine contention is rerun once before it counts as a failure, and the failure card carries the stack trace.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-286 (renumbered by the operator: two reconcile runs drew ids from one counter)
