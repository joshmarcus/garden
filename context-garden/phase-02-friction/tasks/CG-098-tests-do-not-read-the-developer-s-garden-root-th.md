---
id: CG-098
title: Tests do not read the developer's GARDEN_ROOT; the check command need not unset it
status: ready
product: context-garden
phase: phase-02-friction
depends_on: [CG-090, CG-101]
priority: 1
difficulty: easy
reading:
- tests/conftest.py
- tests/test_cli.py
- src/garden/checks.py
- src/garden/config.py
created: '2026-09-04T21:09:46+00:00'
updated: '2026-09-04T21:09:46+00:00'
---

## Goal

The test suite passes whatever `GARDEN_ROOT` and `GARDEN_EXEC_ROOT` are set to in the environment that runs it, so the pre-PR tests check does not need `env -u GARDEN_ROOT` in front of pytest.

## Context

Found on the first live run, right after CG-082 landed. The check runner sets `GARDEN_ROOT` to a non-existent sentinel so a check cannot act on the live garden, which is right. `test_status_ls_graph_validate` in `tests/test_cli.py` runs `garden status` without `--root`, so the CLI read the sentinel and exited 2 ("does not contain garden.yaml; workers must not run garden commands against the live garden"). Every branch failed its tests check for a few ticks, three revise runs were spent on a failure none of them could fix, and CG-091 was marked failed for saying so. The stopgap is `env -u GARDEN_ROOT` in the tests check of the live garden.yaml. The real fix is an autouse fixture in `tests/conftest.py` that deletes both variables (`monkeypatch.delenv(..., raising=False)`) so the suite behaves the same in a developer's shell, in CI and under the check runner. State the rule in the `checks.py` docstring: a product's tests must not depend on the garden's environment variables.

## Acceptance criteria

- [ ] `GARDEN_ROOT=/nonexistent .venv/bin/pytest -q` passes.
- [ ] a test asserts the fixture cleared both variables.
- [ ] the checks docstring states the rule.
