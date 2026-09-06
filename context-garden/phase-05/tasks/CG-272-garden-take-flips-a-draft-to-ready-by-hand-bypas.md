---
id: CG-272
title: garden take flips a draft to ready by hand, bypassing brief_gaps, phase_refusal
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:project-manager:context-garden/phase-04
created: '2026-09-05T23:58:14+00:00'
updated: '2026-09-06T00:50:05+00:00'
---

## Goal

Make take call Scheduler.approve (or refuse a draft) so the one gate covers the manual runner; this was a stated CG-193 follow-up nobody scheduled.

## Context

Raised by the project-manager persona review (brief gate). persona:project-manager:context-garden/phase-04.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-261 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:50:05+00:00 done by CG-238 (merged as PR #192): garden take goes through Scheduler.approve
