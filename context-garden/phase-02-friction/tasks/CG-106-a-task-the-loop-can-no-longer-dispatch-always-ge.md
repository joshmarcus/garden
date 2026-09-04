---
id: CG-106
title: A task the loop can no longer dispatch always gets a card
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/inbox.py
- tests/test_scheduler.py
branch: garden/cg-106-a-task-the-loop-can-no-longer-dispatch-always-ge
pr: https://github.com/joshmarcus/context-garden/pull/53
attempts: 1
last_dispatched_at: '2026-09-04T21:54:10+00:00'
created: '2026-09-04T21:17:43+00:00'
updated: '2026-09-04T22:03:01+00:00'
---

## Goal

No task sits in `changes_requested` (or any non-terminal status) with nothing scheduled and nothing on the Inbox. If the loop cannot dispatch the next round, the task gets a card that says why and what to do.

## Context

Found on the first live run, twice in one hour. `dispatch_ready` queues a revise round only when `pending_feedback` is non-empty, `needs_human` is unset and `revisions < max_revisions`. CG-037 reached three revision rounds (a rebase, a description round and a check poisoned by the garden's own environment); the pre-PR-checks-failed path for a task with an open PR does not look at the cap, so it left the task in `changes_requested` with feedback and no `needs_human`, and the queue skipped it forever. CG-090's tests check was killed with the server (`exit -15`) and recorded with empty output, so `pending_feedback` was `""` and the queue skipped it too. Neither task appeared on the Inbox; `garden status` showed two `chg` and nothing else. Make one rule: whenever a task enters `changes_requested`, either a revise round is dispatchable (feedback present, cap not reached) or `needs_human` is set with the reason. Add a tick-time audit that finds any non-terminal task with no active run and no dispatchable round and flags it (`needs_human` "stuck: <reason>"), so state edits, killed checks and future bugs surface as cards instead of silence. The card's actions: resume with one more round (resets the cap by one, with a note), or send back with a note (CG-045's shape). A killed or empty check result is recorded as "check did not finish", not as a failure with no text.

## Acceptance criteria

- [ ] pre-PR failure at the cap sets `needs_human` like the review path does.
- [ ] an empty or signalled check result is never stored as empty feedback; the task gets a card.
- [ ] the tick audit flags a non-terminal task with no active run and no dispatchable round; a test seeds that state by hand and sees the card.
- [ ] `garden status` counts stuck tasks in the attention column.

## Log

- 2026-09-04T21:26:53+00:00 dispatched work run 20260904T212653Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~8405 tokens)
- 2026-09-04T21:38:50+00:00 opened https://github.com/joshmarcus/context-garden/pull/53 (base main): Made changes_requested self-consistent: pre-PR failure at the revision cap and empty/killed checks now set needs_human instead of leaving a task queued-but-skipped; added a tick-time stuck audit, a retry/triage cap-grant, and an attn column in garden status. cost=$4.66
- 2026-09-04T21:43:01+00:00 automated review: approve — Makes changes_requested self-consistent (cap/empty-check → needs_human), adds a tick-time stuck audit and an attn column; all four acceptance criteria met, 231 tests pass, ruff clean, diff and description are clean and in-scope. cost=$1.16
- 2026-09-04T21:45:19+00:00 3 new review item(s)
- 2026-09-04T21:54:10+00:00 dispatched revise run 20260904T215410Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~10169 tokens)
- 2026-09-04T21:59:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/53: Addressed both Codex P2 review items: checks now classify a signalled (killed) command as 'check did not finish' before trusting any JSON it printed, and scheduler.retry treats a changes_requested task as a revise retry even without a PR so a capped pre-PR failure resumes the revise loop instead of resetting to a work run. Added two regression tests; full suite (233) passes and ruff is clean. cost=$1.60
- 2026-09-04T22:02:54+00:00 automated review requested changes: All four acceptance criteria are met and the code is correct (233 tests pass, ruff clean), but the PR body's 'Review round' section is scar tissue narrating an earlier review round, which fails the description standard. cost=$1.19
- 2026-09-04T22:03:01+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/53
