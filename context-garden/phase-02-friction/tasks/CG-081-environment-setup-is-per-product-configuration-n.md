---
id: CG-081
title: Environment setup is per-product configuration, not a venv assumption
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/runner/local.py
- src/garden/runner/ssh.py
- src/garden/brief.py
- src/garden/config.py
- examples/garden.work.yaml
branch: garden/cg-081-environment-setup-is-per-product-configuration-n
pr: https://github.com/joshmarcus/context-garden/pull/48
attempts: 1
last_dispatched_at: '2026-09-04T21:22:44+00:00'
created: '2026-09-04T19:17:54+00:00'
updated: '2026-09-04T21:25:47+00:00'
---

## Goal

How a product's working environment is prepared (dependencies, virtualenvs, toolchains, environment variables) is a per-product setting in `garden.yaml` and its overlays, and nothing in the scheduler, the runners, the checks or the brief assumes Python, pip, `uv` or a `.venv`.

## Context

Said plainly by the person driving the first live run: "the venv feature is very specific to us developing on this project, but other projects may have very different environment settings; I want to use this in a work setting where dependencies are managed differently." Today the assumptions are scattered: `checks.pre_pr` in this garden's config calls `$GARDEN_ROOT/.venv/bin/python`; the product overview tells workers `uv venv && uv pip install -e ".[dev]"`; workers twice ran `pip install -e` into the garden's own venv; and CG-054, in flight, must not answer "isolate the worker" with "make a venv in the worktree".

Add a `setup` block per product (overridable per environment overlay, per runner host for ssh):

```yaml
products:
  context-garden:
    setup:
      command: "uv sync --extra dev"      # run once in a fresh worktree, before the worker starts; empty = nothing
      env: {UV_PROJECT_ENVIRONMENT: .venv}  # extra environment for the worker and the checks
      test: "uv run pytest -q -x"         # named so the brief can tell the worker how to run checks
      lint: "uv run ruff check src tests"
      timeout_seconds: 600
```

The runner runs `setup.command` in the worktree after creating it (and again when `setup.command` changes, tracked by a marker file), with `setup.env` added to the worker's environment; a failure is a run failure with the log in the task log, not a worker problem. `checks.pre_pr` defaults to the named `test` and `lint` commands run in the worktree with the same env, so the default config for this product no longer reaches into the garden's `.venv`. The brief's operating rules state the test and lint commands from config and say the environment is prepared, replacing the install instructions in the product overview. The ssh runner runs the same setup on the host. `examples/garden.work.yaml` shows a non-Python product (`npm ci`, `make test`) and one where dependencies come from a company tool.

## Acceptance criteria

- [ ] `setup.command` runs once per fresh worktree with `setup.env`, before the worker; its failure fails the run with the log attached; tests with a fake command.
- [ ] `checks.pre_pr` defaults to the product's `test` and `lint` commands in the worktree; this garden's config uses them and no longer names `$GARDEN_ROOT/.venv`.
- [ ] the brief tells the worker the exact test and lint commands and that the environment is prepared; no brief mentions pip, uv or a venv unless the product's config does.
- [ ] `examples/garden.work.yaml` shows two non-Python setups; README documents the block.
- [ ] CG-054's isolation uses this block rather than its own venv logic.

## Log

- 2026-09-04T19:17:54+00:00 approved
- 2026-09-04T20:10:42+00:00 dispatched work run 20260904T201042Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~11193 tokens)
- 2026-09-04T20:26:01+00:00 discovered work filed: CG-092
- 2026-09-04T20:26:04+00:00 pre-PR checks failed (tests); no PR opened yet; revise run will fix cost=$6.25
- 2026-09-04T20:55:50+00:00 dispatched revise run 20260904T205550Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~13483 tokens)
- 2026-09-04T21:01:00+00:00 pre-PR checks failed (tests, lint); no PR opened yet; revise run will fix cost=$1.80
- 2026-09-04T21:01:00+00:00 dispatched revise run 20260904T210100Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~12841 tokens)
- 2026-09-04T21:17:52+00:00 discovered work filed: CG-107
- 2026-09-04T21:18:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/48 (base main): The pre-PR failure came from my branch being based on pre-CG-082 main: CG-082 forced GARDEN_ROOT to a sentinel and moved the venv locator to GARDEN_EXEC_ROOT, breaking the old $GARDEN_ROOT/.venv check. I merged origin/main, resolved conflicts in checks.py (product setup.env + CG-082 sentinel, sentinel last) and test_cli.py, and verified the driving config's current $GARDEN_EXEC_ROOT check commands pass against the worktree (234 tests, lint clean). cost=$4.62
- 2026-09-04T21:22:42+00:00 automated review requested changes: Feature is correct, well-tested (231 pass, ruff clean) and meets the acceptance criteria; only the PR description needs cleanup. It contains a process-narration 'Revision round' section (scar tissue about basing on pre-CG-082 main and resolving merge conflicts) that must be removed. cost=$1.16
- 2026-09-04T21:22:44+00:00 dispatched revise run 20260904T212243Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~13411 tokens)
- 2026-09-04T21:25:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/48: Addressed the sole review item: removed the process-narration '## Revision round' section from the PR description. No code change was needed — the feature is complete, 231 tests pass and ruff is clean (the 23 local failures are only because GARDEN_ROOT is set to the worker sentinel, which test_isolation intentionally refuses). cost=$0.46
