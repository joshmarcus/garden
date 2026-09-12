---
id: CG-619
title: Repair run-reference cleanup and SSH capture CI failures
status: done
product: context-garden
phase: phase-05
depends_on: []
kind: bug
priority: 0
difficulty: hard
reading:
- context-garden/phase-05/docs/cg619-ci-prefix-diagnosis.md
- src/garden/runs.py
branch: codex/fix-cleanup-run-id-prefix
pr: https://github.com/joshmarcus/context-garden/pull/482
runner: remote
discovered_from: CG-617
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-11T02:39:16+00:00'
created: '2026-09-11T02:21:09+00:00'
updated: '2026-09-11T03:18:15+00:00'
---

## Goal

Match complete recorded run identities in branch-cleanup recovery guards so a suffixed run ID does not claim its shorter-prefix sibling. Preserve genuine recovery ownership and every existing deletion safeguard.

## Failure and diagnosis

Actual exact-source CI34552728651 for PR480/head8e4321c8 failed tests/test_storage_cleanup.py::test_completed_worktree_is_removed_before_its_branch: expected removable, observed needed because scheduler recovery state still references a run on the branch. 2753 tests passed,4 skipped,4 deselected. PR CI34552732248 failed its exact-push gate. Original logs are preserved under rc19-deploy-20260910/cg617-ci34552728651-failed.log.

branch_cleanup.py and the failing cleanup test are unchanged by CG617 and already in accepted main base780caa01e9c22521044553cee54cc478a517419f. classify_branches currently tests whether run.run_id is a substring of serialized scheduler state. RunStore.next_run_id makes same-second IDs globally distinct using -2,-3 suffixes. A pointer to 20260911T020516Z-work-2 therefore also falsely matches 20260911T020516Z-work. This explains the timing-sensitive assertion and false recovery holds.

Distinct owners remain CG599 bounded remote-reference discovery, CG600 final-output handoff, CG601 inherited pytest options and CG617 writable local harness state. Preserve their source and original failures. Josh asked whether we should assist the local-startup repair; root is taking this narrow CI correction directly while the existing617 review/rebase finishes.

## Acceptance criteria

- [ ] Match the complete recorded run identity. A pointer to a longer suffixed ID must not keep its shorter-prefix sibling's branch. No sleeps, timestamp assumptions, lucky CI reruns or weakening the failing assertion.
- [ ] Preserve real references in nested state and recorded recovery/backup representations, including escaped literal IDs. Active/queued work, manual/external ownership, PR/stack/protected branches and unpreserved source keep their existing guards. Do not delete live branches or worktrees.
- [ ] Add deterministic prefix-related run IDs proving the referenced branch stays needed and the unrelated fully preserved shorter-prefix branch becomes eligible. Verify the completed-worktree-before-branch integration, focused branch/storage cleanup suites and Ruff, then actual exact-source CI and independent review.
- [ ] Use portable Python and disposable fake repositories. Report Linux, macOS and Windows-through-WSL coverage accurately. Preserve runtime, source history, fleet/caps and browser policy; this is a source correction, not a live cleanup operation.

## Boundaries

Root owns this manual implementation and the requested RC pipeline. Attach the resulting external PR through supported native completion for independent review. No direct set-done. This repairs a reproduced CI defect; no acceptance or security waiver is inferred.


The older cached reading index lacks the newer cleanup modules. Use the exact accepted-source paths and red/green evidence in the context diagnosis document; the original four source/test paths remain mandatory task-specific inspection in the actual checkout.

## Log

- 2026-09-11T02:26:57+00:00 approved (operator: owner requested direct assistance; actual CI prefix defect)
- 2026-09-11T02:39:16+00:00 dispatched work run 20260911T023916Z-work via manual [human] (fresh session, base main, ~15674 tokens)
- 2026-09-11T02:39:16+00:00 Root direct-assistance source is PR482 at672802f8. The four deterministic cases failed on unmodified main;35 focused cleanup tests now pass, including backup/stash/artifact/note references and literal IDs. Manual source reservation waits for actual current CI before independent remote review; no author rerun and no direct set-done.
- 2026-09-11T02:56:14+00:00 The first source672802 passed one full CI but pushCI34555004197 failed the SSH revision capture test: DM001 revise and DM002 work both wrote revision-context.txt, producing the second task context. Root isolates the single-revision fixture by keeping the unrelated dependent draft and asserts only DM001 is dispatched. Exact adverse finding assertions remain; no runtime change or live cleanup. This is direct continuation of the existing manual PR482 branch and claim, which supports advancing an open PR head. Original mixed CI evidence is preserved.
- 2026-09-11T03:09:59+00:00 Root CI correction is complete at69d903ac. Exact current GitHub CI passed before requesting independent remote review. Preserve deterministic original red cases,125 focused passes, original failed source CI and unchanged actual recovery guards; this manual source attachment has no invented model cost.
- 2026-09-11T03:10:00+00:00 external PR attached at codex/fix-cleanup-run-id-prefix; existing CI is SUCCESS
- 2026-09-11T03:16:21+00:00 automated review: approve — The run-reference boundary match fixes the suffixed-ID collision without weakening existing cleanup safeguards, and the SSH fixture is deterministically isolated to its intended revision task. cost=$0.26
- 2026-09-11T03:18:08+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T03:18:15+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/482
