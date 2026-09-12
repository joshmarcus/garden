---
id: CG-409
title: Finish manual work pushed from another machine without a local authoring checkout
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-409-finish-manual-work-pushed-from-another-machine-w
pr: https://github.com/joshmarcus/context-garden/pull/313
runner: local
attempts: 1
last_dispatched_at: '2026-09-08T12:40:14+00:00'
created: '2026-09-07T20:05:52+00:00'
updated: '2026-09-08T17:24:15+00:00'
---

## Goal

Finish manual work pushed from another machine without a local authoring checkout. Recheck current implementation before choosing the smallest compatible change.

## Acceptance criteria

- [ ] Add an explicit remote-manual completion contract or pushed-result option; preserve existing local manual completion behavior.
- [ ] Fetch and materialize the declared repository, branch and exact pushed SHA through existing remote-result handling before validation. Reject missing refs, wrong repository, stale SHA and unauthorized branch replacement.
- [ ] Complete work authored in a separate clone with no local commits, then perform independent current-head checks/review. Preserve truthful no-change and failure handling, provenance and recovery after controller restart.
- [ ] Reconcile with CG-158 and CG-362 rather than duplicating external-completion logic. Do not treat a user-provided success claim as approval.

## Provenance and scope

Owner-provided additional gap F1, 2026-09-07. Generic requirements only. This task remains a phase-07 draft and does not authorize new access, deployment or external notifications. Refer to the shared spec, not the private environment survey.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T12:39:03+00:00 Operator continuation: route this next eligible Phase07 P0 task to the existing four-host AWS pool as capacity frees; keep current 4 AWS + 1 local total and 20:00UTC deadline.
- 2026-09-08T12:40:14+00:00 dispatched work run 20260908T124014Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~8578 tokens)
- 2026-09-08T13:02:29+00:00 opened https://github.com/joshmarcus/context-garden/pull/313 (base main): Added an explicit pushed-result contract for manual work authored in another clone. The scheduler now verifies repository, claimed branch, exact remote SHA, and branch continuity before materializing the head and entering ordinary checks, PR creation, and independent review. cost=$3.36
- 2026-09-08T14:01:26+00:00 check did not run (20260908T140125Z-check): idle 61 min (no output or file change); will retry
- 2026-09-08T14:02:41+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:04:01+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:05:16+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:06:29+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:07:42+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:07:46+00:00 re-enabled by hand; revise run will follow
- 2026-09-08T14:08:59+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:10:14+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:11:25+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:12:39+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:13:53+00:00 check did not run (20260908T140126Z-check-2): idle 62 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:15:01+00:00 triage: marked ready for review (Both exact source CI runs pass. Recover the unexecuted controller-local replay with the correct loca)
- 2026-09-08T14:15:04+00:00 check did not run (20260908T141501Z-check): check run produced no results; will retry
- 2026-09-08T14:16:15+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:17:28+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:18:39+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:19:50+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:21:03+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:22:14+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:23:34+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:24:53+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:26:06+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:26:26+00:00 triage: marked ready for review (Corrected operator launch environment to live service user-owned runtime directory; replay and revie)
- 2026-09-08T14:27:24+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:29:18+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:30:36+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:31:49+00:00 check did not run (20260908T141504Z-check): idle 75 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:32:10+00:00 triage: marked ready for review (Stale completed check retired; real current-head replay/review remains queued with corrected local r)
- 2026-09-08T14:39:39+00:00 automated review: approve — The pushed-result contract verifies and materializes the configured remote branch at the declared exact SHA before entering existing checks and independent review. Focused current-head tests, legacy manual regressions, lint, and the disposable scheduler replay pass. cost=$0.39


## Operator review continuation, 2026-09-08T15:59:43.847292+00:00

Current6525e59 first review approved and CIpassed. The second required round had no queued request. Public review action deferred at local1/1 and did not persist it; queued the required round through the scheduler review-queue API without starting an extra process or changing the resource limit.
- 2026-09-08T16:03:18+00:00 automated review requested changes: The pushed-result implementation passes focused tests, lint, and exact-head CI. The required served-app evidence is blocking because the supplied replay exercises unrelated generic dispatch/reap behavior rather than pushed-result completion and recovery. cost=$0.40
- 2026-09-08T17:24:15+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/313
