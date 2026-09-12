---
id: CG-529
title: Automatically start the phase closing review when prerequisites are met
status: done
product: context-garden
phase: phase-07
depends_on:
- id: CG-585
  after: merge
- id: CG-593
  after: merge
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/retro.py
- src/garden/scheduler/persona.py
- src/garden/scheduler/__init__.py
- src/garden/config.py
- src/garden/cli/planning.py
- src/garden/retro.py
branch: garden/cg-529-automatically-start-the-phase-closing-review-whe
pr: https://github.com/joshmarcus/context-garden/pull/452
runner: remote
attempts: 2
last_dispatched_at: '2026-09-11T03:03:10+00:00'
created: '2026-09-10T12:56:24+00:00'
updated: '2026-09-11T04:16:09+00:00'
---

## Goal

Automatically initiate the configured final phase review/retro when its prerequisites are satisfied, without requiring an operator to notice readiness and run a command or an external heartbeat script. Reuse the native retro workflow and its existing review, reconciliation, finding, PR and closure gates.

## Context

The owner asked whether final reviews start automatically and requested a task if initiation is manual. Current start_retro is invoked by the CLI; scheduler ticks reap and advance a retro that was already started. Phase 05 has needed an operator helper to select the correct closing personas and initiate the workflow. This task fills the readiness-to-start gap rather than replacing the existing automated continuation.

## Acceptance criteria

- [ ] Define and expose the readiness policy for automatic closing review, respecting terminal task state, configured phase prerequisites, accepted stabilization evidence, explicit holds/freeze policy and any required owner decision. Task completion alone never means the phase is closed.
- [ ] Persist an idempotent review request when a phase becomes eligible and start it through normal resource/harness admission. Waiting for capacity, quota or environment readiness remains visible with a reason and resumes automatically; ordinary dispatch does not need a global pause merely to queue or prepare the review.
- [ ] Use the correct phase, accepted-source/evidence identity and configured review roles. Reuse applicable completed reports while distinguishing stale or wrong-phase reports. Do not introduce another mandatory review merely to satisfy a fixed round count.
- [ ] Drive the existing persona, reconciliation, follow-up ownership/approval, PR and closure stages according to policy; retain genuine blockers and require the actual closure verdict and resolved blocking work. Honor existing owner acceptance and the policy that live canaries are optional.
- [ ] Survive process restarts, concurrent readiness detection, an overlapping manual start, partial preparation and failed runs without duplicate model jobs, duplicated findings or premature closure. Expensive preparation and remote metadata collection must not hold the scheduler's mutation lock for their whole duration.
- [ ] Show the current closing-review stage, queued/running state, source/evidence identity and blocking reason in the phase view and operator status, and provide an explicit supported retry or policy override when genuinely needed.
- [ ] Verify readiness transitions, explicit holds, accepted prerequisites, admission limits, restart recovery, manual/automatic races, report freshness, blockers and actual closure in proportionate deterministic tests on portable code paths.

owner_request_key: owner-auto-closing-review-20260910

## Log

- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T14:48:14+00:00 dispatched work run 20260910T144811Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21829 tokens)
- 2026-09-10T14:57:57+00:00 worker blocked: Committed the durable automatic closing-review queue, readiness policy, admission visibility, source-bound report reuse, manual race handling, and operator status. Ruff and Python compilation pass, but pytest cannot collect due to the base branch's garden.runs/garden.hosts.drain circular import, and expensive retro preparation still holds the scheduler controller lock. cost=$2.35

## Operator dependency disposition

