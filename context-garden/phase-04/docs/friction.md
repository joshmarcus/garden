# Friction

_No friction reported yet._

## Reported

### 2026-09-05 · reported by CG-181 (The retro has a Features for the next phase section, fed by the product-manager persona, and each feature becomes a draft in the next phase) in run 20260905T095437Z-work

- Phase-04 goals lists CG-146 (a retro page) as a phase goal, and CG-181's acceptance criteria assume it already exists, but no such page/route exists in this repo yet — only the generic phase-doc markdown viewer.

### 2026-09-05 · reported by CG-182 (The tick never blocks the UI: actions do not wait for a tick, and checks and rebases run as records outside the tick) in run 20260905T103136Z-work

- The reading list omitted rebase.py (_merge_candidate/_run_merge_queue) and poll.py, both of which ran product checks inside the tick and had to be converted; finding the full set of in-tick check sites needed extra exploration.
- Making checks run records adds a tick per check stage, so ~10 tests that asserted single-tick outcomes had to be updated; the design note 'exactly like a review' implies this but the acceptance criteria's single-tick phrasing doesn't call it out.
- The design didn't spell out that a check run in flight must fence the poll and merge-queue phases off its task; without those guards the merge queue re-rebases a task whose pre-merge check hasn't reaped.

### 2026-09-05 · reported by CG-197 (Split cli.py into a cli/ package and fold the four rebase copies into one recorded helper) in run 20260905T112245Z-work

- The brief's "Reading list (read these)" was referenced by the operating rules but no reading list was actually included in the task, so I had to discover the four rebase call sites and the metrics block by search.

### 2026-09-05 · discovered by CG-208 (Browser notifications: an open garden tab notifies through Chrome when a decision appears, with a one-time permission toggle and one notification per tick) in run 20260905T115118Z-work

No scheduler currently emits a retro_question event, though the CG-208 design lists it as a decision kind the notifications endpoint returns. If a retro is ever made to pause for a human decision, emitting retro_question with a phase= field will light up notifications for it with no further work.

### 2026-09-05 · reported by CG-146 (A retro page per phase: the reconciled document, the operator retro, persona reports with scores, and the tasks the retro generated) in run 20260905T115043Z-work

- The task Context points at retro artefact paths (docs/retro/operator.md, docs/retro/README.md) that differ from what garden retro writes today (docs/retro.md); the page handles both, but the spec's file layout is stale.

### 2026-09-05 · reported by CG-208 (Browser notifications: an open garden tab notifies through Chrome when a decision appears, with a one-time permission toggle and one notification per tick) in run 20260905T115118Z-work

- Acceptance criterion 2 asks for a test that drives the client script with a fake Notification, but the test app (TestClient) and garden qa are HTTP-only and there is no JS runtime in the worker environment, so the client JS cannot be unit-tested here.
- The design lists retro_question as a decision kind the endpoint returns, but no scheduler emits that event yet.

### 2026-09-05 · reported by CG-132 (The web UI can create a task from a form, with the same fields as garden new-task) in run 20260905T115127Z-work

- The brief's acceptance criteria didn't say whether the web form's free-text Goal/Context/Acceptance-criteria fields (which `garden new-task` has no flags for) should affect the byte-comparison test; I read 'same inputs' as the CLI's own flags and tested with those fields blank, where the two must match exactly.

### 2026-09-05 · reported by CG-202 (One approve and one rebase: the CLI, web and TUI call the same approve gate, and the sync-rebase-force-push sequence lives in one place) in run 20260905T115109Z-work

- Acceptance criterion 2 describes four sync-rebase call sites, but its parent CG-197 had already unified them into one helper (_rebase_and_record); the criterion reads as if against the pre-parent code.

### 2026-09-05 · reported by CG-191 (The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check) in run 20260905T115101Z-work

- The brief's 'Reading list (read these)' section was referenced but empty in the task text — I explored the merge-queue/automerge code myself to find the touch points.

### 2026-09-05 · reported by CG-187 (Every persona finding is kept: each one becomes a draft with its severity as priority, the retro reconciles all of them, and nothing below high is dropped) in run 20260905T115052Z-work

- dispatch_aux records every phase-persona run under the shared aux task id "_persona" rather than a per-phase id, which the retro's findings lookup has to work around; not something this task changed, but worth knowing if a future task wants per-phase run history.

