# Phase 05 closing account

**Draft updated September 11, 2026 at 07:55 UTC. Phase 05 remains open.** RC21 is live on the controller and all six workers, both rollout pauses are cleared, and cleanup is restored to its normal batch of 20. The first ordinary pass completed 20 cleanups in 109.1 seconds, a substantial improvement that still exceeds the 10-second tick warning budget. Fresh accounting, actual failures and recovery, and current security-policy limits are recorded below. Independent account review and the owner's explicit target/security disposition remain.

This is the existing CG-537 manual session's account, not a phase-close event or a stable-release claim. The [original retrospective](retro.md) retains its **Reopen** verdict. The owner accepted earlier stabilization, retained closing review and asked at 13:16:29 on September 10 to observe real stabilization after reopening. That answer is not a target waiver, fixed soak, arbitrary task count, paid-canary requirement or another persona-review requirement. All 24 original reports and narratives remain byte-identical in [the preservation manifest](closing-account-evidence/preserved-reports.json), including [the narrative renderer](retro/narratives.md). The full prior incident chronology is preserved in [the earlier account](closing-account-evidence/account-history-through-20260911T0440.md); the current status below supersedes its then-pending statuses without rewriting its observations.

## Accepted source and current work


The nine original CG-537 dependencies were verified against native task state, exact reviewed heads and actual GitHub merges at 18:59:46 UTC. The full commit identities and CI observations are in [accepted-source.json](closing-account-evidence/accepted-source.json). A source change being accepted is separate from its deployment.

