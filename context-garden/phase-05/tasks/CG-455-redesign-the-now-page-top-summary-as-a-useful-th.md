---
id: CG-455
title: Redesign the Now page top summary as a useful thematic measurement
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-425
priority: 1
difficulty: hard
reading:
- docs/design/now-1.md
- src/garden/web/templates/_now1_macros.html
- src/garden/web/templates/_now1_head.html
- src/garden/web/templates/now1.html
- src/garden/now1.py
- tests/test_now1.py
branch: garden/cg-455-redesign-the-now-page-top-summary-as-a-useful-th
pr: https://github.com/joshmarcus/context-garden/pull/354
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T14:08:20+00:00'
created: '2026-09-08T21:26:22+00:00'
updated: '2026-09-09T14:57:29+00:00'
---

## Goal

Replace the loose paragraph directly beneath the Now heading with a beautiful, concise and useful summary of the garden's current state. Explore a thematic measurement or another strong visual summary that helps a person understand what matters within five seconds.

## Context

The current `five(snap)` macro combines run and review slots, queued work, phase progress and period cost into one long line of prose. The owner finds it visually arbitrary and not useful enough for the most prominent position on the page.

Use substantial design judgment. A measurement can draw on the herbarium/growth language, but it must represent real, explainable data. A different concise composition is welcome if it serves the page better. Do not invent a health, readiness or quality score.

CG-425 owns the page-wide hierarchy between Now, Next, Where we are and The last period. This task follows CG-425 and owns only the top summary beneath the page title, plus the smallest data/model changes needed to make that summary honest and live. Build on CG-425 rather than replacing its section work.

## Acceptance criteria

- [ ] The top of `/now` presents an intentional, beautiful summary that replaces the undifferentiated sentence and communicates the most useful current facts within five seconds. Labels, units and time windows make every value understandable without opening another page.
- [ ] Any thematic measurement has a documented, testable basis in authentic Garden state and never implies an invented health, quality or readiness score. The summary stays synchronized with live updates and agrees with the detailed Now, Next, phase and period regions.
- [ ] The summary prioritizes actionable conditions such as a pause, constrained capacity or owner attention without turning ordinary variation into an alarm. Existing useful links and the page's read-only behavior remain available.
- [ ] The design is semantic, keyboard and screen-reader legible, does not depend on color alone, and remains composed at representative populated, sparse and paused states at 1280px and 390px in light and dark appearances.
- [ ] Focused model/template regressions and an actual disposable served interaction on the reviewed head verify the affected top summary, live refresh, sparse/empty behavior and a relevant failure followed by recovery. Preserve inspectable desktop/mobile captures when available; missing artifact metadata alone is advisory, while a real render or data error remains blocking.

## Out of scope

- Redesigning the major section headings or page-wide spacing already owned by CG-425.
- Changing scheduler admission, task status semantics, costs or other source measurements merely to improve the presentation.
- Adding an opaque composite score, decorative random text, or unrelated page redesign.

## Log

