# Retrospective: context-garden/phase-04

_2026-09-05T23:15:10+00:00 · hard tier (gpt-6-astra)_

## What changed

Phase 04 shipped asynchronous checks and rebases, a responsive action path, hard-tier queue merging, live config reload, restart and quota recovery, stronger web and worker trust checks, the CLI split and shared queue/rebase machinery, plus retro decisions, backlog and task creation, costs, observation, profiles and trial improvements. The supplied final list takes precedence over earlier persona snapshots: CG-189 and CG-225 are marked done, CG-206 is cancelled, and CG-238 and CG-239 remain drafts. Persona-reported operational results miss several goals: 16 of 57 hand merges, $5.04 per easy task against $4, 1.57 rebase rounds per merge against 0.2, and 71–79% first-pass approval versus 93% previously; the denominators and mechanical/agent split need explicit reconciliation. Operator share is reported below one third, but an exact ledger-backed comparison with the phase-goals baseline of about 60% is not supplied. Reviewers report green lint and roughly 961–962 passing tests with three skipped, and modules below 800 lines; there is no phase-04 walkthrough or aggregate tick-duration evidence. The phase cannot close while the documented security, task-integrity and admission-control blockers remain.

## Numbers

- workers: $477.34
- operator: $0.00 — 0% of total
- total: $477.34

## Verdict

**Reopen.**
These must land before context-garden/phase-04 can close; each carries a freeze exception so it still dispatches.

Follow-ups filed in phase-05:
- CG-284: Build revision briefs from current criteria and failure evidence
- CG-285: Sequence tasks that share a behavior or schema
- CG-286: Enforce acceptance evidence at review finalization
- CG-287: Classify harness failures from structured error results
- CG-288: Cancel obsolete review runs when tasks finish
- CG-289: Make check continuations explicit and recoverable
- CG-290: Enforce scheduler interfaces and the module-size cap
- CG-291: Unify actionable counts and brief-repair controls
- CG-292: Finish phase-page and CLI interaction consistency
- CG-293: Test notification and kickoff behavior in a browser
- CG-294: Align config reload behavior and operating documentation
- CG-295: Validate persona-run provenance and scrub notifications

