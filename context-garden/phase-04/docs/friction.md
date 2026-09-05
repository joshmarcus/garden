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