- 2026-09-08: Owner requested replacing the random text block at the top of Now with a more beautiful and useful summary, possibly a thematic measurement. Scoped as a focused follow-up to CG-425 so its section-hierarchy work remains intact.
- 2026-09-08T21:27:58+00:00 approved (cli)
- 2026-09-09T00:36:25+00:00 dispatched work run 20260909T003625Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15844 tokens)
- 2026-09-09T01:10:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/354 (base main): Replaced the Now page's undifferentiated sentence with a responsive field reading of capacity, next dispatch, current phase progress, and selected-period activity. Explicit pauses and owner-attention items lead the summary, while ordinary variation remains neutral. cost=$1.29
- 2026-09-09T03:46:24+00:00 automated review requested changes: The summary is visually strong, but it can become stale when live configuration changes alter displayed capacity. cost=$0.40
- 2026-09-09T03:46:34+00:00 dispatched revise run 20260909T034634Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18338 tokens)
- 2026-09-09T03:55:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T04:01:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: The Now summary now refreshes whenever profile changes, config reloads, or direct overrides can alter displayed capacity. Verified with 28 focused tests, clean Ruff lint, and a disposable served-browser replay covering populated, sparse, paused, failure/recovery, 1280px/390px, and light/dark states. cost=$0.95
- 2026-09-09T04:05:29+00:00 automated review: approve — The redesigned summary is clear, authentic, actionable, and responsive; the prior stale-capacity defect is fixed. cost=$0.32
- 2026-09-09T04:11:05+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T04:42:15+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T09:45:20+00:00 automated review: approve — The redesigned summary is clear, authentic, actionable, responsive, and remains synchronized after capacity configuration changes. cost=$0.46
- 2026-09-09T09:46:58+00:00 CI failure
- 2026-09-09T09:47:29+00:00 dispatched revise run 20260909T094728Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18222 tokens)
- 2026-09-09T09:59:15+00:00 worker found no change to make: The implementation is already correct and the reported failing state is a duplicate-run/environment issue, not a reproducible branch defect. The separate `actions` analyser error is caused by its unavailable GitHub CLI authentication.; reconciling with checks and a fresh review
- 2026-09-09T10:02:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: Investigated the CI report at commit 7507b41a. The same SHA has a successful pull-request workflow alongside the failed push workflow, and a supervised full local run passed 1,827 tests with 4 skipped and 4 stress tests deselected; focused Now tests and Ruff also pass. cost=$1.26
- 2026-09-09T10:03:16+00:00 CI failure
- 2026-09-09T10:03:32+00:00 dispatched revise run 20260909T100331Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18450 tokens)
- 2026-09-09T10:05:58+00:00 worker found no change to make: No reproducible implementation defect exists to fix. The reported actions error requires runner GitHub authentication, while the applicable product tests pass on the reviewed source.; reconciling with checks and a fresh review
- 2026-09-09T10:05:59+00:00 automated review: approve — The field reading is clear, authentic, actionable, and responsive; the prior stale-capacity issue is resolved. cost=$0.44
- 2026-09-09T10:09:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: Investigated the reported CI state at unchanged head 7507b41a. The Now suite passes 29 tests, Ruff and diff checks are clean, and existing exact-source interaction evidence covers live refresh, sparse, paused, failure/recovery, responsive, and light/dark behavior; the actions analyser failure is an unauthenticated GitHub CLI environment error rather than a branch defect. cost=$0.34
- 2026-09-09T10:11:22+00:00 CI failure
- 2026-09-09T10:12:39+00:00 automated review: approve — The redesigned field reading is clear, authentic, actionable, responsive, and remains synchronized after capacity configuration changes. cost=$0.39
- 2026-09-09T10:18:23+00:00 dispatched revise run 20260909T101823Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18787 tokens)
- 2026-09-09T10:20:47+00:00 worker found no change to make: No reproducible implementation defect exists to fix; changing source would not resolve the runner's missing GitHub authentication.; reconciling with checks and a fresh review
- 2026-09-09T10:22:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: The existing Now summary implementation is correct at 7507b41acdfaf65b8906aa7c8cace3e09ffdc557. The focused Now suite passes 29 tests, Ruff and diff/conflict checks are clean, and the reported actions analyser error is caused by unavailable GitHub CLI authentication rather than a branch defect. cost=$0.38
- 2026-09-09T10:23:31+00:00 CI failure
- 2026-09-09T10:23:41+00:00 dispatched revise run 20260909T102341Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18996 tokens)
- 2026-09-09T10:24:44+00:00 automated review: approve — The Now summary communicates live capacity, next work, phase progress, and period activity clearly while giving explicit pauses and owner attention appropriate prominence. cost=$0.42
- 2026-09-09T10:34:34+00:00 worker found no change to make: The reported test failure does not reproduce, and the actions analyser error is caused by unavailable GitHub CLI authentication; changing product source would not resolve it.; reconciling with checks and a fresh review
- 2026-09-09T10:35:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: The reviewed Now summary implementation is correct at 7507b41acdfaf65b8906aa7c8cace3e09ffdc557. The focused Now suite passed 29 tests, the full ordinary suite passed 1,827 tests with 4 skipped and 4 stress tests deselected, Ruff passed, and the worktree remains clean. cost=$0.68
- 2026-09-09T10:37:14+00:00 CI failure
- 2026-09-09T10:37:32+00:00 dispatched revise run 20260909T103731Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19269 tokens)
- 2026-09-09T10:38:38+00:00 automated review: request_changes — The field reading is clear and well composed, but its period value can diverge from the live detailed region after an automerge. cost=$0.50
- 2026-09-09T10:40:59+00:00 worker found no change to make: No reproducible branch defect exists to fix. `gh auth status` reports that no GitHub hosts are authenticated, so changing product source would not resolve the failing actions analyser.; reconciling with checks and a fresh review
- 2026-09-09T10:42:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: Investigated the repeated CI report at HEAD 7507b41acdfaf65b8906aa7c8cace3e09ffdc557. The focused Now suite passes 29 tests, Ruff passes, diff/conflict checks are clean, and representative desktop/mobile captures remain composed; the actions analyser failure reproduces solely as unavailable GitHub CLI authentication. cost=$0.47
- 2026-09-09T10:43:45+00:00 CI failure, but 6 revision rounds already used; needs a human
- 2026-09-09T10:45:02+00:00 automated review: request_changes — The visual redesign is clear and well composed, but the selected-period reading can become stale after an automerge. cost=$0.40
- 2026-09-09T11:04:11+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-09T11:05:20+00:00 dispatched revise run 20260909T110520Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19638 tokens)
- 2026-09-09T11:10:14+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:11:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: The Now summary's selected-period reading now refreshes atomically with the detailed period region, preventing automerges and other period events from leaving the two values out of sync. Verified with 29 focused tests, clean Ruff lint, and a disposable served replay covering populated, sparse, paused, failure/recovery, 1280px/390px, and light/dark states. cost=$1.00
- 2026-09-09T11:14:40+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: focused regressions and served interac; run `garden triage CG-455 --changes "<feedback>" to unblock`
- 2026-09-09T12:44:39+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-09T12:44:56+00:00 dispatched revise run 20260909T124456Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21024 tokens)
- 2026-09-09T12:52:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:55:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: Shared HEAD/PERIOD events now avoid the standalone head refresh and update the summary and detailed period ledger only through the paired fetch. Current-head focused tests and lint pass; the disposable served-browser replay verified atomic failure/recovery behavior plus populated, sparse, paused, responsive, light, and dark states. cost=$1.06
- 2026-09-09T13:04:52+00:00 automated review requested changes: The Now summary itself is clear and its focused checks pass, but the PR also includes a large unrelated command-host and scheduler implementation that must be removed from this task's branch. cost=$0.27
- 2026-09-09T13:09:17+00:00 dispatched revise run 20260909T130916Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20944 tokens)
- 2026-09-09T13:23:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:26:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: Rebuilt the branch on the intended CG-425/current-main base so the PR now contains only the CG-455 Now summary implementation, documentation, focused tests, replay tooling, and captures. Verified 28 focused tests, clean Ruff lint, a passing disposable served-browser replay with atomic failure/recovery, and composed populated, sparse, and paused views at desktop/mobile in light and dark. cost=$0.73
- 2026-09-09T13:28:44+00:00 automated review requested changes: The redesigned summary is clear and well scoped, but shared period/head events delay its refresh for up to 60 seconds, leaving prominent live facts stale. cost=$0.30
- 2026-09-09T13:29:10+00:00 dispatched revise run 20260909T132910Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21578 tokens)
- 2026-09-09T13:35:16+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:36:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: Shared head/period events now refresh the Now summary and detailed ledger immediately and atomically, eliminating the 60-second stale window. Commit 358cb6cd passed 28 focused tests, Ruff, and an exact-head disposable served-browser replay covering prompt refresh, failure/recovery, populated, sparse, paused, desktop/mobile, and light/dark states. cost=$0.70
- 2026-09-09T13:39:21+00:00 automated review requested changes: The field reading is visually clear and the period/head refresh is now immediate and atomic, but the duplicated Next and phase readings can still diverge from their detailed regions. cost=$0.40
- 2026-09-09T13:42:14+00:00 dispatched revise run 20260909T134213Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21758 tokens)
- 2026-09-09T13:48:54+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:51:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: The Now summary now derives its live-refresh set from the Next and Where event maps, so queue and phase changes cannot update their detailed regions while leaving duplicated top readings stale. At final head e8404ecc, 28 focused tests and Ruff passed, and the disposable served-browser replay passed with explicit Next-only and phase-only refresh checks plus populated, sparse, paused, failure/recovery, desktop/mobile, and light/dark coverage. cost=$0.75
- 2026-09-09T14:07:58+00:00 automated review requested changes: The redesigned summary is clear, but its owner-attention count can remain stale after a live needs-human event. cost=$0.27
- 2026-09-09T14:08:20+00:00 dispatched revise run 20260909T140820Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22037 tokens)
- 2026-09-09T14:25:13+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:26:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/354: Owner-attention events now refresh the top summary alongside the detailed Now region, preventing needs-human counts from becoming stale. Verified at commit 2e743f54 with 28 focused tests, clean Ruff lint, and an exact-head disposable browser replay covering needs-human refresh, failure/recovery, populated, sparse, paused, desktop/mobile, and light/dark states. cost=$1.00
- 2026-09-09T14:50:28+00:00 automated review: approve — The redesigned field reading is clear, authentic, actionable, responsive, and the prior stale owner-attention defect is resolved. cost=$0.33
- 2026-09-09T14:55:57+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T14:57:29+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/354
