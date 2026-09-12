---
id: CG-497
title: Serialize worker answers with scheduler ticks
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/human.py
- tests/test_canary.py
branch: garden/cg-497-serialize-worker-answers-with-scheduler-ticks
pr: https://github.com/joshmarcus/context-garden/pull/401
discovered_from: CG-493
attempts: 1
last_dispatched_at: '2026-09-09T21:28:49+00:00'
created: '2026-09-09T20:54:15+00:00'
updated: '2026-09-09T21:42:08+00:00'
file: src/garden/scheduler/human.py
error: Without serialization, a concurrent scheduler pass may overwrite a resumed task with stale waiting_human
  state.
---

Prevent an in-flight scheduler tick from saving a stale `waiting_human` task over a concurrently resumed worker answer. The prior implementation acquired the cross-process tick lock, invalidated task discovery, reloaded scheduler state, and resolved the current task before dispatching the answer; retain equivalent regression coverage proving an answer waits for the tick and leaves the task running. The implementation and test are preserved in commit b7671295e0d292c47c4dbdcafebf63caec4cda6b but were removed from CG-493 because they are outside its narrow RC14 retention scope.

## Provenance

Discovered by CG-493 (Retain RC14 discovery and CI guards) during run `20260909T205202Z-revise`.
## Log
- 2026-09-09T20:54:15+00:00 discovered by CG-493
- 2026-09-09T21:23:02+00:00 operator completed the discovered-task reading list from preserved commit b7671295: scheduler answer path and canary regression; scope remains the isolated answer/tick race
- 2026-09-09T21:23:04+00:00 approved (cli)
- 2026-09-09T21:28:49+00:00 dispatched work run 20260909T212845Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15570 tokens)
- 2026-09-09T21:30:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T21:32:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/401 (base main): Serialized human worker answers with scheduler ticks, reloading task discovery and state after obtaining the cross-process lock so a stale waiting_human task cannot overwrite a resumed dispatch. Verified with focused scheduler coordination/quota tests (52 passed) and Ruff lint. cost=$0.26
- 2026-09-09T21:34:39+00:00 automated review: approve — Worker answers now serialize with scheduler ticks and reload durable task/state data under the controller lock, preventing stale waiting_human writes. cost=$0.33
- 2026-09-09T21:42:08+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/401
