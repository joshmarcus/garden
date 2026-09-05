---
id: CG-281
title: 'Every status write goes through _transition: Scheduler.mark_done and unapprove, and a source-grep
  test'
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

Web done and unapprove, CLI set-status and take, approve, _approve_retro_blocking, attach_pr and the discovered hold assign task.status directly. Route them through _transition, label the web Mark done as 'Mark done without merging' with a confirm and drop it from the review card's primary row, and add a test like test_queue_state.py that no other module assigns .status. Goal 5 item; user persona high.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
