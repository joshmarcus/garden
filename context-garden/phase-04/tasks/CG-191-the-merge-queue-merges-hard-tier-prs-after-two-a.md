---
id: CG-191
title: The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 1
difficulty: medium
reading: []
branch: garden/cg-191-the-merge-queue-merges-hard-tier-prs-after-two-a
pr: https://github.com/joshmarcus/context-garden/pull/135
discovered_from: retro:context-garden/phase-03
attempts: 1
last_dispatched_at: '2026-09-05T11:51:09+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T12:12:15+00:00'
---

## Goal

**User value:** an approved green hard-tier PR merges without a person, so the queue is shown working live on a batch and hand merges fall from twelve to zero.

**Why now:** twelve of thirty phase-03 merges were by hand, eight when the queue rotated and four on hard-tier PRs; the operator already asked for this policy.

**Size:** medium. **Depends on:** CG-176 (merged); a config key such as merge.hard_tier: two_rounds that a team can turn off, default on (the owner decided on 2026-09-05 that the queue may merge hard-tier PRs).

## Context

Proposed at the context-garden/phase-03 retro. The queue exists but half the merges still need a button; this closes the phase-03 promise the personas say is only half kept.

## Log

- 2026-09-05T10:31:16+00:00 approved (web)
- 2026-09-05T11:51:09+00:00 dispatched work run 20260905T115101Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou stacked on CG-197, ~4516 tokens)
- 2026-09-05T11:55:55+00:00 parent CG-197 merged; will rebase onto main when the current run finishes
- 2026-09-05T12:08:16+00:00 parent CG-197 merged; rebased onto main and retargeted the PR
- 2026-09-05T12:10:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/135 (base main): Added github.automerge_hard_tier (default on): hard-tier PRs now automerge after two approving review rounds and the garden's own scratch-merge check — the pre-PR suite run on the branch rebased onto the base tip in a throwaway worktree, dispatched as a detached scratch_merge check run and recorded keyed to the reviewed diff. Full suite green (608 passed), lint clean, 10 new tests. cost=$6.73
- 2026-09-05T12:12:15+00:00 automated review: approve — Hard-tier automerge behind github.automerge_hard_tier (default on) with two-round and scratch-merge gates; all acceptance criteria met, logic sound, scope clean, tests and lint green. cost=$0.73
