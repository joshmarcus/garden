---
id: CG-032
title: Doctor checks that gh and the harness are logged in and git has an identity
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/github.py
- src/garden/runner/local.py
branch: garden/cg-032-doctor-checks-that-gh-and-the-harness-are-logged
pr: https://github.com/joshmarcus/context-garden/pull/15
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T18:51:53+00:00'
created: '2026-09-04T17:03:09+00:00'
updated: '2026-09-04T18:51:53+00:00'
---

## Goal

`garden doctor` fails when `gh` is not logged in, when the harness is not logged in, or when git has no `user.name`/`user.email`, and says which.

## Context

On the first live run (CG-027) doctor printed "all good" with both tools logged out: it only checks that the binaries are on PATH. The github line shows `gh CLI (path)` without `as <login>` when `gh.me()` is empty, and nothing looks at the harness at all. A logged-out `claude -p` exits 0 with `is_error: true`, so the first sign was a failed attempt. The worktree's first commit failed with "Author identity unknown" because the WSL profile had no git identity; a headless worker would fail the same way. Use `gh auth status`, `claude auth status --json` (or a cheap probe) and `git config user.email`.

## Acceptance criteria

- [ ] doctor exits 1 with a red line when gh, the harness, or the git identity is missing.
- [ ] the github line always shows the login when there is one.
- [ ] a test covers each check with a fake.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:09+00:00 discovered by CG-027
- 2026-09-04T17:23:50+00:00 approved (web)
- 2026-09-04T17:24:44+00:00 dispatched work run 20260904T172444Z-work via local [claude model=haiku] (fresh session, base main, ~6509 tokens)
- 2026-09-04T17:28:24+00:00 pre-PR checks failed (tests, lint); no PR opened yet; revise run will fix cost=$0.53
- 2026-09-04T17:28:26+00:00 dispatched revise run 20260904T172825Z-revise via local [claude model=haiku] (fresh session, base main, ~7583 tokens)
- 2026-09-04T17:32:27+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/15 (base main): Fixed lint error (removed unnecessary f-string prefix) and resolved all test mock issues by refactoring side_effect functions to properly handle subprocess calls without duplicate keyword arguments. All 11 tests pass and linting is clean. cost=$0.52
- 2026-09-04T17:34:19+00:00 automated review requested changes: All acceptance criteria met, implementation is correct and well-tested; PR description has scar tissue focusing on review feedback fixes rather than what the feature accomplishes. cost=$0.13
- 2026-09-04T17:36:39+00:00 dispatched revise run 20260904T173639Z-revise via local [claude model=sonnet] (fresh session, base main, ~7094 tokens)
- 2026-09-04T17:37:40+00:00 environment error (not an attempt): All 4 doctor tests pass and lint is clean. The only thing to address is rewriting the PR description per the reviewer's feedback. There are no code changes needed — I'll just respond with the correcte
- 2026-09-04T17:43:38+00:00 dispatched work run 20260904T174338Z-work via local [claude model=sonnet] (fresh session, base main, ~7088 tokens)
- 2026-09-04T17:46:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/15: garden doctor now fails with exit code 1 and a red [NOT LOGGED IN] line when gh or the harness is unauthenticated, shows the gh login when present, and fails when git has no user.name/user.email. Four tests cover each check. All 117 tests pass and lint is clean. cost=$0.50
- 2026-09-04T17:47:00+00:00 CI failure
- 2026-09-04T17:49:21+00:00 dispatched revise run 20260904T174920Z-revise via local [claude model=sonnet] (fresh session, base main, ~8189 tokens)
- 2026-09-04T18:13:55+00:00 revision failed: worker exited 143: worker produced no output
- 2026-09-04T18:44:22+00:00 re-enabled by hand; revise run will follow
- 2026-09-04T18:51:53+00:00 dispatched revise run 20260904T185152Z-revise via local [claude model=sonnet] (fresh session, base main, ~7492 tokens)
