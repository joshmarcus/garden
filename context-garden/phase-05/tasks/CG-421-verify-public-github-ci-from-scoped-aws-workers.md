---
id: CG-421
title: Verify public GitHub CI from scoped AWS workers without operator credentials
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-05/tasks/CG-363-run-full-worker-tests-on-github-ci-before-comple.md
branch: garden/cg-421-verify-public-github-ci-from-scoped-aws-workers
pr: https://github.com/joshmarcus/context-garden/pull/303
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T10:50:02+00:00'
created: '2026-09-08T09:17:46+00:00'
updated: '2026-09-08T11:33:40+00:00'
---

## Goal

Let the scoped AWS worker perform this public repository's required exact-commit CI check without copying the operator's GitHub credentials or weakening CI acceptance.

## Context

The real production host has no gh executable, intentionally uses a dedicated repository SSH deploy key, and rewrites the push origin to ssh://git@ssh.github.com:443/joshmarcus/context-garden.git. The required scripts/check_ci.py currently depends on authenticated gh and derives the API host directly from that SSH alias. Normal development jobs would therefore fail their required check even though Git transport, model tools and focused tests work. At09:17UTC the host successfully read public Actions run34207829975 for exact release SHA c8c661e8 through GitHub's unauthenticated REST API (HTTP200, remaining59); no new credential is required for public CI metadata. CG363's exact branch/head/latest-run/clean-checkout/remote-tip gates must remain intact.

## Acceptance criteria

- [ ] Support a documented bounded public-REST path for the required CI script when authenticated gh is unavailable, preserving existing authenticated and enterprise behavior.
- [ ] Normalize the official ssh.github.com:443 transport to the github.com API identity without accepting unrelated hosts or credential-bearing destinations.
- [ ] Preserve assigned-branch push restrictions, exact head/branch/push-event/workflow/latest-attempt checks, dirty-checkout and moved-remote rejection. API errors, rate limits, malformed results, missing or pending runs cannot pass.
- [ ] Use measured conservative polling for unauthenticated API limits; do not copy operator tokens or broaden the repository deploy key.
- [ ] Focused meaningful tests, actual AWS invocation against an exact current commit, full exact-head CI and operator self-review pass before merge. Then verify an ordinary useful AWS development run with durable results before routing general work to that host.

## Out of scope

Additional AWS hosts, expanded IAM or GitHub credentials, removal of CI gates, and claims that phase stabilization or a final clean-image bootstrap replay has passed.

## Provenance

Direct operator follow-up to CG419/CG420 production rollout; prepared as manual work while normal scheduling continues at worker/shared2/2. Official public metadata behavior: https://docs.github.com/en/rest/actions/workflow-runs#list-workflow-runs-for-a-repository .

## Log

- 2026-09-08T10:46:29+00:00 approved (web)

## Owner-directed AWS execution

The owner requested four AWS workers and asked for an actual task on the existing host. Run this task there as a normal development job. The missing gh command and SSH transport alias are the exact failure this task repairs; implement the correction in the assigned repository, then run the corrected required CI check against your exact committed branch. A bounded read-only public Actions query may bootstrap diagnosis, but missing, stale or pending CI never counts as passing. Do not access operator credentials, change the controller, widen permissions or launch another host. Preserve existing authenticated/enterprise and branch/publication safety behavior.
- 2026-09-08T10:50:02+00:00 dispatched work run 20260908T105002Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~11647 tokens)
- 2026-09-08T11:15:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/303 (base main): Added a bounded unauthenticated public GitHub Actions REST fallback for scoped deploy-key workers, including ssh.github.com:443 normalization and strict CI safety checks. The final exact-head GitHub CI run passed from this AWS worker. cost=$1.00
- 2026-09-08T11:22:53+00:00 automated review: approve — The bounded public REST fallback is documented, tested, and limited to canonical public GitHub repositories while preserving authenticated enterprise behavior and exact-commit safety gates. Focused tests, lint, and the reported exact-head GitHub Actions run all pass. cost=$0.28
- 2026-09-08T11:23:51+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T11:24:53+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-08T11:33:40+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/303
