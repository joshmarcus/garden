---
id: CG-345
title: Provision and retire an EC2 worker pool from a bounded declarative configuration
status: waiting_human
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 3
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
branch: garden/cg-345-provision-and-retire-an-ec2-worker-pool-from-a-b
attempts: 1
last_dispatched_at: '2026-09-07T17:33:14+00:00'
created: '2026-09-06T16:27:49+00:00'
updated: '2026-09-07T18:42:10+00:00'
---

## Goal and evidence

Implement the on-demand lifecycle and bootstrap portion of specs/ec2-workers.md. Provide a plan/enable boundary, idempotent reconciliation with ownership tags, scoped credential delivery, reachable HTTPS enrollment, pinned versions and explicit failure states. Default to zero idle instances and a one-instance maximum.

Evidence should cover duplicate provisioning requests, delayed AWS responses, controller restart, bootstrap failure and cleanup without touching unrelated resources. A separately enabled bounded AWS canary must register a real worker and retire it with an inventory of any retained billed resources. Fake-provider tests alone do not establish live readiness.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Implement an independently usable host lifecycle with versioned provider and environment-profile contracts. EC2 is an adapter, not the core data model. Expose plan/provision/reconcile/inspect/stop/start/destroy capabilities and lifecycle events without garden task IDs or scheduler imports. Support injected workplace policy/credential resolution and validated namespaced provider options. Supply a fake provider and a minimal extension example proving a second provider can be added without modifying core or garden scheduling. The same lifecycle must support both disposable worker hosts and persistent development hosts; do not assume every termination deletes workspace storage.

## Log

- 2026-09-07T12:47:30+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:31+00:00 approved (owner-phase05-promotion)
- 2026-09-07T16:06:56+00:00 priority 2 -> 0 (web)
- 2026-09-07T17:33:14+00:00 dispatched work run 20260907T173312Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~12929 tokens)
- 2026-09-07T18:04:38+00:00 preserved uncommitted worktree changes from run 20260907T173312Z-work outside the PR: `git stash apply b8b7dc8253b0a8f0fde0c79e6fc0389ef6ec92d3` in /home/joshua/work/worktrees/CG-345 (garden:CG-345:20260907T173312Z-work:reap)
- 2026-09-07T18:04:38+00:00 worker asks: Please provide or enable the bounded AWS canary configuration—account/region, pinned AMI, private subnet, egress-only security group, scoped instance-profile and enrollment-secret ARNs, reachable HTTPS enrollment endpoint, instance type/hourly estimate, runtime budget, and GARDEN_EC2_CANARY=1—so I can provision exactly one worker, verify registration, retire it, and inventory retained billed resources. cost=$2.42


## Operator setup findings and concrete canary plan (2026-09-07)
Owner has requested the AWS setup actions. Configuration is prepared in context-garden/docs/aws-setup (operator garden, not a worker edit target): disabled one t3.xlarge in us-east-1, Canonical Ubuntu24.04 ami-025d99823a4caad37 (root /dev/sda1),40GiB encrypted gp3, standard CPU credits,30minute runtime, proposed$2 admission bound. Endpoint remains tailnet-only https://babel.taild4d2ae.ts.net. No real launch is enabled; tagged subnet/SG, worker role/profile, scoped tailnet enrollment and exact worker build are prerequisites. Owner is being asked for a non-root infrastructure admin profile; garden-provisioner works but cannot create IAM/network resources. Never fall back to root/default or ask for operator credentials in the worker brief.

Source audit of afadab3 found additional launch blockers that must be repaired and reviewed before the canary:
- Provisioner IAM requires ManagedBy=context-garden and Pool=phase05 request tags on instances, volumes and network interfaces. EC2Provider currently writes only context-garden:* tags on the instance. Preserve generic namespaced ownership tags; support injected policy-required tags without allowing reserved ownership spoofing, tag all created required resource types and test the exact generated launch request against the scoped policy requirements. Do not broaden IAM to bypass this mismatch.
- Bootstrap currently executes aws and curl without installing prerequisites, calls nonexistent /api/workers/enroll, and does not install or run the worker. CG216 exposes configured bearer-token claim/heartbeat/finish and CLI garden worker --garden URL --host NAME --token-env GARDEN_WORKER_TOKEN --work-dir DIR. Implement a real pinned/prebuilt environment contract or a tested bootstrap for that contract; actually start the worker as a supervised unprivileged process with disk temp. No moving package versions, hardcoded operator credentials, or fake enrollment readiness. Tailnet enrollment must be scoped and secret values must not appear in userdata/logs.
- t3 standard credits must be expressible to avoid unlimited-credit surprise spend. Root volume and actual post-termination volumes/ENIs/IPs must be discovered and inventoried, not returned as invented attached-storage identifiers. Cleanup completion must be observed, not assumed after a terminate request.
- Isolate task execution from IMDS, bootstrap enrollment material, and controller/provisioner credentials. First live canary uses an independently scoped disposable repository/fake harness; do not copy model credentials or production repo write credentials.
Preserve completed generic lifecycle implementation and tests; these are concrete integration repairs within the original usable EC2 worker outcome. Keep live readiness explicitly unproven until infrastructure/endpoint are ready. The operator will supply real resource identifiers and secret references securely, not fabricate them.
- 2026-09-07T18:42:10+00:00 Owner requested AWS setup; operator prepared disabled infrastructure/canary artifacts and identified concrete IAM-tag/bootstrap integration blockers. Non-root admin profile requested; no instances launched.
