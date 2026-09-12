---
id: CG-461
title: Prevent nested validation admission from stalling remote lifecycle checks
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/validation.py
- src/garden/run_supervisor.py
- src/garden/checkrun.py
- src/garden/checks.py
- src/garden/remote_worker.py
- src/garden/managed_worker.py
- tests/test_remote_worker.py
- tests/test_runners.py
- tests/conftest.py
branch: garden/cg-461-prevent-nested-validation-admission-from-stallin
runner: remote
discovered_from: CG-438
attempts: 1
last_dispatched_at: '2026-09-09T01:05:48+00:00'
created: '2026-09-09T00:30:28+00:00'
updated: '2026-09-09T01:31:05+00:00'
file: tests/test_remote_worker.py
error: Both `test_remote_lifecycle_over_served_http` variants timed out after 30 seconds during `worker("check")`;
  reproduced in isolation and affected paths are unchanged from origin/main.
---

Both standalone and managed served-HTTP remote lifecycle tests time out in their check worker subprocess when run under the supervised validation wrapper. Diagnose validation ownership/admission propagation for nested remote check commands.

## Provenance

Discovered by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) during run `20260908T235138Z-revise-2`.
## Log
- 2026-09-09T00:30:28+00:00 discovered by CG-438

## Acceptance criteria

- [ ] Reproduce or explain the nested supervised remote-lifecycle check wait with the actual owner/run/admission identities preserved. Distinguish inherited fixture environment from a production ownership defect before editing source; plain focused CI currently passes these flows.
- [ ] If the fixture leaks an outer owner, isolate only its synthetic child environment; if the real producer changes authority incorrectly, repair that boundary. Preserve authentic host-scoped admission, fences, and the one-slot cap; do not disable resource checks to make the test pass.
- [ ] A bounded targeted regression covers both standalone and managed check commands beneath the supported validation wrapper and proves completion without self-deadlock or duplicate execution. Preserve timeout evidence and clean up only disposable processes/files.
- [ ] Run the smallest affected validation/runner tests with explicit per-test and suite bounds. No unrelated full stress run, production cgroup experiment, cloud launch, or generic UI screenshot checklist is required.

## Operator scope clarification 2026-09-09T01:05:16.732720+00:00

This is a narrow diagnosis of the concrete CG438 nested-wrapper fixture report, not another broad reviewer/admission repair. CG456 owns remote review and clarification backend selection. CG446 already owns test time budgets; preserve both scopes.
- 2026-09-09T01:05:17+00:00 approved (delegated-operator-proportionate-verification)
- 2026-09-09T01:05:48+00:00 dispatched work run 20260909T010548Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14064 tokens)
- 2026-09-09T01:08:28+00:00 worker found no change to make: Current-head source already contains the narrow fixture isolation and production ownership boundary required by CG-461; adding a duplicate change would not improve behavior.; reconciling with checks and a fresh review
- 2026-09-09T01:08:30+00:00 branch pushed but PR failed (pull request create failed: GraphQL: Head sha can't be blank, Base sha can't be blank, No commits between main and garden/cg-461-prevent-nested-validation-admission-from-stallin, Head ref must be a branch (createPullRequest)); open it by hand and run `garden pr CG-461 <url>` cost=$0.34
- 2026-09-09T01:14:59+00:00 description rewritten by the reviewer (GitHub update failed) cost=$0.28
- 2026-09-09T01:31:05+00:00 Operator completion of already implemented work, under standing owner delegation: author run 20260909T010548Z-work-2 returned no_change; actual native review 20260909T011134Z-review approved all four frozen criteria with no findings at 14acfbccf2fe37b30895c4e22c00140aeee84df3. Reviewer ran both supported-wrapper remote lifecycle variants (2 passed, 22.91s), two targeted runner tests (2 passed, 0.34s), and lint. Fresh GitHub comparison confirms this exact reviewed source is already on main. There is no PR, no source diff, and no active run. Empty PR-description feedback is inapplicable to a no-change completion; preserved all original author/reviewer results. No PR or approval was fabricated and no merge performed.
