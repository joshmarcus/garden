# Retrospective: context-garden/phase-04

_2026-09-05T23:05:56+00:00 · hard tier (claude-fable-5-1)_

## What changed

Phase 04 shipped 59 of 60 tasks and 58 pull requests (CG-206, notify.command in the driving garden, was cancelled). The structure gate held: CG-182 made the tick non-blocking with checks and rebases as run records, CG-197 split cli.py, and the features dispatched after both. The loop is now leaveable in mechanism: garden.yaml reloads each tick with RESTART_KEYS named, the merge queue merges hard-tier PRs after two rounds and a scratch merge, a quota or login error pauses the harness and leaves the task ready, a restart reaps finished runs of every mode, revise runs start from origin's head and push with a lease, and a task is done only when its commits reach the base branch. Trust work landed (no HOME, config-only retry_command, fence hashes on garden.yaml and state.json, DNS-rebinding-safe origin check, opt-in bot trust, guarded-diff automerge hold) but the planner still runs unscrubbed. The retro grew a verdict, features, decision cards, a kickoff, a retro page and per-persona findings filed as drafts. Surfaces caught up: no Set buttons, no 500s on undefined variables, help panels, a Costs page, operating profiles, garden observe, browser notifications, the backlog view, move-between-phases, the new-task form, and a README that walks end to end. Operator spend was recorded and fell from about half to under a third of total. Against the definition of done, hand merges rose to 16 of 57, cost per easy task rose to $5.04, rebase rounds per merge sit at 1.57, first-pass approval fell to roughly 75%, no phase-04 walkthrough was captured and tick duration is only in the CLI; module caps, the cli package, the phase-03 security highs, live reload and operator-spend recording were met.

## Numbers

- workers: $477.34
- operator: $0.00 — 0% of total
- total: $477.34

## Verdict

**Reopen.**
These must land before context-garden/phase-04 can close; each carries a freeze exception so it still dispatches.

Follow-ups filed in phase-05:
- CG-277: Live config reload holds while any in-flight worker's fence manifest disagrees with garden.yaml on disk
- CG-278: Task files get optimistic concurrency and a duplicate id is a validate problem, not a fatal exception
- CG-279: The planner and synchronous kickoff run in the worker environment
- CG-280: Each worker gets a private harness config dir holding only credentials, and the fence covers state.json and task files
- CG-281: Every status write goes through _transition: Scheduler.mark_done and unapprove, and a source-grep test
- CG-282: A brief never ships with an empty or unresolved reading list, and a revise brief restates the criteria and the concrete blocker
- CG-283: Planning sequences dependent tasks and inlines retro evidence into the brief
- CG-284: Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and the architecture module map
- CG-285: One vocabulary and one place for each fact across rail, Config, CLI and Inbox
- CG-286: The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal exit
- CG-287: Persona runs are recorded per phase and the retro validates the run id it reads
- CG-288: Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests, a second opinion for self products

