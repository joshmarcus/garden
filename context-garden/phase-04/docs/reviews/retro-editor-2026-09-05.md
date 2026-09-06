# retro-editor review of context-garden/phase-04

**Persona:** retro-editor · **Score:** 7/10 · 2026-09-05T23:55:39+00:00

Phase 04 made the leaveability mechanism true (a non-blocking tick, live config, harness pauses, restart recovery, hard-tier queue merges, lease pushes, done-means-on-base) and shipped the deferred features, while three definition-of-done numbers moved the wrong way (hand merges 16 of 57, cost per easy task $5.04, first-pass approval 71 to 79%) and the security persona found three new highs in the fence. Both judges said reopen; the joined retro blocks on CG-238 (merged), CG-239 (in revise) and the config-reload hold CG-242, cancels astra's two duplicate blockers, and sends its other five to phase 05 first. The retro process itself produced the defect the staff engineer predicted: two reconcile runs drew ids from one counter, so the retro branch carries duplicate ids and collides with eleven live task files; both retros also printed the operator at $0 because the tool reads the ledger from the garden root while the owner keeps it under the product's docs directory.

## Joined retro

# Retrospective: context-garden/phase-04 (joined)

_One document from two reconcile runs (claude-fable-5-1 at 23:05Z, gpt-6-astra at 23:15Z), the operator's retro and the seven persona reports; where only one judge made a point it is marked (fable) or (astra)._

## Verdict

**Reopen.** Both judges said reopen; they differed on how much must land first. Fable named two blockers, astra eight. The evidence supports three:

