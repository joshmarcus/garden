---
id: CG-323
title: The worker pre-flights its PR against the review rubric, mechanical review items become pre-PR
  checks, and criteria are frozen at dispatch
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/brief.py
- src/garden/review.py
- src/garden/checks.py
- src/garden/checkrun.py
- src/garden/scheduler/review.py
- src/garden/scheduler/dispatch.py
- docs/worker-protocol.md
- tests/test_brief.py
- tests/test_review.py
branch: garden/cg-323-the-worker-pre-flights-its-pr-against-the-review
pr: https://github.com/joshmarcus/context-garden/pull/241
attempts: 1
last_dispatched_at: '2026-09-07T10:02:21+00:00'
created: '2026-09-06T03:59:37+00:00'
updated: '2026-09-07T14:27:18+00:00'
---

## Goal

A PR arrives at its first review already checked against what the reviewer will look for. The work and revise briefs end with the review rubric as a pre-flight the worker walks before writing its result: a test per criterion (or a stated reason there is none), lint clean, no conflict markers, captures at both widths for any UI change, a description in goal-and-outcome form with no history, the criteria addressed by name; the result block carries the pre-flight as a checklist with a line per item. Items a machine can judge (conflict markers, syntax, a UI diff with no captures, a missing description) become pre-PR checks that fail before any reviewer spends a round. The criteria a worker sees are frozen at dispatch: a change to the task file after dispatch reaches the worker as a revise note on the next round, and the reviewer judges the brief the worker had.

## Context

Owner, 2026-09-06 04:05Z: 'How can we reduce the number of review rounds?' Of 85 send-backs so far, 54 were on PRs whose criteria were all met, for the same recurring findings (no test for a criterion, conflict markers, narrative descriptions, unsandboxed HTML, no captures); several more came from criteria added or corrected after dispatch (the Now tasks, CG-212). Sol, reviewing one rung above the writer since 03:20Z, has sent back 11 of 11 PRs on such findings. The reviewer's rubric is in src/garden/review.py; the worker never sees it.

## Acceptance criteria

- [ ] The work and revise briefs include the review rubric as a pre-flight section and the GARDEN_RESULT block carries a pre_flight list with one entry per item and a status; a result missing the list is a mechanical changes_requested naming the missing items
- [ ] Pre-PR checks fail on conflict markers, a syntax error, a UI diff (templates, static, web pages) with no captures under the run, and an empty PR description, each with a one-line reason the revise brief carries
- [ ] The brief records the criteria text it was built from; a task-file change after dispatch is delivered as a revise note and the review brief shows the criteria the worker had, with the delta marked
- [ ] Tests: the pre-flight section renders; each mechanical check fails on its shape and passes on a clean diff; a criteria change after dispatch shows up as a note in the next revise brief
- [ ] Measured after a week in the retro: send-backs on findings-only PRs per merged task, before and after (the number this task exists to move)

- [ ] The work and revise briefs state that the run ends when the worker stops: long commands run in the foreground, nothing is backgrounded to await a notification, and the result is written only after the checks have returned (five Fable runs on 2026-09-06 ended 'waiting for the monitor' with their work committed and no result).