Blocking tasks filed in this phase:
- CG-238: Every path to ready or to a run goes through the approve gate: Dispatch now on a draft, the new-task form's approve-now, and garden take — The definition of done says no task is dispatched with placeholder criteria, and three personas showed it is false in the shipped build; the gate is this phase's goal 2.
- CG-239: resolve_reading refuses absolute and parent paths, and the fence hashes the clone's git config and hooks — Goal 3 claims trust matches the mechanism and the phase runs overnight with automerge on for itself; the security persona verified on git 2.53 that a worker can execute code in the scheduler with the operator's credentials, and that a worker-filed task can inline the gh token into the next brief.

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Briefs reference a 'Reading list (read these)' section that is empty | CG-197 | – | still true | Seven tasks (CG-197, CG-191, CG-180, CG-193, CG-198, CG-200, CG-194) reported it and no merged task makes the brief builder refuse an empty list; CG-193 gates unresolved paths at approve, not empty lists. |
| Reading lists name files that do not exist (cli/reports.py, cli/reviews.py, tests/test_trials.py, personas/product-manager.md, the operate skill) | CG-219 | – | still true | CG-231 and CG-232 still shipped with 'not found when the brief was built' entries after CG-193 merged, so the builder annotates missing paths instead of dropping them. |
| Reading lists too narrow: CG-182, CG-210, CG-228, CG-233 found the real touch points only by full-repo grep | CG-182 | – | still true | No task changed how the planner builds reading lists; CG-233 reported nine unlisted call sites as late as 20:30. |
| Acceptance criteria 'to be written at planning' or absent (CG-156, CG-158, CG-226) | CG-156 | CG-193 | fixed | Approve now refuses placeholder criteria; CG-156 and CG-158 were approved before it merged, and the remaining bypasses (Dispatch now, form approve-now, take) are listed as blocking. |
| CG-181 assumed a retro page that did not exist | CG-181 | CG-146 | fixed | CG-146 (PR 131) added the per-phase retro page and CG-178 wired the verdict into it. |
| CG-146 spec pointed at docs/retro/operator.md paths garden retro does not write | CG-146 | – | outdated | The page handles both layouts; the stale path was in the brief, not the product. |
| CG-182 design omitted that a check run in flight must fence poll and the merge queue off its task | CG-182 | CG-182 | fixed | The guards landed in CG-182 itself and CG-220 later added the in-flight worker guard for branch rewrites. |
| No scheduler emits retro_question though the notifications endpoint lists it | CG-208 | – | still true | CG-225 routes retro questions through the kickoff mechanism and the project-manager persona confirms the kind is still listed with no emitter. |
| Client JS cannot be unit-tested: no JS runtime or headless browser in the worker environment | CG-208 | – | still true | CG-214 hit the same wall at 16:24 and had to curl rendered SVG; nothing merged adds playwright or a run skill. |
| dispatch_aux records every persona run under the shared id _persona | CG-187 | – | still true | No task changed the aux id, and the security persona's low finding shows the retro still recovers the run id from a markdown footer. |
| A rename left stale callers and the tick's broad try/except kept tests green | CG-191 | – | still true | CG-203 records a phase failure and continues, which makes the tick safer but still lets a swallowed AttributeError pass the suite. |
| Dropping HOME breaks claude subscription auth for workers | CG-194 | CG-217 | fixed | CG-217 gives the private HOME each harness's config dir and doctor checks a worker can log in; CG-218 covered ssh workers. |
| Revise briefs say 're-check open comments and CI' when GitHub has no comments and the real blocker is a rebase conflict | CG-194 | – | still true | CG-163 and CG-200 reported the same generic feedback later in the day and gh is unauthenticated in the worker, so the worker cannot read the PR itself. |
| A revise brief does not restate the task's acceptance criteria | CG-193 | – | still true | CG-179 asks results to speak to each criterion but no task added the criteria list to revise-round briefs. |
| A branch fell 55 commits behind main while paused on spend-limit retries | CG-200 | CG-212 | fixed | CG-212 pauses the harness and leaves the task ready instead of burning attempts, and CG-220 starts revise runs from origin's head. |
| The live garden.yaml still carries the 'once CG-207 lands' comment on review.difficulty | CG-207 | – | still true | garden.yaml line 34 in this checkout still reads 'retro/persona tier comes from retro.difficulty once CG-207 lands'; the edit belongs to the garden repo, one line. |
| CG-212 and CG-198 both implemented the dirty-worktree stash because the other was unmerged | CG-212 | CG-220 | fixed | Both merged (PRs 154 and 168) and CG-220 fixed the ordering race between sync_to_origin_head and the stash. |
| Reset-to-ready after a killed run leaves the worktree dirty | CG-158 | CG-198 | fixed | CG-198 stashes and continues on a dirty worktree, and CG-232 clears trial state; CG-234 still saw a dirty draft inlined into its brief, so the brief builder reads the worktree, which is a follow-up. |
| The automated review described a head that a push 88 seconds earlier had replaced | CG-163 | – | still true | CG-220 protects branches from queue rewrites but no task makes a review record the SHA it read and discard itself when the head moved. |
| Two review rounds failed with a harness login error and burned slots | CG-163 | CG-217 | fixed | A not-logged-in exit is now an environment stop that pauses the harness; CG-237 in phase 05 fixes the check reading a worker's prose as a login failure. |
| A branch reset silently discarded a completed revise commit | CG-178 | CG-220 | fixed | CG-220 starts revise and rebase runs from origin's head, pushes with a lease and never rewrites a branch with a run in flight. |
| CG-224 built a parallel question mechanism because CG-189 was unmerged | CG-224 | CG-225 | fixed | CG-225 re-did the retro questions through the kickoff mechanism and CG-189's implementation was dropped. |
| Dependent tasks merge out of order: CG-229 assumed CG-212 had merged and produced a design conflict | CG-212 | – | still true | Goal 2's 'two tasks serving one goal are sequenced at planning' has no task and no PR, as the project-manager persona also notes. |
| No run skill and no headless browser for visual verification of the web UI | CG-214 | – | still true | Nothing merged adds either; the walkthrough is the only capture and phase 04 has none. |
| Ambient CLAUDE_CONFIG_DIR leaks into env tests | CG-218 | – | still true | CG-218 patched its own test; no conftest fixture isolates the variable for the suite. |
| CG-221's prior attempt thought CG-214 did not exist | CG-221 | – | outdated | The revise round corrected it and both merged. |
| Brief inlined a dirty README draft left by earlier attempts instead of main's | CG-234 | – | still true | CG-198 stashes at dispatch but the brief is built from the worktree before that, so the inlined file can be a previous attempt's draft. |
| docs/design.md and roadmap.md list automatic merging as a non-goal; the scaffolded operate skill says any config change needs a restart | CG-234 | – | still true | Four personas found the same three stale statements in the current build. |
| Pre-PR check terminated with exit 143 under machine contention while the suite passes when rerun | CG-235 | – | still true | Checks now run as records outside the tick but still on the shared machine with no retry on a signal exit. |
| The discovered-item schema has no structured file or error field so dedup is a regex | CG-199 | – | still true | No task changed the schema. |
| Phase-03 staff-engineer review files are missing from the path the task's provenance names | CG-204 | – | still true | Only the product-manager review exists under phase-03/docs/reviews; the provenance was judged from the goal text. |
| Where docs/operator-spend.jsonl lives relative to the garden root | CG-223 | – | still true | The worker chose the garden root's docs directory; the owner has not confirmed. |
| Rich console wrap position makes a doctor test flake on path length | CG-217 | – | still true | The task worked around the one line; other doctor lines embed variable-length paths. |
| Brief wording: HTMX pattern, walkthrough test placement, two canary command forms, StrictUndefined scope, automerge_min_review_rounds default | CG-190 | – | outdated | Each was a brief ambiguity the worker resolved in the merged PR (CG-190, CG-195, CG-180, CG-185, CG-200). |
| last_diff_hash backs revise-stall detection and the scratch-merge marker, not just the rebase verdict | CG-210 | – | outdated | CG-210 traced and preserved both uses; the friction was the brief's omission. |
| Restart recovery timing between run.save, events.emit and state.save deserves an architecture note | CG-198 | – | still true | The staff-engineer persona reports the architecture module map also omits kickoff.py, profiles.py, inbox.py and the costs page. |

