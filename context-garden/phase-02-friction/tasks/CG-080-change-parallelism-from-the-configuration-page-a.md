---
id: CG-080
title: Change parallelism from the configuration page and the CLI, effective next tick
status: ready
product: context-garden
phase: phase-02-friction
depends_on:
- CG-069
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- src/garden/config.py
created: '2026-09-04T19:16:39+00:00'
updated: '2026-09-04T19:16:39+00:00'
---

## Goal

`max_parallel` (and `review_parallel` once CG-074 lands) can be changed while the garden runs, from the Configuration page and with `garden set max_parallel 5`, taking effect on the next tick without a restart.

## Context

Asked during the first live run, after three restarts in an hour to move `max_parallel` from 10 to 3 to 5. CG-069 introduces the Configuration page and the `_control` entry in `state.json` that the tick reloads; this task adds the first editable numbers to it. The control entry overrides the value from `garden.yaml`; the page shows both the file value and the live override, with a "clear" that goes back to the file. `garden status` and the Inbox header show the live limit. Running workers are never stopped by lowering the limit; the tick just dispatches nothing until the count drops below it.

## Acceptance criteria

- [ ] setting `max_parallel` on the page or with `garden set` changes how many workers the next tick dispatches; no restart.
- [ ] the page shows file value, live override and a clear control; `garden status` shows the live value.
- [ ] tests for the override, the clear and the tick's use of it.

## Out of scope

- Editing other config keys live; this is the pattern for them to follow.

## Log

- 2026-09-04T19:16:39+00:00 approved
