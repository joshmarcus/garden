---
id: CG-095
title: checks.pre_pr can fail with a confusing exit-127 error if GARDEN_ROOT's venv isn't provisioned
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/brief.py
- src/garden/review.py
discovered_from: CG-037
created: '2026-09-04T21:02:12+00:00'
updated: '2026-09-04T21:02:12+00:00'
---

`checks.pre_pr` commands in garden.yaml shell out to `$GARDEN_ROOT/.venv/bin/python` and `$GARDEN_ROOT/.venv/bin/ruff`, reusing the garden root's installed tooling against each worktree's own src/tests. If GARDEN_ROOT points at a directory without a prepared .venv (as happened on this task's second-to-last revise round, path ending in `no-live-garden/.venv/bin/python`), the check fails with a raw shell 'not found' (exit 127) that reads like a code problem rather than an environment one, and gets fed back into the next revise brief as review feedback to address. Consider a clearer failure message from checks.py when the interpreter/binary itself is missing (vs. a real test/lint failure), so a revise worker doesn't waste a round trying to root-cause an environment gap it can't fix.

## Provenance

Discovered by CG-037 (Stop the revise template and the review prompt contradicting each other) during run `20260904T205753Z-revise`.

## Log

- 2026-09-04T21:02:12+00:00 discovered by CG-037
