---
id: CG-480
title: Make Inbox recovery prompts actionable and distinguish operator work from user decisions
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/human.py
- src/garden/web/pages/inbox.py
- src/garden/web/actions/tasks.py
- src/garden/web/templates/inbox.html
branch: garden/cg-480-make-inbox-recovery-prompts-actionable-and-disti
pr: https://github.com/joshmarcus/context-garden/pull/378
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T00:59:59+00:00'
created: '2026-09-09T13:25:37+00:00'
updated: '2026-09-10T01:18:07+00:00'
---

## Goal

Recurring Inbox prompts must make it clear what happened, whether the user has a meaningful decision to make, and what each available action will actually do. Route routine technical recovery to the operator/agent instead of repeatedly presenting an unexplained needs-human stop.

## Owner request and example

The owner reports that these issues come up all the time and it is never clear what to do or whether the prompt is meaningful. CG230 currently combines an automatic lint check that timed out twice, failing PR tests, merge conflicts and an older review under a generic needs-human card offering Nothing to fix, resume / Continue the loop / Discuss / Cancel. That asks the user to reason about internal recovery without explaining the consequences.

## Acceptance criteria

- [ ] Classify the concrete reason for attention: interrupted infrastructure/check execution, actual source or CI failure, stale bookkeeping, normal pending work, explicit hold, or an unresolved product/access/budget decision. Support combined blockers without conflating their causes. Use current run/PR/head evidence and label historical or unavailable evidence honestly.
- [ ] Every actionable card plainly states what happened, why progress stopped, the effect on the task, who owns the next step, and a recommended next action. Explain whether the user needs to decide anything. Show concise evidence with links to the relevant current run, failed check, review and PR; do not make raw internal IDs and stack/error text the main explanation.
- [ ] Route routine technical recovery and implementation failures to the appropriate operator/agent or existing-source author continuation under existing authority and bounds. Show recovery ownership, progress and outcome. Ask the user only when an actual unresolved decision requires them. Repeated unchanged errors must not repeatedly demand the same human response or start duplicate work.
- [ ] Label actions by their concrete effect, such as Retry the interrupted check or Send failures to the worker, with a short explanation of what is preserved and what will run. Do not offer an unqualified Nothing to fix, resume when a failed prerequisite, substantive review finding or conflict remains. Keep destructive/cancel actions distinct from normal recovery.
- [ ] Reuse the existing decision/recovery machinery, including CG471 atomic check recovery and CG477 deep-dive investigation where appropriate. A requested recovery must be guarded against stale heads, active runs and repeat clicks. Preserve original errors, review findings, counters, source/results and explicit owner/phase holds. Merely assigning ownership must not falsely mark the problem resolved or claim a check passed.
- [ ] Clear or update a card when its actual prerequisite or decision is resolved, and preserve a readable history of the cause and action. Explain why an item remains if another independent blocker still applies.
- [ ] Verify representative rendered flows with targeted tests: CG230-style interrupted check plus source failures, a plain recoverable check interruption, a stale resolved stop, an explicit owner hold, and a genuinely user-owned decision. Confirm both clear wording and the actual action/ownership transition; preserve active work and avoid generic retries or CI bypasses.

## Scope and evidence

Fix the shared Inbox/decision presentation and routing contract, not only CG230 wording. Do not create a competing scheduler or duplicate CG471/CG477. Evidence: /home/joshua/work/operator-test-tmp/cg230-inbox-20260909 and the associated phase07 friction report. Implement in phase05 as a core operator-usability correction.

## Log