Blocking tasks filed in this phase:
- CG-240: Complete CG-238: enforce approval and single-run admission — The phase explicitly promises that incomplete briefs never consume runs, yet demonstrated UI and CLI paths bypass the gate and can launch competing workers.
- CG-241: Complete CG-239: contain reading paths and scheduler git — The security review demonstrates both arbitrary local-file disclosure into model prompts and worker-triggered code execution with scheduler credentials.
- CG-242: Hold untrusted config changes before live reload — Live reload currently activates a worker's configuration write before the fence can reject it, creating a newly introduced privileged execution path.
- CG-243: Preserve task actions across concurrent ticks and moves — The action/tick split can silently discard user decisions and can turn a routine move into duplicate IDs that stop the entire garden.
- CG-244: Reserve retro task IDs and survive duplicate records — Running this phase's own retro can create colliding task IDs whose merge disables every page and tick, so postponing the fix would expose closure itself to the defect.
- CG-245: Isolate planner execution from operator state — A stated phase trust goal remains unshipped, and model-written documents currently drive an edit-capable process in the live garden with operator credentials.
- CG-246: Prevent workers from mutating shared control and harness state — The reported remaining write paths can forge approval evidence or execute code in later operator sessions, undermining the phase's trust guarantees even after git and reload fixes.
- CG-247: Make completion honor the product base branch — The current Mark done action contradicts CG-228's delivered completion invariant and can tell the owner that unshipped work is finished.

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Retro page assumed before it existed | CG-181 | CG-146 / #131 | fixed | CG-146 merged the dedicated phase retro page that CG-181's earlier brief assumed existed. |
| Reading list omitted in-tick check sites | CG-182 | – | still true | CG-182 converted the sites, but later workers repeatedly report incomplete reading lists, so the brief-generation gap remains. |
| Single-tick criteria conflicted with asynchronous checks | CG-182 | CG-182 / #129 | fixed | The report records updating approximately ten single-tick tests as check stages became asynchronous run records. |
| In-flight checks needed poll and queue fences | CG-182 | CG-182 / #129 | fixed | CG-182 shipped checks outside the tick with the reported task guards; later findings concern different continuation and concurrency defects. |
| Missing reading list for CLI and rebase split | CG-197 | – | still true | The split merged, but no supplied evidence establishes that briefs now require a complete, populated reading list. |
| Notifications advertise an unemitted retro_question event | CG-208 | – | still true | CG-225 supplies retro decision cards, but the later project-manager review still reports no emitter for the notification endpoint's retro_question kind. |
| Retro artifact layout in the spec was stale | CG-146 | – | still true | CG-146 handles both layouts, resolving page compatibility without evidence that the contradictory artifact-path guidance was corrected. |
| Notification JavaScript lacks execution tests | CG-208 | – | still true | Repeated reports describe structural HTTP-only coverage, and no merged task establishes a JavaScript execution harness. |
| Web and CLI task equivalence had ambiguous inputs | CG-132 | – | still true | The worker tested equivalent CLI-supported inputs with web-only fields blank, but the supplied evidence does not resolve the broader acceptance-contract ambiguity. |
| Rebase criterion described already-unified call sites | CG-202 | CG-197 / #130 | fixed | CG-197 had already replaced the four rebase implementations with the recorded helper before CG-202 ran. |
| Hard-tier queue brief had no reading list | CG-191 | – | still true | The queue implementation merged, but a missing reading list is not repaired by completing that implementation. |
| Persona runs share the _persona task identity | CG-187 | – | still true | CG-187 explicitly retained a lookup workaround, and no supplied merge changes persona-run identity to be phase-specific. |
| Retro verdict needed a first-class retro-page surface | CG-178 | CG-178 / #139 | fixed | CG-178's later revision report describes wiring retro_verdict into the dedicated retro page and testing the post-merge document path. |
| Vocabulary task dispatched with placeholder criteria | CG-156 | – | still true | CG-193 added an approve gate, but later persona demonstrations and draft CG-238 establish that other dispatch paths still bypass it. |
| Vocabulary task bundled scope that had to be inferred | CG-156 | – | still true | The worker selected four title-level changes, while the project-manager review confirms planning-time scoping and sequencing remain unshipped. |
| Renamed queue helper left stale callers hidden by tick handling | CG-191 | – | still true | The report identifies an integration blind spot, and the staff-engineer review still finds undeclared cross-mixin calls without an enforced interface. |
| Product-manager persona path belonged to the driving garden | CG-188 | – | still true | The editable source is DEFAULT_PERSONAS in personas.py, and no supplied merge corrects repository ownership in generated reading guidance. |
| Canary brief had no reading list | CG-180 | – | still true | The canary shipped, but the worker's missing context remains part of the recurring brief-completeness problem. |
| Canary command had two proposed spellings | CG-180 | CG-180 / #145 | fixed | The worker selected garden canary, and subsequent persona reviews identify canary as an existing CLI command. |
| Brief described a nonexistent HTMX dependency | CG-190 | – | still true | The shipped implementation uses vanilla JavaScript, but no supplied evidence shows the misleading brief wording was corrected. |
| Template guarantee was broader than the named sites | CG-185 | CG-185 / #147 | fixed | The worker reports auditing and fixing sparse template accesses under strict mode, and the designer credits the resulting page-error handling. |
| Live versus restart config boundaries were undocumented | CG-192 | CG-192 / #148 | fixed | CG-192 introduced RESTART_KEYS and a Config-page explanation, although personas identify separate remaining inconsistencies in those surfaces and loop behavior. |
| Brief-gate task itself had no reading list | CG-193 | – | still true | Later tasks still report absent or invalid reading lists, and the gate does not establish that every brief includes all necessary files. |
| Retro-answer timing omitted live versus PR-worktree distinction | CG-189 | – | still true | CG-225 replaces the question mechanism, but no supplied evidence establishes that briefs now explain when retro artifacts become live. |
| Discovery dedup relies on free-text file and error heuristics | CG-199 | – | still true | CG-199 merged heuristic matching without a structured file/error identity, and no later merge supplies one. |
| Restart recovery brief had no reading list | CG-198 | – | still true | The worker had to locate recovery and dispatch modules, with no supplied correction to the missing-context mechanism. |
| Trust-policy brief omitted its reading list | CG-200 | – | still true | The trust changes merged, but later reports continue to demonstrate absent reading context. |
| Resolved review-round defaults lose explicit-setting provenance | CG-200 | – | still true | The implementation uses absence of a per-product override as a workaround, with no merged provenance-aware config resolution shown. |
| Live-garden retro-tier comment was outside the checkout | CG-207 | – | still true | CG-207 and CG-235 remove the need to retune the review tier, but neither supplied evidence confirms editing the separate driving garden's comment. |
| Removing HOME broke harness authentication | CG-194 | CG-217 / #169; CG-218 / #176; CG-212 / #168 | fixed | Merged work supplies harness config defaults, remote-worker handling and auth environment stops, while the security of sharing writable config directories remains a separate open finding. |
| Worker isolation brief omitted its reading list | CG-194 | – | still true | The worker still had to discover the relevant modules, and no general completeness fix is evidenced. |
| Generic revision feedback concealed a rebase conflict | CG-194 | – | still true | The conflict is historical, but later CG-163 and CG-220 reports confirm feedback still omits the actionable blocker or sufficient diagnostic detail. |
| Walkthrough test wording did not specify the test module | CG-195 | – | still true | The scenario test location was inferred, and no supplied change clarifies when a brief requires docs capture versus a behavioral walkthrough test. |
| Trust branch was 55 commits behind after quota pauses | CG-200 | CG-200 / #155 | outdated | The branch subsequently merged, so its paused and conflicted worktree state is no longer an open defect. |
| Trust revision requested nonexistent review comments and CI | CG-200 | – | still true | The merge conflict was resolved, but generic review instructions without actual feedback recur in later worker reports. |
| Referenced staff-engineer review evidence was unavailable | CG-204 | – | still true | The worker reconstructed scope from goals and history, and the project-manager review confirms retro evidence inlining remains unshipped. |
| Revision brief omitted original acceptance criteria | CG-193 | – | still true | CG-179 added criterion reporting, but this later revision still lacked the list and personas found missing evidence accepted at merge. |
| Patch-id reading list omitted other diff-hash consumers | CG-210 | – | still true | The worker traced checkruns and poll independently, demonstrating an unresolved dependency-context gap rather than an unmerged patch-id change. |
| Verdict brief omitted separate retro route and merge timing | CG-178 | – | still true | The page integration landed, but the reading-list and artifact-lifecycle omission was not itself shown to be corrected. |
| CG-198 seemed absent and overlapped dirty-worktree stashing | CG-212 | CG-198 / #154; CG-212 / #168; CG-220 / #172 | fixed | All three tasks merged recovery, quota handling and stash/sync ordering, so planning CG-198 again would duplicate completed work. |
| Manual-task brief retained placeholder acceptance criteria | CG-158 | – | still true | The project-manager review explicitly confirms the placeholder criterion survived merge, and CG-238 remains a draft covering gate bypasses. |
| Killed attempts left dirty worktrees and blocked retries | CG-158 | CG-198 / #154; CG-212 / #168; CG-220 / #172 | fixed | The merged recovery and branch-start work implements dirty-worktree stashing and orders it with origin synchronization. |
| Automated review apparently inspected a pre-push revision | CG-163 | – | still true | The worker cites the already-pushed fix, and no supplied merge demonstrates review results are validated against the exact reviewed head. |
| Authentication failures consumed review rounds | CG-163 | CG-217 / #169; CG-212 / #168; CG-227 / #183 | fixed | Merged auth classification and environment-stop handling extend harness pauses across review and retro dispatch, though false-positive classification remains open. |
| Quota pause consumer was absent during auth work | CG-217 | CG-212 / #168 | fixed | CG-212 subsequently merged the environment-stop consumer that CG-217 could not exercise on its earlier checkout. |
| Doctor mocks assumed the old auth-status command | CG-217 | CG-217 / #169 | fixed | The worker explicitly updated the five affected tests to match the trivial-prompt login check. |
| Recovery persistence and event ordering need documentation | CG-198 | – | still true | No supplied merge adds the requested lifecycle design note, and the staff-engineer review identifies related check continuation recovery risks. |
| Costs UI lacked a supported browser verification workflow | CG-214 | – | still true | Later personas rendered throwaway gardens, but no merged work provides repeatable browser execution coverage for the new interactions. |
| Branch reset discarded a completed local revise commit | CG-178 | CG-220 / #172 | fixed | CG-220 establishes origin-head starts, lease pushes and in-flight queue guards to address competing branch writers; broader concurrent redispatch remains a separate finding. |
| Worker could not read live GitHub comments without GH_TOKEN | CG-163 | – | still true | No supplied change gives the worker complete inlined review evidence, and restoring unrestricted operator credentials would conflict with the isolation goal. |
| Revision feedback was generic rather than actionable | CG-163 | – | still true | Later diagnostic reports still describe omitted files and truncated failures, with no merged feedback-contract fix shown. |
| Doctor console test depended on temporary path length | CG-217 | CG-217 / #169 | fixed | The revision identified the wrapping-sensitive assertion and the final merged build is reported green, without evidence of a remaining doctor regression. |
| Observe reading list named nonexistent cli/reports.py | CG-219 | – | still true | Observe lives in cli/loop.py, and subsequent CG-223 reports repeat the nonexistent reports.py reference. |
| Generated operate skill was presented as a local source file | CG-219 | – | still true | The editable source remains scaffold.py, and CG-234 later reports the same generated-file versus driving-garden confusion. |
| Auth revision depended on unmerged quota field names | CG-217 | CG-212 / #168; CG-217 / #169 | fixed | Both sides of the env_error/env_kind integration merged, although planning unmerged sibling contracts remains unresolved. |
| Two requested rebase guards already existed | CG-220 | – | disputed | The worker tested the existing invariants and found only one new guard necessary, so the claim that all three sites lacked protection was incorrect. |
| Operator-spend brief named nonexistent cli/reports.py | CG-223 | – | still true | The relevant CLI implementation is cli/costs.py, with no supplied correction to the reading-list source. |
| Operator-spend ledger root was unspecified | CG-223 | – | still true | The worker chose garden-root docs/operator-spend.jsonl, but the supplied phase goals and evidence do not record owner confirmation of attribution and layout. |
| Kickoff and retro built parallel question mechanisms | CG-224 | CG-225 / #184 | fixed | CG-225 explicitly reimplements retro questions through kickoff's mechanism, superseding the integration concern about CG-189. |
| Kickoff panel lacks browser-driven tests | CG-224 | – | still true | The report names scheduler-only coverage and no later merge adds browser testing for the panel. |
| Quota brief failed to enumerate every dispatch mode | CG-212 | – | still true | CG-212 and CG-227 complete additional paths, but no merged planning change ensures future cross-cutting briefs enumerate all consumers. |
| Pre-PR feedback truncated the ordering failure diagnosis | CG-220 | – | still true | The worker located the stash/sync race manually, and no supplied merge improves diagnostic payload completeness. |
| SSH test inherited ambient harness config variables | CG-218 | CG-218 / #176 | fixed | The worker explicitly removed ambient variables in the test fixture before validating remote defaults. |
| Costs page was incorrectly assumed not to exist | CG-221 | CG-214 / #170 | disputed | The reviewer identified the already-merged Costs page, so the premise for skipping integration was false. |
| Done-status brief omitted status-keyed UI consumers | CG-228 | – | still true | The worker found CLI, TUI, template and scheduler consumers by repository search, with no subsequent brief-impact inventory fix shown. |
| TUI kickoff-answer task had no acceptance criteria | CG-226 | – | still true | This late-phase task still verified against its goal rather than explicit criteria, demonstrating that the approval promise was not universal. |
| Trial quota integration awaited CG-212 | CG-229 | CG-212 / #168; CG-229 / #182 | fixed | Both the generic trial environment-error consumer and quota classifier are now merged. |
| Trial setup brief named nonexistent tests/test_trials.py | CG-229 | – | still true | Trial scheduler coverage lives in tests/test_extras.py, and later trial briefs repeat the same invalid path. |
| Quota resume revision omitted scheduler/human.py | CG-212 | – | still true | The worker had to discover the actual resume dispatcher separately, and no context-generation correction is evidenced. |
| Trial-wait brief named nonexistent tests/test_trials.py | CG-231 | – | still true | The worker identifies tests/test_extras.py and tests/test_cli.py as the real locations, including an existing branch test the revised brief missed. |
| Trial-again brief named nonexistent trial tests and CLI module | CG-232 | – | still true | The actual files are tests/test_extras.py and cli/loop.py, not tests/test_trials.py and cli/reviews.py. |
| Quota review fix omitted review.py from the reading list | CG-212 | – | still true | The missing module contained both the blocking finding and the fix, illustrating that revision context was not built from the actual failure. |
| Unsequenced quota and trial changes caused a semantic conflict | CG-212 | – | still true | The integrated tasks merged, but the project-manager review confirms the promised planning-time dependency and scope control has no implementation. |
| Codex cost brief omitted RunStore and usage-copy consumers | CG-233 | – | still true | The worker had to trace approximately nine run-finalization sites beyond the apparent harness change, with no impact-aware brief fix shown. |
| README brief inlined leftovers from earlier attempts | CG-234 | – | still true | The worker recovered main's README manually, and the report occurred after recovery improvements without evidence that brief excerpts now identify their source revision. |
| README draft placed doctor before garden initialization | CG-234 | CG-234 / #189 | fixed | The usability review followed the shipped README and confirms its command sequence matches CLI requirements. |
| Operate skill source and live copy diverged | CG-234 | – | still true | Multiple final personas confirm the scaffolded skill still contradicts live reload and differs from the driving garden's operating guidance. |
| Design document still calls automatic merging a non-goal | CG-234 | – | still true | Designer, product-manager and project-manager reviews independently confirm stale merge-queue guidance in design.md and roadmap.md. |
| README reading list omitted config and automerge defaults | CG-234 | – | still true | The README shipped, but its worker report identifies missing authoritative behavior sources with no generator correction shown. |
| Pre-PR suite was terminated near completion | CG-235 | – | outdated | Two identical reruns passed in the same worktree, so the isolated exit 143 does not establish a persistent regression or prove resource contention as its cause. |

