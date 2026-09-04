---
id: CG-010
title: Notification hook for human-needed transitions
status: awaiting_triage
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
estimate: M
difficulty: easy
reading:
- context-garden/phase-02-friction/specs/notifications.md
branch: garden/cg-010-notification-hook-for-human-needed-transitions
pr: https://github.com/joshmarcus/context-garden/pull/17
attempts: 2
last_dispatched_at: '2026-09-04T17:40:46+00:00'
created: '2026-09-04T00:00:00+00:00'
updated: '2026-09-04T17:45:02+00:00'
---

## Goal

Run `notify.command` when a task needs a person: it reaches `awaiting_triage` or `waiting_human`, fails, is flagged `needs_human` (a stall or the revision cap), or its phase hits its budget.

## Context

Transitions go through `Scheduler._transition` and every other human-needed moment is an event (`events.HUMAN_KINDS`, emitted through `EventLog.emit`); hook both chokepoints, guarded by a `notify:` block in config, with a short timeout, and never raising into the tick. The Inbox and the Timeline already show these moments in the UI, so this task is only the outbound hook. Document the config in README and garden.yaml comments.

## Acceptance criteria

- [ ] Hook receives GARDEN_TASK_ID, GARDEN_STATUS, GARDEN_MESSAGE, GARDEN_PR.
- [ ] Test with a command that writes to a file.
- [ ] `garden doctor` reports whether a notify command is configured, and `garden.yaml` documents the block.

## Out of scope

- Per-channel integrations.

## Log

- 2026-09-04T17:23:48+00:00 approved (web)
- 2026-09-04T17:24:44+00:00 dispatched work run 20260904T172443Z-work via local [claude model=haiku] (fresh session, base main, ~2180 tokens)
- 2026-09-04T17:29:27+00:00 attempt 1 failed: worker exited 1: worker error: error_max_turns; will retry
- 2026-09-04T17:30:40+00:00 dispatched work run 20260904T173040Z-work via local [claude model=haiku] (fresh session, base main, ~2242 tokens)
- 2026-09-04T17:35:40+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/17 (base main): Notification hook implemented for human-needed task transitions. The hook runs a configured shell command (notify.command) when a task reaches awaiting_triage, waiting_human, failed, changes_requested, or stalled states, passing GARDEN_TASK_ID, GARDEN_STATUS, GARDEN_MESSAGE, and GARDEN_PR as environment variables. Fully tested and documented in garden.yaml. cost=$0.51
- 2026-09-04T17:39:15+00:00 automated review requested changes: should_notify fires on all changes_requested transitions including those the scheduler handles automatically (auto-revise, pre-PR check revise, rebase revise), causing false-positive notifications on every normal review cycle; only human-needed changes_requested transitions (stall, revision cap, auto_revise off) should trigger the hook. cost=$0.42
- 2026-09-04T17:40:46+00:00 dispatched revise run 20260904T174046Z-revise via local [claude model=sonnet] (fresh session, base main, ~2688 tokens)
- 2026-09-04T17:45:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/17: Fixed spurious notifications on auto-handled changes_requested transitions. `should_notify` now takes `needs_human: bool` instead of `previous_status`; only the two human-required sites (auto_revise=False and revision cap) and stall transitions pass `needs_human=True`. A new test confirms no notification fires during a normal auto-revise cycle. cost=$0.66
