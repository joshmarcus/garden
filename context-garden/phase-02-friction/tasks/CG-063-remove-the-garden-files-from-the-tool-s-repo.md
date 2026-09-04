---
id: CG-063
title: Remove the garden files from the tool's repo
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading: []
branch: garden/cg-063-remove-the-garden-files-from-the-tool-s-repo
pr: https://github.com/joshmarcus/context-garden/pull/34
attempts: 1
last_dispatched_at: '2026-09-04T19:12:19+00:00'
created: '2026-09-04T18:16:39+00:00'
updated: '2026-09-04T19:17:07+00:00'
---

## Goal

The tool's repository no longer carries the garden that drives it: `garden.yaml`, `principles/`, `personas/`, `context-garden/` and the interactive skills live in `joshmarcus/garden`, and the tool's README and CLAUDE.md say so.

## Context

The garden was moved out on 2026-09-04 after workers reached the live garden through the shared checkout. The copies in the tool's repo are now stale and would confuse a worker or a reader. Remove them; keep `docs/`, `examples/` and the tests (which build their own gardens). Update `CLAUDE.md` (the "Try it" lines assumed a garden at the root: point them at a `garden init` in a scratch directory or at the garden repo), the README's "this repo is its own first product" wording, and CI if it referenced any of the removed paths. `garden init` still writes a default principles digest and personas from `scaffold.py`, so the defaults do not depend on the removed files.

## Acceptance criteria

- [ ] none of `garden.yaml`, `principles/`, `personas/`, `context-garden/`, `.claude/skills/` remain in the tool's repo.
- [ ] tests and lint pass; CI is green.
- [ ] README and CLAUDE.md name the garden repo.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T19:12:19+00:00 dispatched work run 20260904T191219Z-work via local [claude model=sonnet] (fresh session, base main, ~2133 tokens)
- 2026-09-04T19:17:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/34 (base main): Removed garden.yaml, principles/, personas/, context-garden/, and .claude/skills/ from the tool repo. Updated CLAUDE.md and README.md to reference joshmarcus/garden and remove stale links to the deleted paths. CI unchanged (it only runs ruff and pytest). All 187 tests pass. cost=$0.64
