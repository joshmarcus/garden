---
id: CG-306
title: 'Update docs: docs/design.md'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading:
- docs/design.md
- docs/roadmap.md
- docs/architecture.md
- docs/worker-protocol.md
branch: garden/cg-306-update-docs-docs-design-md
pr: https://github.com/joshmarcus/context-garden/pull/280
discovered_from: kickoff:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-07T07:37:41+00:00'
created: '2026-09-06T00:07:47+00:00'
updated: '2026-09-07T09:56:40+00:00'
---

## Goal

Update `docs/design.md`'s Non-goals section: it still lists 'automatic merging' as a non-goal, but the loop already automerges. (`docs/roadmap.md` has the same stale claim; that file is out of scope for this task.)

## Context

Raised at the context-garden/phase-05 kickoff; needed by CG-295, CG-265, CG-275.

## Acceptance criteria

- [ ] docs/design.md's Non-goals section no longer lists "automatic merging" as a non-goal; verified by `grep -n "automatic merging" docs/design.md` showing no match under Non-goals.
- [ ] docs/design.md's description of the review/merge loop states that merging is automatic, consistent with the loop behavior described in docs/architecture.md.
- [ ] docs/roadmap.md is left untouched by this task; its own stale non-goal reference, if present, stays out of scope here.
- [ ] The rest of docs/design.md's structure and unrelated non-goals are preserved; the diff is limited to the automatic-merging line(s).

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002118Z-edit) cost=$0.07
- 2026-09-06T00:24:06+00:00 approved (cli)
- 2026-09-07T07:37:41+00:00 dispatched work run 20260907T073719Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11954 tokens)
- 2026-09-07T07:46:55+00:00 preserved uncommitted worktree changes from run 20260907T073719Z-work outside the PR: `git stash apply b1ff507467bd36ea8b20f16da1c166c90295cd4b` in /home/joshua/work/worktrees/CG-306 (garden:CG-306:20260907T073719Z-work:reap)
- 2026-09-07T07:49:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/280 (base main): Updated docs/design.md to reflect automatic PR merging and removed automatic merging from Non-goals. Required lint, targeted assertions, and exact-commit CI passed. cost=$0.04
- 2026-09-07T09:13:25+00:00 automated review: approve — All acceptance criteria are met. The focused documentation change is consistent with docs/architecture.md and the PR description clearly states the outcome, motivation, verification, and roadmap follow-up. cost=$0.19
- 2026-09-07T09:26:40+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T09:44:25+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T09:45:26+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T09:56:40+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/280
