---
id: CG-231
title: garden trial can optionally wait for a trial to conclude
status: ready
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
discovered_from: CG-229
created: '2026-09-05T19:25:33+00:00'
updated: '2026-09-05T19:49:54+00:00'
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
