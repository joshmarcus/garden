---
id: CG-340
title: Demonstrate onboarding and a useful accepted change on an independent project
status: changes_requested
product: context-garden
phase: phase-05
depends_on:
- CG-215
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
branch: garden/cg-340-demonstrate-onboarding-and-a-useful-accepted-cha
pr: https://github.com/joshmarcus/context-garden/pull/246
attempts: 1
last_dispatched_at: '2026-09-06T23:25:37+00:00'
created: '2026-09-06T13:46:35+00:00'
updated: '2026-09-06T23:44:24+00:00'
---

## Goal

Demonstrate onboarding and a useful accepted change on an independent project

## Context

Onboarding CG-215 is the entry point. Execute the independent-project journey in specs/stabilization.md. Use a non-Python disposable fixture for repeatability; explicitly distinguish that from a real existing repository and maintainer acceptance. If the real target is unavailable, return the specific missing decision and preserve fixture evidence rather than claiming adoption.

## Acceptance criteria

- [ ] Evidence shows project setup, a grounded plan, useful implementation, review and final behavior. No fabricated provenance or hand-edited generated configuration. State PASS/FAIL/UNPROVEN separately for repeatable compatibility and real-user adoption.
- [ ] The report cites commands, observed results and artifact paths, distinguishes automated checks from real interaction, and states all unverified requirements.

## Log

- 2026-09-06T13:46:35+00:00 approved (cli)


## Owner-authorized concurrency trial, 2026-09-06

The owner raised the worker/shared local-run limit to four after GitHub CI offload. This task is selected alongside CG354 focused-test cleanup, CG361 resource isolation and CG341 mechanical stabilization recording. Own the isolated non-Python onboarding/journey fixture and honest adoption evidence, keeping implementation independent of those tasks. Use disposable assets inside the assigned worktree; do not onboard or push changes to an unrelated real repository without an identified authorized target. No real external maintainer/project has been supplied in this brief: complete all useful repeatable fixture validation and identify the exact missing real-adoption evidence as UNPROVEN rather than inventing it or claiming full adoption. Keep any needed shared-core changes narrow. Do not rewrite resource/runner enforcement, shared Git fixtures or phase-close/soak mechanisms owned by the other tasks. Full suites use the configured GitHub CI helper on the exact committed head; local checks and fixture services remain bounded and serial. Do not change production services/configuration or start extra model agents.
- 2026-09-06T23:25:37+00:00 dispatched work run 20260906T232518Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10298 tokens)
- 2026-09-06T23:36:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/246 (base main): Added a repeatable, non-Python onboarding journey that demonstrates grounded planning, scheduler approval, useful implementation, scripted fixture review, merge, and final behavior. Compatibility passes; real-user adoption remains explicitly UNPROVEN because no authorized existing project or maintainer was supplied. cost=$1.16
- 2026-09-06T23:37:21+00:00 automated review requested changes: The repeatable fixture journey meets both acceptance criteria and 19 focused tests pass. The PR cannot merge with the unrelated 68k-line generated snapshot rewrite, scar-tissue commit, and CI evidence tied to the previous commit rather than HEAD. cost=$0.22


## Operator mechanical snapshot cleanup, 2026-09-06 23:43 UTC

With no active task run and a clean worktree, preserved scheduler-added snapshot6dc8fb0 as /home/joshua/work/operator-test-tmp/snapshot-salvage-20260906T2343Z/CG-340-6dc8fb0-snapshot.json with SHA256/recovery metadata. Restored only that file from base58e13b99 and pushed cleanup0484952b76a9fa0144ed08868e944dfa8d27b4eb without rewriting history. Verified the complete resulting Git tree equals the intended worker tree7df508f2f1706b6a2511389c74d5553f0e1b0fd3. New-head CI is pending; PR description records that accurately. No local full suite or extra model revision was used. Re-review only after new-head CI and updated evidence; do not redispatch a worker merely to remove the now-cleaned snapshot. Real-project adoption remains UNPROVEN.
