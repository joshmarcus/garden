# Friction

_No friction reported yet._

## Reported

### 2026-09-05 · reported by CG-137 (Split the scheduler by tick phase and the web actions into a registry so features stop colliding) in run 20260905T032209Z-work

- The acceptance criterion names product.md, which lives in the driving garden repo, not in this checkout; it cannot be edited from a product worktree.
- Baseline flake: tests/test_isolation.py::test_conftest_fixture_clears_ambient_env failed once under the runner's ambient GARDEN_ROOT and passed on later runs.

### 2026-09-05 · reported by CG-145 (garden retro waits for the persona reports before it dispatches the reconciliation) in run 20260905T033731Z-work

- The retro's persona-wait logic (aux-run-list based) already existed from CG-133 and looked correct at a glance in a single-process test; the actual bug only appears from state saved mid-dispatch being read by a concurrent process, which took some digging to reconstruct from the incident timestamps in the task log.

### 2026-09-05 · reported by CG-148 (A frozen or closed phase refuses approvals and dispatch; a freeze is a phase state, not a note) in run 20260905T033732Z-work

- The brief's exact meaning of "dispatch" was ambiguous between the scheduler's tick-time auto-dispatch, the `garden dispatch` CLI command, and the web dispatch button; centralizing the guard in Scheduler.dispatch() covers all three, but a brief that named which one(s) explicitly would have saved some investigation.

### 2026-09-05 · reported by CG-152 (An in-process runner for scheduler tests so no test drives a subprocess worker) in run 20260905T033741Z-work

- The task had no acceptance criteria; I took the phase definition-of-done line (no test drives a subprocess worker) as the requirement and treated the ssh end-to-end test, whose subject is a shell script, as the one deliberate exception.

### 2026-09-05 · discovered by CG-154 (Trust at the edges: PR feedback only from trusted authors, a scrubbed worker environment, sanitised HTML and an origin check on POSTs) in run 20260905T034729Z-work

planner.run_planner still launches the harness with the scheduler's full environment; its input is the garden's own files, so the exposure is low, but the same worker_env could apply.

### 2026-09-05 · reported by CG-154 (Trust at the edges: PR feedback only from trusted authors, a scrubbed worker environment, sanitised HTML and an origin check on POSTs) in run 20260905T034729Z-work

- The brief's acceptance criteria were 'to be written at planning' and never were; criteria were derived from the phase-03 goal 4 sentence.
- The referenced retro (../phase-02-friction/docs/retro.md) was not in the worktree and not found under the driving garden's checkout, so the evidence behind item 7 was not readable.

### 2026-09-05 · reported by CG-141 (Rebase is its own mode: mechanical first, an agent only for conflicts, no re-review when the diff is unchanged, a merge queue) in run 20260905T033731Z-work

- The brief says the merge queue 'replaces CG-138's one-per-cycle hold', but no such hold existed in the current code — automerge merged per-task in poll(). Implemented the queue as the intended mechanism.
- The clean-mechanical-rebase path already existed in _handle_pr_conflict but without a run record, checks re-run, or verdict handling; the task's framing as brand-new behavior made it easy to miss that half was already there.

### 2026-09-05 · reported by CG-134 (garden walkthrough: render the live web app's pages for the retro and the persona reviews) in run 20260905T035715Z-work

- The reading list did not point at src/garden/personas.py or src/garden/runs.py, both of which the task needed to touch or read; only cli.py and web/app.py were listed.

### 2026-09-05 · reported by CG-139 (Rebase rounds do not count toward the revision cap) in run 20260905T035733Z-work

- The reading list pointed at src/garden/scheduler.py, which no longer exists post-CG-137 split; had to explore the scheduler/ package directly to find the revise/review/conflict logic.

### 2026-09-05 · reported by CG-160 (garden retro --skip-personas can dispatch reconciliation with an empty persona-reviews section) in run 20260905T040848Z-work

- The brief's reading list pointed at `src/garden/retro.py` as "not found", but it exists and was directly relevant (persona_reports, reconcile_brief); the actual dispatch logic lives in src/garden/scheduler/retro.py which wasn't listed at all.

### 2026-09-05 · reported by CG-134 (garden walkthrough: render the live web app's pages for the retro and the persona reviews) in run 20260905T040848Z-revise

