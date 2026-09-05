---
id: CG-240
title: 'Complete CG-238: enforce approval and single-run admission'
status: cancelled
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The phase explicitly promises that incomplete briefs never consume runs, yet
  demonstrated UI and CLI paths bypass the gate and can launch competing workers.
retro_blocking: true
created: '2026-09-05T23:15:09+00:00'
updated: '2026-09-05T23:57:12+00:00'
---

## Goal

Reuse existing draft CG-238; do not create a replacement. Route Dispatch now on drafts, new-task approve-now and garden take through the shared approval and phase gate; create drafts first and retain them with actionable feedback on refusal. Atomically reject dispatch while a worker is active, including repeated or concurrent button presses, and return the dispatched run ID on success. Verify every route with placeholder criteria, unresolved paths, frozen phases and concurrent dispatch attempts.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The phase explicitly promises that incomplete briefs never consume runs, yet demonstrated UI and CLI paths bypass the gate and can launch competing workers.

## Log

- 2026-09-05T23:15:09+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:57:12+00:00 cancelled by the joined retro (2026-09-05 23:55Z): duplicate of CG-238, which is already merged or in review
