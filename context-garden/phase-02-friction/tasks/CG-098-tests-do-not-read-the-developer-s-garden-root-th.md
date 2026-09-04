---
id: CG-098
title: Tests do not read the developer's GARDEN_ROOT; the check command need not unset it
status: in_review
product: context-garden
phase: phase-02-friction
depends_on:
- CG-090
- CG-101
priority: 1
difficulty: easy
reading:
- tests/conftest.py
- tests/test_cli.py
- src/garden/checks.py
- src/garden/config.py
branch: garden/cg-098-tests-do-not-read-the-developer-s-garden-root-th
pr: https://github.com/joshmarcus/context-garden/pull/54
attempts: 1
last_dispatched_at: '2026-09-04T22:00:15+00:00'
created: '2026-09-04T21:09:46+00:00'
updated: '2026-09-04T22:07:59+00:00'
---

## Goal

The test suite passes whatever `GARDEN_ROOT` and `GARDEN_EXEC_ROOT` are set to in the environment that runs it, so the pre-PR tests check does not need `env -u GARDEN_ROOT` in front of pytest.

## Context

Found on the first live run, right after CG-082 landed. The check runner sets `GARDEN_ROOT` to a non-existent sentinel so a check cannot act on the live garden, which is right. `test_status_ls_graph_validate` in `tests/test_cli.py` runs `garden status` without `--root`, so the CLI read the sentinel and exited 2 ("does not contain garden.yaml; workers must not run garden commands against the live garden"). Every branch failed its tests check for a few ticks, three revise runs were spent on a failure none of them could fix, and CG-091 was marked failed for saying so. The stopgap is `env -u GARDEN_ROOT` in the tests check of the live garden.yaml. The real fix is an autouse fixture in `tests/conftest.py` that deletes both variables (`monkeypatch.delenv(..., raising=False)`) so the suite behaves the same in a developer's shell, in CI and under the check runner. State the rule in the `checks.py` docstring: a product's tests must not depend on the garden's environment variables.

## Acceptance criteria

- [ ] `GARDEN_ROOT=/nonexistent .venv/bin/pytest -q` passes.
- [ ] a test asserts the fixture cleared both variables.
- [ ] the checks docstring states the rule.

## Log

- 2026-09-04T21:35:18+00:00 dispatched work run 20260904T213518Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-090-state-save-never-clears-dirty-keys-after-a-succe stacked on CG-090, ~11620 tokens)
- 2026-09-04T21:42:29+00:00 discovered work filed: CG-113
- 2026-09-04T21:43:00+00:00 opened https://github.com/joshmarcus/context-garden/pull/54 (base garden/cg-090-state-save-never-clears-dirty-keys-after-a-succe): Extended the autouse tests/conftest.py fixture to strip GARDEN_EXEC_ROOT alongside GARDEN_ROOT, documented the rule in checks.py's docstring, and added a subprocess-based test proving both vars are cleared regardless of the invoking shell's environment. cost=$1.89
- 2026-09-04T21:44:08+00:00 automated review: approve — Extends the autouse conftest fixture to strip GARDEN_EXEC_ROOT alongside GARDEN_ROOT, documents the rule in checks.py, and adds a subprocess probe test. All three acceptance criteria verified; full suite passes with ambient env set. cost=$0.46
- 2026-09-04T21:44:14+00:00 CI failure
- 2026-09-04T21:44:15+00:00 dispatched revise run 20260904T214415Z-revise via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-090-state-save-never-clears-dirty-keys-after-a-succe, ~13128 tokens)
- 2026-09-04T21:55:10+00:00 no active run found; back to ready
- 2026-09-04T21:56:21+00:00 back to in_review: the revise run finished with nothing to change but the orphan sweep closed it before the reap; PR #54 stands, CI rerun for the known flake
- 2026-09-04T21:57:25+00:00 2 new review item(s) + CI failure
- 2026-09-04T22:00:15+00:00 dispatched revise run 20260904T220015Z-revise via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-090-state-save-never-clears-dirty-keys-after-a-succe, ~13831 tokens)
- 2026-09-04T22:02:58+00:00 parent CG-090 merged; will rebase onto main when the current run finishes
- 2026-09-04T22:07:19+00:00 discovered work filed: CG-119
- 2026-09-04T22:07:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/54: Fixed the Codex bot's PYTEST_ADDOPTS leak in the ambient-env probe subprocess (tests/test_isolation.py); the CI failure in test_scheduler.py is a pre-existing flake unrelated to this branch's diff (already flagged as such earlier in this PR's history), confirmed by 3x full-suite and 5x targeted-test local runs with no failures. cost=$1.22
- 2026-09-04T22:07:59+00:00 parent CG-090 merged; rebased onto main and retargeted the PR