## What the personas said

Seven personas scored the phase 5 to 7 out of 10 and agree on the shape: the mechanism is right and the late-landing surfaces drifted. The designer and usability-expert list vocabulary and placement drift (the operating profile named three ways, a task id as a Config heading, tick_interval listed as both live and restart-only, three commands outside the help groups, the Kickoff panel leading every phase page, question cards in the wrong Inbox group, three disagreeing needs-you counts, and a walkthrough renderer that prints hidden panels). Three personas independently found that the phase's headline brief gate has open doors: Dispatch now on a draft, the new-task form's approve-now and garden take all skip Scheduler.approve, and the user persona adds that Mark done sets done directly around CG-228's rule. The product-manager reports that three definition-of-done numbers moved the wrong way, that the garden cannot yet report cost per accepted task or first-pass approval per model so phase 05's routing experiment cannot be read, that trial winners and manual-runner PRs never enter the review queue, that CG-187 will drop forty drafts into the next phase, and that the built-in profile stops hard-code Claude model ids. The project-manager finds four goal items with no PR (the planner in the worker environment, take through the approve gate, sequencing at planning, retro evidence inlined) and two merged PRs with unevidenced criteria. The staff-engineer flags two data-integrity hazards created this phase: task files written whole with no concurrency control now that actions and ticks run unlocked, and retro-filed drafts taking live ids into a branch, either of which becomes a fatal duplicate id. The security persona, at 5/10, verified on git 2.53 that a worker's git config write in its worktree lands in the shared clone and executes in the scheduler with the operator's credentials, that resolve_reading accepts absolute and parent paths so a worker-filed task can inline any file into the next brief, and that live config reload applies a worker's shell-redirect write to garden.yaml ticks before the fence reverts it; its mediums are the fence exemptions for .garden and task files, the harness config dir pointing at the operator's real one, and the unscrubbed planner.

