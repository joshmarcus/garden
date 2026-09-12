---
id: CG-509
title: Avoid duplicate same-SHA GitHub test jobs
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- .github/workflows/ci.yml
- scripts/check_ci.py
- tests/test_github_fakes.py
branch: garden/cg-509-avoid-duplicate-same-sha-github-test-jobs
pr: https://github.com/joshmarcus/context-garden/pull/431
runner: remote
discovered_from: CG-502
attempts: 1
last_dispatched_at: '2026-09-10T12:52:06+00:00'
created: '2026-09-10T10:58:32+00:00'
updated: '2026-09-10T13:41:52+00:00'
file: .github/workflows/ci.yml
error: Same-repository PR revisions can trigger two equivalent full-suite jobs at the same SHA.
---

Condition or split `.github/workflows/ci.yml` so a same-repository branch SHA is not tested independently for both its `garden/**` push and matching pull-request event. Preserve one required exact-head result, `scripts/check_ci.py` push-run discovery, fork PR coverage, branch-protection compatibility, and all release/merge identity guards. CG-502 measured the ordinary suite at 424.93–432.31s on AWS, making each duplicate worth about 7.1 runner-minutes before setup cost.

## Provenance

Discovered by CG-502 (Find redundant or low-value expensive tests) during run `20260910T105011Z-work`.
## Log
- 2026-09-10T10:58:32+00:00 discovered by CG-502

## Acceptance criteria

- [ ] A same-repository `garden/**` revision produces one full ordinary-suite result for its exact SHA rather than equivalent push and pull-request jobs; fork pull requests still receive the required test run.
- [ ] Keep the required check name and branch-protection result stable, and keep `scripts/check_ci.py` able to discover and bind the selected push or pull-request run to the exact head, repository and workflow identity.
- [ ] Preserve release/merge identity guards, manual reruns and distinct non-equivalent workflows. Event filtering cannot turn an unavailable or stale result into success.
- [ ] Exercise same-repository push plus PR, fork PR, standalone branch push, stale head and rerun fixtures; record the before/after workflow-job count for one same-SHA revision and run repository lint.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:51:05+00:00 dispatched work run 20260910T115105Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16499 tokens)
- 2026-09-10T11:55:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:56:49+00:00 opened https://github.com/joshmarcus/context-garden/pull/431 (base main): Conditioned the CI test job so same-repository garden PR events skip the duplicate ordinary suite while their exact-head push run remains authoritative. Verified 42 focused CI-helper tests and repository lint on commit ae0a4c34. cost=$0.26
- 2026-09-10T11:59:53+00:00 automated review requested changes: The duplicate suite is suppressed, but the skipped PR job can falsely satisfy branch protection when the authoritative push run is unavailable or stale. cost=$0.20
- 2026-09-10T12:52:06+00:00 dispatched revise run 20260910T125206Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17625 tokens)
- 2026-09-10T12:57:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:02:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/431: Same-repository garden PRs now retain the required `test` check as an exact-head push-CI gate rather than a successful skipped job; fork and non-equivalent events still run the ordinary suite. Verified with 46 focused CI-worker tests and repository lint on commit 45ec9ed4. cost=$0.56
- 2026-09-10T13:04:28+00:00 automated review: approve — The workflow eliminates the duplicate ordinary suite while retaining a fail-closed required `test` check tied to the exact push run. cost=$0.17
- 2026-09-10T13:41:52+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/431
