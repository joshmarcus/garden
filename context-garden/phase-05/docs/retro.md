# Retrospective: context-garden/phase-05

_2026-09-10T13:10:37+00:00 · hard tier (gpt-6-astra)_

## What changed

Phase05 delivered repeatable fixture onboarding, HTTP and managed EC2 workers, resumable scaling, preservation of interrupted work, stronger lease and fence handling, bounded validation, a single improved Now page, clearer recovery actions and versioned release tooling. All tasks in the supplied phase list are terminal, including CG-423. The owner's September10 stabilization acceptance stands, delegated interventions remain recorded costs rather than disqualifying owner actions, and CG-347/348 remain accepted Phase07 scope. The captured 152 done tasks, 45 cancellations, 1,942 runs and $985.14 recorded spend are capture-specific observations, not complete end-to-end economics or current acceptance denominators. First-pass approval, hand-attributed merges and agent rebase targets were reported missed; complete easy-task cost and phase operator share remain unestablished. Repeated review and environment recovery consumed real effort despite later repairs. This retrospective reopens for substantive closing defects and their accountable disposition; it neither repeats stabilization nor authorizes deployment or release before actual closure.

## Numbers

- workers: $996.83
- operator: $197.29 — 837 turns — 17% of total
- total: $1194.12
- hand merges: 54 (of 126 merged PRs)
- tick duration: mean 18.15s, max 246.34s (1669 ticks)

### Outcomes by tier

| tier | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| hard | $0.79 | $12.27 | 24% |
| easy | $0.16 | $2.05 | 24% |
| medium | $0.37 | $4.04 | 34% |

### Outcomes by model

| model | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| claude-fable-5-1 | $9.75 | $64.03 | 0% |
| claude-opus-4-8 | $6.24 | $7.27 | 100% |
| claude-sonnet-5 | $1.48 | $3.18 | 75% |
| gpt-5.6-luna | $0.06 | $2.34 | 17% |
| gpt-5.6-sol | $1.84 | $9.05 | 18% |
| gpt-5.6-terra | $1.05 | $4.28 | 33% |
| gpt-6-astra | $9.78 | $38.77 | 33% |
| unknown | $0.17 | $8.81 | 30% |

### Outcomes by harness

| harness | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| claude | $6.05 | $19.41 | 62% |
| codex | $1.12 | $6.10 | 26% |
| human | $0.00 | $5.87 | 43% |
| unknown | $0.17 | $19.13 | 0% |

## Verdict

**Reopen.**
These must land before context-garden/phase-05 can close; each carries a freeze exception so it still dispatches.

Follow-ups filed in phase-06:
- CG-576: Deliver controller-owned CI diagnostics to isolated workers
- CG-577: Keep short validation checks responsive under shared admission
- CG-578: Use stable identities for preserved worktree changes
- CG-579: Define shared-host validation lease policy
- CG-580: Align QA request timeouts with advertised deadlines
- CG-581: Prevent folded rail stretching on short pages
- CG-582: Separate expected SSE shutdown from application errors

