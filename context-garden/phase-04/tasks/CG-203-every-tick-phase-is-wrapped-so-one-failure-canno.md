---
id: CG-203
title: Every tick phase is wrapped so one failure cannot skip the rest, state is saved on error, and deferred
  reviews are deduplicated
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading: []
branch: garden/cg-203-every-tick-phase-is-wrapped-so-one-failure-canno
pr: https://github.com/joshmarcus/context-garden/pull/151
attempts: 1
last_dispatched_at: '2026-09-05T12:50:14+00:00'
created: '2026-09-05T10:30:01+00:00'
updated: '2026-09-05T13:00:30+00:00'
---

## Goal

`dispatch_edits` and `dispatch_ready` are the only tick phases not wrapped in try/except, and `state.save()` is not reached when a phase raises, so a transition made earlier in the tick can be lost. Deferred review batches are appended without de-duplication; a CG-177 test asserts two pending entries for one task.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (staff-engineer:medium, staff-engineer:low); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] Each tick phase runs under the same guard; an exception is logged with the phase name and the tick continues; state is saved in a `finally`.
- [ ] Deferred reviews are keyed by task; the CG-177 test asserts one entry.
- [ ] A test raises in dispatch and sees the earlier transition persisted.

## Log

- 2026-09-05T10:31:19+00:00 approved (web)
- 2026-09-05T12:50:14+00:00 dispatched work run 20260905T125005Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4411 tokens)
- 2026-09-05T13:00:30+00:00 opened https://github.com/joshmarcus/context-garden/pull/151 (base main): Wrapped dispatch_edits/dispatch_ready in the same tick-phase guard as the rest of the loop, moved state.save() into a finally so an earlier phase's state isn't lost on a later exception, and deduplicated deferred review batches by (kind, name); updated the CG-177 test and added two new tests. cost=$1.36