The partial implementation is preserved at clean local commit1205032847e502540e92b65188f25bcce1e74af0 in the existing CG-529 worktree, with an operator source bundle. Original run144811 remains BLOCKED, not successful. Wait for actual CG-585 merge to repair the shared main import cycle, then continue this existing implementation and resolve its still-unmet criterion: move expensive Git/worktree/walkthrough/metadata preparation outside the scheduler mutation lock using a short persisted claim and guarded reconciliation. Keep this criterion owned by CG-529; do not create a duplicate repair task. Publish/attach the preserved source through the supported PR path before resuming a bounded revision, rather than discarding it in a fresh checkout. Require actual tests/CI after base repair. This is a dependency disposition, not acceptance of the blocked verification or premature phase closure.
- 2026-09-10T15:37:13+00:00 Preserved partial source; wait for CG-585 merge before continuing the existing implementation and its remaining preparation-lock criterion.
- 2026-09-10T15:53:46+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/452 (pr_number none -> 452)
- 2026-09-10T15:53:46+00:00 triage: changes requested by hand: Continue the preserved implementation at1205032847e502540e92b65188f25bcce1e74af0 on this existing branch; the original w
- 2026-09-10T16:28:16+00:00 dispatched revise run 20260910T162811Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22839 tokens)
- 2026-09-10T16:40:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:41:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Closing-review preparation now uses a durable request/claim handoff so Git, worktree, walkthrough and metadata work runs outside the scheduler mutation lock while request and accepted-source identity remain guarded. Rebased onto accepted origin/main and verified the retro lifecycle, phase view, restart recovery, race handling, lint and compilation at commit 05187d8c. cost=$3.13
- 2026-09-10T16:45:11+00:00 automated review requested changes: The durable preparation handoff works for an already queued request, but a fresh manual start still exposes a pre-persistence race that can create duplicate closing reviews. cost=$0.60
- 2026-09-10T16:53:12+00:00 dispatched revise run 20260910T165309Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~23618 tokens)
- 2026-09-10T16:58:35+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:00:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Manual and automatic closing-review starts now converge on one durable request under the scheduler lock, while walkthrough capture and other expensive preparation remain outside it. Verified at commit f16c0985 with 42 retro tests, clean Ruff lint, Python compilation, and diff checks. cost=$0.80
- 2026-09-10T17:02:34+00:00 automated review requested changes: Automatic queueing and lock handoff are well structured, but queued requests can bypass newly introduced holds, and failed persona runs leave the review permanently stuck without an exposed reason or retry. cost=$0.48
- 2026-09-10T17:31:41+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T17:31:42+00:00 delegated operator routed next correction to existing renewed remote fleet after owner reported idle workers; existing scope, review/CI gates and fleet limits preserved
- 2026-09-10T17:32:11+00:00 dispatched revise run 20260910T173211Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24145 tokens)
- 2026-09-10T17:41:34+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:43:27+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Queued automatic closing reviews now revalidate freeze, owner, prerequisite, task-state, and stabilization gates immediately before dispatch. Failed phase-persona runs persist an operator-visible reason and `garden retro <phase>` retries only failed roles; 44 retro tests, Ruff, compilation, and diff checks passed at f9d7f32e. cost=$1.91
- 2026-09-10T17:48:48+00:00 automated review requested changes: The readiness and retry improvements are sound, but dispatch can exceed review capacity, duplicate persona jobs after interrupted preparation, and retain stale evidence identity. cost=$0.59
- 2026-09-10T18:46:02+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T18:47:16+00:00 dispatched revise run 20260910T184716Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24625 tokens)
- 2026-09-10T19:12:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:14:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Rebased onto accepted main repair dc84676e and committed bounded closing-review admission, durable persona launch identity, restart reconciliation, and accepted-evidence rebinding at 4f09530e. The affected retro suite passed 48 tests, related persona coverage passed 56 tests, Ruff and compilation passed; the single full-suite attempt reached 98% but timed out with one unidentified failure before its summary, so controller exact-head CI remains authoritative. cost=$3.39
- 2026-09-10T19:17:09+00:00 automated review requested changes: The durable initial preparation handoff works, but expensive closing-review work still occurs under the controller lock on later ticks. cost=$0.74
- 2026-09-10T19:33:17+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T19:58:55+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T19:59:38+00:00 dispatched revise run 20260910T195937Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24746 tokens)
- 2026-09-10T20:07:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:09:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Extended the durable out-of-lock handoff to deferred persona launches and reconciliation preparation. Verified current-head lock release, restart identity reuse, quota recovery, lint, compilation, and diff integrity at commit 2331c432. cost=$1.84
- 2026-09-10T20:13:17+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: survive process restarts, concurrent r; run `garden triage CG-529 --changes "<feedback>" to unblock`
- 2026-09-10T20:46:39+00:00 triage: changes requested by hand: Correct the specific new review200931-2 finding at2331c432: split automatic reconcile PREPARATION from LAUNCH. Prepare i
- 2026-09-10T20:53:14+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T20:54:33+00:00 dispatched revise run 20260910T205433Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25025 tokens)
- 2026-09-10T21:01:36+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T21:02:53+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Closing-review reconciliation now prepares immutable inputs outside the controller lock, then reloads the durable claim and revalidates accepted source and stabilization evidence before committing and launching the exact input. Verified at d3d10bce with 52 retro tests, clean Ruff lint, Python compilation, and diff integrity. cost=$1.97
- 2026-09-10T21:05:19+00:00 automated review requested changes: The reconciliation race is fixed, but initial automatic persona launch still has a source-identity race that can duplicate model work. cost=$0.61
- 2026-09-10T21:57:08+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T21:57:38+00:00 dispatched revise run 20260910T215738Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25227 tokens)
- 2026-09-10T22:26:33+00:00 revision failed: worker idle 20 min (no output or file change)
- 2026-09-10T22:59:03+00:00 dispatched work run 20260910T225903Z-work via manual [human] (fresh session, base main, ~24358 tokens)
- 2026-09-10T22:59:04+00:00 external PR attached at garden/cg-529-automatically-start-the-phase-closing-review-whe; existing CI is PENDING
- 2026-09-10T22:59:36+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/retro.py); a rebase agent will resolve it
- 2026-09-10T22:59:43+00:00 dispatched rebase run 20260910T225942Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3859 tokens)
- 2026-09-10T23:19:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Rebased CG-529 onto origin/main and resolved the retro, auxiliary dispatch, and persona conflicts while preserving both sides' intent. cost=$0.03
- 2026-09-10T23:24:07+00:00 CI failure
- 2026-09-10T23:43:45+00:00 triage: changes requested by hand: One bounded correction for the new durable automatic-review convergence/retry defect. Recognize and validate the existin
- 2026-09-10T23:47:44+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T23:48:15+00:00 dispatched revise run 20260910T234814Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25856 tokens)
- 2026-09-11T00:01:39+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T00:12:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Existing durable closing-review requests are now recognized before configuration required only for creating a new request, restoring manual/automatic convergence and failed-persona retries. Verified at eaf18ab7 with 54 retro tests, Ruff, Python compilation, and clean diff/conflict checks; controller exact-head CI remains the merge gate. cost=$0.67
- 2026-09-11T00:24:23+00:00 CI failure
- 2026-09-11T00:44:41+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-11T00:45:11+00:00 dispatched revise run 20260911T004511Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25861 tokens)
- 2026-09-11T01:33:46+00:00 discovered work filed: CG-618
- 2026-09-11T01:33:46+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T01:54:16+00:00 check did not run (20260911T013351Z-check): idle 20 min (no output or file change); will retry
- 2026-09-11T02:04:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Rebased onto accepted main and fixed the brief-publication regression by waiting for authoritative supervisor completion before asserting complete content. The isolated regression, 54 retro tests, Ruff, compilation, and diff checks pass at 16d596d8; the full suite reported 2759 passed with one unrelated environment failure reproduced on origin/main. cost=$1.71
- 2026-09-11T02:08:27+00:00 triage: marked ready for review (The committed correction has passing exact CI34551175473/34551172153. Original failed-CI finding rem)
- 2026-09-11T02:08:46+00:00 automated review requested changes: Deferred persona launches still have a source-identity race, and current-head CI is not passing/verified. cost=$0.49
- 2026-09-11T02:26:57+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-11T02:26:58+00:00 One bounded correction for the new deferred-persona source/capacity revalidation race. Preserve full review and all lifetime counts. Its admitted eaf18ab7 CI reference was stale: actual16d596d8 CI34551175473/34551172153 passed; that does not resolve the substantive source race.
- 2026-09-11T02:27:33+00:00 dispatched revise run 20260911T022733Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~26381 tokens)
- 2026-09-11T02:56:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T03:02:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Deferred closing-review personas now use source-bound preparation, locked source/evidence/capacity revalidation, durable exact-run commits, and out-of-lock launch. Verified commit 289e25a6 with 55 passing retro tests, clean Ruff/compilation/diff checks; the single full-suite attempt reported 2760 passed and one unrelated tests/test_validation.py policy failure, so controller exact-head CI remains the merge gate. cost=$2.48
- 2026-09-11T03:03:07+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/persona.py); a rebase agent will resolve it
- 2026-09-11T03:03:10+00:00 dispatched rebase run 20260911T030309Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~5074 tokens)
- 2026-09-11T03:16:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/452: Rebased CG-529 onto origin/main and resolved all textual conflicts while preserving both sides' intent. cost=$0.03
- 2026-09-11T03:28:12+00:00 automated review requested changes: The implementation and race-focused coverage appear coherent, but merge eligibility is not established because exact-head CI for b13354e997a9f612ce275fc101b7c126c0791028 remains pending. cost=$0.65
- 2026-09-11T03:36:35+00:00 triage: marked ready for review (Exact current b13354e9 CI34557420522 and34557417409 both passed. Preserve the original CI-pending re)
- 2026-09-11T03:48:45+00:00 automated review: approve — Automatic phase-closing reviews are durably queued, admission-controlled, source/evidence fenced, restart-safe, and advanced through the existing retro lifecycle. No blocking defect found. cost=$0.69
- 2026-09-11T03:54:00+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T04:16:09+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/452
