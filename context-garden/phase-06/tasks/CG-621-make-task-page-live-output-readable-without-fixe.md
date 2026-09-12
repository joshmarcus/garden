---
id: CG-621
title: Make task-page live output readable without fixed-width truncation
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/web/templates/_stdout.html
- src/garden/web/templates/task.html
- src/garden/web/templates/base.html
- src/garden/web/pages/task.py
branch: garden/cg-621-make-task-page-live-output-readable-without-fixe
pr: https://github.com/joshmarcus/context-garden/pull/487
attempts: 2
last_dispatched_at: '2026-09-11T05:44:35+00:00'
created: '2026-09-11T03:30:06+00:00'
updated: '2026-09-11T06:36:07+00:00'
---

## Goal

Make the task page's Live output panel readable: users can read complete displayed entries and scroll long output without losing text or their place during updates.

## Context

Owner request: "live output on task page is cut off at a fixed width. can we make it readable (and probably scrollable)?"

Inspection of the currently served RC19 template confirms two independent causes. src/garden/web/templates/_stdout.html slices many Claude and Codex text, command and result fields to [:160], and renders them with overflow:hidden, text-overflow:ellipsis and white-space:nowrap. The panel in task.html polls the stdout partial every three seconds. Adding a scrollbar alone cannot recover characters removed by the template.

CG-009 originally supplied live output; CG-073 covers complete run history and CG-427 added Codex transcript rendering. This task fixes the task page's live-output readability and preserves those existing capabilities. Determine whether accepted main already addresses any part of the defect before changing source. Change the product repository, not the installed runtime.

## Acceptance criteria

- [ ] Remove silent fixed-character truncation from displayed live entries, including supported Claude/Codex assistant text, commands and results. Complete entry content must be accessible from the task page. Any deliberate large-output limit must be explicit and offer a usable way to inspect the remainder; do not replace [:160] with another arbitrary silent cutoff.
- [ ] Use a readable layout that preserves meaningful newlines and whitespace. Keep long lines accessible through horizontal scrolling or an explicit wrap option; constrain overflow to the output panel rather than widening or clipping the whole task page.
- [ ] Provide usable vertical scrolling for longer output. Preserve the user's scroll position while they are reading earlier or horizontally scrolled content during live polling. Follow new output only when already following the tail or when the user explicitly requests it.
- [ ] Keep content selectable and copyable, with mouse, touch and keyboard access to overflowing content. The panel remains readable on narrow and wide task-page layouts.
- [ ] Preserve existing escaping/redaction and bounded recent-event loading. Do not render raw HTML from model/tool output or fetch the entire run archive on every update. Keep the existing full transcript/history route available.
- [ ] Verify with representative long text, a command and result exceeding 160 characters, multiline output, a long unbroken line, and a live refresh while scrolled away from the tail. Use focused rendering/interaction checks appropriate to the change and preserve both Claude and Codex event support.

## Scope

A focused task-page rendering and polling fix. No new terminal runtime, Herdr work, service restart, deployment, global page redesign or replacement transcript/history system. Use proportionate verification under the existing owner policy.

owner_request_key: owner-task-live-output-readable-scrollable-20260911

## Log

- 2026-09-11T03:32:44+00:00 approved (web)
- 2026-09-11T03:37:01+00:00 dispatched work run 20260911T033657Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15426 tokens)
- 2026-09-11T03:53:54+00:00 temporary runner hold by delegated_operator: RC19 local startup failed before model output with the already-fixed read-only harness home error. Preserve original033657 bytes and actual failure; hold a retry until root activates the accepted RC20 runtime, then release this specific hold to the original local default without resetting the run history.
- 2026-09-11T03:53:54+00:00 attempt 1 failed: no GARDEN_RESULT in worker output (WARNING: proceeding, even though we could not create PATH aliases: Permission denied (os error 13)
Error: failed to initialize in-process app-server client: Permission denied (os error 13)); will retry
- 2026-09-11T05:44:05+00:00 temporary runner hold released by delegated_operator: RC19 local startup failed before model output with the already-fixed read-only harness home error. Preserve original033657 bytes and actual failure; hold a retry until root activates the accepted RC20 runtime, then release this specific hold to the original local default without resetting the run history.
- 2026-09-11T05:44:35+00:00 dispatched work run 20260911T054432Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~2646 tokens)
- 2026-09-11T06:02:11+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T06:13:32+00:00 opened https://github.com/joshmarcus/context-garden/pull/487 (base main): Live task and run output now retains complete entries in bounded, keyboard-scrollable panels, preserving reader position across polling. Verified rendering, real browser polling behavior, 1280/390 light/dark layouts, the focused web suite, and lint. cost=$1.23
- 2026-09-11T06:24:45+00:00 automated review: approve — The focused change removes silent truncation and makes live task/run output fully scrollable while preserving reader position during polling. cost=$0.27
- 2026-09-11T06:36:07+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/487
