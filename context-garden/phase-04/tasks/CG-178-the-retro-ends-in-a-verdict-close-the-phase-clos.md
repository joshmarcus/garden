---
id: CG-178
title: 'The retro ends in a verdict: close the phase, close with follow-ups for the next phase, or reopen
  with named tasks that must land first'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/cli.py
- src/garden/inbox.py
- src/garden/web/pages/phase.py
created: '2026-09-05T09:40:41+00:00'
updated: '2026-09-05T09:40:41+00:00'
---

## Goal

A retro is not finished until it has decided what happens to the phase. The reconciliation run returns one of three verdicts, the garden files the tasks the verdict names, a person (or the operator acting for them) accepts or changes the verdict on a decision card, and `garden close-phase` follows it.

1. **Close.** Nothing blocks closing; the phase joins the herbarium.
2. **Close with follow-ups.** Nothing blocks closing, and the named items become draft tasks in the next phase, linked to the retro.
3. **Reopen.** The named items must land before the phase can close: they become tasks in this phase, carry a freeze exception so a frozen phase still dispatches them, and `close-phase` refuses until each is done or cancelled.

## Context

Requested by the user on 2026-09-05 during the phase-03 wrap-up. Today `garden retro` writes `docs/retro.md` and a next-goals draft and opens a PR; `garden close-phase` is a separate command with no verdict behind it, so the "should this phase close" decision lives only in the operator's head. Phase 02's retro produced 41 items and the operator sorted them into phase 03 and phase 04 by hand; phase 03's retro is being handled the same way. The freeze exception exists since CG-148; decision cards since CG-100 and CG-112; the retro page (CG-146) is where the verdict and its tasks should be visible.

## Design

- The reconciliation brief asks for a `GARDEN_RETRO` block: `verdict` (`close` | `close_with_followups` | `reopen`), `followups` (title, body, difficulty, priority) and `blocking` (same fields, plus the reason it blocks). The retro document gets a `## Verdict` section that states the choice and lists the tasks by id once filed.
- On reap, the garden files `followups` as drafts in the next phase and `blocking` as drafts in the current phase with `retro_blocking: true` and `freeze_exception: true`, all with `discovered_from: retro:<phase>` provenance, and raises one decision card: "Retro verdict for <phase>: <verdict>" with accept, change to another verdict, or reject (with a note). Accepting `close` closes the phase; accepting `close_with_followups` closes it and leaves the drafts for approval; accepting `reopen` approves the blocking tasks.
- `garden close-phase` refuses while any `retro_blocking` task is open, names them, and says `--force` overrides; it warns (does not refuse) when the phase has no retro verdict at all.
- The phase page and the retro page show the verdict, who accepted it and when, and the generated tasks with their current status.
- CLI parity: `garden retro` prints the verdict; `garden retro-decide <phase> close|followups|reopen [--note]` accepts or changes it.

## Acceptance criteria

- [ ] The reconciliation result carries a verdict and the task lists; the retro document has a `## Verdict` section.
- [ ] Follow-ups are filed as drafts in the next phase and blocking tasks in the current phase with `retro_blocking` and a freeze exception, all with retro provenance; one decision card is raised and accepting it does what the verdict says.
- [ ] `garden close-phase` refuses with the names of open blocking tasks unless forced, and warns when no verdict exists.
- [ ] The phase page and the retro page show the verdict and the generated tasks with status.
- [ ] Tests for each verdict path with the fake harness, including the refusal and the override.

