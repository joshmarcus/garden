---
id: CG-377
title: Scope review validation to affected behavior and acceptance claims
status: in_review
product: context-garden
phase: phase-05
depends_on:
- CG-339
priority: 0
difficulty: medium
reading: []
branch: garden/cg-377-scope-review-validation-to-affected-behavior-and
pr: https://github.com/joshmarcus/context-garden/pull/284
attempts: 1
last_dispatched_at: '2026-09-07T13:38:39+00:00'
created: '2026-09-07T09:31:44+00:00'
updated: '2026-09-07T15:20:39+00:00'
---

## Goal

Require evidence proportional to affected behavior, rather than making every PR satisfy an application-wide validation checklist. Preserve meaningful UI and lifecycle review.

## Context

Owner requested fixing overly broad validation demands on2026-09-07. CG358 had all incident-control criteria accepted yet a blanket missing-captures finding named14 unrelated pages. CG365 suffered the same. CG339 currently repairs package-wide interaction classification and label-only recovery evidence; depend on and preserve that work rather than duplicate it. CG315's historical always-capture core-page rule and available capture inventory must not become unconditional review requirements. CG376 tracks review-loop friction.

## Acceptance criteria

- [ ] Derive one explicit validation plan from changed behavior, acceptance claims and shared dependencies. Each required page/flow/check records its applicability reason; merely being captured or existing in src/garden is insufficient.
- [ ] Separate available artifacts from required artifacts. Missing pages_seen blocks only required affected pages; pure documentation/parser/formatting changes require focused relevant checks, not screenshots or generic empty/failure journeys.
- [ ] Shared templates/styles/navigation and cross-cutting lifecycle changes expand scope to affected consumers with a stated rationale. Require real served/browser behavior for interaction claims; relevant empty/failure/recovery states remain mandatory when behavior can affect them. Unknown scope prompts bounded inspection rather than blanket exemption or whole-app default.
- [ ] Workers, pre-checks and reviewers consume the same head-bound validation plan. New demands identify the changed claim or discovered risk and are logged as scope expansion; preserve frozen acceptance criteria and existing valid evidence without accepting stale-head evidence.
- [ ] Regression cases cover CG358-style backend control change without rendered-page changes, parser-only change, one-page layout change, shared stylesheet change and real failure/recovery behavior. Reject arbitrary14-page demand and reject under-validation of shared UI or claimed interactions.
- [ ] Preserve broad whole-application walkthroughs at phase/milestone validation where appropriate; record avoided review rounds/capture cost and remaining unknowns in friction, linked to CG376.

## Log

- 2026-09-07T09:31:45+00:00 approved (web)
- 2026-09-07T09:39:55+00:00 priority 1 -> 0 (web)
- 2026-09-07T10:23:37+00:00 dispatched work run 20260907T102236Z-work via local [codex model=gpt-5.6-terra] (fresh session, base garden/cg-339-review-affected-behavior-through-the-running-app stacked on CG-339, ~9496 tokens)
- 2026-09-07T10:57:22+00:00 preserved uncommitted worktree changes from run 20260907T102236Z-work outside the PR: `git stash apply 5e416046b4ad8c3c21f360affc036cc70edd17a5` in /home/joshua/work/worktrees/CG-377 (garden:CG-377:20260907T102236Z-work:reap)
- 2026-09-07T10:59:54+00:00 opened https://github.com/joshmarcus/context-garden/pull/284 (base garden/cg-339-review-affected-behavior-through-the-running-app): Validation is now planned from changed behavior and claims, with only affected pages enforced and shared UI deliberately widened. Final exact-commit CI passed. cost=$2.39
- 2026-09-07T11:00:09+00:00 PR conflicts with garden/cg-339-review-affected-behavior-through-the-running-app; rebase onto garden/cg-339-review-affected-behavior-through-the-running-app conflicts (src/garden/review.py, src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-07T11:02:34+00:00 automated review: request_changes — The scoped plan is a useful foundation, but it is not yet consistently enforced or head-bound: reviewers can receive stale captures, unknown UI scope is advisory only, and workers never consume the plan. The required CG376 friction evidence is also absent. cost=$0.60
- 2026-09-07T11:02:45+00:00 dispatched rebase run 20260907T110243Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base garden/cg-339-review-affected-behavior-through-the-running-app, conflict only; easy tier, ~21857 tokens)
- 2026-09-07T11:05:01+00:00 preserved uncommitted worktree changes from run 20260907T110243Z-rebase outside the PR: `git stash apply f9fdf27d0904dd56d68ce9c126a0f9a0cb7cc5b5` in /home/joshua/work/worktrees/CG-377 (garden:CG-377:20260907T110243Z-rebase:reap)
- 2026-09-07T11:06:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/284: Rebased CG-377 onto CG-339 and resolved the marked conflicts while preserving both validation-plan and replay-evidence behavior. cost=$0.02
- 2026-09-07T11:10:10+00:00 automated review requested changes: The validation plan is a useful foundation, but enforcement remains incomplete: generic capture wording still produces whole-app captures, capture artifacts are not head-bound, unknown UI scope is advisory, and workers do not consume the plan. Required friction evidence is also absent. cost=$0.69
- 2026-09-07T11:10:22+00:00 dispatched revise run 20260907T111020Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base garden/cg-339-review-affected-behavior-through-the-running-app, ~10924 tokens)
- 2026-09-07T11:26:35+00:00 preserved uncommitted worktree changes from run 20260907T111020Z-revise outside the PR: `git stash apply 7610589c07ae0313c4139659354cd53b3a8197e1` in /home/joshua/work/worktrees/CG-377 (garden:CG-377:20260907T111020Z-revise:reap)
- 2026-09-07T11:29:02+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:30:14+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:31:30+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:32:43+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:33:58+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:35:15+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:36:30+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:37:45+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:39:02+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:40:16+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:41:31+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:42:42+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:44:09+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:45:21+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:46:13+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:46:15+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:47:27+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:48:39+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:49:50+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human

- 2026-09-07T11:51:02+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:52:14+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:53:26+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:54:38+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:55:51+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:57:03+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:58:15+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:59:32+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:00:55+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:02:08+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:03:29+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:04:42+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:05:53+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:07:03+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:08:14+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:09:24+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:10:38+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:11:50+00:00 check did not run (20260907T112749Z-check): no check result; retry also failed; needs human
- 2026-09-07T12:23:41+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T13:38:39+00:00 dispatched revise run 20260907T133837Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base garden/cg-339-review-affected-behavior-through-the-running-app, ~11889 tokens)
- 2026-09-07T13:51:25+00:00 preserved uncommitted worktree changes from run 20260907T133837Z-revise outside the PR: `git stash apply f7d0741d0033b1794b76cdb6a3b5f6e18fd1c9dd` in /home/joshua/work/worktrees/CG-377 (garden:CG-377:20260907T133837Z-revise:reap)
- 2026-09-07T14:12:05+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T14:13:24+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T14:14:42+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T14:15:57+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T15:12:03+00:00 Owner-authorized fast-forward operator repair/self-review; expected head ec9811fc3ea597a5478fe63bdd4b3dccb5a31fef, exact full CI34136229231/34136233940 success, GitHub CLEAN, retargeted-main merge tree equals tested head. Verified PR284 merged 40373fe99397c5d86f888bafa8dd99e333690db4. Not yet deployed.
- 2026-09-07T15:16:38+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T15:16:41+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T15:17:56+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T15:19:16+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
- 2026-09-07T15:20:39+00:00 check did not run (20260907T141044Z-check): no check result; retry also failed; needs human
