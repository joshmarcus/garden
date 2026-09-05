# phase-03 goals (draft)

_Drafted by `garden retro` from context-garden/phase-02-friction; edit before planning._

# phase-03 goals

## Why this phase

Phase 02 proved the loop runs on itself and stops well, and it removed the environment friction that filled most PR bodies. What survives the reconciliation and what the personas agree on is different: the loop trusts too much at its edges, its core is one class every PR collides in, the briefs and the retro do not see the current record, and the person meets a different vocabulary on every surface. Phase 03 makes the loop safe to leave running, cheap to change, honest about its own record, and consistent to operate, with done criteria in the loop's own numbers.

## Goals

1. **Trust the edges.** PR feedback becomes a prompt only when its author is OWNER, MEMBER, COLLABORATOR or on a `github.trusted_logins` allowlist; other comments park on a needs-human card and feedback is fenced as data. Workers and checks run with a scrubbed environment, no credential variables, and no path to push the base branch; doctor checks branch protection. Rendered markdown is sanitized and POST routes reject cross-origin requests. The fence fails a run on any worker write under `.garden/` or a task file. Automerge pins the reviewed head sha and defaults to requiring a human approval; auto-upgrade skips shas without one. design.md and roadmap.md say automatic merging is opt-in and gated.

2. **A scheduler that can be changed without collisions.** Land CG-137 first and alone: split the scheduler by tick phase, move trials, personas, retro, upgrade, fence and suggestions into modules, and make web actions a registry. One `Run.finish` owns collect, status and save; one rebase helper serves restack, conflict and moved-base; every stop goes through `_set_needs_human` with an explicit kind. Fix the two reproduced defects: dirty keys by value comparison at save, never on read, and `run_finished` emitted once. Split `tests/fake_claude.py` by concern and add an in-process synchronous test Runner for state-machine tests.

3. **Rebase is its own mode, with a merge queue.** Mechanical rebases first, an agent only on conflict, no re-review when the diff is unchanged, and rebase and description-only rounds do not count toward the caps (CG-139, CG-141). Reuse the conflict-feedback path for the conflict-plus-red-base corner. Aux runs (retro, personas, edits) share the worker-to-PR path instead of bespoke pushes.

4. **Briefs and the retro see the current record.** Reading-list snippets are inlined from the branch tip at dispatch and every path is verified, with a missing path reported as such. `garden friction` preserves every hand-written section and skips empty entries; the reconciliation reads PR-body friction, the Reported section and comment friction; `garden retro` waits for the persona reports (CG-145), gets a page per phase (CG-146) and a rendered walkthrough (CG-134), and a QA agent drives the loop through the web app (CG-135). principles/00-index.md says friction goes in the result field. `garden metrics` reports the fixed brief cost per phase.

5. **Notifications that are real and well timed.** `notify.command` is set in the live garden, documented with `output_format: stream-json` in README, the init scaffold and the examples, tested once by doctor, and logged on failure. A triage ping waits for the review verdict on that push; a failed mark-ready stays on the card. `garden init` defaults to a small `max_parallel` and a commented budget, and doctor warns when no phase has a budget. Config reloads on a tick so a YAML edit is not a restart.

6. **One vocabulary and one help.** One label for retry across web, TUI, CLI and README; `unpause` for the scheduler and `resume` for tasks; one Accept/Reject group with `garden decide` as its verb; help panels, `--version`, a `garden status` readable at 80 columns with a wont_do column; `priority_label` everywhere; the budget card, the review card and the in_review task page say what actually sets a budget or merges. README command table and TUI keys generated from the bindings; design docs point at the garden repo. Empty answers are rejected; the friction form posts one product/phase value and flashes on mismatch.

## Non-goals

- Hosted or multi-user operation.
- Automatic merging without gates; automerge stays opt-in and requires a human approval by default.

## Definition of done

- Every task shipped through `garden tick`; the manual exceptions of phase 02 (CG-027, CG-092, CG-113, CG-011, CG-039) and any new ones are listed in the closing document.
- The three high security findings (author trust on feedback, scrubbed worker environment plus branch protection, sanitized HTML plus origin check) are merged.
- `notify.command` fired in a live run this phase and the operator retro records it.
- `garden metrics` shows the fixed brief cost per phase and phase 03's number is at or below phase 02's.
- Conflict rebase rounds per merge and revise rounds per task are both below phase 02's (32 rebase rounds over 94 merges; 1.0 easy, 0.8 medium).
- scheduler.py is under half its current size; no phase-03 PR needs a manual rebase of `tests/fake_claude.py`.
- The retro reconciliation for phase 03 lists every Reported and comment-friction entry.

## Carried over from phase 02

- Ready and drafts: CG-030, CG-125, CG-132, CG-134, CG-135, CG-137, CG-139, CG-141, CG-142, CG-143, CG-144, CG-145, CG-146, CG-147.
- To file: stall-detection AC 3 test (CG-038); friction-form single select (CG-044); revise template wording on pushing (CG-109); a revise path and cost field for manual tasks (CG-027); CG-065's audit of old PRs for ignored bot feedback; line-anchored review comments and a digest of repeated review findings from the review-pass spec.
- Close-out: close phase-01, point roadmap Next at phase 03, revert `review.difficulty` to medium, record the automerge reversal with the CG-129 evidence.
