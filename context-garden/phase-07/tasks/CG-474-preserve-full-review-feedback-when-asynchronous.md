---
id: CG-474
title: Preserve full review feedback when asynchronous CI finishes
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/review.py
- src/garden/scheduler/human.py
- tests/test_review.py
- tests/scheduler/test_poll.py
branch: codex/cg474-preserve-review-feedback
pr: https://github.com/joshmarcus/context-garden/pull/370
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T11:20:19+00:00'
created: '2026-09-09T11:15:29+00:00'
updated: '2026-09-09T12:08:58+00:00'
automerge: false
operator_owner: 'root: owner-requested urgent manual CG474 fix'
---

## Goal

Preserve the complete applicable automated-review feedback when an asynchronous CI analyzer finishes after the review. A revise worker must receive the full current review plus the CI result, rather than a later CI continuation replacing the review with a generic failure note.

## Confirmed incident

CG-438 review `20260909T095747Z-review` recorded a precise blocking finding: repeated started-review environment failures bypass the bounded recovery mechanism, plus six focused test failures. The subsequent revise run `20260909T095937Z-revise` received a `brief.md` whose `## Review feedback to address` contained only a generic CI failure and a GitHub CLI authentication error. The environment-error finding and failed-test detail were absent. That worker fixed the six tests only; review `20260909T101945Z-review` rediscovered the missing environment-error issue and the scheduler stalled on a repeated finding.

Installed RC10 source confirms the overwrite path: `scheduler/poll.py::_after_ci_check` calls `_apply_feedback`, which assigns `st["pending_feedback"] = fb.to_markdown() + ci_note`. An automated review can write detailed feedback while the CI analyzer is in flight; the later CI continuation then replaces it. The ordinary synchronous poll guard for `CHANGES_REQUESTED` does not protect this asynchronous completion ordering.

CG-362 records older missing/stale feedback symptoms around manual completion, and CG-438 owns review-continuation recovery. Neither owns merging concurrent review and CI feedback into the revise brief, so this task is separate and must not restart or duplicate CG-438's active correction.

## Acceptance criteria

- [ ] When review feedback and CI analysis complete in either order for the same current head, `pending_feedback` retains the complete applicable review record and adds the CI findings without replacement, duplicated sections or lost finding identities.
- [ ] The next work/revise brief includes every applicable blocking review finding, failed criterion and concrete CI failure. The CG-438 ordering reproduces before the fix and includes the environment-error recovery finding after the fix.
- [ ] Head, run and review provenance are checked before merging feedback. A stale CI continuation cannot resurrect feedback for an obsolete head, a superseded review cannot return, and an already resolved finding remains resolved.
- [ ] Preserve review-round/revision accounting, original verdicts, run results, source identity and bounded-stall detection. Do not convert a rejection into approval or bypass a genuine CI/source failure.
- [ ] Focused tests cover review-then-CI, CI-then-review, same finding deduplication, stale/moved head, resolved/superseded review items, restart between writes, and the exact revise-brief content supplied to the worker.

## Evidence

- `/home/joshua/garden/.garden/runs/CG-438/20260909T095747Z-review/run.json`
- `/home/joshua/garden/.garden/runs/CG-438/20260909T095937Z-revise/brief.md`
- `/home/joshua/garden/.garden/runs/CG-438/20260909T101945Z-review/run.json`
- `/home/joshua/work/operator-test-tmp/input-sweep.json`

## Log

- 2026-09-09T11:15:00+00:00 filed after the owner asked whether the worker receives the full review; the preserved records prove this worker did not.
- 2026-09-09T11:16:14+00:00 approved (cli)
- 2026-09-09T11:19:22+00:00 Owner requests urgent manual resolution; operator reserved existing task, preserving automatic actions until reviewed publication.
- 2026-09-09T11:20:19+00:00 dispatched work run 20260909T112019Z-work via manual [human] (fresh session, base main, ~16206 tokens)
- 2026-09-09T12:08:58+00:00 operator squash PR merged and verified on main; source patch identity preserved