- main's test_retro.py:287 references a wait_for_runs helper that main itself no longer defines (removed with the in-process-runner refactor); it is a latent F821 that only manifests when a PR merges with main.

### 2026-09-05 · discovered by CG-135 (garden qa: an agent drives the loop end to end through the web app on a throwaway garden) in run 20260905T035723Z-work

garden qa's LLM path uses the harness's medium tier; a garden that caps max_turns for medium may cut a ~50-curl QA run short. Consider a qa-specific tier or a --difficulty option once a live run shows how many turns it takes.

### 2026-09-05 · reported by CG-135 (garden qa: an agent drives the loop end to end through the web app on a throwaway garden) in run 20260905T035723Z-work

- The walkthrough (CG-134) the brief says to use as the agent's script is not merged, so the flows list in the QA brief stands in for its index.
- There is no HTTP route to add a task or close a phase; 'add a task' goes through Plan phase (the fake planner) and a close-phase route had to be added despite the phase's no-new-features rule.
- The inlined tests/conftest.py in the brief was stale: the real one has an autouse fixture that strips GARDEN_ROOT, which matters for any CLI test.
- Merging has no web surface at all (a person merges on GitHub), so the throwaway garden needs a pretend GitHub page to merge on.

### 2026-09-05 · reported by CG-161 (garden plan does not check a frozen phase (only closed)) in run 20260905T041549Z-work