Blocking tasks filed in this phase:
- CG-533: Verify existing security and onboarding closing repairs — Two unresolved security highs violate the phase's no-new-high requirement, and harmful first-run defaults undermine the headline non-Python onboarding outcome; existing later-phase ownership does not discharge those closing obligations.
- CG-534: Refuse destructive recovery from corrupt scheduler state — Silent durable-state loss can remove safety controls and recovery intent, directly contradicting dependable operation.
- CG-535: Preserve maintenance requests across stale scheduler reads — A supposedly safe installation pause can disappear through observation, allowing scheduling to resume across a maintenance boundary.
- CG-536: Make accepted-task costs and phase comparisons trustworthy — Misleading filters and unknown costs shown as definitive values invalidate the phase's central cost-per-accepted-task and comparison outcomes.
- CG-537: Complete the Phase05 closing account and target disposition — Closure needs an explicit disposition of missed contractual outcomes and an authoritative account of accepted source; terminal task counts and accepted stabilization alone do not provide it.

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| No explicit criteria list despite criterion-by-criterion reporting requirement | CG-244 | – | outdated | Current owner policy makes the Goal the contract when criteria are absent and explicitly rejects mandatory placeholder checklists. |
| Full suites exceed the terminal's 30-second reporting window | CG-251 | CG-446 / PR342 | fixed | Bounded validation/check execution and the current foreground validation policy replace the reporting-window assumption also reported by CG-292, CG-311, CG-324 and CG-254. |
| Shared full suites saturate filesystem and obscure completion | CG-215 | CG-361 / PR244 | fixed | Merged supervision, resource admission, focused local validation and stress exclusion address the shared-suite pattern reported by CG-230, CG-296, CG-318, CG-320, CG-324 and CG-358, without proving contention impossible. |
| Temporary retention exhausts shared /tmp | CG-236 | CG-310 / PR209 | fixed | Disk-backed per-run temporary storage and cleanup address the reported tmpfs failure also logged by CG-291; later physical-disk cleanup and reserve work remains separately owned by CG-527/528. |
| Pytest temporary cleanup hangs after assertions finish | CG-316 | CG-310 / PR209 | fixed | Per-run temporary isolation addresses the shared-directory cleanup collision; CG-215 also recorded successful isolated temporary-root verification. |
| Interrupted or detached suites leave duplicate pytest processes | CG-343 | CG-430 / PR319 | fixed | Merged descendant supervision and bounded execution address the orphan-process pattern also reported by CG-293, while interrupted historical runs remain interrupted. |
| Seven-minute ordinary suite | CG-318 | CG-453 / PR353 | fixed | CG-453 records a final-source ordinary-suite pass in 451.50 seconds under the explicit eight-minute objective; this is a measured environment result, not a universal runtime guarantee. |
| Old branch comparison resembles removal of merged security code | CG-245 | – | outdated | The report itself establishes that the alarming diff came from branch ancestry and disappeared after conflict-free integration. |
| Review diff includes already merged commits | CG-307 | – | outdated | This was a stale review-base snapshot, like the later CG-300 and CG-417 historical-divergence reports, rather than evidence that the final task removed those changes. |
| Dispatch brief cites control.py instead of the task approval gate | CG-248 | – | outdated | CG-248/PR203 and CG-249/PR204 used the actual approval mechanism; the erroneous references belong to completed historical briefs. |
| Task notification destination offers no decision or way forward | CG-245 | CG-311 / PR208 | fixed | The task page gained the shared decision card, with subsequent no-change and recovery handling in CG-328, CG-337 and CG-480. |
| Collapsed Inbox cards and overlapping buttons | – | CG-312 / PR211 | fixed | The merged Inbox layout repair directly addresses the owner's observed rendering defect. |
| UI work accepted without inspecting affected rendered behavior | – | CG-315 / PR210 | fixed | Rendered review support landed and was subsequently narrowed by CG-377, CG-390 and current agent-judgment policy; mandatory walkthroughs for every template touch are superseded. |
| Worker cannot execute required garden persona-review | CG-307 | CG-324 / PR223 | fixed | Controller-owned evidence orchestration addresses the worker-authority mismatch also reported by CG-314; current policy permits proportionate verification. |
| Missing Playwright and unreliable Windows narrow-window captures | CG-308 | CG-326 / PR250 | fixed | The merged true-390px capture recipe, browser readiness in CG-368 and compatibility handling in CG-389 address the repeated CG-307/308/312/314 capture failures. |
| WSL interop failures and browser port collisions during captures | CG-314 | – | outdated | These were particular capture-session failures; the records include subsequent successful captures and alternate ports, not an unresolved product render failure. |
| No image library to crop framed captures | CG-308 | – | outdated | The unavailable optional cropping tool was a worker-environment snapshot and does not establish a functional defect in the accepted page. |
| pkill and pgrep match their calling shell | CG-308 | – | outdated | The report identifies a corrected matching pattern; it is a historical command-selection mistake rather than a remaining Garden feature defect. |
| External context paths absent or inaccurately marked unresolved | CG-385 | – | still true | CG-386, CG-434 and CG-437 continue reporting nonexistent checkout paths despite inlined equivalents, so CG-293 did not fully resolve truthful context-location reporting. |
| Incident reading documents absent from worker checkout | CG-358 | – | still true | CG-358 and CG-362 report inaccessible incident references, and the supplied evidence does not establish a general fix for distinguishing controller documents from checkout files. |
| Supplied design snapshot cannot establish shared metrics provenance | CG-314 | – | outdated | The aggregate snapshot was insufficient for that historical design review; later metrics work exists, although current accounting defects are separately retained below. |
| Now hand-merge and tick metrics are placeholders | CG-308 | CG-253 / PR265 | fixed | CG-253 connects hand merges and tick duration to metrics and the rail, replacing the historical placeholder. |
| Mock growth-stage bands disagree with design prose | CG-308 | – | outdated | The implementation followed the prose and the later Now redesign supersedes that mock-specific disagreement. |
| Fixture review cap differs from the design's assumed cap | CG-308 | – | outdated | The fixture assumption was corrected, and optional configured review limits supersede the historical hardcoded design expectation. |
| dict.update and \|= do not persist task state | CG-308 | CG-322 / PR257 | fixed | Merged change tracking routes these mutations through tracked writes; inspected State source contains the implementation. |
| Original phase-04 transcripts were truncated | CG-237 | – | still true | No merge reconstructs the lost original bytes; surviving final results remain the historical evidence and CG-506 owns prospective complete remote transcript return. |
| Short-page shell grid stretches the folded rail | CG-308 | – | still true | The supplied merge descriptions do not establish that the specific tall-viewport grid behavior was repaired; narrow-overflow fixes alone do not prove it. |
| Stream progress test assumes a short machine uptime | CG-308 | – | outdated | This concerns a historical test assumption about monotonic time and is not evidence of a current stream defect. |
| Transient canary or served-QA timeout followed by passing reproduction | CG-317 | – | outdated | CG-317, CG-318, CG-332, CG-338, CG-378, CG-381 and CG-387 describe individual failures followed by passing scoped or final checks, not established persistent regressions. |
| QA advertises thirty seconds but requests time out after ten | CG-216 | – | still true | A general execution deadline repair does not establish correction of this specific advertised-versus-per-request timeout mismatch. |
| Base-only test or CI helper absent from older checkout | CG-316 | – | outdated | CG-316, CG-322 and CG-326 explicitly integrated or accounted for the newer base implementation. |
| Unrelated untracked lint failure or base whitespace | CG-296 | – | outdated | The untracked probe and CG-328/CG-490 base whitespace reports describe excluded historical changes, not demonstrated defects in the completed task diffs. |
| Generated snapshot dirties worker checkouts and collides with merges | CG-342 | CG-483 / PR383 | fixed | Keeping generated worker context out of tracked source addresses the recurring snapshot collision reported across CG-216, CG-294, CG-327, CG-385 and many later tasks. |
| Clean-tree CI requires repeated snapshot stashing | CG-354 | CG-483 / PR383 | fixed | CG-483 removes the recurring generated-context cause; current controller-owned publication also supersedes the old mandatory worker CI-helper workflow reported throughout CG-253 to CG-392. |
| Shared stash indices change during preservation | CG-339 | – | still true | Git's shared stash namespace remains shared, as CG-294, CG-355, CG-364 and CG-368 observed; removing generated-context churn reduces exposure but does not make positional stash references safe. |
| Required production-worker validation is forbidden to a worker | CG-357 | – | outdated | The worker honestly distinguished seeded records from live processes, and the owner later accepted stabilization without authorizing another production experiment. |
| Backend changes receive broad screenshot requests | CG-329 | CG-390 / PR299 | fixed | Scoped validation and visual-change policy address CG-329, CG-337, CG-361 and CG-365's unrelated page matrices without relaxing real functional correctness. |
| Fifty-six captures requested for shared rail changes | CG-361 | CG-377 / PR284 | fixed | The supplied integration evidence demonstrates scoped zero/four-image requests for backend/task-page fixtures instead of the historical fifty-six; production savings remain unmeasured. |
| Gardens sharing a user can advertise inconsistent host lease limits | CG-361 | – | still true | The declined host-owned policy improvement remains an acknowledged configuration-ownership gap; no supplied merged outcome establishes centralized cross-garden policy. |
| Worker cannot safely migrate processes into a disposable cgroup | CG-361 | – | disputed | Refusing to experiment in the only writable production cgroup honors the task's boundary and is not a reason to repeat implementation. |
| Published commit subject contains workflow history | CG-361 | – | disputed | Rewriting shared history for cosmetic wording would violate policy; future descriptions should follow the owner's current style guidance. |
| Direct worker push lacks credentials | CG-322 | – | outdated | CG-216, CG-322 and CG-355 used the authorized helper at the time; current policy assigns publication to the controller and intentionally withholds operator credentials. |
| Host memory.events.high drifts during a test | CG-332 | CG-426 / PR309 | fixed | Opt-in stress selection and focused bounded validation address environment-sensitive ordinary checks also reported by CG-253, CG-331 and CG-355; historical counter changes remain recorded observations. |
| Reading system Python as the prepared test environment | CG-253 | – | outdated | CG-253 and CG-313 successfully used the prepared virtual environment; system Python need not contain pytest. |
| Extra retro capture-order orchestration test requested | CG-253 | – | disputed | The worker cited existing ordering and capture coverage, and current policy does not require an additional test solely to mirror implementation. |
| Legacy unannotated completion fixtures fail CI | CG-253 | CG-253 / PR265 | fixed | The report explicitly records compatibility repair and a passing final run before merge. |
| GitHub CI takes several minutes per head | CG-301 | – | still true | An eight-minute suite does not eliminate external CI latency; existing CG-396 and CG-509 own receipt reuse and duplicate-workflow reduction. |
| Rebased published branch requires a non-force integration merge | CG-336 | CG-464 / PR358 | fixed | Removing unnecessary latest-base rebuilds reduces the recurring cause also reported by CG-374, while legitimate conflict integration and shared-history protection remain required. |
| Transient empty execution.json read in runner tests | CG-300 | – | outdated | CG-300, CG-356 and CG-373 record diagnosed reruns passing, which retires those individual failures without asserting a universal race fix. |
| Live review.max_rounds setting cannot be committed from worker checkout | CG-376 | – | outdated | The handoff records the supported live null setting applied and displayed after release; production configuration is correctly separate from worker source. |
| Validation leases delay short lint and focused tests | CG-380 | – | still true | CG-393 distinguishes waiting from idle failure but does not establish fair low-latency admission for short checks reported by CG-356, CG-362, CG-374, CG-375, CG-378, CG-379, CG-386 and CG-390. |
| Validation wrapper supplies opaque exit-code-only failures | CG-327 | – | still true | Later check-run personas still find no useful command/result presentation, so execution supervision alone did not resolve diagnostic usability. |
| jq unavailable in worker image | CG-385 | – | disputed | CG-385 and CG-393 inspected the data with available tools; jq is not an established product requirement. |
| No-change lifecycle fix repeatedly blocked on generic replay manifests | CG-328 | CG-436 / PR326 | fixed | Unrelated replay admission and optional evidence requirements were relaxed while retaining actual failed checks and source-identity concerns. |
| Generic replay does not model harness quota/auth pauses | CG-332 | – | disputed | Dedicated scheduler regressions and the scoped disposable HTTP check supplied equivalent verification without requiring a universal replay model. |
| Inherited validation leases self-deadlock nested runner fixtures | CG-393 | CG-422 / PR402 | fixed | CG-422's recorded review and wrapped runner tests verify synthetic lease isolation, with CG-468/PR369 covering nested wrapper inheritance; this reconciles CG-375, CG-430 and CG-433 reports. |
| GARDEN_VALIDATION_RUNNER missing on remote worker | CG-421 | CG-429 / PR314 | fixed | Supervised validation provisioning for remote model workers addresses the missing prescribed entry point. |
| LocalRunner completion hangs after stdin consumer exits | CG-431 | CG-433 / PR325 | fixed | The dedicated completion fix addresses the named hang reported by CG-328, CG-431 and CG-438, separately from nested validation admission. |
| Full suite times out without useful named failures | CG-430 | CG-446 / PR342 | fixed | Explicit per-test and command deadlines address unbounded waits, while historical timed-out runs remain failures or interruptions rather than passes. |
| No configured typechecker despite generic requests | CG-494 | – | disputed | CG-425, CG-427, CG-430, CG-444, CG-448, CG-386, CG-389, CG-392 and CG-465 confirm no project typecheck contract, so its absence does not justify adding a new gate. |
| Remote pre-PR checks read controller-only paths or old installed code | CG-427 | CG-431 / PR320 | fixed | Controller-owned replay routing addresses CG-427 and CG-428's locality mismatch; current-source policy handling also landed in CG-434/PR327. |
| Shared onboarding assertions depend on checkout metadata or cache | CG-438 | CG-493 / PR396 | fixed | Retained discovery and CI guards address the checkout-sensitive family; the unrelated historical failures do not become regressions in CG-428 or CG-438. |
| Frozen plan incorrectly says Inbox behavior is nonvisual | CG-437 | – | still true | The plan contradicted the task's changed interaction, and no supplied outcome proves stale scope descriptions are corrected when revisions change behavior. |
| Main base probe actually tests branch head | CG-428 | CG-459 / PR356 | fixed | Advertised-base source pinning and fresh-probe initialization in CG-484 address the invalid source comparison. |
| Worker cannot rerun setup or establish fresh setup duration | CG-453 | – | outdated | This limits the historical measurement to its prepared environment; it does not negate the recorded ordinary-suite runtime or authorize fresh installation for metadata. |
| Interaction tests still demand mandatory replay admission | CG-438 | – | outdated | Current reviewer-judgment policy supersedes those expectations and the task later records repaired transitions and backoff without weakened assertions. |
| Worker CI analyser needs unavailable GitHub authentication | CG-465 | – | still true | Repeated CG-437, CG-438, CG-455, CG-465, CG-480 and CG-491 reports show controller-owned diagnostics still fail to reach workers reliably; existing CG-396 and CG-506 cover related status and transport work. |
| Saved failing workflow log unreadable to worker | CG-465 | – | still true | The final permission-denied report demonstrates a diagnostic delivery defect, distinct from intentional credential isolation and optional artifact commentary. |
| Duplicate same-SHA workflows disagree through a canary flake | CG-493 | – | still true | CG-509 exists and was still in review during read-only inspection, so duplicate-job prevention is not yet established as merged. |
| Successful served replay emits cancellation tracebacks on shutdown | CG-455 | – | still true | CG-496 reports the same benign shutdown noise after successful verification; repeated successful exits distinguish log usability from failed application behavior. |
| Open SSE connection prevents benchmark server shutdown | CG-479 | CG-479 / PR382 | fixed | The report records stopping the first attempt, fixing its harness and reporting only the successful rerun. |
| Optional UI scope mapping repeatedly requested without a defect | CG-455 | – | disputed | CG-437, CG-434, CG-455, CG-480 and CG-485 supplied scoped behavior checks, while current owner policy rejects metadata-only revision demands. |
| Unavailable advisory pre-check treated as source repair | CG-437 | – | disputed | An unavailable advisory result does not establish a code defect; concrete failures found during local reproduction remain actionable. |
| Broad replay-artifact expansion requested for runner cleanup | CG-433 | – | disputed | Direct bounded runner/supervisor verification addresses the change without expanding scheduler artifact persistence. |
| Release protocol absent on branch | CG-384 | CG-384 / PR407 | fixed | CG-384 explicitly added the missing release protocol as part of the merged artifact-validation change. |
| Fresh CI must wait for controller publication | CG-384 | – | disputed | Controller-owned publication is current policy, so worker nonpublication is an intentional authority boundary rather than an implementation failure. |
| Excessive review rounds and recorded cost | CG-437 | – | still true | The logged four-to-seven-round episodes and costs across CG-216, CG-253, CG-294, CG-295, CG-327, CG-328, CG-336, CG-356, CG-362, CG-375, CG-381, CG-385, CG-428, CG-430, CG-434, CG-438, CG-455, CG-465, CG-480, CG-486 and CG-494 remain historical economic evidence; merged prevention mechanisms do not prove savings. |
| Walkthrough omits a decision page when no decision is active | CG-253 | CG-253 / PR265 | fixed | The review-loop finding predates subsequent revisions and the final merged walkthrough task; it must not be quoted as the final task verdict. |
| Planner description cites an earlier commit | CG-294 | – | outdated | The review recorded all criteria met and supplied a description correction without requiring another implementation revision. |
| Architecture map omits new modules | CG-295 | CG-295 / PR287 | fixed | The final merged documentation task and later CG-392 supersede the historical failed module-map review. |
| Fabricated replay actions and nonexistent claimed outputs | CG-327 | – | outdated | The rejected historical claim remains invalid evidence; the later merged fence implementation must be assessed from its final real checks, not that replay. |
| No-PR regression fails during no-change recovery review | CG-328 | CG-328 / PR273 | fixed | The specific failed intermediate head is superseded by later revisions and the final merged lifecycle repair. |
| Duplicated test definition fails lint | CG-362 | CG-362 / PR261 | fixed | The historical duplicated-definition finding precedes the final merged externally implemented-task reconciliation. |
| Malformed planner import can bypass onboarding rollback | CG-356 | CG-356 / PR276 | fixed | The intermediate rejection is followed by further revision and final merged onboarding recovery; it is distinct from the closing planner-authority finding. |
| Reclaim review requests unrelated replay and latest-main reconciliation | CG-385 | – | outdated | The reclaim task merged, and later owner policy removes blanket replay and latest-main requirements while preserving genuine source validation. |
| Remote review environment errors lose usage and cost | CG-438 | CG-438 / PR330 | fixed | The logged rejection precedes later repaired transitions and final merge; it does not establish current loss at the accepted head. |
| Troubled-task actions fail their displayed or configured behavior | CG-437 | CG-437 / PR349 | fixed | The final task repairs supersede the intermediate rejection, with the separate granted-revision recurrence addressed by CG-507/PR413. |
| Incomplete remote validation receipts satisfy the CI gate | CG-434 | CG-434 / PR327 | fixed | The inspected task record ends with approval of fail-closed exact-head receipt handling and a recorded merge at 2026-09-10T05:25Z. |
| Interrupted-check recovery accepts stale PR identity | CG-480 | CG-480 / PR378 | fixed | Later provenance revisions and final merge supersede the logged rejection; CG-471/PR372 also provides guarded atomic recovery. |
| Repository-lock materialization errors escape managed claim loop | CG-486 | CG-486 / PR387 | fixed | The final merged recovery task supersedes its intermediate request-changes finding, without claiming every remote disconnect is solved. |
| Historical leases hide the active watcher | CG-494 | CG-494 / PR404 | fixed | The review-loop snapshot predates the final merged scheduler-health task and is not its final acceptance verdict. |
| Unmerged scripted SVG executes in the operator origin | – | CG-519 / PR426 | fixed | The later closing-editor account and inspected task record establish approved inert artifact responses and merge on September 10; deployment of this source is not established here. |
| Worker-reachable application exposes unauthenticated operator controls | – | – | still true | The security finding has existing owner CG-517/PR430, but that task remained in review during inspection, so ownership does not resolve the closing blocker. |
| Planner retains controller filesystem authority | – | – | still true | CG-245's environment isolation does not satisfy enforced sandboxing, and existing CG-518/PR428 remained changes_requested during inspection. |
| Malformed state JSON becomes empty and can be overwritten | – | – | still true | Inspected State initialization and save paths catch JSONDecodeError by substituting an empty mapping, corroborating the staff-engineer finding. |
| Maintenance inspection can erase a concurrent pause request | – | – | still true | Inspected maintenance() still inserts an empty value through setdefault, corroborating the stale-reader overwrite described by the staff engineer. |
| Accepted-task filters and price completeness are misleading | – | – | still true | Designer, product-manager, staff-engineer and user agree that selected cohorts, forced completion and unknown costs diverge across surfaces; CG-251 and CG-351 do not establish resolution. |
| Phase operator share includes unrelated phases | – | – | still true | The project-manager and closing-editor reports identify inconsistent attribution, so CG-300's ledger integration cannot establish the phase target. |
| Deferred tasks remain presented as owner decisions | – | – | disputed | Earlier designer/product-manager captures report the defect while later usability/user reports recognize explicit deferral notices; current source-specific reconciliation is needed before assuming all deferrals still demand action. |
| Completed pages foreground historical rejection | – | – | still true | Designer, usability-expert and user independently identify missing completion provenance and undifferentiated historical assessments. |
| Check pages show transcript fallback instead of results | – | – | still true | Designer, usability-expert and user consistently report missing check commands, outcomes and consequences despite completed execution. |
| First-run YAML replaces discovered checks and adds a second harness | – | – | still true | The usability finding concerns the recommended onboarding path; CG-504/PR423 was approved but still unmerged during inspection and needs specific confirmation of this correction. |
| Idle remote claims materialize full historical runs | – | – | still true | The staff engineer identifies a request-identity scan before active filtering, so CG-495's bounded active selection does not by itself resolve this separate full-history path. |
| Phase targets and closing account lack explicit disposition | – | – | still true | Accepted stabilization does not establish first-pass, merge, rebase or economic targets, and the evidence bundle lacks a complete consistent phase account. |
| CG-347/348 remain outside phase05 despite old scope language | – | – | outdated | The latest owner context explicitly accepts their Phase07 placement, superseding the earlier expansion decision without claiming Spot recovery or pool control complete. |
| Release records disagree about deployed source | – | – | still true | The closing-editor distinguishes captured 671633857c8a from stale RC12 deployed.json and an RC16 receipt not resolved by this report; no current deployment is inferred. |

