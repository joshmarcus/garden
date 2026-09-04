---
id: CG-123
title: Tasks that edit the garden's own files run in a worktree of the garden repo
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/config.py
- src/garden/scheduler.py
- src/garden/runner/local.py
- docs/architecture.md
created: '2026-09-04T23:13:34+00:00'
updated: '2026-09-04T23:13:34+00:00'
---

## Goal

A task whose deliverable is a change to the garden's own files (a phase's friction document, the next phase's goals, the product overview, `garden.yaml`) can be done by a worker, in a worktree of the garden repo, through a PR to the garden repo, with the same fence, checks and review as any product task.

## Context

Asked during the first live run, after the third such task in one evening. CG-092 (drop the install lines from the live config), CG-107 (adopt the setup block) and CG-029 (close the phase: friction document and next goals) were all dispatched to workers who then rightly said the files are in `joshmarcus/garden`, not in the product checkout, and stopped; each became a manual task or was done by hand. The garden repo is a git repository with an origin like any product, so the simplest shape is to let it be one: a product entry whose repo is the garden itself (`products.garden: {repo: <the garden's origin>, self: true}`), with the task files under it owned by the scheduler as usual. A worker on such a task gets a worktree of the garden repo under `work_dir`, edits docs and config there, and opens a PR to the garden repo; the live garden picks the change up when the person merges and `garden sync` pulls it. The fence (CG-111) must treat that worktree as the worker's own while still denying the live checkout. Checks for that product are whatever the config says (a YAML validation of `garden.yaml`, a link check for docs). Write the constraint in `docs/architecture.md`: the live garden is never edited by a worker; changes to it arrive by PR like everything else.

## Acceptance criteria

- [ ] a product entry can point at the garden's own repo; `garden doctor` shows it and refuses a `work_dir` inside the live garden.
- [ ] a task in that product runs in a worktree of the garden repo and opens a PR there; a test with the fake harness and a temporary garden repo.
- [ ] the fence denies the live garden and allows the worker's garden worktree.
- [ ] `docs/architecture.md` states the rule.
