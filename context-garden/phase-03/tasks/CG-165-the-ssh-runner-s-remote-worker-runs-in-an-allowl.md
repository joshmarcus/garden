---
id: CG-165
title: The ssh runner's remote worker runs in an allowlisted environment
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-154
priority: 3
difficulty: medium
reading: []
discovered_from: CG-154
created: '2026-09-05T04:01:03+00:00'
updated: '2026-09-05T04:05:55+00:00'
---

## Goal

`runner/ssh.py`'s remote script runs the harness in the remote login environment. Apply the same allowlist as `runner.base.PASS_ENV` (plus `worker_env.pass` and `setup.env`) on the remote side, e.g. `env -i` with the kept variables, so a remote host's ambient tokens do not reach the worker either.

## Context

CG-154 scrubbed the local runner; the ssh runner was left as documented in docs/architecture.md (rules the code keeps).

## Provenance

Discovered by CG-154 (Trust at the edges: PR feedback only from trusted authors, a scrubbed worker environment, sanitised HTML and an origin check on POSTs) during run `20260905T034729Z-work`.

## Log

- 2026-09-05T04:01:03+00:00 discovered by CG-154
- 2026-09-05T04:05:54+00:00 approved (web)
- 2026-09-05T04:05:55+00:00 priority 1 -> 3 (web)
