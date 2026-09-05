# Retrospective: context-garden/phase-04 (joined)

_One document from two reconcile runs (claude-fable-5-1 at 23:05Z, gpt-6-astra at 23:15Z), the operator's retro and the seven persona reports; where only one judge made a point it is marked (fable) or (astra)._

## Verdict

**Reopen.** Both judges said reopen; they differed on how much must land first. Fable named two blockers, astra eight. The evidence supports three:

- **CG-238** (every path to ready or to a run goes through the approve gate): merged as PR #192. Three personas showed the phase's headline gate had three open doors on the shipped build; goal 2 and a definition-of-done line said it did not.
- **CG-239** (resolve_reading refuses absolute and parent paths; the fence hashes the clone's git config and hooks): PR #193, in a revise round after the automated review found the hooksPath mitigation used a shared, predictable temp directory and a fourth raw git call bypassed the block. The security persona verified on git 2.53 that a worker's config write executes in the scheduler with the operator's credentials, which reopens the self-approve-then-merge path goal 3 says is closed.
- **CG-242** (hold an untrusted garden.yaml change until every in-flight worker's fence manifest agrees with the file on disk) (astra). This is the security persona's third high and phase 04 created the path: CG-192's per-tick reload applies a worker's shell-redirect write to notify.command, checks, setup.command or worker_env.pass ticks before the fence reverts it at reap. Fable filed the same item as a phase-05 follow-up (CG-288) on the ground that it is not in the frozen goals text; but goal 3 is "trust claims match the mechanism", the garden runs overnight with automerge on for itself, and the owner chose the strict option on the analogous question. It is a medium task in one function of store.py.

Of astra's other five blocking drafts, none must hold the phase open: **CG-240** and **CG-241** duplicate CG-238 and CG-239 and should be cancelled with a reason; **CG-243** (task-file concurrency), **CG-244** (retro id reservation and duplicate ids as a validate problem), **CG-245** (the planner in the worker environment), **CG-246** (workers cannot write state.json, task files or the harness config dir) and **CG-247** (Mark done through _transition and the base-branch rule) are real, backed by the staff-engineer, security and user reports, and become phase 05's first tasks in that order. CG-245 was deferred by CG-194 explicitly and is phase 05's goal 3 in the stub; CG-243 and CG-244 are hazards with a hand workaround; CG-247 is an escape hatch the owner presses.

Done by hand before the retro PR merged: the retro branch carried both judges' drafts from one live counter (its CG-240 to CG-250 collided with eleven files filed live since), so fable's 49 drafts were refiled through `garden new-task` as CG-251 to CG-299 in phase 05 and astra's copies were dropped. CG-244 (reserved ids; a duplicate id as a validate problem) is phase 05's fix.

## What the owner has answered

Recorded under Decisions in phase-05/goals.md on 2026-09-05:

- The reopen carries CG-238 and CG-239; astra's further blockers are settled above.
- **Phase 05 is about adoption**: onboarding (CG-215), any model (CG-213), shared quotas (CG-230), any machine (CG-216). Cost per accepted task is measured from the phase's first task as a prerequisite, not the headline.
- **Every finding is filed as a draft at its severity, no cap.** The kickoff and the operator prune at approval; a finding not worth a task is cancelled with a reason. This overrules the feature both judges ranked third.
- **Phase-05 numbers**: at most $4 per accepted easy task and at least 90% first-pass approval, measured per accepted task, from the sonnet-era baseline.
- **Ratified**: automerge by merge commit, review.max_rounds 4, reviews on the easy tier, the codex tier map luna/terra/sol. The eight queue-rotation hand merges were a bug (CG-176), not a policy.
- **The operator ledger** lives at `context-garden/docs/operator-spend.jsonl`, product and phase attribution welcome.
- **CG-206** stays cancelled: browser notifications first; unattended delivery to a phone is parked.

Still open: whether codex stays in bypass-permissions mode once CG-239 and CG-242 land (both judges asked); whether a named second team and repository exist for CG-215 (both); whether a self product's second approving round should be a persona or a person rather than the same reviewer twice (astra, from the security persona's low finding).

## Numbers

Both retro documents printed "operator: $0.00, 0% of total". That figure is wrong: the retro reads `<garden root>/docs/operator-spend.jsonl` and the ledger is at the product's `docs/`, where the owner says it lives. The operator's own numbers:

| | phase 03 | phase 04 |
|---|---|---|
| workers | $190 | $474 (the retro counts $477.34) |
| operator | $190, 941 turns | $195, 673 turns |
| operator share | 50% | 29% |
| tasks done | 30 | 59 of 60 (CG-206 cancelled) |
| merged by the queue | 18 of 30 | 41 of 57 |

Against the definition of done (operator retro, `garden metrics`):

| line | goal | phase 03 | phase 04 |
|---|---|---|---|
| hand merges | 0 | 12 of 30 | 16 of 57: 8 in the 05:37Z queue rotation, the rest around a stacked branch, the pin lagging main, and CG-030 on the manual runner |
| web action under 1 s during a check; tick under 10 s | yes | no | yes since CG-182; tick duration is printed by the CLI only, not reported by metrics |
| garden.yaml live within a tick | yes | partly | yes (CG-192); five settings changed during the day with no restart |
| no placeholder criteria or unresolved reading path dispatched | 0 | n/a | gate since CG-193; CG-156, CG-158 and CG-226 were approved before it; three bypasses closed by CG-238 |
| rebase rounds per merge | under 0.2 | 0.70 | 1.57: 1.02 mechanical by design (every head is rebased before merge, at $0) and 0.55 agent (31 conflicts in 56 merges, $17.46) |
| cost per easy task | at most $4 | $4.34 | $5.04 over 29: $3.67 in the opus era, $5.88 in the sonnet era |
| no module over 800 lines; cli.py a package | 0 | 1 | 0; largest `cli/loop.py` at 722 (CG-197) |
| walkthrough shows the three fixes | yes | no | CG-195 and CG-196 shipped them; no phase-04 walkthrough was captured, so unverified |
| security persona's three highs closed | 3 | 0 | 3 (CG-194); the persona found three new highs on this build |
| every task through `garden tick`, exceptions listed | yes | no | exceptions: CG-030 merged by hand, CG-189 merged into CG-178's branch and redone as CG-225, eight rotation merges, CG-234's first run killed by hand |
| operator turns and spend recorded, share lower | yes | 50% | 29%, recorded |

First-pass approval fell from 93% to 79% on easy and 71% on medium. The operator's finding of the phase: after the 14:50Z tier change, sonnet halved the run price ($4.56 to $2.53 per work run) and did not lower the bill per task, because sonnet-era tasks needed more revise and review rounds (CG-212 took six of each). Codex on four tasks: terra beat sonnet on CG-225 (9 to 7) at $1.01 against $5.03; astra beat sonnet on CG-158 at $3.77 against $4.41; CG-226 was approved first round.

## What the phase set out to do, and did

Both judges and the operator agree on the shape. The structure gate held: CG-182 first and alone, then CG-197, then the features.

- **The loop runs overnight (goal 1).** Checks and rebases are detached run records and a web action answers in under a second (CG-182); the queue merges hard-tier PRs after two rounds and a scratch merge (CG-191); garden.yaml reloads each tick with RESTART_KEYS named (CG-192); a restart reaps finished runs of every mode (CG-198); a quota or login error pauses the harness and leaves the task where it was (CG-212, CG-217, CG-227); a revise run starts from origin's head and pushes with a lease (CG-220); a task is done only when its commits reach the base (CG-228); the canary (CG-180). Not done: notify.command in the driving garden (CG-206 cancelled).
- **Briefs complete before they cost a run (goal 2).** Approve refuses placeholder criteria and unresolved paths and the Inbox card shows the gap (CG-193, CG-209, CG-238); discovered work is deduplicated (CG-199); results and reviews speak to each criterion (CG-179). Not done: retro evidence inlined into the brief, and dependent tasks sequenced at planning; neither had a task (project-manager).
- **Trust matches the mechanism (goal 3).** No HOME for workers and checks, retry_command from config only, the fence hashes garden*.yaml and state.json, automerge holds on a guarded diff (CG-194); the origin check resists DNS rebinding, bot trust is opt-in, self products need two rounds (CG-200); the private HOME carries each harness's own config dir (CG-217, CG-218); the notify example is quoted and walkthrough captures are scrubbed (CG-201). Not done: the planner still copies os.environ wholesale (planner.py line 218); the security persona found three new highs and three mediums, and the fence remains a prefix deny plus after-the-fact attribution.
- **Every state has a surface (goal 4).** Inbox cards read the log and terminal tasks drop stale flags (CG-195); rebase runs, the new event kinds and the merge queue are rendered (CG-196); pages never 500 (CG-185); approve exits 1 on refusal and new-phase refuses an unregistered product (CG-205); help panels, --version and status at 80 columns (CG-156). Not done: an in-flight review is swept after it finishes, not cancelled (project-manager).
- **One writer per fact (goal 5).** One approve gate, one sync-rebase, one writer for queue state with a source-grep test (CG-202); one recorded rebase helper and cli/ as a package (CG-197); every tick phase guarded and state saved in a finally (CG-203); a GitHubLike contract (CG-204); close-phase through the scheduler (CG-211). Not done: status is still assigned directly in eight places, including the web Mark done and unapprove actions, CLI set-status, attach_pr and the retro's own blocking-task approval.
- **The features (goal 6).** The retro's verdict, features, questions and page (CG-178, CG-181, CG-188, CG-189, CG-225, CG-146); kickoff (CG-224, CG-226); the new-task form, move, backlog, approve-into-phase (CG-132, CG-162, CG-163, CG-186); every finding a draft (CG-187); plates and the mark (CG-030, CG-183, CG-184); no Set buttons (CG-190); notifications (CG-208); the Costs page and operator spend as an activity (CG-214, CG-223); observe and the profile slider (CG-219, CG-221); trials that survive an environment failure, wait and rerun (CG-229, CG-231, CG-232); codex priced from usage (CG-233); the retro's own model (CG-207, CG-235); the README (CG-234).

## Friction, reconciled against what merged

67 items were logged. Fable reconciled 36 rows and astra 79; the table below merges them, one row per underlying cause.

| Friction | Logged by | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Empty reading lists ("Reading list (read these)" with nothing under it) | CG-197, CG-191, CG-180, CG-193, CG-198, CG-200, CG-194 | – | still true | No merged task makes the brief builder refuse an empty list; CG-193 gates unresolved paths, not absence. |
| Reading lists name files that do not exist (cli/reports.py, cli/reviews.py, tests/test_trials.py, the operate skill as a source file) | CG-219, CG-223, CG-229, CG-231, CG-232, CG-188, CG-234 | – | still true | CG-231 and CG-232 shipped with "not found when the brief was built" after CG-193 merged, so the builder annotates a missing path rather than refusing it (fable). |
| Reading lists too narrow for the change | CG-182, CG-210, CG-228, CG-233, CG-212 | – | still true | CG-233 found nine unlisted run-finalisation sites by grep at 20:30Z; CG-212's revise omitted review.py, the file that held both the finding and the fix. |
| Placeholder or absent acceptance criteria | CG-156, CG-158, CG-226 | CG-193, CG-238 | fixed | Approve refuses them and the three bypasses are closed; CG-158 and CG-217 still merged with unevidenced criteria, so the CG-179 rule is stated, not enforced. |
| Revise briefs are generic ("re-check comments and CI") and omit the criteria and the real blocker | CG-194, CG-193, CG-163, CG-200, CG-220 | – | still true | gh is unauthenticated in the worker so it cannot read the PR; nothing adds the criteria list or the diagnostic to a revise brief. |
| A brief inlined a dirty README draft from an earlier attempt | CG-234 | – | still true | CG-198 stashes at dispatch, but the brief is built from the worktree before that (fable). |
| CG-181 assumed a retro page that did not exist | CG-181 | CG-146 | fixed | PR #131; CG-178 wired the verdict into it. |
| CG-146's spec named retro paths the tool does not write | CG-146 | – | outdated | The page reads both layouts; the stale path was in the brief. |
| A check run in flight must fence poll and the queue off its task | CG-182 | CG-182, CG-220 | fixed | The guards landed in CG-182; CG-220 added the in-flight worker guard for branch rewrites. |
| retro_question is listed by the notifications endpoint and never emitted | CG-208 | – | still true | CG-225 routes retro questions through kickoff cards; the kind still has no emitter. |
| No JS runtime, headless browser or run skill in the worker environment | CG-208, CG-214, CG-224 | – | still true | CG-214 curled rendered SVG; nothing merged adds a browser. |
| Persona runs share the aux id _persona; the retro lifts the run id from a markdown footer | CG-187 | – | still true | The security persona's low finding confirms the regex accepts any non-space text. |
| A rename left stale callers and the tick's broad try/except kept tests green | CG-191 | – | still true | CG-203 records a phase failure and continues, which is safer but still lets a swallowed AttributeError pass the suite. |
| Dropping HOME logged every worker out | CG-194 | CG-217, CG-218 | fixed | Private HOME carries each harness's config dir; doctor proves login through the scrubbed env; ssh workers covered. |
| A branch fell 55 commits behind during spend-limit retries | CG-200 | CG-212, CG-220 | fixed | The harness pauses instead of burning attempts and a revise starts from origin's head. Astra marked this outdated because the branch merged; fable's reading names the mechanism. |
| garden.yaml still says "once CG-207 lands" | CG-207 | – | still true | Line 34 of the live garden.yaml; a one-line edit in the garden repo (fable). |
| CG-212 and CG-198 both implemented the dirty-worktree stash | CG-212 | CG-220 | fixed | Both merged; CG-220 fixed the ordering race between sync and stash. |
| A killed run left the worktree dirty and blocked retry | CG-158 | CG-198 | fixed | Stash and continue on dispatch; CG-232 clears trial state. |
| The automated review described a head a push had replaced 88 seconds earlier | CG-163 | – | still true | No task makes a review record the SHA it read and discard itself when the head moved. |
| Two review rounds burned on a harness login error | CG-163 | CG-217, CG-237 | fixed | Not-logged-in is an environment stop; CG-237 (phase 05, now merged as PR #191) stops the check reading a worker's prose as a login failure. |
| A branch reset discarded a completed revise commit | CG-178 | CG-220 | fixed | Origin-head starts, lease pushes, no rewrite with a run in flight. |
| CG-224 built a parallel question mechanism because CG-189 was unmerged | CG-224 | CG-225 | fixed | CG-225 redid retro questions through the kickoff cards; CG-189's code was dropped. |
| Dependent tasks merge out of order (CG-229 assumed CG-212; CG-217 depended on CG-212's field names) | CG-212, CG-229, CG-217 | – | still true | Goal 2's "sequenced at planning" has no task; the field names happened to agree. |
| Two of three requested rebase guards already existed | CG-220 | – | disputed | The worker tested the invariants and added only the conflict-rebase guard; the brief's premise was wrong (astra). |
| CG-221's earlier attempt thought CG-214 did not exist | CG-221 | – | outdated | The revise round found the merged Costs page. |
| Ambient CLAUDE_CONFIG_DIR leaks into env tests | CG-218 | – | still true | CG-218 patched its own test; no conftest fixture isolates the variable. |
| design.md and roadmap.md list automatic merging as a non-goal; the scaffolded operate skill says any config change needs a restart | CG-234 | – | still true | Four personas found the same three stale statements on this build. |
| Pre-PR check killed with exit 143 under machine contention | CG-235 | – | still true | Checks run detached but on the shared machine with no retry on a signal exit (fable); astra marks it outdated because two reruns passed, which is true of the symptom and not of the cause. |
| The discovered-item schema has no structured file or error field | CG-199 | – | still true | Dedup is a regex. |
| Phase-03 staff-engineer reviews missing from the path the provenance names | CG-204 | – | still true | Only the product-manager review exists under phase-03/docs/reviews. |
| Where the operator ledger lives | CG-223 | – | answered | The owner chose the product's docs directory; the tool's default still reads the garden root, so both retros printed $0 for the operator. |
| Rich wrap position makes a doctor test flake on path length | CG-217 | CG-217 | fixed | The worker rewrote the assertion; other doctor lines still embed variable-length paths. |
| Brief wording ambiguities (HTMX, walkthrough test placement, two canary spellings, StrictUndefined scope, review-round defaults) | CG-190, CG-195, CG-180, CG-185, CG-200 | – | outdated | Each was resolved in the merged PR. |
| last_diff_hash has consumers beyond the rebase verdict | CG-210 | – | outdated | CG-210 traced and preserved both uses. |
| Restart recovery ordering (run.save, events.emit, state.save) deserves an architecture note | CG-198 | – | still true | The module map also omits kickoff.py, profiles.py, inbox.py and the costs page (staff-engineer). |

## What the personas said

Seven reports, all on claude-fable-5-1: designer 7, product-manager 7, project-manager 7, staff-engineer 7, user 7, usability-expert 6, security 5. They agree the mechanism is right and the late surfaces drifted. Three personas independently found the brief gate's open doors (closed by CG-238). The designer and usability expert list vocabulary and placement drift: the operating profile named three ways, a task id as a Config heading, tick_interval in both Config lists, three commands outside the help groups, the Kickoff panel leading every phase page, question cards in the wrong Inbox group, three disagreeing needs-you counts, a walkthrough renderer that prints hidden panels. The product manager reports three definition-of-done numbers moving the wrong way, no cost-per-accepted-task metric, trial winners and manual-runner PRs never entering the review queue, and Claude model ids hard-coded in the built-in stops. The project manager finds four goal items with no PR. The staff engineer flags two data-integrity hazards created this phase, task files written whole with no concurrency control and retro-filed drafts taking live ids into a branch, and the second one has now happened. The security persona verified three new highs (the git-config escape, reading-path containment, the reload window) and three mediums (fence exemptions for .garden and task files, the harness config dir being the operator's real one, the unscrubbed planner).

## Still open

- The reopen blockers: CG-239 (in revise) and CG-242 (draft).
- Task-file concurrency (CG-243), retro id reservation (CG-244), the planner in the worker environment (CG-245), worker writes to state.json, task files and the harness config dir (CG-246), Mark done through _transition (CG-247): phase 05, first.
- Eight direct status writes outside _transition; no source-grep test for them.
- Briefs: empty and nonexistent reading lists, lists too narrow, generic revise briefs, files inlined from a dirty worktree; no sequencing at planning; retro evidence not inlined.
- Hand merges 16 of 57, cost per easy task $5.04, rebase rounds 1.57, first-pass approval 71 to 79%; no cost-per-accepted-task or first-pass metric per model, tier or harness; no phase-04 walkthrough; tick duration and hand merges not in metrics; the retro's Numbers section reads the wrong ledger path.
- Trial winners and manual-runner PRs do not queue a review on their own (CG-236 covers trials); an in-flight review is swept, not cancelled; redispatch leaves the old worker running; moving the pin is a hand sequence.
- Docs drift: the scaffolded operate skill, design.md and roadmap.md non-goals, the architecture module map; the stale line 34 comment in the live garden.yaml.
- Vocabulary and placement: profile named three ways, task ids in copy, tick_interval twice, unlabeled help commands, Kickoff panel placement, question-card grouping, needs-you counts.
- Built-in stops hard-code Claude model ids and economy routes hard work to haiku.
- Harness error classification is a substring match over the transcript (the CG-237 incident in the persona runs themselves); watch and serve apply RESTART_KEYS differently (staff-engineer).
- retro_question has no emitter; the backlog phase pulldown needs JavaScript; persona runs share one aux id.
- Both judges filed the same 31 persona findings as drafts; one set is kept, refiled as CG-257 to CG-287 in phase 05.
- Accounting: CG-222 sits in phase 06; CG-213, CG-215, CG-216, CG-230, CG-236, CG-237 and CG-250 in phase 05; list them in the closing document with the ratified exceptions.

## What to change

- **First-pass approval is the cost lever.** Cheaper models cut the rate and not the bill per task. Measure cost per accepted task and first-pass approval per model, tier and harness before any routing change, and put the reviewer's usual findings (criteria by name, no scar tissue) into the work brief so the first round passes (operator, both judges).
- **Every path that produces a PR ends in the review queue**, on every runner; resume, review and accept mean the same everywhere (operator, both judges).
- **Recurring hand steps become commands**: redispatch kills the superseded worker; pin runs the canary, installs and restarts after a tick; freeze and close follow the verdict without hand steps (operator; CG-250 covers the reopen path).
- **Measure the definition of done with the tool**: the retro captures its own walkthrough before the personas; hand merges and tick duration in metrics and the rail; the Numbers section reads the ledger where the owner put it.
- **A second judge must not file tasks.** Two reconcile runs from one counter produced the duplicate-id collision the staff engineer predicted; until CG-244 lands, run a comparison judge with filing off.
- **Brief generation is the next quality gate**: refuse an empty reading list, refuse a path that does not exist at build time, build revise briefs from the criteria and the actual failure, inline files from the task's base rather than the worktree.
- **Keep the fence honest.** After CG-239 and CG-242, the remaining mediums (state.json restore, task-file attribution, a private harness config dir, the scrubbed planner) are phase 05's trust goal; say so in the goals text rather than claiming the mechanism matches.

## Features for the next phase

Ranked. Both judges ranked the first two the same; the owner's answers reorder the rest. The feature both judges ranked third (file only high findings, cap the rest) is dropped: the owner decided every finding is filed at its severity with no cap.

1. **Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs page and the retro's Numbers** (CG-251). User value: the operator reads whether a cheaper model lowers the bill per merged task, the finding of this phase. Accepted means merged to the base (CG-228); include revise, review, rebase and failed-run cost without double counting; distinguish unpriced usage from zero (astra). Size: medium. Depends on CG-233 and CG-214 (merged). CG-213 and CG-230 dispatch only after this.
2. **Every PR with no review recorded for its head is queued on the next tick, on every runner** (widen CG-236, phase 05). User value: no PR waits for a hand press; two trial winners waited 45 and 51 minutes and a manual-runner task ignores resume. Also discard a verdict whose head moved and cancel a review whose task went terminal (astra). Size: easy to medium. Depends on nothing.
3. **The retro captures its own walkthrough, hand merges and tick duration are in metrics and the rail, and the Numbers section reads the ledger at the product's docs directory** (CG-253). User value: the definition of done is measured by the tool and the personas read the phase's own pages; the walkthrough renderer skips hidden elements and attributes so reviewers stop filing phantom findings. Size: easy. Depends on CG-182, CG-201, CG-223 (merged).
4. **redispatch kills the superseded worker; pin runs the canary, installs and restarts after a tick** (CG-254). User value: two recurring hand sequences become one command each; a re-dispatch from codex to fable cost $4.34 for a run with no PR. Two sequenced slices (astra). Size: medium. Depends on CG-180, CG-198, CG-220 (merged).
5. **Operating-profile stops name a tier per harness; one word for the operating point; no task ids in copy** (CG-255). User value: a codex garden switching stops no longer gets Claude model names, and the Config page reads as a product. Size: easy to medium. Depends on CG-221 (merged).
6. **A draft's acceptance criteria and reading list can be edited inline on the task page, validated by brief_gaps** (CG-256). User value: the approve card says "fix the brief" and today the only in-app path costs an edit run; with every finding filed as a draft and pruned at approval, the repair path is where the owner will spend their time. Size: medium. Depends on CG-193, CG-190 (merged).
7. **Onboarding: garden onboard drafts a garden from an existing repository** (CG-215, phase 05, the owner's headline). User value: the week-one feature for the next user. Keep the draft as written; it must produce a garden doctor pass on a non-Python fixture with no hand edits and run its planner under the approve gate and the scrubbed environment. Size: hard. Depends on CG-193, CG-224 (merged), CG-238 (merged), CG-245.
8. **A tier names several harness and model options and dispatch spreads runs across them, skipping a paused member** (CG-230, phase 05). User value: the loop keeps working through a quota outage, and each run records its member so item 1 can compare them. Size: medium. Depends on CG-212 (merged) and item 1.
