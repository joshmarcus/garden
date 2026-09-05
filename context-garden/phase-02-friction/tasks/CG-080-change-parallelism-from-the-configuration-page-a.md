---
id: CG-080
title: Change parallelism from the configuration page and the CLI, effective next tick
status: done
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
branch: garden/cg-080-change-parallelism-from-the-configuration-page-a
pr: https://github.com/joshmarcus/context-garden/pull/72
attempts: 1
last_dispatched_at: '2026-09-05T00:19:32+00:00'
created: '2026-09-04T19:16:39+00:00'
updated: '2026-09-05T00:28:00+00:00'
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
- 2026-09-04T22:45:20+00:00 dispatched work run 20260904T224511Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4592 tokens)
- 2026-09-04T22:53:49+00:00 opened https://github.com/joshmarcus/context-garden/pull/72 (base main): Added a live max_parallel override: Scheduler.overrides()/set_override()/clear_override()/effective() persist to _control.overrides and slots_free() reads it every tick; garden set/clear CLI commands and a Configuration-page form/clear control let you change it without a restart; garden status, garden doctor and the Inbox header show the live value. cost=$5.76
- 2026-09-04T22:56:33+00:00 automated review: approve — Live max_parallel override via garden set/clear and the Configuration page, effective next tick; all three acceptance criteria met with tests, persistence and dirty-tracking verified, checks green. cost=$0.70
- 2026-09-05T00:02:16+00:00 PR conflicts with main (src/garden/web/app.py); revise run will rebase and resolve
- 2026-09-05T00:19:32+00:00 dispatched revise run 20260905T001932Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~6016 tokens)
- 2026-09-05T00:23:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/72: Rebased the branch onto the current main, resolving the two-hunk conflict in src/garden/web/app.py by keeping both sides' additions (closed_count + max_parallel in ctx(), budget_overrides + max_parallel controls in the config route). All tests (359 passed) and ruff lint pass after rebase. cost=$0.86
- 2026-09-05T00:26:30+00:00 automated review: approve — Live max_parallel override via garden set/clear and the Configuration page, effective next tick; all three acceptance criteria met with passing tests, and the tick reloads state from disk so no restart is needed. cost=$0.67
- 2026-09-05T00:28:00+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/72
