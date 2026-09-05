# Retrospective: context-garden/phase-03

_2026-09-05T10:26:55+00:00_

## What changed

Phase 03 shipped its plumbing: the scheduler is split into tick-phase mixins and the web actions into a registry (CG-137), rebase is its own mode with a sticky merge queue and no re-review of an unchanged diff (CG-141, CG-139, CG-176), state and cost accounting stopped clobbering and double-counting (CG-153, CG-144, CG-142, CG-148, CG-175, CG-177), all four trust items merged (CG-154, CG-164, CG-165), scheduler tests run in-process and the QA agent passes every flow on a throwaway garden (CG-152, CG-134, CG-135, CG-169), and the operability items other than config reload landed (CG-155, CG-147, CG-145, CG-149, CG-150, CG-143). Thirty PRs merged, hand actions fell from about a hundred to about twenty-five, and first-pass approval reached 93%. Two definition-of-done items were missed: a garden.yaml change still needs a restart and has no task anywhere, and twelve merges plus one fix of main were done by hand because the queue does not merge hard-tier PRs. Reading-list staleness, the dominant friction early in the phase, was fixed by CG-149 mid-phase; unreachable retro evidence, placeholder acceptance criteria, and incomplete reading lists remain.

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Briefs point at evidence in the garden repo (../phase-02-friction/docs/retro.md, product.md) that is unreachable from the product worktree | CG-137, CG-154, CG-149, CG-150, CG-157 | – | still true | CG-149 verifies reading-list paths but nothing inlines retro evidence into the brief, and CG-159 (the product.md module map) was cancelled; the project-manager persona counts four tasks hit by it. |
| Acceptance criteria left 'to be written at planning' or absent at dispatch; one brief had no reading-list section at all | CG-152, CG-154, CG-149, CG-157, CG-165 | – | still true | No merged task makes approve refuse or flag placeholder criteria; CG-179 in phase-04 speaks to criteria but does not require them. |
| Reading lists pointed at src/garden/scheduler.py and tests/test_scheduler.py, which the CG-137 split removed | CG-139, CG-142, CG-144 | CG-149 | fixed | CG-149 inlines snippets from the target checkout and verifies every path before the brief is built. |
| Reading-list paths marked 'not found when the brief was built' although present in the checkout (discovery ran before the worktree existed) | CG-160, CG-173, CG-175 | CG-149 | fixed | CG-149 resolves paths against the target checkout; CG-175's brief was built under the pre-CG-149 pin. |
| Inlined snippets (inbox.py, gitops.py, tests/conftest.py) were older than the file on disk | CG-170, CG-147, CG-135 | CG-149 | fixed | Snippets are now read from the target checkout at brief time rather than a cached copy. |
| Reading lists omitted the files the fix lived in (personas.py, runs.py, scheduler/human.py, scheduler/retro.py) and Context prose described pre-split code paths | CG-134, CG-174, CG-160, CG-177 | – | still true | Path verification cannot add a file the planner never named and does not check the Context prose; no merged task widens reading-list coverage. |
| main was red: tests/test_retro.py referenced the removed wait_for_runs helper | CG-134, CG-161, CG-164 | #104 | fixed | Fixed by hand in PR #104; the scheduled fixes CG-166, CG-167, CG-168 and CG-172 were cancelled as duplicates. |
| Six discovered drafts were filed for the one red-main fix; discovered work is not deduplicated | CG-166, CG-167, CG-168, CG-172 | – | still true | The duplicates were cancelled by hand and no merged task deduplicates discovered tasks or holds drafts while the base is red. |
| Baseline flake in tests/test_isolation.py under the runner's ambient GARDEN_ROOT | CG-137 | – | outdated | Seen once at the start of the phase and not reported by any of the 30 later runs. |
| Retro persona-wait bug only reproduces when state saved mid-dispatch is read by a concurrent process | CG-145 | CG-145 | fixed | CG-145 made the retro wait on persona reports and CG-153 stopped dirty-on-read from clobbering concurrent writes. |
| The brief's 'dispatch' was ambiguous between tick auto-dispatch, garden dispatch and the web button | CG-148 | CG-148 | fixed | CG-148 put the frozen/closed guard in Scheduler.dispatch, which all three paths call; CG-161 extended it to plan. |
| Brief said the merge queue replaces a CG-138 one-per-cycle hold that did not exist in the code | CG-141 | – | outdated | The premise was stale but moot: CG-141 built the queue as the mechanism and CG-176 made it sticky. |
| The clean mechanical-rebase path already existed in _handle_pr_conflict without a run record, checks or verdict handling | CG-141 | CG-141 | fixed | CG-141 added the run record and verdict handling, though the staff-engineer persona now counts four copies of the rebase sequence of which only two record a run. |
| planner.run_planner launches the harness with the scheduler's full environment | CG-154 | – | still true | CG-164 and CG-165 scrubbed checks and the ssh worker but neither touched the planner; the security persona verified HOME still passes through everywhere. |
| The walkthrough (CG-134) was not merged when the QA agent needed it as a script | CG-135 | CG-134 | outdated | CG-134 merged as PR #103 on the same day. |
| No HTTP route to add a task; a close-phase route was added despite the no-new-features rule | CG-135 | – | still true | The new-task form is CG-132, a phase-04 draft; the close-phase route shipped inside CG-135 and is noted as the phase's scope exception. |
| Merging has no web surface, so the throwaway QA garden needs a pretend GitHub | CG-135 | CG-135 | fixed | CG-135 shipped MemoryGitHub; the staff-engineer persona notes it lacks reopen_pr, branch_exists, base_ref_deleted and is_trusted, which CG-180 partly covers. |
| tests/inprocess.py keys its fakes on argv[0]'s file name, so a harness run as 'python some_script.py' cannot be faked in process | CG-135 | – | still true | No merged PR changed how the in-process runner matches a harness command. |
| The suite-wide in-process runner fixture silently breaks any test that runs a real harness, surfacing only as a refused dispatch in the web log | CG-135 | – | still true | No task addressed it; the staff-engineer persona adds that LocalRunner.launch is now covered only by two Popen-stubbed tests. |
| garden qa's LLM path uses the medium tier, so a garden that caps max_turns for medium may cut a long QA run short | CG-135 | – | still true | No live LLM QA run was reported this phase, so it is unproven and unaddressed; CG-169 runs the scripted agent only. |
| A revision branch drifted 15 commits behind main; nothing rebased before merge | CG-139 | CG-141 | fixed | CG-141's merge queue rebases the head right before it merges and CG-176 keeps a rebased head in flight while CI runs. |
| CG-139 and CG-141 served the same goal and the later one drafted an overlapping mechanism | CG-139 | – | still true | Nothing at planning sequences or narrows tasks that target the same behaviour; the project-manager persona costs the overlap at $12.03 for CG-139. |
| The skills' source of truth was the driving garden's checkout; garden init scaffolded none and the README had no skills section | CG-143 | CG-143 | fixed | CG-143 ships all four SKILL.md files with the tool and adds a Skills section to the README. |

