---
id: CG-215
title: 'Onboarding skill and command: analyse an existing project and its environment to create a garden
  product, principles, setup config and a first phase'
status: changes_requested
product: context-garden
phase: phase-05
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
branch: garden/cg-215-onboarding-skill-and-command-analyse-an-existing
pr: https://github.com/joshmarcus/context-garden/pull/216
attempts: 1
last_dispatched_at: '2026-09-06T12:16:36+00:00'
created: '2026-09-05T16:09:07+00:00'
updated: '2026-09-06T13:14:52+00:00'
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

## Log

- 2026-09-05T16:11:15+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-06T00:50:16+00:00 approved (cli)
- 2026-09-06T03:11:25+00:00 dispatched work run 20260906T031110Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20130 tokens)
- 2026-09-06T03:36:53+00:00 opened https://github.com/joshmarcus/context-garden/pull/216 (base main): Added deterministic, secret-safe onboarding for local paths and git URLs, including generated product context, principles, setup configuration, first-phase planner drafts, and an onboarding report. Added and scaffolded the interactive garden-onboard skill. cost=$2.41
- 2026-09-06T03:42:26+00:00 automated review requested changes: The implementation passes all checks, but it can overwrite an existing product and does not provide complete, deterministic discovery/reporting as required. cost=$0.59
- 2026-09-06T03:44:35+00:00 dispatched revise run 20260906T034432Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21475 tokens)
- 2026-09-06T04:02:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/216: Made onboarding collision-safe, auditable, and locally deterministic. Optional GitHub enrichment is now separated from deterministic discovery, generated facts carry provenance, and stable project names are retained across worktrees and URL clones. cost=$0.86
- 2026-09-06T04:04:13+00:00 automated review requested changes: The core onboarding flow works for the Node fixture, but required provenance, secret safety, and environment discovery remain incomplete. cost=$0.35
- 2026-09-06T04:04:57+00:00 dispatched revise run 20260906T040456Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21948 tokens)
- 2026-09-06T04:28:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/216: Completed safe, deterministic onboarding discovery with preserved backlog provenance, credential-safe CI command handling, broader environment input support, and exact inference reporting. The revision is committed and the full test and lint suites pass. cost=$1.32
- 2026-09-06T04:34:40+00:00 automated review requested changes: The Node fixture flow works, but onboarding does not produce this repository's required commands and the report/provenance guarantees remain incomplete. cost=$0.45
- 2026-09-06T04:37:11+00:00 dispatched revise run 20260906T043710Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22266 tokens)
- 2026-09-06T05:06:08+00:00 pre-PR checks failed (test) and 3 revision rounds already used; needs a human cost=$1.63
- 2026-09-06T05:25:16+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-06T05:29:21+00:00 dispatched revise run 20260906T052917Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22231 tokens)
- 2026-09-06T05:58:06+00:00 worker says nothing to change: The reported pre-PR failure was a SIGTERM rather than a code assertion failure. A rerun passed the entire onboarding suite; the full suite advanced beyond the prior termination point but later stalled under severe concurrent test/process contention on the host, so there is no branch defect to fix from the supplied feedback. cost=$1.28
- 2026-09-06T06:22:42+00:00 no-change accepted by the person; resuming the round without a new work run
- 2026-09-06T06:22:51+00:00 operator: no-change accepted (the check was killed by the 05:25 service restart); back to review (CG-328)
- 2026-09-06T07:02:48+00:00 pre-PR check(s) test failed at the stale base 58184073c06b; the base branch `main` had moved, so rebased onto it and the checks pass now — no revise round
- 2026-09-06T07:02:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/216: Verified the existing onboarding implementation without modifying the clean branch. All 14 onboarding tests and the complete lint check pass.
- 2026-09-06T07:02:52+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-215` for one more round, or review on GitHub
- 2026-09-06T07:04:19+00:00 automated review requested changes: The core onboarding flow and tests work, but CODEOWNERS team parsing can trust the wrong account and the report is not a complete record of inspected inputs. cost=$0.43
- 2026-09-06T10:04:59+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-06T10:17:35+00:00 dispatched revise run 20260906T101732Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22895 tokens)
- 2026-09-06T11:11:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/216: Completed onboarding provenance and CODEOWNERS safety: team ownership tokens are no longer added as trusted users, and the report records every local source, workflow, documentation, and environment input inspected. The change is committed and all tests and lint pass. cost=$1.46
- 2026-09-06T11:11:40+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-215` for one more round, or review on GitHub
- 2026-09-06T11:38:51+00:00 automated review requested changes: The onboarding flow passes its focused tests, but it does not meaningfully derive project conventions and can fabricate backlog provenance for planner tasks. Both undermine the core promise that generated drafts are grounded in the existing project. cost=$0.52
- 2026-09-06T11:41:11+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-215`) or send it back (`garden triage CG-215 --changes "..."`)
- 2026-09-06T11:53:27+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-06T12:16:36+00:00 dispatched revise run 20260906T121626Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~23143 tokens)
- 2026-09-06T12:52:39+00:00 revision failed: no GARDEN_RESULT in worker output (see final.md)
- 2026-09-06T13:14:52+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