## What the personas said

The designer focuses on whether filters and labels make truthful promises; the product manager asks whether delegated operation returns time and money; the project manager preserves missed targets and consistent phase attribution. Security identifies authority gaps, with its SVG finding subsequently corrected by CG-519 but worker ingress and planner isolation still owned by unfinished CG-517/518. The staff engineer finds corrupt-state overwrite and maintenance-pause races, plus duplicated metrics and historical claim scans. Usability finds harmful first-run defaults and confusing completion/check pages; the intended user independently distrusts filtered costs, unknown prices shown as zero and historical rejection displayed as current. The closing editor asks for one source-specific account connecting these voices to existing tasks, accepted evidence and release provenance. Later reflections are preserved perspectives, not independent new runtime validations; deferral presentation receives conflicting observations and needs scoped reconciliation.

## Still open

- Security closure depends on existing CG-517 and CG-518 completing with independent current-source review; CG-519 is merged but its deployment is not established here.
- Malformed state can be overwritten and stale maintenance reads can erase a requested pause.
- Accepted-task cohorts, forced-completion treatment, unknown pricing and phase-scoped operator share need a shared trustworthy calculation.
- The recommended first-project configuration must preserve discovered non-Python checks and the selected single harness; verify the correction through existing CG-504.
- Missed numerical targets need explicit owner disposition, and the final closing account needs denominators, pricing coverage, intervention exceptions and verified source provenance.
- Completed-task provenance and check-run result presentation remain confusing.
- Earlier and later deferral observations disagree; shared badges, actions and execution holds need one current-source assessment.
- Short validation commands can queue behind heavy work, and controller-owned failing-check diagnostics do not reliably reach credential-isolated workers.
- Briefs still mislabel inlined context as missing checkout files and can retain inaccurate validation scope.
- Shared Git stashes still require stable object identities for safe preservation.
- Host-wide lease policy across multiple gardens remains unresolved.
- Tall-viewport rail stretching and advertised QA request deadlines lack a demonstrated final correction.
- SSE shutdown diagnostics remain noisy; historical capture consolidation already has CG-524.
- Idle claim request-identity lookup still traverses historical runs.
- Existing CG-396, CG-501, CG-504/505, CG-506, CG-509, CG-514 and CG-527/528 should continue in their assigned scopes without duplicate filing.
- Historical transcript loss and recorded review costs cannot be repaired retroactively or converted into savings claims.