- 2026-09-09T13:25:37+00:00 approved (owner explicitly requested an issue for recurring unclear and potentially meaningless Inbox recovery prompts)
- 2026-09-09T13:47:53+00:00 dispatched work run 20260909T134753Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23852 tokens)
- 2026-09-09T14:05:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:06:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/378 (base main): Inbox recovery cards now distinguish user decisions from operator-owned recovery, explain cause/effect/ownership, preserve independent blockers, and provide concrete guarded actions. Committed as caa1dd04; 250 focused tests and Ruff passed. cost=$4.16
- 2026-09-09T14:25:18+00:00 automated review requested changes: Revision-cap stops are incorrectly presented as operator-owned even when delegated recovery is disabled, hiding a real user authorization decision. cost=$0.36
- 2026-09-09T14:27:32+00:00 dispatched revise run 20260909T142731Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25089 tokens)
- 2026-09-09T14:51:50+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:57:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Revision-cap cards now remain user-owned when delegated recovery is disabled and become operator-owned only when delegation is recorded. Fixed the decision-card walkthrough rendering and retry notice regressions; committed as 38accf6e after 110 focused Inbox/walkthrough tests, 78 attention/recovery tests, and Ruff passed. cost=$1.27
- 2026-09-09T15:06:33+00:00 automated review requested changes: Explicit holds awaiting owner authorization are shown as operator-owned and claim no user decision is required. cost=$0.47
- 2026-09-09T15:11:04+00:00 dispatched revise run 20260909T151104Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25225 tokens)
- 2026-09-09T15:18:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:22:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Explicit deployment holds awaiting owner approval now appear under Needs your decision with a concrete authorization action; routine deployment prerequisites remain operator-owned. Committed as 6b080fe8 and verified with 19 exact-head attention tests, a 132-test focused Inbox/web run, and clean Ruff lint. cost=$1.03
- 2026-09-09T15:22:25+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py, src/garden/scheduler/checkruns.py); a rebase agent will resolve it
- 2026-09-09T15:27:41+00:00 dispatched rebase run 20260909T152741Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2394 tokens)
- 2026-09-09T15:30:05+00:00 automated review: request_changes — The recovery presentation is substantially improved, but interrupted CI recovery is not actually guarded against stale PR heads. cost=$0.44
- 2026-09-09T15:58:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Rebased CG-480 onto origin/main and resolved all conflicts while preserving actionable recovery, stale-stop handling, deep-dive behavior, and owner authorization semantics. cost=$0.05
- 2026-09-09T16:14:36+00:00 automated review requested changes: Interrupted CI recovery remains insufficiently guarded against stale PR heads, and an applicable focused web test fails. cost=$0.44
- 2026-09-09T16:14:55+00:00 dispatched revise run 20260909T161455Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25821 tokens)
- 2026-09-09T16:23:01+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T16:24:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Interrupted CI recovery now persists its source head and verifies it against the live PR head before launching; missing, unavailable, or changed identity fails closed. Restored the rendered “Recover check and resume pipeline” contract; 334 focused tests and repository-wide Ruff lint passed on committed head c6ad15efa6b232920ddd54e81a886b2fef0993a5. cost=$1.04
- 2026-09-09T16:31:40+00:00 automated review requested changes: Recovery cards are substantially clearer, and guarded CI reruns now verify the live PR head. However, stale-success reconciliation can still clear an interrupted-check stop using success evidence from an older head. cost=$0.67
- 2026-09-09T16:32:31+00:00 dispatched revise run 20260909T163230Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~26322 tokens)
- 2026-09-09T16:39:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T16:41:24+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Guarded both stale-success recovery paths against changed or unavailable live PR heads. Matching heads still recover normally, while mismatches preserve the original stop, cached result, and continuation; committed as 66453c6d after 169 focused tests and clean Ruff lint. cost=$1.65
- 2026-09-09T16:44:13+00:00 automated review requested changes: Recovery cards are substantially clearer, but stale successful check evidence can still clear a stop when its original source head is unavailable. cost=$0.67
- 2026-09-09T17:33:09+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T17:35:08+00:00 dispatched revise run 20260909T173507Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~26316 tokens)
- 2026-09-09T17:41:12+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T17:43:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Terminal stale-success recovery now fails closed when the stopped check has no immutable source-head identity, even if mutable task state matches the live PR head. The original stop, cached result, and continuation remain preserved; 276 focused tests and repository-wide Ruff lint passed on commit c6411dcf874deb2454066fd8c1ee85e3ce42c1f3. cost=$0.73
- 2026-09-09T17:45:03+00:00 check did not run (20260909T174413Z-check): check execution did not complete

