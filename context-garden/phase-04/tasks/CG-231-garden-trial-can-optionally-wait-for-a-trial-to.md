---
id: CG-231
title: garden trial can optionally wait for a trial to conclude
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/scheduler/trials.py
- src/garden/scheduler/dispatch.py
- src/garden/runner/local.py
- src/garden/trials.py
- tests/test_trials.py
branch: garden/cg-231-garden-trial-can-optionally-wait-for-a-trial-to
pr: https://github.com/joshmarcus/context-garden/pull/186
discovered_from: CG-229
attempts: 1
last_dispatched_at: '2026-09-05T20:12:19+00:00'
created: '2026-09-05T19:25:33+00:00'
updated: '2026-09-05T20:24:07+00:00'
---

## Goal

`garden trial` currently prints a contenders table right after dispatching, so every row shows `running` with no cost yet. A `--wait` (or poll) option that blocks until the trial resolves (comparing/done/inconclusive) would let the CLI's summary genuinely match what the trials/task pages show once contenders finish, instead of only right after the dispatch.

## Acceptance criteria

- [ ] `garden trial ... --wait` polls until the trial reaches a terminal state (done or inconclusive) and prints the resolved contender table.

## Provenance

Discovered by CG-229 (Trial contender worktrees get the product setup like any work run, and a contender that reports a blocked environment is a harness failure, not a model loss) during run `20260905T185206Z-work`.

## Log

- 2026-09-05T19:25:33+00:00 discovered by CG-229
- 2026-09-05T19:49:54+00:00 approved (web)
- 2026-09-05T19:49:54+00:00 priority 1 -> 3 (web)
- 2026-09-05T19:50:13+00:00 dispatched work run 20260905T194957Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~17527 tokens)
- 2026-09-05T20:07:26+00:00 opened https://github.com/joshmarcus/context-garden/pull/186 (base main): Added a `--wait`/`--interval` option to `garden trial` that ticks the scheduler until the trial reaches a terminal state (done/inconclusive), then prints the resolved contender table instead of the just-dispatched snapshot. cost=$1.55
- 2026-09-05T20:12:00+00:00 automated review requested changes: The --wait loop's shape is correct, but --interval 0 is silently coerced to the 60s config default, making the new test actually sleep 60 real seconds and leaving no way to request a zero-delay poll. cost=$0.52
- 2026-09-05T20:12:19+00:00 dispatched revise run 20260905T201219Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~17989 tokens)
- 2026-09-05T20:17:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/186: Fixed the reviewer's blocking finding: `--interval 0` no longer gets silently coerced to the 60s config default, since `interval` now defaults to `None` and only falls back to config when genuinely unset. Full test suite and lint pass. cost=$0.37
- 2026-09-05T20:22:29+00:00 automated review: approve — garden trial --wait correctly polls until the trial concludes and prints the resolved table; tests and lint pass, description is clean. cost=$0.39
- 2026-09-05T20:22:35+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-05T20:24:07+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/186
