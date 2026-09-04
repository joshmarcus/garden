---
id: CG-112
title: A worker's discovery can be a decision for the person, not only a new task
status: ready
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
created: '2026-09-04T21:29:53+00:00'
updated: '2026-09-04T21:29:53+00:00'
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
