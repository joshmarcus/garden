---
id: CG-182
title: 'The tick never blocks the UI: actions do not wait for a tick, and checks and rebases run as records
  outside the tick'
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/web/common.py
- src/garden/web/actions/tasks.py
- src/garden/scheduler/__init__.py
- src/garden/scheduler/rebase.py
- src/garden/scheduler/reap.py
- src/garden/checks.py
- src/garden/scheduler/state.py
branch: garden/cg-182-the-tick-never-blocks-the-ui-actions-do-not-wait
pr: https://github.com/joshmarcus/context-garden/pull/129
attempts: 1
last_dispatched_at: '2026-09-05T11:29:43+00:00'
created: '2026-09-05T10:00:03+00:00'
updated: '2026-09-05T11:43:28+00:00'
---

## Goal

A person using the web UI never waits for the scheduler. A button press returns within a second regardless of what the tick is doing, a page renders in under half a second while a tick runs, and the tick itself stays under ten seconds because nothing that takes a minute (a test suite, a rebase with checks) runs inside it.

## Context

Seen by the user on 2026-09-05 at 09:43 and again at 09:55 ("the web page isn't opening", "web is slow again"). Measured: `GET /` took 1 to 18 seconds while a tick ran and 0.4 seconds between ticks; an independent process reading the same files took 0.4 seconds throughout and iowait was zero, so the contention is inside the server process. `Hub.tick()` holds `hub.lock` for the whole tick, and every POST action in `web/actions/*` takes that lock, so a button press waits for the tick to end. Since the merge queue (CG-141) the tick runs the product's full test suite in-process via `subprocess.run` for every pre-merge mechanical rebase (about 55 seconds each), so ticks grew from a few seconds to one or two minutes. The operator's mitigation that day was to turn off the `test` pre-PR check in garden.yaml and rely on GitHub CI, which is the gate the merge queue waits for anyway.

## Design

- Actions do not take a lock shared with the tick. `State.save()` already merges per key under its own file lock (CG-153), and task files are written whole; an action that needs the scheduler builds one, applies the change and saves. If serialising two actions matters, use a short lock around the action only.
- Checks become run records. A pre-PR check, a base probe or a pre-merge rebase-and-check is dispatched as a `check` (or `rebase`) run with its own directory, started by the tick and reaped on a later tick, exactly like a review; the task shows it on its page and the slot accounting counts it. The tick only starts and reaps.
- The tick has a budget: it logs its own duration in the tick report and warns when a pass exceeds ten seconds, naming the slowest step.
- GET pages never build a scheduler for reading if a lighter reader exists; `Site` reads tasks and state directly.

## Acceptance criteria

- [ ] With a tick running a pre-merge rebase and its checks, `POST /tasks/<id>/approve` returns within one second and `GET /` within half a second (a test drives a slow fake check and measures both).
- [ ] Pre-PR checks, base probes and pre-merge checks are run records reaped by a later tick; no `subprocess.run` of a product check remains inside `tick()`.
- [ ] The tick report carries the pass duration and the slowest step; a pass over ten seconds logs a warning.
- [ ] The `test` pre-PR check can be turned back on in garden.yaml without the UI slowing down.

## Log

- 2026-09-05T10:31:14+00:00 approved (web)
- 2026-09-05T10:31:45+00:00 dispatched work run 20260905T103136Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~23545 tokens)
- 2026-09-05T11:22:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/129 (base main): The web actions take a short action-only lock (never the tick's), and pre-PR checks, base probes, pre-merge rebase-checks and CI analysers all run as detached `check` run records reaped on a later tick, so no product-check subprocess runs inside tick(); the tick reports its own duration and slowest step and warns over budget. cost=$29.19
- 2026-09-05T11:29:39+00:00 automated review requested changes: Solid non-blocking-tick conversion with all four acceptance criteria tested, but detaching the pre-merge check opens a multi-tick window where the merge queue rebases a second candidate while the head's check is in flight, breaking CG-176's one-head invariant in the very config this task enables. cost=$3.25
- 2026-09-05T11:29:43+00:00 dispatched revise run 20260905T112943Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~25146 tokens)
- 2026-09-05T11:36:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/129: Fixed the multi-tick window where a detached pre-merge check let the merge queue rebase a second head: the queue now treats an in-flight merge_rebase check as the head via _merge_head_pending and picks no other candidate until it reaps. Added a regression test that holds the head's check open across ticks and asserts no second head is rebased. cost=$2.77
- 2026-09-05T11:42:12+00:00 automated review: approve — All four acceptance criteria are met and tested, the prior blocking one-head-invariant finding is genuinely fixed with a regression test, full suite and lint pass, and docs/description are clean and accurate. cost=$2.38
- 2026-09-05T11:42:16+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-05T11:43:28+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/129