## What the personas said

Scores ranged from 5 (designer, security) to 7 (product-manager, project-manager, staff-engineer). All seven agree the mechanisms improved and the operator copy is coherent, and all seven name the same gaps: config reload was promised and not built, twelve of thirty merges were by hand, ticks block the web UI for about a minute because checks run inside them, and the walkthrough pages show eight of thirteen Inbox cards ending in a '] Tests cover' checklist fragment, 'needs you' badges on done tasks, and mechanical rebase run pages that describe a model run with no model. The designer and usability reviewers add that every new event kind renders blank on the timeline and the merge queue has no surface. Security says the isolation claims exceed the mechanism: HOME still reaches workers so the gh token is readable, the fence ignores .garden/ so a forged verdict could automerge, a check's JSON retry_command runs with shell=True in the full environment, and the origin check falls to DNS rebinding. The staff engineer counts the rebase sequence four times, approve five times (the TUI copy skipping the freeze gate), and merge-queue state written from seven places. The product manager asks phase 04 to finish the leave-it-running promise (CG-182, hard-tier queue merges, restart-safe reaps, live config) before the features.

## Still open

- A garden.yaml change still needs a restart; only budgets and max_parallel reload, and no task in any phase carries it
- The merge queue does not merge hard-tier PRs, so twelve of thirty merges were by hand and the queue has not been shown working live on a batch
- Pre-merge checks and rebases run inside the tick, so pages and button presses wait about a minute (carried by CG-182)
- Briefs still point at retro evidence by path into the garden repo, which a product worktree cannot read
- Tasks are approved and dispatched with placeholder acceptance criteria and reading lists that omit the file the fix lives in
- Discovered work is not deduplicated: six drafts for one red-main fix were cancelled by hand
- Inbox cards end in an acceptance-checkbox fragment because _last_log_line reads the task body, not the log
- Done tasks keep needs_human and automerge_blocked in the Board and task page; CG-175 only clears on new transitions
- Mechanical rebase runs render as model runs, the new event kinds (rebase, merge_head, feedback_ignored, retro_failed, rebased_stale_base, phase_frozen) print blank, and the merge queue has no surface
- Workers and checks run with HOME so on-disk credentials are reachable; the fence ignores .garden/ and garden.yaml; retry_command is taken from check output and run with shell=True in the full environment; the origin check compares Origin to Host
- planner.run_planner still launches the harness with the scheduler's full environment
- The rebase sequence exists four times and only two copies record a run, so garden metrics undercounts rebases; the metrics rebase block also ignores the phase filter
- Approve is implemented five times and the TUI copy has no freeze check; the web done action bypasses _transition
- dispatch_edits and dispatch_ready are not wrapped and state.save() is not in a finally; run_finished can double-emit and digest/metrics do not de-duplicate by run id
- A restart or pin move can lose a verdict reaped in the old server's last tick
- tests/inprocess.py cannot fake a harness run as 'python script.py', and the suite-wide fixture silently breaks tests that run a real harness
- cli.py is 1995 lines and reap.py 754, against the 800-line cap
- notify.command is implemented but the driving garden's garden.yaml does not configure it
- An in-flight review is not cancelled when its PR merges, and dispatch fails a task on a dirty worktree instead of resetting it
- garden approve exits 0 on a frozen-phase refusal while dispatch exits 1; new-phase accepts an unregistered product

