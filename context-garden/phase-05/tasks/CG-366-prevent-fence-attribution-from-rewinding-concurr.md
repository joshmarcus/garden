---
id: CG-366
title: Prevent fence attribution from rewinding concurrent worker logs
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading: []
branch: garden/cg-366-prevent-fence-attribution-from-rewinding-concurr
pr: https://github.com/joshmarcus/context-garden/pull/256
attempts: 1
last_dispatched_at: '2026-09-07T02:31:24+00:00'
created: '2026-09-07T02:04:01+00:00'
updated: '2026-09-07T02:51:31+00:00'
---

## Goal

Stop legitimate concurrent worker output from being attributed to another worker and destructively restored from an old fence snapshot. Preserve real write-escape detection and trusted manifest checks.

## Incident and source evidence

At2026-09-07 02:00:16 UTC, CG365 run20260907T015006Z-revise-2 was failed by the installedfc658809 fence after successful implementation/CI. It reported reverting sibling CG323 run014143/stdout.json and CG332 run015006/stdout.json. The CG365 resource evidence commands inspect processes/read-only data, and emitted output contains other process command lines. _worker_named searches the ENTIRE raw transcript for a full path, including tool output and prose. _fence_guard_targets snapshots mutable sibling outputs as config=True; _fence_guard_check treats a changed hash plus mention as proof of a write and writes the old bytes back. This confuses observation with causation and can destroy concurrently appended audit history. Operator preserved available transcripts/run manifests before further intervention under /home/joshua/work/operator-test-tmp/fence-concurrency-20260907T0203; do not mutate that evidence or production logs.

Ordinary dispatch is temporarily paused for this distinct integrity incident, not because memory is unhealthy. Existing workers were preserved. Source starts from current main; resource workCG365/PR249 ataf21cb846357197f856954befdeaa53c42e9cb05 must remain preserved for later review. Do not retry or edit that task/worktree from this worker.

## Acceptance criteria

- [ ] A read-only command or tool result/prose mentioning another active run's path cannot make its normal append/update a write violation. Cover the actual Codex JSONL observation shape and supported Claude shapes. Attribution uses explicit write evidence, not arbitrary substring occurrence in echoed command output or final prose. Keep a clear honest boundary for commands whose write effect cannot be established.
- [ ] Never rewind mutable live sibling stdout/stderr/run evidence from an old snapshot on ambiguous attribution. Preserve suspected changes and recovery evidence for inspection; actual explicit forbidden writes remain blocked/flagged. Cover two overlapping runs where the innocent observer finishes after the sibling appends, and verify the sibling's exact latest bytes remain intact. Do not broadly disable fences, remove trusted manifest verification, or exempt actual forged approvals/config/state writes.
- [ ] Regression coverage proves explicit forbidden sibling/config writes still produce a meaningful failure without clobbering unrelated concurrent scheduler/worker updates. Existing trusted-manifest corruption and root/worktree escape tests remain passing. Treat old in-flight manifests safely as well as newly created ones.
- [ ] Focused local fence tests/lint pass serially within existing limits, then exact-final-head full GitHub CI passes. Document the narrow fix and containment/recovery semantics. Self-review and fix findings internally; report ordinary acceptance evidence. No local full suite or parallel model agents.

## Safety and scope

Do not change production services, live state/task statuses, audit files or fence manifests. Do not apply a broad fence bypass. Do not run read/probe commands across production process trees merely to reproduce a known transcript pattern: use disposable fixture data. Preserve dirty/unrelated files with named salvage. Worker handles product code/tests only; operator owns incident recovery, verifying other logs and deploying after accounted drain. Keep this patch narrow; do not bundle resource-isolation changes fromCG365.

## Provenance

Priority0 incident repair after observed destructive false attribution. Existing CG291 introduced control/sibling protections; CG344 owns trusted manifests. Preserve those contracts while fixing attribution and non-destructive concurrent recovery.

## Log

- 2026-09-07T02:04:39+00:00 Operator02:06 UTC filed and approved urgent isolated repair. Existing workers and available logs preserved; general admission paused for new integrity risk.
- 2026-09-07T02:04:39+00:00 approved (cli)
- 2026-09-07T02:06:56+00:00 dispatched work run 20260907T020637Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9696 tokens)
- 2026-09-07T02:18:38+00:00 preserved uncommitted worktree changes from run 20260907T020637Z-work outside the PR: `git stash apply 0a0665ab2aafee914c1ccf736697c8dffee27cde` in /home/joshua/work/worktrees/CG-366 (garden:CG-366:20260907T020637Z-work:reap)
- 2026-09-07T02:21:18+00:00 opened https://github.com/joshmarcus/context-garden/pull/256 (base main): Fence attribution now relies on structured write evidence instead of arbitrary transcript substrings, preventing read-only observations and prose from implicating concurrent workers. Mutable sibling run evidence is never rewound from stale snapshots, while explicit forbidden writes and trusted-manifest corruption remain blocked and reported. cost=$1.64
- 2026-09-07T02:23:10+00:00 automated review requested changes: Structured event filtering and non-destructive sibling-log handling are sound, but shell attribution still treats every path in any mutating command as a write target. This can falsely fail workers and restore unrelated concurrent config changes. cost=$0.31
- 2026-09-07T02:31:24+00:00 dispatched revise run 20260907T023123Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10448 tokens)
- 2026-09-07T02:46:40+00:00 preserved uncommitted worktree changes from run 20260907T023123Z-revise outside the PR: `git stash apply b88f06064b695bf0224e5514e0c05a502cff90c0` in /home/joshua/work/worktrees/CG-366 (garden:CG-366:20260907T023123Z-revise:reap)
- 2026-09-07T02:47:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/256: Shell fence attribution now identifies only explicit destination paths instead of treating every path in a mutating command as written. Claude and Codex regressions cover guarded source/input operands, while explicit forbidden destinations remain detected and concurrent sibling evidence remains non-destructive. cost=$1.55
- 2026-09-07T02:49:01+00:00 automated review: approve — Structured write attribution prevents observed paths and prose from implicating concurrent workers, while preserving explicit-write failures and trusted fence checks. Mutable sibling evidence remains intact, and all required verification passes. cost=$0.30
- 2026-09-07T02:50:11+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-07T02:50:20+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T02:51:31+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/256
