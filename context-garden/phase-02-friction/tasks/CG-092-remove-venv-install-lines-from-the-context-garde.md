---
id: CG-092
title: Remove venv install lines from the context-garden garden config and product overview
status: running
product: context-garden
phase: phase-02-friction
depends_on:
- CG-081
priority: 1
difficulty: easy
reading:
- src/garden/runner/local.py
- src/garden/runner/ssh.py
- src/garden/brief.py
- src/garden/config.py
- examples/garden.work.yaml
branch: garden/cg-092-remove-venv-install-lines-from-the-context-garde
discovered_from: CG-081
attempts: 1
last_dispatched_at: '2026-09-04T21:21:03+00:00'
created: '2026-09-04T20:26:01+00:00'
updated: '2026-09-04T21:21:03+00:00'
---

## Goal

In the `joshmarcus/garden` repo, now that the tool defaults `checks.pre_pr` to the product's `setup.test`/`setup.lint` and the brief states the prepared environment, update context-garden's live config to use a `setup` block (`uv sync --extra dev`, `test`/`lint`) and drop the `$GARDEN_ROOT/.venv/bin/python` `checks.pre_pr`, and remove the `uv venv && uv pip install -e` install instructions from the product overview so no brief inlines them. This is in the garden repo, not the tool repo.

## Provenance

Discovered by CG-081 (Environment setup is per-product configuration, not a venv assumption) during run `20260904T201042Z-work`.

## Log

- 2026-09-04T20:26:01+00:00 discovered by CG-081
- 2026-09-04T20:57:20+00:00 approved (web)
- 2026-09-04T21:11:10+00:00 dispatched work run 20260904T211110Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~10800 tokens)
- 2026-09-04T21:13:39+00:00 worker asks: This task's edits belong in the joshmarcus/garden repo (garden.yaml checks.pre_pr, context-garden/product.md), not in this context-garden tool checkout, and it also depends on CG-081's setup-block feature which is still an unmerged branch. Should this task be re-dispatched against a proper checkout/worktree of the garden repo (after CG-081 merges), rather than as a context-garden task? cost=$0.96
- 2026-09-04T21:14:56+00:00 manual task: the edits are in the garden repo (garden.yaml, product.md), which no worker checks out; a person does it after CG-081 merges
- 2026-09-04T21:19:42+00:00 back to waiting_human: the person's answer was dropped while the task was parked; answer again and the worker resumes
- 2026-09-04T21:21:03+00:00 dispatched resume run 20260904T212102Z-resume via local [claude model=claude-sonnet-5] (resumed session, base main, ~183 tokens)
