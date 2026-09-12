---
id: CG-325
title: 'A dependency can require the parent to merge, not only to have a PR: depends_on entries take after:
  merge, the default for a design-to-build pair'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/graph.py
- src/garden/model.py
- src/garden/scheduler/dispatch.py
- docs/design.md
- tests/test_graph.py
branch: garden/cg-325-a-dependency-can-require-the-parent-to-merge-not
pr: https://github.com/joshmarcus/context-garden/pull/272
attempts: 1
last_dispatched_at: '2026-09-07T07:12:22+00:00'
created: '2026-09-06T04:03:15+00:00'
updated: '2026-09-07T07:33:01+00:00'
---

## Goal

A task can say that it needs its dependency merged, not merely under review. `depends_on` accepts either an id (today's meaning: the child may start stacked on the parent's open PR) or `{id: CG-307, after: merge}`, which keeps the child blocked until the parent's commits are on the base branch. A task whose parent is a design, spec or document task defaults to `after: merge`, since the child builds from the document's content and a document under revision is not a stable base. The task page and the graph show which rule applies.

## Context

Owner, 2026-09-06 04:05Z: "Why is Now 1 design and build running at the same time? Isn't build dependent on design?" The build (CG-308) depends on the design (CG-307); the scheduler dispatched the build at 02:58Z stacked on the design's open PR, which is the stacking rule made for code-on-code chains. The design then took a revise round for six persona findings while the build was already running from the earlier version. Stacking is right when the child needs the parent's code; it is wrong when the child needs the parent's final words.

## Acceptance criteria

- [ ] `depends_on` parses both forms; `after: merge` keeps the child blocked until the parent is done (commits on base), while the bare form keeps today's stacking; `garden validate` reports a malformed entry.
- [ ] A parent whose title or body marks it as a design, spec or document task (a `kind: design` frontmatter field, set by the planner and by hand) makes `after: merge` the default for its children unless overridden.
- [ ] The task page and `garden graph` show "after merge" against such a dependency; tests cover both forms, the default, and dispatch honouring them.

## Log
- 2026-09-06T04:03:15+00:00 approved (cli)
- 2026-09-06T13:13:21+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:36+00:00 reset to ready by hand
- 2026-09-07T06:53:35+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply 878de867a58568393abe824c7dbee2cafadb4476` in /home/joshua/work/worktrees/CG-325 to recover them (garden:CG-325:20260907T065335Z-work:pre-dispatch, run 20260907T065335Z-work)
- 2026-09-07T06:54:12+00:00 dispatched work run 20260907T065335Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~20335 tokens)
- 2026-09-07T07:04:44+00:00 preserved uncommitted worktree changes from run 20260907T065335Z-work outside the PR: `git stash apply 060e90bff206b1d5159aea3098d8ffd64b592116` in /home/joshua/work/worktrees/CG-325 (garden:CG-325:20260907T065335Z-work:reap)
- 2026-09-07T07:08:00+00:00 opened https://github.com/joshmarcus/context-garden/pull/272 (base main): Added merge-aware dependency rules with design/spec/document defaults, validation, dispatch gating, and UI/graph labels. cost=$0.10
- 2026-09-07T07:12:03+00:00 automated review requested changes: Merge-aware dependency behavior is implemented and the focused 62-test suite passes, but malformed planner output can persist an invalid rule that breaks subsequent task loading. The PR description also needs the broader motivation, phase fit, verification, and follow-up status. cost=$0.96
- 2026-09-07T07:12:22+00:00 dispatched revise run 20260907T071221Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~22135 tokens)
- 2026-09-07T07:21:24+00:00 preserved uncommitted worktree changes from run 20260907T071221Z-revise outside the PR: `git stash apply 0333322d1125f7c5dab7a94c1a6afdd13d580904` in /home/joshua/work/worktrees/CG-325 (garden:CG-325:20260907T071221Z-revise:reap)
- 2026-09-07T07:22:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/272: Validated planner dependency rules before task creation and expanded merge-default/stack-override regression coverage. Focused tests, full Ruff, and exact-commit CI all pass. cost=$0.07
- 2026-09-07T07:24:50+00:00 automated review: approve — Merge-aware dependency parsing, defaults, dispatch gating, and labels are correctly implemented. The focused 67-test suite passes, and all required UI captures render cleanly. cost=$0.61
- 2026-09-07T07:25:11+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T07:26:11+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T07:33:01+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/272
