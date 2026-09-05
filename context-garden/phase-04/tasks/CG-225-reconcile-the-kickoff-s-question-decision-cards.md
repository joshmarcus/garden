---
id: CG-225
title: The retro's questions become decision cards through the kickoff's mechanism (re-doing CG-189, whose
  implementation was dropped from CG-178 before merge)
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-224
priority: 1
difficulty: medium
reading:
- src/garden/planner.py
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/web/pages/phase.py
- src/garden/cli/planning.py
branch: garden/cg-225-reconcile-the-kickoff-s-question-decision-cards-trial-codex-trial-codex-gpt-5-6-terra
pr: https://github.com/joshmarcus/context-garden/pull/184
harness: codex
model: gpt-5.6-terra
discovered_from: CG-224
last_dispatched_at: '2026-09-05T21:03:30+00:00'
created: '2026-09-05T17:39:03+00:00'
updated: '2026-09-05T21:28:47+00:00'
---

## Goal

The retro's "questions for the human" reach the owner as decision cards and their answers land in the retro document and the next phase's goals, as CG-189 specified, built on the question-card mechanism CG-224 (phase kickoff) merged to main. There is one question/decision mechanism, shared by kickoff and retro.

## Context

CG-189 was implemented on a branch stacked on CG-178 and its PR #150 was merged into CG-178's branch on 2026-09-05, which marked CG-189 `done`. During CG-178's later revise rounds commit a08b6b8 removed the CG-189 questions feature, and CG-178 merged to main without it. So main has no retro-question cards, CG-189's status is wrong (see CG-228 for the rule that fixes it), and this task's original wording, "reconcile the two mechanisms", sent two workers and two trial contenders to look for code that is not there. Both stopped correctly. CG-224's kickoff cards are on main (`garden decide --answer/--dismiss`, the Inbox card, the phase page panel); extend them rather than add a second path.

## Acceptance criteria

- [ ] The retro reconciliation's `questions` (CG-189's field) are filed as decision cards of the kickoff kind, one per question, with the retro as their source; the Inbox shows them and `garden decide` answers or dismisses them.
- [ ] An answer is appended under `## Answers` in `docs/retro.md` and under `## Decisions` in the next phase's `goals.md` with who and when, and `garden plan` for the next phase includes them.
- [ ] The retro page (CG-146) lists the questions with their answers; a question the retro marked blocking (CG-178's `reopen`) is answered before the verdict card can be accepted.
- [ ] Tests with the fake harness: a retro with two questions, one answered on the web and one on the CLI.

## Log

- 2026-09-05T17:39:03+00:00 discovered by CG-224
- 2026-09-05T17:48:27+00:00 approved (web)
- 2026-09-05T17:48:46+00:00 dispatched work run 20260905T174831Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-224-phase-kickoff-before-a-phase-starts-flag-topics stacked on CG-224, ~25703 tokens)
- 2026-09-05T17:53:28+00:00 worker blocked: CG-189 has not merged: its branch is not an ancestor of main, origin/main, or this branch, and it forked before the kickoff mechanism (CG-224) existed, so there is no second question/decision implementation in the tree to reconcile the kickoff's cards against yet. Reimplementing or guessing CG-189's design here would be out of scope and likely to conflict with whatever actually lands. cost=$0.51
- 2026-09-05T17:58:01+00:00 parent CG-224 merged; rebased onto main and retargeted the PR
- 2026-09-05T18:11:40+00:00 dispatched trial run 20260905T181127Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~25925 tokens)
- 2026-09-05T18:11:56+00:00 dispatched trial run 20260905T181141Z-trial via local [codex] (fresh session, base main, ~25960 tokens)
- 2026-09-05T18:11:56+00:00 trial started with claude:claude-sonnet-5, codex
- 2026-09-05T18:12:38+00:00 trial: no contender produced a PR
- 2026-09-05T18:14:44+00:00 reset to ready by hand
- 2026-09-05T18:15:51+00:00 dispatched work run 20260905T181551Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~26037 tokens)
- 2026-09-05T18:17:35+00:00 worker blocked: CG-189 (the fuller retro question/decision mechanism) still has not merged into main — its branch is not an ancestor of main and no corresponding PR exists in main's history — so there is nothing yet to reconcile the kickoff's question-decision cards (CG-224) against. cost=$0.30
- 2026-09-05T18:25:03+00:00 dispatched trial run 20260905T182503Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~26164 tokens)
- 2026-09-05T18:25:04+00:00 dispatched trial run 20260905T182504Z-trial via local [codex] (fresh session, base main, ~26198 tokens)
- 2026-09-05T18:25:04+00:00 trial started with claude:claude-sonnet-5, codex
- 2026-09-05T18:27:25+00:00 trial: no contender produced a PR
- 2026-09-05T18:49:52+00:00 reset to ready by hand
- 2026-09-05T18:50:17+00:00 dispatched trial run 20260905T185017Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~26557 tokens)
- 2026-09-05T18:50:17+00:00 dispatched trial run 20260905T185017Z-trial-2 via local [codex] (fresh session, base main, ~26592 tokens)
- 2026-09-05T18:50:17+00:00 trial started with claude:claude-sonnet-5, codex
- 2026-09-05T19:07:48+00:00 all contenders finished; comparison run started
- 2026-09-05T19:15:21+00:00 trial won by codex (scores: claude:claude-sonnet-5=6, codex=8): https://github.com/joshmarcus/context-garden/pull/179
- 2026-09-05T19:45:48+00:00 operator: trial re-run on gpt-5.6-terra vs claude sonnet 5 (apples to apples); the astra and sonnet PRs #179/#181 are closed, branches kept
- 2026-09-05T19:46:31+00:00 dispatched trial run 20260905T194631Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~26749 tokens)
- 2026-09-05T19:46:46+00:00 dispatched trial run 20260905T194631Z-trial-2 via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26787 tokens)
- 2026-09-05T19:46:46+00:00 trial started with claude:claude-sonnet-5, codex:gpt-5.6-terra
- 2026-09-05T20:04:25+00:00 all contenders finished; comparison run started
- 2026-09-05T20:10:29+00:00 trial won by codex:gpt-5.6-terra (scores: claude:claude-sonnet-5=7, codex:gpt-5.6-terra=9): https://github.com/joshmarcus/context-garden/pull/184
- 2026-09-05T21:02:57+00:00 automated review requested changes: The shared question/decision mechanism and its retro-side answer recording are implemented correctly and covered by a new fake-harness test, but the pre-existing phase-page Kickoff panel and Inbox 'why' text were not updated to distinguish retro-sourced questions from kickoff ones, so retro questions leak into the Kickoff panel mislabeled as kickoff's. cost=$0.82
- 2026-09-05T21:03:30+00:00 dispatched revise run 20260905T210329Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~27625 tokens)
- 2026-09-05T21:13:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/184: Retro decision cards are now excluded from the phase Kickoff panel and labeled as retro-originated in the Inbox. Added regression coverage alongside the existing fake-harness retro flow.
- 2026-09-05T21:13:51+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-225` for one more round, or review on GitHub
- 2026-09-05T21:22:38+00:00 automated review: approve — All four acceptance criteria are met and verified by a solid new fake-harness test; two pre-existing, unrelated-file surfaces (TUI messages, a resolve_decision error string) now say "kickoff" for what can also be a retro question, but these are cosmetic nits. cost=$0.73
- 2026-09-05T21:22:45+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T21:25:37+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T21:28:47+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/184
