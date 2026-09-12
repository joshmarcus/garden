---
id: CG-256
title: A draft's acceptance criteria and reading list can be edited inline on the task page
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: medium
reading: []
branch: garden/cg-256-a-draft-s-acceptance-criteria-and-reading-list-c
pr: https://github.com/joshmarcus/context-garden/pull/230
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-06T14:12:18+00:00'
created: '2026-09-05T23:58:10+00:00'
updated: '2026-09-06T16:13:44+00:00'
---

## Goal

**User value:** the approve card says 'fix the brief' but offers no way to do it; today the only in-app path costs an edit run.

**Why now:** the brief gate (CG-193) creates the refusal; this closes the loop with the same brief_gaps check on save.

**Size:** medium. **Depends on:** CG-193, CG-190 (merged).

## Context

A refusal without a repair path sends the owner to a text editor. This adds inline editing of acceptance criteria and reading list on the task page, gated by the same brief_gaps check used on approve.

## Acceptance criteria

- [ ] When brief_gaps flags missing or short acceptance criteria or reading list, the approve card on the task page shows an inline editor instead of only the refusal message.
- [ ] The inline editor lets the owner add or edit '## Acceptance criteria' checkboxes and reading-list paths directly on the task page.
- [ ] Saving the inline edit re-runs the same brief_gaps check CG-193 uses on approve, and the approve card reflects the new pass/fail state without a page reload.
- [ ] A reading-list path that doesn't exist in the product checkout is rejected on save with an inline error, matching brief_gaps' existing path check.
- [ ] A test (e.g. test_inline_edit_clears_brief_gate) covers: a draft that fails brief_gaps on acceptance criteria, the owner editing inline and saving, and the approve card unblocking.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-245 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002112Z-edit) cost=$0.10
- 2026-09-06T00:24:03+00:00 approved (cli)
- 2026-09-06T13:16:31+00:00 dispatched work run 20260906T131505Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~7768 tokens)
- 2026-09-06T13:49:40+00:00 pre-PR checks failed (test) (still failing after a rebase onto `main`); no PR opened yet; revise run will fix cost=$1.30
- 2026-09-06T14:12:18+00:00 dispatched revise run 20260906T141200Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9202 tokens)
- 2026-09-06T15:02:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/230 (base main): Inline draft brief editing remains in place, and the pre-PR CLI command-registration conflict is fixed. Both Now pages are selectable and all required checks pass. cost=$0.31
- 2026-09-06T15:04:18+00:00 automated review requested changes: The inline brief editor satisfies the task criteria and focused tests pass, but the PR includes unrelated Now CLI behavior that should be separated. The description also omits test verification and phase context. cost=$0.27
- 2026-09-06T16:13:44+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/230
