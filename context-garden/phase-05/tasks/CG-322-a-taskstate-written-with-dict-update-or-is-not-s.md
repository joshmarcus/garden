---
id: CG-322
title: A _TaskState written with dict.update or |= is not saved
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/state.py
- tests/test_state.py
branch: garden/cg-322-a-taskstate-written-with-dict-update-or-is-not-s
pr: https://github.com/joshmarcus/context-garden/pull/257
discovered_from: CG-308
attempts: 1
last_dispatched_at: '2026-09-07T03:45:20+00:00'
created: '2026-09-06T03:36:56+00:00'
updated: '2026-09-07T15:18:09+00:00'
---

## Goal

`scheduler/state.py`'s `_TaskState` tracks dirty keys through `__setitem__`, `pop` and `setdefault`, so `st.update({...})` or `st |= {...}` changes the in-memory dict but `State.save()` never writes those keys. Either override `update` (and `__ior__`, `clear`) to mark keys written, or make the class refuse them with a clear error.

## Context

Found while writing the Now 1 tests: a merge-queue head set with `update` never reached state.json. No production code path uses `update` today, but the next one will lose a write silently.

## Provenance

Discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) during run `20260906T025753Z-work`.

## Log

- 2026-09-06T03:36:56+00:00 discovered by CG-308

## Acceptance criteria

- [ ] All supported dict mutators persist their changes through State.save and retain concurrent disjoint updates; regression tests cover update, |= and deletion via clear. Unsupported mutators fail explicitly rather than silently losing writes.
- 2026-09-06T13:20:31+00:00 approved (cli)
- 2026-09-06T20:29:27+00:00 dispatched work run 20260906T202905Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~13526 tokens)
- 2026-09-06T20:37:20+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit c1f75cb08e47, not because of this branch; waiting for the base to go green, no revise round cost=$0.02

20:40 operator diagnosis: the original base probe was terminated(SIGTERM), so it did not prove main broken. A fresh detached checkout of c1f75cb08e47 at /home/joshua/work/operator-test-tmp/base-check-2039 passed exactly tests/scheduler/test_reap.py::test_failed_rebase_retries_then_parks_without_restarting_work (1 passed, .88s, bounded CPU100%/512MiB). The same test failed on this branch after106 passes. Investigate branch State mutator effects on retry state; do not restart implementation from scratch or blame main on the interrupted probe. Full base suite not rerun; claim only the specific reproduced comparison.
- 2026-09-06T20:40:08+00:00 nothing to fix; needs-human stop cleared by hand
- 2026-09-06T20:40:31+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-322`) or send it back (`garden triage CG-322 --changes "..."`)


## Operator continuation decision

Preserve the existing dirty-tracking implementation/worktree; this is a pre-PR repair, not work to restart. Refresh against current main. The recorded branch regression was tests/scheduler/test_reap.py::test_failed_rebase_retries_then_parks_without_restarting_work: the stop reason lost the original rebase-conflict context when a runner lacked GARDEN_RESULT. A bounded same-base comparison passed on clean c1f75cb and failed on this branch; the killed full base probe did not prove broken main. Determine whether the new state mutator semantics expose stale update ordering and fix the actual behavior or stale assertion using current code evidence. Keep update/ior/clear/del/popitem and concurrent disjoint-key persistence coverage. No open PR exists yet. Focused local checks only; exact-head full CI on GitHub once committed/pushed.
- 2026-09-07T02:18:45+00:00 Owner delegated human-queue resolution: retain implementation and queue targeted pre-PR regression repair; clear lost-feedback stall through supported retry.
- 2026-09-07T02:18:48+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T03:00:27+00:00 dispatched revise run 20260907T030025Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~15207 tokens)
- 2026-09-07T03:08:39+00:00 preserved uncommitted worktree changes from run 20260907T030025Z-revise outside the PR: `git stash apply d415796103e8f3301a5005ebaa6188480b1362f8` in /home/joshua/work/worktrees/CG-322 (garden:CG-322:20260907T030025Z-revise:reap)
- 2026-09-07T03:23:20+00:00 opened https://github.com/joshmarcus/context-garden/pull/257 (base main): TaskState dict mutators now persist correctly with concurrent disjoint updates preserved. Regression coverage passes locally and exact-head GitHub CI succeeded. cost=$0.06
- 2026-09-07T03:25:39+00:00 automated review requested changes: The TaskState mutator fix meets its acceptance criterion and focused tests plus exact-head CI pass. The PR must not merge with the unrelated 67k-line runtime snapshot rewrite and unclean leftover-work commit. cost=$0.33
- 2026-09-07T03:32:44+00:00 dispatched revise run 20260907T033242Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~15911 tokens)
- 2026-09-07T03:41:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/257: TaskState mutators now persist updates and deletions while preserving concurrent disjoint writes. Removed the unrelated generated snapshot and preserved rebase-conflict context. cost=$0.04
- 2026-09-07T03:44:27+00:00 automated review requested changes: The mutator implementation behaves correctly in inspection and all 25 focused tests pass, but the required regression coverage can pass even if update or |= dirty tracking is removed because clear() subsequently marks those keys dirty. The branch also retains leftover-work and cleanup commit messages in its final history. cost=$0.25
- 2026-09-07T03:45:20+00:00 dispatched revise run 20260907T034518Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~16038 tokens)
- 2026-09-07T03:58:31+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/257: TaskState dict mutators now persist updates and deletions while preserving concurrent disjoint writes. Independent regression tests prove update and |= persistence separately, and the clean replacement branch passed exact-head CI. cost=$0.05
- 2026-09-07T04:00:20+00:00 automated review: approve — The exact PR head correctly persists all TaskState mutators, preserves concurrent disjoint writes, and passes all 28 focused tests. cost=$0.34
- 2026-09-07T04:01:08+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T04:09:29+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/257
- 2026-09-07T15:18:09+00:00 automated review could not start: CG-322 is done: #257 was merged at 04:09:29
