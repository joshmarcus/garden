---
id: CG-083
title: 'A reap is atomic: a restart mid-tick never loses a finished run'
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/runs.py
branch: garden/cg-083-a-reap-is-atomic-a-restart-mid-tick-never-loses
pr: https://github.com/joshmarcus/context-garden/pull/81
attempts: 2
last_dispatched_at: '2026-09-05T00:23:41+00:00'
created: '2026-09-04T19:25:01+00:00'
updated: '2026-09-05T00:23:41+00:00'
---

## Goal

Reaping a finished run either completes (run record updated, task transitioned, PR opened or updated) or leaves everything as it was, so a scheduler killed mid-tick does not strand a finished run.

## Context

At 19:23 UTC during the first live run, `garden serve` was restarted while a tick was reaping CG-050's finished work run. The run record had already been written `done`, but the task had not been transitioned and no push or PR had happened. The next tick saw a `running` task with no `running` run, logged "no active run found; back to ready", and dispatched a second work run on the same worktree, spending a second run to redo or re-report the first one's commits. Restarts are routine (config changes, upgrades; CG-050 makes the garden restart itself), so the reap must survive them. Write the run record's final status last, after the task transition and the PR step, or record a `reaping` marker that the next tick resumes from, and make "no active run found" look for a finished-but-unreaped run before giving up on the task.

## Acceptance criteria

- [ ] a run whose record says done but whose task is still running is finalized on the next tick, not redispatched.
- [ ] a test that interrupts the reap between the record write and the transition, then ticks again.
- [ ] `garden runs` shows such a run as "finished, not yet reaped" until it is.

## Log

- 2026-09-04T19:25:01+00:00 approved
- 2026-09-04T22:54:11+00:00 dispatched work run 20260904T225403Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4498 tokens)
- 2026-09-04T23:06:05+00:00 no active run found; back to ready
- 2026-09-04T23:07:01+00:00 dispatched work run 20260904T230700Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4552 tokens)
- 2026-09-04T23:09:36+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$0.97
- 2026-09-04T23:09:51+00:00 dispatched revise run 20260904T230950Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~5629 tokens)
- 2026-09-04T23:19:07+00:00 discovered work filed: CG-124
- 2026-09-04T23:19:42+00:00 opened https://github.com/joshmarcus/context-garden/pull/81 (base main): Fixed the pre-PR check failure, which was an unrelated pre-existing test-harness flake (commit-collision between a stacked task's work run and its parent's revise round), not a bug in the atomic-reap changes. Applied the same fix already diagnosed on sibling task CG-064 (unmerged): mix task/run identity into the fake worker's commit message, scope the duplicate-PR assertion to the task's own branch, and add a deterministic regression test. cost=$3.34
- 2026-09-04T23:22:47+00:00 automated review: approve — Atomic-reap resume is correctly designed (terminal-run + RUNNING-task uniquely flags an interrupted reap; resume is idempotent for PR/discovery/push) and all three acceptance criteria are met with direct tests; full suite and ruff pass. cost=$0.72
- 2026-09-05T00:02:18+00:00 PR conflicts with main (tests/test_scheduler.py); revise run will rebase and resolve
- 2026-09-05T00:23:41+00:00 dispatched revise run 20260905T002340Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~5490 tokens)
