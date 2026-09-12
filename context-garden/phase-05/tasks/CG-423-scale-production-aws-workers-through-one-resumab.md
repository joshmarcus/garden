---
id: CG-423
title: Scale production AWS workers through one resumable operation
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-420
- CG-421
priority: 1
difficulty: hard
reading:
- docs/worker-protocol.md
- src/garden/managed_worker.py
- src/garden/hosts/ec2.py
- scripts/managed-worker-bootstrap
- context-garden/phase-06/specs/ec2-workers.md
branch: garden/cg-423-scale-production-aws-workers-through-one-resumab
pr: https://github.com/joshmarcus/context-garden/pull/333
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T00:03:55+00:00'
created: '2026-09-08T11:15:49+00:00'
updated: '2026-09-10T03:42:05+00:00'
---

## Owner validation policy, 2026-09-10

Live canaries are optional and cannot be required for task acceptance, review, merge, release or phase closure. Proportionate deterministic tests, provider fakes, protocol integration and disposable offline bootstrap/lifecycle exercises establish the required behavior. Report live-cloud coverage as untested when absent; that absence alone is not a blocker. Preserve genuine correctness, security, recovery, deadline and resource requirements. Any optional live exercise still requires its own applicable resource/spending authorization. This supersedes older live-canary or paid clean-image rollout requirements, including historical operator dispositions below.

# Goal
Scale a production AWS worker pool through one resumable product operation instead of requiring bespoke operator scripts and repeated browser setup.

## Context
Owner requested this on 2026-09-08 after the one-to-four host expansion required manual dedicated Codex device logins, single-use tailnet enrollment, per-host repository keys and controller tokens, bootstrap-secret setup, release/CI/budget verification, EC2 launch plans, controller registration, independent deadlines and cleanup receipts. Build on CG345/346/419/420 and CG421; CG347 retains Spot interruption recovery and CG348 retains broader pool visibility.

The live operation evidence is in docs/aws-setup and the operator four-worker rollout record. Do not copy private enrollment material into a brief, PR or result. This task automates the supported lifecycle, not authentication by impersonating an owner or copying a shared refresh session to concurrent hosts.

## Acceptance criteria
- [ ] A single CLI or app scale request shows the desired total, existing healthy/pending hosts, exact version, cost/deadline limits and only the missing setup steps; continuing or retrying it resumes durable progress without duplicate hosts, credentials or charges.
- [ ] Normal scale-up uses scoped provisioning and separate per-host model/repository/tailnet/controller enrollment; initial administrator or interactive account setup is requested only when actually missing or expired, with clear owner handoff and no operator/root credentials installed on workers.
- [ ] A new host is reported ready only after pinned bootstrap, authenticated registration, scoped repository/CI access and real task execution with durable result return succeed. Partial failures preserve useful work and support bounded retry, drain or cleanup through the same operation.
- [ ] Aggregate budget admission, pool/local resource limits and independent absolute per-host termination deadlines survive controller/app restarts; teardown verifies instances, disks/network resources and ephemeral credentials, while retained resources and delayed costs remain visible.
- [ ] Focused lifecycle tests cover interrupted setup/resume, expired enrollment, duplicate requests, bootstrap failure, partial pool success and cleanup. Verify the supported bootstrap, enrollment, protocol and deadline journey through executable deterministic tests and disposable offline environments. A live clean-image cloud rollout is optional and is not an acceptance or merge requirement; report absent live coverage as untested.

## Scope
Respect the existing $80 aggregate trial allocation and current phase holds. No standing permission to expand administrative privileges or launch an unbounded fleet. Keep auth secret values out of source and evidence. Reuse the existing provider/lifecycle abstractions; avoid introducing another independent orchestration system.

## Log

- 2026-09-08T11:17:17+00:00 Owner requested automating the manual four-host production enrollment and launch process; complements CG347/348 rather than duplicating them.

## Authentication follow-up
Owner asked for authentication that avoids login for each new instance. Prefer supported unattended machine identities: scoped AWS temporary credentials (for example Roles Anywhere for a controller outside AWS), a tag-limited Tailscale OAuth client, and renewable repository installation credentials. Existing Codex account sessions refresh automatically; assess durable per-runner sessions and supported noninteractive API-key or eligible Enterprise access-token/workload-identity options. Make account eligibility and separate API billing explicit before changing model authentication or spending outside the authorized allocation.

Primary references: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html ; https://tailscale.com/docs/features/oauth-clients ; https://learn.chatgpt.com/docs/auth ; https://learn.chatgpt.com/docs/auth/ci-cd-auth .
- 2026-09-08T11:25:47+00:00 Owner requested considering a different authentication mechanism that does not require repeated login; include supported unattended identity options and explicit billing implications.


## Confirmed deployment requirements

The six-host rollout exposed required test prerequisites: gh, make, Chromium system libraries and cache, modern bundled pip for nested venvs, and host-owned browser environment transport. Include them in repeatable bootstrap and a full ordinary-suite readiness check. Preserve the absolute trial deadline and single-use enrollment cleanup; do not provision additional hosts merely to validate this implementation. Evidence: /home/joshua/work/operator-test-tmp/aws-six-workers-20260908.
- 2026-09-08T14:15:01+00:00 approved (owner-handle-all-human-input)
- 2026-09-08T17:54:10+00:00 dispatched work run 20260908T175410Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23291 tokens)


