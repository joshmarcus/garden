---
id: CG-351
title: Compare total cost with average cost per task and activity counts on the Costs page
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 1
order: 9
difficulty: medium
reading:
- src/garden/costs.py
- src/garden/web/pages/costs.py
- docs/architecture.md
branch: garden/cg-351-compare-total-cost-with-average-cost-per-task-an
pr: https://github.com/joshmarcus/context-garden/pull/377
attempts: 1
last_dispatched_at: '2026-09-09T14:49:25+00:00'
created: '2026-09-06T16:40:42+00:00'
updated: '2026-09-09T15:08:51+00:00'
---

## Goal

The Costs page offers Total cost and Average cost per task views for the selected grouping and time range, so an operator can distinguish more activity from higher cost per participating task. Keep total cost and the denominator accessible in either view. This complements cost per accepted task; it is a different measure.

## Semantics and evidence

- For each category/time bucket, divide its recorded run cost by the distinct task IDs contributing runs to that category within the same filters/window. Sum all repeated revisions of a task before dividing; never call cost per run cost per task. Show contributing task count and run count alongside the average.
- A task may participate in several categories/buckets, so their counts are not additive. Compute an overall average from overall total and the union of contributing tasks, not by averaging category averages. Explain that work and revise categories may have different task cohorts; a cost ratio between them does not by itself measure rework for matched tasks.
- Count a task with recorded zero-cost activity as participating. Keep missing/unpriced usage distinct from zero, flag partial totals/averages, and avoid an exact-looking complete average when pricing is missing. Activity with no task ID is shown separately with per-task average unavailable, not assigned a fabricated task.
- Preserve current filters/groupings and reflect the chosen metric in labels, units, URLs and chart/table/tooltips. Accessible explanations define the denominator and note that an activity-window average is not lifetime cost per completed task. Empty buckets show unavailable rather than division by zero.
- Tests use unequal cohorts and repeated runs: doubling participating tasks with equal per-task spend doubles total but leaves average unchanged; a second revise run for one task increases that task's category cost without increasing the task denominator; overall average uses unique tasks. Cover missing prices and taskless activity.
- Walk through the actual app with filters and the toggle, verifying totals/counts/averages against a small known dataset. Record interaction outcomes, not only screenshots.

## Provenance and scheduling

Josh requested this on 2026-09-06 after observing the rising revise/work cost ratio: make it clear whether costs change because of more activity. Filed as a draft feature in frozen phase 06; do not expand stabilization scope or dispatch without the existing gate or an explicit exception.

## Log

- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T20:10:03+00:00 approved (owner-unfreeze-phase06)
- 2026-09-09T09:48:41+00:00 priority 2 -> 1 (web)
- 2026-09-09T13:57:10+00:00 dispatched work run 20260909T135706Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~14181 tokens)
- 2026-09-09T14:02:22+00:00 preserved uncommitted worktree changes from run 20260909T135706Z-work outside the PR: `git stash apply 8393a66b7b16eb55c6840d12cae5f91d5b9029b8` in /home/joshua/work/worktrees/CG-351 (garden:CG-351:20260909T135706Z-work:reap)
- 2026-09-09T14:02:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:03:44+00:00 opened https://github.com/joshmarcus/context-garden/pull/377 (base main): Added total-cost versus average-cost-per-participating-task comparison on Costs, with unique-task denominators, pricing completeness, taskless handling, and cohort guidance. Verified on commit 37004ea43 with focused Costs page/aggregation tests (22 passed) and ruff lint (passed). cost=$0.59
- 2026-09-09T14:29:50+00:00 automated review requested changes: Distinct-task and missing-price behavior is otherwise well covered, but taskless spend is not actually separated and suppresses valid tasked averages. cost=$0.33
- 2026-09-09T14:49:25+00:00 dispatched revise run 20260909T144920Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15285 tokens)
- 2026-09-09T14:51:56+00:00 preserved uncommitted worktree changes from run 20260909T144920Z-revise outside the PR: `git stash apply b59c8471a41da1450f98d9abe0002cc68ff5837a` in /home/joshua/work/worktrees/CG-351 (garden:CG-351:20260909T144920Z-revise:reap)
- 2026-09-09T14:51:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:53:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/377: Separated taskless spend from tasked per-task averages while retaining complete total spend; added the taskless-spend breakdown column. Verified commit 0e47e92b6 with focused Costs tests (24 passed) and ruff lint (passed). cost=$0.24
- 2026-09-09T15:06:35+00:00 automated review: approve — The Costs page correctly compares total spend with average cost per participating task, including distinct-task denominators, repeated runs, partial pricing, and separately reported taskless spend. cost=$0.36
- 2026-09-09T15:08:51+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/377
