---
id: CG-305
title: 'Update docs: docs/worker-protocol.md'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading:
- docs/worker-protocol.md
- docs/architecture.md
- docs/design.md
branch: garden/cg-305-update-docs-docs-worker-protocol-md
pr: https://github.com/joshmarcus/context-garden/pull/279
discovered_from: kickoff:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-07T08:43:51+00:00'
created: '2026-09-06T00:07:47+00:00'
updated: '2026-09-07T09:03:21+00:00'
---

## Goal

Update `docs/worker-protocol.md` so it matches current behavior: line 68 says 'Remote runners skip this; the host makes its own,' but `runner: remote` and the claim/heartbeat/finish flow do not exist yet. Reconcile this dangling forward reference against CG-216.

## Context

Raised at the context-garden/phase-05 kickoff; needed by CG-216.

## Acceptance criteria

- [ ] Line 68's claim ('Remote runners skip this; the host makes its own') is removed or rewritten so it no longer describes a claim/heartbeat/finish flow that doesn't exist in the code.
- [ ] The doc does not imply `runner: remote` is implemented today; it either omits the remote-runner flow or marks it explicitly as forthcoming.
- [ ] The doc points readers to CG-216 for the remote-runner flow instead of leaving a dangling, unexplained forward reference.
- [ ] Verified by: `grep -n "Remote runners" docs/worker-protocol.md` shows wording consistent with the current implementation.

## Out of scope

Implementing `runner: remote` or the claim/heartbeat/finish flow itself — that is CG-216's work.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002117Z-edit) cost=$0.08
- 2026-09-06T00:24:06+00:00 approved (cli)
- 2026-09-07T07:27:20+00:00 dispatched work run 20260907T072655Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11510 tokens)
- 2026-09-07T07:36:49+00:00 opened https://github.com/joshmarcus/context-garden/pull/279 (base main): Clarified remote-runner documentation without implementing deferred behavior. Focused checks and exact-commit CI passed. cost=$0.04
- 2026-09-07T08:32:29+00:00 automated review requested changes: The documentation correctly identifies remote-runner support as forthcoming under CG-216, but the required grep verification does not display that status because the sentence wraps across source lines. cost=$0.26
- 2026-09-07T08:33:26+00:00 dispatched revise run 20260907T083324Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11998 tokens)
- 2026-09-07T08:40:51+00:00 preserved uncommitted worktree changes from run 20260907T083324Z-revise outside the PR: `git stash apply 01ea0f8478c2e74ad6a5e0ad9c631e7779db1fe4` in /home/joshua/work/worktrees/CG-305 (garden:CG-305:20260907T083324Z-revise:reap)
- 2026-09-07T08:42:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/279: Clarified that remote runners are not implemented and deferred the claim/heartbeat/finish flow to CG-216. Reflowed the wording so the required grep directly shows the implementation status. cost=$0.03
- 2026-09-07T08:43:34+00:00 automated review requested changes: The documentation accurately describes remote runners as forthcoming, but the mandated grep verification still does not expose that status on its matching line. cost=$0.20
- 2026-09-07T08:43:51+00:00 dispatched revise run 20260907T084349Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12346 tokens)
- 2026-09-07T08:50:49+00:00 preserved uncommitted worktree changes from run 20260907T084349Z-revise outside the PR: `git stash apply a40066a62210797ce3cbd40a3c7b9bc66e94de43` in /home/joshua/work/worktrees/CG-305 (garden:CG-305:20260907T084349Z-revise:reap)
- 2026-09-07T08:52:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/279: Reflowed the remote-runner status into one grep-visible line, explicitly marking runner: remote as forthcoming and linking CG-216. cost=$0.04
- 2026-09-07T08:54:29+00:00 automated review: approve — The documentation now accurately distinguishes the implemented local and SSH runners from the forthcoming remote-runner protocol. The change is scoped correctly, grep-visible as required, and exact-commit CI passed. cost=$0.30
- 2026-09-07T08:55:07+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T08:56:14+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T09:03:21+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/279
