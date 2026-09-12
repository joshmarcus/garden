---
id: CG-533
title: Verify existing security and onboarding closing repairs
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/web/app.py
- src/garden/web/trust.py
- src/garden/web/pages/design.py
- src/garden/kickoff.py
- src/garden/runner/base.py
- README.md
- docs/worker-protocol.md
branch: garden/cg-533-verify-existing-security-and-onboarding-closing
discovered_from: retro:context-garden/phase-05
freeze_exception: true
freeze_exception_reason: Two unresolved security highs violate the phase's no-new-high requirement, and
  harmful first-run defaults undermine the headline non-Python onboarding outcome; existing later-phase
  ownership does not discharge those closing obligations.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T13:17:01+00:00'
created: '2026-09-10T13:10:35+00:00'
updated: '2026-09-10T13:28:05+00:00'
---

## Goal

This is a Phase05 closing-dependency verification task, not a second implementation of existing work. Preserve active CG-517/PR430 and CG-518/PR428 as the owners of worker/operator ingress separation and enforced planner isolation. CG-519/PR426 already owns and supplies inert previews. Coordinate the first-run YAML correction with existing CG-504/PR423, limiting the closure dependency to preserving discovered checks and the selected harness rather than its entire documentation scope. Record exact accepted source and independent review for each correction; task assignment or an unrelated approved head is insufficient.

## Context

Filed by the context-garden/phase-05 retro `reopen` verdict: it must land before the phase can close. Reason: Two unresolved security highs violate the phase's no-new-high requirement, and harmful first-run defaults undermine the headline non-Python onboarding outcome; existing later-phase ownership does not discharge those closing obligations.

## Acceptance criteria

- [ ] Unauthenticated and worker-authenticated requests cannot invoke operator controls, including requests without Origin; permitted worker operations remain functional, verified through CG-517's accepted source.
- [ ] Planner execution cannot read or write controller state or credentials through injected planning instructions; bypass modes cannot silently defeat the enforced boundary, verified through CG-518's accepted source.
- [ ] CG-519's merged inert-preview correction is retained in the accepted closure source and its prior security finding is explicitly marked fixed without claiming an unverified deployment.
- [ ] The recommended first-run configuration preserves a discovered non-Python test/lint command and a selected single harness; the specific CG-504 correction is merged or otherwise independently accepted in the closure source.
- [ ] The closing account links the existing task/PR evidence and distinguishes reviewed merged source from installed controller/worker builds; no duplicate implementation or live canary is required.

## Log

- 2026-09-10T13:10:35+00:00 filed by the context-garden/phase-05 retro reopen verdict (blocking)
- 2026-09-10T13:16:43+00:00 approved by the retro reopen verdict
- 2026-09-10T13:17:01+00:00 dispatched work run 20260910T131658Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~15440 tokens)
- 2026-09-10T13:20:55+00:00 worker blocked: Verified the Phase-05 closing dependencies without duplicating their implementations. CG-519 is merged and its inert-preview regressions pass, but CG-517, CG-518, and the narrow CG-504 first-run correction do not yet provide reviewed merged closure source. cost=$0.59
- 2026-09-10T13:28:05+00:00 cancelled (web)