## Still open

- Three brief-gate bypasses: Dispatch now on a draft, the new-task form's approve-now, and garden take skip Scheduler.approve
- Security high: a worktree git config write executes in the scheduler with the operator's credentials
- Security high: resolve_reading accepts absolute and ../ paths so any file can be inlined into a brief
- Security high: live config reload applies a worker's garden.yaml write before the fence reverts it
- Task files have no concurrency control across the action/tick split, and a duplicate id is fatal
- Retro-filed drafts take live ids into a branch that merges later
- The planner and synchronous kickoff run with the operator's full environment (goal 3, unshipped)
- Status assigned outside _transition in eight places, including web Mark done
- Briefs ship with empty reading lists, nonexistent paths, or lists too narrow for the change; revise briefs are generic and omit the criteria
- Dependent tasks are not sequenced at planning and retro evidence is not inlined (goal 2, unshipped)
- Hand merges 16 of 57, cost per easy task $5.04, rebase rounds 1.57 per merge, first-pass approval about 75%
- No phase-04 walkthrough captured; tick duration and hand merges not in garden metrics
- No cost-per-accepted-task or first-pass-approval metric per model, tier or harness
- CG-187 files every finding at every severity as a draft with no cap
- Scaffolded operate skill says config needs a restart; design.md and roadmap.md list automatic merging as a non-goal; architecture module map omits five modules
- Vocabulary and placement drift: operating profile named three ways, task ids in copy, tick_interval in two Config lists, unlabeled help commands, Kickoff panel placement, question-card grouping, needs-you counts disagree
- Built-in profile stops hard-code Claude model ids and economy routes hard-tier work to haiku
- Trial winners and manual-runner PRs do not enter the review queue on their own (CG-236 covers trials only)
- Re-dispatch leaves the old worker running; moving the pin is a hand sequence
- retro_question notification kind has no emitter; backlog phase pulldown needs JavaScript
- The live garden.yaml still carries the stale 'once CG-207 lands' comment
- Persona runs share the aux id _persona; the retro lifts the run id from a markdown footer without validation
- Client JS and web pages have no runtime or browser in the worker environment for verification
- CG-222 sits in phase 06 and CG-213, CG-215, CG-216, CG-230 in phase 05; the closing document should list them

## Questions for the owner

- **Does the reopen carry all three blocking items, or only the brief-gate closure, with the two security fixes moved to phase 05 as its first tasks?** — decision card `20260905T230012Z-retro-q0` (blocking)
  - The brief gate is this phase's own goal 2 and definition-of-done line; the git-config escape and reading-list containment reopen goal 3's self-approve-then-merge path on a product that runs overnight with automerge on, but they are not in the frozen goals text and the clone-config fix needs a day.
  - options: All three block (recommended), Only the brief-gate item blocks; security items open phase 05, Close now and file all three as phase-05 followups
- **Is phase 05 about adoption (a second team on its own machines) or about cost per accepted task?** — decision card `20260905T230012Z-retro-q1`
  - The phase-05 drafts pull both ways (CG-215 onboarding and CG-216 remote workers versus CG-213 routing and CG-230 pools); the product-manager asks for one sentence.
  - options: Cost first, onboarding as the one headline feature, Adoption first, Both, with a budget cap
