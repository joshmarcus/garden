---
id: CG-253
title: The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics
  and the rail
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:09+00:00'
updated: '2026-09-06T13:14:24+00:00'
---

## Goal

**User value:** the definition of done is measured by the tool, not counted by hand; personas read the phase's own pages.

**Why now:** phase 04 has no walkthrough, tick duration is only in the CLI tick line, and hand merges were counted by hand. Add Costs, backlog and retro pages to pages_for, run garden walkthrough before the personas, report hand merges as merged PRs the queue did not merge, and mean and max tick duration.

**Size:** easy. **Depends on:** CG-182, CG-201 (merged).

## Context

Proposed at the context-garden/phase-04 retro. Three definition-of-done lines were guessed this phase because nothing measured them.

## Acceptance criteria

- [ ] `pages_for` includes Costs, backlog, and retro pages, verified by `tests/test_pages_for.py::test_includes_costs_backlog_retro`.
- [ ] `garden walkthrough` runs before the persona pages so its output feeds them.
- [ ] Garden metrics report hand merges as merged PRs the queue did not merge, not counted by hand.
- [ ] Garden metrics and the rail show mean and max tick duration, not just the CLI tick line.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Folded in at approval (operator, 2026-09-06)

- [ ] From CG-264 (designer): `garden walkthrough` captures today's page set, not phase 02's: Costs, the backlog view, the retro page, the kickoff panel and a task page with a decision card.
- [ ] From CG-274 (project manager): `garden metrics` and the rail report hand merges, rebase rounds per merge split into mechanical and agent, and the operator's share of spend from the ledger.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-242 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002109Z-edit) cost=$0.09
- 2026-09-06T00:24:03+00:00 approved (cli)
- 2026-09-06T13:13:08+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:24+00:00 reset to ready by hand
