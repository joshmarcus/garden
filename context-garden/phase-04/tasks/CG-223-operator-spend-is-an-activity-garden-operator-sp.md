---
id: CG-223
title: 'Operator spend is an activity: garden operator-spend, the operator series on the costs page, the
  retro''s share, and the design doc''s operator-seat section'
status: in_review
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
branch: garden/cg-223-operator-spend-is-an-activity-garden-operator-sp
pr: https://github.com/joshmarcus/context-garden/pull/173
attempts: 1
last_dispatched_at: '2026-09-05T17:32:30+00:00'
created: '2026-09-05T17:04:17+00:00'
updated: '2026-09-05T17:46:45+00:00'
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
- 2026-09-05T17:05:38+00:00 dispatched work run 20260905T170522Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~16361 tokens)
- 2026-09-05T17:32:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/173 (base main): Added garden operator-spend (record/print, docs/operator-spend.jsonl), an operator activity on garden costs / the Costs page (its own validated color, sliceable by session, with compaction annotations), a retro Numbers section reporting operator spend and its share, and a new 'The operator seat' section in docs/design.md. cost=$6.08
- 2026-09-05T17:32:14+00:00 PR conflicts with main; rebase onto main conflicts (docs/architecture.md); a rebase agent will resolve it
- 2026-09-05T17:32:30+00:00 dispatched rebase run 20260905T173230Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~14140 tokens)
- 2026-09-05T17:39:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/173: Rebased onto origin/main; resolved the single conflict in docs/architecture.md's module map by keeping main's new `observe.py` row and adding this branch's new `costs.py`/`charts.py`/`operator_spend.py` row after it, plus the review.py row's CG-223 Numbers-section mention. Full test suite (827 passed, 3 skipped) confirms the merge is sound. No other files touched; did not push. cost=$0.38
- 2026-09-05T17:46:37+00:00 automated review: approve — All four acceptance criteria are met and verified against the diff; tests (827 passed) and lint are clean, and the new operator palette slot passes the dataviz validator in both themes. cost=$0.83
- 2026-09-05T17:46:45+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
