---
id: CG-090
title: State.save() never clears dirty keys after a successful write
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
branch: garden/cg-090-state-save-never-clears-dirty-keys-after-a-succe
pr: https://github.com/joshmarcus/context-garden/pull/52
discovered_from: CG-082
attempts: 1
last_dispatched_at: '2026-09-04T21:32:33+00:00'
created: '2026-09-04T19:55:45+00:00'
updated: '2026-09-04T22:02:58+00:00'
---

In `src/garden/scheduler.py`, `_TaskState` (from CG-053) marks keys dirty on write/mutation-prone read, and `State.save()` merges only dirty keys into the on-disk file — but never clears the in-memory dirty set after a successful save. Every subsequent `save()` call re-writes all previously-dirty keys with their current in-memory values, which can silently clobber a concurrent writer's later update to the same key. Needs a fix in `State.save()` to clear each `_TaskState`'s dirty set (or just the keys it wrote) after the write succeeds.

## Provenance

Discovered by CG-082 (Separate GARDEN_ROOT (guard) from the check-command venv path variable) during run `20260904T195040Z-revise`.

## Log

- 2026-09-04T19:55:45+00:00 discovered by CG-082
- 2026-09-04T20:16:13+00:00 approved (web)
- 2026-09-04T20:55:51+00:00 dispatched work run 20260904T205550Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8496 tokens)
- 2026-09-04T20:58:55+00:00 pre-PR checks failed (tests, lint); no PR opened yet; revise run will fix cost=$1.24
- 2026-09-04T20:58:56+00:00 dispatched revise run 20260904T205855Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8723 tokens)
- 2026-09-04T21:03:37+00:00 discovered work filed: CG-097
- 2026-09-04T21:03:39+00:00 pre-PR checks failed (tests); no PR opened yet; revise run will fix cost=$1.30
- 2026-09-04T21:05:43+00:00 dispatched revise run 20260904T210543Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~9261 tokens)
- 2026-09-04T21:10:52+00:00 discovered work filed: CG-101
- 2026-09-04T21:11:00+00:00 pre-PR checks failed (tests); no PR opened yet; revise run will fix cost=$1.39
- 2026-09-04T21:19:42+00:00 reset to ready by hand
- 2026-09-04T21:24:18+00:00 dispatched work run 20260904T212417Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8723 tokens)
- 2026-09-04T21:26:44+00:00 opened https://github.com/joshmarcus/context-garden/pull/52 (base main): State.save() already clears each _TaskState's dirty set after a successful write (scheduler.py, commit 5544f4a), with a regression test guarding against re-clobbering a concurrent writer's update (test_state.py), plus a test-isolation fix for ambient GARDEN_ROOT leakage (commit 7f973a2). Verified: 220 passed/3 skipped in pytest, ruff clean. cost=$0.58
- 2026-09-04T21:26:52+00:00 PR conflicts with main (src/garden/scheduler.py); revise run will rebase and resolve
- 2026-09-04T21:27:55+00:00 automated review: approve — State.save() now clears each _TaskState's dirty set after a successful write (via live set references), backed by a regression test for the clobber scenario; a justified conftest fix isolates tests from the ambient GARDEN_ROOT. Tests and lint pass. cost=$0.47
- 2026-09-04T21:27:57+00:00 dispatched revise run 20260904T212757Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~9189 tokens)
- 2026-09-04T21:31:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/52: Rebased branch onto main, resolving the scheduler.py conflict by keeping main's atomic os.replace() write and layering the dirty-key-clear fix on top; dropped the now-redundant conftest.py commit since main already carries the identical ambient-GARDEN_ROOT fix from CG-101. Tests (239 passed, 3 skipped) and ruff pass. cost=$1.50
- 2026-09-04T21:32:32+00:00 automated review requested changes: The fix correctly clears each _TaskState's dirty set after a successful atomic write and is well-tested against the clobber scenario; acceptance criteria are fully met. The only blocker is the PR description's '## Review responses' section, which narrates the rebase and a dropped commit — scar tissue that must be removed. cost=$0.37
- 2026-09-04T21:32:33+00:00 dispatched revise run 20260904T213233Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~9723 tokens)
- 2026-09-04T21:34:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/52: No code changes needed this round: State.save() already clears each _TaskState's dirty set after a successful write (b09845e), with a regression test guarding the clobber scenario. Rewrote the PR description to drop the '## Review responses' section that narrated the rebase/dropped-commit history, per reviewer feedback. cost=$0.42
- 2026-09-04T22:02:58+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/52
