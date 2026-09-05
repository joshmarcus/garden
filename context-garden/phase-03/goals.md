# phase-03 goals (draft)

_Drafted by `garden retro` from context-garden/phase-02-friction; edit before planning._

# phase-03 goals

## Why this phase

Phase 02 proved the loop can run on itself and stop well. The worker-environment friction that dominated the phase is gone (CG-081, CG-082, CG-098). What the personas and the surviving friction agree on is that the loop now trusts too much at its edges, that its core has grown into one 3,200-line class every PR collides in, and that the person meets a different vocabulary on every surface. Phase 03 makes the loop safe to leave running, cheap to change, and consistent to operate, and it measures what phase 02 only claimed.

## Goals

1. **Trust the edges.** Feedback from GitHub is only a prompt when its author is trusted (OWNER/MEMBER/COLLABORATOR or an allowlist); other comments become a needs-human card. Workers and checks run with a scrubbed environment and no path to push main. Rendered markdown is sanitized and POST routes check origin. The fence covers `.garden/` and task files. Automerge requires a pinned reviewed head and, by default, a human approval; auto-upgrade skips shas without one. Record in design.md and roadmap.md that automatic merging is opt-in and gated, not a non-goal.

2. **Notifications that are real and well timed.** `notify.command` is configured in the live garden, documented in README and the init scaffold with `output_format: stream-json`, tested once by `garden doctor`, and its failures are logged. A triage ping waits for the automated review verdict for that push; a failed mark-ready stays on the card instead of bouncing. `garden init` defaults to a small `max_parallel` and a commented budget.

3. **A scheduler that can be changed without collisions.** Split by tick phase and move trials, personas, retro, upgrade, fence and suggestions into modules (CG-137). One `Run.finish` owning collect/status/save; one `_rebase_branch` helper for restack, conflict and moved-base paths; every stop routed through `_set_needs_human` with an explicit kind. Fix the two reproduced defects: state keys are dirtied by value comparison at save, never by read, and `run_finished` is emitted exactly once. Add an in-process synchronous test Runner and move state-machine tests onto it.

4. **Rebase is its own mode, and a merge queue.** Mechanical rebases first, an agent only on conflict, no re-review when the diff is unchanged, rebase rounds not counted toward the revision cap (CG-139, CG-141). Refresh local main before revise checks, and reuse the conflict-feedback path for the conflict-plus-red-base corner.

5. **Briefs that match the checkout, with a number.** Reading-list snippets are inlined from the target checkout at dispatch and every path is verified to exist. `garden metrics` reports the fixed brief cost per phase; this phase's done criterion is that it does not rise.

6. **One vocabulary and one help.** One label for retry, `unpause` for the scheduler and `resume` for tasks, one Accept/Reject group with `garden decide` as its CLI verb, help panels instead of a flat list, `--version`, a readable `garden status` at 80 columns, `priority_label` everywhere. The budget and review cards and the in_review task page say what actually merges or sets a budget. README command table and TUI keys are generated from the bindings; design docs point at the garden repo.

7. **The retro sees the whole record.** `garden friction` preserves hand-written sections and skips empty entries; the reconciliation reads the Reported section and comment friction; `garden retro` waits for the persona reports (CG-145), gets a page per phase (CG-146) and a rendered walkthrough of the web app (CG-134). Aux runs share the worker-to-PR path so retro and personas are not bespoke.

## Non-goals

- Hosted or multi-user operation.
- Automatic merging without gates; automerge stays opt-in and requires a human approval by default.

## Definition of done

- Every task shipped through `garden tick`; manual exceptions listed in the closing document.
- The three high security findings (author trust on feedback, scrubbed worker environment plus branch protection, sanitized HTML plus origin check) are merged.
- `notify.command` fired at least once in a live run this phase, and the operator retro records it.
- `garden metrics` shows the fixed brief cost per phase and phase 03's number is at or below phase 02's.
- No worker reports environment friction; zero harvested items about venvs, installs or GARDEN_ROOT.
- scheduler.py is under half its current size and no PR this phase needs a manual rebase of `tests/fake_claude.py`.

## Carried over from phase 02

- Drafts: CG-125, CG-132, CG-134, CG-135, CG-137, CG-139, CG-141, CG-142, CG-143, CG-144, CG-145, CG-146, CG-147; CG-030 (plates).
- Close-out: close phase-01, point roadmap Next at phase 03, fix principles/00-index.md on where friction goes, revert `review.difficulty`, file the stall-detection AC 3 test (CG-038) and the friction-form mismatch flash (CG-044).
