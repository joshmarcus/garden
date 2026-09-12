---
id: CG-433
title: Prevent LocalRunner process_finished from hanging on a completed stdin consumer
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/runner/local.py
- src/garden/run_supervisor.py
- src/garden/runs.py
- tests/test_runners.py
branch: garden/cg-433-prevent-localrunner-process-finished-from-hangin
pr: https://github.com/joshmarcus/context-garden/pull/325
runner: remote
discovered_from: CG-328
attempts: 1
last_dispatched_at: '2026-09-08T16:51:57+00:00'
created: '2026-09-08T15:33:14+00:00'
updated: '2026-09-08T17:29:26+00:00'
file: tests/test_runners.py
error: test_local_runner_launch_flips_process_finished blocks at line 218; isolated run required KeyboardInterrupt
  after 25.91s
---

## Goal

Ensure LocalRunner and its supervisor detect EOF and complete a finished stdin-consuming command without hanging process_finished or the ordinary suite.

## Context

CG328 repeatedly observed tests/test_runners.py::test_local_runner_launch_flips_process_finished hang under Python3.14.4 with the fixture command sleep0.5;cat. This is distinct from CG430's accumulation of already-exited adopted children; inspect/reuse that repair but do not assume it fixes a still-live stdin consumer.

## Acceptance criteria

- [ ] Reproduce the reported stdin/EOF completion behavior in an isolated bounded fixture, recording interpreter, fd/process ownership and actual liveness. Compare Python3.14 with the supported3.12 environment where useful.
- [ ] Fix the responsible runner/supervisor or fixture behavior without stealing exit statuses, closing unrelated input, leaking descendants or weakening validation ownership.
- [ ] The regression has its own bounded deadline and cleanup, so a future failure fails promptly instead of wedging the ordinary suite.
- [ ] Verify normal EOF, a still-active consumer, nonzero exit and cancellation through the actual LocalRunner/supervisor path. Preserve useful CG328 work; no production-process fault injection or default stress workload.

## Provenance

Discovered by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`.
## Log
- 2026-09-08T15:33:14+00:00 discovered by CG-328
- 2026-09-08T15:34:48+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:36:12+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:37:32+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:39:01+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:40:29+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:42:04+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:43:34+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:45:10+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:46:31+00:00 also found by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) during run `20260908T145444Z-revise`
- 2026-09-08T15:56:32+00:00 approved (owner-delegated-input-triage)
- 2026-09-08T16:05:21+00:00 dispatched work run 20260908T160521Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~18328 tokens)


## Corroborating discovery, 2026-09-08T16:04:51.955690+00:00

CG435 from CG411/run20260908T153212Z-work reports the same test hanging after the sleep/cat child exits, with the supervisor waiting despite no children. Preserve both reports and establish real process/fd state; do not assume a live stdin consumer is the cause. CG435 is consolidated here to avoid duplicate implementation.
- 2026-09-08T16:35:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/325 (base main): LocalRunner supervisors now reap adopted descendants without consuming the primary shell status, allowing stdin-consuming commands to complete and publish exit_code. Bounded lifecycle regressions cover EOF, active consumers, nonzero exits, cancellation, and descendant cleanup. cost=$0.88
- 2026-09-08T16:50:13+00:00 automated review requested changes: The supervisor fix is focused and the runner suite and lint pass, but the new lifecycle regressions do not guarantee cleanup on all failure paths. The scheduler interaction manifest could not be inspected because its referenced path was unavailable. cost=$0.35
- 2026-09-08T16:51:57+00:00 dispatched revise run 20260908T165157Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19392 tokens)
- 2026-09-08T17:03:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/325: Detached LocalRunner lifecycle tests now always stop and reap their supervisor, including when an assertion happens before completion. A bounded regression proves failed fixture cleanup while preserving EOF, nonzero, cancellation, and adopted-descendant coverage. cost=$0.48


## Consolidated discovery CG-440

The AWS ordinary suite fails `tests/test_onboard.py::test_onboard_this_repository_uses_documented_setup_and_ci_tests` because the generated report lacks `GitHub repository metadata`, then hangs in `tests/test_runners.py::test_local_runner_launch_flips_to_running_only_after_pid` with a supervisor running `sleep 0.5; cat`. Diagnose these baseline validation failures so the ordinary suite completes deterministically.

## Provenance

Discovered by CG-428 (Keep remote worker runs alive across controller redeploys) during run `20260908T154233Z-work`.
## Log
- 2026-09-08T16:21:10+00:00 discovered by CG-428


Operator disposition: reuse this existing repair; preserve all reporter evidence. CG432 owns onboarding metadata transport identity. CG433 owns completed stdin-consumer liveness and bounded regression cleanup. Do not duplicate implementation.


## Consolidated discovery CG-441

The ordinary suite can hang indefinitely in `test_local_runner_launch_flips_process_finished` because it calls blocking `os.waitpid(run.pid, 0)` without a timeout. During CG-404 validation, its `sleep 0.5; cat` supervisor remained alive for more than six minutes and prevented pytest from reporting the suite's earlier failure detail. Replace the unbounded wait with bounded polling/cleanup while preserving end-to-end launch coverage.

## Provenance

Discovered by CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle) during run `20260908T162136Z-revise`.
## Log
- 2026-09-08T16:46:47+00:00 discovered by CG-404


Operator disposition: reuse this existing repair; preserve all reporter evidence. CG432 owns onboarding metadata transport identity. CG433 owns completed stdin-consumer liveness and bounded regression cleanup. Do not duplicate implementation.
- 2026-09-08T17:22:29+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/325
- 2026-09-08T17:29:26+00:00 automated review could not start: CG-433 is done: #325 was merged at 17:22:29
