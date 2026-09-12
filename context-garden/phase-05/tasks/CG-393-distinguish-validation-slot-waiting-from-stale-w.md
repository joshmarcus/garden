---
id: CG-393
title: Distinguish validation-slot waiting from stale-worktree idle timeouts
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 0
difficulty: medium
reading:
- src/garden/runner/base.py
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/reap.py
branch: garden/cg-393-distinguish-validation-slot-waiting-from-stale-w
pr: https://github.com/joshmarcus/context-garden/pull/304
attempts: 1
last_dispatched_at: '2026-09-08T12:07:33+00:00'
created: '2026-09-07T19:26:26+00:00'
updated: '2026-09-08T17:22:26+00:00'
---

## Goal

A newly launched check waiting for the shared heavy-validation lease is not killed as idle based on worktree timestamps predating that run. Waiting remains visible as operator-owned resource admission, not a request for a human to retry code.

## Evidence

CG385 check20260907T183736Z-check and CG386 check20260907T183624Z-check were killed about72seconds after launch with idle22minutes. Both execution.json records said waiting/heavy-test budget full(limit1), with no stdout or stderr; exit143. Run.last_activity_at uses old worktree mtimes without clamping to started_at. Their collected failures then replayed owner stops every tick (relatedCG386).

## Acceptance criteria

- [ ] New run idle age cannot predate run start; explicit supervisor waiting has its own bounded admission-wait policy and truthful reason.
- [ ] Preserve real silent-worker timeouts and shared heavy-work cap; do not disable resource safeguards or fabricate pass results.
- [ ] Focused lifecycle regression uses an old checkout, occupied lease, newly created check, release/recovery and real idle timeout. Waiting releases normally once capacity is available, without code revision or duplicate execution.
- [ ] Missing check results remain unverified, with recoverable continuation. LinkCG386 idempotency rather than duplicate its scope.

## Log

- 2026-09-07T20:22:47+00:00 reordered in context-garden/phase-05 (order None -> 0) (web)
- 2026-09-07T20:22:47+00:00 Operator prioritizes repeated false idle-timeout repair ahead of ordinary phase05 backlog; preserve active runs and normal admission. CG385/386 retries failed again while waiting on heavy-test capacity.
- 2026-09-07T21:09:10+00:00 Operator corrected missing checklist markers and reading manifest that prevented dispatch of this ready task; acceptance scope unchanged.
- 2026-09-08T11:08:42+00:00 dispatched work run 20260908T110840Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~19314 tokens)
- 2026-09-08T11:26:48+00:00 preserved uncommitted worktree changes from run 20260908T110840Z-work outside the PR: `git stash apply e6e7b266d469477435f46e990e869ad55cf23a53` in /home/joshua/work/worktrees/CG-393 (garden:CG-393:20260908T110840Z-work:reap)
- 2026-09-08T11:28:48+00:00 opened https://github.com/joshmarcus/context-garden/pull/304 (base main): Validation-slot waiting no longer inherits stale checkout idle time, has a bounded admission timeout with the supervisor's reason, and returns to normal idle protection after capacity is released. CI passed for commit 6d7e1e798e454efdc4006ff54507ed7efd8c750e. cost=$1.46
- 2026-09-08T12:06:29+00:00 automated review requested changes: Admission waiting is distinguished from idle time, but its timeout incorrectly counts the run's entire lifetime and the required real lease/release lifecycle is unverified. cost=$0.35
- 2026-09-08T12:07:33+00:00 dispatched revise run 20260908T120731Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~20656 tokens)
- 2026-09-08T12:22:38+00:00 preserved uncommitted worktree changes from run 20260908T120731Z-revise outside the PR: `git stash apply 4635e494855695dbf6a0250d161273cad9ecc1b5` in /home/joshua/work/worktrees/CG-393 (garden:CG-393:20260908T120731Z-revise:reap)
- 2026-09-08T12:56:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/304: Admission timeouts now begin when the supervisor first publishes waiting, not when the run began. A real-process lifecycle regression proves held-lease waiting, release, single execution, and ordinary silent-worker timeout behavior. cost=$1.27
- 2026-09-08T13:52:26+00:00 automated review requested changes: Implementation and focused lifecycle regressions pass, but the required exact-head served interaction does not exercise admission waiting, lease release, or its recovery outcome. cost=$0.35


## Repeated remote-check observation, 2026-09-08T1454

CG401 run20260908T144431Z-check was queued unclaimed at14:44, then reported idle22minutes from older worktree activity. CG409 showed the same classification at62/75minutes despite newly queued checks. Separately, an operator-created local CG409 attempt exited immediately with an explicit XDG_RUNTIME_DIR ownership error; its later stale classification obscured that actual startup failure. Preserve existing scope/work and test that queued/no-process and explicit startup-failure states are not misrepresented as idle implementation. CG431 owns the separate controller-local replay/backend routing defect. Evidence: operator-test-tmp/heartbeat-20260908T1454 and human-input-20260908T1405.


## Unclaimed review age corroboration, 2026-09-08T16:15:35.229474+00:00

CG398153509 and CG430153506 review records have no host/claim/PID/output, only brief/run metadata; they expired three minutes later as idle42/39min. CG395153507 similarly idle21min. CG-438 owns lost review intention/requeue, while this task owns queued-vs-running age correctness. Preserve exact records and do not duplicate the recovery state machine.
- 2026-09-08T17:22:26+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/304
