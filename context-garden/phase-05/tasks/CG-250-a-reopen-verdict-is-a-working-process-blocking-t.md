---
id: CG-250
title: 'A reopen verdict is a working process: blocking tasks arrive with a complete brief, are approved
  through the gate, and the phase reopens and closes on them without hand steps'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/retro.py
- src/garden/retro.py
- src/garden/scheduler/human.py
- src/garden/brief.py
- tests/test_retro.py
branch: garden/cg-250-a-reopen-verdict-is-a-working-process-blocking-t
pr: https://github.com/joshmarcus/context-garden/pull/197
harness: codex
attempts: 1
last_dispatched_at: '2026-09-06T00:43:29+00:00'
created: '2026-09-05T23:41:22+00:00'
updated: '2026-09-06T00:43:29+00:00'
---

## Goal

When a retro's verdict is `reopen`, the loop carries it through on its own: each blocking item is filed in the phase as a task with a complete brief (acceptance criteria as a checklist, a reading list whose paths exist, a difficulty), accepting the verdict approves those tasks through the same gate every other task passes, the phase is unfrozen for them, and once they are done the phase closes on the verdict's terms. A person's part is the one decision (accept, or change the verdict), and even that is optional when the owner has said close need not wait.

## Context

Phase 04's retro (2026-09-05 23:05Z, fable) returned `reopen` with two blocking tasks, CG-238 and CG-239. CG-178 built the path: the items were filed live in phase 04 with `retro_blocking` and a freeze exception, the Inbox showed the decision card, and `close-phase` refuses while they are open. What did not work: the reconcile filed both with no `## Acceptance criteria` and `reading: []`, so `garden approve` refused them; `retro_decide`'s own `_approve_retro_blocking` flips draft to ready directly and would have skipped that gate (the bypass CG-238 itself is about); the operator wrote criteria and reading lists by hand, guessing paths twice (one guess named modules that do not exist), then approved. The user asked whether a real process exists: it does, but not end to end.

## Acceptance criteria

- [ ] The reconcile brief asks for each blocking item's acceptance criteria (a checklist), reading list (paths under the product) and difficulty, and `_file_retro_blocking` writes them; an item without criteria is filed with a `brief_gap` note and the decision card says which items need a brief before the verdict can be accepted.
- [ ] `retro_decide reopen` approves blocking tasks through `Scheduler.approve` (brief gaps and phase refusals apply); a refused task stays a draft and is named on the decision card with the gap.
- [ ] `retro_decide reopen` lifts the phase freeze for the blocking tasks (or the freeze exception is enough, documented either way) and records the decision; when every blocking task is terminal, the next tick closes the phase per the recorded verdict and emits `phase_closed`, without `close-phase` by hand.
- [ ] Tests with the fake harness: a reopen verdict with one complete and one incomplete item; the complete one is approved on decide, the incomplete one is refused and named; closing follows the last blocking merge.
- [ ] `docs/design.md` describes the reopen path in one paragraph.

## Log

- 2026-09-06T00:24:05+00:00 approved (cli)
- 2026-09-06T00:25:04+00:00 dispatched work run 20260906T002447Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~6949 tokens)
- 2026-09-06T00:35:47+00:00 opened https://github.com/joshmarcus/context-garden/pull/197 (base main): Reopen verdicts now file complete blocker briefs, pass through the normal approval gate, retain incomplete blockers as visible pending work, and automatically close the phase after all blockers become terminal. cost=$0.76
- 2026-09-06T00:41:31+00:00 automated review requested changes: Approval-gate delegation, freeze handling, and self-closing all work and are tested, but the decision card only reveals which blockers need a brief after a failed decide attempt, not proactively as the criterion requires. cost=$0.66
- 2026-09-06T00:43:29+00:00 dispatched revise run 20260906T004328Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~7424 tokens)
