---
id: CG-293
title: A brief never ships with an empty or unresolved reading list, and a revise brief restates the criteria
  and the concrete blocker
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-293-a-brief-never-ships-with-an-empty-or-unresolved
pr: https://github.com/joshmarcus/context-garden/pull/240
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-06T20:44:54+00:00'
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-07T02:13:54+00:00'
---

## Goal

The brief builder refuses an empty reading list, drops entries that do not resolve and reports the drop as a gap, and builds inlined files from the task's base commit rather than a dirty worktree. A revise brief restates the acceptance criteria, inlines the actual review comments and the failing check's stack trace, and when GitHub has nothing to address, names the rebase conflict as the concrete blocker. A per-task `true` escape supports the rare mechanical task, and amended criteria flow through results, reap, and review.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict, consolidating seventeen phase-04 friction items.

## Acceptance criteria

- [ ] Brief builder rejects a brief with an empty reading list before it reaches the approve gate, returning a validation error instead of shipping it.
- [ ] Reading-list entries that fail to resolve to a real path are dropped from the list and reported as a gap in the brief output, not silently discarded.
- [ ] Inlined file contents in a brief are read from the task's base commit, not from an uncommitted or dirty worktree, even when the worktree has local changes.
- [ ] A revise brief restates the task's acceptance criteria verbatim and inlines the actual GitHub review comments and the failing check's stack trace, rather than a summary.
- [ ] When a revise brief finds nothing on GitHub to address, it names the rebase conflict as the blocker instead of leaving the field empty or generic; covered by a test asserting the revise-brief path sets this blocker when there are no open review comments.
- [ ] A per-task `true` escape is available for the rare mechanical task.
- [ ] The result block carries `criteria_amended: [{index, text, reason}]`; on reap, the task file is updated and the reason is recorded in the log; the review brief marks the amended line as amended; and the reviewer judges that line. Tests cover the full round trip.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.
- [x] A criterion that names a file, a function or a field is accepted as written; the work and review briefs say such names are guidance and the outcome is what is judged (owner, 2026-09-06 04:00Z: no refusal on names).
- [x] A worker may amend a criterion: the result block carries `criteria_amended: [{index, text, reason}]`, the task file is updated on reap with the reason in the log, the review brief shows the amended line marked as amended, and the reviewer judges that line; tests cover the round trip.
- [x] Criteria are optional: `brief_gaps` and the approve gate accept a task with no `## Acceptance criteria` section (a placeholder checklist such as 'TODO' or '...' is still refused); the work brief then says the Goal is the contract and asks the worker to state what it verified and how; the review brief asks the reviewer to judge the goal on that evidence and return `criteria: []`; tests cover approve, brief and review for a criteria-less task (owner, 2026-09-06 03:55Z: 'also allow tasks without acceptance criteria').

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-282 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005022Z-edit) cost=$0.11
- 2026-09-06T00:52:23+00:00 approved (cli)
- 2026-09-06T03:49:25+00:00 difficulty medium -> medium
- 2026-09-06T03:51:40+00:00 integrated 3 suggestion(s) (run 20260906T034959Z-edit) cost=$0.03
- 2026-09-06T04:33:38+00:00 dispatched work run 20260906T043153Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8069 tokens)
- 2026-09-06T05:20:50+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$2.97
- 2026-09-06T05:22:09+00:00 dispatched revise run 20260906T052157Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9023 tokens)
- 2026-09-06T06:16:05+00:00 pre-PR checks failed (checks); no PR opened yet; revise run will fix cost=$0.79
- 2026-09-06T06:16:57+00:00 dispatched revise run 20260906T061656Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8361 tokens)
- 2026-09-06T06:51:56+00:00 pre-PR checks failed (test) (still failing after a rebase onto `main`); no PR opened yet; revise run will fix cost=$0.85
- 2026-09-06T07:11:04+00:00 dispatched revise run 20260906T071103Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9104 tokens)
- 2026-09-06T07:27:30+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 508a28c4fe30, not because of this branch; waiting for the base to go green, no revise round cost=$0.37
- 2026-09-06T07:40:14+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 67134b3102cb, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-06T08:50:02+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 746c745d314f, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-06T09:25:17+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 56af81dfcba5, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-06T12:18:02+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 40fc26107ed2, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-06T12:51:22+00:00 pre-PR checks failed (test) and 3 revision rounds already used; needs a human
- 2026-09-06T13:19:11+00:00 nothing to fix; needs-human stop cleared by hand
- 2026-09-06T13:25:38+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-293`) or send it back (`garden triage CG-293 --changes "..."`)
- 2026-09-06T13:35:20+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-06T14:19:17+00:00 dispatched revise run 20260906T141858Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9686 tokens)
- 2026-09-06T14:59:03+00:00 revision failed: no GARDEN_RESULT in worker output (see final.md)
- 2026-09-06T16:55:49+00:00 reset to ready by hand
- 2026-09-06T19:48:00+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply 4d71cfa531acb2f444c1dd0c3875961b6f326bf0` in /home/joshua/work/worktrees/CG-293 to recover them (garden:CG-293:2026-09-06T19:48:00+00:00)
- 2026-09-06T19:48:01+00:00 dispatched work run 20260906T194800Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10055 tokens)
- 2026-09-06T20:10:27+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$0.73
- 2026-09-06T20:10:38+00:00 dispatched revise run 20260906T201037Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, rebase round 6 (not counted), ~10974 tokens)
- 2026-09-06T20:31:36+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$0.88
- 2026-09-06T20:31:41+00:00 dispatched revise run 20260906T203139Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, rebase round 7 (not counted), ~10926 tokens)
- 2026-09-06T20:44:46+00:00 opened https://github.com/joshmarcus/context-garden/pull/240 (base main): Updated the successful web task-creation fixture so its approve-now request includes a resolvable reading list, matching the brief-completeness gate. Committed as feb1e06. cost=$0.55
- 2026-09-06T20:44:52+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/brief.py); a rebase agent will resolve it
- 2026-09-06T20:44:54+00:00 dispatched rebase run 20260906T204452Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~9232 tokens)
- 2026-09-06T20:51:14+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit c1f75cb08e47, not because of this branch; waiting for the base to go green, no revise round cost=$0.03
- 2026-09-06T20:52:21+00:00 automated review: request_changes — Core brief behavior is implemented and focused tests pass, but amendment persistence is not idempotent and the PR includes a large unrelated runtime snapshot. The claimed full-round-trip amendment test is also absent. cost=$0.48
- 2026-09-06T21:16:18+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 6dd3ae49f448, not because of this branch; waiting for the base to go green, no revise round
- 2026-09-06T22:02:08+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-293`) or send it back (`garden triage CG-293 --changes "..."`)
- 2026-09-07T02:13:51+00:00 triage: changes requested by hand: Recover the existing PR240 rather than restart implementation. Incorporate current main and resolve conflicts, then reva
- 2026-09-07T02:13:54+00:00 Operator02:12 UTC investigated owner question: no live run; PR240 open at95ea8829, conflicts and historical failed CI. Persisted last_review has three concrete findings but pending_feedback was empty, producing stuck no-feedback since22:02. Restored findings via supported triage-changes/retry, preserving branch and nine-rebase history; eligible when integrity pause is lifted, not newly dispatched. Revalidate findings against current main, preserve unrelated snapshot, use current exact-head CI.
