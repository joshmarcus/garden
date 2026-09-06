---
id: CG-251
title: Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs
  page and the retro
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-251-cost-per-accepted-task-and-first-pass-approval-p
pr: https://github.com/joshmarcus/context-garden/pull/198
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-06T00:45:08+00:00'
created: '2026-09-05T23:58:09+00:00'
updated: '2026-09-06T01:55:17+00:00'
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

- [ ] Owner's ask (2026-09-06 02:25Z): one table per metric with difficulty as rows and every model that did work as columns, on the Costs page and in `garden metrics`: mean total cost per accepted task, work-run cost, revise rounds, review rounds, first-pass approval, median lead time and runs per task, each cell with its n; the model is the one whose work or trial run produced the merged PR, and reviews, rebases and checks count toward the task's total regardless of their own model.

- [ ] Every table of numbers shades its cells within each row from a light green ground for the best value to a light red for the worst (direction per metric: lower is better for cost, revise rounds and lead time; higher for first-pass approval), cells with n under three shaded faintly and marked, legible in light and dark, with a small mark on best and worst so colour is never the only signal (owner, 2026-09-06 02:45Z).

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-240 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002108Z-edit) cost=$0.10
- 2026-09-06T00:24:02+00:00 approved (cli)
- 2026-09-06T00:25:21+00:00 dispatched work run 20260906T002504Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~6698 tokens)
- 2026-09-06T00:37:25+00:00 opened https://github.com/joshmarcus/context-garden/pull/198 (base main): Adds accepted-task cost and first-pass approval outcomes by tier, model, and harness across metrics, Costs, and retro reporting. cost=$0.85
- 2026-09-06T00:42:52+00:00 automated review requested changes: Feature is wired through CLI, Costs page and retro correctly, but the per-model/per-harness cost-per-accepted-task figure silently excludes review and edit run costs (no model/harness tag on those events), understating exactly the routing-comparison finding this task is meant to surface. cost=$0.83
- 2026-09-06T00:45:08+00:00 dispatched revise run 20260906T004507Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~7178 tokens)
- 2026-09-06T00:57:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/198: Accepted-task cost now assigns all supporting run costs to the task's implementation model and harness, avoiding an understated routing bill. Added regression coverage for untagged review and edit costs. cost=$0.60
- 2026-09-06T01:55:17+00:00 marked done (web)
