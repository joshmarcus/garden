---
id: CG-288
title: Cancel obsolete review runs when tasks finish
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:15:10+00:00'
---

## Goal

Terminate the review process tree when its task becomes terminal or the reviewed head is superseded, preserve the run outcome and spend, and release the active pointer once. An orphan sweep after the model finishes does not meet the original cancellation goal. Coordinate with existing CG-236 rather than duplicating review dispatch work.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
