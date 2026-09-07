---
id: CG-295
title: 'Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and
  the architecture module map'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scaffold.py
- docs/design.md
- docs/roadmap.md
- docs/architecture.md
- src/garden/kickoff.py
- src/garden/scheduler/kickoff.py
- src/garden/profiles.py
- src/garden/inbox.py
branch: garden/cg-295-docs-match-the-mechanism-the-scaffolded-operate
discovered_from: retro:context-garden/phase-04
last_dispatched_at: '2026-09-07T06:06:12+00:00'
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-07T11:50:52+00:00'
completion_track: documentation
---

## Goal

scaffold.py's skill template should say garden.yaml reloads each tick and only RESTART_KEYS need a restart; design.md and roadmap.md should drop automatic merging from non-goals; the architecture map should add kickoff.py, scheduler/kickoff.py, profiles.py, inbox.py and web/pages/costs, with a test that every module appears, plus the restart-recovery timing note CG-198 asked for. Also remove the stale 'once CG-207 lands' comment from the live garden.yaml.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Acceptance criteria

- [ ] scaffold.py's skill template states garden.yaml reloads each tick and only RESTART_KEYS require a restart (src/garden/scaffold.py)
- [ ] design.md and roadmap.md no longer list automatic merging under non-goals (docs/design.md, docs/roadmap.md)
- [ ] The architecture module map lists kickoff.py, scheduler/kickoff.py, profiles.py, inbox.py and web/pages/costs, and includes the CG-198 restart-recovery timing note (docs/architecture.md)
- [ ] A test fails if any module is missing from the architecture map (tests/test_architecture.py)
- [x] Operator verified live garden.yaml on 2026-09-07: it no longer contains the 'once CG-207 lands' comment (garden.yaml)

## Out of scope

(none)

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-284 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005024Z-edit) cost=$0.07
- 2026-09-06T00:52:24+00:00 approved (cli)
- 2026-09-06T13:13:13+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:31+00:00 reset to ready by hand
- 2026-09-07T06:05:55+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply e9fc940ac9bb37a54de90f83dbfc4fc2aab1fd74` in /home/joshua/work/worktrees/CG-295 to recover them (garden:CG-295:20260907T060555Z-work:pre-dispatch, run 20260907T060555Z-work)
- 2026-09-07T06:06:12+00:00 dispatched work run 20260907T060555Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~19395 tokens)
- 2026-09-07T06:24:06+00:00 preserved uncommitted worktree changes from run 20260907T060555Z-work outside the PR: `git stash apply d0c0ffe02920b7e6ff4c9f8df896f85fe639489c` in /home/joshua/work/worktrees/CG-295 (garden:CG-295:20260907T060555Z-work:reap)
- 2026-09-07T06:24:06+00:00 worker asks: Please provide the live garden.yaml within this checkout or authorize the correct path to edit it. cost=$0.20

## Operator answer
The live garden.yaml comment is already absent (verified directly). That criterion is fulfilled by the operator. Work only inside the product checkout on remaining documentation and tests; do not request or edit live garden configuration. Preserve existing implementation.
- 2026-09-07T09:14:05+00:00 Owner-delegated answer: live config cleanup already satisfied; resume product-only work via admission queue.
- 2026-09-07T09:14:05+00:00 reset to ready by hand

## Completion track

Current, usable documentation (`documentation`), grouped by owner request. Members: CG-295, CG-378.

Integrate detailed documentation corrections first, then the Astra README synthesis. Validate quickstart commands, links and supported-versus-deferred behavior against the resulting build; reuse factual evidence instead of duplicating implementation.

This is shared integration guidance, not additional implementation scope or a replacement for this task’s acceptance criteria. Preserve existing work and current-run criteria; the operator owns combined validation. Garden plan: context-garden/phase-05/completion-tracks.md.
