---
id: CG-304
title: 'Update docs: docs/architecture.md'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading:
- docs/architecture.md
- src/garden/kickoff.py
- src/garden/scheduler/kickoff.py
- src/garden/profiles.py
- src/garden/runner/ssh.py
- src/garden/runner/manual.py
- src/garden/web/pages/api.py
branch: garden/cg-304-update-docs-docs-architecture-md
pr: https://github.com/joshmarcus/context-garden/pull/278
discovered_from: kickoff:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-07T08:21:30+00:00'
created: '2026-09-06T00:07:47+00:00'
updated: '2026-09-07T09:24:49+00:00'
---

## Goal

Update `docs/architecture.md`'s module map to add kickoff.py, scheduler/kickoff.py, profiles.py, runner/ssh.py, runner/manual.py and web/pages/api.py, and to reflect the remote runner and runs API added by CG-216.

## Context

Raised at the context-garden/phase-05 kickoff; needed by CG-216, CG-295, CG-275.

## Acceptance criteria

- [ ] Module map in docs/architecture.md lists kickoff.py, scheduler/kickoff.py, profiles.py, runner/ssh.py and runner/manual.py, each with a one-line description
- [ ] Module map lists web/pages/api.py and the remote runner and runs API surface added by CG-216
- [ ] Every path named in the module map exists in the product checkout, confirmed by diffing the map against the actual file tree (e.g. `git ls-files`)
- [ ] No module map entries reference files that have since been removed or renamed
- [ ] docs/architecture.md still renders correctly (headings and links intact) after the edit

## Out of scope

- Any documentation file other than docs/architecture.md
- Describing CG-216's remote runner/runs API design beyond naming it in the module map

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002116Z-edit) cost=$0.06
- 2026-09-06T00:25:04+00:00 approved (cli)
- 2026-09-07T07:26:54+00:00 dispatched work run 20260907T072631Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~19959 tokens)
- 2026-09-07T07:35:29+00:00 preserved uncommitted worktree changes from run 20260907T072631Z-work outside the PR: `git stash apply 6b3bc1b5ddd983e88fcbd6fe72d7072194fbc3e9` in /home/joshua/work/worktrees/CG-304 (garden:CG-304:20260907T072631Z-work:reap)
- 2026-09-07T07:36:46+00:00 opened https://github.com/joshmarcus/context-garden/pull/278 (base main): Updated the architecture module map with kickoff, profiles, remote/manual runners, runs storage, and the JSON API. Exact-commit CI passed. cost=$0.07
- 2026-09-07T08:20:44+00:00 automated review requested changes: The requested modules are documented and the Markdown structure is intact, but the claimed path audit missed a nonexistent test path and the new API row overstates its backing services. cost=$0.32
- 2026-09-07T08:21:30+00:00 dispatched revise run 20260907T082128Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~20694 tokens)
- 2026-09-07T08:30:32+00:00 preserved uncommitted worktree changes from run 20260907T082128Z-revise outside the PR: `git stash apply 75fba569ce1f0a2751135892c3d3af0d2d6761e5` in /home/joshua/work/worktrees/CG-304 (garden:CG-304:20260907T082128Z-revise:reap)
- 2026-09-07T08:32:27+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/278: Corrected the architecture module map's queue-test reference and API description, with all requested modules and remote-runner surfaces documented. cost=$0.06
- 2026-09-07T09:10:31+00:00 automated review: approve — The architecture map accurately documents the requested kickoff, profile, runner, run-store, and API modules; all mapped paths exist and the Markdown remains structurally valid. cost=$0.31
- 2026-09-07T09:15:14+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T09:16:15+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T09:24:49+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/278
