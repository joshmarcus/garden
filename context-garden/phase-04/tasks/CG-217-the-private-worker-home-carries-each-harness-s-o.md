---
id: CG-217
title: The private worker HOME carries each harness's own config by default (CLAUDE_CONFIG_DIR, CODEX_HOME),
  doctor checks a worker can log in, and a not-logged-in exit is an environment stop
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/runner/base.py
- src/garden/harness.py
- src/garden/cli/diagnostics.py
- tests/test_runners.py
- docs/architecture.md
branch: garden/cg-217-the-private-worker-home-carries-each-harness-s-o
pr: https://github.com/joshmarcus/context-garden/pull/169
attempts: 1
last_dispatched_at: '2026-09-05T17:17:14+00:00'
created: '2026-09-05T16:26:12+00:00'
updated: '2026-09-05T17:42:08+00:00'
---

## Goal

Isolating a worker's HOME (CG-194) must not log the harness out. By default the scrubbed environment points each harness at its own configuration and credentials without exposing the operator's home: `CLAUDE_CONFIG_DIR` for claude (its credentials live in `~/.claude/.credentials.json`), `CODEX_HOME` for codex, and a documented key for a custom harness. `garden doctor` runs a one-line prompt through the scrubbed environment for every configured harness and fails when it is not logged in. A "Not logged in" exit is classified as an environment stop (CG-212's mechanism), so it pauses the harness instead of failing tasks.

## Context

2026-09-05 15:58: the pin moved to a build containing CG-194 (workers get no HOME). From that minute every worker and reviewer exited within a minute with "Not logged in · Please run /login": CG-214 burned both attempts and went `failed`, four reviews returned no verdict, and the six approved PRs in the queue stalled, until the operator found it at 16:23, put `CLAUDE_CONFIG_DIR=/home/joshua/.claude` into the service's environment (it passes through the `CLAUDE_*` allowlist) and restarted. The unit tests passed because the fake harness needs no login. `garden doctor` checks the binaries are on PATH, not that a worker can authenticate through the environment it will actually get.

## Acceptance criteria

- [ ] `scrubbed_env` sets `CLAUDE_CONFIG_DIR` (default `~/.claude`) and `CODEX_HOME` (default `~/.codex`) when the operator has not set them, so the private HOME does not hide the credentials; `worker_env.config_dirs` overrides the defaults per harness, and the docs say what each harness reads.
- [ ] `garden doctor` runs each configured harness once through the scrubbed environment with a trivial prompt and reports logged-in or not, with the fix; the walkthrough's doctor output shows the line.
- [ ] `Harness.parse` classifies "Not logged in" as `env_error` kind `auth`; with CG-212 that pauses the harness and leaves the task ready.
- [ ] A test builds the scrubbed environment and asserts the config-dir variables are present and HOME is not the operator's.

## Log

- 2026-09-05T16:26:12+00:00 approved (web)
- 2026-09-05T16:27:40+00:00 dispatched work run 20260905T162724Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~17849 tokens)
- 2026-09-05T16:48:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/169 (base main): scrubbed_env now defaults CLAUDE_CONFIG_DIR/CODEX_HOME to the operator's home (overridable via worker_env.config_dirs), garden doctor verifies each harness's login through that same environment with a trivial prompt, and Harness.parse tags a login failure as an auth env_error. cost=$3.73
- 2026-09-05T16:52:58+00:00 automated review: approve — Scrubbed-env config-dir defaults, doctor's real login probe, and the auth error_kind classification are all correctly implemented and tested; full suite and lint pass. cost=$0.70
- 2026-09-05T16:54:10+00:00 CI failure
- 2026-09-05T16:54:27+00:00 dispatched revise run 20260905T165427Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~20290 tokens)
- 2026-09-05T17:06:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/169: Fixed the CI failure by making garden doctor's harness-login line render with soft_wrap so a long worktree path can no longer split the login-failure detail mid-word across a terminal-width line break; the CG-217 feature itself was already correctly implemented in the prior commit. cost=$1.45
- 2026-09-05T17:12:24+00:00 automated review requested changes: Config-dir defaults, doctor's real login probe, and the soft-wrap fix are all correct and tested, but the auth classification uses a different field name (error_kind) than CG-212's actual env_error/env_kind convention, so it won't trigger an environment stop once CG-212 merges — the core motivation for this task. cost=$0.75
- 2026-09-05T17:17:14+00:00 dispatched revise run 20260905T171714Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~20253 tokens)
- 2026-09-05T17:25:05+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/169: Renamed the auth-failure classification from error_kind:"auth" to CG-212's env_error/env_kind convention (env_error=True, env_kind="auth") in Harness.parse and check_login, so a not-logged-in exit will be recognized as an environment stop once CG-212 merges, and updated docs/tests accordingly. cost=$0.93
- 2026-09-05T17:29:37+00:00 automated review: approve — Config-dir defaults, doctor's real login probe, and the env_error/env_kind auth classification are all correctly implemented and verified to actually feed CG-212's harness-pause path; full suite and lint pass. cost=$0.63
- 2026-09-05T17:36:42+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T17:39:01+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T17:42:08+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/169
