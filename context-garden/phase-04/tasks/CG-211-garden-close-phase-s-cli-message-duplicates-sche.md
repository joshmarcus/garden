---
id: CG-211
title: garden close-phase's CLI message duplicates Scheduler.close_phase's refusal text
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading: []
discovered_from: CG-205
created: '2026-09-05T13:05:12+00:00'
updated: '2026-09-05T13:05:12+00:00'
---

## Goal\n\n`garden close-phase` (src/garden/cli/scaffold.py) builds its own open-tasks refusal message by hand instead of calling `Scheduler.close_phase`, so its CLI text differs slightly from the message the web `close` action flashes (via `sched.close_phase`, src/garden/scheduler/human.py). Both exit/refuse correctly, but the wording isn't the single shared string the way `approve`/`dispatch` refusals are (via `phase_refusal`).\n\n## Context\n\nFits phase-04's goal 5 (\"one writer per fact\"): CLI should call the scheduler method and print its RuntimeError, not re-implement the check.\n\n## Acceptance criteria\n\n- [ ] `garden close-phase`'s refusal text is produced by `Scheduler.close_phase`, not duplicated in the CLI.\n- [ ] Existing close-phase tests (test_close_phase.py) still pass with matching assertions.

## Provenance

Discovered by CG-205 (CLI first-run and exit codes: new-phase refuses an unregistered product, approve exits non-zero on a refusal, doctor says how to fix a missing git identity) during run `20260905T125137Z-work`.

## Log

- 2026-09-05T13:05:12+00:00 discovered by CG-205