## Questions for the owner

- **Should the recorded first-pass, hand-merge and agent-rebase target misses be accepted as explicit Phase05 exceptions with accountable follow-ups once substantive closing defects are resolved?** — decision card `20260910T130021Z-retro-q0` (blocking)
  - Stabilization evidence is already accepted, but that decision does not state a disposition of the separate numerical targets; incomplete cost measures must remain unknown pending corrected accounting, and no new stabilization run is requested.
  - options: Accept the historical misses with measured follow-ups and preserve all exceptions., Require a bounded in-phase remediation plan for specified missed outcomes before closure.

## Findings from persona reviews

### High

- **designer** — Accepted-task outcome tables ignore the page's selected window and filters without explaining their different scope. → CG-544 [draft]
- **product-manager** — Accepted-task outcome tables ignore selected Costs filters and present definitive prices despite incomplete underlying pricing. → CG-549 [draft]
- **project-manager** — Recorded first-pass approval, hand-attributed merges and agent rebase frequency miss the written phase targets despite task completion. → CG-555 [draft]
- **security** — When the shared application is reachable from worker networks, requests without Origin or credentials can invoke operator controls outside the authenticated worker API. → CG-558 [draft]
- **security** — An unmerged scripted SVG is served without CSP sandboxing and can execute in the operator UI origin when opened. → CG-559 [draft]
- **security** — Injected planning documents can drive shell execution with controller filesystem authority because bypass modes discard deny paths and default Claude planning lacks an OS sandbox. → CG-560 [draft]
- **staff-engineer** — Malformed state JSON silently becomes an empty side-store and can be overwritten, losing durable controls and recovery intent. → CG-561 [draft]
- **staff-engineer** — Reading absent maintenance state marks an empty entry dirty, allowing a stale tick save to erase a concurrent maintenance-pause request. → CG-562 [draft]
- **usability-expert** — The recommended first-run YAML overrides discovered project checks with pytest and introduces a mixed-harness pool despite the earlier single-harness choice. → CG-565 [draft]
- **user** — I can select a phase or time window while the accepted-task tables silently keep reporting all-history outcomes. → CG-568 [draft]
- **user** — I can see an accepted task priced at $0.00 when its work-run price is unknown. → CG-569 [draft]
- **phase05-closing-editor** — The available Phase 05 material contains seven preserved voices but no authoritative closing account connecting delivered outcomes, missed targets, interventions and accepted evidence. → CG-572 [draft]
- **phase05-closing-editor** — Current closing reports lack a consolidated disposition that distinguishes unresolved blockers from findings already covered by active or completed tasks. → CG-573 [draft]

