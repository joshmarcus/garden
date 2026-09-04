---
id: CG-083
title: 'A reap is atomic: a restart mid-tick never loses a finished run'
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/runs.py
created: '2026-09-04T19:25:01+00:00'
updated: '2026-09-04T19:25:01+00:00'
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
