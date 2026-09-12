---
id: CG-592
title: Show each run's worker or local execution location on the Runs page
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/web/pages/runs.py
- src/garden/runs.py
- src/garden/now1.py
branch: garden/cg-592-show-each-run-s-worker-or-local-execution-locati
pr: https://github.com/joshmarcus/context-garden/pull/472
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T19:42:18+00:00'
created: '2026-09-10T16:21:44+00:00'
updated: '2026-09-10T19:57:07+00:00'
---

## Goal

Show where each run executed directly on the Runs page: the specific worker for remote execution, or a clear local-process label for local execution.

## Context

Owner request: "runs page should include *where* each run ran, aka which worker or was it a local process". An operator should be able to scan the run list and identify execution location without opening every transcript. Reuse existing authoritative runner and host attribution. CG-216 supplied remote host attribution and CG-485 corrected lifecycle presentation; CG-539 separately owns check commands and outcomes. Preserve those accepted behaviors and reconcile any shared run-page changes without duplicating their scope.

## Acceptance criteria

- [ ] Every row in the Runs page exposes a readable execution-location value. Local execution says Local; remote execution identifies the actual worker by its supported display name or stable safe identifier. Keep that value consistent with the run detail page and present it alongside existing status and mode information.
- [ ] Derive the value from recorded execution attribution, not the task's current runner preference or a worker's current availability. Historical completed and failed runs retain their recorded location even when a worker is offline, removed or renamed. Reuse stored attribution and existing compatibility behavior; do not invent missing history.
- [ ] Distinguish remote work awaiting a claim, manual/external work, and legacy records with unknown location. A missing remote host or missing local PID must not automatically turn a run into Local or imply it executed. Preserve the lifecycle distinctions established by CG-485.
- [ ] Use the existing authorized worker labels and display/privacy rules. Where a worker detail link already exists, reuse it when available and keep a readable fallback for historical workers. Do not expose credentials or private connection endpoints in the location label.
- [ ] Preserve sorting, filtering, pagination and live refresh behavior. Verify the location is usable at desktop and narrow widths, with long worker names handled without breaking the page layout.
- [ ] Add proportionate focused coverage for local and remote runs, active and finished history, unclaimed/manual/unknown records, and historical workers no longer in current configuration. Use portable APIs for Linux, macOS and Windows through WSL, and report the environments actually tested.

owner_request_key: owner-runs-page-execution-location-20260910

## Log

- 2026-09-10T16:31:26+00:00 approved (delegated operator; owner Runs location request, duplicate and scope review complete)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:42:02+00:00 dispatched work run 20260910T174200Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~13582 tokens)
- 2026-09-10T17:48:37+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:52:04+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.87
- 2026-09-10T18:34:35+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:37+00:00 opened https://github.com/joshmarcus/context-garden/pull/472 (base main): Added durable execution-location labels to Runs rows and run details, derived exclusively from recorded run attribution. Verified the focused web regression and changed-file lint; full lint currently reports an unrelated existing import-order error in src/garden/runner/local.py.
- 2026-09-10T18:34:37+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:50:10+00:00 automated review requested changes: Execution locations render consistently, but terminal local reservations that never launched are mislabeled as Local. cost=$0.26
- 2026-09-10T18:50:34+00:00 dispatched revise run 20260910T185034Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14538 tokens)
- 2026-09-10T18:54:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:56:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/472: Fixed terminal local pre-launch failures so Local requires a recorded PID, and added regression coverage. Exact-head targeted test passed; the full affected web test file and required lint passed on identical source before the commit. cost=$0.33
- 2026-09-10T19:06:50+00:00 automated review: approve — Execution locations are derived from durable run attribution and consistently displayed in the Runs list and detail page, with clear local, remote, awaiting-claim, manual, and unknown states. cost=$0.35
- 2026-09-10T19:08:17+00:00 CI failure
- 2026-09-10T19:08:47+00:00 dispatched revise run 20260910T190847Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14571 tokens)
- 2026-09-10T19:14:13+00:00 worker blocked: Investigated CI at 8f5ed288: the exact-head guard intentionally stops one duplicate job, while the actual pytest job fails. Locally, the full affected web module passed under the supervised validator (exit 0), and `.venv/bin/ruff check src tests scripts` passed; no configured type-check command exists. cost=$0.45
- 2026-09-10T19:33:21+00:00 triage: changes requested by hand: Preserve current independent approval at8f5ed288 while fixing the two actual CI failures in34517203083 (2623passed): tes
- 2026-09-10T19:42:18+00:00 difficulty medium -> hard after 2 substantive revisions; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-10T19:42:18+00:00 dispatched revise run 20260910T194218Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14992 tokens)
- 2026-09-10T19:44:29+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:45:43+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/472: Updated the two failing end-to-end remote-worker tests to validate durable host attribution and the new served label `Remote · build-1`. All three focused tests passed on Linux/Python 3.12, required lint passed, and the worktree is clean at commit 18323960. cost=$0.46
- 2026-09-10T19:48:12+00:00 automated review: approve — Execution locations are consistently shown in the Runs list and detail page, using recorded attribution without mislabeling unlaunched runs. cost=$0.37
- 2026-09-10T19:55:45+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T19:57:07+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/472