### Medium

- **designer** — Accepted-task prices appear definitive even though their computation treats missing run prices as zero. → CG-545 [draft]
- **designer** — Deferring a troubled task leaves it counted and presented as an unresolved human decision. → CG-546 [draft]
- **designer** — Completed task pages display historical rejected criteria and review findings without distinguishing them from the accepted result. → CG-547 [draft]
- **designer** — Check runs use model-transcript fallback copy instead of explaining which commands ran and whether verification passed. → CG-548 [draft]
- **product-manager** — The captured application presents delegated check recovery and an explicitly deferred task as unresolved owner decisions. → CG-550 [draft]
- **product-manager** — Completed task and check pages foreground historical rejection or generic transcript copy instead of explaining the accepted result and verification outcome. → CG-551 [draft]
- **product-manager** — Queued work exposes policy holds without making their relationship to configured rules and deployed source clear. → CG-552 [draft]
- **product-manager** — Recorded throughput and owner-action freedom do not establish that delegated operation is cheaper than supervising an interactive agent. → CG-553 [draft]
- **product-manager** — Current roadmap and phase goal summaries lag the active product, making the next useful journey difficult for a new user to understand. → CG-554 [draft]
- **project-manager** — Operator-share aggregation includes unrelated phases' spend and cannot establish the Phase 05 operator-share target. → CG-556 [draft]
- **project-manager** — AWS Spot recovery and pool cost/control remain in Phase 07 although the earlier Phase 05 scope explicitly included them. → CG-557 [draft]
- **staff-engineer** — Separate outcome implementations disagree about forced completion and unknown pricing, allowing Now to report false acceptance and zero cost. → CG-563 [draft]
- **staff-engineer** — Every idle claim deep-copies all run history for request-identity lookup before applying active-run selection. → CG-564 [draft]
- **usability-expert** — The completed onboarding task presents unmet criteria and a request-changes review without prominently explaining the later owner merge and historical assessment context. → CG-566 [draft]
- **usability-expert** — Opening the latest onboarding check leads to a done run with generic model-transcript wording and no final message rather than an explanation of its checks. → CG-567 [draft]
- **user** — I open the completed onboarding task and see unmet criteria and a prominent request-changes verdict without an immediate completion explanation. → CG-570 [draft]
- **user** — I open a completed check run and get a generic model-transcript explanation instead of the checks and their outcomes. → CG-571 [draft]
- **phase05-closing-editor** — The evidence set contains conflicting temporal authorities: the walkthrough identifies build 671633857c8a, while docs/releases/deployed.json still identifies RC12 and obsolete stabilization and scope restrictions. → CG-574 [draft]

