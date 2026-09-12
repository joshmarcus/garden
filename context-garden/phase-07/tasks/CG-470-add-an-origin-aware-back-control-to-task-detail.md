---
id: CG-470
title: Add an origin-aware back control to task detail
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- context-garden/product.md
- docs/design.md
- docs/architecture.md
branch: garden/cg-470-add-an-origin-aware-back-control-to-task-detail
pr: https://github.com/joshmarcus/context-garden/pull/366
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T15:13:18+00:00'
created: '2026-09-09T11:04:11+00:00'
updated: '2026-09-09T15:26:22+00:00'
---

## Goal

Add a small, subtle, accessible `‹` back control in the upper-left of the task detail page when the user arrived from another page within Garden. Return to the actual in-app origin, preserving its query string and filter state.

## Acceptance criteria

- [ ] A task detail reached from another Garden page shows a small `‹` back control in the upper-left, using the established task-detail visual language.
- [ ] Activating it returns to the actual originating Garden URL, including query parameters and filter state.
- [ ] A direct visit, bookmark, reload, external referrer, malformed origin, or new-tab visit has safe behavior and never navigates outside Garden; hide the control or use an appropriate safe in-app fallback.
- [ ] The control has an accessible name, visible keyboard focus, and a touch target that remains usable without making the control visually prominent.
- [ ] Existing task-detail navigation and narrow/mobile layouts remain usable.

## Scope

Reuse the existing web UI and navigation patterns. Keep this to the task-detail return control and origin preservation; do not redesign global navigation or task content.

## Log

- 2026-09-09T11:04:11+00:00 approved (owner)
- 2026-09-09T11:05:21+00:00 dispatched work run 20260909T110521Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14469 tokens)
- 2026-09-09T11:11:47+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:13:20+00:00 opened https://github.com/joshmarcus/context-garden/pull/366 (base main): Added and committed an origin-aware task-detail back control that preserves safe in-app query state while hiding for unsafe or absent origins. Verified the focused regression (1 passed) and `.venv/bin/ruff check src tests scripts` (clean). cost=$0.47
- 2026-09-09T11:16:00+00:00 automated review: approve — The origin-aware back control meets the requested behavior without widening scope. cost=$0.22
- 2026-09-09T14:28:28+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T14:44:14+00:00 dispatched revise run 20260909T144414Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15742 tokens)
- 2026-09-09T15:10:37+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:12:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/366: Added the safe origin-aware task-detail back control and incorporated the current-main decision persistence correction. Verified targeted task-detail and decision-publication behavior (3 passed) plus Ruff on commit ca2b335b. cost=$0.41
- 2026-09-09T15:13:15+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/templates/task.html); a rebase agent will resolve it
- 2026-09-09T15:13:18+00:00 dispatched rebase run 20260909T151318Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1294 tokens)
- 2026-09-09T15:15:31+00:00 automated review: request_changes — The back control meets all requested behaviors, but the PR also changes unrelated scheduler decision persistence despite the task’s explicit narrow scope. cost=$0.23
- 2026-09-09T15:19:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/366: Rebased onto origin/main and resolved the task-detail template conflict while preserving owner metadata and the origin-aware back control. cost=$0.02
- 2026-09-09T15:23:33+00:00 automated review: approve — The scoped change safely provides the requested origin-aware task-detail back control. cost=$0.27
- 2026-09-09T15:26:22+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/366
