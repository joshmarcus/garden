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