## What the personas said

Designer, product-manager, project-manager, staff-engineer and user scored the phase 7/10, usability 6/10 and security 5/10. They agree the structural and usability improvements are substantial, but broad completion claims exceed the mechanism: approval and done-state bypasses remain, new concurrent writes can lose actions or create fatal duplicate IDs, and the security review demonstrates shared-git execution, reading-path disclosure and unsafe config-reload paths alongside planner and harness-directory exposure. Product management prioritizes cost per accepted task, review coverage on every runner and onboarding, with a smaller retro triage burden; design and usability prioritize consistent counts, profile vocabulary, truthful config guidance and representative walkthroughs. The earlier claim that the three previous security highs were closed does not resolve the newly demonstrated attack chains. Reports conflict on CG-189's status and historical task counts, so this report uses the supplied final task list and treats live metrics as reported rather than independently verified.

## Still open

- CG-238 remains draft: Dispatch now, new-task approve-now and garden take bypass the common approval gate; repeated dispatch can orphan an active run.
- CG-239 remains draft: reading paths can escape their roots and shared git metadata can execute code in the scheduler; its acceptance scope must include prevention before scheduler git runs.
- Live reload can apply worker-written executable configuration before fence recovery.
- Task-file writes can overwrite concurrent user actions, and a move can resurrect an old path and create a fatal duplicate ID.
- Retro drafts allocate IDs on a branch without durable live reservation; a later merge can collide with live-created tasks.
- Planner execution still uses the operator environment in the live garden; workers can modify shared harness configuration and insufficiently protected task/run/state files.
- Mark done bypasses both the shared transition path and the promised base-branch completion invariant.
- Review coverage is incomplete for trial winners and manual runners; terminal tasks do not promptly cancel in-flight review processes.
- Brief generation still omits criteria, repository ownership, current source revisions, relevant call sites and precise failure evidence; dependency sequencing and retro-evidence inlining remain unshipped.
- Criterion evidence is reported but not mechanically enforced; discovery matching remains heuristic and persona-run history uses a shared identity.
- Cost per accepted task and first-pass approval by model, tier and harness are absent; reported phase outcomes miss hand-merge, rebase and easy-cost targets.
- Phase-04 walkthrough, aggregate tick timing, exact operator-share comparison and the complete dispatch/hand-merge exception ledger are missing.
- Harness-error classification can mistake quoted prose for auth/quota failures; CG-237 is referenced as a remedy but no final status or merged PR is supplied.
- Profiles hard-code Claude models, config surfaces disagree about restart keys, and watch and serve apply config differently.
- Retro and kickoff can produce excessive drafts; changing CG-187's all-findings policy requires an owner decision.
- Browser execution coverage is absent for notifications and kickoff; retro_question notifications, backlog noscript submission and walkthrough parsing/page coverage remain incomplete.
- UI counts, approve affordances, phase-page kickoff placement, help grouping, task-phase controls, activity labels and first-run guidance remain inconsistent.
- Scaffolded operator guidance, design.md, roadmap.md and the architecture map are stale; the separate driving-garden comment and operator-spend ledger location remain unconfirmed.
- Recurring hand operations need safe redispatch and a canary-backed pin command; safe reset work does not prevent two independently dispatched workers sharing a worktree.
- CG-206 is cancelled, so configured live notify.command is not demonstrated; browser notifications do not establish unattended notification coverage.
- CG-213, CG-215, CG-216 and CG-230 are identified in the product-manager report as next-phase work, but their detailed final statuses are not supplied; CG-222's disposition is unaccounted for.
- Check continuations lack typed persisted state and safe failure handling, status still has multiple writers, scheduler coupling lacks an interface/size enforcement, and some production helpers exist only for tests.

