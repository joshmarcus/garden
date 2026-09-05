# project-manager review of context-garden/phase-04

**Persona:** project-manager · **Score:** 7/10 · 2026-09-05T22:38:57+00:00

Phase 04 delivered its structural promise (fast tick, live config, hard-tier automerge, restart recovery, brief gate, single writers) plus a large set of unplanned features, with 961 tests and lint green and every module under the line cap; the structure gate was respected. But four goal items shipped nowhere (planner still runs in the operator's environment, garden take skips the approve gate, planning-time sequencing, retro evidence inlining), two merged PRs carried unevidenced or placeholder criteria despite the new per-criterion rule, the measured definition-of-done numbers can only come from the live garden, and the README rewrite left the operate skill, design doc and roadmap contradicting the merge queue and live reload.

## High

- **trust** — run_planner copies os.environ wholesale so the planner still sees the operator's HOME and tokens, leaving goal 3's 'planner runs in the worker environment' unshipped.
  - suggestion: Route the planner call through runner.base.scrubbed_env with the harness config-dir defaults, and add a test asserting HOME is not the operator's.
- **brief gate** — garden take flips a draft to ready by hand, bypassing brief_gaps, phase_refusal and the kickoff warning that every other approve path enforces.
  - suggestion: Make take call Scheduler.approve (or refuse a draft) so the one gate covers the manual runner; this was a stated CG-193 follow-up nobody scheduled.

## Medium

- **acceptance criteria** — CG-217 merged with a criterion marked 'no evidence given' and CG-158 with a placeholder criterion, so the CG-179 rule that an unevidenced criterion blocks is not being applied.
  - suggestion: Turn a reviewer met:false or missing evidence on any criterion into a mechanical changes_requested, or restate the goal as advisory.
- **definition of done** — Hand merges, rebase rounds per merge, cost per easy task and the operator's share of spend are only measurable from the live garden and are not evidenced anywhere in the merged work.
  - suggestion: Have the retro run garden metrics and garden operator-spend against phase 03 and paste the numbers into the closing document before the close verdict.
- **docs** — The generated garden-operate skill still says any config change needs a restart, and design.md and roadmap.md list automatic merging as a non-goal while the merge queue shipped.
  - suggestion: Fix the scaffold template line, update the two docs' non-goals and the roadmap's Next section, and add kickoff.py and profiles.py to the architecture module map.
- **planning** — Goal 2's 'two tasks serving one goal are sequenced or scoped at planning' and 'retro evidence inlined into the brief' have no task and no PR.
  - suggestion: Either file them into phase 05 explicitly or strike them from the goals so the closing document is honest about scope.

## Low

- **unaccounted work** — CG-206, CG-213, CG-215, CG-216, CG-222 and CG-230 appear in no merged PR and their status is unknown from this checkout.
  - suggestion: List each with its status (open, cancelled, moved) in the phase closing document.
- **review cost** — An in-flight review whose PR merges is swept by reap_orphaned after it finishes rather than cancelled, so the model run still spends to completion.
  - suggestion: Kill the review process when its task reaches a terminal status, or reword the goal 4 item to match the sweep.
- **draft volume** — Persona findings at every severity, kickoff items and retro follow-ups all file drafts, so phase 05 is likely to open with an unreadable approve queue.
  - suggestion: Default persona-review --min-severity to medium and keep low findings in the retro document only.
- **follow-ups** — The backlog phase pulldown needs JavaScript (CG-163) and the notification endpoint lists a retro_question kind nothing emits (CG-208).
  - suggestion: Add a noscript submit to the backlog form and drop or wire retro_question so the kind set matches the emitters.

_garden persona run 20260905T223442Z-persona_