- **Who is the second team, and is there a real repository to onboard before phase 05 closes?** — decision card `20260905T230012Z-retro-q2`
  - Without one, CG-215 and CG-216 test against fixtures only.
  - options: Name a repository, Fixtures are enough for phase 05
- **How many drafts may a retro file, and at what severity?** — decision card `20260905T230012Z-retro-q3`
  - CG-187 files every finding from seven personas; this retro alone would produce over forty drafts on top of the followups below.
  - options: High only as drafts, the rest on the retro page with file-as-task, High and medium, No cap
- **Codex runs in bypass-permissions mode since 2026-09-05; ratify or revert?** — decision card `20260905T230012Z-retro-q4`
  - The fence and the scrubbed environment now carry that trust alone, and the security persona shows the fence is a prefix deny plus after-the-fact attribution.
  - options: Ratify, Revert and fix the sandbox's git and network access
- **Are cost per accepted easy task at or under $4 and first-pass approval at or above 90% the phase-05 numbers?** — decision card `20260905T230012Z-retro-q5`
  - Phase 04 measured $5.04 and about 75%; the product-manager proposes these.
  - options: Yes, Different numbers
- **Ratify the decisions made in the owner's name this phase: automerge_method merge, review.max_rounds 4, reviews on the easy tier, the codex tier map, and eight queue-rotation hand merges.** — decision card `20260905T230012Z-retro-q6`
  - They belong in the closing document as exceptions.
  - options: Ratify all, Revert some
- **Does docs/operator-spend.jsonl live at the garden root's docs directory?** — decision card `20260905T230012Z-retro-q7`
  - CG-223 chose it because the operator watches the whole garden; the reference tool hardcoded a product path.
  - options: Garden root docs (as shipped), Per product

## Findings from persona reviews

### High

- **designer** — The rail, Config page, CLI and status line use 'operating profile', 'stop' and 'profile' for the same control, and 'profile' also names the separate observe feed level. → CG-246 [draft]
- **designer** — The Kickoff panel with a primary 'Kick off' button is the first thing on every open phase page, above the verdict, progress and task table, even on a phase well underway. → CG-247 [draft]
- **project-manager** — run_planner copies os.environ wholesale so the planner still sees the operator's HOME and tokens, leaving goal 3's 'planner runs in the worker environment' unshipped. → CG-260 [draft]
- **project-manager** — garden take flips a draft to ready by hand, bypassing brief_gaps, phase_refusal and the kickoff warning that every other approve path enforces. → CG-261 [draft]
- **user** — Dispatch now on a draft and the New task form's approve-now both skip the approve gate, so a task with placeholder criteria dispatches a run. → CG-270 [draft]
- **user** — The Mark done button on every in-review card sets status to done directly in the web action, bypassing _transition and the done-means-on-base rule from CG-228. → CG-271 [draft]

### Medium