| Owner | Exact reviewed head and PR | Actual merge | Disposition |
|---|---|---|---|
| CG-504 | [c9ff23791cf1](https://github.com/joshmarcus/context-garden/pull/423) | `f27112428b57` | approve / merged |
| CG-517 | [843051cbc305](https://github.com/joshmarcus/context-garden/pull/430) | `a7bae7f6b97d` | approve / merged |
| CG-518 | [9c308aae5152](https://github.com/joshmarcus/context-garden/pull/428) | `d640f92d41aa` | approve / merged |
| CG-519 | [e79d011949d7](https://github.com/joshmarcus/context-garden/pull/426) | `5d1bb57dbfc9` | approve / merged |
| CG-534 | [5e1969163136](https://github.com/joshmarcus/context-garden/pull/442) | `ea016f47e173` | approve / merged |
| CG-535 | [7db2a96098fb](https://github.com/joshmarcus/context-garden/pull/441) | `8861a6b84225` | approve / merged |
| CG-536 | [52d581bd94ac](https://github.com/joshmarcus/context-garden/pull/446) | `5b481b7c01c9` | approve / merged |
| CG-584 | [e82422e680c1](https://github.com/joshmarcus/context-garden/pull/443) | `9565228279b5` | approve / merged |
| CG-585 | [6ea7dd8ca15e](https://github.com/joshmarcus/context-garden/pull/449) | `51241517dbcc` | approve / merged |

These owners cover user/operator documentation (CG-504), separation of authenticated worker ingress from operator controls (CG-517), workload isolation (CG-518), inert artifact previews (CG-519), corrupt-state refusal (CG-534), preservation of maintenance intent (CG-535), truthful accepted-task accounting (CG-536), cross-process worker completion persistence (CG-584), and the shared-locking import recovery (CG-585). Their accepted reviews and tests retain their original scope and limitations. This account does not turn documentation review into a live security test or cancellation into acceptance. The owner's cancellation of CG-533 and its original blocked security-verification result remain preserved; accepted corrections by the existing owners, and the actual source and deployment controls, are the evidence to assess.

Two subsequent accepted repairs must remain part of the story. CG-593 repaired real integration failures on main: a stale operator-metrics assertion and an import-order regression. CG-598 repaired the accepted-history aggregation that made RC18 page rendering too slow. Its worker's original full-suite timeout, unidentified failure marker and blocked result remain intact. The exact authenticated source was later independently reviewed, passed actual CI and merged as PR 476 at 20:34:54; this is a recovered source acceptance, not a rewritten successful worker attempt.


The following subsequent owners determine the current operational state:

| Owner | Accepted or current source | Present disposition |
|---|---|---|
| CG-599 | PR 477, `8df02641fec6`, merge `059a28e42772` | Bounded remote branch inventory is accepted and installed in RC20. |
| CG-600 | PR 478, `9945f1f2bf27`, merge `3471e86aad71` | Bounded final-output ownership and draining are accepted and installed. Original failed candidates and source simulations remain preserved. |
| CG-619 | PR 482, `69d903ace815`, merge `d77d551a1a73` | Literal complete run-ID matching is accepted and installed. The later CPU scaling problem is separately owned by CG-622. |
| CG-617 | PR 480, `f3c08b2dfb1e`, merge `52d8ed540995` | Writable disposable harness state is accepted and installed. Original approval survives the proven mechanical rebase; no count-only review was required. |
| CG-620 | PR 486, `250e098d0bfd`, merge `b4f8c19132b6` | Accepted and included in published RC21; absent from earlier immutable RC20. |
| CG-616 | PR 481, `cedee2730d58`, merge `ad708237f3db` | Explicit browser-work policy is accepted and included in RC21. The original orphan check was preserved and retired natively after actual merge. |
| CG-601 | PR 484, recovered `250a5b3b416c`, merge `cbe7874c0bb7` | Native independent approval and both exact CI runs passed; actually merged at 06:02:28 and native DONE. Included in RC21. |
| CG-621 | PR 487, `5f33ffb74800`, merge `0af5eb7db1a5` | RC20 local retry actually completed, then focused/browser review and current CI passed. Merged 06:24:59; native DONE; included in RC21. |
| CG-622 | PR 488, `9e2b01c8aab2`, merge `5d88157d1fd5` | Original capacity failure retained. Native retry, independent review, both exact CIs and scratch verification passed. Merged 06:47:13; native DONE 06:52:27; included in RC21. |

CG-601's original `040612` attempt remains a timeout with no authenticated final, original exit or known native cost. Its completed source and original outputs were preserved before one fast-forward of the existing PR; the separately parsed $0.6178936 model cost does not convert that timeout into success. The new manual attachment did not create another author run or revision allowance. Source recovery and later acceptance are separate from original execution success.

CG-620 corrects a deterministic stale-collector continuation gap without weakening CG-584's preservation of newer completion generations. The original live CG-616 interleaving was not instrumented, so it is not presented as proof of that precise interleaving. Its original orphan bytes and actual native retirement remain independently preserved.

## RC20 publication and actual activation

RC17 was published and never deployed. RC18's controller activation timed out and rolled back; no worker was activated on RC18. RC19 subsequently ran on the controller and six workers, exposing cleanup, final-output and local-startup failures recorded in the historical account. Later acceptance does not erase those outcomes.

RC20 release source is `c2c862a77eb04189dda0ad863a3510d5161d713d`, with accepted main parent `52d8ed540995efc108961364c76fc86a7bd7c6c8`. Exact candidate CI 34559139310 and main CI 34559084240 passed, alongside 198 focused tests, the actual RC19-client TCP protocol exercise and 22 worker-ingress checks. An initial cross-version invocation failed before HTTP because a helper was missing; its corrected invocation is preserved separately. The first independent review approved source and identified three deployment-guard defects. After correction, native review `043803` approved all ten helpers with 87 tests plus two subtests. Worker3's actual daemon change caused staging to refuse correctly; a separately reviewed, hash-bound reconciliation accounted for that identity, retaining the original failed stage and review findings.

Publication completed at 04:43:08. The controller switch verified all 229 installed source files at 05:11:06, and all six worker switches completed by 05:14. Maintenance resumed at 05:14:57 and dispatch at 05:14:59; both remain resumed. Exact package/VCS source, machine/process identity, configuration ownership, physical caps and deadline timers passed the postactivation audit. The operator UI remains on port 8765; the worker-only listener on 8766 denies operator routes and retains bearer authentication. The RC19 rollback was retained at that boundary; RC20 is now the immediate rollback source for RC21. The source/identity audit had no completed ordinary events and does not itself establish scheduler stabilization.

## Actual RC20 operation and cleanup failure

The first resumed RC20 tick remained CPU-bound in cleanup. Read-only samples at 05:25 and 05:38 show `re.search` through `_has_run_reference`, `classify_branches`, `branch_cleanup_inventory` and `_branch_delete_recheck`. The private state is 13,250,012 bytes with approximately 5,090 run records. Matching scans the state separately for each run, including repeated all-run matching in each branch deletion recheck. The old watch consumed 28 minutes 22 seconds of CPU over 33 minutes 10 seconds of wall time before graceful recovery. This is the new CG-622 CPU scaling defect; it is distinct from CG-599's installed remote-inventory repair.

Root performed four RC20 watch-main graceful interruptions at 05:44:04, 05:48:05, 05:50:48 and 06:52:24 to release the scheduler lock for native recovery and configuration reload. Together with 52 historical RC19 root interventions and the separate Herdr withdrawal event, these remain operator interventions, not completed ordinary ticks. Exact installed source, service/PID identity, process-only shutdown and separately supervised local work were preserved. A preceding fresh-stack attempt timed out, safely resumed and sent no interrupt. Further WSL launches failed with `0x8007274c`; no WSL restart or runtime hotpatch was applied. The original helper path error, reading-list failure and configuration-editor refusal remain recorded.

Cleanup batch size was reduced from 20 to **one** at 05:49:38. The configuration loader validates this setting, although the editable-key catalogue omits it. Only that YAML value changed through an atomic edit under the native configuration lock, after full layered validation and inherited-policy checks. The original private bytes, all other settings and the 20 GiB physical reserve remain intact. Cleanup is enabled, and every deletion guard remains required. The temporary limit was removed after all six RC21 worker activations, as recorded below. Three subsequent ordinary RC20 passes still took 604.4, 614.5 and 613.7 seconds. The temporary setting did not establish acceptable scheduler latency; it is not the repair.

The service PATH initially could not locate PowerShell despite the saved verified backing path. An alias to the existing genuine Windows executable made that same PATH resolve it; a real capacity probe passed. Native resource pressure cleared at 05:44:27, and CG-621's local retry launched at 05:44:32 and produced model output. Its original pre-model failure and hold-release hash remain unchanged. CG-601's independent reviewer also completed and returned an authenticated final under RC20. These establish specific recovered behavior while collection remains delayed; neither is treated as universal stabilization.

Performance evidence retains its actual scope. RC19's accepted-metrics calculation improved from 16.616 seconds to 0.192 seconds on an identical fixture and one-CPU bound. Actual Windows navigation later ranged around 2.8–3.1 seconds with a 4.564-second cold request. During RC20 concurrent validation, Inbox took 11.245 seconds and Now 5.512 seconds. The complete Inbox sweep at 05:51:38 returned HTTP 200 in 3.392 seconds and found no unhandled operator actions. No universal subsecond claim follows from any of these samples. Original CPU, ingress-memory, disk and output failures remain part of the account.

## RC21 activation and observed ordinary work

[RC21](https://github.com/joshmarcus/context-garden/releases/tag/v0.3.0rc21) is exact `e38b8404175e9b3a9ffcddb41251db3ac2d6f611`, based on accepted main `5d88157d1fd5d9a15fcd746a888d05e179c75543`. The [accepted repair identities](closing-account-evidence/accepted-repairs-rc21.json) bind actual heads and merges. Main CI 34571430810 and candidate CI 34572425877 passed; 317 focused tests, the actual RC20-client TCP lifecycle and 22 ingress checks passed. The initial focused invocation selected a nonexistent test path and ran no tests; its failure was retained separately from the corrected run. Native independent release review `071336` approved source and all ten deployment helpers with no blocking findings. Publication was verified at 07:27:25.

Staging initially preserved workers 0, 1 and 3 because their daemon identities had changed. Fresh all-six audits verified the same installed source, machine, configuration, caps and deadline. Ubuntu unattended-update logs established two clean worker-service restarts on each affected host while upgrading Python and libc; these are OS-maintenance events, not root interventions or automatic crash recovery. A separate independent review `073556` approved the narrowly pinned identity reconciliation with 25 tests. Published helper/preflight bytes and original stage refusals remain unchanged.

The native drain at 07:47:44 found no active execution or unreaped result and preserved CG537's original manual reservation. The controller switch verified at 07:48:21, all six worker activations finished by 07:49:06, and cleanup returned from one to 20 at 07:49:07. Maintenance resumed at 07:49:10 and dispatch at 07:49:12. All 229 source files on the controller and each worker, exact process/configuration identity, physical caps and deadline timers passed the postactivation audit. The switch preserved 18,945 stable payloads and all three active manual payloads. RC20 rollback remains available. No further graceful watch interruption was needed for this rollout.

The first ordinary RC21 pass completed at 07:51:10 in **109.1 seconds**, including a 101.5-second audit and 20 guarded branch deletions. The latest pre-switch RC20 pass took 599.3 seconds for one deletion. This is an observed workload change, not a same-fixture benchmark; the independent pure-matcher comparison separately matched all 4,984 actual IDs in 0.923066 seconds. The native 10-second tick warning remains material: deletion work still causes a slow pass, and the account does not declare universally fast scheduling. The inventory retained 379 needed branches and one uncertain branch; normal cleanup does not authorize dropping their protection.

Native Windows localhost HTTP requests returned 200 for Now, Inbox and CG621 in 3.888, 3.364 and 3.994 seconds. These are PowerShell HTTP measurements, not browser interactions or proof of subsecond pages. Earlier candidate page probes under concurrent tests took as long as 14.559 seconds; a separate quiet observation ranged from 1.333 to 3.063 seconds for full pages. All observations remain preserved.

## Historical release and action provenance

The authoritative historical RC16 source is `671633857c8ac253d9238196a684d58838d7fa34`; its September 9 independent final deployment approval verified all 194 source files and the split controller, with the actual Windows and stress-test limits retained. Stale RC12 and still-earlier deployment documents are historical records, not evidence of the current installed source. The old deployment documents remain preserved; [the current deployed record](../../docs/releases/deployed.json) now identifies RC21 separately from accepted source and the still-unpublished stable release.

Owner actions include the explicit budget/deadline renewals, freeing backing-drive space, selecting the CG506 storage/S3 deferral, cancelling CG533 and withdrawing Herdr. The delegated operator performed deployment, native Inbox decisions, exact-source recovery and the recorded watch interruptions. The four RC20 interruptions and 52 historical RC19 interruptions are specific counted actions, not a complete count of all operator activity or proof of personal human hours. RC18's failed activation/rollback, RC19 ingress-memory recovery, original task timeouts, source recovery and OS updates retain distinct provenance.

CG347/348 retain their owner-approved Phase07 placement. CG423's accepted product enrollment work is distinct from the operator's earlier saved-key setup and six-host renewal; that setup does not itself establish a product ScaleOperation rollout. Its recorded macOS/live-rollout limitations remain, without making an optional live canary a closure requirement.

## Security, onboarding and validation scope

[Direct RC21 inspection](closing-account-evidence/accepted-source-inspection-rc21-0737.json) used exact published source with non-executing policy and response construction. Design and run-artifact responses apply a sandbox CSP and `nosniff` to SVG; unknown formats are attachments. Live worker-route denial and native authentication were verified separately. This is not an executed malicious-payload exercise.

CG-518 remains an **opt-in capability**. The currently configured required policy is false, no OS wrapper is configured, and constructing the current Codex planner command shows bypass mode. Enabling the required policy rejects bypass, but current operation does not establish enforced planner isolation. The cancelled CG-533 security verifier's original blocked report remains preserved; cancellation does not resolve that finding. Final disposition must explicitly address this actual policy state.

Onboarding stores discovered commands in setup metadata. The scaffold selects Claude and initially has empty pre-PR/CI checks. Accepted documentation instructs Codex-only users to select that harness before onboarding, verify discovered commands in a disposable clone and review configuration before approving work. This is a documented manual workflow; automatic harness selection and activation of discovered checks are not established here.

Operational rollout covered the Ubuntu WSL controller and existing Linux/systemd workers. macOS rollout was not tested. Deterministic source, protocol, response and disposable lifecycle tests retain their own recorded platform coverage. Live canaries are optional and have not been converted into acceptance or closure gates.

## Resource authority and preserved deferrals

The owner extended the same six workers by twelve hours at 23:25 on September 10. All six host and six external timers are verified for **September 11 at 11:36:42 UTC (7:36:42 a.m. Eastern)**. No replacement launch followed. Six hosts, the aggregate $80 AWS cap, $8 reserve and $79.200648 conservative bound remain; model-ledger spending is separate. Controller aggregate 2 CPU/5 GiB, worker 3 CPU/12 GiB/no swap, global seven/local two/review three/heavy-test one limits remain. The worker-ingress component's earlier accounted 512 MiB high/768 MiB maximum allocation stays within that aggregate cap. No further spending or deadline extension is inferred.

CG-506's owner-selected storage-growth/S3 deferral and frozen Phase08 work remain held. Accepted archive/cleanup code is not authority for a new bulk archive or migration. Herdr Phase09 remains withdrawn, frozen and administratively closed; CG-602 is cancelled and CG-603–615 are removed from discovery with original source/briefs and reserved IDs preserved. Withdrawal is not implementation success or permission to resume that work.

## Outcome accounting through September 11 at 07:00 UTC

The cutoff is **September 11 at 07:00:29.509833 UTC**, calculated from exact accepted main `5d88157d1fd5d9a15fcd746a888d05e179c75543`. The [sanitized input projection](closing-account-evidence/calculation-20260911T0700/calculation-input.json), [full results](closing-account-evidence/calculation-20260911T0700/calculation.json), [exact replay](closing-account-evidence/calculation-20260911T0700/replay-verification.json) and [reproduction instructions](closing-account-evidence/calculation-20260911T0700/README.md) retain missing observations. Membership follows current phase assignment. The completion window selects proven accepted tasks, then includes their runs through acceptance; the reopening total is not merely spending incurred after reopening. The previous September 10 calculation and its inputs remain unchanged. Its source was `d640f92d`, not RC19 as earlier account prose incorrectly stated; the [attribution correction](closing-account-evidence/calculation-20260911T0700/preparation.json) preserves that distinction.

| Measure | Phase 04 lifetime | Phase 05 lifetime | Phase 05 accepted since reopening |
|---|---:|---:|---:|
| Proven accepted tasks | 62 | 141 | 16 |
| Fully priced accepted tasks | 55 | 94 | 12 |
| Accepted tasks with unknown cost | 7 | 47 | 4 |
| Known accepted-task cost | $504.8745 | $879.4230 | $57.8696 |
| Complete cost per accepted task | unavailable | unavailable | unavailable |
| First-pass approvals / reviewed accepted tasks | 45 / 61 | 48 / 131 | 10 / 16 |
| First-pass rate | 73.77% | 36.64% | 62.50% |
| Recorded merge transitions | 62 | 142 | 16 |
| Unique accepted tasks merged outside the queue | 18 | 62 | 8 |
| Agent rebases / counted merge transitions | 61 / 62 | 89 / 142 | 1 / 16 |

Phase 05's 168 current done statuses are not interchangeable with its 141 proven accepted tasks. The 27-task difference is not promoted into the accepted cohort. The extra merge transition is not an additional unique accepted task. An outside-queue merge records a mechanism, not proof that Josh personally had to merge it; this data does not establish human hours or required personal intervention. Accepted status, actual source acceptance, source recovery and an original successful execution remain separate.

The operator ledger contains 41 priced but phase-unattributed records totaling $995.53, with no phase-attributed observations for these cohorts and no ledger observation in the reopening window. Operator share is therefore **unmeasured**, not zero. A raw zero from an empty filtered ledger reflects absent observations. No billing or human-hours estimate has been invented.

## Target disposition still required

| Phase target | Current evidence | Disposition |
|---|---|---|
| At most $4 per accepted easy task | 26 accepted easy tasks, only 17 fully priced; nine have unknown cost | Unproven; neither dividing the known $53.2834 subtotal by all 26 nor by the 17 priced tasks establishes the complete accepted-cohort average |
| At least 90% first-pass approval | 48 of 131 reviewed accepted tasks, 36.64%; ten accepted tasks have no review observation | Missed |
| Zero hand merges | 62 unique outside-queue merges; actor attribution does not establish required personal human work | Recorded mechanism target missed; personal-effort claim unestablished |
| Fewer than 0.3 agent rebases per merge | 89 / 142 = 0.6268 | Missed |
| Operator share below 29% | No phase-attributed operator ledger coverage | Unproven |

The reopening cohort provides later evidence: 10/16 first-pass approvals, eight outside-queue merges and one agent rebase across 16 counted merges. Four accepted tasks still lack complete cost, so its complete cost per accepted task is now unavailable. Those later unknowns supersede the earlier nine-task cohort's fully priced average without rewriting it. No easy task completed in the reopening cohort. Improved later observations do not erase full-phase misses or establish absent easy-task economics and operator costs.

The accepted cleanup repair is activated and its actual ordinary behavior is recorded. Complete independent review of this account and obtain the owner's explicit disposition of the documented target misses/unknowns, residual cleanup latency and current policy limits before closure. The owner may accept the limits with accountable follow-ups or retain the phase open for specified remediation. The existing stabilization answer is neither disposition. Stable publication follows actual closure and exact-source release gates.

The existing implementation owners remain accountable for their accepted behavior: CG536 and CG541 for truthful accepted-cost/effort accounting, CG526 for objective escalation, CG454 and CG514 for avoiding unnecessary rebases and count-only review gates, and CG517/518/519 for ingress, sandbox and artifact boundaries. Their accepted fixes do not supply missing historical billing, erase target misses or establish enforced isolation in this deployment. The proposed operational follow-through is for the delegated operator to keep subsequent cohort reporting honest and for the product owner to decide when required sandbox enforcement and remaining latency work become requirements. This is a proposed disposition for the owner, not a newly approved exception or a duplicate implementation task.

The [dated operational evidence index](closing-account-evidence/operational-update-20260911T0755.json) binds actual receipts and the preservation check. Private scheduler snapshots, credentials and worker identity material are not copied into this account.