## Questions for the owner

- **Should phase 05 make onboarding the headline, with cost measurement as its first prerequisite, or make cost reduction the headline?** — decision card `20260905T230805Z-retro-q0`
  - The product-manager report identifies adoption and cost as competing phase scopes; the draft goals below assume onboarding after measurement.
  - options: Onboarding headline; measurement first, Cost reduction headline; onboarding follows
- **Which second team and existing repository will serve as the onboarding acceptance user?** — decision card `20260905T230805Z-retro-q1`
  - CG-215 can be validated against a non-Python fixture, but that alone does not demonstrate adoption by a real team.
  - options: Name a team and repository, Use a fixture and describe the result as fixture validation
- **Should retros keep filing every finding, or automatically file only high findings with an eight-draft cap and retain all others for explicit filing?** — decision card `20260905T230805Z-retro-q2`
  - CG-187 deliberately preserves every severity as drafts; changing that behavior requires a policy decision, and medium and low findings must remain visible either way.
  - options: High findings only; cap eight automatic drafts, High findings only; choose another cap, Keep every finding as a draft
- **Should Codex bypass permission mode remain the live operating policy after the required containment fixes, or should the live garden return to sandboxed execution?** — decision card `20260905T230805Z-retro-q3`
  - The product-manager reports an operator-selected bypass, while security demonstrates concrete failures of the existing fence; this decision does not waive the mandatory blocker fixes.
  - options: Return to sandboxed execution, Retain bypass after validated containment fixes
