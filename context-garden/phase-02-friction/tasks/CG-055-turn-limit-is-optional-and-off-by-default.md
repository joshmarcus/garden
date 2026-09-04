---
id: CG-055
title: Turn limit is optional and off by default
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/harness.py
- garden.yaml
- README.md
branch: garden/cg-055-turn-limit-is-optional-and-off-by-default
pr: https://github.com/joshmarcus/context-garden/pull/27
attempts: 1
last_dispatched_at: '2026-09-04T17:43:20+00:00'
created: '2026-09-04T17:43:19+00:00'
updated: '2026-09-04T17:49:20+00:00'
---

## Goal

The harness's hard turn limit (`--max-turns` for claude) is an optional setting, off unless `harnesses.<name>.max_turns` is set to a number.

## Context

Asked during the first live run after four of fifteen worker runs died on the default cap of 60 turns with no final message, no result line and their commits unreported, so each cap hit doubled the task's cost. The guards that matter are the wall-clock `timeout_minutes` and the phase budget; a turn count is a poor proxy for either. `Harness` puts `--max-turns 60` on every claude command from a default in its config table. Remove the default, pass the flag only when the setting is present and greater than zero, say so in the README and the comment in `garden.yaml`, and keep the setting working for anyone who wants a cap.

## Acceptance criteria

- [ ] with no `max_turns` in config, the claude command has no `--max-turns` argument.
- [ ] `max_turns: 80` puts `--max-turns 80` on the command; `max_turns: 0` is the same as unset.
- [ ] `garden.yaml` and the README describe the setting as optional and off by default.
- [ ] tests for both cases.

## Out of scope

- Resuming a run that hit a cap (CG-040).

## Log

- 2026-09-04T17:43:19+00:00 approved
- 2026-09-04T17:43:20+00:00 dispatched work run 20260904T174319Z-work via manual [human] (fresh session, base main, ~11155 tokens)
- 2026-09-04T17:47:30+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/27 (base main): The claude harness passes --max-turns only when max_turns is configured; the default cap is gone, and garden.yaml carries today's budget and model decisions.
- 2026-09-04T17:49:20+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/27
