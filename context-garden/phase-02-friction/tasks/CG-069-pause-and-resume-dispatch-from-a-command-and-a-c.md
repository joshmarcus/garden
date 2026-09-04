---
id: CG-069
title: Pause and resume dispatch from a command and a configuration page
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/cli.py
- src/garden/web/app.py
- src/garden/config.py
branch: garden/cg-069-pause-and-resume-dispatch-from-a-command-and-a-c
pr: https://github.com/joshmarcus/context-garden/pull/38
attempts: 1
last_dispatched_at: '2026-09-04T19:22:45+00:00'
created: '2026-09-04T18:40:41+00:00'
updated: '2026-09-04T19:34:52+00:00'
---

## Goal

Dispatch can be paused and resumed without editing a file or restarting: `garden pause` / `garden resume` on the CLI, and a switch on a new Configuration page in the web UI, with the paused state visible everywhere the loop is described.

## Context

During the first live run, pausing dispatch meant writing `auto_dispatch: false` into the gitignored `garden.local.yaml` and restarting `garden serve`, and resuming means deleting the file and restarting again. The scheduler reads config once at startup, so nothing else works. A pause is the first thing a person reaches for when workers misbehave, and it has to be instant.

Keep the state in `.garden/state.json` under a `_control` entry (`{"dispatch": "paused", "by": "cli|web", "at": ..., "reason": ...}`), which every tick already reloads, so the change takes effect on the next pass with no restart. `auto_dispatch` in config stays as the default; the control entry overrides it. The tick's dispatch step checks the entry; reaping, polling and reviews continue while paused. Revise rounds are dispatch too and pause with it.

CLI: `garden pause [--reason ...]`, `garden resume`, and `garden status` / `garden doctor` print "dispatch paused (by web at 18:12: reason)". Web: a Configuration page (`/config`) with the pause switch and reason at the top, the loaded config files and the effective values of the keys a person changes most (`max_parallel`, `auto_dispatch`, `auto_revise`, budgets per phase, the tier map, `review.difficulty`, `github.draft_pr`) shown read-only for now; CG-048 adds editing budgets there. The Inbox header line "scheduler loop on · tick …" becomes "dispatch paused" with a Resume button when paused.

## Acceptance criteria

- [ ] `garden pause` stops new work and revise dispatch on the next tick without a restart; `garden resume` restarts it; both are logged as events.
- [ ] the Configuration page shows the switch and the effective config; the Inbox header shows the paused state with a Resume button.
- [ ] a tick while paused still reaps, polls and starts reviews (tests).
- [ ] the state survives a server restart and overrides `auto_dispatch` in config.

## Out of scope

- Editing config values from the page beyond the pause switch (CG-048 for budgets; a later task for the rest).

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T19:22:45+00:00 dispatched work run 20260904T192245Z-work via local [claude model=sonnet] (fresh session, base main, ~9813 tokens)
- 2026-09-04T19:32:39+00:00 opened https://github.com/joshmarcus/context-garden/pull/38 (base main): Implemented pause/resume dispatch via garden pause/resume CLI commands and a /config web page. Paused state is stored in .garden/state.json under _control, reloaded every tick, so changes take effect instantly without restart. The inbox footer shows 'dispatch paused' with a Resume button when active. All 191 tests pass. cost=$2.87
- 2026-09-04T19:34:52+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/38
