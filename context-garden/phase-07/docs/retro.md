# Retrospective: context-garden/phase-07

_2026-09-13T16:57:41+00:00 · hard tier (gpt-6-astra)_

## What changed

Phase 07 delivered enterprise repository routing, exact-head and provider-neutral validation, manual takeover and PR adoption, command-backed hosts, admission and canonical-checkout foundations, Spot recovery, feedback preservation, review-policy improvements, operational visibility, cleanup, packaging, CI sharding, SSH attachment and closed-task defect annotations. Its amended inventory is 83 done and 11 cancelled with no unfinished Phase 07 tasks, and CG-405's stranded correction is now delivered through PR #545 at reviewed source 3d7d290a3e135abec476d98961023fd4958f5215. Later merges resolve many early environment and review findings, but completion machinery and several process or credential boundaries still need focused follow-ups. Close under the amended scope: the high-priority canonical timeout repair should precede reliance on that opt-in mode, while closure itself does not assert private enterprise acceptance, deploy merged source or release deferred work.

## Numbers

- workers: $540.23 partial known spend
- operator: $0.00 — 0 turns — 0% of total
- total: $540.23 partial known spend
- accepted cohort: 79 tasks (54 priced, 25 unpriced); cost/accepted: unavailable
- cohort rule: completion in the phase window; all task runs through acceptance
- hand merges: 31 (of 80 merged PRs)
- tick duration: mean 22.91s, max 617.33s (3483 ticks)

### Outcomes by tier

| tier | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| hard | — | — | 31% |
| medium | — | — | 32% |
| easy | $0.08 | $0.23 | 100% |

### Outcomes by model

| model | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| gpt-5.6-luna | $0.02 | $0.23 | 100% |
| gpt-5.6-sol | — | — | 30% |
| gpt-5.6-terra | — | — | 28% |
| unknown | — | — | 13% |

### Outcomes by harness

| harness | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| codex | — | — | 32% |
| human | — | — | 17% |
| unknown | — | — | 0% |

### Outcomes by pool member

| pool member | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| unknown | $0.44 | $6.84 | 33% |

## Verdict

**Close with follow-ups.**
Nothing blocks closing context-garden/phase-07. The follow-ups below become draft tasks in phase-08.

