---
id: CG-227
title: garden retro's own persona-phase and reconcile dispatch aren't gated on a paused harness
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-212
priority: 1
difficulty: easy
reading:
- src/garden/harness.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/budget.py
- src/garden/inbox.py
- context-garden/phase-02-friction/tasks/CG-033-an-environment-error-in-a-worker-pauses-dispatch.md
branch: garden/cg-227-garden-retro-s-own-persona-phase-and-reconcile-d
pr: https://github.com/joshmarcus/context-garden/pull/183
discovered_from: CG-212
attempts: 1
last_dispatched_at: '2026-09-05T19:30:39+00:00'
created: '2026-09-05T17:49:54+00:00'
updated: '2026-09-05T19:43:34+00:00'
---

## Goal

`start_retro`'s loop over missing personas (`dispatch_persona_phase`, which now goes through the gated `dispatch_aux`) and `_dispatch_retro_run` (used by `_dispatch_reconcile`, which dispatches its own run directly via `runner_for`/`runner.start`, not through `dispatch_aux`) can still start a run against a harness that is currently paused, or fail to recognise a quota `env_error` if one hits mid-retro. `dispatch_persona_phase` will now raise if paused (an improvement from this round), but the reconcile dispatch has neither the gate nor env_error handling.

## Context

Out of scope for CG-212's reviewer feedback (which named trial contenders, automated review, and persona/compare aux runs specifically); retro is a rarer, human-triggered flow so the risk is lower, but the same account-limit trouble could still strand a retro mid-flight without pausing the harness for other dispatch.

## Acceptance criteria

- [ ] `_dispatch_retro_run` refuses (or the retro flow otherwise handles) a paused harness before dispatching.
- [ ] `reap_retro`'s reconcile-collection path recognises `env_error` and pauses the harness instead of treating it as a failed retro.

## Provenance

Discovered by CG-212 (A usage or spend-limit error from a harness pauses dispatch for that harness and leaves the task ready, instead of burning attempts and failing tasks) during run `20260905T172529Z-revise`.

## Log

- 2026-09-05T17:49:54+00:00 discovered by CG-212
- 2026-09-05T19:16:28+00:00 approved (web)
- 2026-09-05T19:30:39+00:00 dispatched work run 20260905T193023Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus stacked on CG-212, ~18448 tokens)
- 2026-09-05T19:43:34+00:00 opened https://github.com/joshmarcus/context-garden/pull/183 (base garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus): Gated the retro's reconcile dispatch on a paused harness: _dispatch_retro_run now refuses when paused, reap_retro defers the reconcile pre-dispatch instead of raising, and env_error mid-reconcile pauses the harness and retries rather than being read as a failed retro. cost=$1.87
