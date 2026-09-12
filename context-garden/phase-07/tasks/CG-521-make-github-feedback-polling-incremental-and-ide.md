---
id: CG-521
title: Make GitHub feedback polling incremental and identity-safe
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/github.py
- src/garden/scheduler/poll.py
- tests/test_github_feedback.py
- tests/scheduler/test_poll.py
branch: garden/cg-521-make-github-feedback-polling-incremental-and-ide
pr: https://github.com/joshmarcus/context-garden/pull/437
runner: remote
discovered_from: CG-503
attempts: 1
last_dispatched_at: '2026-09-10T13:16:57+00:00'
created: '2026-09-10T11:25:38+00:00'
updated: '2026-09-10T13:33:50+00:00'
file: src/garden/github.py
error: Routine polling passes an empty cursor and rereads complete reviews, line comments, and issue comments
  for every open PR each tick.
---

Reduce routine scheduler polling from three fully paginated feedback reads per open PR while preserving trusted-author filtering, bot notices, equal-timestamp comments, stable-ID deduplication, restart behavior, and provider-failure recovery. Compare provider command/page counts on the same unchanged-history workload and retain complete feedback retrieval for explicit investigations.

## Provenance

Discovered by CG-503 (Find removable and overengineered code to simplify and optimize) during run `20260910T111342Z-work`.
## Log
- 2026-09-10T11:25:38+00:00 discovered by CG-503

## Acceptance criteria

- [ ] Persist an identity-safe per-PR feedback cursor or equivalent high-water state that resumes after restart and retains equal-timestamp items through stable IDs.
- [ ] An unchanged open PR does not reread every page of reviews, line comments and issue comments on each tick; new comments across a pagination boundary are still observed exactly once.
- [ ] Trusted-author filtering, bot notices and provider-error behavior remain intact. A failed or partial fetch cannot advance the durable cursor or erase prior evidence, and explicit investigations can still request complete history.
- [ ] Compare provider command/page counts on the same unchanged-history workload before and after; cover restart, equal timestamps, new-page arrival, transient failure and full-history investigation in focused tests and run lint.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T12:52:11+00:00 dispatched work run 20260910T125210Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~18579 tokens)
- 2026-09-10T13:02:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:04:31+00:00 opened https://github.com/joshmarcus/context-garden/pull/437 (base main): Implemented and committed identity-safe incremental GitHub feedback polling in d656244a. Focused feedback/poll tests passed (50), and full requested lint passed. cost=$0.93
- 2026-09-10T13:07:37+00:00 automated review requested changes: The incremental cursor implementation is plausible and focused checks pass, but the frozen verification criterion is not met. cost=$0.26
- 2026-09-10T13:08:15+00:00 dispatched revise run 20260910T130815Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19547 tokens)
- 2026-09-10T13:12:14+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:13:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/437: Added provider-level regression coverage for unchanged-history page counts (6 full-history page reads versus 3 incremental requests) and a multi-page equal-timestamp review arrival that emits once after restart. Verified with focused feedback/poll tests (52 passed) and lint. cost=$0.41
- 2026-09-10T13:16:30+00:00 automated review requested changes: Incremental retrieval and identity deduplication are well covered, but the durable cursor can move backward on an unchanged PR, undermining incremental polling. cost=$0.27
- 2026-09-10T13:16:57+00:00 dispatched revise run 20260910T131657Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19964 tokens)
- 2026-09-10T13:19:36+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:20:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/437: Made the durable per-PR feedback cursor monotonic in both normal polling and CI-check feedback handling, with a regression test for an older-review-only response. Verified focused feedback/poll tests (53 passed) and lint on commit ace451e2. cost=$0.26
- 2026-09-10T13:23:52+00:00 automated review: approve — Incremental polling is identity-safe, cursor advancement is monotonic, and complete-history retrieval remains available. cost=$0.40
- 2026-09-10T13:33:50+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/437
