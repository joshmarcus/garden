---
id: CG-360
title: Keep restored archived runs visible when directory fingerprints do not change
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
branch: codex/cg-360-restore-index
pr: https://github.com/joshmarcus/context-garden/pull/242
runner: manual
attempts: 1
last_dispatched_at: '2026-09-06T22:01:27+00:00'
created: '2026-09-06T21:28:37+00:00'
updated: '2026-09-06T22:23:09+00:00'
---

## Goal

After restoring an archived run, every reader immediately sees the restored record and correct totals, including on ext4 and when filesystem freshness signals collide.

## Evidence

Owner-requested tmpfs/ext4 full-suite comparison at main c1f75cb: tmpfs1181passed/3skipped; ext4 failed tests/test_run_index.py::test_archive_round_trip_preserves_summary_and_artifacts at line69, rs.all_runs()[0] IndexError immediately after restore_archived returnedTrue. Independent ext4 rerun of tests/test_run_index.py reproduced1failed/6passed. See context-garden/docs/incidents/test-temp-ab/README.md and raw logs in /home/joshua/work/operator-test-tmp/io-ab-20260906.

Current restore_archived moves the directory, rebuilds archive index and calls generic invalidate, while incremental refresh selects changed task buckets from directory fingerprints. Suspect insufficient explicit task-bucket invalidation when archive/restore occurs within filesystem timestamp granularity; verify rather than assume. No production archive was operated on. Preserve records; this is a visibility/consistency failure, not established data deletion.

## Acceptance criteria

- [ ] Reproduce and explain the failure on disk-backed temp; verify restored physical artifacts and index/total behavior before and after expiry.
- [ ] Archive, restore and metadata correction explicitly invalidate the affected live/archive state without relying exclusively on directory timestamps. Preserve bounded ordinary reads and concurrent mutation correctness.
- [ ] Deterministic regression with unchanged/colliding directory fingerprints verifies immediate visibility, exactly one run, intact artifacts and unchanged cost through archive/restore, fresh RunStore and cache expiry.
- [ ] Focused tests pass with tmpfs and ext4 temp, followed by relevant full CI. No production archive changes during testing.

## Priority

Priority0 correctness follow-up to CG-357. Until verified, do not recommend production archive/restore as an operational memory mitigation.

## Log

- 2026-09-06T21:49:07+00:00 Owner authorized direct implementation in the operator session alongside the one recovery worker. Operator owns CG-360; runner manual prevents duplicate dispatch. Tests will remain serial.
- 2026-09-06T22:01:27+00:00 dispatched work run 20260906T220127Z-work via manual [human] (fresh session, base main, ~8763 tokens)
- 2026-09-06T22:18:46+00:00 git guard: the clone's git internals changed since dispatch: worktree .git (/home/joshua/work/worktrees/CG-360/.git), worktree .git/worktrees/<id> (/home/joshua/work/repos/context-garden/.git/worktrees/CG-360); every git command in this clone is refused until it is recreated by hand
- 2026-09-06T22:23:09+00:00 PR242 merged44b9a312 verified by ancestry after final CI1201passed/3skipped and focused ext4/tmpfs checks. Restored original operator worktree path, verified every git-guard hash matches the dispatch snapshot, archived the resolved operator-move block and corrected the actual PR branch. The manual completion attempt remains an honest failed bookkeeping run. Source fix is merged; deployment pending worker drain.
