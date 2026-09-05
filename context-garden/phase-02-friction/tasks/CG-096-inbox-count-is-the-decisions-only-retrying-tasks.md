---
id: CG-096
title: Inbox count is the decisions only; retrying tasks show but do not count
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/inbox.py
- src/garden/web/app.py
- src/garden/web/templates/inbox.html
- src/garden/web/templates/base.html
branch: garden/cg-096-inbox-count-is-the-decisions-only-retrying-tasks
pr: https://github.com/joshmarcus/context-garden/pull/76
attempts: 1
last_dispatched_at: '2026-09-05T00:39:21+00:00'
created: '2026-09-04T21:02:13+00:00'
updated: '2026-09-05T00:44:13+00:00'
---

## Goal

The Inbox's count (the badge in the rail, the "N need you" figure, the digest line) counts only items that need a person's decision; the "Retrying" group stays on the page as information but does not count, and the same rule applies to any other informational group.

## Context

Asked during the first live run. CG-035 added the "Retrying" group so a first failed attempt is no longer invisible; it works, but every task in it now adds to the Inbox count, so "9 need you" may be three decisions and six retries the loop is handling by itself, which teaches the person to ignore the number. Give each Inbox group a kind: `decision` (question, triage, review, attention, budget, approve) or `notice` (retrying, and later the upgrade-available and suggestions-pending lines). The count, the rail badge and the digest use decisions only; notices render under their own subdued heading with their own count in the heading ("Retrying · 6, no action needed"). The TUI's Inbox tab follows the same rule.

## Acceptance criteria

- [ ] the rail badge and "need you" figure exclude notice groups; the Retrying group still renders with its own count.
- [ ] `garden inbox` and `garden digest` print decisions and notices separately.
- [ ] tests for the counts with a garden that has both kinds.

## Log

- 2026-09-04T21:02:14+00:00 approved
- 2026-09-04T22:56:54+00:00 dispatched work run 20260904T225645Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~11586 tokens)
- 2026-09-04T23:06:42+00:00 opened https://github.com/joshmarcus/context-garden/pull/76 (base main): Inbox groups now carry a decision/notice kind; the rail badge, "need you" KPI, garden inbox, garden digest and the TUI status bar all count decisions only, while notice groups (retrying, tool upgrade) still render under their own subdued heading with their own count. Added tests covering the split across web, CLI and TUI; full suite and lint pass. cost=$6.96
- 2026-09-04T23:09:37+00:00 automated review: approve — Cleanly implements the decision/notice split across web badge/KPI, garden inbox, garden digest and the TUI status bar; all three acceptance criteria are met and tested, lint and targeted tests pass. cost=$1.08
- 2026-09-05T00:02:22+00:00 PR conflicts with main (src/garden/tui/app.py); revise run will rebase and resolve
- 2026-09-05T00:39:21+00:00 dispatched revise run 20260905T003920Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~9557 tokens)
- 2026-09-05T00:44:13+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/76: Rebased CG-096 onto main, resolving conflicts in src/garden/tui/app.py (merged the notice-dimming/decision-count logic with main's decision-key accept/reject row handling) and src/garden/web/templates/inbox.html (combined the inbox_count KPI with main's running/max_parallel display). Full test suite (373 passed) and ruff lint pass. cost=$1.16