Follow-ups filed in phase-08:
- CG-681: Align merge-policy guides with delivered behavior
- CG-682: Distinguish unmapped acceptance rows from missing evidence
- CG-683: Deliver readable required context to retrospective workers

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Validation runner variable unset; prescribed wrapper failed | CG-395, CG-397, CG-406, CG-409 | – | outdated | Current run_supervisor.py supplies GARDEN_VALIDATION_RUNNER and remote_worker.py supplies the worker interpreter; the reported unset-variable failures describe earlier launch environments. |
| Required enterprise specification missing from dispatched reading lists | CG-396, CG-401, CG-404, CG-405, CG-406, CG-409, CG-411, CG-412, CG-413, CG-505 | – | still true | CG-543 improves reference labeling, but CG-412 still reported an unresolved required specification on September 11 and no preserved fresh dispatch demonstrates that every affected required reference became available. |
| Inlined product and phase context incorrectly presented as checkout paths | CG-528 | CG-543 / PR #466 | fixed | Merged brief handling distinguishes inlined, checkout-readable, controller-owned and missing inputs, with 196 focused tests recorded for CG-543. |
| Nested validation admission deadlocked local runner tests | CG-401, CG-404, CG-406, CG-411, CG-412, CG-415, CG-396 | CG-468 / PR #369; CG-422 / PR #402 | fixed | Merged nested-lease handling and isolation regressions address the enclosing validation lease that blocked child workers, with later ordinary-suite completion independently recorded. |
| Served remote-worker tests retained validation capacity or waited on detached checks | CG-414, CG-432, CG-447, CG-454, CG-457 | CG-501 / PR #414; CG-422 / PR #402 | fixed | Merged source includes fd272e19 sharing nested check leases and CG-501's durable claim and launch lifecycle repairs, followed by successful ordinary-suite verification. |
| Completed pytest child left a disposable supervisor holding its wrapper open | CG-397, CG-447 | – | outdated | The reports record scoped cleanup of those exact disposable processes, while later validation completed; this does not establish that every possible descendant-cleanup defect is fixed. |
| Full suite failed or stalled without identifying a failing node | CG-398, CG-404, CG-529 | – | outdated | These interrupted attempts remain failed or incomplete historical evidence, but later accepted hosted ordinary-suite results supersede their description of the phase's current validation state. |
| Full suite stalled in trial-wait polling | CG-395 | – | outdated | The stopped attempt is preserved, while subsequent merged-source ordinary suites completed; no current reproduction of that specific polling stall is supplied. |
| Onboarding assertion depended on unavailable GitHub repository metadata | CG-404, CG-457 | CG-432 / PR #337 | fixed | Merged onboarding uses the shared repository resolver and transport-equivalence coverage instead of the earlier transport-sensitive metadata detection. |
| Public Actions API polling exhausted its unauthenticated quota | CG-399 | – | outdated | The exact reported run was subsequently confirmed successful through its public Actions page; that exhausted polling window is not a current failed check. |
| Scoped workers could not inspect authenticated GitHub comments or failure logs | CG-396, CG-404, CG-406, CG-413, CG-414, CG-452, CG-475, CG-597, CG-616, CG-643, CG-644 | – | still true | Late reports still document authentication-limited diagnostics, and public metadata support does not provide authenticated job logs; approved controller-to-worker diagnostic handoff remains necessary. |
| Reading failed Actions logs necessarily requires repository-admin access | CG-452 | – | disputed | The preserved observation establishes that this worker lacked usable authentication, not that repository-admin authority is intrinsically required; broader credentials should not be inferred from the failure. |
| Known stress exclusions were unnamed on an older branch | CG-406 | CG-426 / PR #309 | fixed | Merged validation policy names and enforces stress opt-in behavior, with current test_validation.py covering old-branch compatibility. |
| Operator pyproject overlay invalidated the clean-head replay check | CG-406 | – | outdated | This was a preserved worktree overlay during that validation attempt, not an uncommitted defect in the final canonical-checkout implementation. |
| No configured standalone static type checker | CG-348, CG-396, CG-404, CG-406, CG-411, CG-412, CG-415, CG-432, CG-443, CG-451, CG-452, CG-468, CG-492, CG-498, CG-510, CG-515, CG-523, CG-625, CG-626 | – | still true | Current pyproject.toml and documented test commands still configure no mypy, pyright or standalone typecheck command; Ruff, compilation and pytest must not be described as a separate static typecheck. |
| Mandatory served replay demanded for changes whose frozen plan excluded it | CG-395, CG-396, CG-415, CG-432, CG-456 | CG-443 / PR #336; CG-462 / PR #355; CG-616 / PR #481 | fixed | Merged proportionate-review and browser-opt-in policies accept relevant CLI, source or behavioral evidence without requiring an unrelated served replay. |
| Declined optional UI mappings without a concrete rendered defect | CG-396, CG-413, CG-414, CG-466, CG-470, CG-473, CG-475, CG-477, CG-478 | – | disputed | The recorded suggestions concern optional metadata or unchanged rendering, and the accepted policy does not make those omissions implementation defects or grounds for another author round. |
| Broader owner-test selections returned partial progress | CG-414 | – | outdated | The worker subsequently ran the exact owner and remote UI nodes successfully, so the earlier partial selection is not an unresolved owner-feature finding. |
| Initially requested nonexistent or renamed test nodes | CG-347, CG-443, CG-473, CG-498, CG-506, CG-514, CG-526, CG-528, CG-625 | – | outdated | Each report records correcting the test selection and running existing tests; the failed initial commands remain historical mistakes rather than current missing product behavior. |
| Canonical dispatch and collection could mutate without proper checkout ownership | CG-406 | CG-406 / PR #311 | fixed | Current prepare_canonical_run saves checkout identity before claiming and protects active or unreaped owners, while the final review accepted pre-mutation fencing across execution paths. |
| Malformed host inspect responses bypassed recoverable environment errors | CG-404 | CG-404 / PR #316 | fixed | The February-shaped response concern was resolved by the September 9 revision validating null, object, scalar and malformed-row inspect responses before decoding, with focused lifecycle tests recorded. |
| Rebase left interleaved conflict fragments in scheduler code | CG-413 | CG-413 / PR #324 | fixed | Later conflict resolution and the final independent review accepted product-specific budgets and admission before PR #324 merged. |
| Legacy remote checks received product execution timeouts | CG-413 | CG-413 / PR #324 | fixed | The final review explicitly verified independent check timeouts alongside product execution budgets, restart accounting and weighted admission. |
| Routine recovery presented as an unexplained owner decision | CG-406, CG-437, CG-434 | CG-480 / PR #378 | fixed | Merged Inbox recovery classification separates operator repairs from owner decisions and preserves independent blockers; the current captured Inbox also describes those distinct responsibilities. |
| Plain resume recreated the same terminal-check stop | CG-406, CG-437, CG-434 | CG-471 / PR #372 | fixed | Merged atomic recovery reconciles matching terminal check state while preserving newer or live continuations and choosing the appropriate existing-source continuation. |
| Asynchronous CI replaced detailed review feedback | CG-438 | CG-474 / PR #370 | fixed | The merged feedback composition keeps review and CI contributions separately identified instead of replacing the worker's substantive review handoff. |
| Manual reservation could be mutated by replacement model trials | CG-473 | CG-473 / PR #368 | fixed | The final independent review accepted lifecycle parking across automatic paths, including the corrected trial guards, before the task merged. |
| Open-PR status understated widespread failed CI | – | CG-475 / PR #371 | fixed | Merged PR-wide observation exposes current conflicts, checks and comments rather than relying on isolated green runs; the reported 19-PR denominator remains a dated September 9 snapshot. |
| Operator reassurance substituted isolated successes for complete delivery accounting | – | – | still true | The historical reporting failure is established, but merged observation features alone do not demonstrate sustained operator reporting of the full denominator and actual corrected delivery. |
| CG-477's dispatched base lacked its completed investigation prerequisite | CG-477 | – | outdated | The report states that the prerequisite lifecycle commits were integrated before extension, and the final deep-dive delivery was subsequently accepted. |
| CG-230 recovery card mixed interrupted checks, real failures and stale review identity | CG-230 | CG-480 / PR #378; CG-471 / PR #372 | fixed | CG-480 explicitly used this incident to implement cause, ownership, evidence and action distinctions on top of guarded terminal-check recovery. |
| Initial feedback migration and REST pagination lost PR observations | CG-475 | CG-475 / PR #371 | fixed | Subsequent revisions repaired feedback migration, pagination and independent check/status reads before merged PR-wide observation was accepted. |
| A repaired PR remained blocked by a forgotten operator automerge hold | CG-464 | – | outdated | The incident records restoration of the original absent setting after its release gates were met, without a manual merge. |
| Hold ownership and release conditions require continuing reconciliation | CG-464 | – | still true | Restoring that one hold does not prove that every Task.extra.automerge hold is automatically reevaluated; existing ownership and recovery mechanisms should be used during bounded sweeps. |
| Exact-head CI lacked status-context and per-product policy integration | CG-396 | CG-396 / PR #343 | fixed | Later revisions completed gh and REST status pagination and fail-closed completeness checks, with 91 provider tests recorded before merge. |
| Validation output detached while the durable run succeeded | CG-466 | – | outdated | The preserved supervisor receipt reports terminal exit zero, resolving uncertainty about that attempt without relabeling earlier partial output as a separate failure. |
| Frozen tasks could mutate trial state before dispatch refusal | CG-478 | CG-478 / PR #375 | fixed | The merged revision moves phase refusal before destructive trial reset and includes focused freeze, move and trial coverage. |
| PR adoption persisted incomplete identity or mishandled external head movement | CG-411 | CG-411 / PR #321 | fixed | Revision 862a53ff validates complete metadata before persistence and refreshes safe same-branch head movement, with 2073 ordinary tests reported passing. |
| Historical generated HTML whitespace appeared in broad branch diffs | CG-499, CG-501, CG-527 | – | disputed | The reports distinguish inherited artifact whitespace from clean task revisions; this is not evidence that those revisions introduced a defect or need another author round. |
| Enrolled workers disappeared until their first contact | CG-499 | CG-499 / PR #411 | fixed | The final correction includes enrollment-registry workers as unknown or unavailable before contact and deduplicates configured, enrolled and contacted identities. |
| Worker-side exact-head CI was unavailable before controller publication | CG-492, CG-501 | – | outdated | Those unpublished-worker snapshots were followed by publication and ordinary guarded merges; inability to query an unpushed SHA is not itself an implementation defect. |
| Remote checks lacked restart-recoverable active-claim handoff | CG-501 | CG-501 / PR #414 | fixed | Merged recovery durably stages claim identity and input before releasing the launch gate and includes focused remote-check restart coverage. |
| Spot CLI allowed provisioning without interruption handling | CG-347 | CG-347 / PR #417 | fixed | The later CLI correction rejects Spot scale operations lacking durable interruption-event configuration before AWS access, followed by independent approval. |
| Transcript restart recovery and superseded-attempt retrieval remained incomplete | CG-506 | – | still true | CG-506 remains the existing deferred transcript-storage task in Phase 11; moving it out of Phase 07 changes closure scope but does not deliver its unresolved behavior. |
| Zero-run benchmark requested a nonexistent fixed run route | CG-503 | CG-523 / PR #438 | fixed | Merged benchmark size and route handling includes the fixture-size route repair and preserves valid zero-run inventories. |
| Visible specification files were newer than their recorded workspace commit | CG-505 | – | outdated | The audit explicitly recorded both the older commit and newer visible source rather than falsely attributing the files to that commit; this is a dated provenance discrepancy. |
| Ruby unavailable for link validation | CG-505 | – | outdated | An equivalent read-only Perl validation completed, so Ruby's absence did not leave the reported link check unresolved. |
| Web discovery-generation test failed outside the changed design-file selection | CG-513 | – | outdated | The failed attempt remains historical evidence, while the current test and later ordinary-suite verification no longer establish that branch's inherited failure as open. |
| Real Windows backing-volume validation was unavailable in the WSL worker | CG-528 | – | still true | The supplied evidence does not establish a successful real Windows backing-volume exercise; source and fixture coverage must remain distinct from that environment validation. |
| Disk reserve checks occurred too early for later scratch and setup writes | CG-528 | CG-528 / PR #445 | fixed | The final independent review accepted shared storage admission across execution and staging, and current canonical preparation rechecks before environment materialization and reconciliation. |
| RunStore and host-drain circular imports blocked test collection | CG-526 | CG-585 / PR #449 | fixed | Merged history contains the RunStore import-cycle repair and later focused and ordinary suites successfully collected. |
| Local main was stale or contained obsolete stacked implementations | CG-515, CG-529 | – | outdated | The reports record isolation or rebasing onto accepted origin/main, with CG-515 later validating 625 affected tests and its final provider changes. |
| Escalation treated infrastructure findings as implementation failures | CG-526 | CG-526 / PR #450 | fixed | Merged revisions preserve originating failure eligibility through review, revise and base-probe paths so infrastructure failures do not cause implementation-model escalation. |
| Closing-review preparation still held the controller lock on later ticks | CG-529 | CG-529 / PR #452 | fixed | The later revision implements source-bound preparation, locked revalidation and durable run commitment followed by out-of-lock launch. |
| Sequential phase gating missed fresh investigation-agent runs | CG-586 | CG-586 / PR #473 | fixed | Revision 1449d55f gates fresh investigation-agent admission while preserving pending state for retry after phase advancement. |
| Archive recovery marker could clear before durable index publication | CG-583 | CG-583 / PR #454 | fixed | Merged archive and restore transaction revisions preserve recovery across failed index publication and test exactly-once history and accounting after restart. |
| Inherited PYTEST_ADDOPTS corrupted the old-branch stress fixture | CG-529 | CG-601 / PR #484 | fixed | Current test_validation.py parameterizes explicit fixture options and preserves unrelated environment values, including the merged 250a5b3b stabilization. |
| Old-branch stress opt-in unexpectedly deselected the failing tests | CG-529 | CG-601 / PR #484 | fixed | The repaired fixture explicitly removes enforced policy options for authorized opt-in and checks the expected three failures and one pass. |
| System Python lacked the Markdown dependency | CG-626 | – | outdated | Rendering validation used the prepared project virtual environment successfully, resolving that interpreter-selection problem. |
| Rollout verification could accept an unstaged runtime | CG-492 | CG-492 / PR #492 | fixed | Revision 6d8dd1e6 binds post-switch verification to the durable staged runtime and executable attestation, with 72 focused tests recorded. |
| Validation wrapper rejected the indirect shard-inventory helper | CG-628 | – | disputed | The repository helper ran directly and passed under the stated policy; rejection by a wrapper that only accepts direct validation commands does not establish a product defect. |
| Rebase retained attach tests but replaced their implementation | CG-643 | CG-643 / PR #510 | fixed | Later independent reviews accepted the restored SSH attachment behavior and its read-only session contract before the final merge. |
| Inherited multiplayer claim fixtures returned 204 instead of 200 | CG-643, CG-644 | CG-644 / PR #513 | fixed | The preserved revision records correction of the synthetic claim fixture to satisfy strengthened admission, with parent integration and focused lifecycle tests retained. |
| Provider polling fixtures overwrote manually assigned fake PR heads | CG-515 | CG-515 / PR #427 | fixed | The final provider revision restored accepted parent behavior and verified the affected scheduler paths; merged history also contains exact-remote-head fixture isolation. |
| Provider REST rewrite lost rate-limit and authentication diagnostics | CG-515 | CG-515 / PR #427 | fixed | The final revision explicitly repaired REST error classification and passed the recorded provider and scheduler selections. |
| Count-only review loops despite accepted outcomes | CG-443, CG-412, CG-471, CG-477, CG-513, CG-643 | CG-514 / PR #422 | fixed | Current _automerge_min_review_rounds returns one, eliminating extra reviews solely to satisfy a count while preserving substantive review and CI gates. |
| Pending or unavailable exact-head CI treated as another source revision | CG-616, CG-644 | CG-597 / PR #474 | fixed | Merged review handling separates external CI waiting from actionable source failures, and CG-644's final record explicitly reconciles the SHA-only rejection with accepted source and passing hosted CI. |
| Recorded multi-round review cost remains real but causes are incompletely classified | CG-347, CG-396, CG-404, CG-406, CG-411, CG-412, CG-413, CG-414, CG-443, CG-471, CG-473, CG-475, CG-477, CG-478, CG-492, CG-499, CG-501, CG-506, CG-513, CG-515, CG-526, CG-528, CG-529, CG-583, CG-586, CG-616, CG-643, CG-644 | – | still true | Preserved loop records repeatedly say cause unknown and include both real corrective findings and accepted outcomes, so neither universal waste nor measured savings can be inferred from round counts. |
| CG-414 review-loop entry identifies no actionable defect | CG-414 | – | disputed | The entry reports four rounds and cost but explicitly labels both cause and actionable evidence unknown, which is insufficient to claim an unresolved ownership defect. |
| CG-405 correction remained undelivered after its original merge | CG-405 | CG-405 / PR #545 | fixed | The reviewed checkout is recovery merge 3d7d290a, and the closeout records independent review, 121 host tests and successful hosted CI for the recovered cancellation and release corrections. |
| General late-revision and rewritten-parent delivery reconciliation remains unsafe | CG-405 | – | still true | PR #545 repairs the specific lost correction, while existing draft CG-659 explicitly owns prevention and content-equivalent delivery reconciliation, including the CG-452 counterexample. |
| Terminal claim rejection can trap worker startup before pending-result persistence | – | – | still true | Existing CG-660 documents the actual restart incident and the remaining pending-file-first recovery guard; no supplied merge resolves that case. |
| Broad acceptance labels falsely identify different defects as repeated findings | CG-405 | – | still true | CG-661 preserves the cancellation-then-release review sequence showing two substantive defects collapsed into the same synthesized criterion label. |
| Canonical timeout can release ownership while a child can still write | – | – | still true | Current canonical.reconcile uses shell subprocess.run without descendant cleanup and prepare_canonical_run releases the lease on exception, corroborating the staff engineer's preserved harmless-child probe. |
| Removing approved tool-file mappings leaves stale worker copies | – | – | still true | install_config_files returns immediately for an empty mapping and the SSH renderer emits only current mappings, with no reconciliation of previously managed destinations. |
| Friction and doctor commands can use ambient gh instead of scoped credentials | – | – | still true | cli/planning.py and cli/diagnostics.py construct GitHub with use_gh enabled despite token_env, unlike the scheduler's scoped-transport construction. |
| Command CI blocks controller progress while querying adapters | – | – | still true | Command queries execute synchronously during the locked scheduler tick, with a default 120-second timeout and no aggregate bound across distinct heads. |
| Command-CI output limits apply only after buffering | – | – | still true | _command_answer captures complete stdout and stderr before _command_result checks stdout size, so the rejection threshold does not bound memory consumption. |
| Operating guides describe obsolete additional review requirements | – | – | still true | docs/operations.md and docs/architecture.md still promise count-based or second-opinion gates that conflict with the delivered one-approval policy. |
| Generated acceptance rows say no evidence despite detailed narrative verification | CG-628 | – | still true | criteria.py still renders missing structured row evidence as no evidence given, while the preserved CG-628 record contains hosted timing, inventory and behavioral validation. |
| Persona workers could not read the requested walkthrough pages | – | – | still true | All four persona reports record denied page access and the supplied reference snapshot omits those pages; this reconciliation can read the canonical copy, which does not establish portable access for dispatched workers. |
| Incomplete historical review can break phase-page rendering | CG-404 | – | still true | Existing draft CG-663 records the findings-only review that broke capture and the operator's display-only recovery, preserving the missing-verdict record without claiming a source fix. |
| Private enterprise pilot and deployed-environment acceptance remain unproven | – | – | still true | CG-641 establishes focused source verification and a local tmux probe, while CG-403 and CG-408 remain deliberately deferred and no private pilot or live-cloud acceptance is established. |

