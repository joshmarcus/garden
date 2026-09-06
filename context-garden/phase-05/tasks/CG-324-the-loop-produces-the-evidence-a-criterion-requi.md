---
id: CG-324
title: 'The loop produces the evidence a criterion requires: persona reviews, captures and checks named
  by a task''s criteria run when its PR opens, before the first review'
status: waiting_human
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/review.py
- src/garden/scheduler/persona.py
- src/garden/scheduler/poll.py
- src/garden/personas.py
- src/garden/web/pages/task.py
- docs/worker-protocol.md
- tests/scheduler/test_poll.py
branch: garden/cg-324-the-loop-produces-the-evidence-a-criterion-requi
pr: https://github.com/joshmarcus/context-garden/pull/223
attempts: 1
last_dispatched_at: '2026-09-06T12:20:27+00:00'
created: '2026-09-06T03:59:38+00:00'
updated: '2026-09-06T12:39:46+00:00'
---

## Goal

When a task's acceptance criteria name evidence the loop can produce, the loop produces it without a hand: a criterion that asks for a persona review dispatches those personas on the PR when it opens; one that asks for captures runs the ui check; one that names a command runs it as a check; the review round waits until that evidence is on the PR, and the review brief carries it. The task page shows each required item with its state (queued, running, posted).

## Context

Owner, 2026-09-06 04:05Z, on reducing review rounds. Tonight's design tasks required designer and usability persona reviews on their PRs; nobody runs those automatically, so sol sent CG-314 back three times for their absence while the operator pressed them by hand for both design PRs. Reviews that wait on evidence that exists cost a round each time; evidence that is produced automatically costs one dispatch.

## Acceptance criteria

- [ ] A criterion matching 'persona-review ... -p <name>' (or a structured requires: list in the task frontmatter) dispatches those personas on the PR when it opens, and the automated review is queued after their comments are posted; tests with the fake harness cover the ordering
- [ ] A criterion requiring captures or a named check runs it as a pre-review check whose result the review brief includes; a failed check is a mechanical changes_requested with the diagnostic
- [ ] The task page lists each required evidence item and its state; the Inbox never shows a review-cap card for a PR whose required evidence has not been produced yet
- [ ] Docs: worker-protocol.md describes requires: and the review ordering

## Log
- 2026-09-06T03:59:39+00:00 approved (cli)
- 2026-09-06T06:23:05+00:00 dispatched work run 20260906T061704Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~19289 tokens)
- 2026-09-06T07:04:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/223 (base main): The scheduler now produces criterion-required PR evidence, waits for required persona comments before automated review, and displays evidence state on task pages. cost=$1.46
- 2026-09-06T07:12:33+00:00 automated review requested changes: Required checks, captures, persona ordering, UI state, and documentation are implemented, but failed persona production can strand the automated review indefinitely. The PR description also needs phase motivation and verification details. cost=$0.89
- 2026-09-06T09:26:14+00:00 dispatched revise run 20260906T092606Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~20470 tokens)
- 2026-09-06T10:23:35+00:00 pre-PR checks failed (test) (still failing after a rebase onto `main`); revise run will fix before the PR is updated cost=$1.45
- 2026-09-06T10:50:23+00:00 dispatched revise run 20260906T105016Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~21928 tokens)
- 2026-09-06T11:46:19+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 56af81dfcba5, not because of this branch; waiting for the base to go green, no revise round cost=$1.97
- 2026-09-06T11:53:26+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T12:20:27+00:00 dispatched revise run 20260906T122022Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~21382 tokens)
- 2026-09-06T12:39:46+00:00 worker says nothing to change: No actionable review feedback or CI failure remains on the open PR. cost=$0.62
