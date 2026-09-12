---
id: CG-348
title: Make EC2 pool cost health draining and teardown understandable and verifiable
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-345
- CG-346
- CG-347
priority: 2
order: 7
difficulty: medium
reading:
- context-garden/phase-06/specs/ec2-workers.md
branch: garden/cg-348-make-ec2-pool-cost-health-draining-and-teardown
pr: https://github.com/joshmarcus/context-garden/pull/418
attempts: 1
last_dispatched_at: '2026-09-10T11:07:38+00:00'
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-10T14:09:11+00:00'
---

## Owner validation policy, 2026-09-10

Live canaries are optional and cannot be required for task acceptance, review, merge, release or phase closure. Proportionate deterministic tests, provider fakes, protocol integration and disposable offline bootstrap/lifecycle exercises establish the required behavior. Report live-cloud coverage as untested when absent; that absence alone is not a blocker. Preserve genuine correctness, security, recovery, deadline and resource requirements. Any optional live exercise still requires its own applicable resource/spending authorization. This supersedes older live-canary or paid clean-image rollout requirements, including historical operator dispositions below.

## Goal and evidence

Deliver pool status and operator controls from the spec, integrating lifecycle, execution and Spot recovery. Show actual executing work, resource headroom, recovery state, estimated machine spend and model retry spend. Implement bounded launch/runtime policies, safe drain/disable, explicit emergency stop, and orphan-resource reconciliation. Billing delays must not be presented as an instantaneous hard budget guard.

Run an independently repeatable disposable acceptance exercise with provider fakes and offline protocol/lifecycle integration covering provisioning, work/check/review, interruption, controller restart and teardown. Verify cost accounting with declared synthetic prices and inventory modeled retained resources. Exercise operator actions and their consequences in the disposable application. A separately authorized live AWS canary is optional; report absent live coverage as untested without blocking acceptance.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Provide common host inventory, lifecycle and cost controls independently of garden, then garden-specific task views as an integration. Include a standalone remote-dev workflow using the same EC2 provider and lifecycle: create from a dev profile, obtain approved SSH/editor connection information, preserve edits through stop/start, and release with an explicit workspace retention/deletion choice. Respect active sessions and workplace-supplied access policies. Demonstrate no dependency on a garden daemon or model account. Document how a work platform supplies its own identity, network, images and secrets. Real workplace acceptance is optional and separate from the disposable example.

## Log

- 2026-09-07T12:47:31+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:31+00:00 approved (owner-phase05-promotion)
- 2026-09-09T13:56:28+00:00 owner moved deferred work from context-garden/phase-05 to context-garden/phase-08; destination remains frozen, status/history/dependencies preserved
- 2026-09-10T01:24:07+00:00 moved from context-garden/phase-08 to context-garden/phase-07
- 2026-09-10T06:30:30+00:00 dispatched work run 20260910T063027Z-work via local [codex model=gpt-5.6-terra] (fresh session, base garden/cg-347-recover-ec2-spot-interruptions-without-losing-ac stacked on CG-347, ~13098 tokens)
- 2026-09-10T06:33:45+00:00 preserved uncommitted worktree changes from run 20260910T063027Z-work outside the PR: `git stash apply 867ff3de4f115b4924b22bc21899e2cd5d9ad245` in /home/joshua/work/worktrees/CG-348 (garden:CG-348:20260910T063027Z-work:reap)
- 2026-09-10T06:33:45+00:00 environment stop (quota): quota limit hit on codex; not counted as an attempt; dispatch paused for codex until a probe succeeds
- 2026-09-10T10:47:53+00:00 dispatched work run 20260910T104750Z-work via local [codex model=gpt-5.6-terra] (fresh session, base garden/cg-347-recover-ec2-spot-interruptions-without-losing-ac stacked on CG-347, ~13257 tokens)
- 2026-09-10T10:51:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T10:52:28+00:00 opened https://github.com/joshmarcus/context-garden/pull/418 (base garden/cg-347-recover-ec2-spot-interruptions-without-losing-ac): Added durable pool draining, explicit emergency teardown, and EC2 orphan-resource inventory in commit 7d833e47. Verified 70 focused host lifecycle/scale tests, Ruff, and the hosts-scale CLI surface; live AWS was not exercised. cost=$0.85
- 2026-09-10T10:54:54+00:00 automated review requested changes: Safe draining and durable teardown status are covered, but emergency stop fails its defining behavior for interrupted hosts. cost=$0.30
- 2026-09-10T11:01:22+00:00 dispatched revise run 20260910T110117Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base garden/cg-347-recover-ec2-spot-interruptions-without-losing-ac, ~13841 tokens)
- 2026-09-10T11:03:32+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:04:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/418: Emergency stop now uses a dedicated force-retirement lifecycle path, including for interrupted Spot hosts with a pending drain callback. Verified current commit d5094d89 with 41 focused host lifecycle/scale tests and Ruff. cost=$0.42
- 2026-09-10T11:07:22+00:00 automated review requested changes: Emergency stop now force-retires interrupted hosts correctly, and drain/orphan reconciliation tests pass. However, the status model change breaks the existing scale CLI test. cost=$0.37
- 2026-09-10T11:07:38+00:00 dispatched revise run 20260910T110733Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base garden/cg-347-recover-ec2-spot-interruptions-without-losing-ac, ~14305 tokens)
- 2026-09-10T11:09:55+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:11:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/418: Restored backward compatibility for positional ScaleStatus consumers while preserving the new lifecycle phase output. Verified commit 0080207051213d89e59a429a543f2a28ab4ce1d7 with 44 focused host lifecycle/CLI tests and Ruff. cost=$0.22
- 2026-09-10T11:13:32+00:00 automated review: approve — Safe draining, durable restart-visible status, explicit emergency teardown, and owned-resource reconciliation are implemented coherently; the positional ScaleStatus compatibility regression is fixed. cost=$0.30
- 2026-09-10T13:50:04+00:00 stack parent CG-347 merging; retargeted this PR to main before the parent branch is deleted
- 2026-09-10T13:51:30+00:00 parent CG-347 merged; rebased onto main and retargeted the PR
- 2026-09-10T14:07:46+00:00 automated review: approve — Safe draining, restart-visible lifecycle state, explicit emergency teardown, and owned-resource reconciliation remain correct after the rebase. cost=$0.43
- 2026-09-10T14:09:11+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/418
