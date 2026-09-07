---
id: CG-322
title: A _TaskState written with dict.update or |= is not saved
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/state.py
- tests/test_state.py
branch: garden/cg-322-a-taskstate-written-with-dict-update-or-is-not-s
discovered_from: CG-308
attempts: 1
last_dispatched_at: '2026-09-06T20:29:27+00:00'
created: '2026-09-06T03:36:56+00:00'
updated: '2026-09-07T02:18:48+00:00'
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