## What the personas said

All four selected personas recommend close_with_followups: Project manager scored 8/10, and Staff engineer, Security and User each scored 7/10; no product-manager persona ran. They value explicit authority, preserved feedback, manual continuity and precise source-verification claims. Staff engineer identified surviving canonical writers plus synchronous and unbounded command-CI execution; Security identified stale approved-tool copies and ambient credential fallback; Project manager identified misleading acceptance rendering and inaccessible dispatched evidence; User identified obsolete merge-policy documentation and completion trust. All support reusing CG-659–661 rather than duplicating recovery work. Their assessments primarily inspect source and records, with limited harmless probes, and none establishes hands-on private enterprise acceptance. This reconciliation additionally read the canonical captured walkthrough, whose index records HTTP responses, but did not run the app, rerun CI, edit files or commit.

## Still open

- Canonical reconciliation must terminate owned descendants before releasing checkout ownership, retaining the lease when cleanup is uncertain.
- Approved tool-file revocation must remove obsolete Garden-managed copies across supported transports.
- Auxiliary CLI commands must honor explicit scoped credentials and fail closed instead of using ambient gh authority.
- Command-CI observations need bounded output consumption and execution outside the controller critical section.
- CG-659 remains the existing draft for late corrective delivery and content-equivalent rewritten-parent reconciliation.
- CG-660 remains the existing draft for terminal-claim startup recovery; CG-661 remains the existing draft for substantive repeated-defect identity.
- CG-663 remains the existing draft for safe rendering and capture of incomplete historical reviews.
- Operating guides and generated acceptance summaries still contradict the delivered policy or accepted evidence.
- Dispatched reference snapshots must reliably include readable required context and the requested sanitized walkthrough pages.
- Authenticated CI diagnostics remain unavailable to some intentionally scoped workers; preserve useful exact-run diagnostics through approved handoff without widening credentials.
- No standalone static typecheck is configured; requested validation should reflect the supported tooling.
- Review-loop cost is recorded, but avoidable rounds and their causes are not yet reliably measured; preserve full denominators and distinguish genuine fixes from mechanical or policy-only continuations.
- Continue explicit hold ownership and release-condition review through existing recovery mechanisms; resolving one stale hold is not proof of universal automatic reconciliation.
- CG-402 evidence policy, CG-403 enterprise pilot and CG-408 environment acceptance retain their Phase 08 holds; real Windows backing-volume validation is not established.
- CG-506 transcript storage remains deferred in Phase 11, outside Phase 07 closure.