worker materialization failed during checkout preflight: warm checkout has unresolved index; preserved at /var/lib/garden-worker/work/preserved-materializations/CG-480/20260909T174413Z-check-7000c8c4c827; will retry
- 2026-09-09T17:45:54+00:00 feedback from an untrusted author ignored: Copilot: > @copilot resolve the merge conflicts in this pull request

Resolved by merging `origin/main` into this PR branch and fixing the conflict in `src/garden/scheduler/poll.py` while preserving CI phase-h
- 2026-09-09T17:45:54+00:00 1 new review item(s) + CI failure
- 2026-09-09T17:57:37+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T17:59:03+00:00 dispatched revise run 20260909T175859Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~26888 tokens)
- 2026-09-09T18:26:20+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T18:29:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Stale successful-check recovery now fails closed unless immutable check provenance matches the live PR head; mutable polling state can no longer clear the stop. Committed as b3db631e after 368 focused tests and repository-wide Ruff lint passed, with a clean worktree and no conflict markers. cost=$1.13
- 2026-09-09T18:33:03+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py); a rebase agent will resolve it
- 2026-09-09T18:33:17+00:00 dispatched rebase run 20260909T183314Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3770 tokens)
- 2026-09-09T18:52:25+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Rebased CG-480 onto origin/main and preserved both owner-hold presentation and guarded CI recovery behavior. cost=$0.02
- 2026-09-09T18:57:31+00:00 automated review requested changes: Recovery presentation is much clearer and the stale-head guards are sound, but cards remain actionable-looking when immutable check provenance is unavailable even though the actions fail closed. cost=$0.90
- 2026-09-09T19:26:40+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T20:07:51+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T20:08:14+00:00 dispatched revise run 20260909T200814Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~27280 tokens)
- 2026-09-09T23:54:03+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:55:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Inbox cards now identify missing immutable check provenance honestly and route it to a bounded operator investigation instead of offering recovery actions that must fail closed. Committed as 8105f5fb after 325 focused tests and repository-wide Ruff lint passed. cost=$1.08
- 2026-09-09T23:58:13+00:00 automated review requested changes: Recovery and stale-head handling are substantially improved, but launching the new operator investigation immediately turns it back into a user-owned decision card. cost=$0.57
- 2026-09-09T23:58:25+00:00 dispatched revise run 20260909T235825Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~27608 tokens)
- 2026-09-10T00:03:19+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T00:04:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Pending investigations now derive ownership, status, recommendation, and actions from durable investigation state. Verified the post-action Inbox remains operator-owned with no user decision required; 253 focused tests and repository-wide Ruff lint passed on commit b00a5687. cost=$0.75
- 2026-09-10T00:08:36+00:00 automated review requested changes: Plain interrupted-check cards expose both the guarded retry and a reconciliation action that can clear the failed prerequisite without rerunning it. cost=$0.59
- 2026-09-10T00:11:46+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T00:59:23+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T00:59:59+00:00 dispatched revise run 20260910T005959Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~28033 tokens)
- 2026-09-10T01:06:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:07:31+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/378: Plain interrupted-check cards now expose only the guarded retry that reruns the preserved continuation; they can no longer bypass the check through reconciliation. Committed as 6a8a0295 after 253 focused tests and repository-wide Ruff lint passed. cost=$0.67
- 2026-09-10T01:11:24+00:00 automated review: approve — Recovery cards clearly separate operator-owned repairs from user decisions, preserve independent blockers, and guard interrupted-check recovery against stale or unavailable source identity. cost=$0.42
- 2026-09-10T01:16:34+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T01:18:07+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/378
