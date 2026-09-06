---
id: CG-292
title: 'Every status write goes through _transition: Scheduler.mark_done and unapprove, and a source-grep
  test'
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-05T23:58:18+00:00'
discovered_from: retro:context-garden/phase-04
---

## Goal

Web done and unapprove, CLI set-status and take, approve, _approve_retro_blocking, attach_pr and the discovered hold assign task.status directly. Route them through _transition, label the web Mark done as 'Mark done without merging' with a confirm and drop it from the review card's primary row, and add a test like test_queue_state.py that no other module assigns .status. Goal 5 item; user persona high.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

Folded in from CG-247 and CG-282 (cancelled as duplicates): the web Mark done on an in-review card is the escape hatch, labelled 'Mark done without merging' with a confirm and dropped from the card's primary row; a PR-backed task reports done only when its commits are on the base branch (CG-228's rule), so mark_done refuses otherwise unless forced.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-281 (renumbered by the operator: two reconcile runs drew ids from one counter)