### 2026-09-05 · reported by CG-208 (Browser notifications: an open garden tab notifies through Chrome when a decision appears, with a one-time permission toggle and one notification per tick) in run 20260905T120439Z-revise

- Acceptance criterion asks for a test that drives the notification script with a fake Notification, but there's no JS runtime in the Python/TestClient test harness (playwright optional-extra not installed; garden qa doesn't execute JS), so client JS can only be covered structurally.

### 2026-09-05 · discovered by CG-178 (The retro ends in a verdict: close the phase, close with follow-ups for the next phase, or reopen with named tasks that must land first) in run 20260905T115043Z-work

CG-146 (a retro page per phase) should render the retro verdict record (scheduler.retro_verdict) as a first-class surface, replacing the phase-page panel added here; the record already carries verdict, status, who accepted it, when, and the filed task ids.

### 2026-09-05 · reported by CG-156 (One vocabulary and readable help: retry, resume and decide named once; help panels; --version; garden status at 80 columns) in run 20260905T120144Z-work

- CG-156's acceptance criteria were never written ("to be written at planning"); had to reconstruct the intended scope from the phase-02 retro item and phase-03 goals.md item 6.
- The retro item bundled several unrelated fixes (vocabulary, help, --version, 80-col status, card copy, priority_label); only the title's four are this task's scope, but the boundary had to be inferred.

### 2026-09-05 · reported by CG-191 (The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check) in run 20260905T122004Z-revise

- A rebase that renames a widely-called helper (CG-202: _hold_automerge -> _queue_hold) left two callers stale; the tick's broad try/except masked the AttributeError so tests stayed green by luck.

### 2026-09-05 · reported by CG-188 (A persona can report in its own shape: the review runner keeps the findings block and adds the persona's sections (vision, features, not now, questions), rendered in the report and fed to the retro) in run 20260905T122531Z-work

- The reading list pointed at personas/product-manager.md, which lives in the separate driving-garden repo, not this checkout; the editable equivalent here is DEFAULT_PERSONAS['product-manager'] in personas.py.

### 2026-09-05 · reported by CG-180 (The fake GitHub models CI latency and base-branch deletion, and a canary run checks a new pin before it is trusted) in run 20260905T121232Z-work

- The brief referenced a 'Reading list (read these)' section but listed no files, so I explored from the module map instead.
- AC4 gave two command forms ('garden canary' or 'garden qa --scripted --pin <sha>') without saying which is canonical; I picked one and noted it.

### 2026-09-05 · reported by CG-190 (No Set buttons anywhere: every editable value in the web UI applies when the user changes it, with a saved mark and an undo) in run 20260905T122540Z-work

- The brief's reading list described CG-099's pulldown pattern as "the same HTMX pattern," but there is no htmx (or any JS library) in this codebase — the existing and new behavior is a small hand-rolled vanilla-JS enhancement, consistent with the project's dependency-light convention. Worth correcting the wording in future briefs so it doesn't send the next agent looking for a library that isn't there.

### 2026-09-05 · reported by CG-185 (A page never 500s on an undefined template variable: tojson gets a value on every path, and a template error renders as a flash, not a traceback) in run 20260905T121711Z-work

- The brief's acceptance criteria implied a broad, general 'no undefined template variable ever 500s' guarantee (StrictUndefined across the whole app), which is a much larger change than the tojson incident alone — it required auditing and fixing every sparse-dict access idiom (_TaskState, event dicts, usage rollups) used across every template, not just the three named tojson sites. It happened to be tractable here (all fixed in ~4 small, well-understood spots), but that was empirical luck from running the suite under strict mode repeatedly, not something obvious from the brief up front.

### 2026-09-05 · reported by CG-192 (garden.yaml is re-read each tick when it changes, and the Config page says which keys are live) in run 20260905T123359Z-work

- The brief's hint ("Scheduler reads store.config per tick") is satisfied, but nothing in the brief flagged that config is consumed once at construction for the GitHub client, the upgrade installer, and the watch/serve loop interval; deciding which keys are 'live' vs 'restart' required reading those call sites. Documented as RESTART_KEYS.

### 2026-09-05 · reported by CG-193 (Approve refuses placeholder acceptance criteria and unresolved reading-list paths) in run 20260905T123408Z-work

