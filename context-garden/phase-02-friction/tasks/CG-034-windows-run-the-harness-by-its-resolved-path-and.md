---
id: CG-034
title: 'Windows: run the harness by its resolved path and give pre-PR checks a shell'
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/runner/local.py
- src/garden/checks.py
- garden.yaml
branch: garden/cg-034-windows-run-the-harness-by-its-resolved-path-and
pr: https://github.com/joshmarcus/context-garden/pull/16
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T18:43:39+00:00'
created: '2026-09-04T17:03:09+00:00'
updated: '2026-09-04T18:55:23+00:00'
---

## Goal

A garden on Windows either works with a harness installed as `claude.cmd` and the default `checks.pre_pr`, or doctor says plainly that Windows needs WSL.

## Context

On the Windows attempt before CG-027, doctor passed (`shutil.which` finds `claude.cmd`) but the local runner starts every worker through `sh -c`, which does not find it. The `checks.pre_pr` commands use `$GARDEN_ROOT` and POSIX quoting. Options: resolve the binary with `shutil.which` at dispatch and put the absolute path in the command; run commands through the platform shell; or refuse on `os.name == 'nt'` in doctor with a pointer to WSL. Pick one and document it in the README.

## Acceptance criteria

- [ ] the runner's command uses the resolved harness path.
- [ ] either the checks run on Windows or doctor reports Windows as unsupported.
- [ ] README says which.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:09+00:00 discovered by CG-027
- 2026-09-04T17:23:51+00:00 approved (web)
- 2026-09-04T17:24:46+00:00 dispatched work run 20260904T172445Z-work via local [claude model=sonnet] (fresh session, base main, ~6266 tokens)
- 2026-09-04T17:34:19+00:00 discovered work filed: CG-049
- 2026-09-04T17:34:41+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/16 (base main): Harness.command() now resolves the binary via shutil.which so the absolute path appears in the sh -c script. LocalRunner.doctor() refuses on Windows (os.name == 'nt') with a WSL pointer. README documents the requirement. 119 tests pass, lint clean. cost=$1.64
- 2026-09-04T17:37:41+00:00 automated review: approve — All three acceptance criteria met with tests; implementation is correct and well-scoped. No blocking findings. cost=$0.25
- 2026-09-04T18:07:21+00:00 marked ready for review on GitHub; triage done
- 2026-09-04T18:07:23+00:00 1 new review item(s)
- 2026-09-04T18:35:27+00:00 triage: changes requested by hand: Codex review on PR #16, dropped at the time. (P1) src/garden/harness.py:74: resolving the harness to the scheduler's abs
- 2026-09-04T18:43:39+00:00 dispatched revise run 20260904T184339Z-revise via local [claude model=sonnet] (fresh session, base main, ~6749 tokens)
- 2026-09-04T18:54:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/16: Moved shutil.which bin resolution from Harness.command() into LocalRunner.harness_shell() so SSH runs keep the bare binary name (resolved on the scheduler's machine would be wrong for the remote host). Rebased onto main, resolving the harness.py conflict. 153 tests pass, lint clean. cost=$1.79
- 2026-09-04T18:55:23+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/16
