---
id: CG-294
title: Planning sequences dependent tasks and inlines retro evidence into the brief
status: running
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
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-06T13:18:07+00:00'
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-06T13:18:07+00:00'
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
