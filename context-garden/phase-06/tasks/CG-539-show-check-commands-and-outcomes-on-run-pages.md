---
id: CG-539
title: Show check commands and outcomes on run pages
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/web/pages/runs.py
- src/garden/checkrun.py
- src/garden/checks.py
- src/garden/runs.py
branch: garden/cg-539-show-check-commands-and-outcomes-on-run-pages
pr: https://github.com/joshmarcus/context-garden/pull/448
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T16:42:59+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T17:05:23+00:00'
---

## Goal

User value: distinguish a finished process from successful validation and see the next action. Why now: generic transcript fallback hides the result of ordinary checks. Size: medium. Dependencies: existing check records and CG-506 for remote transport where needed; reuse available diagnostics without requiring new artifact formats.

## Context

Proposed at the context-garden/phase-05 retro. Actionable check results remove repeated investigation from the most common recovery journey.


## Reviewed scope and verification

Use existing accepted check records to show command, source identity, exit/conclusion, useful diagnostics and available next action. Distinguish process completion from check success and retain uncertainty for incomplete records. This display change does not wait for CG-506: the owner deferred that transcript-storage design. Reuse current records and expose a compatible boundary for any future accepted transport. Verify success/failure/incomplete check pages proportionately.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T15:06:59+00:00 dispatched work run 20260910T150655Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~17826 tokens)
- 2026-09-10T15:12:06+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:13:25+00:00 opened https://github.com/joshmarcus/context-garden/pull/448 (base main): Check run pages now distinguish runner completion from successful validation and show command, source, diagnostics, and next action. Ruff, compilation, and template rendering passed; the focused web suite was blocked during collection by an existing import cycle. cost=$0.65
- 2026-09-10T15:14:41+00:00 CI failure
- 2026-09-10T15:14:59+00:00 dispatched revise run 20260910T151454Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~18550 tokens)
- 2026-09-10T15:17:11+00:00 automated review: request_changes — The outcome/source presentation is sound, but command evidence is incomplete and can be misattributed. cost=$0.34
- 2026-09-10T15:18:26+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:19:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/448: Fixed the CI-blocking circular import and committed it as 22936410. Verified run-page check-result tests, run-index/web focused suite, direct imports, and lint. cost=$0.35
- 2026-09-10T15:22:10+00:00 automated review requested changes: Check outcomes render correctly in the covered success, failure, and empty-result cases, but the command/result association is not reliable. cost=$0.44
- 2026-09-10T15:22:25+00:00 dispatched revise run 20260910T152222Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~18935 tokens)
- 2026-09-10T15:27:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:28:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/448: Separated configured check commands from unmatched reported outcomes so setup failures cannot be attributed to a command that never ran. Verified focused run-page cases, the complete web test file (supervised exit code 0), lint, and compilation. cost=$0.54
- 2026-09-10T15:31:44+00:00 automated review: approve — Run pages reliably separate process completion from validation outcomes and avoid attributing setup or runner failures to commands that did not run. cost=$0.38
- 2026-09-10T15:45:39+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/hosts/locking.py, src/garden/locking.py); a rebase agent will resolve it
- 2026-09-10T15:48:22+00:00 triage: changes requested by hand: Preserve the approved run-page commands/outcomes implementation and167 passing web tests. CG585 now owns the accepted pa
- 2026-09-10T15:51:54+00:00 dispatched rebase run 20260910T155153Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2192 tokens)
- 2026-09-10T15:55:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/448: Rebased onto origin/main and resolved the two locking-file conflicts while preserving the existing implementation. cost=$0.01
- 2026-09-10T15:59:25+00:00 automated review requested changes: The run-page presentation distinguishes process and validation state well, but setup outcomes are not reliably kept separate from configured commands. cost=$0.43
- 2026-09-10T16:06:37+00:00 difficulty medium -> hard after 2 substantive revisions; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-10T16:06:43+00:00 dispatched revise run 20260910T160637Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19530 tokens)
- 2026-09-10T16:11:50+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:13:13+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/448: Run pages no longer attribute infrastructure setup or runner failures to configured commands with the same name. Committed as 5ffaf1fe; 168 web tests passed, 50 affected tests passed after the final changes, and Ruff passed. cost=$0.90
- 2026-09-10T16:15:58+00:00 automated review: approve — Run pages clearly separate process completion from validation success and safely leave infrastructure or ambiguous outcomes unmatched. cost=$0.41
- 2026-09-10T16:31:25+00:00 triage: changes requested by hand: The current run-page implementation has independent approval and its focused tests pass, but actual push CI34500556937 f
- 2026-09-10T16:42:59+00:00 dispatched revise run 20260910T164256Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19816 tokens)
- 2026-09-10T16:46:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:47:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/448: Updated the base-probe recovery regression to require the explicit infrastructure origin while retaining setup diagnostics, exit 127, unavailable=true, two-attempt bounded recovery, and no revision/model escalation. Commit e935c988 passes the combined 7-test scheduler/run-page selection, Ruff, and byte-compilation; controller-owned push CI remains the merge gate. cost=$0.66
- 2026-09-10T16:51:28+00:00 automated review: approve — Run pages clearly distinguish runner completion from validation success while preserving incomplete and unassociated outcomes. cost=$0.35
- 2026-09-10T17:03:51+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T17:05:23+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/448
