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