- **Do you ratify the phase's merge method, four-round review cap, easy-tier reviews, Codex tier map and eight queue-rotation hand merges?** — decision card `20260905T230805Z-retro-q4`
  - These were reported as decisions made in the owner's name and need an explicit closing-record disposition, with the eight rotation merges distinguished from the reported sixteen total hand merges.
  - options: Ratify with the exceptions recorded, Revisit the operating settings individually
- **Are phase-05 targets of at most $4 per accepted easy task and at least 90% first-pass approval the intended acceptance thresholds?** — decision card `20260905T230805Z-retro-q5`
  - The goals draft uses these proposed targets, but they require consistent cost allocation and a fixed comparison cohort before they can guide routing.
  - options: Adopt both targets, Set targets after the baseline is measured
- **Should operator sessions use one garden-root docs/operator-spend.jsonl ledger with explicit product and phase attribution?** — decision card `20260905T230805Z-retro-q6`
  - CG-223 chose a garden-root ledger, while the goals refer to phase reporting and the exact historical operator-share comparison is not supplied.
  - options: Garden-root ledger with explicit attribution, Product-level ledgers with garden-wide aggregation
- **Was CG-206 cancelled because browser notifications are sufficient, or is unattended notification delivery still required?** — decision card `20260905T230805Z-retro-q7`
  - The final list cancels the live notify.command task, and an open browser tab does not cover the original overnight notification goal.
  - options: Browser notifications are sufficient, Keep unattended delivery as a live-garden follow-up
- **Should self-product approval require an independent second reviewer or retain repeated rounds from the same reviewer?** — decision card `20260905T230805Z-retro-q8`
  - Security notes that repeated automated approval is not independent evidence; this is a policy enhancement beyond the mandatory execution and data-containment fixes.
  - options: Require an independent second reviewer, Retain the current two-round policy

## Findings from persona reviews

### High

- **designer** — The rail, Config page, CLI and status line use 'operating profile', 'stop' and 'profile' for the same control, and 'profile' also names the separate observe feed level. → CG-253 [draft]
- **designer** — The Kickoff panel with a primary 'Kick off' button is the first thing on every open phase page, above the verdict, progress and task table, even on a phase well underway. → CG-254 [draft]
- **project-manager** — run_planner copies os.environ wholesale so the planner still sees the operator's HOME and tokens, leaving goal 3's 'planner runs in the worker environment' unshipped. → CG-267 [draft]
- **project-manager** — garden take flips a draft to ready by hand, bypassing brief_gaps, phase_refusal and the kickoff warning that every other approve path enforces. → CG-268 [draft]
- **user** — Dispatch now on a draft and the New task form's approve-now both skip the approve gate, so a task with placeholder criteria dispatches a run. → CG-277 [draft]
- **user** — The Mark done button on every in-review card sets status to done directly in the web action, bypassing _transition and the done-means-on-base rule from CG-228. → CG-278 [draft]

### Medium

