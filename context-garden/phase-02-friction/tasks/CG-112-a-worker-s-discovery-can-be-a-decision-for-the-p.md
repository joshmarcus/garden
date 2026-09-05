---
id: CG-112
title: A worker's discovery can be a decision for the person, not only a new task
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/inbox.py
- src/garden/web/templates/inbox.html
- docs/worker-protocol.md
branch: garden/cg-112-a-worker-s-discovery-can-be-a-decision-for-the-p
pr: https://github.com/joshmarcus/context-garden/pull/55
attempts: 1
last_dispatched_at: '2026-09-04T22:10:44+00:00'
created: '2026-09-04T21:29:53+00:00'
updated: '2026-09-04T23:58:30+00:00'
---

## Goal

When a worker notices something that calls for a person's decision rather than new work, it reaches the person as a decision card with Accept and Reject, not as a draft task that has to be read, understood and cancelled.

## Context

Asked during the first live run. CG-092's worker noticed that CG-107 described the same change as CG-092 and filed it as a discovered task, CG-110, titled "CG-107 duplicates CG-092". That was exactly right as an observation and wrong as a task: it sat in the draft list next to real work, and the person had to open it, agree, cancel CG-107 by hand and then cancel CG-110 too. The result contract's `discovered` list takes only tasks. Give each discovered item a `kind`: `task` (as today), `duplicate` (`of` and `duplicates`, proposing that one be cancelled in favour of the other), `cancel` (a task the worker believes is obsolete, with a reason) and `note` (information for the phase's friction record, no action). The decision kinds become Inbox cards under "Needs a decision" that quote the worker's reason: Accept cancels the named task with a note that records who proposed it and from which run; Reject dismisses the card and logs the disagreement on the task. Notes go to the friction record and never make a card. `garden inbox` and the digest list decisions the same way. The brief's result section shows the shapes. Same family as CG-100 (won't-do and no-change results) and CG-079 (suggested changes to a task); reuse the card shape from CG-045.

## Acceptance criteria

- [ ] a `duplicate` or `cancel` discovery makes a decision card, not a draft task; Accept cancels the named task with the provenance in its log; Reject logs the disagreement.
- [ ] a `note` discovery reaches the friction record and makes no card.
- [ ] a discovery with no `kind` is still a task, so existing workers keep working.
- [ ] tests for each kind with the fake harness.

## Log

- 2026-09-04T21:40:27+00:00 dispatched work run 20260904T214026Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~9711 tokens)
- 2026-09-04T21:53:33+00:00 discovered work filed: CG-114
- 2026-09-04T21:54:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/55 (base main): Discovered items now carry a `kind`: `task` files work as before, while `duplicate`/`cancel` become Accept/Reject decision cards (Accept cancels the named task with provenance, Reject logs the disagreement) and `note` goes to the phase friction record with no card. Surfaced in the web Inbox, `garden inbox`/`garden decide`, and the digest; covered by fake-harness tests for each kind. cost=$6.75
- 2026-09-04T21:57:17+00:00 automated review: approve — Adds a `kind` to discovered items so duplicate/cancel become Accept/Reject decision cards and note goes to the friction record, with task remaining the default. All four acceptance criteria are implemented and tested; full suite and ruff pass. cost=$1.01
- 2026-09-04T21:57:29+00:00 3 new review item(s)
- 2026-09-04T22:03:05+00:00 dispatched revise run 20260904T220305Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~11542 tokens)
- 2026-09-04T22:10:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/55: Addressed both P1 review items: accepting a duplicate decision now repoints the cancelled task's dependents onto the retained `of` task so they aren't left permanently blocked, and the TUI inbox now routes a/x on a decision row through resolve_decision() (accept/reject) instead of cancelling or retrying the target task. Added tests for each and updated the worker-protocol doc. cost=$2.91
- 2026-09-04T22:10:43+00:00 PR conflicts with main (docs/worker-protocol.md, src/garden/brief.py, src/garden/scheduler.py); revise run will rebase and resolve
- 2026-09-04T22:10:44+00:00 dispatched revise run 20260904T221043Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~11346 tokens)
- 2026-09-04T22:17:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/55: Rebased the branch onto origin/main and resolved all conflicts (docs/worker-protocol.md, src/garden/brief.py, src/garden/scheduler.py, src/garden/cli.py, tests/fake_claude.py, and an add/add collision on tests/test_decisions.py) keeping both sides' intent. Full suite (295 passed, 3 skipped) and ruff are green. cost=$2.96
- 2026-09-04T23:58:30+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/55