- The brief's "Reading list (read these)" section named no files, so I inferred the entry points (approve gate, brief.py, inbox) from the codebase.

### 2026-09-05 · reported by CG-189 (The retro's questions for the human are decision cards: answer each in the UI, the answers land in the retro document and the next phase's goals, and the planner reads them) in run 20260905T123227Z-work

- The brief's Design says the answer appends to `docs/retro.md` and the next phase's `goals.md`, but the retro writes those into a PR worktree, not the live garden; it took a read of scheduler/retro.py to confirm the answer is meant to edit the live (post-merge) copies. One sentence in the brief on that timing would have saved the digging.

### 2026-09-05 · reported by CG-199 (Discovered work is deduplicated before it is filed: the same finding from several workers becomes one draft) in run 20260905T124816Z-work

- The discovered-item schema (title/body free text) has no structured file/error field, so the 'same file and error' match had to be a regex heuristic over free text rather than a precise comparison — reasonable for the common case but not foolproof against very differently-worded reports of the same bug.

### 2026-09-05 · reported by CG-198 (A restart reaps finished-but-unreaped runs of every mode before its first tick, and a dispatch onto a dirty worktree stashes and continues) in run 20260905T124807Z-work

- The brief's 'Reading list (read these)' section was empty, so I had to locate the relevant scheduler code (reap/finalize/review/dispatch) myself.

### 2026-09-05 · reported by CG-200 (Trust policy round two: the origin check resists DNS rebinding, bot trust is opt-in, and self-product PRs need a person or a second round) in run 20260905T124956Z-work

- The brief's "Reading list (read these)" section was referenced by the operating rules but not present in the task, so I explored to find the three touch points myself.
- github.automerge_min_review_rounds is set to 1 in DEFAULTS, so a resolved config value can't distinguish operator-set-1 from the default; I keyed the self/tool floor on the absence of a per-product override instead.

### 2026-09-05 · reported by CG-207 (Retros and persona reviews use the hard tier by default (retro.difficulty), so nobody edits garden.yaml before a retro) in run 20260905T130057Z-work

- The brief's acceptance criteria ask for the 'live garden' garden.yaml to drop its 'set to hard for a retro' comment on review.difficulty, but that file lives in the separate joshmarcus/garden repo per CLAUDE.md, not in this checkout — this worktree has no way to make that edit.

### 2026-09-05 · reported by CG-194 (Workers get no HOME, retry_command comes only from config, and the fence hash-checks garden.yaml and state.json) in run 20260905T124209Z-work

- Dropping HOME can break claude subscription auth (~/.claude) for workers; needed a judgement call — followed the explicit spec and added the worker_env.pass:[HOME] escape hatch, but the operational impact on the live garden should be verified before merge.
- The brief's 'Reading list (read these)' was referenced in the operating rules but no list was actually included in the task; had to explore to find the relevant modules.

### 2026-09-05 · reported by CG-194 (Workers get no HOME, retry_command comes only from config, and the fence hash-checks garden.yaml and state.json) in run 20260905T145937Z-revise

- The 'review feedback to address' in this revision round was generic ('re-check open review comments and CI') but GitHub had no actual review comments, reviews, or CI runs on the PR — the real blocker was the unresolved rebase conflict already noted in the task log from the prior attempt's failed rebase run (hit the monthly spend limit twice).

### 2026-09-05 · reported by CG-195 (Inbox cards read only the log, and terminal tasks drop needs-you and automerge notes in every view) in run 20260905T145948Z-work

- The brief's 'walkthrough test' phrasing could be read as literally belonging in tests/test_walkthrough.py (a separate docs-capture test module); the prior attempt reasonably read it as 'a test that walks through the scenario' and placed it in test_inbox_digest.py instead — worth clarifying in future task wording.

### 2026-09-05 · reported by CG-200 (Trust policy round two: the origin check resists DNS rebinding, bot trust is opt-in, and self-product PRs need a person or a second round) in run 20260905T145937Z-revise