## Log
- 2026-09-06T03:59:39+00:00 approved (cli)
- 2026-09-06T05:25:22+00:00 dispatched work run 20260906T052256Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~28859 tokens)
- 2026-09-06T06:42:21+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 508a28c4fe30, not because of this branch; waiting for the base to go green, no revise round cost=$1.36
- 2026-09-06T07:18:11+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T08:57:54+00:00 dispatched revise run 20260906T085752Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~29428 tokens)
- 2026-09-06T09:49:41+00:00 pre-PR checks failed (test) (still failing after a rebase onto `main`); no PR opened yet; revise run will fix cost=$2.39
- 2026-09-06T10:36:05+00:00 dispatched revise run 20260906T103604Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9055 tokens)
- 2026-09-06T11:00:31+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 56af81dfcba5, not because of this branch; waiting for the base to go green, no revise round cost=$0.81
- 2026-09-06T11:26:56+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T11:47:30+00:00 dispatched revise run 20260906T114724Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~29917 tokens)
- 2026-09-06T12:52:43+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$2.01
- 2026-09-06T13:04:37+00:00 dispatched revise run 20260906T130433Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, rebase round 2 (not counted), ~9403 tokens)
- 2026-09-06T13:07:04+00:00 revision failed: no GARDEN_RESULT in worker output (see final.md)
- 2026-09-06T13:13:31+00:00 reset to ready by hand
- 2026-09-06T20:51:18+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply f8d7e2abd2650f03fdbf6a656ebf9deac7c09016` in /home/joshua/work/worktrees/CG-323 to recover them (garden:CG-323:2026-09-06T20:51:18+00:00)
- 2026-09-06T20:51:19+00:00 dispatched work run 20260906T205118Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9731 tokens)
- 2026-09-06T21:14:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/241 (base main): Workers receive and report a review pre-flight, mechanical defects stop before PR creation, and dispatched criteria remain the review contract even when later edits occur. cost=$1.65
- 2026-09-06T21:14:08+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/review.py, src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-06T21:16:19+00:00 automated review: request_changes — The core pre-flight works and focused tests pass, but criteria edits are lost when the first revise round originates from a pre-PR failure. The branch also includes a large unrelated generated snapshot. cost=$0.39
- 2026-09-07T01:22:50+00:00 dispatched rebase run 20260907T012248Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~15657 tokens)
- 2026-09-07T01:25:10+00:00 preserved uncommitted worktree changes from run 20260907T012248Z-rebase outside the PR: `git stash apply 0ca2b4100c9a37caabf967098700d5c9cae60c74` in /home/joshua/work/worktrees/CG-323 (garden:CG-323:20260907T012248Z-rebase:reap)
- 2026-09-07T01:26:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Rebased CG-323 onto origin/main and resolved all conflicts while preserving both sides' intent. cost=$0.03
- 2026-09-07T01:29:19+00:00 automated review requested changes: The pre-flight implementation and focused tests are largely sound, but criteria edits are still omitted when the next revise round is triggered by a pre-PR failure. The branch also retains a large unrelated generated snapshot rewrite. cost=$0.43
- 2026-09-07T01:29:31+00:00 dispatched revise run 20260907T012930Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~22442 tokens)
- 2026-09-07T01:39:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Retains criteria edits in the immediate revise brief after a mechanical pre-PR failure and removes the unrelated runtime snapshot from the branch diff. Full CI passed on 6b0c4724c7c22f66205393842d50ef1541d498f3. cost=$0.68
- 2026-09-07T01:41:24+00:00 automated review requested changes: The worker rubric, result gate, frozen criteria, revise delta, and focused coverage are present. The mechanical pre-PR implementation must fail closed when it cannot inspect the diff and must avoid modifying the checked worktree. cost=$0.45
- 2026-09-07T01:41:45+00:00 dispatched revise run 20260907T014143Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~22766 tokens)
- 2026-09-07T01:58:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Mechanical pre-flight now fails closed when Git cannot inspect the candidate and syntax validation leaves the worktree untouched. The unrelated snapshot delta is absent; focused tests, lint, and exact-commit CI pass. cost=$0.93
- 2026-09-07T02:00:15+00:00 automated review requested changes: The worker rubric, result gate, frozen criteria, and focused coverage are present, but mechanical failures do not reliably reach an automatic revise round and Git inspection still does not fully fail closed. cost=$0.49
- 2026-09-07T02:00:51+00:00 dispatched revise run 20260907T020049Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~23064 tokens)
- 2026-09-07T02:08:18+00:00 worker asks: Should missing-result recovery from current main continue directly to review, or should CG-323 require it to enter an automatic revise round for the missing pre-flight? cost=$1.04
- 2026-09-07T02:19:00+00:00 kept 4 local-only commit(s) on `backup/20260907T021858Z-resume` before syncing to origin/garden/cg-323-the-worker-pre-flights-its-pr-against-the-review's head: 7d20ecc Merge remote-tracking branch 'origin/main' into garden/cg-323-the-worker-pre-flights-its-pr-against-the-review; b84d521 fix: route mechanical pre-flight failures to revise; 061e71f Merge pull request #253 from joshmarcus/garden/cg-333-a-run-that-ends-without-a-result-but-with-new-co; b705093 Reap committed runs missing results
- 2026-09-07T02:19:05+00:00 dispatched resume run 20260907T021858Z-resume via local [codex model=gpt-5.6-terra] (fresh session, base main, ~22917 tokens)
- 2026-09-07T02:32:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Workers now receive, report, and are mechanically gated by the review pre-flight; dispatched criteria remain frozen. Missing results under the new contract preserve committed work and enter an automatic revise round with the required reason and frozen criteria. cost=$1.17
- 2026-09-07T02:32:53+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-323` for one more round, or review on GitHub
- 2026-09-07T02:37:54+00:00 triage: marked ready for review
- 2026-09-07T02:39:41+00:00 automated review requested changes: The rubric, result gate, frozen criteria, revise delta, and focused coverage are implemented. However, changed-file inspection can still raise outside the fail-closed mechanical checker, so a Git error may abort the tick instead of producing revise feedback. cost=$0.43
- 2026-09-07T02:40:09+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-323`) or send it back (`garden triage CG-323 --changes "..."`)
- 2026-09-07T02:44:13+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-07T03:00:29+00:00 dispatched revise run 20260907T030027Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~23654 tokens)
- 2026-09-07T03:11:00+00:00 preserved uncommitted worktree changes from run 20260907T030027Z-revise outside the PR: `git stash apply d2fc7e540ede8cc38e7b28181cee72d75250f16d` in /home/joshua/work/worktrees/CG-323 (garden:CG-323:20260907T030027Z-revise:reap)
- 2026-09-07T03:26:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Pre-PR changed-file inspection now fails closed into an automatic revise brief instead of aborting a scheduler tick. The guarded mechanical pre-flight remains the sole post-check diff inspector, with lifecycle coverage for the Git-error path. cost=$0.78
- 2026-09-07T03:26:51+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-323` for one more round, or review on GitHub
- 2026-09-07T03:29:13+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/brief.py, src/garden/review.py, tests/fake_claude.py); a rebase agent will resolve it
- 2026-09-07T04:22:09+00:00 triage: changes requested by hand: Current a7cf4ae exact CI passed but PR241 now has merge conflicts with current main. Preserve completed fail-closed fixe
- 2026-09-07T04:34:26+00:00 dispatched rebase run 20260907T043425Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~23905 tokens)
- 2026-09-07T04:38:17+00:00 preserved uncommitted worktree changes from run 20260907T043425Z-rebase outside the PR: `git stash apply d8e30deb364527c7067469dcc34a30828af2b4f6` in /home/joshua/work/worktrees/CG-323 (garden:CG-323:20260907T043425Z-rebase:reap)
- 2026-09-07T04:42:43+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit 3043e3025794, not because of this branch; waiting for the base to go green, no revise round cost=$0.02
- 2026-09-07T04:57:36+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit 03845f27cdbd, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-07T05:53:32+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit 242f51d2785a, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-07T06:02:53+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit 6795a178483d, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-07T06:17:04+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bc7a1fd65f11, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-07T06:26:47+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit 77169d72cadb, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-07T06:31:19+00:00 pre-PR checks failed (lint) (rebase onto `main` did not apply cleanly); revise run will fix before the PR is updated
- 2026-09-07T06:31:40+00:00 dispatched revise run 20260907T063139Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~25215 tokens)
- 2026-09-07T06:40:32+00:00 preserved uncommitted worktree changes from run 20260907T063139Z-revise outside the PR: `git stash apply 5fdb418b311016c20ec0d7c996e7c19f577ecec5` in /home/joshua/work/worktrees/CG-323 (garden:CG-323:20260907T063139Z-revise:reap)
- 2026-09-07T06:41:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Fixed the reported import-order lint failure. Focused checks and exact-head GitHub CI pass on c9850e0aa1f7f332adf2d3472bdef7d35f2ff674. cost=$0.56
- 2026-09-07T06:41:52+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-323` for one more round, or review on GitHub
- 2026-09-07T06:42:02+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/review.py); a rebase agent will resolve it
- 2026-09-07T09:13:10+00:00 triage: changes requested by hand: Owner delegates this routine recovery. Address the concrete preserved review findings below; self-review and repair befo
- 2026-09-07T09:13:11+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T09:13:43+00:00 dispatched rebase run 20260907T091341Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8245 tokens)
- 2026-09-07T09:16:16+00:00 preserved uncommitted worktree changes from run 20260907T091341Z-rebase outside the PR: `git stash apply 9bb8abf6c6c7e979d22ea360262f269692ea1c2a` in /home/joshua/work/worktrees/CG-323 (garden:CG-323:20260907T091341Z-rebase:reap)
- 2026-09-07T09:18:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Rebased onto origin/main and resolved all conflicts without altering unrelated work. cost=$0.02
- 2026-09-07T09:18:33+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-323` for one more round, or review on GitHub
- 2026-09-07T09:35:05+00:00 triage: marked ready for review
- 2026-09-07T09:38:20+00:00 stuck: pending feedback recorded but the task is in_review, not changes_requested; resume with one more round (`garden retry CG-323`) or send it back (`garden triage CG-323 --changes "..."`)
- 2026-09-07T09:39:48+00:00 priority 1 -> 0 (web)
- 2026-09-07T09:48:22+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T10:02:21+00:00 dispatched revise run 20260907T100219Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26016 tokens)
- 2026-09-07T10:11:25+00:00 preserved uncommitted worktree changes from run 20260907T100219Z-revise outside the PR: `git stash apply da3f4aa3e09fba519ee3a79742fabf3d9c258bbd` in /home/joshua/work/worktrees/CG-323 (garden:CG-323:20260907T100219Z-revise:reap)
- 2026-09-07T10:11:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/241: Pre-PR diff-inspection errors are retained as mechanical failures and routed into actionable revise feedback instead of aborting a tick. Current main is integrated and exact-head CI passed. cost=$0.68
- 2026-09-07T10:11:30+00:00 stalled: revise run 20260907T100219Z-revise produced no change to the diff or PR description; run `garden triage CG-323 --changes "<feedback>" to unblock`
- 2026-09-07T10:15:53+00:00 automated review: request_changes — The pre-flight and frozen-criteria flows are largely implemented and 107 focused tests pass, but the conflict-marker check rejects valid clean diffs containing an added Setext heading underline. cost=$0.96
- 2026-09-07T10:17:09+00:00 triage: marked ready for review
- 2026-09-07T14:27:18+00:00 Operator fast-forward: GitHub merge verified 8998db4310f69a4194179d5960a77ada2e002a92; exact-head CI and operator self-review passed. Not yet deployed.
