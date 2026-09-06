---
id: CG-351
title: Compare total cost with average cost per task and activity counts on the Costs page
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-06T16:40:42+00:00'
updated: '2026-09-06T16:40:42+00:00'
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
