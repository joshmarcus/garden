---
id: CG-295
title: 'Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and
  the architecture module map'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/scaffold.py
- docs/design.md
- docs/roadmap.md
- docs/architecture.md
- src/garden/kickoff.py
- src/garden/scheduler/kickoff.py
- src/garden/profiles.py
- src/garden/inbox.py
branch: garden/cg-295-docs-match-the-mechanism-the-scaffolded-operate
pr: https://github.com/joshmarcus/context-garden/pull/287
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-07T15:40:45+00:00'
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-07T16:28:18+00:00'
---

## Goal

scaffold.py's skill template should say garden.yaml reloads each tick and only RESTART_KEYS need a restart; design.md and roadmap.md should drop automatic merging from non-goals; the architecture map should add kickoff.py, scheduler/kickoff.py, profiles.py, inbox.py and web/pages/costs, with a test that every module appears, plus the restart-recovery timing note CG-198 asked for. Also remove the stale 'once CG-207 lands' comment from the live garden.yaml.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Acceptance criteria

- [ ] scaffold.py's skill template states garden.yaml reloads each tick and only RESTART_KEYS require a restart (src/garden/scaffold.py)
- [ ] design.md and roadmap.md no longer list automatic merging under non-goals (docs/design.md, docs/roadmap.md)
- [ ] The architecture module map lists kickoff.py, scheduler/kickoff.py, profiles.py, inbox.py and web/pages/costs, and includes the CG-198 restart-recovery timing note (docs/architecture.md)
- [ ] A test fails if any module is missing from the architecture map (tests/test_architecture.py)
- [x] Operator verified live garden.yaml on 2026-09-07: it no longer contains the 'once CG-207 lands' comment (garden.yaml)

## Out of scope