## Owner deployment checkpoint 2026-09-08T18:43:07.597309+00:00

Owner-requested deployment interruption after shared test hangs; exact source and streamed outputs checkpointed at /home/joshua/work/operator-test-tmp/rc6-deploy-20260908T1818/checkpoint-CG-423
Source 66244c4f3e807afe669ab3296e40dc63f7ec4035 is preserved in source.bundle; this interruption is not a code-failure verdict. Resume this implementation with focused tests and bounded validation; do not repeat unchanged full-suite failures.
- 2026-09-08T18:43:07+00:00 Operator-owned deployment recovery; preserved implementation, no author failure verdict.
- 2026-09-08T18:44:00+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-423`) or send it back (`garden triage CG-423 --changes "..."`)
- 2026-09-08T19:09:00+00:00 dispatched revise run 20260908T190859Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25115 tokens)
- 2026-09-08T19:16:18+00:00 opened https://github.com/joshmarcus/context-garden/pull/333 (base main): Added regression coverage ensuring the resumable AWS scaling operation's production bootstrap includes the clean-image test prerequisites and durable browser environment. The preserved implementation and focused lifecycle coverage pass at exact head. cost=$0.52
- 2026-09-08T21:34:31+00:00 Delegated Input sweep retired the proven never-started remote request and queued one local review in its original logical round.
- 2026-09-08T21:39:19+00:00 automated review requested changes: The 28 focused tests and scoped lint pass, but the durable operation does not constrain continuation to its admitted request, the production browser cache is installed with unusable ownership, and the required production enrollment/readiness/clean-image journey remains materially unverified. cost=$0.48
- 2026-09-08T23:34:34+00:00 dispatched revise run 20260908T233432Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~26598 tokens)
- 2026-09-08T23:47:15+00:00 preserved uncommitted worktree changes from run 20260908T233432Z-revise outside the PR: `git stash apply 5bb4cde9cfd486af2f709efe5caa2ebd73dd5bcf` in /home/joshua/work/worktrees/CG-423 (garden:CG-423:20260908T233432Z-revise:reap)
- 2026-09-08T23:47:15+00:00 worker asks: May the operator authorize one bounded clean-image AWS rollout within the existing $80 allocation to validate commit 6279dfc6d29057fefa8c50469f236408c676643b, or should the prior six-host rollout plus current-head executable bootstrap tests be accepted as equivalent evidence? cost=$1.69
- 2026-09-09T00:03:36+00:00 RC8 controller routing repairs verified; restored original remote runner for future work/checks/reviews without restarting existing work.

## Operator-owned rollout investigation 2026-09-09T00:03:54.509001+00:00

Delegated operator answer: Do not launch another EC2 host. The current six-host allocation, existing absolute deadlines and $80 aggregate limit remain. The earlier rollout predates the final admission, enrollment/readiness and Chromium ownership changes, so it is supporting history rather than current-source proof. Preserve the completed6279dfc6 implementation,57focusedtests and lint; the operator will publish/review this exact source and owns the remaining bounded current-source bootstrap/rollout investigation using the existing allocation. Do not weaken READY/attestation/durable-result gates, claim criterion5 passed from string assertions, or restart completed implementation. No additional owner decision is needed for this investigation; any actual fresh-host authorization remains outside this answer.
- 2026-09-09T00:03:55+00:00 dispatched revise run 20260909T000355Z-revise via manual [human] (fresh session, base main, ~25920 tokens)


## Renewed-fleet credential provenance 2026-09-10

The renewed six-host operation supplied current operational evidence without changing this task's source identity or claiming PR333 deployed. Durable Tailscale OAuth credentials live privately under `/home/joshua/.config/context-garden/provisioning`; the installed mint helper and runbook live under `/home/joshua/.local/lib/context-garden`. AWS uses the separately reviewed scoped durable provisioning identity. Final secret values are absent from all task evidence.

Receipts: `/home/joshua/work/operator-test-tmp/aws-renew-20260909/aws-renew-final.json`, `/home/joshua/work/operator-test-tmp/aws-renew-20260909/tailscale-oauth-created.json`, `/home/joshua/work/operator-test-tmp/aws-renew-20260909/tailscale-temporary-api-token-retired.json`, `/home/joshua/.local/lib/context-garden/tailscale-oauth-install.json`, and `/home/joshua/.local/lib/context-garden/tailscale-oauth-runbook.md`. These are supporting operational evidence only. The previously observed PR333 head 6279dfc6 was not the deployed RC16 bootstrap or orchestration implementation and still requires preserved-source integration and review. The exact manual reservation `20260909T000355Z-revise` remains active and preserved.
- 2026-09-10T00:15:01+00:00 attached secret-free renewed-fleet credential and readiness provenance; manual reservation, PR/source identity and active history preserved; no deployed-feature claim
- 2026-09-10T03:42:05+00:00 external PR merged and verified on main