## Questions for the owner

_No questions for the owner._

## Findings from persona reviews

### High

- **staff-engineer** — Local reconciliation can leave a child running after timeout while the scheduler releases its checkout lease, permitting overlapping mutation during a retry. → CG-669 [draft]
- **user** — I cannot rely on task completion alone when the supplied CG-405 history shows that an author correction remained undelivered after its original PR merged. → CG-677 [draft]

### Medium

- **staff-engineer** — Command CI queries execute synchronously under the controller lock, so an unavailable adapter can block unrelated scheduler work and locked operator actions for its full timeout on each distinct head. → CG-670 [draft]
- **staff-engineer** — The command-CI output limit is checked only after subprocess.run has buffered all stdout and stderr, so it does not bound controller memory consumption. → CG-671 [draft]
- **security** — Removing or changing an approved config-file mapping leaves the previously installed file available in the persistent worker HOME. → CG-672 [draft]
- **security** — The friction and doctor CLI paths can use ambient gh authentication even when the product explicitly names a scoped token source. → CG-673 [draft]
- **project-manager** — CG-405's original PR merged before its later correction was committed, demonstrating that task completion could leave reviewed corrective work undelivered. → CG-674 [draft]
- **user** — I would expect extra approval gates from docs/operations.md and docs/architecture.md that CG-514 intentionally removed from the delivered scheduler. → CG-678 [draft]
- **user** — I would still have to intervene unnecessarily when different defects under a broad acceptance criterion are classified as the same repeated finding, as acknowledged in the closeout brief. → CG-679 [draft]
- **user** — I would hesitate to leave workers unattended while the acknowledged terminal-claim rejection startup recovery gap remains open. → CG-680 [draft]