### Low

- **phase05-closing-editor** — The seven-voice collection is substantive, but the captured Retro destination says no retro exists and does not guide readers to those current reflections. → CG-575 [draft]

## Features for the next phase

1. **Explain accepted completion before historical reviews** — CG-538 [draft]
   - size: medium
   - why now: Clear completion provenance makes the existing workflow understandable without weakening review history.
   - User value: understand why a task is complete without reconstructing its timeline. Why now: three personas found historical rejection presented as current. Size: medium. Dependencies: existing completion provenance, CG-362/487 and the canonical acceptance correction; retain complete dated, source-specific findings.
2. **Show check commands and outcomes on run pages** — CG-539 [draft]
   - size: medium
   - why now: Actionable check results remove repeated investigation from the most common recovery journey.
   - User value: distinguish a finished process from successful validation and see the next action. Why now: generic transcript fallback hides the result of ordinary checks. Size: medium. Dependencies: existing check records and CG-506 for remote transport where needed; reuse available diagnostics without requiring new artifact formats.
3. **Reconcile deferred notices and attention ownership** — CG-540 [draft]
   - size: medium
   - why now: Resolve observed ownership inconsistencies with current behavior rather than replaying an older UI assessment.
   - User value: a saved deferral stops demanding a decision while preserving the execution hold. Why now: persona observations disagree across snapshots. Size: medium. Dependencies: CG-437, CG-480 and current shared attention logic; first establish which current states are wrong, then align notices, badges and reconsider actions.
