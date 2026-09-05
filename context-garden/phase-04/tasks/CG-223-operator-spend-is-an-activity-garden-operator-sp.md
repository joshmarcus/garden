---
id: CG-223
title: 'Operator spend is an activity: garden operator-spend, the operator series on the costs page, the
  retro''s share, and the design doc''s operator-seat section'
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/events.py
- src/garden/cli/reports.py
- src/garden/retro.py
- tools/operator_spend.py
- docs/design.md
created: '2026-09-05T17:04:17+00:00'
updated: '2026-09-05T17:04:17+00:00'
---

## Goal

The operator's own spend is a first-class activity beside work, review, rebase, persona and retro: `garden costs` and the costs page (CG-214) show an `operator` series read from `docs/operator-spend.jsonl`, the retro reports the operator's share of the phase's total, and `docs/design.md` states the goal that the operator thread stays cheap and how the product serves it.

## Context

The user on 2026-09-05: make it explicit in the plans that keeping the high-level operator agent thread cheap is a goal, remind the operator to compact at boundaries, and keep ongoing records of operator session spend. The garden now carries the goal in `product.md`, the phase-04 goals and the operator skill, and `tools/operator_spend.py` appends a record per heartbeat (turns, tokens by kind, average context, list-price estimate) from the Claude Code transcript. That record is outside the product; this task brings it in so the costs page can draw it and the retro can quote it.

## Acceptance criteria

- [ ] `garden operator-spend record [--transcript <path>]` (the script's logic moved into the tool) appends a record; `garden operator-spend` prints the sessions and totals; the file format is documented.
- [ ] `garden costs` and the costs page treat `operator` as an activity with its own colour, read from the record, sliceable by session; the annotation for a compaction (a `compacted` record) is drawn like the others.
- [ ] The retro's numbers section reports operator spend and its share of the phase total.
- [ ] `docs/design.md` gains a short section, "The operator seat", stating the goal and the three levers: fewer cards, a configurable observation feed, compaction at boundaries.

## Log

- 2026-09-05T17:04:17+00:00 approved (web)
