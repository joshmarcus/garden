---
id: CG-092
title: Remove venv install lines from the context-garden garden config and product overview
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/runner/local.py
- src/garden/runner/ssh.py
- src/garden/brief.py
- src/garden/config.py
- examples/garden.work.yaml
discovered_from: CG-081
created: '2026-09-04T20:26:01+00:00'
updated: '2026-09-04T20:57:20+00:00'
---

## Goal

In the `joshmarcus/garden` repo, now that the tool defaults `checks.pre_pr` to the product's `setup.test`/`setup.lint` and the brief states the prepared environment, update context-garden's live config to use a `setup` block (`uv sync --extra dev`, `test`/`lint`) and drop the `$GARDEN_ROOT/.venv/bin/python` `checks.pre_pr`, and remove the `uv venv && uv pip install -e` install instructions from the product overview so no brief inlines them. This is in the garden repo, not the tool repo.

## Provenance

Discovered by CG-081 (Environment setup is per-product configuration, not a venv assumption) during run `20260904T201042Z-work`.

## Log

- 2026-09-04T20:26:01+00:00 discovered by CG-081
- 2026-09-04T20:57:20+00:00 approved (web)
