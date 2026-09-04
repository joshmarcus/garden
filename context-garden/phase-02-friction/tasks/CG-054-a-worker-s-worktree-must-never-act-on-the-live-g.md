---
id: CG-054
title: A worker's worktree must never act on the live garden
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
branch: garden/cg-054-a-worker-s-worktree-must-never-act-on-the-live-g
pr: https://github.com/joshmarcus/context-garden/pull/35
attempts: 1
last_dispatched_at: '2026-09-04T19:33:50+00:00'
created: '2026-09-04T17:42:42+00:00'
updated: '2026-09-04T19:33:50+00:00'
---

## Goal

Code running inside a worker's worktree (the worker itself, its tests, the pre-PR checks) can never find and mutate the live garden's `.garden/` state and task files.

## Context

During the first live run, at 17:37:40 UTC the live garden logged "environment error (not an attempt)" for CG-032 and moved it back to ready. That string exists in no code the running `garden serve` had loaded; it exists only in the CG-033 worker's worktree, where that feature was being written. Worktrees live at `.garden/worktrees/<id>` inside the garden, so `find_root()` walking upward from a worktree (from a `Store()` with no path, from `garden` run by a worker to try its feature, from a test that forgets to pass a root) lands on the real garden, and the unreviewed code in the worktree then reaps real runs and writes real task files. The same route explains a pre-PR test failing under load: tests in worktrees share one live root if any of them resolves it.

Fixes, all of them: (1) `find_root()` stops at a `.garden/worktrees` boundary and refuses to return a root that contains the starting path under `.garden/`; (2) the runner sets `GARDEN_ROOT` for the worker to an explicit, non-existent or sandbox path unless the brief says otherwise, and `Store` honours it; (3) the brief's rules say plainly: do not run `garden` commands against this garden; run the test suite only; (4) the pre-PR checks run with the same guard. A test creates a worktree under a temp garden's `.garden/worktrees/x` and asserts `find_root()` from inside it raises.


A second route, seen an hour later: a worker ran `pip install -e .` inside its worktree (the product overview tells workers how to install), which re-pointed the garden's shared `.venv` editable install at `.garden/worktrees/CG-041/src`. When that worktree was removed after its merge, `garden` itself failed to import and `garden serve` answered 500 until the install was repaired by hand. Another worker installed playwright into the same venv. Workers must get their own environment (a venv inside the worktree, or `uv run` with an isolated project), and the pre-PR checks must not depend on the shared `.venv` being untouched.


## Constraint (added 2026-09-04, from the person)

Isolation must not hard-code Python. Other products managed by this garden will use different dependency tooling (a work setting with its own package manager, Node projects, monorepo tools). Whatever runs to prepare a worktree must come from per-product configuration (see the environment-setup task filed alongside this one: a `setup` block with `command`, `env`, `test`, `lint`), with this product's `uv`/venv as one configuration, not as code in the runner. `GARDEN_ROOT`, `find_root()` boundaries and the brief's rules are generic; anything that names pip, uv or `.venv` outside `garden.yaml` fails review.

## Acceptance criteria

- [ ] `find_root()` from inside `.garden/worktrees/<id>` does not return the enclosing garden.
- [ ] workers get `GARDEN_ROOT` pointing away from the live garden, and `garden` run in a worktree refuses with a clear message.
- [ ] the brief tells workers not to run the garden against itself.
- [ ] a test for the boundary.
- [ ] a worker cannot change the garden's own `.venv`: workers run with their own environment and the brief says so.
- [ ] no Python-, pip-, uv- or venv-specific logic in the runner or scheduler; environment preparation comes from per-product config.

## Out of scope

- Remote (ssh) worktrees, which live outside the garden already.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T18:59:59+00:00 dispatched work run 20260904T185958Z-work via local [claude model=sonnet] (fresh session, base main, ~2483 tokens)
- 2026-09-04T19:08:06+00:00 pre-PR checks failed (tests); no PR opened yet; revise run will fix cost=$1.80
- 2026-09-04T19:08:09+00:00 dispatched revise run 20260904T190809Z-revise via local [claude model=sonnet] (fresh session, base main, ~9515 tokens)
- 2026-09-04T19:18:10+00:00 discovered work filed: CG-082
- 2026-09-04T19:18:36+00:00 opened https://github.com/joshmarcus/context-garden/pull/35 (base main): Fixed the pre-PR test failure: `find_root()` was treating `GARDEN_ROOT` pointing to the live garden (set by `check_ctx` for check commands) as an authoritative redirect, so tests running inside a pre-PR check subprocess all returned live CG-* tasks instead of their temp garden. The fix makes `find_root()` ignore `GARDEN_ROOT` when it points to an existing garden and fall through to the normal cwd walk; it still raises immediately when `GARDEN_ROOT` points to a non-existent path (the worker guard). Two `test_isolation.py` tests that asserted the obsolete redirect behaviour were updated to reflect the correct semantics. cost=$1.24
- 2026-09-04T19:19:42+00:00 1 new review item(s)
- 2026-09-04T19:22:34+00:00 triage: changes requested by hand: Two things. (1) The boundary and the GARDEN_ROOT redirect are right and generic; keep them. The new operating rule in br
- 2026-09-04T19:22:44+00:00 automated review: request_changes — Two blocking issues: brief.py names uv/pip/.venv in OPERATING_RULES, violating the explicit constraint that brief rules must be generic; PR description contains a 'Root cause of the revision' section that is scar tissue from the revision round. cost=$0.47
- 2026-09-04T19:22:45+00:00 dispatched revise run 20260904T192245Z-revise via local [claude model=sonnet] (fresh session, base main, ~9801 tokens)
- 2026-09-04T19:32:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/35: Rebased onto origin/main resolving the brief.py conflict, and made the operating-rules install guidance generic. The OPERATING_RULES no longer name uv, pip, or .venv — the rule now says 'do not install packages into a shared environment or outside this worktree; the environment is prepared; run the product's own check commands from the product overview'. All 191 tests pass, lint clean. cost=$0.73
- 2026-09-04T19:32:44+00:00 2 new review item(s)
- 2026-09-04T19:33:50+00:00 dispatched revise run 20260904T193350Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~10252 tokens)
