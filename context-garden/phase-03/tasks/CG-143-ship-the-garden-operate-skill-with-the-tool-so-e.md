---
id: CG-143
title: Ship the garden-operate skill with the tool so every new garden gets it
status: done
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading:
- src/garden/scaffold.py
- README.md
branch: garden/cg-143-ship-the-garden-operate-skill-with-the-tool-so-e
pr: https://github.com/joshmarcus/context-garden/pull/111
attempts: 1
last_dispatched_at: '2026-09-05T04:24:57+00:00'
created: '2026-09-05T02:21:14+00:00'
updated: '2026-09-05T04:38:10+00:00'
---

## Goal

`garden init` (and the README's setup steps) install `.claude/skills/garden-operate/SKILL.md` alongside `garden-take`, `garden-plan` and `garden-review`, so the agent that runs a garden knows the stall patterns and the product actions that clear them without learning them the hard way.

## Context

Written at the end of the first live run from the operator's notes: where the state lives, the first-look commands, the table of stall patterns with the action for each, the safe restart and pin recipes, cost hygiene, and the list of things never to do by hand. It lives in the garden repo now (`.claude/skills/garden-operate/SKILL.md`, 2026-09-05). Move the source into the tool's scaffold templates so it is versioned with the code and updated by pin bumps, and mention it in the README's "skills" line.

## Acceptance criteria

- [ ] `garden init` writes the four skills; a test checks the file exists and names the product's repo in its examples.
- [ ] the README lists `garden-operate` with the other skills.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T02:22:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:01:28+00:00 approved (web)
- 2026-09-05T03:05:54+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:58+00:00 approved (web)
- 2026-09-05T04:24:57+00:00 dispatched work run 20260905T042449Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~10550 tokens)
- 2026-09-05T04:33:10+00:00 opened https://github.com/joshmarcus/context-garden/pull/111 (base main): garden init now writes all four .claude/skills/*/SKILL.md files (garden-take, garden-plan, garden-review, garden-operate) from templates in scaffold.py, with garden-operate's pin recipe naming the tool's own repo; README and architecture.md updated to match, and a test covers the new files. cost=$1.28
- 2026-09-05T04:36:55+00:00 automated review: approve — garden init now scaffolds all four .claude/skills/*/SKILL.md files (take/plan/review/operate) from scaffold.py templates, with a test covering existence and the operate skill naming the tool's repo; README and architecture.md updated. Both acceptance criteria met, tests and lint pass. cost=$0.81
- 2026-09-05T04:38:10+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/111
