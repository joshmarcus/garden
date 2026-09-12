---
id: CG-346
title: Run work reviews and checks on managed EC2 hosts with shared resource admission
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-216
- CG-338
- CG-345
priority: 0
order: 2
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
branch: codex/cg346-managed-worker-canary
pr: https://github.com/joshmarcus/context-garden/pull/300
last_dispatched_at: '2026-09-08T03:27:47+00:00'
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-08T03:48:08+00:00'
---

## Goal and evidence

Integrate the managed pool lifecycle with the portable worker protocol, using the lifecycle task as a dependency. All execution modes, including setup and base probes, share measured host admission; use disk-backed temp by default and preserve a memory reserve. Deliver durable transcripts, changes and results without scheduler filesystem assumptions.

Evidence should complete a work/review/check cycle on an independent host, demonstrate that a one-slot pool does not start overlapping unchecked suites, and recover artifacts after instance loss. Show actual host/version/resource attribution and no exposed controller credentials.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Garden is a consumer adapter of the shared host lifecycle. Keep task admission, CG-216 enrollment and results within that adapter; generic provisioning must function without garden scheduling or model credentials. Implement the garden-worker environment profile through the documented profile contract. Do not hard-code worker-only semantics into EC2 host lifecycle or credentials.

## Log

- 2026-09-07T12:47:31+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:31+00:00 approved (owner-phase05-promotion)
- 2026-09-07T16:04:36+00:00 priority 2 -> 1 (web)
- 2026-09-07T16:04:46+00:00 priority 1 -> 0 (web)


## Integrated canary ownership, owner-directed PR resolution

This task owns the real one-host/30-minute/$2 worker canary previously also demanded by prerequisite CG-345. After the lifecycle and protocol merge, prepare the pinned worker image/bootstrap, verify actual authenticated enrollment/work/check/review and recovery, terminate the instance and inventory retained billed resources with elapsed time/cost. CG-345 merging is not proof of live readiness. Preserve the aggregate $80 allocation and independent termination deadline.
- 2026-09-07T21:55:32+00:00 Owner requested direct operator implementation and live canary; reserved from scheduled dispatch during this pass.
- 2026-09-07T22:38:23+00:00 Operator direct canary completed on EC2 i-0f14bee6ae2b3355b: real work/check/review, unprivileged/IMDS/disk/host-lock checks, preserved stream after termination and stale-lease rejection. Instance terminated; owned volumes/ENIs zero. PR300 contains source/evidence and explicit model/fresh-image limitations. Reservation released for normal automated review; production build unchanged.
- 2026-09-07T22:38:23+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/300 (pr_number none -> 300)
- 2026-09-07T22:51:18+00:00 Final f1ab705 PR CI34167292449 passed; branch CI34167289320 failed only test_qa::test_a_broken_flow_names_the_step_and_exits_non_zero (1532 passed). Requested one failed-job rerun to distinguish intermittent QA timing from regression; do not waive CI or claim both green. No implementation rerun needed from this observation.
- 2026-09-08T02:52:41+00:00 automated review requested changes: Managed workers omit configured product setup, so all required execution stages do not share host admission. The reviewed-head interaction replay also misses the affected remote-worker API journey. cost=$0.32
- 2026-09-08T03:27:47+00:00 dispatched revise run 20260908T032745Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~14394 tokens)
- 2026-09-08T03:48:08+00:00 Owner fast-forward direct repair/self-review: PR300 merged21e64a3c after exact ad1ca77c full CI passed twice and39focused tests plus real HTTP setup/lease evidence. Production rollout remains separate and pending.
