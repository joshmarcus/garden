---
id: CG-215
title: 'Onboarding skill and command: analyse an existing project and its environment to create a garden
  product, principles, setup config and a first phase'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/scaffold.py
- src/garden/planner.py
- src/garden/cli/scaffold.py
- .claude/skills/garden-plan/SKILL.md
- .claude/skills/garden-operate/SKILL.md
- examples/garden.work.yaml
- docs/design.md
created: '2026-09-05T16:09:07+00:00'
updated: '2026-09-05T16:09:07+00:00'
---

## Goal

A team can point the garden at a repository they already have and get a working garden out of it in one sitting: `garden onboard <repo> [--into <garden>]` (and the same flow as a Claude Code skill, `garden-onboard`, for someone who prefers the interactive session) reads what the project already says about itself and its environment, then drafts the garden files for a person to edit and approve: `product.md` with a module map, `principles/` seeded from the project's conventions, a `garden.yaml` products entry with the setup commands the project really uses, and a first phase with goals and draft tasks from the project's existing backlog.

## Context

Requested by the user on 2026-09-05 for enterprise use: "analyzing an existing project (docs, task lists, etc) and environment to create a new project." The user's standing constraint applies (2026-09-04): the venv-and-pip setup is specific to this repository; in a work setting dependencies, tests and lint are run differently, so the onboarding must discover the project's own commands rather than assume Python. Today `garden init` scaffolds an empty garden and `garden plan` turns goals into tasks, but nothing reads an existing project, and the operator wrote product.md, the principles and the setup block by hand for this garden.

## What it reads

- Docs: README, CONTRIBUTING, ARCHITECTURE and `docs/`, ADRs, CODEOWNERS, issue and PR templates.
- The environment: package manifests and lockfiles (pyproject, package.json, go.mod, Cargo.toml, pom, Gemfile, Makefile, justfile, Taskfile), CI workflows (which commands run tests and lint, which runners and secrets), Dockerfiles and devcontainers, pre-commit config, branch protection and review rules (via `gh`), the default branch.
- The backlog: TODO and FIXME comments with owners, GitHub issues and milestones (via `gh`), a `docs/roadmap.md` or `TODO.md`, open PRs.
- What it must not read or copy: secrets, `.env` files, credentials in CI config; it names them as "configure by hand" in the output.

## What it writes (all as drafts for a person to edit)

- `<product>/product.md`: purpose, users, a module map from the tree, conventions, the commands to build, test and lint.
- `principles/` entries for conventions it found (formatting, review rules, commit style) that are not already covered.
- The `garden.yaml` products entry: repo, base branch, id prefix, `setup.command`, `setup.test`, `setup.lint`, `setup.env` names (not values), `trusted_authors` from CODEOWNERS, and a note on anything it could not determine.
- `<product>/phase-01/goals.md` and draft tasks from the backlog with provenance (`discovered_from: onboard:<source>`), through the planner so they have criteria and reading lists; `garden validate` and `garden doctor` pass on the result.
- An onboarding report (`<product>/docs/onboarding.md`) listing what it read, what it inferred, what it could not, and the decisions the person must make (tiers, budgets, notify, automerge policy).

## Acceptance criteria

- [ ] `garden onboard <path-or-url>` on this repository produces a product.md, a products entry with the right setup commands, principles and a first phase of drafts, and `garden validate` passes; the same for a fixture project that is not Python (a small Node or Go repo in `tests/fixtures/`).
- [ ] Nothing secret is copied: a fixture with a `.env` and a CI secret reference yields "configure by hand" entries, and a test asserts no value leaked.
- [ ] The Claude Code skill `garden-onboard` drives the same flow interactively and ships with `garden init` like the other skills (CG-143).
- [ ] The onboarding report names every inference and every open decision.
- [ ] Tests with the fake harness for the planner step; the discovery step is deterministic and tested without a model.

