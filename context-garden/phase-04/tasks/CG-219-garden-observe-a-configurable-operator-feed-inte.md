---
id: CG-219
title: 'garden observe: a configurable operator feed (interval, event kinds, digest window) that prints
  one status line, the cards, stuck runs and a digest, for a person or an operator agent'
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/cli/reports.py
- src/garden/events.py
- src/garden/inbox.py
- src/garden/runs.py
- .claude/skills/garden-operate/SKILL.md
- docs/architecture.md
created: '2026-09-05T16:48:29+00:00'
updated: '2026-09-05T16:48:29+00:00'
---

## Goal

`garden observe` is the one command an operator, human or agent, reads the garden through: at a configurable interval it prints a status line (service, slots, spend, counts per status for the open phases), then only what needs a hand (decision cards, runs with no output for longer than a threshold or whose process is gone, tracebacks in the log), then a digest of the window. `garden observe --follow` streams the event kinds the operator chose as they happen. Every knob lives in `garden.yaml` under `observe:` with sensible defaults, so an operator does not maintain a script and a cheaper cadence is one line of config.

## Context

Asked by the user on 2026-09-05 ("can we make it configurable?") after the operator replaced a ten-minute, forty-line heartbeat and a firehose event monitor with a fifteen-minute one-line script plus a filtered tail, to cut the cost of the orchestrating session: each observation turn re-reads the session's whole context, so cadence and volume are the cost. The script and the filter live in the session's scratch directory today; the `garden-operate` skill describes the same first-look block by hand. `garden digest --since` and `garden inbox` already compute the pieces.

## Design

- `observe:` in garden.yaml: `interval: 30m`, `digest_window: 30m`, `events: [question, needs_human, failed]` (the kinds `--follow` streams), `stuck_after: 15m`, `line_width: 160`, `phases: open` (or a list). Defaults are those values.
- **Profiles.** `observe.profiles` names presets and `observe.profile` picks one; built-ins: `quiet` (interval 30m, events question, needs_human, failed; digest 30m), `watch` (interval 10m, plus decision, stall, budget, phase and retro events, review verdicts with changes requested; digest 10m) and `debug` (interval 5m, every transition, dispatch, review and merge; stuck_after 5m). The user's words: "sometimes you want to run efficiently, sometimes you want more observability." `--profile` overrides per invocation, the Config page switches the profile live (the config reload picks it up within a tick), and a running `--follow` switches without a restart.
- **Switch it from the UI.** The rail carries an "Observation" pulldown (quiet, watch, debug, plus any custom profile) that applies on change with no Set button (CG-190) and writes the profile as a live override in state, exactly like `max_parallel` (CG-080); the Config page shows the same control with each profile's interval and events beside it. `garden observe --follow` and the scheduler read the override within a tick, so an operator agent's feed changes without a restart and a person can turn the volume up while watching something and down when leaving.
- `garden observe` prints one pass and exits (for a scheduler, a cron, or an agent's heartbeat); `garden observe --follow` prints a pass every `interval` and, between passes, one line per configured event as it lands; `--json` emits the same as one object per pass for an agent that parses.
- The status line is one line; each card is one line with the task id, its kind and the action that clears it (from `inbox.py`'s decision table); a stuck run is one line; the digest is `garden digest`'s summary trimmed to a few lines. Nothing prints when a section is empty.
- The `garden-operate` skill's first-look block becomes "run `garden observe`", and its stall table stays as the interpretation.

## Acceptance criteria

- [ ] `garden observe` prints the status line, cards, stuck runs, tracebacks and digest, omitting empty sections; `--json` carries the same fields; a test renders both on a fixture garden with one card and one stuck run.
- [ ] `garden observe --follow` respects `observe.interval` and streams only `observe.events`; a test feeds three events and sees one line.
- [ ] The rail and the Config page have the Observation pulldown; changing it writes the live override, shows a saved mark, and a running `garden observe --follow` switches on its next pass; a test changes the profile through the web action and reads it back through `garden observe --json`.
- [ ] The three built-in profiles exist, `observe.profile` and `--profile` select one, a custom profile in `observe.profiles` overrides any field, and switching the profile in the Config page changes a running `--follow` within a tick; a test covers quiet and debug on the same event log.
- [ ] Every knob has a default and is documented in `docs/architecture.md`; `garden config` (or the Config page) shows the observe block.
- [ ] `.claude/skills/garden-operate/SKILL.md` points its first look at `garden observe`.

## Log

- 2026-09-05T16:48:29+00:00 approved (web)
