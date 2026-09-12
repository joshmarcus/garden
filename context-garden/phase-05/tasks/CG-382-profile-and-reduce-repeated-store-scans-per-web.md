---
id: CG-382
title: Profile and reduce repeated Store scans per web request
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/store.py
branch: garden/cg-382-profile-and-reduce-repeated-store-scans-per-web
pr: https://github.com/joshmarcus/context-garden/pull/292
discovered_from: CG-380
attempts: 1
last_dispatched_at: '2026-09-08T02:20:31+00:00'
created: '2026-09-07T13:02:16+00:00'
updated: '2026-09-08T17:27:18+00:00'
file: src/garden/store.py
error: Task/product scanning averaged about 52ms on Now and Inbox, roughly 40% of request CPU, and was
  the largest named controller span.
---

Instrument Store scanning on the retained-history fixture to count filesystem stats and YAML parses per page request. If repeated work is confirmed, reuse one immutable request-local snapshot while preserving cross-process freshness and compare matched page latency before and after.

## Provenance

Discovered by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`.
## Log
- 2026-09-07T13:02:16+00:00 discovered by CG-380
- 2026-09-07T13:03:31+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:04:53+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:06:07+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:07:21+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:08:35+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:09:48+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:03+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:29+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:39+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:12:55+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:14:13+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:15:32+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:16:55+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:18:20+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`

## Acceptance criteria

- [ ] Preserve exact build, fixture size, commands, sample counts and matched before/after evidence for the proposed mechanism. Distinguish measured savings from hypotheses.
- [ ] Retain data freshness and existing hard caps/pressure safeguards. All load experiments use disposable bounded environments; no production cache deletion, pressure injection, or cap relaxation.
- [ ] Report a narrow justified fix or explicit evidence-backed disposition; focused regression tests and exact-head CI for code changes. Self-review and repair findings before completion.
- 2026-09-07T13:19:06+00:00 approved (operator-incident-followup)
- 2026-09-07T13:19:45+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:21:10+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:22:36+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:24:01+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:25:27+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:26:42+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:27:57+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:29:10+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:30:25+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:31:40+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:32:56+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:34:12+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:35:29+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:36:59+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:44:03+00:00 dispatched work run 20260907T134402Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10490 tokens)
- 2026-09-07T14:09:14+00:00 preserved uncommitted worktree changes from run 20260907T134402Z-work outside the PR: `git stash apply a1ce9eb772952206881ef7927e63c4ba4f37dc07` in /home/joshua/work/worktrees/CG-382 (garden:CG-382:20260907T134402Z-work:reap)
- 2026-09-07T14:12:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/292 (base main): Web requests now use one fresh request-local Store snapshot, eliminating repeated discovery scans while preserving next-request freshness and the scheduler's config reload gate. A retained-task regression profile records matched scan, YAML parse, stat, and latency evidence. cost=$1.30
- 2026-09-07T15:29:27+00:00 automated review requested changes: Request changes because the required served scalability replay is unavailable and the committed test does not cover the validation plan’s larger histories, repeated expiry intervals, or concurrent executing processes. The implementation otherwise passes focused tests, lint, and exact-head CI. cost=$0.36
- 2026-09-07T16:37:55+00:00 Temporary operator incident admission hold to reserve next drained slot for P0 CG385 recovery; preserve all work. Restore original runner from docs/incidents/cg385-recovery-admission-holds.json after CG385 starts.
- 2026-09-07T16:39:06+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-382`) or send it back (`garden triage CG-382 --changes "..."`)
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.
- 2026-09-07T18:59:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T18:59:47+00:00 Delegated operator Inbox audit: cleared stale manual-hold stop after verified normal runner restoration; existing implementation, PR and pending review feedback retained. No owner decision required.
- 2026-09-08T02:20:31+00:00 dispatched revise run 20260908T022028Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12897 tokens)
- 2026-09-08T03:12:05+00:00 Owner shutdown: 20260908T022028Z-revise interrupted; preserve worktree and saved artifacts. No resume without owner instruction.
- 2026-09-08T03:28:04+00:00 preserved uncommitted worktree changes from run 20260908T022028Z-revise outside the PR: `git stash apply 2568f63afe8ed054d686c6bc4b885f13deb56ba2` in /home/joshua/work/worktrees/CG-382 (garden:CG-382:20260908T022028Z-revise:reap)
- 2026-09-08T03:28:04+00:00 revision failed: worker exited -15:
- 2026-09-08T12:35:50+00:00 triage: changes requested by hand: Operator audit: preserved interrupted localff71d1f and fast-forwarded to existing remotef1f8c0d. Continue useful existin
- 2026-09-08T12:35:50+00:00 Delegated operator Inbox review: preserved PR/worktree and queued one concrete continuation within current 4 AWS + 1 local limits.
- 2026-09-08T17:27:18+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/292