- **designer** — A draft with brief gaps shows 'Fix the brief before approving' beside an enabled primary 'Approve into…' button whose press only produces a refusal flash. → CG-255 [draft]
- **designer** — tick_interval is listed both under live re-read values and under 'Needs a restart', and the operating-profile panel's eyebrow reads 'CG-221' (the CLI help also cites the task id). → CG-256 [draft]
- **designer** — move, retro-decide and canary appear in an unlabeled Commands box above the named help groups CG-156 introduced. → CG-257 [draft]
- **designer** — A draft task page shows both 'Approve into [phase]' and a separate move 'phase' pulldown listing the same phases with different submit behaviour, and the Inbox shows the approve pulldown even with a single option. → CG-258 [draft]
- **designer** — Kickoff and retro question cards sit in the 'Needs a decision' group whose description says the loop stopped on a stall, cap, closed PR or failed worker. → CG-259 [draft]
- **designer** — garden walkthrough still captures the phase-02 page set; Costs, the backlog view and the retro page are never captured for persona review. → CG-260 [draft]
- **designer** — The scaffolded garden-operate skill says any config change needs a restart, and docs/design.md lists automatic merging as a non-goal, both contradicting the shipped product. → CG-261 [draft]
- **project-manager** — CG-217 merged with a criterion marked 'no evidence given' and CG-158 with a placeholder criterion, so the CG-179 rule that an unevidenced criterion blocks is not being applied. → CG-269 [draft]
- **project-manager** — Hand merges, rebase rounds per merge, cost per easy task and the operator's share of spend are only measurable from the live garden and are not evidenced anywhere in the merged work. → CG-270 [draft]
- **project-manager** — The generated garden-operate skill still says any config change needs a restart, and design.md and roadmap.md list automatic merging as a non-goal while the merge queue shipped. → CG-271 [draft]
- **project-manager** — Goal 2's 'two tasks serving one goal are sequenced or scoped at planning' and 'retro evidence inlined into the brief' have no task and no PR. → CG-272 [draft]
- **user** — The built-in economy, balanced and fast stops hardcode Claude model ids and model_for applies a stop's tier map to any harness, so a codex garden switching stops gets Claude model names. → CG-279 [draft]
- **user** — The approve card says to fix the brief but the task page offers no way to edit criteria or the reading list; the only in-app path costs an edit run. → CG-280 [draft]

### Low

- **designer** — The worker's question is printed twice on its card because the reason line and the question line carry the same text. → CG-262 [draft]
- **designer** — Resume, trial, compare and edit runs fold into an unnamed 'other' activity that can be a large share on a small garden. → CG-263 [draft]
- **designer** — Spend appears three ways in the rail (a whole-dollar Runs figure, a Costs link, an hourly rate) and the rounded figure disagrees with the Inbox KPI; the profile select's default reads 'plain garden.yaml values'. → CG-264 [draft]
- **designer** — The Costs form submits every select on change yet keeps a visible Filter button, unlike the noscript fallback the rail uses. → CG-265 [draft]
- **designer** — A cancelled task's only action is 'Continue the loop', the TUI label is 'Continue loop', and the phase page names a 'planner-tier' review no surface defines. → CG-266 [draft]
- **project-manager** — CG-206, CG-213, CG-215, CG-216, CG-222 and CG-230 appear in no merged PR and their status is unknown from this checkout. → CG-273 [draft]
- **project-manager** — An in-flight review whose PR merges is swept by reap_orphaned after it finishes rather than cancelled, so the model run still spends to completion. → CG-274 [draft]
- **project-manager** — Persona findings at every severity, kickoff items and retro follow-ups all file drafts, so phase 05 is likely to open with an unreadable approve queue. → CG-275 [draft]
- **project-manager** — The backlog phase pulldown needs JavaScript (CG-163) and the notification endpoint lists a retro_question kind nothing emits (CG-208). → CG-276 [draft]
- **user** — tick_interval appears both under live re-read values and under the needs-a-restart list. → CG-281 [draft]
- **user** — The Costs page files a resume round as 'other', and garden observe's digest reported one failed run on a QA garden whose event log has no failed transition. → CG-282 [draft]
- **user** — With every phase closed, garden status prints an empty table and its legend before the closed-phase note. → CG-283 [draft]

## Features for the next phase

1. **Measure cost per accepted task and first-pass approval** — CG-248 [draft]
   - size: medium
   - why now: Outcome-based cost measurement must precede another routing or concurrency experiment.
   - User value: compare models by the cost of delivering accepted work, including unsuccessful attempts, rather than run price. Why now: easy-task cost rose to $5.04 while approval rates fell, so routing experiments currently lack an outcome measure. Size: medium. Dependencies: merged CG-233 and CG-214. Add consistent model, tier and harness cohorts to metrics, Costs and retro Numbers; accepted means merged to the product base. Define mixed-model attribution and include revise, review, rebase and failed-run costs without double counting. Gate CG-213 and CG-230 evaluation on this measurement.
2. **Queue every unreviewed PR on every runner** — _skipped: flagged by the retro as a duplicate of CG-236_
   - size: medium
   - why now: The existing CG-236 should finish the review-queue promise across all PR-producing paths.
   - User value: trial winners and manual-runner PRs progress without a hand press. Why now: the report records 45- and 51-minute waits and sixteen hand merges. Size: medium. Dependencies: existing review and poll machinery. Widen existing CG-236 to queue any eligible PR whose current head lacks a review, cover manual-runner resume semantics, deduplicate review dispatch and validate results against the reviewed head; do not create a parallel task.
3. **Keep retro triage within a visible draft budget** — CG-249 [draft]
   - size: medium
   - why now: The new retro machinery needs a deliberate triage policy before it recreates an overloaded Inbox.
   - User value: the owner can review the next phase in one sitting while retaining every finding. Why now: personas, features and kickoff can multiply drafts after this large phase. Size: medium. Dependencies: merged CG-146, CG-187 and CG-225, plus the owner's severity and cap decision. Show every finding with provenance, deduplicate against existing tasks, support file-as-task, and report automatic-filed and held-back counts. Do not silently change the current all-findings policy before the decision.
