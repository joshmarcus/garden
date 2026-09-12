---
id: CG-388
title: Make revision-limit recovery the primary action and resume work in one click
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/web/actions/tasks.py
- src/garden/web/templates/task.html
- src/garden/scheduler/human.py
created: '2026-09-07T15:49:16+00:00'
updated: '2026-09-08T16:10:12+00:00'
---

## Goal

When a revision limit is the reason work needs attention, make the correct recovery action obvious and complete: reset the revision allowance and queue the preserved work to continue in one click.

## Owner request and current defect

Owner asked to highlight Reset revisions when a stuck-loop todo is caused by revisions, and make that action correct if necessary. Currently the reset-revisions web action only assigns revisions=0 and logs it; it does not clear the revision-cap stop or request continuation. Scheduler.retry clears the stop and queues the existing revision. The operator raised the configured max_revisions from3 to6 separately; do not confuse revision allowance with review-round caps or concurrent slots.

## Acceptance criteria

- [ ] On Inbox needs-attention cards and task details, a verified revision-cap stop shows one prominent accessible primary action, labelled Reset revisions and continue (or equally clear wording), with used/configured allowance and a short explanation of its effect. Do not highlight it for unrelated review limits, quota, memory pressure, missing evidence or other failures.
- [ ] One click uses a shared supported recovery operation to reset the applicable allowance, clear only the corresponding revision-cap stop and queue the existing revision. Preserve branch, PR, concrete feedback, run history and costs; no second Retry click or new implementation run is required.
- [ ] Respect phase holds, terminal tasks, active writers and normal resource/concurrency admission. Repeated/stale clicks cannot duplicate a run or reopen a merged task. Raising max_revisions does not alter concurrent worker/reviewer limits.
- [ ] Validate the real rendered Inbox-to-task recovery flow on a disposable capped garden, including the primary button state before/after, a retained-feedback revision queued under full capacity, and unrelated/terminal stop cases. Provide proportionate focused tests, self-review and exact-head CI; report unknowns honestly.

## Configuration change

max_revisions is now6 in the operating garden at the owner's request. The UI change is queued, not deployed. No resource cap or current temporary admission limit was relaxed.

## Log

- 2026-09-07T18:43:53+00:00 dispatch failed: work deferred by resource pressure: available memory 1527 MiB is below 1536 MiB; pause dispatch or wait for active runs to drain, then retry
- 2026-09-07T20:06:51+00:00 reset to ready by hand
- 2026-09-08T16:10:12+00:00 Unstarted cap-recovery scope and all owner requirements consolidated into CG-437 troubled-task/escalation ticket; preserve this history, do not implement a duplicate recovery operation.
