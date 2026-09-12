---
id: CG-459
title: Pin remote base probes to the advertised base source
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/checkruns.py
- src/garden/runner/remote.py
- src/garden/remote_worker.py
- src/garden/web/pages/api.py
- src/garden/runs.py
- tests/scheduler/test_reap.py
- tests/test_branch_coordination.py
- tests/test_remote_worker.py
- docs/worker-protocol.md
branch: garden/cg-459-pin-remote-base-probes-to-the-advertised-base-so
pr: https://github.com/joshmarcus/context-garden/pull/356
runner: remote
discovered_from: CG-428
attempts: 1
last_dispatched_at: '2026-09-09T12:03:31+00:00'
created: '2026-09-09T00:20:56+00:00'
updated: '2026-09-09T12:13:33+00:00'
file: src/garden/scheduler/checkruns.py
error: A base probe advertised main but executed branch head 542a3eb7e858f8ab8c5a90b077f957fc4c3e51df.
---

Ensure remote base-probe runs materialize and report the advertised base commit rather than inheriting the task branch checkout. The CG-428 probe labeled as main recorded the task branch head for both start_head and pushed_head, making its base-health conclusion invalid.

## Provenance

Discovered by CG-428 (Keep remote worker runs alive across controller redeploys) during run `20260909T001659Z-revise`.
## Log
- 2026-09-09T00:20:56+00:00 discovered by CG-428

## Acceptance criteria

- [ ] A remote base probe carries an immutable advertised base revision and actually materializes that revision, with start_head and returned source identity matching the advertised base instead of the task branch. Normal task-branch execution and result publication retain their existing behavior.
- [ ] Before applying a base-health conclusion, compare advertised and executed source identity. A mismatch is a concrete verification/provenance failure and cannot classify main as broken or silently rewrite the task branch. Preserve the failed branch result and original probe evidence.
- [ ] Add a bounded temporary-Git regression with distinct base/branch marker contents through the actual remote check materialization/executor path. Verify the base command reads base content and both actual source receipts match it; cover an unavailable or mismatched revision without mutating the author branch.
- [ ] Use focused parser/runner/check regressions and source/command receipts proportionate to this check-routing change. No generic application empty/failure/recovery matrix, new AWS host, or stress suite is required.

## Operator scope clarification 2026-09-09T01:05:16.732720+00:00

Original CG428 checks234759 and234907 both executed542a3eb7 while the second advertised base6fb64db8; original logs are retained under input-sweep-20260908T2125. CG428 already corrected its separate branch-only unused import/assignment. This existing discovered ticket is the single owner of base-probe source pinning.
- 2026-09-09T01:05:17+00:00 approved (delegated-operator-proportionate-verification)
- 2026-09-09T01:05:48+00:00 dispatched work run 20260909T010548Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~23618 tokens)
- 2026-09-09T01:48:30+00:00 pre-PR checks failed (UI captures); no PR opened yet; revise run will fix cost=$1.08
- 2026-09-09T01:49:12+00:00 dispatched revise run 20260909T014911Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~23790 tokens)
- 2026-09-09T02:15:07+00:00 check did not run (20260909T015402Z-check): idle 21 min (no output or file change); will retry
- 2026-09-09T02:27:03+00:00 opened https://github.com/joshmarcus/context-garden/pull/356 (base main): Pinned remote base-probe implementation remains intact, and the pre-PR capture classifier no longer mistakes its JSON API endpoint change for a rendered UI change. Committed as 4022607e. cost=$0.61
- 2026-09-09T02:52:57+00:00 automated review:  —
- 2026-09-09T05:11:08+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-09T09:42:45+00:00 dispatched rebase run 20260909T094245Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1259 tokens)
- 2026-09-09T09:45:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/356: Rebased onto origin/main and merged the conflicting remote-worker regression tests. cost=$0.01
- 2026-09-09T09:50:00+00:00 automated review: approve — Remote base probes are pinned to the advertised immutable revision, and provenance mismatches cannot produce a base-health conclusion or mutate the author branch. cost=$0.63
- 2026-09-09T12:03:19+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/checkruns.py); a rebase agent will resolve it
- 2026-09-09T12:03:31+00:00 dispatched rebase run 20260909T120331Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1449 tokens)
- 2026-09-09T12:05:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/356: Rebased onto origin/main and resolved the checkruns.py conflict while preserving both main’s CI head snapshot and the PR’s durable advertised source head. cost=$0.01
- 2026-09-09T12:09:23+00:00 automated review: approve — Remote base probes are pinned to the advertised commit, and mismatched provenance cannot classify the base as broken or alter the author branch. cost=$0.47
- 2026-09-09T12:13:33+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/356