### Low

- **project-manager** — CG-628's supplied PR description reports detailed hosted validation but labels every generated acceptance row 'no evidence given', making the completion record internally misleading. → CG-675 [draft]
- **project-manager** — The supplied walkthrough directory was unreadable to the review worker, preventing the requested inspection of captured page content. → CG-676 [draft]

## Features for the next phase

1. **Fence canonical checkout recovery until writers stop** — CG-664 [draft]
   - size: hard
   - why now: This closes a demonstrated data-integrity gap before users rely on opt-in canonical execution.
   - User value: retries cannot overlap a timed-out reconciliation writer and damage a shared checkout. Why now: the staff review's harmless probe and current exception path establish a concrete ownership gap. Size: hard. Dependencies: existing CG-406 checkout leases and process supervision. Terminate and reap owned descendants before releasing the lease; retain an actionable fenced state when cleanup cannot be confirmed.
2. **Revoke obsolete approved worker config files** — CG-665 [draft]
   - size: medium
   - why now: Current operator authorization must determine the capabilities available to the next worker.
   - User value: removing an approved mapping actually removes Garden's retained credential copy before another run. Why now: current installers only process mappings that remain configured. Size: medium. Dependencies: CG-401 mapping validation and local/SSH installation paths. Reconcile previously managed destinations for mapping deletion, destination changes and an empty allowlist while preserving unrelated files and symlink protections.
