---
id: CG-278
title: Task files get optimistic concurrency and a duplicate id is a validate problem, not a fatal exception
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

Store.save records the on-disk updated stamp at load and re-reads on mismatch, re-applying only changed fields (or _transition re-reads before writing); Store.tasks flags the newer of two files with one id and keeps serving; retro-filed drafts get an id that cannot collide with the live counter (a reservation in state.json). Add a test that interleaves an action between a tick's read and save. Staff-engineer highs 1 and 2.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