## Features for the next phase

1. **The tick never blocks the UI: checks and pre-merge rebases run as records outside the tick** — _skipped: flagged by the retro as a duplicate of CG-182_
   - size: hard
   - why now: The product manager and user personas both say to ship this first because it is what makes the loop leaveable.
   - **User value:** pages and button presses answer in under a second while a pre-merge check runs, so the operator can watch the loop instead of waiting for it.

**Why now:** every persona names the one-minute tick as the reason the loop cannot be left running; the operator turned off the pre-PR check to cope.

**Size:** hard. **Depends on:** nothing; should merge first in phase 04.
2. **The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check** — CG-191 [draft]
   - size: medium
   - why now: The queue exists but half the merges still need a button; this closes the phase-03 promise the personas say is only half kept.
   - **User value:** an approved green hard-tier PR merges without a person, so the queue is shown working live on a batch and hand merges fall from twelve to zero.

**Why now:** twelve of thirty phase-03 merges were by hand, eight when the queue rotated and four on hard-tier PRs; the operator already asked for this policy.

**Size:** medium. **Depends on:** CG-176 (merged); a config key such as merge.hard_tier: two_rounds that the owner turns on, default off.
3. **garden.yaml is re-read each tick when it changes, and the Config page says which keys are live** — CG-192 [draft]
   - size: medium
   - why now: A promised item with no owner is the one thing every reviewer called out; it is small and unblocks unattended operation.
   - **User value:** editing garden.yaml takes effect within one tick with the changed keys logged; the Config page names what is live so nobody restarts to be safe.

**Why now:** this was a phase-03 goal and definition-of-done item that did not ship and has no task in any phase; six of seven personas flagged it.

**Size:** medium. **Depends on:** nothing. Reload in Store.invalidate on mtime change, Scheduler reads store.config per tick, one test that a max_parallel change between two ticks is honoured.
4. **Approve refuses placeholder acceptance criteria and unresolved reading-list paths** — CG-193 [draft]
   - size: medium
   - why now: The recurring brief defects have a single chokepoint, approve, and fixing it there makes every later task cheaper.
   - **User value:** a task cannot be dispatched with 'to be written at planning' criteria or a reading list that names a missing file; the Inbox approve card shows the gap so the person fixes the brief before spending a run.

**Why now:** four tasks shipped with placeholder criteria and six with stale reading lists this phase; the project-manager persona calls it half the phase's friction, and CG-179 (results speak to each criterion) is empty without real criteria.

**Size:** medium. **Depends on:** CG-149 (merged) for path verification; prerequisite for CG-179.
5. **Workers get no HOME, retry_command comes only from config, and the fence hash-checks garden.yaml and state.json** — CG-194 [draft]
   - size: medium
   - why now: Phase 03 claimed trust at the edges; the verified gaps are small, local fixes that make the claim true.
   - **User value:** a worker or a branch's test suite cannot read the operator's gh token, cannot forge an approve verdict into .garden/state.json, and cannot run a shell command through a check's JSON output; the docs say exactly what is and is not isolated.

**Why now:** the security persona verified all three on the phase-03 build and with automerge on they chain into a self-approved merge.

