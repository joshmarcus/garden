---
id: CG-029
title: 'Close the phase: friction document, what changed, and the next goals'
status: done
product: context-garden
phase: phase-02-friction
depends_on:
- CG-009
- CG-008
- CG-013
priority: 3
estimate: M
difficulty: medium
reading:
- context-garden/phase-02-friction/docs/friction.md
- docs/roadmap.md
- principles/agent-loop.md
branch: garden/cg-029-close-the-phase-friction-document-what-changed-a
runner: manual
attempts: 1
last_dispatched_at: '2026-09-04T23:10:09+00:00'
created: '2026-09-04T14:02:28+00:00'
updated: '2026-09-05T03:14:58+00:00'
---

## Goal

Turn the phase's friction record into a finished document and a draft of the next phase's goals, so the next planning round starts from evidence.

## Context

By the time this runs, `garden friction context-garden/phase-02-friction` (CG-008) harvests the `## Friction` sections of every PR in the phase into `docs/friction.md`, and that file also holds the "First live run" and "Tiers" sections written by hand (CG-027, CG-028). `garden metrics context-garden/phase-02-friction` gives lead time, revise rounds, first-pass approval and cost per tier; `garden digest` gives the history. Write for the person who plans the next phase: short, specific, with task ids.

Closing the phase itself is `garden close-phase context-garden/phase-02-friction` (from CG-078, PR #73), run against the live garden; do that last, after the friction document and the next phase's goals are committed.

## Process (added at the freeze, 2026-09-05)

Run the retro as one process (`garden retro`, CG-133, is on main): (0) the operator's retro first, written by the agent that watched the loop all evening, as `docs/retro-operator.md`: what the process did well, every hand intervention with its cause and cost, and what to change, with the phase's numbers; independent of the personas, so write it before they run; (1) `garden friction context-garden/phase-02-friction` to harvest the Friction sections from every PR body; (2) `garden persona-review context-garden/phase-02-friction -p designer -p project-manager -p staff-engineer -p usability-expert -p user -p security`; (3) reconcile every harvested friction item against what merged: still true, fixed by which task, outdated, or wrong, with the evidence; (4) write the friction document from the reconciled table and the persona reports, then the next phase's goals; (5) `garden close-phase`. The output is a PR to the garden repo.


## Acceptance criteria

- [ ] `docs/friction.md` is organised as: what workers reported (harvested), what the first live run showed, the tier numbers, what changed in response (with task ids), and what remains.
- [ ] A metrics table for the phase, from `garden metrics`, is in the document.
- [ ] A `phase-03` directory exists under `context-garden/` (create it with `garden new-phase`) with a draft `goals.md` drawn from the "what remains" list, and no tasks yet.
- [ ] The "Next" section of `docs/roadmap.md` points at phase 3.

## Out of scope

- Planning phase 3's tasks; that is `garden plan`, after the goals are reviewed.

## Log

- 2026-09-04T17:23:50+00:00 approved (web)
- 2026-09-04T22:08:17+00:00 not yet: the phase is still open (30 tasks); approve when the structural work has landed so the friction document and next goals rest on the finished phase
- 2026-09-04T22:09:35+00:00 approved (web)
- 2026-09-04T23:10:09+00:00 dispatched work run 20260904T231000Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~5758 tokens)
- 2026-09-04T23:13:00+00:00 worker asks: This task edits garden-repo content (context-garden/phase-02-friction/docs/friction.md and a new context-garden/phase-03/ via `garden new-phase`, plus a `garden metrics` table), but I'm running in the context-garden tool repo worktree where none of that exists and where garden commands are disabled. Should CG-029 be re-dispatched against the garden repo (joshmarcus/garden) instead, or do you want me to author the finished friction document and phase-03 goals as new files inside this tool repo (and if so, under what paths, given there is no context-garden/ directory here)? cost=$0.64
- 2026-09-04T23:13:34+00:00 manual: closing the phase edits the garden repo (friction.md, the next phase's goals), which no worker checks out; a person or a garden-side agent does it when the phase's work has landed
- 2026-09-05T03:14:58+00:00 closed by hand: the retro (garden retro, PR #1 on the garden repo) produced docs/retro.md and phase-03/goals.md; the operator retro, walkthrough and nine persona reports are under docs/; phase 03 and 04 are scaffolded and the drafts moved; closing the phase next
