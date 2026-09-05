---
id: CG-133
title: 'garden retro: harvest PR friction, run the personas, reconcile what is still true, draft the next
  phase'
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/cli.py
- src/garden/review.py
- personas/00-index.md
- docs/design.md
branch: garden/cg-133-garden-retro-harvest-pr-friction-run-the-persona
pr: https://github.com/joshmarcus/context-garden/pull/94
attempts: 1
last_dispatched_at: '2026-09-05T00:50:08+00:00'
created: '2026-09-05T00:36:04+00:00'
updated: '2026-09-05T01:14:23+00:00'
---

## Goal

One command, `garden retro product/phase`, runs the phase's retrospective as a process rather than a pile of pieces: it harvests the Friction sections from the phase's PR bodies, runs the persona reviews against the phase's body of work, has an agent reconcile every friction item against what actually merged (still true, fixed by which task, outdated or wrong), and writes one retro document plus a draft of the next phase's goals for the person to edit. Approved into the frozen phase as the one exception, because the wrap-up itself needs it.

## Context

Asked at the end of the first live run, when the phase had 59 PRs with Friction sections and six personas to run. Friction logged by a worker is a snapshot: "this worktree has no venv" was true at 21:05 and fixed by 22:06; "the check command references $GARDEN_ROOT" was true for twenty minutes. A retro that quotes those as findings misleads the next phase. `garden friction` already collects the sections into `docs/friction.md`, `garden persona-review` already produces per-persona reports, and CG-029 is the task that turns them into a document. `garden retro` sequences them and adds the reconciliation step: an agent brief that carries the harvested friction, the persona reports, the phase's task list with statuses, and the merged PR titles, and asks for a table: friction item, when logged, by which PR, verdict (still true / fixed by CG-nnn / outdated / disputed), and the evidence; then the retro document with what changed, what the personas said, what is still open, and a draft `phase-03/goals.md`. The command runs in the garden (it edits the garden's own files), so it uses the self product from CG-123 or runs as a manual step with `garden take`; either way the output is a PR to the garden repo, not a direct edit. Dry-run prints the plan and the cost estimate first; a `--skip-personas` flag reuses reports that already exist.

## Acceptance criteria

- [ ] `garden retro product/phase` harvests, runs the personas (or reuses reports), reconciles and writes the retro document and next-goals draft; `--dry-run` prints the plan and estimated cost.
- [ ] the reconciliation table marks each friction item with a verdict and evidence; a test with fake reports and a fake PR list checks the verdicts.
- [ ] the result arrives as a PR to the garden repo; nothing edits the live garden directly.

## Log

- 2026-09-05T00:50:08+00:00 dispatched work run 20260905T004959Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~6289 tokens)
- 2026-09-05T01:10:37+00:00 opened https://github.com/joshmarcus/context-garden/pull/94 (base main): Added `garden retro product/phase`: harvests PR-body friction, runs or reuses persona reviews, has one agent reconcile each friction item against what merged (still true/fixed/outdated/disputed with evidence), and opens a PR to the garden's own self repo with a retro document and a next-phase goals draft. --dry-run prints the plan and a cost estimate. 9 new tests; full suite and lint green. cost=$8.47
- 2026-09-05T01:14:23+00:00 automated review: approve — Adds `garden retro` end-to-end (harvest → personas → reconcile → PR to the self repo) with a clean, well-tested reconciliation table; acceptance criteria met, full suite (376 passed) and lint green, scope limited to retro files. cost=$1.05
