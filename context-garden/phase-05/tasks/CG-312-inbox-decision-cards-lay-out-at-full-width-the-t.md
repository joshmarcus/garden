---
id: CG-312
title: 'Inbox decision cards lay out at full width: the text column no longer collapses to one word per
  line and the action buttons no longer overlap the evidence list'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/web/templates/inbox.html
- src/garden/web/templates/base.html
- src/garden/web/templates/task.html
- src/garden/web/pages/inbox.py
- src/garden/inbox.py
- tests/test_web.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-312-inbox-decision-cards-lay-out-at-full-width-the-t
pr: https://github.com/joshmarcus/context-garden/pull/211
attempts: 1
last_dispatched_at: '2026-09-06T03:08:43+00:00'
created: '2026-09-06T02:03:53+00:00'
updated: '2026-09-06T03:08:43+00:00'
---

## Goal

A "Needs a decision" card on the Inbox reads as one card: the title and the reason run the full width of the card, the evidence list (runs, the last review) sits under them at a readable measure, and the action buttons (Continue the loop, Discuss, Cancel, Open PR) sit in their own row with their explanations beside them, never over the text. The same holds for every card group on the Inbox and on the task page's decision panel, at 1280 wide and on a phone.

## Context

Seen by the owner on 2026-09-06 01:58Z on the live Inbox (CG-242's failed-worker card): the card's text column had collapsed to a few characters wide, so the title "Hold untrusted config changes before live reload", the reason and the run list wrapped one word per line down the page, while the action buttons were drawn on top of the run list with their explanations to the right. The card grid gives the text column no minimum width and the actions column is absolutely placed or floated over it; a long unbreakable token (a run id such as 20260906T010102Z-revise) makes it worse. The Inbox is the page the owner acts from; it must be right before the Now page ships.

## Acceptance criteria

- [ ] On the Inbox, every card's text column has a minimum width (the run ids and reason text wrap by word, never one word per line) and the actions render in a row below or beside the text without overlapping it, verified at 1280 and 390 wide.
- [ ] The task page's decision panel uses the same card layout, so the two pages agree.
- [ ] A test renders the Inbox with a failed-worker card carrying a long run id and a long reason and asserts the actions and the evidence are in separate containers with no absolute positioning over the text (structure test), and `garden walkthrough` captures the Inbox with such a card.
- [ ] No Set buttons, no new colours; the botanical theme's type and spacing are kept.

## Log

- 2026-09-06T02:03:53+00:00 approved (cli)
- 2026-09-06T02:46:36+00:00 dispatched work run 20260906T024545Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11337 tokens)
- 2026-09-06T03:05:49+00:00 opened https://github.com/joshmarcus/context-garden/pull/211 (base main): Decision cards now keep text, evidence, and actions in separate responsive rows on the Inbox and task page. Long run IDs wrap safely, and the walkthrough capture includes a failed-worker decision card. cost=$1.06
- 2026-09-06T03:07:57+00:00 automated review requested changes: The action-column overlap is removed, but the Inbox text track still has a zero minimum width, so the stated minimum-width guarantee is not implemented. Focused regression tests and Ruff pass. cost=$0.15
- 2026-09-06T03:08:43+00:00 dispatched revise run 20260906T030840Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11834 tokens)