- **designer** — A draft with brief gaps shows 'Fix the brief before approving' beside an enabled primary 'Approve into…' button whose press only produces a refusal flash. → CG-248 [draft]
- **designer** — tick_interval is listed both under live re-read values and under 'Needs a restart', and the operating-profile panel's eyebrow reads 'CG-221' (the CLI help also cites the task id). → CG-249 [draft]
- **designer** — move, retro-decide and canary appear in an unlabeled Commands box above the named help groups CG-156 introduced. → CG-250 [draft]
- **designer** — A draft task page shows both 'Approve into [phase]' and a separate move 'phase' pulldown listing the same phases with different submit behaviour, and the Inbox shows the approve pulldown even with a single option. → CG-251 [draft]
- **designer** — Kickoff and retro question cards sit in the 'Needs a decision' group whose description says the loop stopped on a stall, cap, closed PR or failed worker. → CG-252 [draft]
- **designer** — garden walkthrough still captures the phase-02 page set; Costs, the backlog view and the retro page are never captured for persona review. → CG-253 [draft]
- **designer** — The scaffolded garden-operate skill says any config change needs a restart, and docs/design.md lists automatic merging as a non-goal, both contradicting the shipped product. → CG-254 [draft]
- **project-manager** — CG-217 merged with a criterion marked 'no evidence given' and CG-158 with a placeholder criterion, so the CG-179 rule that an unevidenced criterion blocks is not being applied. → CG-262 [draft]
- **project-manager** — Hand merges, rebase rounds per merge, cost per easy task and the operator's share of spend are only measurable from the live garden and are not evidenced anywhere in the merged work. → CG-263 [draft]
- **project-manager** — The generated garden-operate skill still says any config change needs a restart, and design.md and roadmap.md list automatic merging as a non-goal while the merge queue shipped. → CG-264 [draft]
- **project-manager** — Goal 2's 'two tasks serving one goal are sequenced or scoped at planning' and 'retro evidence inlined into the brief' have no task and no PR. → CG-265 [draft]
- **user** — The built-in economy, balanced and fast stops hardcode Claude model ids and model_for applies a stop's tier map to any harness, so a codex garden switching stops gets Claude model names. → CG-272 [draft]
- **user** — The approve card says to fix the brief but the task page offers no way to edit criteria or the reading list; the only in-app path costs an edit run. → CG-273 [draft]

### Low

- **designer** — The worker's question is printed twice on its card because the reason line and the question line carry the same text. → CG-255 [draft]
- **designer** — Resume, trial, compare and edit runs fold into an unnamed 'other' activity that can be a large share on a small garden. → CG-256 [draft]
- **designer** — Spend appears three ways in the rail (a whole-dollar Runs figure, a Costs link, an hourly rate) and the rounded figure disagrees with the Inbox KPI; the profile select's default reads 'plain garden.yaml values'. → CG-257 [draft]
- **designer** — The Costs form submits every select on change yet keeps a visible Filter button, unlike the noscript fallback the rail uses. → CG-258 [draft]
- **designer** — A cancelled task's only action is 'Continue the loop', the TUI label is 'Continue loop', and the phase page names a 'planner-tier' review no surface defines. → CG-259 [draft]
- **project-manager** — CG-206, CG-213, CG-215, CG-216, CG-222 and CG-230 appear in no merged PR and their status is unknown from this checkout. → CG-266 [draft]
- **project-manager** — An in-flight review whose PR merges is swept by reap_orphaned after it finishes rather than cancelled, so the model run still spends to completion. → CG-267 [draft]
- **project-manager** — Persona findings at every severity, kickoff items and retro follow-ups all file drafts, so phase 05 is likely to open with an unreadable approve queue. → CG-268 [draft]
- **project-manager** — The backlog phase pulldown needs JavaScript (CG-163) and the notification endpoint lists a retro_question kind nothing emits (CG-208). → CG-269 [draft]
- **user** — tick_interval appears both under live re-read values and under the needs-a-restart list. → CG-274 [draft]
- **user** — The Costs page files a resume round as 'other', and garden observe's digest reported one failed run on a QA garden whose event log has no failed transition. → CG-275 [draft]
- **user** — With every phase closed, garden status prints an empty table and its legend before the closed-phase note. → CG-276 [draft]

## Features for the next phase

1. **Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs page and the retro** — CG-240 [draft]
   - size: medium
   - why now: Every routing decision in phase 05 is a guess until the garden reports this number.
   - **User value:** the operator can read whether a cheaper model lowers the bill per merged task, which is the finding of this phase (sonnet halved the run price and did not lower the bill).

**Why now:** CG-213 and CG-230 cannot be evaluated without it; CG-233 and CG-214 (merged) supply the per-run cost and the page.

**Size:** medium. **Depends on:** CG-233, CG-214. Accepted means merged to the base branch (CG-228).
2. **Every path that produces a PR ends in the review queue, on every runner** — _skipped: flagged by the retro as a duplicate of CG-236_
   - size: medium
   - why now: This is the remaining gap between the hand-merge count and the definition of done.
   - **User value:** no PR waits for a hand press; two trial winners waited 45 and 51 minutes and a manual-runner task ignores resume.

