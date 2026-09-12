---
id: CG-514
title: Never require a second review solely by count
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-490
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/review.py
- src/garden/config.py
- src/garden/web/pages/task.py
- tests/test_automerge.py
- tests/test_review.py
branch: garden/cg-514-never-require-a-second-review-solely-by-count
pr: https://github.com/joshmarcus/context-garden/pull/422
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T13:38:44+00:00'
created: '2026-09-10T11:16:35+00:00'
updated: '2026-09-10T13:58:01+00:00'
---

## Goal

Make one valid approval for the current PR head sufficient for every Garden task. No task may wait for a second review merely because of its difficulty, self-hosting status, tool-provider status, or a configured numeric review floor.

## Confirmed residual defect

Completed CG-490 removed the implicit hard-tier floor, but current main still has two other count-based holds. `Scheduler._automerge_min_review_rounds` raises the default to two for `provides_tool: true`, while self-products require an additional current-head persona or human opinion after the automated approval. Current Inbox cards have consequently shown `need 2` after a valid approving round. The owner explicitly requires that tasks never require two reviews. Treat this as a focused residual of CG-490 rather than reopening its merged implementation.

## Acceptance criteria

- [ ] One valid approval bound to the current PR head satisfies the review-count gate for every easy, medium, and hard task, including `self: true` and `provides_tool: true` products.
- [ ] Remove the self-product persona-or-human second-opinion hold and the tool-provider two-round default. Review scheduling, pending-review recovery, merge gating, and Inbox/task-page reasons must agree and must not queue or display `need 2` once one current-head approval exists.
- [ ] A configured `automerge_min_review_rounds` value above one cannot reintroduce a two-review requirement. Validate, migrate, or safely normalize existing global and per-product values with a clear diagnostic, while preserving ordinary one-review behavior.
- [ ] Preserve substantive review findings, revisions after requested changes, current-head freshness, applicable CI, conflicts, scratch-merge checks, explicit/manual holds, required non-review evidence, merge serialization, and source lineage. A later source change still requires a fresh approval for that new head.
- [ ] Add focused regressions for hard, self, and tool-provider products; legacy global and per-product values above one; a requested-changes revision that changes the head; queued/recovered review state; and removal of stale `need 2` UI text. Verify Linux and portable behavior; report macOS and Windows-through-WSL if not exercised.

## Scope

Follow up CG-490 in the existing review scheduler, automerge gate, configuration validation/migration, and focused UI status paths. Do not weaken non-review gates or erase historical review records.

## Log

- 2026-09-10T11:16:35+00:00 approved (owner instruction)
- 2026-09-10T11:17:25+00:00 dispatched work run 20260910T111725Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19464 tokens)
- 2026-09-10T11:33:09+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:35:37+00:00 opened https://github.com/joshmarcus/context-garden/pull/422 (base main): Made one current-head automated approval sufficient for all task difficulties and self/tool-provider products. Legacy global and per-product review floors above one now normalize to one with warnings; focused tests passed (192 tests plus targeted reruns), Ruff passed, and Linux behavior was exercised. cost=$2.38
- 2026-09-10T11:40:41+00:00 automated review requested changes: The fixed merge minimum and configuration normalization work, but existing queued count-only second reviews are not retired and will still run before merge. cost=$0.55
- 2026-09-10T11:49:38+00:00 dispatched revise run 20260910T114938Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20466 tokens)
- 2026-09-10T11:57:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:59:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/422: A proven current-head approval now retires legacy queued count-only review work and same-head recovery state before dispatch, while preserving persona and non-counted fresh-review work. The affected 194 tests and Ruff passed on Linux. cost=$0.73
- 2026-09-10T12:02:57+00:00 automated review: approve — One current-head approval is sufficient across hard, self, and tool-provider products, including legacy configurations and queued count-only recovery state. cost=$0.33
- 2026-09-10T13:36:58+00:00 triage: changes requested by hand: Current exact-head CI34474008753 and34474005295 both fail tests/test_queue_state.py because review.py directly removes a
- 2026-09-10T13:38:44+00:00 dispatched revise run 20260910T133843Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20542 tokens)
- 2026-09-10T13:43:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:44:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/422: Routed stale count-only automerge hold removal through the canonical queue-state owner while preserving the approved one-review behavior. Committed as 9f3ceaff; 186 focused tests, the exact-head queue-state test, Ruff, and diff checks passed on Linux. cost=$0.49
- 2026-09-10T13:47:04+00:00 automated review: approve — One current-head approval now suffices across task tiers and self/tool-provider products while preserving independent merge and freshness gates. Legacy count-only queued work and UI holds are retired through the canonical queue-state API. cost=$0.41
- 2026-09-10T13:56:26+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T13:58:01+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/422
