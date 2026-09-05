# project-manager review of context-garden/phase-03

**Persona:** project-manager · **Score:** 7/10 · 2026-09-05T10:22:12+00:00

Phase 03 shipped what it set out to ship: the split, rebase as a mode with a sticky merge queue, correct state and cost accounting, all trust items, and tests that run in-process with a QA agent that passes every flow. Hand actions fell from about a hundred to about thirty, and the post-pin numbers meet the definition of done on rebases, description rounds and first-pass approval. It does not fully close: the config-live item in goal 6 has no task in either phase, the metric that measures the rebase goal is unscoped and mixes mechanical with agent rebases, easy-task cost is marginally over target, and the phase needed twelve hand merges and one hand fix of main that the closing document must list. The friction log shows three recurring brief defects (unreachable evidence, empty criteria, stale reading lists) and duplicate discovered drafts that nobody has scheduled.

## High

- **goal 6 / DoD** — A garden.yaml change still needs a restart: Store loads config once per process and no phase-03 or phase-04 task addresses it.
  - suggestion: File a small task to re-read garden.yaml at the top of each tick before closing the phase, or strike the DoD item in the closing document.
- **metrics** — The rebase block of garden metrics ignores the phase filter and mixes mechanical with agent rebases, so the reported 0.19 per merge is a garden-wide coincidence, not the phase's number.
  - suggestion: Scope the rebase counts to the selected tasks and report mechanical and conflict rebases separately; quote the corrected figure in the closing document.

## Medium

- **process** — Twelve merges and one fix of main happened by hand (PR #104, four hard-tier merges, eight queue merges), which the DoD requires listing as exceptions.
  - suggestion: List them in the closing document and decide whether the queue may merge hard-tier PRs after two approving rounds.
- **planning** — Friction repeated across the phase without a task: unreachable retro evidence paths in briefs (4 tasks), placeholder acceptance criteria at dispatch (4), reading lists stale after the split (6).
  - suggestion: Have approve refuse a task with placeholder criteria, validate reading-list paths against the checkout, and inline retro evidence instead of pointing at the garden repo.
- **discovered work** — Six discovered drafts were filed for one red-main fix and cancelled by hand; discovered work is not deduplicated.
  - suggestion: Deduplicate discovered tasks by normalised title and file, and hold new drafts while the base is red.
- **operability** — notify.command is implemented and doctor-tested but the driving garden's garden.yaml does not configure it, so notifications still do not fire for this operator.
  - suggestion: Configure notify.command in the live garden and run garden doctor before the next unattended run.

## Low

- **cost** — Cost per easy task is $4.34 mean against a $4 target, driven by two pre-queue conflict chains (CG-139 at $12.03, CG-142 at $8.52) and the CG-139/CG-141 overlap.
  - suggestion: When two tasks serve the same goal, sequence them or scope the later one narrower at planning.
- **structure** — cli.py is 1995 lines and reap.py is 754, so the next collision file is known and the cap is nearly hit.
  - suggestion: Split cli.py by command family as an early phase-04 structure task, and carve reap.py before it grows.
- **scope** — CG-181, a phase-04 feature task, merged one minute before the phase-03 freeze.
  - suggestion: Note it in the closing document as the one feature that entered during the phase.

_garden persona run 20260905T101500Z-persona_
