---
id: CG-444
title: Support configured SSH ports in canonical enterprise repository identity
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-395
- CG-432
- CG-447
priority: 1
difficulty: medium
reading:
- src/garden/github.py
- src/garden/config.py
- src/garden/onboard.py
- tests/test_remote_worker.py
branch: garden/cg-444-support-configured-ssh-ports-in-canonical-enterp
pr: https://github.com/joshmarcus/context-garden/pull/347
runner: remote
discovered_from: CG-428
attempts: 1
last_dispatched_at: '2026-09-09T01:13:52+00:00'
created: '2026-09-08T17:49:22+00:00'
updated: '2026-09-09T01:45:25+00:00'
file: src/garden/onboard.py
error: '`_add_github_metadata` regex does not match ssh.github.com remotes containing port 443, so the
  onboarding report lacks `GitHub repository metadata`.'
---

Update onboarding GitHub repository discovery to recognize remotes such as `ssh://git@ssh.github.com:443/owner/repo.git`. The AWS worker checkout uses this valid form, causing repository metadata to be silently omitted and `test_onboard_this_repository_uses_documented_setup_and_ci_tests` to fail.

## Provenance

Discovered by CG-428 (Keep remote worker runs alive across controller redeploys) during run `20260908T172731Z-revise`.
## Log
- 2026-09-08T17:49:22+00:00 discovered by CG-428


## Operator scope reconciliation

The original public ssh.github.com:443 onboarding observation is already owned by active CG432. Retain this follow-up for the distinct merged-CG395 shared parser defect: repo_slug_from_remote at669f519a only accepts SSH port22, although remote claims preserve valid443. Sol exact-source calls returnedNone for ssh://acct-1234@forge-one.test:443/Team/Repo.git and port2222. Recheck merged CG432/447 first and reuse their classifier; do not duplicate those implementations.

## Acceptance criteria

- [ ] Valid configured enterprise SSH URLs with numeric ports443/custom2222 retain the correct repository and API-host identity; public official alias normalization remains correct.
- [ ] Reject invalid/out-of-range ports, malformed URLs and password-bearing references without cross-host requests.
- [ ] Focused synthetic two-host tests cover valid ports, refusal and config/onboarding/claim agreement; if dependencies already fix this, report exact-source evidence without redundant code.
- 2026-09-08T19:24:45+00:00 approved (owner-delegated-hourly-audit)
- 2026-09-08T21:56:38+00:00 dispatched work run 20260908T215638Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~12749 tokens)
- 2026-09-08T22:03:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/347 (base main): Configured enterprise SSH remotes now accept valid numeric ports while preserving host-scoped repository identity, and onboarding reuses the canonical parser including GitHub's official SSH alias. Invalid, out-of-range, oversized, malformed, and password-bearing references are rejected. cost=$0.72
- 2026-09-09T01:02:46+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_onboard.py); a rebase agent will resolve it
- 2026-09-09T01:02:56+00:00 dispatched rebase run 20260909T010256Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1051 tokens)
- 2026-09-09T01:08:11+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit a4b27c72a7ef, not because of this branch; waiting for the base to go green, no revise round cost=$0.01
- 2026-09-09T01:13:09+00:00 pre-PR checks failed (lint) (still failing after a rebase onto `main`); revise run will fix before the PR is updated
- 2026-09-09T01:13:52+00:00 dispatched revise run 20260909T011350Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14799 tokens)
- 2026-09-09T01:24:53+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/347: Configured SSH port support remains intact, lint duplication is removed, and the public ssh.github.com:443 alias is restricted to github.com identity. cost=$0.56
- 2026-09-09T01:35:16+00:00 automated review: approve — Configured enterprise SSH ports are validated and retain host-scoped repository identity, while invalid, credentialed, cross-host, and misclassified public-alias routes are refused. Focused tests and lint pass at the reviewed head. cost=$0.51
- 2026-09-09T01:35:47+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T01:36:58+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T01:41:28+00:00 automated review: approve — Configured enterprise SSH ports are safely accepted while preserving host-scoped identity; malformed, credentialed, cross-host, and invalid-port remotes remain rejected. Focused tests and lint pass at the reviewed head. cost=$0.28
- 2026-09-09T01:43:33+00:00 rebasing before merge; reviewed remote head already contains main; not rebased or pushed
- 2026-09-09T01:45:25+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/347
