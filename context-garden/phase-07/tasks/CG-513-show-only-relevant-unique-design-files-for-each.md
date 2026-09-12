---
id: CG-513
title: Show only relevant unique design files for each pull request
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/web/pages/task.py
- src/garden/web/templates/task.html
- src/garden/gitops.py
- tests/test_web.py
branch: garden/cg-513-show-only-relevant-unique-design-files-for-each
pr: https://github.com/joshmarcus/context-garden/pull/425
runner: remote
discovered_from: CG-318
attempts: 1
last_dispatched_at: '2026-09-10T14:03:14+00:00'
created: '2026-09-10T11:09:09+00:00'
updated: '2026-09-10T14:22:32+00:00'
---

## Goal

Make the task page's "Design files in this PR" useful: show only designs actually added or changed by the task's current PR, once each, and link shared repository designs separately when relevant instead of repeatedly presenting them as new PR output.

## Context

Owner reports that the PR design panel repeats the same repository design files across PRs. Specific example PR is requested but not yet supplied. Completed CG-318 originally owns this surface; this is a focused residual follow-up, not another artifact-capture pipeline. Inspect current source first. The RC16 selector uses a local base...branch diff, which needs diagnosis for stale refs and inherited stacked-branch files; this is a hypothesis, not a confirmed root cause.

## Acceptance criteria

- [ ] Derive the panel from the current task/PR source and its correct comparison base, accounting for stale local refs and stacked dependencies; inherited unchanged repository designs do not appear as this PR's design output.
- [ ] Show each changed design once with working safe links to the appropriate revision, distinguish relevant shared references, and omit the panel when there are no relevant changed designs.
- [ ] Preserve intentionally changed designs and genuinely distinct variants; do not delete repository design files or hide differences just because filenames look similar.
- [ ] Add focused fixtures for unchanged shared designs, an actual design modification, inherited parent changes, repeated entries and a task without design changes. Verify the affected task-page behavior and repository lint proportionately.

## Boundaries

No mandatory screenshots or live canaries. Existing artifact security and access checks remain. Do not broaden into all transcript/capture reporting or reimplement completed CG-318. Record the example PR when supplied without making that reference the only reproducible test.

## Log

- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:37:03+00:00 dispatched work run 20260910T113703Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15099 tokens)
- 2026-09-10T11:44:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:46:51+00:00 opened https://github.com/joshmarcus/context-garden/pull/425 (base main): Scoped task design output to the refreshed PR head and recorded PR base, with separately linked shared design references. Verified the full web test file and repository lint; committed as ed5cd00c. cost=$0.95
- 2026-09-10T11:49:29+00:00 automated review requested changes: The refreshed-head and stacked-base behavior is well covered, but deleted design files produce broken links in the PR design panel. cost=$0.27
- 2026-09-10T11:49:38+00:00 dispatched revise run 20260910T114938Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15984 tokens)
- 2026-09-10T11:53:44+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:57:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/425: Excluded deleted design paths from PR output and added a regression case proving the deleted file has no broken head-revision link. Verified exact-head focused task-page coverage and repository lint. cost=$0.39
- 2026-09-10T12:00:25+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/task.py); a rebase agent will resolve it
- 2026-09-10T12:04:16+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: show each changed design once with wor; run `garden triage CG-513 --changes "<feedback>" to unblock`
- 2026-09-10T13:25:04+00:00 triage: changes requested by hand: Preserve current PR/base scoping and deletion handling. Address the repeated concrete pure-rename defect: include rename
- 2026-09-10T13:25:39+00:00 dispatched rebase run 20260910T132538Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1576 tokens)
- 2026-09-10T13:28:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/425: Rebased CG-513 onto origin/main and preserved the PR-scoped unique design-file behavior plus deleted-file handling. cost=$0.02
- 2026-09-10T13:30:58+00:00 automated review requested changes: PR/base scoping, deduplication, deletion handling, and shared-reference separation work, but pure design renames remain omitted from the panel. cost=$0.20
- 2026-09-10T13:31:13+00:00 dispatched revise run 20260910T133113Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16533 tokens)
- 2026-09-10T13:36:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:38:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/425: Design-file diffs now detect pure renames and display only the destination with a valid head-revision link. Verified the focused task-page regression and final repository lint. cost=$0.35
- 2026-09-10T13:41:40+00:00 automated review: approve — PR-scoped design output correctly handles refreshed refs, stacked bases, deduplication, deletions, shared references, and pure renames. cost=$0.24
- 2026-09-10T14:02:22+00:00 triage: changes requested by hand: Both current-head CI34483716586 and34483710217 fail test_web::test_active_worktree_design_files_are_inert_and_visible_fr
- 2026-09-10T14:03:14+00:00 difficulty medium -> hard after 2 substantive revisions; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-10T14:03:14+00:00 dispatched revise run 20260910T140314Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16671 tokens)
- 2026-09-10T14:09:03+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:10:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/425: Restored active-worktree design previews while preserving PR/base scoping, rename handling, deletion filtering, and shared-reference separation. Committed as 54d5c354; the full web suite passed with 158 tests and repository lint passed. cost=$0.64
- 2026-09-10T14:14:07+00:00 automated review: approve — PR-scoped design output correctly handles refreshed refs, stacked bases, deduplication, deletions, renames, shared references, and active worktrees. cost=$0.33
- 2026-09-10T14:20:55+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T14:22:32+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/425
