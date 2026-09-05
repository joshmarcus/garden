---
id: CG-191
title: The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-03
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T10:26:55+00:00'
---

## Goal

**User value:** an approved green hard-tier PR merges without a person, so the queue is shown working live on a batch and hand merges fall from twelve to zero.

**Why now:** twelve of thirty phase-03 merges were by hand, eight when the queue rotated and four on hard-tier PRs; the operator already asked for this policy.

**Size:** medium. **Depends on:** CG-176 (merged); a config key such as merge.hard_tier: two_rounds that a team can turn off, default on (the owner decided on 2026-09-05 that the queue may merge hard-tier PRs).

## Context

Proposed at the context-garden/phase-03 retro. The queue exists but half the merges still need a button; this closes the phase-03 promise the personas say is only half kept.
