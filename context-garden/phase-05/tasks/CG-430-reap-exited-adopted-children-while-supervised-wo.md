---
id: CG-430
title: Reap exited adopted children while supervised workers are still running
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 0
difficulty: hard
reading:
- src/garden/run_supervisor.py
- src/garden/validation.py
- tests/test_runners.py
- context-garden/docs/incident-protocol.md
branch: garden/cg-430-reap-exited-adopted-children-while-supervised-wo
pr: https://github.com/joshmarcus/context-garden/pull/319
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T00:53:08+00:00'
created: '2026-09-08T14:20:11+00:00'
updated: '2026-09-09T01:26:43+00:00'
---

## Goal

Keep adopted child processes reaped throughout a supervised worker's lifetime while preserving its exit status, descendant containment and validation-slot ownership.

## Incident evidence

During the 2026-09-08 13:56-14:02UTC web availability incident on rc5, many exited git grandchildren accumulated as zombies under the live CG-253 supervisor PID466322. WSL launches intermittently failed with Wsl/Service/0x8007274c and pages timed out after12-15seconds. The zombie population disappeared when that worker ended; the interface recovered without a restart. Memory pressure/high/max/OOM were zero. This correlation does not prove zombies were the sole cause of HTTP timeouts.

The installed `run_supervisor.main` calls `child.wait()` before its `os.waitpid(-1, WNOHANG)` loop, so it cannot reap adopted exits until the primary command finishes. This is a confirmed independent lifecycle defect. Compare the existing CG-382 request-scan work and CG-393 waiting-state repair; avoid duplicating their changes. Evidence is in /home/joshua/work/operator-test-tmp/web-incident-20260908T1356 and the incident/retrospective context docs.

## Acceptance criteria

- [ ] Reap exited adopted descendants promptly while the primary command remains alive, without stealing its exit status or waiting on unrelated processes.
- [ ] Preserve SIGTERM escalation, cleanup of live descendants, genuine nonzero exit codes and ownership of the validation slot until all owned live work ends.
- [ ] Add a small deterministic isolated subprocess regression that creates a few orphaned grandchildren and keeps the leader alive; prove those exits are reaped before leader completion. Keep load/stress workloads explicitly opt-in.
- [ ] Exercise the actual supervised validation entrypoint and collect bounded process/HTTP/CPU observations on a disposable fixture. Separate established causes from hypotheses about the September8 web outage.
- [ ] Record any remaining controller or WSL responsiveness issue with targeted diagnostic evidence rather than claiming this patch alone resolves the whole incident.

## Log

- 2026-09-08T14:20:11+00:00 approved (operator-incident-recovery)
- 2026-09-08T14:42:18+00:00 dispatched work run 20260908T144218Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18194 tokens)
- 2026-09-08T14:59:29+00:00 opened https://github.com/joshmarcus/context-garden/pull/319 (base main): The run supervisor now polls the primary command by PID while promptly reaping other adopted children, preserving exit status, signal escalation, descendant containment, and lease lifetime. Deterministic subprocess regressions and a bounded validation-entrypoint HTTP fixture passed. cost=$1.13
- 2026-09-08T15:33:22+00:00 check did not run (20260908T153317Z-check): idle 36 min (no output or file change); will retry
- 2026-09-08T15:36:13+00:00 automated review produced no verdict (idle 39 min (no output or file change))
- 2026-09-08T16:19:50+00:00 automated review requested changes: The supervisor now reaps exited adopted descendants while the leader remains active without consuming its status, and retains signal, cleanup, and validation-slot behavior. Focused tests, lint, and a disposable validation-entrypoint HTTP interaction passed; the broader WSL incident cause remains explicitly unresolved. cost=$0.29


## Operator verification scope clarification 2026-09-08T17:12:01.153329+00:00

All five frozen acceptance criteria were assessed met in review 20260908T161605Z-review. The sole blocking mechanical gap came from interaction.unverified containing the broader September8 WSL outage cause. That cause is explicitly outside this lifecycle repair and remains unresolved in the separate incident investigation. Reassess existing exact-head source and actual supervised HTTP/process evidence; keep this limitation in the report as an out-of-scope follow-up, not as an unperformed required interaction. Do not invent evidence, change the prior report, or spend an implementation revision only to relabel metadata.
- 2026-09-08T17:12:01+00:00 Operator requests scope clarification of existing passing acceptance evidence; unresolved incident cause retained separately.
- 2026-09-08T17:17:44+00:00 automated review: approve — The supervisor promptly reaps adopted exits while preserving leader status, termination escalation, descendant draining, and validation-slot ownership. Exact-head tests, lint, and a disposable supervised HTTP/process replay passed; the broader September 8 WSL incident remains correctly scoped as a separate investigation. cost=$0.62
- 2026-09-08T17:27:22+00:00 1 new review item(s)
- 2026-09-08T17:28:54+00:00 automated review: approve — The supervisor promptly reaps adopted exits while preserving leader status, termination escalation, descendant draining, and validation-slot ownership. Exact-head tests, lint, and a disposable supervised HTTP/process replay passed; the broader September 8 WSL incident remains correctly scoped as a separate investigation. cost=$0.31
- 2026-09-08T19:23:55+00:00 triage: marked ready for review (GitHub now publishes conflict-resolved ae7bb363; review exact current source, preserving prior appro)
- 2026-09-08T19:25:53+00:00 feedback from an untrusted author ignored: Copilot: > @copilot resolve the merge conflicts in this pull request