- The branch had fallen ~55 commits behind main (a large batch of phase-04 work, including CG-185, CG-190, CG-192, CG-197's cli split, CG-199, CG-203, CG-207, and a Codex-adaptation merge) while paused for spend-limit retries, so the revision round required a full rebase with real conflict resolution rather than a small fix.
- No GitHub review comments, review threads, or CI check results existed on PR #155 to address; the only outstanding item was the merge conflict.

### 2026-09-05 · reported by CG-204 (Test debt from phase 03: a shared contract for the two GitHub fakes, real LocalRunner coverage, event-based assertions, and the state store's dict.get snapshot) in run 20260905T150731Z-work

- The task's Provenance points at context-garden/phase-03/docs/reviews/ for the staff-engineer findings, but only a product-manager review file exists there now — the staff-engineer reviews referenced in the task weren't recoverable at that path, so completeness of the 'prose assertions named in the review' criterion was judged from the goal text and commit history rather than the original review documents.

### 2026-09-05 · reported by CG-193 (Approve refuses placeholder acceptance criteria and unresolved reading-list paths) in run 20260905T152647Z-revise

- This revision-round brief did not restate the task's '## Acceptance criteria' list (only Goal/Context/Log/Review feedback), so this report verifies against the review feedback items plus the green test suite rather than quoting the original criteria verbatim.

### 2026-09-05 · reported by CG-210 (The pre-merge rebase keeps the verdict when the PR's own patch is unchanged: compare git patch-ids, not diff hashes, so a rebase onto a moved main never forces a re-review) in run 20260905T151445Z-work

- The brief's reading list for docs/architecture.md and the rebase.py/gitops.py inlined excerpts didn't mention that `last_diff_hash` also backs revise-stall detection and the hard-tier scratch-merge marker (checkruns.py, poll.py) — had to trace those separately to avoid regressing them while swapping the rebase-verdict comparison to patch ids.

### 2026-09-05 · reported by CG-178 (The retro ends in a verdict: close the phase, close with follow-ups for the next phase, or reopen with named tasks that must land first) in run 20260905T153644Z-revise

- The brief's reading list didn't mention that the phase_retro route/template exists separately from the phase page, or that a live garden's docs/retro.md only appears after the retro PR merges (tests need a _merge_retro_into_live helper) — both took extra digging to find the right place to wire retro_verdict into the retro page and test it end to end.

### 2026-09-05 · discovered by CG-212 (A usage or spend-limit error from a harness pauses dispatch for that harness and leaves the task ready, instead of burning attempts and failing tasks) in run 20260905T153346Z-work

CG-198 (the dirty-worktree stash task referenced in this brief) does not exist yet in this checkout; since 'stash before dispatch' was one of this task's own acceptance criteria, it's implemented here (src/garden/gitops.py stash_dirty, wired into scheduler/dispatch.py). Whoever plans CG-198 should check it isn't now fully redundant, or narrow its scope to whatever is left (e.g. surfacing stashed work in the UI).

### 2026-09-05 · reported by CG-158 (Manual tasks get a revise path, a reviewer that can see garden state, and a cost field on garden finish) in run 20260905T153522Z-work

- This task's acceptance criteria were literally 'to be written at planning' — the brief never got the planner's pass promised by the retro item, so I derived concrete, testable criteria from the task's goal sentence and the phase-02 retro/CG-027 pointer instead of stopping for input.
- The task log shows five prior dispatch attempts (spend limits, and twice a merge conflict against a dirty worktree with leftover changes from a killed prior attempt) before this run — the worktree needed no cleanup this time, but the log entries suggest the reset-to-ready path after a killed run doesn't always leave the worktree clean.

### 2026-09-05 · reported by CG-212 (A usage or spend-limit error from a harness pauses dispatch for that harness and leaves the task ready, instead of burning attempts and failing tasks) in run 20260905T153346Z-work

- The brief's acceptance criteria bundle a harness-level quota pause with a general dirty-worktree stash (marked 'shared with CG-198'), but CG-198 doesn't exist yet in this checkout; I implemented the stash here since it's in this task's own acceptance criteria, but CG-198's scope should be reconciled against it once planned.

### 2026-09-05 · reported by CG-163 (A backlog view across phases: sections per phase, drag a task to reorder it or to move it to another phase) in run 20260905T154318Z-revise

- The automated review appears to have raced the push: it flagged an issue that the immediately-preceding commit (2696b93, pushed 88s earlier) had already fixed, describing the pre-rebase client() rather than HEAD.

### 2026-09-05 · reported by CG-163 (A backlog view across phases: sections per phase, drag a task to reorder it or to move it to another phase) in run 20260905T163142Z-revise

- Two automated review rounds (16:02 and 16:12) failed outright with a harness login error and produced no verdict, burning review slots without giving feedback.

### 2026-09-05 · reported by CG-217 (The private worker HOME carries each harness's own config by default (CLAUDE_CONFIG_DIR, CODEX_HOME), doctor checks a worker can log in, and a not-logged-in exit is an environment stop) in run 20260905T162724Z-work

- CG-212 (the mechanism that pauses a harness on an environment stop) isn't in the codebase yet, so the brief's reference to 'with CG-212 that pauses the harness' describes a future consumer of Harness.parse's new error_kind field, not something this task could verify end-to-end.
- Changing garden doctor's harness login check broke five existing test_cli.py doctor tests that mocked subprocess.run around the old 'auth status' call shape; all had to be updated to match the new trivial-prompt invocation.

### 2026-09-05 · reported by CG-198 (A restart reaps finished-but-unreaped runs of every mode before its first tick, and a dispatch onto a dirty worktree stashes and continues) in run 20260905T163302Z-revise

- The recovery path's correctness turns on subtle timing between run.save(), events.emit(), and state.save() at different granularities (per-run vs per-tick); worth a design note in docs/architecture.md if another mode grows a similar restart-recovery path.

### 2026-09-05 · reported by CG-214 (A costs page: spend per activity over time, sliceable by difficulty, model, harness, phase and task, with the same numbers in garden costs) in run 20260905T162439Z-work

- No project-specific 'run' skill exists for this repo's web UI, and garden CLI invocations are blocked in this sandbox (GARDEN_ROOT sentinel) plus no headless browser is available, so visual verification was done by hand-building a throwaway garden, running uvicorn directly against garden.web.app.create_app, and curling/inspecting the rendered SVG rather than a real screenshot.

### 2026-09-05 · reported by CG-178 (The retro ends in a verdict: close the phase, close with follow-ups for the next phase, or reopen with named tasks that must land first) in run 20260905T164953Z-revise

- A branch reset (likely from the automated re-enable/reset-to-origin flow after a failed non-fast-forward push) silently discarded a completed revise commit that had already fixed the reviewer's undisclosed-bundling complaint; the fix had to be recovered from the local reflog rather than being redone from scratch, which only worked because the dangling commit was still reachable.

### 2026-09-05 · reported by CG-163 (A backlog view across phases: sections per phase, drag a task to reorder it or to move it to another phase) in run 20260905T164651Z-revise

- gh CLI is not authenticated in this worker environment (no GH_TOKEN), so I could not read the PR's live review comments or CI check status directly; I worked from the task's inlined log plus a fresh rebase against origin/main to find what was actually still broken.
- The review feedback for this round was generic ('re-check open comments and CI') rather than a specific finding, which cost time diagnosing rather than fixing.

### 2026-09-05 · reported by CG-217 (The private worker HOME carries each harness's own config by default (CLAUDE_CONFIG_DIR, CODEX_HOME), doctor checks a worker can log in, and a not-logged-in exit is an environment stop) in run 20260905T165427Z-revise

- The failing CI check was a genuine flake (Rich's default console wrap position for the doctor harness line depends on the CI runner's temp-directory path length, which differs from a local run), not a functional regression — worth remembering for other doctor/console.print lines that embed variable-length paths.

### 2026-09-05 · reported by CG-219 (garden observe: a configurable operator feed (interval, event kinds, digest window) that prints one status line, the cards, stuck runs and a digest, for a person or an operator agent) in run 20260905T165157Z-work

- The brief's reading list points at src/garden/cli/reports.py, which doesn't exist; garden observe ended up in cli/loop.py, which already houses digest/metrics/inbox/events — worth fixing the reading list or actually splitting a reports.py module in a future task.
- The brief inlines .claude/skills/garden-operate/SKILL.md as if it were a file to read in this repo, but it's generated by `garden init` from src/garden/scaffold.py's template and isn't tracked at that path here — future briefs touching this skill should point at scaffold.py directly.

### 2026-09-05 · reported by CG-217 (The private worker HOME carries each harness's own config by default (CLAUDE_CONFIG_DIR, CODEX_HOME), doctor checks a worker can log in, and a not-logged-in exit is an environment stop) in run 20260905T171714Z-revise

- The review feedback referenced CG-212's env_error/env_kind convention, but CG-212 is an unmerged sibling branch not present in this task's reading list or worktree; had to git fetch and inspect origin/garden/cg-212-... directly to find the exact field names to match.

### 2026-09-05 · reported by CG-220 (A revise or rebase run starts from the branch's head on origin and pushes with a lease, and the queue never rewrites a branch with a worker run in flight) in run 20260905T165010Z-work

- The brief's third criterion reads as if all three mechanical-rebase call sites needed a new guard; two (the merge queue via _automerge_gate, the stale-base probe via dispatch()'s needs_human pop) were already fully protected by existing invariants, confirmed by deliberately removing a candidate guard and watching tests still pass before committing to the real gap.