**Why now:** hand merges rose to 16 of 57 against a goal of zero. CG-236 covers trial winners; widen it so the poll queues any PR with no review recorded for its head and resume means the same on the manual runner.

**Size:** easy to medium. **Depends on:** nothing.
3. **The retro files only high findings as drafts and keeps the rest on the retro page with a one-press file-as-task** — CG-241 [draft]
   - size: medium
   - why now: Prevents the drafts-only Inbox that phase 03 fixed from returning through the retro.
   - **User value:** the owner opens phase 05 with an approve queue they can triage in one sitting instead of forty drafts.

**Why now:** CG-187, CG-181 and CG-224 together file every finding, feature, spike and doc item; this retro alone produces over forty.

**Size:** medium. **Depends on:** CG-146, CG-187 (merged); the owner's answer on the cap.
4. **The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail** — CG-242 [draft]
   - size: easy
   - why now: Three definition-of-done lines were guessed this phase because nothing measured them.
   - **User value:** the definition of done is measured by the tool, not counted by hand; personas read the phase's own pages.

**Why now:** phase 04 has no walkthrough, tick duration is only in the CLI tick line, and hand merges were counted by hand. Add Costs, backlog and retro pages to pages_for, run garden walkthrough before the personas, report hand merges as merged PRs the queue did not merge, and mean and max tick duration.

**Size:** easy. **Depends on:** CG-182, CG-201 (merged).
5. **redispatch kills the superseded worker, and pin runs the canary, installs and restarts after a tick** — CG-243 [draft]
   - size: medium
   - why now: Operator hand steps are the operator-spend goal in another form.
   - **User value:** the two recurring operator hand sequences become one command each; re-dispatching from codex to fable left two workers in one worktree and cost $4.34 for a run with no PR.

**Why now:** both were done by hand several times this phase and each is a known failure mode.

**Size:** medium. **Depends on:** CG-180, CG-198 (merged).
6. **Operating-profile stops name a tier per harness, and user-facing copy drops task ids** — CG-244 [draft]
   - size: easy
   - why now: Three personas raised it and the fix is small.
   - **User value:** a codex-only garden switching stops no longer gets Claude model names, and the Config page reads as a product, not a task list.

**Why now:** economy routes hard-tier work to haiku, which the phase's own cost finding says costs more per task; the Config panel eyebrow reads CG-221 and its retro column is empty.

**Size:** easy. **Depends on:** CG-221 (merged).
7. **A draft's acceptance criteria and reading list can be edited inline on the task page** — CG-245 [draft]
   - size: medium
   - why now: A refusal without a repair path sends the owner to a text editor.
   - **User value:** the approve card says 'fix the brief' but offers no way to do it; today the only in-app path costs an edit run.

**Why now:** the brief gate (CG-193) creates the refusal; this closes the loop with the same brief_gaps check on save.

**Size:** medium. **Depends on:** CG-193, CG-190 (merged).
8. **Onboarding: garden onboard drafts a garden from an existing repository** — _skipped: flagged by the retro as a duplicate of CG-215_
   - size: hard
   - why now: The product-manager's headline for phase 05; already drafted.
   - **User value:** the week-one feature for the next user. Keep the draft as written; it must produce a garden doctor pass on a non-Python fixture with no hand edits and run its planner under the approve brief gate.

**Size:** hard. **Depends on:** CG-193, CG-224 (merged).

## Persona reports

- [designer](context-garden/phase-04/docs/reviews/designer-2026-09-05.md)
- [product-manager](context-garden/phase-04/docs/reviews/product-manager-2026-09-05.md)
- [project-manager](context-garden/phase-04/docs/reviews/project-manager-2026-09-05.md)
- [security](context-garden/phase-04/docs/reviews/security-2026-09-05.md)
- [staff-engineer](context-garden/phase-04/docs/reviews/staff-engineer-2026-09-05.md)
- [usability-expert](context-garden/phase-04/docs/reviews/usability-expert-2026-09-05.md)
- [user](context-garden/phase-04/docs/reviews/user-2026-09-05.md)
