---
id: CG-294
title: Planning sequences dependent tasks and inlines retro evidence into the brief
status: in_review
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: medium
reading:
- src/garden/planner.py
- src/garden/graph.py
- src/garden/model.py
- tests/test_planner.py
- docs/design.md
branch: garden/cg-294-planning-sequences-dependent-tasks-and-inlines-r
pr: https://github.com/joshmarcus/context-garden/pull/275
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 2
last_dispatched_at: '2026-09-07T10:37:17+00:00'
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-07T12:54:17+00:00'
runner: manual
---

## Goal

Two tasks serving one goal are sequenced as dependencies at planning so one never merges assuming the other has, and the planner inlines the retro evidence a task cites into the brief instead of pointing at a garden path.

## Context

Phase-04's retro found both pieces of Goal 2 undone: CG-229's design assumed CG-212's quota convention had already merged, and the two tasks landed out of order, producing a design conflict a rebase didn't catch until a test failed. This is a follow-up carried into phase-05 by that retro verdict.

## Acceptance criteria

- [ ] `PLAN_INSTRUCTIONS` in `src/garden/planner.py` tells the planner to link two draft tasks with `depends_on` when they serve one goal and one's design assumes the other has already merged, not only when it needs the other's code outright.
- [ ] `plan_prompt`/`import_plan` in `src/garden/planner.py` inline the text of a retro finding a task's body or human guidance cites by garden path (e.g. `docs/friction.md`, `docs/retro.md`) into the generated task's body, rather than leaving a bare path for the worker to chase down.
- [ ] A new `tests/test_planner.py` case feeds `import_plan` two batch items where one's body assumes the other merged first and asserts the resulting tasks come back linked by `depends_on`, extending the pattern in `test_import_resolves_title_deps`.
- [ ] A new `tests/test_planner.py` case asserts the planner inlines a cited retro-evidence excerpt into the generated task body instead of leaving only the path.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-283 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:55:37+00:00 integrated 1 suggestion(s) (run 20260906T005023Z-edit) cost=$0.62
- 2026-09-06T00:55:55+00:00 approved (cli)
- 2026-09-06T13:18:07+00:00 dispatched work run 20260906T131632Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~22973 tokens)
- 2026-09-06T13:36:08+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$0.55
- 2026-09-06T17:42:17+00:00 dispatched revise run 20260906T174213Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, rebase round 1 (not counted), ~25854 tokens)
- 2026-09-06T17:51:56+00:00 Operator preempted revise run for priority-0 web outage CG-357. Worktree and transcript preserved; extra patch at /home/joshua/work/operator-test-tmp/CG294-web-outage-recovery.patch. Resume preserved work after web repair; interrupted tests are not code failures.
- 2026-09-07T07:10:59+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply 221a16806917265cee675037b74f55ed83e49cca` in /home/joshua/work/worktrees/CG-294 to recover them (garden:CG-294:20260907T071059Z-work:pre-dispatch, run 20260907T071059Z-work)
- 2026-09-07T07:11:01+00:00 dispatched work run 20260907T071059Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~25782 tokens)
- 2026-09-07T07:20:00+00:00 preserved uncommitted worktree changes from run 20260907T071059Z-work outside the PR: `git stash apply 7b78ccaabe739bc7fc33be04bb9c7eba55b11202` in /home/joshua/work/worktrees/CG-294 (garden:CG-294:20260907T071059Z-work:reap)
- 2026-09-07T07:21:22+00:00 opened https://github.com/joshmarcus/context-garden/pull/275 (base main): Planner instructions now sequence design assumptions as dependencies, and cited retro/friction evidence is inlined into planning prompts and created task bodies. Regression coverage proves both behaviors. cost=$0.55
- 2026-09-07T07:22:45+00:00 description rewritten by the reviewer cost=$0.35
- 2026-09-07T07:34:25+00:00 rebasing before merge; rebase onto main conflicts (docs/design/snapshot.json); a rebase agent will resolve it
- 2026-09-07T07:37:18+00:00 dispatched rebase run 20260907T073717Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~398628 tokens)
- 2026-09-07T07:38:42+00:00 preserved uncommitted worktree changes from run 20260907T073717Z-rebase outside the PR: `git stash apply 7d42a968cba1af67a0ca8079ac976c0e75f9fc25` in /home/joshua/work/worktrees/CG-294 (garden:CG-294:20260907T073717Z-rebase:reap)
- 2026-09-07T07:38:42+00:00 rebase run 20260907T073717Z-rebase did not finish: worker exited 1: Error: turn/start: turn/start failed: Input exceeds the maximum length of 1048576 characters. (code -32602), data: {"input_error_code":"input_too_large","max_chars":1048576,"actual_chars":1594512}; will retry
- 2026-09-07T07:38:42+00:00 rebase run 20260907T073717Z-rebase did not finish: worker exited 1: Error: turn/start: turn/start failed: Input exceeds the maximum length of 1048576 characters. (code -32602), data: {"input_error_code":"input_too_large","max_chars":1048576,"actual_chars":1594512}; will retry
- 2026-09-07T07:38:57+00:00 dispatched rebase run 20260907T073856Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~398890 tokens)
- 2026-09-07T07:40:00+00:00 preserved uncommitted worktree changes from run 20260907T073856Z-rebase outside the PR: `git stash apply 396fb4648bcb1b410484117dbffd90e528e8c96d` in /home/joshua/work/worktrees/CG-294 (garden:CG-294:20260907T073856Z-rebase:reap)
- 2026-09-07T07:40:00+00:00 rebase run 20260907T073856Z-rebase did not finish: worker exited 1: Error: turn/start: turn/start failed: Input exceeds the maximum length of 1048576 characters. (code -32602), data: {"input_error_code":"input_too_large","max_chars":1048576,"actual_chars":1595560}; retry also failed; needs human to resolve docs/design/snapshot.json
- 2026-09-07T09:14:08+00:00 triage: changes requested by hand: Recover via a normal bounded revision, not the oversized conflict-only prompt. Preserve planner implementation and snaps
- 2026-09-07T09:14:10+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T09:28:21+00:00 dispatched revise run 20260907T092819Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26996 tokens)
- 2026-09-07T09:39:24+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/275: Merged current main without rewriting the PR branch, retained the canonical generated snapshot, and preserved snapshot salvage in a named stash. Planner dependency sequencing and retro-evidence inlining remain covered by focused tests; exact-head CI passed. cost=$0.58
- 2026-09-07T09:42:39+00:00 automated review requested changes: Dependency sequencing is correctly instructed and covered, but retro evidence inlining fails for backtick- or quote-delimited paths—the repository’s own standard citation format. This leaves two acceptance criteria unmet. cost=$0.44
- 2026-09-07T09:59:37+00:00 dispatched revise run 20260907T095935Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~28590 tokens)
- 2026-09-07T10:09:42+00:00 preserved uncommitted worktree changes from run 20260907T095935Z-revise outside the PR: `git stash apply f80997aa5f50fb174ba43f737717a00dcb73247b` in /home/joshua/work/worktrees/CG-294 (garden:CG-294:20260907T095935Z-revise:reap)
- 2026-09-07T10:11:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/275: Planner retro-evidence recognition now accepts backtick- and quote-delimited paths, including canonical garden-relative paths. Regression coverage and exact-head GitHub CI pass. cost=$0.61
- 2026-09-07T10:12:59+00:00 automated review requested changes: The acceptance criteria are implemented and the focused planner suite passes, but retro-evidence resolution can inline the wrong document when a short path is cited more than once. Fix the fallback/deduplication ordering before merge. cost=$0.26
- 2026-09-07T10:16:16+00:00 dispatched revise run 20260907T101614Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~28908 tokens)
- 2026-09-07T10:26:36+00:00 preserved uncommitted worktree changes from run 20260907T101614Z-revise outside the PR: `git stash apply 3f91c710aa65fa012258c132b5d5c30cd628d6fa` in /home/joshua/work/worktrees/CG-294 (garden:CG-294:20260907T101614Z-revise:reap)
- 2026-09-07T10:29:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/275: Fixed repeated short retro citations so phase-local evidence is resolved once without falling through to an unrelated root document. Added regression coverage; focused tests, lint, and exact-head CI pass. cost=$0.30
- 2026-09-07T10:32:10+00:00 description rewritten by the reviewer cost=$0.27
- 2026-09-07T10:33:32+00:00 rebasing before merge; rebase onto main conflicts (docs/design/snapshot.json); a rebase agent will resolve it
- 2026-09-07T10:33:35+00:00 dispatched rebase run 20260907T103332Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~399848 tokens)
- 2026-09-07T10:34:36+00:00 preserved uncommitted worktree changes from run 20260907T103332Z-rebase outside the PR: `git stash apply 9336c1d617aaa240fbd7447d4d7170b7ee55106b` in /home/joshua/work/worktrees/CG-294 (garden:CG-294:20260907T103332Z-rebase:reap)
- 2026-09-07T10:34:36+00:00 rebase run 20260907T103332Z-rebase did not finish: worker exited 1: Error: turn/start: turn/start failed: Input exceeds the maximum length of 1048576 characters. (code -32602), data: {"input_error_code":"input_too_large","max_chars":1048576,"actual_chars":1599395}; will retry
- 2026-09-07T10:34:36+00:00 rebase run 20260907T103332Z-rebase did not finish: worker exited 1: Error: turn/start: turn/start failed: Input exceeds the maximum length of 1048576 characters. (code -32602), data: {"input_error_code":"input_too_large","max_chars":1048576,"actual_chars":1599395}; will retry
- 2026-09-07T10:37:17+00:00 dispatched rebase run 20260907T103715Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~400110 tokens)
- 2026-09-07T10:38:18+00:00 preserved uncommitted worktree changes from run 20260907T103715Z-rebase outside the PR: `git stash apply 1987955b3e2f6441559a4558a83febf7bb5f5651` in /home/joshua/work/worktrees/CG-294 (garden:CG-294:20260907T103715Z-rebase:reap)
- 2026-09-07T10:38:18+00:00 rebase run 20260907T103715Z-rebase did not finish: worker exited 1: Error: turn/start: turn/start failed: Input exceeds the maximum length of 1048576 characters. (code -32602), data: {"input_error_code":"input_too_large","max_chars":1048576,"actual_chars":1600443}; retry also failed; needs human to resolve docs/design/snapshot.json
- 2026-09-07T12:54:17+00:00 triage: marked ready for review
- 2026-09-07T12:54:17+00:00 Operator owns deployment prerequisite: CG373/PR283 is merged but not installed. Temporary manual hold prevents oversized rebase retry; restore ordinary runner and continue preserved PR275 after verified deployment. No owner decision remains.
