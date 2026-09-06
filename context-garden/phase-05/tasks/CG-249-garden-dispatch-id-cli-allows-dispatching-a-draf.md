---
id: CG-249
title: '`garden dispatch <id>` (CLI) allows dispatching a draft directly'
status: in_review
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/web/actions/control.py
- src/garden/web/actions/tasks.py
- src/garden/scheduler/human.py
- src/garden/cli/planning.py
- src/garden/cli/state.py
- tests/test_web.py
- tests/test_cli.py
branch: garden/cg-249-garden-dispatch-id-cli-allows-dispatching-a-draf
pr: https://github.com/joshmarcus/context-garden/pull/204
discovered_from: CG-238
attempts: 1
last_dispatched_at: '2026-09-06T00:40:28+00:00'
created: '2026-09-05T23:28:25+00:00'
updated: '2026-09-06T00:50:04+00:00'
---

## Goal

Close the draft-dispatch gap in the CLI: `garden dispatch <id>` must not let `mode == "work"` start on a task in DRAFT status without going through the same approve gate CG-238 already applies to the web dispatch button and `garden take`.

## Context

`cli/loop.py`'s `dispatch` command currently permits `mode == "work"` on a DRAFT task without `--force`, and never checks `brief_gaps`. This is the same underlying gap CG-238 closed for the web button and `garden take`, just left open at a third call site.

## Acceptance criteria

- [ ] `garden dispatch <id>` with `mode == "work"` on a DRAFT task, called without `--force`, is refused the same way the web dispatch button and `garden take` refuse it — verified in tests/test_cli.py
- [ ] Before allowing a DRAFT task into work mode, `garden dispatch` checks `brief_gaps` (or the equivalent gate used elsewhere) and refuses when gaps are reported — verified in tests/test_cli.py
- [ ] `--force` still allows dispatching a DRAFT task, preserving the existing override path — verified in tests/test_cli.py
- [ ] The check mirrors the draft-gate logic in src/garden/web/actions/control.py and src/garden/scheduler/human.py so all three call sites (web button, `garden take`, `garden dispatch`) enforce the same rule

## Out of scope

Changing the gate logic itself or its behavior for the web button and `garden take`, which CG-238 already fixed.

## Provenance

Discovered by CG-238 (Every path to ready or to a run goes through the approve gate: Dispatch now on a draft, the new-task form's approve-now, and garden take) during run `20260905T231202Z-work`.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:28:25+00:00 discovered by CG-238; deferred by the freeze
- 2026-09-06T00:18:31+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002115Z-edit) cost=$0.07
- 2026-09-06T00:24:04+00:00 approved (cli)
- 2026-09-06T00:40:28+00:00 dispatched work run 20260906T004012Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~18750 tokens)
- 2026-09-06T00:50:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/204 (base main): garden dispatch now routes a DRAFT task through Scheduler.approve (the same brief_gaps/phase_refusal gate used by garden take and the web) before allowing mode=work, refusing an incomplete brief unless --force is passed. cost=$0.84