- tests/test_retro.py::test_retro_waits_for_every_persona_report_before_reconciling fails on a bare NameError (wait_for_runs undefined) independent of this change -- looks like leftover breakage from the CG-152/CG-148 in-process-runner rebase (introduced in commit d08d17a, merged via PR #100), predating this branch.

### 2026-09-05 · reported by CG-164 (Pre-PR and CI checks run in the scrubbed worker environment) in run 20260905T041557Z-work

- tests/test_retro.py::test_retro_waits_for_every_persona_report_before_reconciling fails on this branch (before my changes) with NameError: name 'wait_for_runs' is not defined — a missing test helper, unrelated to this task's diff.

### 2026-09-05 · discovered by CG-135 (garden qa: an agent drives the loop end to end through the web app on a throwaway garden) in run 20260905T042003Z-revise

tests/inprocess.py keys its fakes on argv[0]'s file name, so a harness configured as `python some_script.py` can never be faked in process; garden qa's worker is the first such harness.

### 2026-09-05 · reported by CG-135 (garden qa: an agent drives the loop end to end through the web app on a throwaway garden) in run 20260905T042003Z-revise

- The rebase surfaced a hidden coupling: the suite-wide in-process runner fixture from CG-152 silently breaks any test that runs a real harness command, and the error only shows up as a refused dispatch inside the web app's log.

### 2026-09-05 · reported by CG-139 (Rebase rounds do not count toward the revision cap) in run 20260905T042004Z-revise

- The brief's inlined reading list (tests/test_scheduler.py, src/garden/scheduler.py) was stale from before CG-137 split the scheduler tests and module — neither path exists any more, and the real relevant test lives in tests/scheduler/test_poll.py.
- The branch had drifted 15 commits behind main by the time this revision round ran, which is exactly the CI failure's root cause; a merge-queue rebase-before-dispatch (goal 2 of this phase) would have caught this earlier.

### 2026-09-05 · reported by CG-143 (Ship the garden-operate skill with the tool so every new garden gets it) in run 20260905T042449Z-work

- The task brief assumed garden-take/garden-plan/garden-review were already written by `garden init` and this task only needed to add garden-operate. In fact `garden init` never scaffolded any skill files -- only docs/architecture.md and docs/worker-protocol.md referenced them conceptually. The actual SKILL.md source for all four only existed in the driving garden's own checkout (~/garden/.claude/skills/), outside this repo and this worktree, so this task ended up sourcing and moving all four rather than just one. A future brief for skill work should note that these files' source of truth is the driving garden's checkout, not this repo, until this fix lands.
- The README had no existing 'skills' line or section to extend, despite the task phrasing ('mention it in the README's skills line') implying one existed -- I added a new ## Skills section.

### 2026-09-05 · reported by CG-142 (Task actions refuse a task that is done or cancelled) in run 20260905T042005Z-work

- The brief's reading list pointed at src/garden/scheduler.py and src/garden/web/app.py as single files, but the scheduler is already split into src/garden/scheduler/ (mixins per tick phase) and the task-action registry already lives in src/garden/web/actions/tasks.py, both from CG-137 having already merged.

### 2026-09-05 · reported by CG-170 (A task parked because the base branch was broken re-probes the base every tick and continues by itself when it goes green) in run 20260905T042440Z-work

- The inlined src/garden/inbox.py in the brief's reading list was an older version than the file on disk (no needs_human_info / attention_view / ATTENTION_KINDS); I worked from the actual file.

### 2026-09-05 · reported by CG-144 (A superseded review run is closed when a newer review starts; no run record outlives its process) in run 20260905T042706Z-work

- The brief's inlined reading list (runs.py, tests/test_scheduler.py) reflected a pre-CG-137 monolithic scheduler.py; the actual code is already split into src/garden/scheduler/ mixins with an existing orphan sweep (CG-116) in review.py, so the brief needed re-deriving from the current module layout rather than the inlined excerpts.

### 2026-09-05 · reported by CG-173 (Merging a stack parent retargets its children before the branch is deleted, and a child never opens a PR against a deleted branch) in run 20260905T043320Z-work

- Reading list pointed at src/garden/scheduler/poll.py, reap.py, dispatch.py and tests/scheduler/test_poll.py as "not found when the brief was built" though they exist at those paths in the checkout — the brief's file-discovery seems to have run before the worktree was materialised.

### 2026-09-05 · reported by CG-150 (garden friction keeps hand-written sections and the retro reads the Reported section and comment friction) in run 20260905T044804Z-work

- The task brief pointed at `../phase-02-friction/docs/retro.md` and `../phase-02-friction/docs/reviews/` for the original evidence, but those live in the separate garden data repo, not this tool repo — they weren't reachable from this checkout, so the fix was derived from the retro item's one-line description and the current code instead.

### 2026-09-05 · reported by CG-139 (Rebase rounds do not count toward the revision cap) in run 20260905T044056Z-revise

- The brief's Context/acceptance criteria describe rebase-round exemptions as one undifferentiated concern, but by the time this revision ran, a sibling task (CG-141) had already merged a complete, independently-designed implementation for the PR-conflict half. Worth flagging in planning when two tasks in the same phase goal (here, phase-03 goal 2) target overlapping scheduler behavior: the later one should either be scoped narrower up front or explicitly told to check the other's status before drafting its own mechanism.

### 2026-09-05 · reported by CG-149 (Briefs inline reading-list snippets from the target checkout and verify every path; the fixed brief cost is measured per phase) in run 20260905T044755Z-work

- The task's reading list was empty and the acceptance criteria were left 'to be written at planning', so the concrete requirement had to be reconstructed from the retro item quoted in the context.
- The retro and persona reports referenced (../phase-02-friction/...) live in the garden repo, not the product checkout, so they could not be read from the worktree.

### 2026-09-05 · reported by CG-147 (A product clone gets a git identity when it is made, and doctor checks every clone) in run 20260905T044746Z-work

- gitops.py had grown several functions (sync_remote_branch, rebase_onto_capture, etc.) since the brief's inlined copy was generated — had to re-read the live file rather than trust the brief's snapshot.

### 2026-09-05 · reported by CG-174 (garden pr and the web attach a new PR by refreshing the cached PR number and state, so the poll follows the new PR) in run 20260905T045725Z-work

- The brief's reading list pointed at scheduler/__init__.py, poll.py and state.py, but the actual fix (a hand-actions method) belonged in scheduler/human.py alongside triage/retry/mark_wont_do — worth noting for future PR-attach-related briefs so the reading list points there too.

### 2026-09-05 · reported by CG-157 (The Inbox friction form's product and phase selects cannot produce a 404) in run 20260905T050153Z-work

- The brief's reading list pointed at `../phase-02-friction/docs/retro.md` and its `docs/reviews/` persona reports for context, but this worktree only contains the context-garden repo itself at phase-03 — that sibling phase directory doesn't exist in the checkout, so the retro evidence was unavailable and the fix was derived directly from the described symptom and the form code instead.
- The task's acceptance criteria were left as 'to be written at planning' and were apparently never filled in before dispatch.