Resolved the merge conflict in `src/garden/run_supervisor.py` and finalized the two-parent merge commit `ae7bb36`. The adopted-child reapin
- 2026-09-08T19:25:53+00:00 1 new review item(s)
- 2026-09-08T19:43:50+00:00 triage: marked ready for review (External merge conflicts are resolved atae7bb363; approved pending Copilot CI workflows and queued c)
- 2026-09-08T19:50:42+00:00 automated review: approve — The supervisor promptly reaps adopted exits while preserving leader status, termination escalation, descendant draining, and validation-slot ownership. Exact-head tests, lint, and an inspectable disposable supervised HTTP/process replay passed; the broader September 8 WSL incident remains correctly scoped as a separate investigation. cost=$0.32
- 2026-09-08T21:43:51+00:00 dispatched revise run 20260908T214351Z-revise-2 via manual [human] (fresh session, base main, ~20544 tokens)
- 2026-09-08T21:45:26+00:00 external PR attached at garden/cg-430-reap-exited-adopted-children-while-supervised-wo; existing CI is PENDING
- 2026-09-08T21:59:03+00:00 automated review requested changes: The supervisor promptly reaps adopted exits while preserving leader status, termination escalation, descendant draining, and validation-slot ownership. Exact-head focused tests, lint, and the disposable served replay pass; the broader WSL incident remains a separate investigation. cost=$0.43
- 2026-09-08T22:05:29+00:00 triage: marked ready for review (All five actual criteria pass; execute missing current-head pre-check before repeating review. No ne)
- 2026-09-08T22:06:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/319: Removed the duplicated adopted-child regression introduced while integrating CG433. The retained version includes guaranteed release/cleanup and bounded wait; the separate nonzero leader-status/descendant regression remains. Both focused tests passed in0.56seconds and repository Ruff passed. Full current-head CI and automated review remain required.
- 2026-09-08T22:10:52+00:00 automated review requested changes: The supervisor promptly reaps adopted exits while preserving leader status, termination behavior, descendant draining, and validation-slot ownership. Exact-head focused tests, lint, and a disposable supervised HTTP/process replay pass; the broader September 8 WSL incident remains a separate investigation. cost=$0.37
- 2026-09-08T22:15:26+00:00 dispatched revise run 20260908T221525Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21496 tokens)
- 2026-09-08T22:33:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/319: Recorded durable supervised-validation interaction evidence with explicit HTTP methods, URLs, statuses, process-tree data, and bounded CPU observations. The exact committed head preserves adopted-child reaping and lifecycle behavior, passes six focused regressions, and passes repository lint. cost=$0.99
- 2026-09-08T22:38:33+00:00 automated review: approve — The supervisor promptly reaps adopted exits while preserving leader status, termination behavior, descendant draining, and validation-slot ownership. Current-head focused tests, lint, and the disposable supervised HTTP/process evidence pass; the broader September 8 outage remains a separate investigation. cost=$0.29
- 2026-09-08T22:44:35+00:00 CI failure
- 2026-09-08T22:45:26+00:00 dispatched revise run 20260908T224525Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21478 tokens)
- 2026-09-08T23:49:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/319: Isolated the adopted-child and nonzero-status subprocess regressions from the enclosing supervised validation lease, eliminating the reproducible self-wait. The focused regressions and lint pass at commit 9c8abca; the single full-suite attempt exceeded its 900-second bound after reaching 78%, and the GitHub actions lookup remains unavailable without authentication. cost=$2.01
- 2026-09-08T23:55:03+00:00 automated review: approve — The supervisor promptly reaps adopted exits while preserving leader status, termination behavior, descendant draining, and validation-slot ownership. Exact-head focused tests, lint, and a disposable supervised HTTP/process replay pass; the broader September 8 outage remains correctly scoped to separate investigation. cost=$0.31
- 2026-09-09T00:41:06+00:00 hard-tier scratch result recovered from false plain-rebase conflict: current base is an ancestor of the reviewed head, exact merge-tree is clean, two current-head CI runs pass, and current-head review approves; returned to the normal merge queue
- 2026-09-09T00:44:02+00:00 rebasing before merge; rebase onto main conflicts (src/garden/run_supervisor.py); a rebase agent will resolve it
- 2026-09-09T00:44:03+00:00 dispatched rebase run 20260909T004403Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3018 tokens)
- 2026-09-09T00:46:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/319: Rebased onto origin/main and resolved the run_supervisor.py conflict while preserving both sides' changes. cost=$0.01
- 2026-09-09T00:52:40+00:00 automated review requested changes: The supervisor promptly reaps adopted exits while preserving leader status, termination behavior, descendant draining, and validation-slot ownership. Exact-head focused tests, lint, and disposable supervised HTTP/process evidence pass; the broader September 8 outage remains a separate investigation. cost=$0.49
- 2026-09-09T00:53:08+00:00 dispatched revise run 20260909T005308Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23231 tokens)
- 2026-09-09T00:59:43+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/319: Refreshed the durable supervised-validation evidence against the reviewed source and added explicit affected, empty, failure, and recovery observations. The focused supervisor regressions and repository lint pass. cost=$0.58
- 2026-09-09T01:08:11+00:00 automated review: approve — The supervisor promptly reaps adopted exits while preserving leader status, termination behavior, descendant draining, and validation-slot ownership. Exact-head focused tests, lint, and disposable supervised HTTP/process evidence pass; the broader September 8 outage remains a separate investigation. cost=$0.31
- 2026-09-09T01:13:08+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T01:13:46+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T01:14:59+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T01:23:10+00:00 automated review: approve — The supervisor promptly reaps adopted exits while preserving leader status, termination behavior, descendant draining, and validation-slot ownership. Focused current-head tests, lint, and disposable supervised interaction evidence pass; the broader September 8 outage remains a separate investigation. cost=$0.43
- 2026-09-09T01:24:49+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T01:25:26+00:00 rebasing before merge; reviewed remote head already contains main; not rebased or pushed
- 2026-09-09T01:26:43+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/319