### 2026-09-05 · reported by CG-223 (Operator spend is an activity: garden operator-spend, the operator series on the costs page, the retro's share, and the design doc's operator-seat section) in run 20260905T170522Z-work

- The brief's reading list pointed at src/garden/cli/reports.py, which doesn't exist; the relevant CLI logic (garden costs) actually lives in src/garden/cli/costs.py.
- The brief didn't say where docs/operator-spend.jsonl should live relative to the garden root (the reference tools/operator_spend.py hardcoded a product-specific path); I used the garden root's own docs/ directory since the operator watches the whole garden, not one product — worth confirming that's the intended layout.

### 2026-09-05 · reported by CG-224 (Phase kickoff: before a phase starts, flag topics that need design, goals without a definition of done, questions for the owner, and docs that need attention) in run 20260905T170505Z-work

- CG-189 ("the retro's questions for the human are decision cards") already exists on its own unmerged branch with a fuller question/answer mechanism (Inbox, retro page, CLI); this task's brief pointed at it as if merged. I built a self-contained, smaller question-decision-card mechanism instead of depending on unmerged work — when CG-189 lands, the two should be reconciled rather than kept as two parallel mechanisms.
- The phase-page Kickoff panel has no browser-driven test in this change; only the underlying scheduler/data-path is tested.

