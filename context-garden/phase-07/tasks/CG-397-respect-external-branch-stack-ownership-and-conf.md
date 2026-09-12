---
id: CG-397
title: Respect external branch-stack ownership and configurable protected paths
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-397-respect-external-branch-stack-ownership-and-conf
pr: https://github.com/joshmarcus/context-garden/pull/308
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T14:29:35+00:00'
created: '2026-09-07T19:56:15+00:00'
updated: '2026-09-08T17:32:04+00:00'
---

## Goal

Make external stack ownership explicit per product and prevent competing history writers. Reuse existing stacking configuration where sufficient.

## Acceptance criteria

- [ ] With externally managed stacks, garden does not automatically restack, retarget or force-push dependency branches; unsupported combinations fail validation.
- [ ] Add product protected-path patterns to existing sensitive-path defaults without weakening them; affected changes remain human-gated.
- [ ] Document ownership and recovery when another tool changes a head; test stale-head handling and an empty-diff branch without claiming its content shipped.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G6. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T12:02:32+00:00 Owner four-host rollout verified; route this eligible Phase07 P0 task to the authenticated AWS pool while retaining two local resource slots.
- 2026-09-08T12:03:26+00:00 dispatched work run 20260908T120326Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~8319 tokens)
- 2026-09-08T12:24:01+00:00 opened https://github.com/joshmarcus/context-garden/pull/308 (base main): Added explicit per-product external stack ownership, additive protected paths, recovery guidance, and regression coverage. Exact-head GitHub CI passed for commit 55f193b78e5f91c1c9e16b961291a8ad839b2469. cost=$1.53
- 2026-09-08T12:51:06+00:00 check did not run (20260908T125038Z-check): idle 28 min (no output or file change); will retry
- 2026-09-08T13:55:58+00:00 automated review requested changes: External ownership is bypassed when a garden-owned parent has an externally owned stacked child, allowing garden to retarget that child’s PR. Focused tests and lint pass, but the required saved interaction replay is inaccessible from this reviewer environment. cost=$0.25
- 2026-09-08T14:29:35+00:00 dispatched revise run 20260908T142935Z-revise-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~10118 tokens)


## Operator approved-policy recovery, 2026-09-08T1529

The operator preserved this worker checkout and applied only already-approved CG426 stress opt-in hunks because this old/stacked branch predated them. Retain the policy in the final source and verify the ordinary selection. Preservation receipts are under /var/lib/garden-worker/operator-preservation/CG-397-stress-policy-20260908T1527 on its worker host. The running plain pytest PID191097 was intentionally interrupted with SIGINT; this was a policy intervention, not a code failure. The model and daemon were preserved. The current-policy propagation repair is CG-434.
- 2026-09-08T15:42:13+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/308: Protected externally owned stacked child PRs from garden retargeting and parent-branch deletion, with a mixed-ownership regression test. Existing ownership, protected-path, stale-head, empty-diff, and recovery coverage remains green. cost=$1.81
- 2026-09-08T15:57:24+00:00 stalled: review finding repeated after a revise round: running-app evidence incomplete: affected interaction is missing or failed; empt; run `garden triage CG-397 --changes "<feedback>" to unblock`


## Delegated Inbox decision, 2026-09-08T16:15:35.229474+00:00

Owner delegated this input. Decision: investigate the verification handoff under CG436 before authorizing more implementation retries; retain current branch, PR, current-head tests, report and actual unresolved outcome checks. This is now an operator-owned investigation, not a request for Josh to reset the cap or guess whether to merge. Installed rc5 cannot yet render a dedicated investigation card (CG437); keep the protective stop until evidence or its protocol repair is concrete.
- 2026-09-08T17:32:04+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/308