3. **Honor scoped credentials in auxiliary CLI commands** — CG-666 [draft]
   - size: medium
   - why now: Consistent credential selection closes an avoidable authority mismatch across existing entry points.
   - User value: doctor tests the identity the product will actually use and friction collection cannot silently read under another identity. Why now: source and the Security persona's mocked probe show ambient gh fallback. Size: medium. Dependencies: existing CG-395/CG-515 scoped client construction. Reuse that construction and test missing or revoked scoped credentials with ambient gh present.
4. **Make command CI asynchronous and resource bounded** — CG-667 [draft]
   - size: hard
   - why now: Enterprise adapter failures should remain isolated while exact-head merge protection stays intact.
   - User value: a slow or noisy adapter cannot stall unrelated work or consume unbounded controller memory. Why now: queries run synchronously under the controller lock and output is capped only after buffering. Size: hard. Dependencies: existing command-CI exact-head contract and detached-work/process supervision. Consume bounded stdout and stderr, terminate owned processes on timeout or overflow, and accept results only for the unchanged source and provider policy.
5. **Recover late revisions after PR or parent merge** — _skipped: flagged by the retro as a duplicate of CG-659_
   - size: hard
   - why now: The repaired incident exposed a general completion-trust problem already scoped in the backlog.
   - User value: completed tasks cannot silently omit saved corrective work, and equivalent delivered patches do not trigger unnecessary authors. Why now: CG-405 required recovery while CG-452 demonstrated rewritten-parent equivalence. Size: hard. Dependencies: existing poll, author collection and parent-terminal reconciliation. Reuse the existing draft and its preserved incident evidence.
