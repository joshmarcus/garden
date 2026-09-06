---
id: CG-292
title: 'Every status write goes through _transition: Scheduler.mark_done and unapprove, and a source-grep
  test'
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
branch: garden/cg-292-every-status-write-goes-through-transition-sched
pr: https://github.com/joshmarcus/context-garden/pull/201
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-06T00:50:48+00:00'
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-06T02:01:13+00:00'
---

## Goal

Route every status write through `_transition`. Web `Mark done` and `unapprove`, CLI `set-status`, `take`, `approve`, `_approve_retro_blocking`, `attach_pr`, and the discovered hold all currently assign `task.status` directly and need to go through `_transition` instead. Label the web `Mark done` action on an in-review card as 'Mark done without merging', require a confirm, and drop it from the review card's primary row. Add a test, alongside `test_queue_state.py`, that source-greps the codebase to assert no other module assigns `.status` directly.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict. Folds in CG-247 and CG-282 (cancelled as duplicates): the web `Mark done` on an in-review card is the escape hatch, labelled 'Mark done without merging' with a confirm, and dropped from the card's primary row. A PR-backed task reports done only when its commits are on the base branch (CG-228's rule), so `mark_done` refuses otherwise unless forced.

## Acceptance criteria

- [ ] Web `unapprove` and the review card's `Mark done` handler call `_transition` instead of assigning `task.status` directly.
- [ ] CLI `set-status`, `take`, `approve`, `_approve_retro_blocking`, `attach_pr`, and the discovered-hold path all call `_transition` instead of assigning `.status` directly.
- [ ] The web review card labels the done action 'Mark done without merging', shows a confirm before proceeding, and the button sits outside the card's primary row.
- [ ] `mark_done` refuses to mark a PR-backed task done unless its commits are on the base branch or the call is forced, per CG-228.
- [ ] A new test alongside `test_queue_state.py` source-greps the codebase and fails if any module other than `_transition` assigns `.status` directly.

## Out of scope

(none)

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-281 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002111Z-edit) cost=$0.10
- 2026-09-06T00:24:02+00:00 approved (cli)
- 2026-09-06T00:27:49+00:00 dispatched work run 20260906T002733Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~6863 tokens)
- 2026-09-06T00:42:54+00:00 opened https://github.com/joshmarcus/context-garden/pull/201 (base main): Routes task status mutations through Scheduler._transition, adds a base-branch guard to mark_done, and makes the web escape hatch explicit and confirmed. Commit: 6088bd7. cost=$1.09
- 2026-09-06T00:48:10+00:00 automated review requested changes: Status-write centralization is correct and well-tested, but the web review card's 'Mark done without merging' relocation criterion isn't actually met: the button was deleted from the Inbox review card entirely rather than relabeled/confirmed/demoted in place, and its new home on the task page sits in the same undivided actions row as primary buttons. cost=$0.85
- 2026-09-06T00:50:48+00:00 dispatched revise run 20260906T005047Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~7325 tokens)
- 2026-09-06T01:49:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/201: Restored the Inbox review-card escape hatch as a distinct, visually secondary action with explicit confirmation. The existing status-transition centralization remains intact. cost=$0.47
- 2026-09-06T01:53:16+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/retro.py); a rebase agent will resolve it
- 2026-09-06T02:01:13+00:00 automated review: approve — All five acceptance criteria are met and verified against the diff and a full test run; only a harmless unnecessary --force in one CLI test as a nit. cost=$0.68
