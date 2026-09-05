---
id: CG-209
title: Brief gate for blocking discovered tasks
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-193
priority: 2
difficulty: easy
reading: []
discovered_from: CG-193
created: '2026-09-05T12:46:14+00:00'
updated: '2026-09-05T12:50:55+00:00'
---

## Goal

Blocking discovered tasks (`discovered.auto_approve_blocking`) are created straight to `ready` in `scheduler/discovered.py`, bypassing the `approve` gate and so the CG-193 brief_gaps check. Decide whether an auto-approved discovered task with placeholder criteria or an unresolved reading path should be held as a draft (or flagged) rather than dispatched.

## Context

CG-193 put the placeholder/reading check in `approve`; this is the one ready-transition that does not pass through it.

## Provenance

Discovered by CG-193 (Approve refuses placeholder acceptance criteria and unresolved reading-list paths) during run `20260905T123408Z-work`.

## Log

- 2026-09-05T12:46:14+00:00 discovered by CG-193
- 2026-09-05T12:50:55+00:00 approved (web)
