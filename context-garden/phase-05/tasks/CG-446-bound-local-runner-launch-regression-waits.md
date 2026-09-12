---
id: CG-446
title: Bound validation and check execution time
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: -104
difficulty: medium
reading:
- src/garden/validation.py
- src/garden/run_supervisor.py
- src/garden/runner/local.py
- src/garden/remote_worker.py
- src/garden/scheduler/checkruns.py
- tests/test_runners.py
branch: codex/bounded-validation-runtime
pr: https://github.com/joshmarcus/context-garden/pull/342
runner: local
discovered_from: CG-438
last_dispatched_at: '2026-09-08T20:59:58+00:00'
created: '2026-09-08T17:49:27+00:00'
updated: '2026-09-08T21:23:36+00:00'
file: tests/test_runners.py
error: Full suite and combined focused runner suite stalled indefinitely around `test_local_runner_launch_flips...`.
---

The ordinary suite stalled in the local runner launch test with a `run_supervisor ... sleep 0.5; cat` process still waiting more than twelve minutes. Give the regression a bounded failure path and diagnose why the brief/input stream remained open.

## Provenance

Discovered by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) during run `20260908T170122Z-work`.
## Log
- 2026-09-08T17:49:27+00:00 discovered by CG-438


## Expanded owner runtime policy 2026-09-08T18:48:27.507724+00:00

Owner requests120seconds per ordinary test and hard900seconds per validation command. Preserve parent model execution, owned descendant cleanup/logs, exact timeout status and slot release; admission waiting must not silently consume running-time budget. This task owns general enforcement beyond the already-merged CG433 stdin-hang repair; coordinate CG412/413 product check/execution timeout settings rather than duplicating them. Operator Sol implementation will use codex/bounded-validation-runtime; do not launch another author.


## Completed Sol implementation

Exact source dd7c5aeeba734245a649163888a2fc2e8be467cb in https://github.com/joshmarcus/context-garden/pull/342 implements the120spertest/900shardvalidation policy, current local/SSH/remote propagation, preserved timeout/output records, parent-model survival and safe descendant/slot cleanup.83runner/remote tests passed35.96s;8scope tests7.35s; actualreap-race node.90s; Ruff/diffchecks passed under the real validation wrapper. Independent Sol peer review is underway; full exact CI is required. No production install yet.
- 2026-09-08T19:46:01+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/342 (pr_number none -> 342)
- 2026-09-08T19:46:22+00:00 PR conflicts with main; rebase onto main conflicts (git worktree add /home/joshua/work/worktrees/CG-446 codex/bounded-validation-runtime (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/bounded-validation-runtime')
fatal: 'codex/bounded-validation-runtime' is already used by worktree at '/home/joshua/work/operator-test-tmp/test-timeouts-sol'); a rebase agent will resolve it
- 2026-09-08T19:47:40+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-446 codex/bounded-validation-runtime (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/bounded-validation-runtime')
fatal: 'codex/bounded-validation-runtime' is already used by worktree at '/home/joshua/work/operator-test-tmp/test-timeouts-sol'
- 2026-09-08T20:39:56+00:00 triage: marked ready for review (Current68190007 clean and two exact-head CI successes; operator checkout detached, previous merge co)
- 2026-09-08T20:46:16+00:00 automated review requested changes: The timeout implementation passes lint and 132 focused tests, but the head deletes two regression tests—including admission/idle behavior directly adjacent to this change—and the supplied served replay does not exercise validation timeout behavior. cost=$0.44


## Authoritative owner decision and current evidence

Owner explicitly requested removal of test_real_check_waits_for_lease_then_runs_once_and_silent_process_times_out and test_stacked_runs_never_collide_into_the_same_commit at2026-09-08T19:58:57Z. The removal in68190007 is intentional approved scope. A generic rule to retain every existing test must not reverse that decision; evaluate retained deterministic coverage and actual defects. No source defect was found by the204229 reviewer, who passed132focused tests. Its genuine affected-journey gap is now filled by /home/joshua/work/operator-test-tmp/emergency-merges-20260908/cg446-review-interaction.json and the underlying immutable receipts.

## Acceptance criteria

- [ ] Enforce120seconds per ordinary test and at most900seconds per executing validation/check across local,SSH and pull workers; keep parent model execution and admission waiting separate.
- [ ] Preserve truthful timeout status, exact failure reason and available logs/receipts; terminate owned descendants and retain slot ownership until cleanup, then allow subsequent work.
- [ ] Retain meaningful deterministic timeout,admission,ownership and cleanup coverage while honoring the owner-approved removal of the two named flaky tests.
- [ ] Verify the affected validation/check lifecycle using bounded actual process execution and the changed HTTP claim boundary; use synthetic local credentials and a disposable fixture, with current-head source references and full CI.
- 2026-09-08T20:59:58+00:00 dispatched revise run 20260908T205958Z-revise via manual [human] (fresh session, base main, ~23309 tokens)
- 2026-09-08T20:59:59+00:00 external PR attached at codex/bounded-validation-runtime; existing CI is SUCCESS
- 2026-09-08T21:06:03+00:00 description rewritten by the reviewer cost=$0.73
- 2026-09-08T21:06:26+00:00 rebasing before merge; rebase onto main conflicts (src/garden/remote_worker.py, src/garden/web/pages/api.py); a rebase agent will resolve it
- 2026-09-08T21:10:20+00:00 automated review: approve — The reviewed head enforces bounded post-admission validation/check execution across local, SSH, and pull workers while preserving timeout evidence, descendant cleanup, parent sessions, and slot reuse. Focused validation passed 132 tests, lint passed, and the exact-head disposable HTTP lifecycle and CI receipts are consistent with the implementation. cost=$0.59
- 2026-09-08T21:20:50+00:00 triage: marked ready for review (Verified published68190007 already contains currentorigin/main020eced, current reviewed diff unchang)
- 2026-09-08T21:23:36+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/342
