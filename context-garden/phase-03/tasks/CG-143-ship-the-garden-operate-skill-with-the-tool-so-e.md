---
id: CG-143
title: Ship the garden-operate skill with the tool so every new garden gets it
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading:
- src/garden/scaffold.py
- README.md
created: '2026-09-05T02:21:14+00:00'
updated: '2026-09-05T03:19:58+00:00'
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