### 2026-09-05 · reported by CG-212 (A usage or spend-limit error from a harness pauses dispatch for that harness and leaves the task ready, instead of burning attempts and failing tasks) in run 20260905T172529Z-revise

- The revision loop for this task ran to three review rounds (fresh gap found each time: revise/rebase state, then trial/review/persona dispatch); a brief that named every place a harness gets dispatched (work/revise/rebase, review, persona, compare, trial) up front might have caught this in one pass.

### 2026-09-05 · reported by CG-220 (A revise or rebase run starts from the branch's head on origin and pushes with a lease, and the queue never rewrites a branch with a worker run in flight) in run 20260905T174526Z-revise

- The failing pre-PR check in the review feedback only showed the assertion failure and a truncated captured log, not a stack trace pointing at which line in dispatch.py caused the wrong ordering; had to trace sync_to_origin_head vs _stash_dirty_worktree call order by hand to find the race between the two uncommitted-changes handlers.

### 2026-09-05 · reported by CG-218 (SSH remote workers don't get the CLAUDE_CONFIG_DIR/CODEX_HOME defaults) in run 20260905T175023Z-work

- This session's own ambient environment already carries a real CLAUDE_CONFIG_DIR (since I'm running as a worker under the same scrubbed-env mechanism this task modifies), so the new ssh test initially failed until I added monkeypatch.delenv calls — worth flagging in case other CG-217/CG-218-adjacent tests hit the same surprise.

### 2026-09-05 · reported by CG-221 (A slider from efficient to fast: named operating profiles that set workers, the tier map, the review tier and the observation feed together, switched live from the rail) in run 20260905T175649Z-revise

- The review flagged that CG-214 (the /costs page) already existed on main; the prior attempt had incorrectly treated it as not-yet-built and skipped the annotation work on that premise.

### 2026-09-05 · reported by CG-228 (A task is done only when its commits reach the product's base branch: a stacked child merged into its parent's branch stays open until the parent merges) in run 20260905T181552Z-work

- The brief's reading list only pointed at poll.py/rebase.py/graph.py; getting the status fully surfaced also required touching plants.py, web/common.py, web/templates/{base,task,_board}.html, cli/views.py, cli/common.py, tui/app.py and scheduler/dispatch.py's stuck-audit whitelist - none of that was discoverable from the reading list alone, only from a full-repo grep for status-keyed maps.
