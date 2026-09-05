---
id: CG-217
title: The private worker HOME carries each harness's own config by default (CLAUDE_CONFIG_DIR, CODEX_HOME),
  doctor checks a worker can log in, and a not-logged-in exit is an environment stop
status: ready
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
created: '2026-09-05T16:26:12+00:00'
updated: '2026-09-05T16:26:12+00:00'
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
