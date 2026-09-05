---
id: CG-214
title: 'A costs page: spend per activity over time, sliceable by difficulty, model, harness, phase and
  task, with the same numbers in garden costs'
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/events.py
- src/garden/runs.py
- src/garden/web/pages/runs.py
- src/garden/web/pages/phase.py
- src/garden/web/templates/base.html
- src/garden/plants.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
created: '2026-09-05T16:05:50+00:00'
updated: '2026-09-05T16:05:50+00:00'
---

## Goal

A `/costs` page answers "what are we paying for, and is it changing" without reading transcripts: spend over time as a stacked chart by activity (work, revise, rebase, review, persona, retro, check), a breakdown table under it, and controls to slice both by difficulty tier, model, harness, product and phase, or task, and to pick the time window. `garden costs` prints the same breakdown for the same filters, so a manager and an operator read one set of numbers.

## Context

Asked by the user on 2026-09-05 after a day in which spend reached $1,100, the account hit its monthly limit at 13:12, and the tier map was changed at 14:50 to cut cost; the only way to see what the change did was a script over `events.jsonl`. Every `run_finished` event already carries `cost_usd`, `mode`, `model`, `harness`, `task` and usage; the task file carries `difficulty`, `product` and `phase`; `garden metrics` and `garden usage` give per-tier and per-task totals but no time axis and no slicing. The herbarium look applies: drawings in the line style of `plants.py`, no chart library, inline SVG that reads in both themes and prints.

## Design

- One aggregation in `events.py` (or a new `costs.py`): `cost_series(events, tasks, *, since, until, bucket, group_by, filters)` returns buckets (hour or day) with totals per group and a grand total; `group_by` is one of activity, difficulty, model, harness, phase, task; filters are the same keys. Cache reads and cache writes are reported beside cost so a cache-heavy run is visible.
- `/costs`: a stacked area or bar chart (inline SVG, one colour per group from a small fixed palette, legend with totals, hover shows the bucket's numbers as text), the controls above it as pulldowns that apply on change (CG-190 rule), the table below with group, runs, cost, mean per run, and share; a link from the rail and from each phase page (pre-filtered to the phase).
- `garden costs [--since 24h] [--by activity|difficulty|model|harness|phase|task] [--phase P] [--model M] ...` prints the table; `--json` for scripts.
- The phase page's cost line links to the page filtered to that phase; the retro's numbers section uses the same aggregation.
- **Annotations as dotted vertical lines.** Events that change what the numbers mean are drawn on the chart as dotted vertical lines with a short label at the top: `config_reloaded` (with the keys that changed, for example `harnesses` at 14:59 or `review` at 14:36), a pin move (the `tool_upgraded` event or a `pin` note), a phase freeze or close, a pause and resume, a budget change, and a note the operator adds by hand (`garden costs --note "tier map: mediums to sonnet"` writes an `annotation` event). Hovering a line shows the full text; the table lists the annotations in the window.

## Acceptance criteria

- [ ] `/costs` renders the chart and table for the whole garden by activity and by day by default; every pulldown changes the group or filter on change with no button; the page reads correctly in light and dark and with JavaScript off (the form posts).
- [ ] `garden costs` prints the same totals for the same filters; a test compares web and CLI output on a fixture event log.
- [ ] Slicing by difficulty, model, harness, phase and task each work; a test covers a log with two models and two tiers across two days.
- [ ] The page answers today's question: it shows spend per hour on 2026-09-05 dropping after 14:50, when the tier map changed.
- [ ] Annotations: config reloads, pin moves, freezes, closes, pauses, budget changes and hand-written notes appear as labelled dotted vertical lines; `garden costs --note` writes one; a test renders a log with two annotations and finds both lines.

## Log

- 2026-09-05T16:05:50+00:00 approved (web)
