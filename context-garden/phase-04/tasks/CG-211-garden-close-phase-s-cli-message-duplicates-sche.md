---
id: CG-211
title: garden close-phase's CLI message duplicates Scheduler.close_phase's refusal text
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading: []
branch: garden/cg-211-garden-close-phase-s-cli-message-duplicates-sche
pr: https://github.com/joshmarcus/context-garden/pull/160
discovered_from: CG-205
attempts: 1
last_dispatched_at: '2026-09-05T14:59:47+00:00'
created: '2026-09-05T13:05:12+00:00'
updated: '2026-09-05T15:10:20+00:00'
---

## Goal\n\n`garden close-phase` (src/garden/cli/scaffold.py) builds its own open-tasks refusal message by hand instead of calling `Scheduler.close_phase`, so its CLI text differs slightly from the message the web `close` action flashes (via `sched.close_phase`, src/garden/scheduler/human.py). Both exit/refuse correctly, but the wording isn't the single shared string the way `approve`/`dispatch` refusals are (via `phase_refusal`).\n\n## Context\n\nFits phase-04's goal 5 (\"one writer per fact\"): CLI should call the scheduler method and print its RuntimeError, not re-implement the check.\n\n## Acceptance criteria\n\n- [ ] `garden close-phase`'s refusal text is produced by `Scheduler.close_phase`, not duplicated in the CLI.\n- [ ] Existing close-phase tests (test_close_phase.py) still pass with matching assertions.

## Provenance

Discovered by CG-205 (CLI first-run and exit codes: new-phase refuses an unregistered product, approve exits non-zero on a refusal, doctor says how to fix a missing git identity) during run `20260905T125137Z-work`.

## Log

- 2026-09-05T13:05:12+00:00 discovered by CG-205
- 2026-09-05T14:59:04+00:00 approved (web)
- 2026-09-05T14:59:47+00:00 dispatched work run 20260905T145938Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4628 tokens)
- 2026-09-05T15:05:37+00:00 opened https://github.com/joshmarcus/context-garden/pull/160 (base main): garden close-phase now calls Scheduler.close_phase and prints its RuntimeError instead of re-implementing the open-tasks check, so CLI and web refusals share the same message text. cost=$0.42
- 2026-09-05T15:07:11+00:00 automated review: approve — CLI close-phase now delegates its refusal check and message to Scheduler.close_phase as intended; tests updated to match and pass, lint clean, diff is minimal and scoped. cost=$0.31
- 2026-09-05T15:08:44+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-05T15:10:20+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/160