4. **Measure delegated effort per accepted change** — CG-541 [draft]
   - size: hard
   - why now: Measure total operating effort before claiming savings or expanding model and infrastructure experiments.
   - User value: judge whether unattended development saves total effort and cost. Why now: accepted stabilization and task throughput do not establish economic benefit. Size: hard. Dependencies: corrected phase/cohort accounting, CG-336/375 and existing intervention events; show owner versus operator actions, recovery causes, lead time and priced/unpriced coverage.
5. **Finish effective review-policy continuity** — _skipped: flagged by the retro as a duplicate of CG-514_
   - size: hard
   - why now: Complete existing policy work before adding more controls that can disagree with it.
   - User value: understand the actual rule behind a queued hold. Why now: the product-manager report identifies policy/source ambiguity after repeated policy changes. Size: hard. Dependencies: CG-490 and existing CG-514; retain current-head safeguards and show effective policy without adding a second implementation of count-based hold removal.
6. **Publish a resumable first-change journey** — _skipped: flagged by the retro as a duplicate of CG-504_
   - size: hard
   - why now: Finish the existing adoption documentation instead of filing another broad documentation project.
   - User value: onboard a real non-Python project while keeping its checks and chosen harness. Why now: the first-run example and roadmap lag the product. Size: hard. Dependencies: existing CG-504 documentation work, CG-505 specification reconciliation and the Phase05 first-run-default correction; a voluntary new-user attempt is learning, not a renewed closure gate.
