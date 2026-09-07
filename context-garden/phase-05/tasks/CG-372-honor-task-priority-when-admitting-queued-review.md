---
id: CG-372
title: Honor task priority when admitting queued reviews and prevent starvation
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
branch: garden/cg-372-honor-task-priority-when-admitting-queued-review
pr: https://github.com/joshmarcus/context-garden/pull/266
attempts: 1
last_dispatched_at: '2026-09-07T05:34:25+00:00'
created: '2026-09-07T05:24:29+00:00'
updated: '2026-09-07T14:47:19+00:00'
---

## Goal

Honor owner task priority across review admission and avoid starving a ready review behind repeatedly admitted lower-priority work.

## Evidence

CG364 was owner-promoted P0. PR260 head21036d54 has passed exact CI since04:41, pending_reviews=[{kind:review,count_round:true}], no needs_human, zero reviews by05:23. Lower-priority tasks repeatedly occupied available shared slots. Installed scheduler/review.py:_drain_pending_reviews iterates tasks.values() without priority ordering; investigate full tick ordering/shared admission too. Operator checks could not launch review without violating the shared4/reviewer1 cap. Do not solve by exceeding caps or deleting review gates.

## Acceptance criteria

- [ ] Eligible pending reviews honor task priority and deterministic fairness within equal priorities. Worker/check/review shared-cap admission cannot indefinitely starve ready priority-critical validation through repeated lower-priority starts. Define interaction with existing round-robin/admission rules explicitly.
- [ ] With P0 review queued and lower-priority work available, releasing one shared slot selects the P0 review when its reviewer/harness/evidence gates permit. Cover occupied reviewer, held/stale review, active same-task worker and paused harness; preserve slot limits and no duplicate dispatch.
- [ ] Admission/wait explanations identify the actual blocking gate and queue ordering. No fabricated approval, forced termination or hidden reserved capacity.
- [ ] Focused deterministic scheduler tests and exact-head GitHubCI, bounded serial local work, internal self-review/fix. No production edits.

## Log
## Goal

One or two sentences.

## Context

What the agent needs to know that is not in the reading list.

## Acceptance criteria

- [ ] ...

## Out of scope

- ...
- 2026-09-07T05:34:25+00:00 dispatched work run 20260907T053359Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9160 tokens)
- 2026-09-07T05:52:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/266 (base main): Queued reviews now drain in strict task-priority order before ready workers claim shared local capacity. Equal-priority queued reviews retain their turn over newly requested rounds, and wait text identifies a preceding queue entry. cost=$1.78
- 2026-09-07T09:40:02+00:00 priority 1 -> 0 (web)
- 2026-09-07T14:47:19+00:00 Fast-forward: verified GitHub merge 933912ec5132299a71432b1ba01e45f1b60b1e6a after exact-head CI and operator self-review. Not yet deployed.