**Size:** medium. **Depends on:** CG-164 and CG-165 (merged) for the shared allowlist. Also hold automerge when a diff touches garden*.yaml, **/tasks/, .github/ or principles/, and require a loopback Host on POSTs.
6. **Inbox cards read only the log, and terminal tasks drop needs-you and automerge notes in every view** — CG-195 [draft]
   - size: easy
   - why now: Cheap, visible on every page and the top finding of the designer, usability and user personas.
   - **User value:** no Inbox card ends in a '] Tests cover' fragment, no done task wears a 'needs you' badge on the Board, and a merged task page no longer says automerge is held.

**Why now:** eight of thirteen Inbox cards and three done tasks are wrong on the walkthrough pages a person opens first; all seven personas list it.

**Size:** easy. **Depends on:** CG-175 (merged) for the transition cleanup; add a one-tick sweep of existing terminal tasks and gate the templates on a non-terminal status, with a walkthrough test that a fresh draft renders no fragment.
7. **Rebase runs, the new event kinds and the merge queue have a surface** — CG-196 [draft]
   - size: medium
   - why now: The queue and rebase mode are the phase's main mechanisms and are invisible, so the operator cannot trust them unattended.
   - **User value:** a mechanical rebase run page says 'mechanical rebase onto main, no model, no cost' with what git did and the check result; the timeline formats rebase, merge_head, feedback_ignored, retro_failed, rebased_stale_base and phase_frozen; the Board or Inbox shows the queue head, whether it waits on CI, and the last drop reason.

**Why now:** every state phase 03 added reached the UI unlabelled, and the operator cannot see why nothing merges.

**Size:** medium. **Depends on:** CG-141 and CG-176 (merged). Pairs with CG-184 but is a different set of pages.
8. **Split cli.py into a cli/ package and fold the four rebase copies into one recorded helper** — CG-197 [draft]
   - size: medium
   - why now: Phase 03 showed that structure first and alone removes conflicts for the rest of the phase, and the metric the phase is judged by is currently wrong.
   - **User value:** the next collision file is gone before phase 04 opens many PRs, and garden metrics counts every rebase because each path records a run.

**Why now:** cli.py is 1995 lines against the 800-line cap and absorbed seven commands this phase; the rebase sequence exists four times with only two copies recording a run, so the definition-of-done metric is undercounted. Also scope the metrics rebase block to the phase filter and split mechanical from agent rebases.

**Size:** medium. **Depends on:** nothing; run early and alone like CG-137 did.

## Verdict

**Close with follow-ups.** Every phase-03 task is done or cancelled, the definition of done is met on
first-pass approval (93%), trust items (5) and the testing goal, and missed on conflict rounds per
merge (0.47 against 0.2), one module over 800 lines (`cli.py`) and live config reload. Nothing in the
still-open list blocks closing: each item is a phase-04 task (CG-182, CG-191 to CG-197, and the
drafts filed from the persona findings). Decided by the operator with the owner's authority on
2026-09-05; the owner's answers to the product manager's questions are below.

## Answers

The product manager's five questions, answered by the owner on 2026-09-05:

- **Hard-tier merges** — the queue may merge them, after two approving rounds and its own scratch-merge check (CG-191, default on).
- **Structure gate** — yes: phase 04 dispatches CG-182 first and alone, then the cli.py split (CG-197), before any feature.
- **Budget** — no cap on phase 04; the owner does not want to block on budget.
- **Retro closing a phase** — a close verdict closes without waiting for approval; only reopen raises a decision (CG-178).
- **Operator decisions** — ratified: the eight hand merges when the queue rotated, cancelling CG-171, filing CG-162 and CG-163 in phase 04, hard-tier merges by hand until CG-191.

## Persona reports

Also: the operator retro at `retro/operator.md`, the product manager's vision report at
`reviews/product-manager-vision-2026-09-05.md`, and the walkthrough at `walkthrough/2026-09-05/`.

- [designer](context-garden/phase-03/docs/reviews/designer-2026-09-05.md)
- [product-manager](context-garden/phase-03/docs/reviews/product-manager-2026-09-05.md)
- [project-manager](context-garden/phase-03/docs/reviews/project-manager-2026-09-05.md)
- [security](context-garden/phase-03/docs/reviews/security-2026-09-05.md)
- [staff-engineer](context-garden/phase-03/docs/reviews/staff-engineer-2026-09-05.md)
- [usability-expert](context-garden/phase-03/docs/reviews/usability-expert-2026-09-05.md)
- [user](context-garden/phase-03/docs/reviews/user-2026-09-05.md)