4. **Add safe redispatch and canary-backed pin commands** — CG-250 [draft]
   - size: medium
   - why now: These commands eliminate demonstrated operator effort and wasted runs after their safety prerequisites land.
   - User value: replace recurring hand sequences with observable operations that preserve work and prevent competing workers. Why now: a superseded worker reportedly spent $4.34 without a PR. Size: medium. Dependencies: merged CG-180, CG-198 and CG-220, plus the phase-04 dispatch-concurrency blocker. Plan two sequenced slices: redispatch terminates and confirms exit of the previous process tree before reuse; pin checks the candidate, installs it and restarts at a tick boundary with failure recovery.
5. **Make retros capture and measure their own evidence** — CG-251 [draft]
   - size: medium
   - why now: Automated closure evidence prevents another phase from substituting implementation claims for measured outcomes.
   - User value: a phase verdict cites current screens and reproducible numbers. Why now: phase 04 lacked its walkthrough and aggregate timing, and hand merges were counted manually. Size: medium. Dependencies: merged CG-182 and CG-201. Capture Costs, Backlog and Retro before personas; use an HTML parser that excludes hidden content; make capture failure explicit. Report hand merges, tick mean/max, mechanical versus agent rebases and exact operator-share attribution in metrics and retro; show last-tick duration in the rail.
6. **Make operating profiles harness-aware and consistently named** — CG-252 [draft]
   - size: medium
   - why now: Profiles must be valid for the installed harness before users can safely use the operating-point control.
   - User value: a profile switch selects runnable models on the user's configured harness and clearly describes its effect. Why now: built-in Claude identifiers are applied to Codex gardens and economy's hard-tier choice lacks outcome evidence. Size: medium. Dependencies: merged CG-221 and the cost baseline. Reference per-harness tier maps, reject incompatible combinations, retain safe defaults, distinguish operating profile from observation feed, remove task IDs from copy and reconcile the retro column and live/restart lists.
7. **Onboard an existing repository into a working garden** — _skipped: flagged by the retro as a duplicate of CG-215_
   - size: hard
   - why now: CG-215 is the existing adoption feature and should be strengthened rather than duplicated.
   - User value: a new team reaches a running garden in one sitting. Why now: this is the product-manager's recommended adoption headline after the loop's blockers and measurement work. Size: hard. Dependencies: merged CG-193 and CG-224, completed CG-238, and isolated planner execution. Reuse CG-215; require its generated garden to pass doctor on a non-Python fixture without hand edits and pass the common brief gate, then validate with a named team's repository if available.
8. **Route tiers across harness and model pools** — _skipped: flagged by the retro as a duplicate of CG-230_
   - size: medium
   - why now: CG-230 can turn existing quota awareness into resilience once its cost and attribution prerequisites exist.
   - User value: continue useful work when one paid harness reaches quota and compare accepted outcomes by pool member. Why now: both accounts encountered quota limits, and CG-212 now exposes pauses. Size: medium. Dependencies: merged CG-212, the cost-per-accepted-task baseline and harness-aware profiles. Reuse CG-230, record the chosen member on every run and avoid paused or incompatible members; evaluate on a fixed cohort before broad rollout.

## Persona reports

- [designer](context-garden/phase-04/docs/reviews/designer-2026-09-05.md)
- [product-manager](context-garden/phase-04/docs/reviews/product-manager-2026-09-05.md)
- [project-manager](context-garden/phase-04/docs/reviews/project-manager-2026-09-05.md)
- [security](context-garden/phase-04/docs/reviews/security-2026-09-05.md)
- [staff-engineer](context-garden/phase-04/docs/reviews/staff-engineer-2026-09-05.md)
- [usability-expert](context-garden/phase-04/docs/reviews/usability-expert-2026-09-05.md)
- [user](context-garden/phase-04/docs/reviews/user-2026-09-05.md)

## Answers

