---
id: CG-060
title: Reading lists resolve product paths against the product repo
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- context-garden/phase-01-bootstrap/specs/brief.md
branch: garden/cg-060-reading-lists-resolve-product-paths-against-the
pr: https://github.com/joshmarcus/context-garden/pull/31
attempts: 1
last_dispatched_at: '2026-09-04T18:16:40+00:00'
created: '2026-09-04T18:16:39+00:00'
updated: '2026-09-04T18:25:21+00:00'
---

## Goal

A task's reading list may name files in the product's repository (`src/garden/brief.py`) as well as in the garden (`context-garden/.../specs/x.md`); the brief inlines both, `garden validate` checks both, and a file it cannot find is still listed for the worker rather than dropped.

## Context

The garden now lives in its own repository and names the product by URL, so the product's files are under `.garden/repos/context-garden` (and, at dispatch, in the task's worktree at the base branch). `build_brief` resolves every reading path against the garden root only: in this garden 69 reading entries are reported missing by `garden validate`, and the brief silently drops them, so a worker gets the task body and the product's module map but none of the source it was meant to read. Resolve each path first against the garden root, then against the product's checkout (the worktree if one exists for the task, else the clone at the base branch, cloning if needed); inline from there under the same size rules; list what is still missing under "Reading list (read these)" with a note that it was not found, since paths are relative to the worker's directory anyway. `validate` and `garden brief --stats` use the same resolution.

## Acceptance criteria

- [ ] a reading path that exists only in the product repo is inlined (or referenced when large) with its product-relative path.
- [ ] a path found nowhere is still listed for the worker and reported by `validate`, not dropped.
- [ ] `garden validate` on this garden reports no missing product paths.
- [ ] tests with a garden whose product is a separate local repo.

## Log

- 2026-09-04T18:16:40+00:00 dispatched work run 20260904T181639Z-work via manual [human] (fresh session, base main, ~2509 tokens)
- 2026-09-04T18:21:23+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/31 (base main): Reading-list paths resolve against the garden, then the task's worktree, then the product clone; validate uses the same rule; a path found nowhere is still listed for the worker instead of dropped.
- 2026-09-04T18:25:15+00:00 automated review: approve — All four acceptance criteria are met with correct logic and a focused test. One nit: the loop variable `base` in `build_brief` shadows the function parameter of the same name — no current bug, but a latent trap. cost=$0.35
- 2026-09-04T18:25:21+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/31