(none)

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-284 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005024Z-edit) cost=$0.07
- 2026-09-06T00:52:24+00:00 approved (cli)
- 2026-09-06T13:13:13+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:31+00:00 reset to ready by hand
- 2026-09-07T06:05:55+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply e9fc940ac9bb37a54de90f83dbfc4fc2aab1fd74` in /home/joshua/work/worktrees/CG-295 to recover them (garden:CG-295:20260907T060555Z-work:pre-dispatch, run 20260907T060555Z-work)
- 2026-09-07T06:06:12+00:00 dispatched work run 20260907T060555Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~19395 tokens)
- 2026-09-07T06:24:06+00:00 preserved uncommitted worktree changes from run 20260907T060555Z-work outside the PR: `git stash apply d0c0ffe02920b7e6ff4c9f8df896f85fe639489c` in /home/joshua/work/worktrees/CG-295 (garden:CG-295:20260907T060555Z-work:reap)
- 2026-09-07T06:24:06+00:00 worker asks: Please provide the live garden.yaml within this checkout or authorize the correct path to edit it. cost=$0.20

## Operator answer
The live garden.yaml comment is already absent (verified directly). That criterion is fulfilled by the operator. Work only inside the product checkout on remaining documentation and tests; do not request or edit live garden configuration. Preserve existing implementation.
- 2026-09-07T09:14:05+00:00 Owner-delegated answer: live config cleanup already satisfied; resume product-only work via admission queue.
- 2026-09-07T09:14:05+00:00 reset to ready by hand
- 2026-09-07T12:02:28+00:00 dispatched work run 20260907T120226Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~19921 tokens)
- 2026-09-07T12:11:48+00:00 preserved uncommitted worktree changes from run 20260907T120226Z-work outside the PR: `git stash apply c870dc809effd4072ed074ce38e79e5d03e792ea` in /home/joshua/work/worktrees/CG-295 (garden:CG-295:20260907T120226Z-work:reap)
- 2026-09-07T12:19:09+00:00 opened https://github.com/joshmarcus/context-garden/pull/287 (base main): Updated scaffold, design and roadmap documentation; expanded the architecture map with restart-recovery guidance and module coverage enforcement. All required validation passed. cost=$0.03
- 2026-09-07T12:19:15+00:00 PR conflicts with main; rebase onto main conflicts (docs/architecture.md); a rebase agent will resolve it
- 2026-09-07T12:32:35+00:00 dispatched rebase run 20260907T123233Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~18714 tokens)
- 2026-09-07T12:35:06+00:00 preserved uncommitted worktree changes from run 20260907T123233Z-rebase outside the PR: `git stash apply e6fa24be430bb0db987792ab09f3b6758ec49ed7` in /home/joshua/work/worktrees/CG-295 (garden:CG-295:20260907T123233Z-rebase:reap)
- 2026-09-07T13:35:28+00:00 check did not run (20260907T133409Z-check): idle 60 min (no output or file change); will retry
- 2026-09-07T13:36:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/287: Rebased CG-295 onto origin/main and resolved the architecture documentation conflict while preserving both sides. cost=$0.01
- 2026-09-07T13:39:41+00:00 automated review requested changes: Four criteria are satisfied, but the architecture-map regression test does not reliably detect missing module entries because it uses unrestricted substring matching. cost=$0.42
- 2026-09-07T13:39:56+00:00 dispatched revise run 20260907T133954Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~21011 tokens)
- 2026-09-07T13:50:08+00:00 preserved uncommitted worktree changes from run 20260907T133954Z-revise outside the PR: `git stash apply e420608e346fcaca33fc2e8a27b3ed4ae8eefe55` in /home/joshua/work/worktrees/CG-295 (garden:CG-295:20260907T133954Z-revise:reap)
- 2026-09-07T14:10:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/287: Updated the scaffolded operate skill and product documentation to match live configuration reload and restart behavior, completed the architecture map, and added exact module-coverage regression tests. cost=$0.07
- 2026-09-07T14:13:24+00:00 automated review: approve — The documentation now matches live reload and restart behavior, removes the stale automatic-merging non-goal, and provides exact architecture-module coverage. Focused architecture tests pass. cost=$0.28
- 2026-09-07T14:13:41+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T15:18:02+00:00 PR conflicts with main; rebase onto main conflicts (docs/architecture.md); a rebase agent will resolve it
- 2026-09-07T15:32:26+00:00 automated review: approve — All five acceptance criteria are satisfied. The documentation matches the live reload/restart mechanism, and exact architecture-module coverage is enforced by passing regression tests. cost=$0.47
- 2026-09-07T15:33:00+00:00 dispatched rebase run 20260907T153259Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2232 tokens)
- 2026-09-07T15:35:35+00:00 preserved uncommitted worktree changes from run 20260907T153259Z-rebase outside the PR: `git stash apply 3978a9ef792514105f8f644229d4cebf7edd8149` in /home/joshua/work/worktrees/CG-295 (garden:CG-295:20260907T153259Z-rebase:reap)
- 2026-09-07T15:37:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/287: Rebased CG-295 onto origin/main and resolved the architecture documentation conflict while preserving both the CG-198 restart-recovery note and main's loop-cap updates. cost=$0.01
- 2026-09-07T15:40:24+00:00 automated review requested changes: The focused architecture test fails because `interaction_replay.py` and `preflight.py` are absent from the module map. Ruff passes and the remaining acceptance criteria are supported. cost=$0.32
- 2026-09-07T15:40:45+00:00 dispatched revise run 20260907T154043Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~22149 tokens)
- 2026-09-07T15:51:14+00:00 difficulty easy -> hard (web)
- 2026-09-07T15:51:20+00:00 preserved uncommitted worktree changes from run 20260907T154043Z-revise outside the PR: `git stash apply 035d52e0d17ea905c8adb0a4aaf3b04054004b7d` in /home/joshua/work/worktrees/CG-295 (garden:CG-295:20260907T154043Z-revise:reap)
- 2026-09-07T16:07:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/287: Completed the documentation alignment and architecture coverage fix. CI passed for the final commit. cost=$0.13
- 2026-09-07T16:17:19+00:00 automated review: approve — Documentation matches the live reload and restart mechanism, and exact architecture-module coverage is enforced by passing tests. No blocking correctness, scope, description, or principle issues found. cost=$0.38
- 2026-09-07T16:18:32+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-07T16:18:46+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T16:19:47+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T16:28:18+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/287
