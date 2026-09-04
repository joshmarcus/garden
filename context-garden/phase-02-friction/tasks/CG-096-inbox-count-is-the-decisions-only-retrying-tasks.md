---
id: CG-096
title: Inbox count is the decisions only; retrying tasks show but do not count
status: ready
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
created: '2026-09-04T21:02:13+00:00'
updated: '2026-09-04T21:02:14+00:00'
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
