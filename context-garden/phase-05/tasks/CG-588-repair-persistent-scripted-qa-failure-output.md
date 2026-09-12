---
id: CG-588
title: Repair persistent scripted QA failure output
status: done
product: context-garden
phase: phase-05
depends_on:
- id: CG-585
  after: merge
priority: 1
difficulty: medium
reading:
- tests/test_qa.py
- src/garden/runs.py
- src/garden/scheduler/reap.py
branch: garden/cg-588-repair-persistent-scripted-qa-failure-output
pr: https://github.com/joshmarcus/context-garden/pull/455
runner: remote
discovered_from: CG-585
attempts: 1
last_dispatched_at: '2026-09-10T16:08:08+00:00'
created: '2026-09-10T15:31:37+00:00'
updated: '2026-09-10T16:23:57+00:00'
file: tests/test_qa.py
error: Expected detailed triage failure text is absent from the captured CLI output.
---

## Goal

Diagnose and repair scripted QA behavior and failure reporting so the exercised failing step, reason and nonzero exit are accurate, while successful scripted flows can complete through the supported lifecycle.

## Acceptance criteria

- [ ] On the accepted CG585 import repair or later main, preserve the original full-suite and focused failure from test_a_broken_flow_names_the_step_and_exits_non_zero. Identify why expected triage detail is absent: determine whether an earlier lifecycle refusal prevents reaching that step, reporting loses the detail, or the fixture is invalid. Record the actual source and environment.
- [ ] Include the related real CI34495761876 failure in test_scripted_agent_completes_every_flow: reconciliation of a nothing-to-change report refused POST /tasks/DM-002/dispatch with 'run field error changed concurrently'. Coordinate CG539's run-page owner and preserve both observations rather than assuming they share a cause.
- [ ] Correct production behavior or an invalid fixture according to the supported lifecycle contract. Keep precise failed-step output and nonzero exits for actual failures; preserve valid no-change reconciliation. Do not silence errors, skip the scenario, weaken RunStore concurrency/fencing or merely change the expectation to whichever error occurred first.
- [ ] Demonstrate the failing case before the fix, both QA nodes after it, and the relevant surrounding suite. Preserve initial failures and report actual platform coverage; no paid live canary is required.

## Original discovery

After the RunStore import repair allowed the main suite to collect, `tests/test_qa.py::test_a_broken_flow_names_the_step_and_exits_non_zero` failed both in the full suite and an exact focused rerun because the expected `FAILED at 'triage'` detail was absent from CLI output. Diagnose the scripted QA reporting path separately from RunStore locking.

## Provenance

Discovered by CG-585 (Repair the RunStore import cycle on merged main) during run `20260910T145928Z-work`.
## Log
- 2026-09-10T15:31:37+00:00 discovered by CG-585
- 2026-09-10T15:48:24+00:00 approved (delegated operator; complete bounded follow-up with original nonblocking discovery preserved)
- 2026-09-10T15:49:30+00:00 dispatched work run 20260910T154927Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17105 tokens)
- 2026-09-10T16:03:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:04:58+00:00 opened https://github.com/joshmarcus/context-garden/pull/455 (base main): Repaired scripted QA lifecycle races and sandbox teardown; verified 28 focused QA/dead-run tests and Ruff clean on commit 77fd0d0b. The historical isolated triage-output failure did not reproduce on accepted CG-585 main; combined QA exposed earlier lifecycle refusals, which are now covered. cost=$1.61
- 2026-09-10T16:07:47+00:00 automated review requested changes: The concurrent-dispatch repair introduces a restart regression: abandoned launch reservations are no longer reconciled, so tasks can remain stuck instead of becoming retryable. cost=$0.31
- 2026-09-10T16:08:08+00:00 dispatched revise run 20260910T160808Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~18144 tokens)
- 2026-09-10T16:13:06+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:14:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/455: Committed 01f50816 to persist local launch preparer ownership and reap only reservations whose preparer is still alive; abandoned pre-PID runs again become retryable after restart. Verified scripted QA flows, recovery launch behavior, restart/dead-run coverage, resource coverage, and Ruff. cost=$0.55
- 2026-09-10T16:17:19+00:00 automated review: approve — The revision fixes the concurrent launch/reap race while retaining orphan recovery and precise scripted QA failures. cost=$0.30
- 2026-09-10T16:23:57+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/455
