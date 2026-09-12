---
id: CG-463
title: Move the serving build to a quiet nav footer detail
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
- src/garden/web/templates/base.html
- src/garden/web/templates/inbox.html
- src/garden/web/pages/inbox.py
- src/garden/web/common.py
- src/garden/scheduler/upgrades.py
- tests/test_web.py
- tests/test_upgrade.py
branch: garden/cg-463-move-the-serving-build-to-a-quiet-nav-footer-det
pr: https://github.com/joshmarcus/context-garden/pull/361
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T03:39:49+00:00'
created: '2026-09-09T02:03:27+00:00'
updated: '2026-09-09T16:46:26+00:00'
---

## Goal

Keep the current serving build available for occasional developer troubleshooting without giving it prominent Inbox space. Move the build identifier to the bottom of the left navigation as a small, muted detail.

## Context

The Inbox currently opens with a full-width “Serving build” panel sourced from sched.upgrade_status(), while the shared left rail already ends with secondary scheduler and tick controls. The owner wants build information available but unobtrusive.

Remove the prominent build presentation from the Inbox and place the useful active-build detail at the bottom of the shared left rail. Preserve actionable upgrade/update controls and warnings where they already belong; this task changes the routine build label’s hierarchy, not upgrade behavior. Fit the existing botanical/editorial shell and give the implementer latitude over exact wording, spacing, typography, and whether a pending-update hint belongs beside the active identifier. Keep the detail restrained and developer-oriented.

CG-425’s Now-page hierarchy is complete and CG-455 owns only the Now top summary. This shared-shell/Inbox change does not duplicate either task.

## Acceptance criteria

- [ ] The active serving build or source identifier remains available on every shared-shell page at the bottom of the left navigation/rail, styled as a small muted secondary detail that does not compete with primary navigation, phase links, status warnings, or controls.
- [ ] The prominent “Serving build” panel is removed from the Inbox. Existing upgrade availability, failure, and action behavior remains accurate and actionable; moving the routine identifier does not hide a real update problem or change scheduler/upgrade semantics.
- [ ] The shared rail and Inbox remain composed at desktop and phone widths. The new detail fits the existing footer flow without overlap, overflow, or a new prominent card, and other navigation/mobile behavior is preserved.
- [ ] Add focused model/template/page coverage for the moved context and absence of the old Inbox panel. The implementer and reviewer choose proportionate visual or served verification for this small hierarchy change; no prescribed screenshot matrix is required.

## Out of scope

- ...

## Log

- 2026-09-09T02:03:28+00:00 approved (web)
- 2026-09-09T02:06:26+00:00 Owner-requested small build detail uses existing AWS capacity; preserve local shared limit one.
- 2026-09-09T02:23:21+00:00 dispatched work run 20260909T022321Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~13988 tokens)
- 2026-09-09T02:55:47+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T03:17:15+00:00 check did not run (20260909T025559Z-check): idle 21 min (no output or file change); will retry
- 2026-09-09T03:38:08+00:00 opened https://github.com/joshmarcus/context-garden/pull/361 (base main): Serving build identifiers now render as a muted shared-rail footer detail; Inbox retains actionable update notices and controls without the prominent panel. Verified 24 focused upgrade/web tests and lint. cost=$0.46
- 2026-09-09T03:38:20+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_web.py); a rebase agent will resolve it
- 2026-09-09T03:39:49+00:00 dispatched rebase run 20260909T033949Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1349 tokens)
- 2026-09-09T03:50:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/361: Rebased onto origin/main and resolved the tests/test_web.py conflict while preserving both sides' coverage cost=$0.01
- 2026-09-09T03:58:22+00:00 automated review: approve — The serving build is now a restrained shared-rail footer detail, while the Inbox retains actionable upgrade notices and controls. cost=$0.25
- 2026-09-09T04:51:03+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T04:52:05+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T04:59:48+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/361
- 2026-09-09T09:42:43+00:00 automated review could not start: CG-463 is done: #361 was merged at 04:59:48
- 2026-09-09T16:46:26+00:00 automatic review recovery retired because task is done