6. **Recover worker startup after terminal claim rejection** — _skipped: flagged by the retro as a duplicate of CG-660_
   - size: medium
   - why now: Bounded recovery should restore useful service without reviving rejected work.
   - User value: one stale completed claim cannot prevent a worker from accepting valid work. Why now: the preserved incident reached repeated daemon restarts before pending-result persistence. Size: medium. Dependencies: existing claim-generation fencing, quarantine and startup recovery. Reuse the existing draft without weakening ownership or discarding evidence.
7. **Identify repeated review defects by substance** — _skipped: flagged by the retro as a duplicate of CG-661_
   - size: medium
   - why now: This reduces unnecessary intervention while preserving independent scrutiny of real defects.
   - User value: a new defect receives a normal correction instead of an erroneous repeated-finding stop. Why now: distinct cancellation and release races shared one broad criterion label. Size: medium. Dependencies: review normalization and scheduler stall classification. Reuse the existing draft, retaining genuine repeated-defect detection and lifetime limits.
8. **Make completion explanations match accepted evidence** — CG-668 [draft]
   - size: medium
   - why now: Accurate completion explanations are essential to the trust promised by delegated work.
   - User value: operators can understand what was verified and what approval policy actually applies without inspecting Python. Why now: CG-628's narrative evidence conflicts with generated rows, and operating guides still promise removed review gates. Size: medium. Dependencies: CG-514's delivered policy and existing criteria/report rendering. Correct evidence wording and operating documentation without changing accepted outcomes or requiring new author rounds.

## Persona reports

- [staff-engineer](context-garden/phase-07/docs/reviews/staff-engineer-2026-09-13.md)
- [security](context-garden/phase-07/docs/reviews/security-2026-09-13.md)
- [project-manager](context-garden/phase-07/docs/reviews/project-manager-2026-09-13.md)
- [user](context-garden/phase-07/docs/reviews/user-2026-09-13.md)