7. **Index durable remote claim request identities** — CG-542 [draft]
   - size: hard
   - why now: Remove the demonstrated historical scan without weakening idempotency or expanding the worker fleet.
   - User value: keep idle polling responsive as history grows. Why now: active-run filtering still follows a full-history request-identity lookup. Size: hard. Dependencies: CG-491/495 and current durable lease/replay rules; preserve rejection of stale, expired and replaced generations while avoiding terminal-history materialization.
8. **Make brief paths and validation scope truthful** — CG-543 [draft]
   - size: medium
   - why now: Repeated late-phase context errors show that presence checks alone are insufficient.
   - User value: workers spend time on implementation rather than locating context that is already supplied. Why now: late CG-434/437 reports persist after brief-gate work. Size: medium. Dependencies: CG-293/294/483 and existing scope planning; distinguish inlined, controller-owned and checkout-readable content and refresh scope when behavior changes.

## Persona reports

- [designer](context-garden/phase-05/docs/reviews/designer-2026-09-10.md)
- [product-manager](context-garden/phase-05/docs/reviews/product-manager-2026-09-10.md)
- [project-manager](context-garden/phase-05/docs/reviews/project-manager-2026-09-10.md)
- [security](context-garden/phase-05/docs/reviews/security-2026-09-10.md)
- [staff-engineer](context-garden/phase-05/docs/reviews/staff-engineer-2026-09-10.md)
- [usability-expert](context-garden/phase-05/docs/reviews/usability-expert-2026-09-10.md)
- [user](context-garden/phase-05/docs/reviews/user-2026-09-10.md)
- [phase05-closing-editor](context-garden/phase-05/docs/reviews/phase05-closing-editor-2026-09-10.md)
