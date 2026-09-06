---
id: CG-251
title: Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs
  page and the retro
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
harness: codex
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:09+00:00'
updated: '2026-09-06T00:24:02+00:00'
---

## Goal

**User value:** the operator can read whether a cheaper model lowers the bill per merged task, which is the finding of this phase (sonnet halved the run price and did not lower the bill).

**Why now:** CG-213 and CG-230 cannot be evaluated without it; CG-233 and CG-214 (merged) supply the per-run cost and the page.

**Size:** medium. **Depends on:** CG-233, CG-214. Accepted means merged to the base branch (CG-228).

## Context

Every routing decision in phase 05 is a guess until the garden reports this number.

## Acceptance criteria

- [ ] The Costs page shows cost per accepted (merged) task, computed from CG-233's per-run cost data.
- [ ] Metrics report first-pass approval rate broken down by model, tier, and harness.
- [ ] The retro output includes both the cost-per-accepted-task figure and the first-pass approval breakdown.
- [ ] A test confirms the cost-per-accepted-task calculation counts only tasks merged to the base branch (CG-228) as accepted.
- [ ] Sonnet's cost-per-accepted-task figure appears alongside its per-run cost so the "halved run price but didn't lower the bill" finding is directly checkable.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-240 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002108Z-edit) cost=$0.10
- 2026-09-06T00:24:02+00:00 approved (cli)
