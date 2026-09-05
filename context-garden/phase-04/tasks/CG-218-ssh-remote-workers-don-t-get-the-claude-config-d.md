---
id: CG-218
title: SSH remote workers don't get the CLAUDE_CONFIG_DIR/CODEX_HOME defaults
status: in_review
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
branch: garden/cg-218-ssh-remote-workers-don-t-get-the-claude-config-d
pr: https://github.com/joshmarcus/context-garden/pull/176
discovered_from: CG-217
attempts: 1
last_dispatched_at: '2026-09-05T17:50:42+00:00'
created: '2026-09-05T16:45:22+00:00'
updated: '2026-09-05T18:09:43+00:00'
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
- 2026-09-05T17:50:42+00:00 dispatched work run 20260905T175023Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~19516 tokens)
- 2026-09-05T18:05:26+00:00 opened https://github.com/joshmarcus/context-garden/pull/176 (base main): Threaded resolved CLAUDE_CONFIG_DIR/CODEX_HOME (and worker_env.config_dirs overrides) into the ssh runner's remote script as conditional export lines, sharing the resolution logic with the local runner's scrubbed_env via a new config_dir_env helper. cost=$1.81
- 2026-09-05T18:09:37+00:00 description rewritten by the reviewer cost=$0.50
- 2026-09-05T18:09:43+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
