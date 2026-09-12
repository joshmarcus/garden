---
id: CG-511
title: Narrow duplicated remote lifecycle variants
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/remote_worker.py
- src/garden/managed_worker.py
- tests/test_remote_worker.py
branch: garden/cg-511-narrow-duplicated-remote-lifecycle-variants
pr: https://github.com/joshmarcus/context-garden/pull/434
runner: remote
discovered_from: CG-502
attempts: 1
last_dispatched_at: '2026-09-10T11:54:11+00:00'
created: '2026-09-10T10:58:32+00:00'
updated: '2026-09-10T12:59:35+00:00'
file: tests/test_remote_worker.py
error: Standalone and managed parameters repeat nearly the entire server, subprocess, Git, and check lifecycle.
---

Keep one complete real TCP/separate-CLI remote lifecycle journey, then cover the managed mode's unique host-lock and setup-cache contract through a smaller worker-boundary test. Preserve authentication, lease fencing, setup/check result transport, PR creation, and the managed lock assertion; compare assertion inventories before removing duplicated setup. CG-502 measured the two variants at about 2.5s each.

## Provenance

Discovered by CG-502 (Find redundant or low-value expensive tests) during run `20260910T105011Z-work`.
## Log
- 2026-09-10T10:58:32+00:00 discovered by CG-502

## Acceptance criteria

- [ ] Keep one complete real TCP and separate-CLI lifecycle covering authentication, lease fencing, source/setup, check and result transport, publication and PR creation.
- [ ] Replace the duplicated managed parameter journey with a smaller worker-boundary regression that still proves managed host locking and setup-cache behavior.
- [ ] Compare the assertion inventory before removal and retain every behavior unique to standalone or managed mode; shared assertions may be removed only when the retained end-to-end path proves them.
- [ ] Run the focused remote-worker suite and repository lint, and report the before/after duplicate test runtime without requiring live infrastructure.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:54:11+00:00 dispatched work run 20260910T115411Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15890 tokens)
- 2026-09-10T12:01:29+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T12:02:56+00:00 opened https://github.com/joshmarcus/context-garden/pull/434 (base main): Committed 434b8d11, retaining one full standalone real-TCP/separate-CLI lifecycle and replacing the managed duplicate with a focused host-lock/setup-handoff regression. Targeted tests passed and lint is clean; the full remote-worker suite was attempted twice but the supervised local runner returned at 90% without a completion status. cost=$0.55
- 2026-09-10T12:54:57+00:00 automated review: approve — The PR retains the complete standalone TCP/CLI lifecycle and replaces the managed variant with focused lock and single-setup-handoff coverage. No blocking defects found. cost=$0.34
- 2026-09-10T12:59:35+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/434
