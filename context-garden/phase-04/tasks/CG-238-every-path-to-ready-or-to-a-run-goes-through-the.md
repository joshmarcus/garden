---
id: CG-238
title: 'Every path to ready or to a run goes through the approve gate: Dispatch now on a draft, the new-task
  form''s approve-now, and garden take'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The definition of done says no task is dispatched with placeholder criteria,
  and three personas showed it is false in the shipped build; the gate is this phase's goal 2.
retro_blocking: true
created: '2026-09-05T23:05:55+00:00'
updated: '2026-09-05T23:05:55+00:00'
---

## Goal

Dispatch now on a draft dispatches a placeholder brief silently and a second press orphans the first run; the phase page's New task form with approve-now writes status ready directly; garden take flips a draft to ready by hand. Route all three through Scheduler.approve so brief_gaps and phase_refusal apply, hide Dispatch now on a draft, refuse dispatch when a run is in flight, flash the dispatched run id, and on a form refusal keep the task a draft and flash the gap with the file path. Tests for each path.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The definition of done says no task is dispatched with placeholder criteria, and three personas showed it is false in the shipped build; the gate is this phase's goal 2.

## Log

- 2026-09-05T23:05:55+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
