---
id: CG-439
title: Declare controller ownership for pre-PR UI capture checks
status: cancelled
product: context-garden
phase: phase-05
depends_on:
- id: CG-431
  after: merge
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/reap.py
- src/garden/walkthrough.py
- src/garden/runner/remote.py
- tests/test_review.py
- tests/test_runners.py
branch: garden/cg-439-declare-controller-ownership-for-pre-pr-ui-captu
pr: https://github.com/joshmarcus/context-garden/pull/328
runner: remote
discovered_from: CG-427
attempts: 1
last_dispatched_at: '2026-09-08T17:05:44+00:00'
created: '2026-09-08T16:19:23+00:00'
updated: '2026-09-08T18:25:57+00:00'
---

## Goal

Apply CG431's explicit check-backend mechanism to the pre-PR UI check payloads that actually require controller worktrees and output paths, preventing renderer revision loops caused by path ownership errors.

## Evidence

CG427 checks20260908T154033Z and154635Z passed lint then errored with PermissionError for /home/joshua/work/worktrees/CG-427/src on AWS. The completed renderer/captures were revalidated repeatedly. Temporary local task routing allowed capture and actual review; review161046 then found a real duplicate-command rendering defect. Preserve that useful distinction.

CG431/PR320 head870338025e215687860abaca990757764f73ed7d implements _check_execution with stage interaction_replay or spec.execution_owner=controller. An exact git grep finds execution_owner only in that resolver: no UI producer declares it. Thus merging/deploying CG431 alone does not cover this pre-PR payload.

## Acceptance criteria

- [ ] Reuse the merged CG431 resolver/metadata. Mark controller-dependent UI capture specs at their producer, or provide a demonstrably portable path/output mapping with equivalent artifact return; select backend before execution. Do not duplicate the routing state machine or permanently change the author's runner.
- [ ] A remote-authored renderer change gets real pre-PR UI captures at controller-readable durable paths under normal local admission, then enters review. Existing portable lint/ordinary-suite checks remain remotely eligible where separable, with truthful backend/source provenance.
- [ ] Retry, collection and restart retain input/output ownership and current source identity. An inaccessible infrastructure path cannot claim a passing capture or trigger repeated unchanged renderer implementation. Preserve real failed behavior and genuine missing-outcome gates.
- [ ] Add focused tests for the actual generated pre-PR UI payload, mixed portable/controller checks, retry under full local capacity, and durable PNG/receipt collection; demonstrate the bounded CG427-shaped capture journey. Coordinate CG436 semantic replay coverage independently.

No production restart/deployment, permission widening, credential copying or stress workload is authorized by this ticket.

## Log

- 2026-09-08T16:19:23+00:00 approved (owner-delegated-inbox-routing-followup)
- 2026-09-08T17:05:44+00:00 dispatched work run 20260908T170544Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~12294 tokens)
- 2026-09-08T17:28:57+00:00 opened https://github.com/joshmarcus/context-garden/pull/328 (base main): Generated pre-PR UI capture payloads now declare controller ownership before routing, keeping their controller worktree and durable run output paths local while portable checks remain unchanged. Focused scheduler/review tests and lint pass on commit b39fbf9456638a9f5f073be9f6c6b4f632427db7. cost=$0.81
- 2026-09-08T17:40:50+00:00 automated review produced no verdict (idle 21 min (no output or file change))
- 2026-09-08T18:25:57+00:00 cancelled (web)
