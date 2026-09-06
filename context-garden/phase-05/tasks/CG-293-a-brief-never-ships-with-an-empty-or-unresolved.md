---
id: CG-293
title: A brief never ships with an empty or unresolved reading list, and a revise brief restates the criteria
  and the concrete blocker
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
harness: codex
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-06T03:49:25+00:00'
---

## Goal

The brief builder refuses an empty reading list, drops entries that do not resolve and reports the drop as a gap, and builds inlined files from the task's base commit rather than a dirty worktree. A revise brief restates the acceptance criteria, inlines the actual review comments and the failing check's stack trace, and when GitHub has nothing to address, names the rebase conflict as the concrete blocker.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict, consolidating seventeen phase-04 friction items.

## Acceptance criteria

- [ ] Brief builder rejects a brief with an empty reading list before it reaches the approve gate, returning a validation error instead of shipping it.
- [ ] Reading-list entries that fail to resolve to a real path are dropped from the list and reported as a gap in the brief output, not silently discarded.
- [ ] Inlined file contents in a brief are read from the task's base commit, not from an uncommitted or dirty worktree, even when the worktree has local changes.
- [ ] A revise brief restates the task's acceptance criteria verbatim and inlines the actual GitHub review comments and the failing check's stack trace, rather than a summary.
- [ ] When a revise brief finds nothing on GitHub to address, it names the rebase conflict as the blocker instead of leaving the field empty or generic; covered by a test asserting the revise-brief path sets this blocker when there are no open review comments.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

- [ ] `brief_gaps` (and so the approve gate and the New task form) refuses a criterion that names a path under src/ or tests/, a function or method (`name()`), a config key or a field name, with the message that criteria state outcomes and evidence and the detail belongs in the context or reading list; the check is a small, documented heuristic with a test per shape and an `allow_implementation_criteria: true` escape per task for the rare mechanical task (owner, 2026-09-06 03:50Z).
- [ ] A worker may amend a criterion: the result block carries `criteria_amended: [{index, text, reason}]`, the task file is updated on reap with the reason in the log, the review brief shows the amended line marked as amended, and the reviewer judges that line; tests cover the round trip.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-282 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005022Z-edit) cost=$0.11
- 2026-09-06T00:52:23+00:00 approved (cli)
- 2026-09-06T03:49:25+00:00 difficulty medium -> medium
