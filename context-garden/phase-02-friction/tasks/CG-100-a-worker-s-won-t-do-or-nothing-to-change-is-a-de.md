---
id: CG-100
title: A worker's won't-do or nothing-to-change is a decision for the person, not a failure
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/harness.py
- src/garden/inbox.py
- src/garden/model.py
- docs/worker-protocol.md
created: '2026-09-04T21:09:47+00:00'
updated: '2026-09-04T21:09:47+00:00'
---

## Goal

When a worker reports that the task should not be done, or that a revision round has nothing to change, the task goes to the person as a decision with the worker's reasoning; the person accepts or rejects it. Accepted becomes a `wont_do` status of its own; rejected sends the reasoning back with the person's note.

## Context

Asked during the first live run. CG-091's revise round found that the failing check was the environment (it was: see CG-098) and reported that the code was right. The scheduler had one word for that, "worker blocked", and marked the task failed, so the person saw a failure card for a worker that was correct. The card showed the first 140 characters of the log line and nothing else; the worker's reasoning was only in the run's `final.md`. The card and the task page must show the worker's final message in full for this decision. The result contract in `docs/worker-protocol.md` has `done` and `blocked`; add `wont_do` (the task itself should not be done; give `reason`) and `no_change` (this round has nothing to change; give `reason`). Both move the task to `waiting_human` with an Inbox card that quotes the reason and offers Accept and Reject with a note. Accept on `wont_do` sets status `wont_do`, a terminal status that is neither done nor failed, closes the PR if there is one with a comment carrying the reason, and writes the reason to the task file's log. Accept on `no_change` re-runs the checks and continues to the PR or the review as if the round had pushed. Reject sends the task back to a revise round whose brief carries the person's note under a heading such as "The person disagrees". `garden set-status ID wont_do --reason` and `garden answer` do the same from the CLI. Trellis, board and phase tables show `wont_do` with its own glyph and word (keep copy plain; the closing header from CG-078 lists them under "not done"). Overlaps CG-045 (attention cards say what to do): the "nothing to fix, resume" action there is this `no_change` case, so implement it here and let CG-045 point at it.

## Acceptance criteria

- [ ] `wont_do` and `no_change` results move the task to `waiting_human` with a card that shows the reason and Accept/Reject.
- [ ] accept on `wont_do` ends the task in `wont_do`, closes the PR and records the reason; accept on `no_change` resumes the round without a new work run.
- [ ] reject carries the note into the next brief.
- [ ] `wont_do` counts in neither done, failed nor the Inbox count; CLI and web agree.
- [ ] tests for each path with the fake harness.
