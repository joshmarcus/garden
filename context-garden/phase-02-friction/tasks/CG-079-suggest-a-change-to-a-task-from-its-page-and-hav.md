---
id: CG-079
title: Suggest a change to a task from its page, and have an agent fold it in
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/web/app.py
- src/garden/web/templates/task.html
- src/garden/planner.py
- src/garden/model.py
- src/garden/scheduler.py
branch: garden/cg-079-suggest-a-change-to-a-task-from-its-page-and-hav
pr: https://github.com/joshmarcus/context-garden/pull/75
attempts: 1
last_dispatched_at: '2026-09-05T01:44:37+00:00'
created: '2026-09-04T19:15:32+00:00'
updated: '2026-09-05T01:48:02+00:00'
---

## Goal

On a task's page a person can write a suggestion about the task itself (its goal, context, acceptance criteria, reading list, priority, difficulty), and the garden later has an agent integrate the suggestion into the task file, showing what changed, without the person editing markdown by hand.

## Context

Asked during the first live run, on `/tasks/CG-052`. Today the task page has forms for answering a worker, triage and friction reports (CG-044), but nothing for "this task should say X": the only way is to edit the file. Task files are the spec a worker gets, so a good suggestion is worth folding in before dispatch, and a person's wording is usually not the final wording.

Design:

1. **Capture.** A "Suggest a change" form on the task page (textarea, optional "applies to" select: goal / context / acceptance / reading / priority / difficulty / anything). It appends to a `## Suggestions` section in the task file (`- <date> <author>: <text>`, `author` being the web session or `garden suggest --by`) and emits a `suggestion` event. `garden suggest <id> "<text>"` does the same from the CLI and from chat sessions. Suggestions never touch scheduler-owned fields.
2. **Integrate.** A new run mode, `edit`, dispatched by the tick when a task has unintegrated suggestions and is not `running` (or by "Integrate now" on the page, or `garden integrate <id>`). The brief is the planner-style prompt with the task body and the suggestions, asking for a revised body (goal, context, acceptance, reading, and proposed priority/difficulty) that folds the suggestions in and keeps everything else; the result is JSON like the planner's. The scheduler writes the new body, marks the suggestions integrated (`- [x]`), logs "integrated N suggestion(s) (run …)", and keeps the old body in the run directory. If the task is `running`, suggestions wait and also ride the next revise brief as feedback so the worker knows the spec moved.
3. **Show.** The task page shows the suggestions with their state and, after integration, a diff of the body (old and new from the run directory). The Inbox counts tasks with pending suggestions in the digest line, not as a card.
4. **Model.** `review.difficulty`'s tier for the edit run; cheap, one turn, no tools.

## Acceptance criteria

- [ ] a suggestion made on the page or with `garden suggest` lands in the task file and the event log.
- [ ] an `edit` run rewrites the body to include it, marks it integrated, and the page shows the diff; scheduler-owned fields are untouched.
- [ ] a suggestion on a `running` task waits and reaches the next revise brief.
- [ ] tests with the fake harness returning a revised body.

## Out of scope

- Suggestions on phase goals or specs; those are files a person edits or the planner re-reads.

## Log

- 2026-09-04T19:15:32+00:00 approved
- 2026-09-04T22:45:11+00:00 dispatched work run 20260904T224502Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~11192 tokens)
- 2026-09-04T23:06:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/75 (base main): Added task suggestions: capture on the task page and via `garden suggest`, a new cheap `edit` run that folds pending suggestions into the task body and marks them integrated (with the old/new body kept for a diff), running tasks' suggestions ride the next revise brief, and the page/inbox show suggestion state. Scheduler-owned fields are untouched. cost=$10.22
- 2026-09-05T00:02:15+00:00 PR conflicts with main (src/garden/scheduler.py); revise run will rebase and resolve
- 2026-09-05T00:07:56+00:00 dispatched revise run 20260905T000756Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~13305 tokens)
- 2026-09-05T00:15:41+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$2.64
- 2026-09-05T00:19:32+00:00 dispatched revise run 20260905T001932Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~14410 tokens)
- 2026-09-05T00:26:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/75: Fixed the failing pre-PR check: test_set_budget_none_removes_cap was missing the intermediate reap tick its two sibling budget tests use, so the first batch's finished runs held both max_parallel slots and the retried tasks could not dispatch. Added the reap tick; full test suite and ruff now pass. cost=$2.63
- 2026-09-05T00:30:16+00:00 automated review requested changes: Code meets all four acceptance criteria with clean tests and correct scheduler integration; full suite and ruff pass. The only blocker is one line of process/scar-tissue narration in the PR description. cost=$1.33
- 2026-09-05T00:30:22+00:00 dispatched revise run 20260905T003021Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~14064 tokens)
- 2026-09-05T00:33:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/75: Addressed the sole review blocker by removing the process-narration sentence from the PR description; the budget-test rationale stays in the Friction section. No code change was needed — the suggestions feature already met all four acceptance criteria and the full suite (366 passed) and ruff pass. cost=$0.41
- 2026-09-05T00:33:06+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-079` for one more round, or review on GitHub
- 2026-09-05T01:19:07+00:00 PR conflicts with main (tests/fake_claude.py); revision cap reached; needs a human
- 2026-09-05T01:19:30+00:00 revision counter reset (web)
- 2026-09-05T01:19:30+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T01:22:18+00:00 dispatched revise run 20260905T012217Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~14641 tokens)
- 2026-09-05T01:26:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/75: Rebased the suggestions branch onto current main, resolving the tests/fake_claude.py conflict by keeping both the retro (main) and edit (this branch) harness modes. Full suite (411 passed) and ruff pass; the branch diff is only the suggestions feature. cost=$1.05
- 2026-09-05T01:26:35+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-079` for one more round, or review on GitHub
- 2026-09-05T01:26:38+00:00 PR conflicts with main (src/garden/scheduler.py); revise run will rebase and resolve
- 2026-09-05T01:42:49+00:00 revision counter reset (web)
- 2026-09-05T01:42:49+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T01:44:37+00:00 dispatched revise run 20260905T014436Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~15296 tokens)
- 2026-09-05T01:48:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/75: Rebased the suggestions branch onto current origin/main, resolving the src/garden/scheduler.py conflict by keeping both the CG-109 revise_easy flag and this branch's pending-suggestions revise-brief block. Full suite (420 passed) and ruff pass; the branch diff is only the suggestions feature. cost=$0.72
- 2026-09-05T01:48:02+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-079` for one more round, or review on GitHub
