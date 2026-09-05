---
id: CG-048
title: Set or remove a phase budget from the web UI
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/web/app.py
- src/garden/web/templates/phase.html
- src/garden/config.py
- src/garden/scheduler.py
branch: garden/cg-048-set-or-remove-a-phase-budget-from-the-web-ui
pr: https://github.com/joshmarcus/context-garden/pull/61
attempts: 1
last_dispatched_at: '2026-09-04T22:18:46+00:00'
created: '2026-09-04T17:30:24+00:00'
updated: '2026-09-04T23:58:12+00:00'
---

## Goal

A person can set a phase's budget, raise it, or switch it off, from the phase page in the web UI, and the running scheduler honours the change without a restart.

## Context

Asked during the first live run. Today the only place a budget lives is `budgets:` in `garden.yaml` (or `products.<name>.budget_usd`), the scheduler reads config once at startup (`Scheduler.cfg` is `store.config`), and the phase page only prints "spent $x of $y". Raising this phase's cap from 25 to 100 meant editing the YAML by hand and restarting `garden serve`. Three things are needed:

1. A small form on the phase page: a number for the cap in USD, a "no budget" checkbox that removes the cap for that phase, and the current spend beside it. Post to a new route that writes the value.
2. Where the value goes: `garden.local.yaml` is per machine and gitignored, `garden.yaml` is shared; write to `garden.yaml` under `budgets:` (a budget is a team decision, and the file already documents the key), preserving comments and order of the rest of the file, or if that proves brittle, to a `budgets` block in `.garden/state.json` that overrides config and is shown as such. Say which in the PR.
3. Reload: the scheduler re-reads task files and state every tick; make it re-read config too (or at least `budgets`), so the loop picks the change up on the next pass and the "budget exceeded, dispatch paused" state clears when the cap is raised.

A `garden budget <product/phase> <usd|none>` CLI command should share the same code path.

## Acceptance criteria

- [ ] the phase page shows the cap with a form to set a number or choose "no budget".
- [ ] the change is visible on the next tick without restarting `garden serve`, and a paused phase resumes when its cap is raised or removed.
- [ ] `garden budget` sets and clears the same value.
- [ ] tests for the route, the CLI command and the reload.

## Out of scope

- Per-product budgets and the `budget_usd` default; only the per-phase cap.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T22:18:46+00:00 dispatched work run 20260904T221838Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~6389 tokens)
- 2026-09-04T22:25:59+00:00 opened https://github.com/joshmarcus/context-garden/pull/61 (base main): Added set/remove of a per-phase budget from the web UI phase page, a `garden budget` CLI command, and a shared `Scheduler.set_budget` code path. Budgets are stored as overrides in .garden/state.json (chosen over editing garden.yaml, which PyYAML cannot round-trip without stripping comments), so the running scheduler picks up changes on the next tick and a paused phase resumes when the cap is raised or removed. cost=$3.26
- 2026-09-04T22:28:33+00:00 automated review: approve — All four acceptance criteria are met with tests; the shared set_budget code path, state.json storage, and per-tick reload are correct, and the PR description is clean and complete. cost=$0.77
- 2026-09-04T23:58:12+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/61
