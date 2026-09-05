---
id: CG-204
title: 'Test debt from phase 03: a shared contract for the two GitHub fakes, real LocalRunner coverage,
  event-based assertions, and the state store''s dict.get snapshot'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 3
difficulty: medium
reading: []
created: '2026-09-05T10:30:01+00:00'
updated: '2026-09-05T10:30:01+00:00'
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

