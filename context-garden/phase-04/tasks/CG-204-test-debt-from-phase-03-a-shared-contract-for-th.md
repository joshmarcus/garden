---
id: CG-204
title: 'Test debt from phase 03: a shared contract for the two GitHub fakes, real LocalRunner coverage,
  event-based assertions, and the state store''s dict.get snapshot'
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: medium
reading: []
branch: garden/cg-204-test-debt-from-phase-03-a-shared-contract-for-th
last_dispatched_at: '2026-09-05T13:18:09+00:00'
created: '2026-09-05T10:30:01+00:00'
updated: '2026-09-05T14:33:49+00:00'
---

## Goal

`FakeGitHub` and `MemoryGitHub` imitate GitHub with no shared contract (`MemoryGitHub` lacks `reopen_pr` and `branch_exists`); the real `LocalRunner.launch` shell wrapper and pid-based `process_finished` are covered only by two Popen-stubbed tests; several new tests assert on task-log prose where an event carries the same fact; `_TaskState.__getitem__` snapshots mutable values but `dict.get` is not overridden, so an in-place mutation of a value read through `.get` is not written back.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (staff-engineer:medium, staff-engineer:low, staff-engineer:low, staff-engineer:low); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] One `GitHubLike` protocol both fakes implement, with a shared test that runs the same scenarios against both.
- [ ] One test starts a real `LocalRunner` with a tiny script and sees `process_finished` flip.
- [ ] The prose assertions named in the staff engineer's review assert on events instead.
- [ ] `_TaskState.get` snapshots like `__getitem__`; a test mutates a value read through `.get` and sees it saved.

## Log

- 2026-09-05T10:31:19+00:00 approved (web)
- 2026-09-05T13:16:43+00:00 dispatched work run 20260905T131635Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4502 tokens)
- 2026-09-05T13:17:49+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:18:09+00:00 dispatched work run 20260905T131809Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4603 tokens)
- 2026-09-05T13:19:15+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:49+00:00 reset to ready by hand
