---
id: CG-499
title: Show worker status and current jobs in a Now tab and API
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/remote_worker.py
- src/garden/managed_worker.py
- src/garden/runs.py
- src/garden/web/pages/now1.py
branch: garden/cg-499-show-worker-status-and-current-jobs-in-a-now-tab
pr: https://github.com/joshmarcus/context-garden/pull/411
attempts: 1
last_dispatched_at: '2026-09-10T04:29:37+00:00'
created: '2026-09-10T01:56:31+00:00'
updated: '2026-09-10T05:11:07+00:00'
---

## Goal

Provide a read-only worker-status API and a Workers tab within Now so the operator can see every configured or enrolled worker, whether it is available, and exactly what is running on it. Zero running tasks must not imply that the fleet has disappeared.

## Context

Owner request: "We need an api/tab in now to view the status of the workers and what's running on them." Initially filed as a draft at the owner request. On September 10 the owner explicitly requested reviewing drafts and marking them ready, authorizing normal implementation through the approval gate.

The current UI emphasizes active runs, making an idle fleet look like lost workers. Recent real observations include six online hosts with no eligible jobs, daemon restarts after idle claim HTTP 502 responses, active authenticated remote leases, and manual reservations that do not represent executing processes. Distinguish infrastructure presence, worker-agent contact, admission availability, and task execution rather than deriving every status from active run counts.

Reuse existing host registry, enrollment/claim/heartbeat and run data. Coordinate with CG-348 pool health and controls, CG-494 controller scheduler health, and CG-491 transient idle-claim recovery; this task owns the provider-neutral worker view and API rather than duplicating those features. Idle worker liveness needs its own observable contact evidence, independent of a task lease.

## Acceptance criteria

- [ ] Add a read-only API returning all configured/enrolled workers, including idle workers and unavailable workers, with stable identity, local/remote placement, observed status, last contact and evidence timestamp, available capacity, and current task/run/mode links. Clearly mark unknown or stale evidence.
- [ ] Add a Workers tab in Now showing fleet totals and individual workers, with their current jobs and drill-down links. Distinguish idle/available, executing, draining, restarting or reconnecting, unreachable/stale, and explicitly terminated/disabled states when supported by evidence; do not call a host terminated merely because contact expired.
- [ ] Show task lease expiry/recovery separately from worker liveness. Explain that available workers poll for work and receive a job lease when a claim succeeds; they do not need a new task lease merely to appear online. Show why idle capacity cannot take queued work where the scheduler knows the reason.
- [ ] Do not count manual reservations, queued but unclaimed runs, or completed work as executing jobs. Reconcile stale/replaced worker identities and lease generations without duplicate workers or duplicate job occupancy; preserve useful last-seen history.
- [ ] Keep the UI responsive with bounded reads and refresh work. Avoid synchronous cloud or SSH fan-out on page requests; reuse cached/recorded telemetry with explicit freshness. Apply existing access controls and never expose enrollment keys, bearer tokens, cloud credentials, or other secret configuration.
- [ ] Verify zero-job/all-workers-idle, busy mixed local/remote work, daemon reconnect, expired task lease, lost contact, terminated/replaced hosts, stale telemetry, and no configured workers. Cover API/UI agreement and desktop/mobile tab behavior. Use portable APIs and configurable paths for Linux, macOS, and Windows through WSL, and report any untested platform.

## Out of scope

- Provisioning, replacing, restarting, terminating, or upgrading workers from this read-only view.
- New cloud spending, deadline extensions, or changes to fleet capacity and scheduling limits.

## Log

- 2026-09-10T02:33:40+00:00 approved (owner requested draft review and readiness; operator verified brief)
- 2026-09-10T02:56:29+00:00 dispatched work run 20260910T025626Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17924 tokens)
- 2026-09-10T03:12:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:13:45+00:00 opened https://github.com/joshmarcus/context-garden/pull/411 (base main): Added durable idle-worker contact telemetry, a secret-free read-only /api/workers endpoint, and a responsive Workers tab under Now. Verified worker/job state reconciliation with 211 focused tests, full Ruff lint, and inspected 1280px and 390px renders without horizontal overflow. cost=$3.53
- 2026-09-10T03:19:01+00:00 automated review requested changes: Worker freshness is computed against the idle poll interval, causing healthy busy workers to appear stale and stale workers to contribute available capacity. cost=$0.66
- 2026-09-10T03:30:22+00:00 dispatched revise run 20260910T033019Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19183 tokens)
- 2026-09-10T03:36:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:37:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/411: Corrected worker freshness and capacity accounting at commit 90f78cc6. Busy workers remain fresh across their normal heartbeat cadence, while lost-contact workers remain visibly occupied but report unreachable with zero available capacity; 82 focused tests and full Ruff lint passed. cost=$0.95
- 2026-09-10T03:39:42+00:00 automated review requested changes: Worker status, freshness, occupancy, and API/UI behavior are generally sound, but queued-work diagnostics are missing for executing workers with spare capacity. cost=$0.32
- 2026-09-10T03:39:54+00:00 dispatched revise run 20260910T033950Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19226 tokens)
- 2026-09-10T03:42:08+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:43:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/411: Executing remote workers with spare capacity now evaluate queued-work compatibility against their remaining capacity, and the API and Workers tab explain when queued work is incompatible or too heavy. Verified at commit 780aff39a26d6d767729c000cf324d2c363ce5e4 with 10 focused worker tests and full Ruff lint. cost=$0.44
- 2026-09-10T03:43:30+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/api.py); a rebase agent will resolve it
- 2026-09-10T03:45:51+00:00 dispatched rebase run 20260910T034550Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2231 tokens)
- 2026-09-10T03:48:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/411: Rebased CG-499 onto origin/main and resolved the worker heartbeat API conflict. cost=$0.01
- 2026-09-10T03:50:25+00:00 automated review requested changes: The API and Now tab omit enrolled workers until their first successful contact, so an idle or unavailable enrolled fleet can disappear. cost=$0.37
- 2026-09-10T04:07:34+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T04:29:37+00:00 dispatched revise run 20260910T042934Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20171 tokens)
- 2026-09-10T04:33:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:34:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/411: Enrollment-registry workers now remain visible before first contact as unknown/unavailable with zero jobs, while configured, enrolled, and contacted instances of the same identity are counted once. Added the missing architecture-map entry and verified final HEAD 2b449bb22c82c0b80f3513dde99a1ca8c28a0b6e with 18 worker/registry tests, 2 architecture tests, and clean Ruff lint; controller-owned exact-head CI and review remain to run after publication. cost=$0.61
- 2026-09-10T04:40:10+00:00 automated review: approve — The read-only API and Now Workers tab meet the requested fleet visibility, status, occupancy, freshness, and secret-handling outcomes. The previous omission of enrolled workers before first contact is resolved. cost=$0.37
- 2026-09-10T05:09:35+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T05:11:07+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/411
