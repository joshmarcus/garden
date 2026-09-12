---
id: CG-490
title: Remove redundant two-review-round automerge hold for hard tasks
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/review.py
- tests/test_automerge.py
- tests/test_review.py
branch: garden/cg-490-remove-redundant-two-review-round-automerge-hold
pr: https://github.com/joshmarcus/context-garden/pull/403
attempts: 1
last_dispatched_at: '2026-09-10T01:51:47+00:00'
created: '2026-09-09T17:01:11+00:00'
updated: '2026-09-10T02:05:26+00:00'
---

## Goal

Allow an approved current-head hard task to merge once applicable CI passes and a fresh conflict check is clean, without requiring a redundant second automated review solely because the task is hard.

## Context

Observed in RC13 c42bf592e3943fd54a1186e818cc6324596041f1: CG-487/PR388 and CG-488/PR386 each had an approving verdict and one review round, but automerge_blocked said only 1 review round(s) so far, need 2. In src/garden/scheduler/poll.py, _automerge_gate unconditionally applies max(min_rounds, 2) for hard-tier tasks. This overrides a configured minimum of one and was missed by the clean-head policy change. Review scheduling/recovery must agree with the merge gate. GitHub issue #392 was filed in error and closed at owner request; this native task is the intended record.

## Acceptance criteria

- [ ] A hard task with one valid current-head approval and a configured minimum of one can merge after other applicable gates pass.
- [ ] An explicitly configured higher review minimum remains respected; task difficulty alone does not silently raise it.
- [ ] Review scheduling does not queue an extra round solely to satisfy the removed implicit hard-tier floor.
- [ ] Current-head approval provenance, failed applicable CI, substantive findings, pending revision feedback, explicit holds, fresh conflict checks, serialized merges and atomic head guards retain their existing protections.
- [ ] Focused regressions cover the merge gate and affected scheduling; no historical review/revision counters or approvals are reset or fabricated.
## Out of scope

- ...

## Suggestions

- [x] 2026-09-09 web (applies to reading): Set the reading list to src/garden/scheduler/poll.py, src/garden/scheduler/review.py, tests/test_automerge.py, and tests/test_review.py. These are the merge-gate, review-scheduling, and regression files named by the task context and acceptance criteria.

## Log

- 2026-09-09T17:38:53+00:00 approved (web)
- 2026-09-09T17:52:55+00:00 integrated 1 suggestion(s) (run 20260909T175124Z-edit) cost=$0.06
- 2026-09-09T21:45:43+00:00 dispatched work run 20260909T214540Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~18952 tokens)
- 2026-09-09T21:49:03+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T21:50:16+00:00 opened https://github.com/joshmarcus/context-garden/pull/403 (base main): Hard-tier automerge now honors the configured review minimum while retaining its scratch-merge gate. Review-recovery scheduling uses the same policy; focused automerge/review tests (150 passed) and Ruff passed on commit 653d5401. cost=$0.46
- 2026-09-09T21:52:45+00:00 automated review: approve — Hard-tier automerge and review recovery now consistently honor the configured review minimum without weakening surrounding merge protections. cost=$0.32
- 2026-09-10T01:49:32+00:00 triage: changes requested by hand: Exact-head full CI fails test_hard_tier_needs_two_rounds and test_hard_tier_one_round_never_dispatches_a_scratch_check b
- 2026-09-10T01:51:47+00:00 dispatched revise run 20260910T015143Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~19735 tokens)
- 2026-09-10T01:55:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:56:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/403: Updated stale hard-tier merge regressions on c718bb339816fe8288276e8fd6dccf52d1b2dcd3 to follow the configured review minimum while preserving scratch-merge coverage. Focused automerge/review tests passed (160); Ruff passed. No typecheck command is configured; macOS was not exercised in this Linux environment. cost=$0.40
- 2026-09-10T01:59:09+00:00 automated review: approve — Hard-tier automerge and review recovery consistently honor the configured review minimum while preserving existing merge protections. cost=$0.33
- 2026-09-10T02:05:26+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/403
