---
id: CG-218
title: SSH remote workers don't get the CLAUDE_CONFIG_DIR/CODEX_HOME defaults
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/runner/base.py
- src/garden/harness.py
- src/garden/cli/diagnostics.py
- tests/test_runners.py
- docs/architecture.md
discovered_from: CG-217
created: '2026-09-05T16:45:22+00:00'
updated: '2026-09-05T17:48:27+00:00'
---

## Goal

CG-217 added CLAUDE_CONFIG_DIR/CODEX_HOME defaulting to runner.base.scrubbed_env, used by the local runner and checks. The ssh runner's remote script (runner/ssh.py's REMOTE_SCRIPT) does its own shell-side environment scrub (garden_scrub()) and never learns these defaults, so an ssh-dispatched worker's isolated remote HOME can still hide the harness's login the way CG-194 broke the local runner.

Fix: thread the resolved CLAUDE_CONFIG_DIR/CODEX_HOME (and any worker_env.config_dirs overrides) into the remote script as extra `export` lines, the same way setup.env already rides along.

## Provenance

Discovered by CG-217 (The private worker HOME carries each harness's own config by default (CLAUDE_CONFIG_DIR, CODEX_HOME), doctor checks a worker can log in, and a not-logged-in exit is an environment stop) during run `20260905T162724Z-work`.

## Log

- 2026-09-05T16:45:22+00:00 discovered by CG-217
- 2026-09-05T17:48:26+00:00 approved (web)
- 2026-09-05T17:48:27+00:00 priority 0 -> 3 (web)