- **CG-238** (every path to ready or to a run goes through the approve gate): merged as PR #192. Three personas showed the phase's headline gate had three open doors on the shipped build; goal 2 and a definition-of-done line said it did not.
- **CG-239** (resolve_reading refuses absolute and parent paths; the fence hashes the clone's git config and hooks): PR #193, in a revise round after the automated review found the hooksPath mitigation used a shared, predictable temp directory and a fourth raw git call bypassed the block. The security persona verified on git 2.53 that a worker's config write executes in the scheduler with the operator's credentials, which reopens the self-approve-then-merge path goal 3 says is closed.
- **CG-242** (hold an untrusted garden.yaml change until every in-flight worker's fence manifest agrees with the file on disk) (astra). This is the security persona's third high and phase 04 created the path: CG-192's per-tick reload applies a worker's shell-redirect write to notify.command, checks, setup.command or worker_env.pass ticks before the fence reverts it at reap. Fable filed the same item as a phase-05 follow-up (CG-277 on the retro branch) on the ground that it is not in the frozen goals text; but goal 3 is "trust claims match the mechanism", the garden runs overnight with automerge on for itself, and the owner chose the strict option on the analogous question. It is a medium task in one function of store.py.

Of astra's other five blocking drafts, none must hold the phase open: **CG-240** and **CG-241** duplicate CG-238 and CG-239 and should be cancelled with a reason; **CG-243** (task-file concurrency), **CG-244** (retro id reservation and duplicate ids as a validate problem), **CG-245** (the planner in the worker environment), **CG-246** (workers cannot write state.json, task files or the harness config dir) and **CG-247** (Mark done through _transition and the base-branch rule) are real, backed by the staff-engineer, security and user reports, and become phase 05's first tasks in that order. CG-245 was deferred by CG-194 explicitly and is phase 05's goal 3 in the stub; CG-243 and CG-244 are hazards with a hand workaround; CG-247 is an escape hatch the owner presses.

One thing must happen by hand before the phase closes: the retro branch `garden/retro-context-garden-phase-04` carries both judges' drafts from the same live counter. It holds CG-248, CG-249 and CG-250 twice each, and its CG-240 to CG-250 collide with the eleven files now live under phase-04 and phase-05. Merging it as it stands makes `Store.tasks()` raise on every page and tick, which is the staff-engineer's second high finding, demonstrated by the retro itself. Renumber or refile the branch's drafts before the retro PR merges.

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
- The retro branch's duplicate ids, before its PR merges.
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
- Both judges' persona-finding drafts (CG-246 to CG-276 and CG-253 to CG-283 on the branch) are the same 31 findings filed twice; keep one set.
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

1. **Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs page and the retro's Numbers** (fable CG-240, astra CG-248 on the branch). User value: the operator reads whether a cheaper model lowers the bill per merged task, the finding of this phase. Accepted means merged to the base (CG-228); include revise, review, rebase and failed-run cost without double counting; distinguish unpriced usage from zero (astra). Size: medium. Depends on CG-233 and CG-214 (merged). CG-213 and CG-230 dispatch only after this.
2. **Every PR with no review recorded for its head is queued on the next tick, on every runner** (widen CG-236, phase 05). User value: no PR waits for a hand press; two trial winners waited 45 and 51 minutes and a manual-runner task ignores resume. Also discard a verdict whose head moved and cancel a review whose task went terminal (astra). Size: easy to medium. Depends on nothing.
3. **The retro captures its own walkthrough, hand merges and tick duration are in metrics and the rail, and the Numbers section reads the ledger at the product's docs directory** (fable CG-242, astra CG-251 on the branch). User value: the definition of done is measured by the tool and the personas read the phase's own pages; the walkthrough renderer skips hidden elements and attributes so reviewers stop filing phantom findings. Size: easy. Depends on CG-182, CG-201, CG-223 (merged).
4. **redispatch kills the superseded worker; pin runs the canary, installs and restarts after a tick** (fable CG-243, astra CG-250 on the branch). User value: two recurring hand sequences become one command each; a re-dispatch from codex to fable cost $4.34 for a run with no PR. Two sequenced slices (astra). Size: medium. Depends on CG-180, CG-198, CG-220 (merged).
5. **Operating-profile stops name a tier per harness; one word for the operating point; no task ids in copy** (fable CG-244, astra CG-252 on the branch). User value: a codex garden switching stops no longer gets Claude model names, and the Config page reads as a product. Size: easy to medium. Depends on CG-221 (merged).
6. **A draft's acceptance criteria and reading list can be edited inline on the task page, validated by brief_gaps** (fable CG-245 on the branch). User value: the approve card says "fix the brief" and today the only in-app path costs an edit run; with every finding filed as a draft and pruned at approval, the repair path is where the owner will spend their time. Size: medium. Depends on CG-193, CG-190 (merged).
7. **Onboarding: garden onboard drafts a garden from an existing repository** (CG-215, phase 05, the owner's headline). User value: the week-one feature for the next user. Keep the draft as written; it must produce a garden doctor pass on a non-Python fixture with no hand edits and run its planner under the approve gate and the scrubbed environment. Size: hard. Depends on CG-193, CG-224 (merged), CG-238 (merged), CG-245.
8. **A tier names several harness and model options and dispatch spreads runs across them, skipping a paused member** (CG-230, phase 05). User value: the loop keeps working through a quota outage, and each run records its member so item 1 can compare them. Size: medium. Depends on CG-212 (merged) and item 1.

## Next goals

---
plant: poppy
latin: Papaver argemone
plate: V
---

# phase-05 goals

_Stub written by the operator on 2026-09-05; rewritten by the phase-04 retro (joined from two reconcile runs) with the owner's decisions under Decisions._

**In one sentence: the garden runs in someone else's environment, not only in this one, and it can say what a merged task costs.** Phase 03 made the loop leaveable and phase 04 gave it its features and made the leaveability mechanism true; phase 05 is about adoption: a team points it at a project they already have, on models and machines they already pay for, and the tier map is set from cost per accepted task rather than from a price list.

## Why this phase

A second team cannot use the garden today: setting it up means writing product.md, principles and the setup block by hand, its workers only run on the scheduler's own machine or over ssh from it, and every model call goes through two vendor accounts that both hit their quota on 2026-09-05. Phase 04 also left three numbers pointing the wrong way (hand merges 16 of 57, cost per easy task $5.04, first-pass approval 71 to 79%) and no metric that would tell a routing experiment apart from noise: sonnet halved the run price and did not lower the bill per task. And the security review of the phase-04 build found three new highs and three mediums in the worker fence, two of which block phase 04's close and the rest of which land here first.

## Goals

1. **Onboarding.** `garden onboard` and the `garden-onboard` skill read an existing project and its environment and draft the garden for it (CG-215). Its output passes `garden doctor` on a non-Python fixture with no hand edits, its planner runs in the scrubbed environment, and every draft it writes passes the approve gate.
2. **Any model, at the right price.** An OpenRouter harness with per-tier models and cost from the response (CG-213), as an adapter around an existing OpenAI-compatible CLI rather than a garden-owned tool-calling loop, routed by difficulty with failure-driven escalation and measured by cost per accepted task, per `specs/cost-aware-model-routing.md`. It dispatches only after the measurement in goal 5 has merged.
3. **Shared quotas.** A tier can name several harness and model options and dispatch spreads runs across them, skipping a paused or exhausted account and recording the member on each run (CG-230).
4. **Any machine.** Workers on independent remote hosts that claim runs over HTTP and push results back (CG-216); last in dispatch order, and its acceptance test is a named second team's machine if one exists, a throwaway host otherwise.
5. **What the phase-04 retro adds.**
   - *The numbers exist before the experiments.* Cost per accepted task and first-pass approval per model, tier and harness in `garden metrics`, the Costs page and the retro's Numbers; hand merges and tick duration in metrics and the rail; the retro captures its own walkthrough before the personas run and its Numbers section reads the operator ledger at `context-garden/docs/operator-spend.jsonl`.
   - *Trust, round three.* The planner and the synchronous kickoff run in the worker environment; a worker cannot rewrite state.json, a task file or the harness config dir without it being restored and attributed; notify.command runs scrubbed. These follow CG-239 and CG-242 from the reopen.
   - *One writer, no lost writes.* Task files get optimistic concurrency and a duplicate id is a validate problem, not a fatal exception; retro-filed drafts reserve ids that cannot collide; every status write goes through `_transition` (Scheduler.mark_done and unapprove exist, with a source-grep test); Mark done honours the base-branch rule.
   - *Every PR reaches the queue.* Any PR with no review recorded for its head is queued on the next tick, on every runner (widen CG-236); resume means the same on the manual runner; a review whose head moved is discarded and a review whose task went terminal is cancelled.
   - *Briefs are right the first time.* No brief ships with an empty or unresolved reading list; inlined files come from the task's base, not a dirty worktree; a revise brief restates the criteria and the concrete blocker; dependent tasks are sequenced at planning; retro evidence is inlined; a missing or false criterion is a mechanical changes_requested.
   - *Hand steps become commands.* redispatch kills the superseded worker; pin runs the canary, installs and restarts after a tick; a reopen verdict carries through approve, dispatch and close without hand steps (CG-250).
   - *The surfaces say one thing.* One word for the operating point and stops that name a tier per harness; no task ids in copy; one needs-you predicate; a draft's criteria and reading list editable inline; the scaffolded operate skill, design.md, roadmap.md and the architecture map match the product.

## Non-goals

- Hosted or multi-user operation of the garden itself.
- New UI beyond what the goals need; TUI parity tasks are not filed by default.
- A garden-owned tool-calling loop for OpenRouter; the 20 to 50 task evaluation corpus in the routing spec is phase 06.
- Changing the operating point (workers, tier map) before cost per accepted task can be read.
- A cap on the drafts a retro files (the owner's decision: every finding at its severity, pruned at approval).

## Definition of done

Measured with `garden metrics` against phase 04, by the tool, not by hand.

- A non-Python fixture project is onboarded to a passing `garden validate` and `garden doctor` with no hand-written files.
- One task each completes through OpenRouter and through a remote worker on a throwaway host, reviewed and merged by the loop.
- Cost per accepted easy task at or under $4 (phase 04: $5.04) and first-pass approval at or above 90% (phase 04: 79% easy, 71% medium), both reported per model, tier and harness; the sonnet-era figures from the phase-04 operator retro are the baseline.
- Hand merges zero on every tier and runner (phase 04: 16 of 57); agent rebase rounds per merge under 0.3 (phase 04: 0.55, with 1.02 mechanical by design).
- A phase-05 walkthrough committed by the retro before the personas run; tick duration and hand merges visible in the rail and in metrics.
- No task reaches ready or a run without Scheduler.approve on any surface; no brief ships with an empty or unresolved reading list; no status assigned outside `_transition` (a source-grep test).
- The security persona's three phase-04 highs closed (CG-239, CG-242 and the planner) and its three mediums closed or reworded in the goals as accepted risk; no new high.
- The retro's Numbers section reports the operator's spend and share from the ledger; operator share below phase 04's 29%.
- Every task through `garden tick`; exceptions listed in the closing document.

## Decisions

- **Does the reopen carry all three blocking items, or only the brief-gate closure, with the two security fixes moved to phase 05 as its first tasks?** — answered: All of them. With the user's standing authority: CG-238 is merged and CG-239 is in review, so the reopen carries both; nothing moves to phase 05. Astra's reconcile has since filed CG-240 to CG-247 as further blocking items; which of those block and which become phase-05 follow-ups is settled by the joined retro. (by cli at 2026-09-05T23:43:16+00:00)
- **Joined retro on astra's CG-240 to CG-247:** CG-242 (hold a config reload while an in-flight worker's fence manifest disagrees) joins the reopen as its third blocker; CG-240 and CG-241 are duplicates of CG-238 and CG-239 and are cancelled; CG-243, CG-244, CG-245, CG-246 and CG-247 move to phase 05 and dispatch first, in that order.
- **Is phase 05 about adoption or about cost per accepted task?** — answered: Adoption is the headline (CG-215, CG-213, CG-230, CG-216). Cost per accepted task is measured from the phase's first task as a prerequisite, not the headline. (2026-09-05T23:45Z)
- **How many drafts may a retro file, and at what severity?** — answered: Every finding is filed as a draft at its severity, no cap. The kickoff and the operator prune at approval; a finding that is not worth a task is cancelled with a reason, not dropped silently. (2026-09-05T23:45Z)
- **Phase-05 numbers** — answered: at most $4 per accepted easy task and at least 90% first-pass approval, measured per accepted task, from the sonnet-era baseline. (2026-09-05T23:45Z)
- **Decisions made in the owner's name in phase 04** — answered: ratified: automerge by merge commit, review.max_rounds 4, reviews on the easy tier, the codex tier map luna/terra/sol. The eight queue-rotation hand merges were a bug (CG-176), not a policy. (2026-09-05T23:45Z)
- **Where the operator ledger lives** — answered: one ledger at `context-garden/docs/operator-spend.jsonl`, product and phase attribution welcome. The tool's default path must follow. (2026-09-05T23:45Z)
- **CG-206** — answered: cancelled; browser notifications first, unattended delivery to a phone parked. (2026-09-05T23:45Z)
- **Open:** whether codex stays in bypass-permissions mode once CG-239 and CG-242 land; whether a named second team and repository exist for CG-215 and CG-216, or fixtures are the acceptance claim; whether a self product's second approving round should be a persona or a person rather than the same reviewer twice.

## Carried over from phase 04

Blocking the phase-04 close: CG-238 (merged), CG-239 (PR #193, in revise), CG-242 (draft). Moved here from astra's blocking set, first in dispatch order: CG-243 task-file concurrency, CG-244 retro id reservation and duplicate ids as a validate problem, CG-245 the planner in the worker environment, CG-246 worker writes to state.json, task files and the harness config dir, CG-247 Mark done through `_transition`. Follow-ups filed by the two retro runs on the retro branch (to be renumbered before that PR merges, then kept once): brief completeness and revise briefs, planning sequencing and retro evidence, one writer for status, docs drift, one vocabulary, the walkthrough renderer and check retry on a signal exit, per-phase persona runs and run-id validation, acceptance evidence enforced at review, harness failures classified from structured errors, obsolete reviews cancelled, typed check continuations, a scheduler interface and a module-size test, browser-driven tests for notifications and kickoff, and the small items (retro_question kind, backlog noscript, the ambient config dir in tests, a second opinion for self products). Drafts already here: CG-213, CG-215, CG-216, CG-230, CG-236, CG-237 (merged as PR #191), CG-250; CG-222 sits in phase 06. Cancelled: CG-206, CG-240, CG-241. Exceptions for the phase-04 closing document: sixteen hand merges (eight from the queue-rotation bug), reviews to the easy tier at 14:40Z, mediums to sonnet at 14:50Z, automerge_method merge, review.max_rounds 4, codex in bypass-permissions mode, CG-189 redone as CG-225, CG-234's first run killed by hand, four persona runs discarded and restored by hand after CG-237, and the retro branch renumbered by hand.

## Features for the next phase

- CG-215: Onboarding: garden onboard drafts a garden from an existing repository (the headline)
- Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs page and the retro (fable's CG-240 on the retro branch)
- Widen CG-236: every PR with no review recorded for its head is queued on the next tick, on every runner
- The retro captures its own walkthrough, hand merges and tick duration are in metrics and the rail, and the Numbers section reads the product's ledger (fable's CG-242 on the retro branch)
- redispatch kills the superseded worker, and pin runs the canary, installs and restarts after a tick (fable's CG-243 on the retro branch)
- Operating-profile stops name a tier per harness, one word for the operating point, and user-facing copy drops task ids (fable's CG-244 on the retro branch)
- A draft's acceptance criteria and reading list can be edited inline on the task page (fable's CG-245 on the retro branch)
- CG-230: A tier can name several harness and model options, after the measurement lands
- CG-213: OpenRouter as an adapter around an existing CLI, after the measurement lands
- CG-216: Workers on independent remote hosts, last

## Comparison

# The two judges

| judge | model | cost (list) | duration | retro words | goals words | friction rows | verdict | blocking filed |
|---|---|---|---|---|---|---|---|---|
| fable | claude-fable-5-1 | $2.68 | 5 min 43 s | 5,233 | 1,251 | 36 | reopen | CG-238, CG-239 |
| astra | gpt-6-astra | $0.99 | 7 min 04 s | 6,475 | 1,039 | 79 | reopen | CG-240 to CG-247 |

## Where they agreed

Both said reopen, both named the brief-gate closure and the reading-path and git-config fence as the reasons, and both drew the same numbers from the operator retro (16 of 57 hand merges, $5.04, 1.57, first-pass approval down from 93%). Their "Findings from persona reviews" sections are identical because the tool generates them from the same seven reports; each judge filed the same 31 findings as drafts under different ids. Their feature lists share the top seven items in nearly the same order: cost per accepted task first, widen CG-236 second, a draft cap third, redispatch and pin, the retro's own walkthrough, harness-aware profiles, onboarding as CG-215. Both asked the owner the same six questions, and both marked the CG-181 retro-page item, the CG-194 HOME item and the CG-224 parallel-questions item fixed by the same PRs.

## What each caught that the other did not

**Fable** read the merged work and the live garden closely and its friction verdicts name a mechanism. It cited garden.yaml line 34 still saying "once CG-207 lands" (true in this checkout), CG-231 and CG-232 shipping "not found when the brief was built" entries after CG-193 merged (so the builder annotates a missing path rather than refusing it), CG-233 finding nine unlisted call sites at 20:30Z, the brief being built from the worktree before CG-198's stash runs, the reason no test isolates CLAUDE_CONFIG_DIR, and the accounting that CG-222 sits in phase 06. Its follow-up drafts (CG-277 to CG-288 on the branch) are twelve items with titles a task could carry, and its next-goals draft kept the stub's shape. It was right on all of these; astra reached the same "still true" verdicts on the reading-list items but with evidence of the form "no supplied evidence establishes that briefs now require a populated list", which is absence of evidence stated as a finding.

**Astra** was right on three things fable missed or placed lower. It argued the config-reload window (the security persona's third high) blocks the close because phase 04 created the path; the joined retro adopts that. It promoted the staff engineer's two data-integrity highs to blockers, and its own run then demonstrated the second one: the retro branch now holds CG-248, CG-249 and CG-250 twice and CG-240 to CG-250 collide with live files. It marked two friction items "disputed" (CG-220's brief claiming three missing guards when two existed; CG-221's attempt assuming no Costs page), which is the correct verdict and a category fable lacks. It also asked two questions fable did not: whether CG-206's cancellation means unattended notification is no longer wanted (the owner answered), and whether a self product's second round should be an independent reviewer (still open). Where astra was wrong: it marked the 55-commits-behind branch "outdated" because the branch merged, when CG-212 and CG-220 fixed the cause; it marked CG-235's exit 143 "outdated" because reruns passed, when no retry on a signal exit exists; and eight blockers including three hard tasks would hold phase 04 open for a week to fix hazards that have hand workarounds.

## Verdict and ranking

Same verdict, different blast radius: two blockers against eight. Fable's set matches what the owner then chose; astra's set was over-inclusive by five but under-inclusive by zero. On features the only ranking difference is that astra folds CG-230 in as an eighth item and treats every feature as "reuse the existing draft"; fable filed six new drafts and marked two as duplicates. Both ranked a draft cap third, and the owner overruled both.

## Friction and persona findings

Fable kept 36 rows, one per cause, dropping nothing of substance and marking eight outdated. Astra kept 79 rows, one per report, so the missing-reading-list complaint appears fifteen times with the same verdict; it merged nothing and dropped nothing. Both carried every persona finding into a draft because the tool does that. Fable's "What the personas said" paragraph reads as a summary of the reports with the specifics kept (the three disagreeing needs-you counts, forty drafts, git 2.53); astra's is a paragraph of categories ("admission control", "closure evidence") and includes a line about which task list it trusted, which is process narration the retro should not carry.

## Writing

Fable is specific: task ids, timestamps, line numbers, a number per claim, and no history of its own making. Its weakest part is the Numbers section, which the tool rendered wrong for both ($0 operator). Astra is a quarter longer and reads as a compliance report: abstract nouns, verdict evidence phrased as what was not supplied, and a next-goals draft that abandoned the stub's structure (no Goals, Non-goals, Definition of done, Carried over headings) and reframed the stub's four named goals as "entry conditions" and prose sections. Neither has scar tissue in the PR-description sense. On the raw counts astra costs 37% of fable and takes 24% longer.

## Which judge next time

Use fable as the judge that writes the document and files the tasks. Its friction verdicts point at the PR or the line that settles them, its drafts are tasks, and its goals draft is the owner's stub with the retro's additions rather than a new document. Astra's run earned its $0.99 in one place, the blocking set, where its stricter reading of three security and integrity findings was the better call and the joined retro adopts one of them; it also proved a staff-engineer finding by reproducing it. That is worth a second run when the verdict is reopen, and not otherwise, and only in a mode that files nothing: two judges drawing ids from one counter cost the operator a hand renumbering of the retro branch, and a second copy of every persona finding. Once CG-244 reserves ids, a second judge run on the cheaper model as a check on the blocking set is a reasonable standing practice for a reopen; for a close-with-follow-ups verdict one judge is enough.

## High

- **retro ids** — Both reconcile runs filed drafts from the same live counter, so the retro branch holds CG-248, CG-249 and CG-250 twice and its CG-240 to CG-250 collide with the eleven task files now live in phase-04 and phase-05; merging the retro PR would make Store.tasks() raise on every page and tick.
  - suggestion: Renumber the branch's drafts by hand before the retro PR merges, keep one copy of the 31 persona-finding drafts, land CG-244 (reserved ids, duplicate id as a validate problem) first in phase 05, and never run a second judge with task filing on until it does.

## Medium

- **retro numbers** — Both retro documents report the operator at $0.00 and 0% of total because the Numbers section reads <garden root>/docs/operator-spend.jsonl while the ledger the owner chose is at context-garden/docs/operator-spend.jsonl, so the phase-04 definition-of-done line on operator share is unverifiable from the retro.
  - suggestion: Point operator_spend.default_path at the product's docs directory (or a config key), re-render the Numbers section with $195 of $669 and 29%, and add a retro test that a ledger at the configured path is read.
- **retro questions** — The two runs asked the same six questions in different words and each was answered separately, so phase-05/goals.md now carries every decision twice; the reconcile also filed blocking tasks with no acceptance criteria and an empty reading list, which the approve gate then refused (CG-250 records this).
  - suggestion: Deduplicate questions across retro runs by normalised text before filing cards, and have the reconcile brief require criteria, reading list and difficulty on every blocking item (CG-250 covers the second half).

_garden persona run 20260905T234503Z-persona_
