---
id: CG-296
title: One vocabulary and one place for each fact across rail, Config, CLI and Inbox
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: medium
reading: []
branch: garden/cg-296-one-vocabulary-and-one-place-for-each-fact-acros
pr: https://github.com/joshmarcus/context-garden/pull/228
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-06T13:51:20+00:00'
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-06T17:32:55+00:00'
---

## Goal

One name for the operating point and 'feed' for the observe level; no task ids in headings or help; tick_interval in one Config list; move, retro-decide and canary in help panels with a test; the Kickoff panel below the fold once a phase has approved tasks; the approve button demoted while gaps exist; question cards in their own Inbox group; one shared needs-you predicate for status, inbox, observe and the rail; resume named on the Costs page. Designer, usability and user findings.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Items folded in (kickoff q2, 2026-09-06)

Each of these persona findings was a draft of its own; they are cancelled with this task as their owner and every one is a checklist line here.

- [ ] CG-255: Operating-profile stops name a tier per harness, and user-facing copy drops task ids — **User value:** a codex-only garden switching stops no longer gets Claude model names, and the Config page reads as a product, not a task list.
- [ ] CG-257: The rail, Config page, CLI and status line use 'operating profile', 'stop' and  — Pick one word for the operating point and rename the observe level to 'feed' or 'observe level' on every surface and in docs.
- [ ] CG-258: The Kickoff panel with a primary 'Kick off' button is the first thing on every o — Show it above the fold only while the phase has no approved tasks; afterwards fold it into a header note or move it below the task table.
- [ ] CG-259: A draft with brief gaps shows 'Fix the brief before approving' beside an enabled — Disable or demote the approve button while gaps exist and make fixing the brief (link to Suggest a change) the primary action.
- [ ] CG-260: tick_interval is listed both under live re-read values and under 'Needs a restar — Remove restart-only keys from the live list, replace the eyebrow with a plain label like the other panels, and drop task ids from help text.
- [ ] CG-261: move, retro-decide and canary appear in an unlabeled Commands box above the name — Assign each a panel and add a test asserting every command names one.
- [ ] CG-262: A draft task page shows both 'Approve into [phase]' and a separate move 'phase — Hide the move pulldown on drafts and hide either select when it has one option, matching the task page's existing rule.
- [ ] CG-263: Kickoff and retro question cards sit in the 'Needs a decision' group whose descr — Give questions their own group or fold them into the worker-question group with a source label.
- [ ] CG-266: The worker's question is printed twice on its card because the reason line and t — Use the reason line for context and show the question once.
- [ ] CG-267: Resume, trial, compare and edit runs fold into an unnamed 'other' activity that — Name common modes such as resume, or list the folded modes in the bar's hover title.
- [ ] CG-268: Spend appears three ways in the rail (a whole-dollar Runs figure, a Costs link, — Drop the dollar figure from the Runs link now that Costs exists and give the default option a plain name such as 'no profile'.
- [ ] CG-269: The Costs form submits every select on change yet keeps a visible Filter button, — Use the same noscript pattern for the fallback button.
- [ ] CG-270: A cancelled task's only action is 'Continue the loop', the TUI label is 'Continu — Label the cancelled-task action 'Reopen', align the TUI label, and name the tier the kickoff actually uses.
- [ ] CG-285: tick_interval appears both under live re-read values and under the needs-a-resta — Show each key in one list only; put tick_interval under restart.
- [ ] CG-286: The Costs page files a resume round as 'other', and garden observe's digest repo — Give resume its own activity name and make the digest's failed count read the same terminal statuses the Board does.
- [ ] CG-287: With every phase closed, garden status prints an empty table and its legend befo — Skip the table and legend when there are no open phases and lead with the closed-phase line.

## Acceptance criteria

- [ ] The rail, Config page, CLI output and status line all use one shared term for the operating point and 'feed' for the observe level, with no task ids left in headings or help text.
- [ ] tick_interval appears in exactly one Config list — the restart-required list — and not under live re-read values.
- [ ] move, retro-decide and canary each surface in a named help panel, verified by a test asserting every command names one panel.
- [ ] The Kickoff panel shows above the fold only while a phase has no approved tasks and moves below the task table once it does; the approve button is disabled or demoted while brief gaps exist, with fixing the brief as the primary action.
- [ ] Question cards get their own Inbox group (or a labeled spot in the worker-question group), and resume appears as its own named activity on the Costs page rather than folding into 'other'.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-285 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:20:37+00:00 difficulty easy -> medium
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002113Z-edit) cost=$0.10
- 2026-09-06T00:24:04+00:00 approved (cli)
- 2026-09-06T13:20:54+00:00 dispatched work run 20260906T131807Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8662 tokens)
- 2026-09-06T13:44:51+00:00 opened https://github.com/joshmarcus/context-garden/pull/228 (base main): Unified operating controls, Inbox decision presentation, and Costs activity naming across CLI and web surfaces. Committed as e42daf6. cost=$1.35
- 2026-09-06T13:45:54+00:00 PR conflicts with main; rebase onto main conflicts (docs/design/snapshot.json); a rebase agent will resolve it
- 2026-09-06T13:51:20+00:00 dispatched rebase run 20260906T135114Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~399467 tokens)
- 2026-09-06T13:53:09+00:00 attempt 1 failed: worker exited 1: Error: turn/start: turn/start failed: Input exceeds the maximum length of 1048576 characters. (code -32602), data: {"input_error_code":"input_too_large","max_chars":1048576,"actual_chars":1597868}; will retry
- 2026-09-06T15:12:38+00:00 Recover completed review 20260906T134945Z-review from stale ready state. Result and exit code are present; collect once and validate head freshness before applying. Do not spawn a duplicate review.
- 2026-09-06T15:13:12+00:00 automated review requested changes: Core Config, kickoff, help-panel, Inbox-grouping, and Costs activity changes are present, but the vocabulary and folded requirements remain incomplete, question cards duplicate content, and an operational snapshot accidentally widens the PR. cost=$0.29
- 2026-09-06T17:32:55+00:00 Owner fast-forward: PR 228 verified merged at 14676f5; 169 targeted tests, full CI and actual UI repair journeys passed.
