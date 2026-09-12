---
id: CG-452
title: Keep GitHub Actions analyzers scoped to the configured repository host
status: merged_into_parent
product: context-garden
phase: phase-07
depends_on:
- CG-395
- CG-396
priority: 1
difficulty: medium
reading:
- src/garden/checks.py
- src/garden/scheduler/reap.py
- src/garden/github.py
branch: garden/cg-452-keep-github-actions-analyzers-scoped-to-the-conf
pr: https://github.com/joshmarcus/context-garden/pull/344
runner: remote
discovered_from: Owner criteria/enterprise review audit2026-09-08
attempts: 1
last_dispatched_at: '2026-09-08T21:59:30+00:00'
created: '2026-09-08T19:24:46+00:00'
updated: '2026-09-10T15:10:57+00:00'
---

## Goal

Preserve enterprise host identity through serialized check context and every GitHub Actions analyzer command.

Sol audited mergedPR307/head669f519a: check_ctx serializes RepositorySlug as plain repo_slug, losing its host. Built-in github_actions_failures in checks.py invokes gh run list/view/rerun with -R owner/repo only, so ambient gh defaults can select another host. CG396 owns new CI receipts/status integration; wait for it and reuse its solution wherever possible.

## Acceptance criteria

- [ ] Serialized check context explicitly retains configured GitHub host identity.
- [ ] Actions list/view and suggested or invoked rerun commands consistently target that host; public and enterprise products with the same slug never cross routes.
- [ ] Deterministic two-host CLI/fallback tests prove command routing without live credentials; if mergedCG396 already covers it, provide exact-source evidence without duplicate implementation.

## Log

- 2026-09-08T19:26:15+00:00 approved (owner-delegated-hourly-audit)
- 2026-09-08T19:49:39+00:00 dispatched work run 20260908T194939Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an stacked on CG-396, ~14357 tokens)
- 2026-09-08T19:55:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/344 (base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an): Serialized check contexts now retain `repo_host`, and GitHub Actions list, view, and rerun operations use fully qualified host/repository selectors. Deterministic two-host tests prevent same-slug cross-routing. cost=$0.42
- 2026-09-08T21:53:26+00:00 CI failure
- 2026-09-08T21:53:47+00:00 dispatched revise run 20260908T215347Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an, ~14869 tokens)
- 2026-09-08T21:57:39+00:00 worker found no change to make: No source change is warranted: commit 204da1aed already satisfies the host-routing criteria, targeted tests pass, and exact-head CI also passed in run 34271610667.; reconciling with checks and a fresh review
- 2026-09-08T21:59:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/344: The existing implementation is correct and the reported CI test failure is non-reproducible: the identical commit has a successful GitHub Actions push run including lint and pytest. The unauthenticated Actions-analyzer message reflects unavailable credentials, not a routing defect. cost=$0.44
- 2026-09-08T21:59:28+00:00 PR conflicts with garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an; rebase onto garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an conflicts (src/garden/validation.py); a rebase agent will resolve it
- 2026-09-08T21:59:30+00:00 dispatched rebase run 20260908T215930Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an, conflict only; easy tier, ~2011 tokens)
- 2026-09-08T22:02:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/344: Rebased CG-452 and resolved both textual conflicts while preserving both sides. cost=$0.01
- 2026-09-09T01:08:50+00:00 PR merged into CG-396's branch (`garden/cg-396-use-pluggable-exact-head-ci-status-for-review-an`), not the base `main`; will be done once CG-396 reaches the base
- 2026-09-10T15:10:57+00:00 parent CG-396 merged to main, but this task's commits are not on main yet; still waiting
