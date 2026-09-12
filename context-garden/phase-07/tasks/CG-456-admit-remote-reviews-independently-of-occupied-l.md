---
id: CG-456
title: Admit remote reviews independently of occupied local review capacity
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/__init__.py
- src/garden/scheduler/review.py
- src/garden/scheduler/resources.py
- tests/test_review.py
branch: garden/cg-456-admit-remote-reviews-independently-of-occupied-l
pr: https://github.com/joshmarcus/context-garden/pull/350
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T00:10:54+00:00'
created: '2026-09-08T22:18:25+00:00'
updated: '2026-09-09T01:11:32+00:00'
---

During the six-host AWS restoration, the installed scheduler computes review_slots_free as min(global reviewer slots, local_slots_free). _drain_pending_reviews breaks on that result before considering the task runner. Consequently one legitimate local worker/check can prevent queued AWS reviews from using idle remote hosts. This is separate from lost-review continuation ownership (CG438): a durable queue still cannot advance under the wrong backend admission predicate.

Fix backend-aware admission while preserving the global reviewer ceiling and all local resource gates. Use the actual resolved review backend, including persona/comparison differences. Keep queue ordering, retry accounting and user-facing wait explanations accurate. Do not increase configured local concurrency, alter OS limits, or give checks/remote jobs an unbounded bypass.

## Acceptance criteria

- [ ] With one local slot occupied, a queued eligible remote review can start if global reviewer capacity and its remote execution capacity are available; a queued local review remains deferred without creating a failed run or consuming a round.
- [ ] The global reviewer ceiling still covers remote/local review modes, and every local launch retains atomic physical admission and existing memory/disk/paused-harness gates.
- [ ] Pending review drain and wait explanations use the same backend-aware decisions; a blocked local queue entry cannot incorrectly starve an independently eligible remote review, and true global/remote holds remain visible.
- [ ] Focused mixed-backend regressions demonstrate occupied local capacity, remote admission, global ceiling exhaustion and recovery after local release. Verify actual scheduler dispatch decisions with recorded run backend/rounds; a generic unrelated UI replay is not evidence for this behavior.

## Log

- 2026-09-08T22:18:39+00:00 approved (owner-delegated emergency throughput recovery)
- 2026-09-08T22:19:43+00:00 dispatched work run 20260908T221943Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14002 tokens)
- 2026-09-08T22:44:54+00:00 opened https://github.com/joshmarcus/context-garden/pull/350 (base main): Separated global review concurrency from backend-specific local admission so remote reviews can use available remote workers while local capacity is occupied. Added mixed-backend and atomic-admission race regressions, with local rounds remaining unconsumed while deferred. cost=$1.13
- 2026-09-08T22:51:11+00:00 check did not run (20260908T225007Z-check): exit 2; will retry
- 2026-09-08T22:52:38+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T22:54:00+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T22:54:07+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T22:54:39+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T22:55:48+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T22:57:33+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T22:59:13+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T23:00:50+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T23:02:23+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T23:03:51+00:00 check did not run (20260908T225111Z-check): exit 2; retry also failed; needs human
- 2026-09-08T23:05:03+00:00 triage: marked ready for review (Operator confirmed parser-only replay failure: option-like nonce was passed as a separate argument. )
- 2026-09-08T23:05:18+00:00 check did not run (20260908T225111Z-check): exit 2; will retry
- 2026-09-08T23:06:45+00:00 check did not run (20260908T225111Z-check): exit 2; will retry
- 2026-09-08T23:08:09+00:00 check did not run (20260908T225111Z-check): exit 2; will retry
- 2026-09-08T23:49:25+00:00 automated review requested changes: Backend-aware review admission is correctly separated from the global reviewer ceiling, with local atomic resource admission preserved. The named focused suite passed 211 tests; the supplied external interaction manifest was unavailable in this worktree, but the scheduler outcomes are directly covered by focused regressions. cost=$0.48
- 2026-09-08T23:49:52+00:00 dispatched revise run 20260908T234952Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15178 tokens)
- 2026-09-08T23:58:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/350: Added explicit coverage proving queued remote persona reviews bypass occupied local capacity while preserving the global review ceiling and leaving local rounds unconsumed. The backend-aware scheduler implementation and focused resource-admission suite pass on commit 8862a0d6712c36af11dcc0da43d57294b66ea486. cost=$0.67
- 2026-09-09T00:10:26+00:00 automated review requested changes: Remote review and persona admission is correctly separated from occupied local capacity while retaining the global reviewer ceiling and atomic local resource gates. Focused validation passed at the reviewed head; the supplied HTTP replay is unrelated to this scheduler-only flow, whose meaningful evidence is the disposable scheduler interaction. cost=$0.47
- 2026-09-09T00:10:54+00:00 dispatched revise run 20260909T001054Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15448 tokens)
- 2026-09-09T00:14:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/350: Confirmed the committed backend-aware review admission change at 8862a0d6712c36af11dcc0da43d57294b66ea486. The focused scheduler suite passes 152 tests and lint is clean; no further source change was warranted. cost=$0.38
- 2026-09-09T00:15:00+00:00 stalled: revise run 20260909T001054Z-revise produced no change to the diff or PR description; run `garden triage CG-456 --changes "<feedback>" to unblock`
- 2026-09-09T00:32:57+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/350
- 2026-09-09T01:11:32+00:00 automated review could not start: CG-456 is done: #350 was merged at 00:32:57