- **Does the reopen carry all three blocking items, or only the brief-gate closure, with the two security fixes moved to phase 05 as its first tasks?** — answered: All of them. With the user's standing authority: CG-238 is merged and CG-239 is in review, so the reopen carries both; nothing moves to phase 05. Astra's reconcile has since filed CG-240 to CG-247 as further blocking items; which of those block and which become phase-05 follow-ups is settled by the joined retro. (by cli at 2026-09-05T23:43:16+00:00)
- **Is phase 05 about adoption (a second team on its own machines) or about cost per accepted task?** — answered: Adoption is the headline: phase 05 is the garden running in someone else's environment (onboarding CG-215, any model CG-213, shared quotas CG-230, any machine CG-216). Cost per accepted task is measured from the phase's first task as a prerequisite, not the headline (user's stub, 2026-09-05). (by cli at 2026-09-05T23:45:33+00:00)
- **Should phase 05 make onboarding the headline, with cost measurement as its first prerequisite, or make cost reduction the headline?** — answered: Adoption is the headline: phase 05 is the garden running in someone else's environment (onboarding CG-215, any model CG-213, shared quotas CG-230, any machine CG-216). Cost per accepted task is measured from the phase's first task as a prerequisite, not the headline (user's stub, 2026-09-05). (by cli at 2026-09-05T23:45:34+00:00)
- **How many drafts may a retro file, and at what severity?** — answered: Every finding is filed as a draft at its severity, no cap (user, 2026-09-05: do not schedule only two high items per review and toss the rest). The kickoff and the operator prune at approval; a finding that is not worth a task is cancelled with a reason, not dropped silently. (by cli at 2026-09-05T23:45:36+00:00)
- **Should retros keep filing every finding, or automatically file only high findings with an eight-draft cap and retain all others for explicit filing?** — answered: Every finding is filed as a draft at its severity, no cap (user, 2026-09-05: do not schedule only two high items per review and toss the rest). The kickoff and the operator prune at approval; a finding that is not worth a task is cancelled with a reason, not dropped silently. (by cli at 2026-09-05T23:45:38+00:00)
- **Are cost per accepted easy task at or under $4 and first-pass approval at or above 90% the phase-05 numbers?** — answered: Yes: at most $4 per accepted easy task and at least 90% first-pass approval carry over as phase-05 targets, measured per accepted task (garden metrics), with the sonnet-era baseline from the phase-04 operator retro as the starting point. (by cli at 2026-09-05T23:45:39+00:00)
- **Are phase-05 targets of at most $4 per accepted easy task and at least 90% first-pass approval the intended acceptance thresholds?** — answered: Yes: at most $4 per accepted easy task and at least 90% first-pass approval carry over as phase-05 targets, measured per accepted task (garden metrics), with the sonnet-era baseline from the phase-04 operator retro as the starting point. (by cli at 2026-09-05T23:45:41+00:00)
- **Ratify the decisions made in the owner's name this phase: automerge_method merge, review.max_rounds 4, reviews on the easy tier, the codex tier map, and eight queue-rotation hand merges.** — answered: Ratified (user, 2026-09-05: 'I ratify your decisions'): automerge by merge commit, review.max_rounds 4, reviews on the easy tier, the codex tier map luna/terra/sol. The eight queue-rotation hand merges were a bug (fixed by CG-176), not a policy. (by cli at 2026-09-05T23:45:42+00:00)
- **Do you ratify the phase's merge method, four-round review cap, easy-tier reviews, Codex tier map and eight queue-rotation hand merges?** — answered: Ratified (user, 2026-09-05: 'I ratify your decisions'): automerge by merge commit, review.max_rounds 4, reviews on the easy tier, the codex tier map luna/terra/sol. The eight queue-rotation hand merges were a bug (fixed by CG-176), not a policy. (by cli at 2026-09-05T23:45:44+00:00)
- **Does docs/operator-spend.jsonl live at the garden root's docs directory?** — answered: Yes: one ledger at context-garden/docs/operator-spend.jsonl in the garden repo (the product's docs directory), appended by tools/operator_spend.py and shown on the costs page (CG-223). Product and phase attribution per record is welcome. (by cli at 2026-09-05T23:45:45+00:00)
- **Should operator sessions use one garden-root docs/operator-spend.jsonl ledger with explicit product and phase attribution?** — answered: Yes: one ledger at context-garden/docs/operator-spend.jsonl in the garden repo (the product's docs directory), appended by tools/operator_spend.py and shown on the costs page (CG-223). Product and phase attribution per record is welcome. (by cli at 2026-09-05T23:45:47+00:00)
- **Was CG-206 cancelled because browser notifications are sufficient, or is unattended notification delivery still required?** — answered: Yes for now: the user chose Chrome notifications first (CG-208); unattended delivery to a phone is parked (Tailscale idea, 2026-09-05). (by cli at 2026-09-05T23:45:49+00:00)
- **Who is the second team, and is there a real repository to onboard before phase 05 closes?** — answered: No second team is named yet. Phase 05's kickoff (CG-224) asks the owner for it before CG-215 is approved; the acceptance case is one existing repository with its own docs and task list, on a machine that is not this one, not context-garden itself. Until it is named, CG-215 is built against a fresh clone of a public, well-documented repository and the real onboarding is the phase's exit criterion. (by cli at 2026-09-05T23:55:08+00:00)
- **Which second team and existing repository will serve as the onboarding acceptance user?** — answered: No second team is named yet. Phase 05's kickoff (CG-224) asks the owner for it before CG-215 is approved; the acceptance case is one existing repository with its own docs and task list, on a machine that is not this one, not context-garden itself. Until it is named, CG-215 is built against a fresh clone of a public, well-documented repository and the real onboarding is the phase's exit criterion. (by cli at 2026-09-05T23:55:10+00:00)
- **Codex runs in bypass-permissions mode since 2026-09-05; ratify or revert?** — answered: Keep bypass as the live policy until the containment fixes land (CG-239: reading paths and the clone's git config and hooks; CG-246: workers cannot mutate shared control or harness state), then return codex to sandboxed execution with the two allowances it needs (.git writes in its own worktree and network for gh) and record the change on the costs page annotations. Decided by the operator on the owner's instruction, 2026-09-05. (by cli at 2026-09-05T23:55:11+00:00)
- **Should Codex bypass permission mode remain the live operating policy after the required containment fixes, or should the live garden return to sandboxed execution?** — answered: Keep bypass as the live policy until the containment fixes land (CG-239: reading paths and the clone's git config and hooks; CG-246: workers cannot mutate shared control or harness state), then return codex to sandboxed execution with the two allowances it needs (.git writes in its own worktree and network for gh) and record the change on the costs page annotations. Decided by the operator on the owner's instruction, 2026-09-05. (by cli at 2026-09-05T23:55:13+00:00)
- **Should self-product approval require an independent second reviewer or retain repeated rounds from the same reviewer?** — answered: Hard-tier PRs get a second round from a stronger model (the harness's retro_model) before the queue merges them, on top of CG-191's two approving rounds; easy and medium PRs keep repeated rounds from the review-tier reviewer. Decided by the operator on the owner's instruction, 2026-09-05. (by cli at 2026-09-05T23:55:15+00:00)
