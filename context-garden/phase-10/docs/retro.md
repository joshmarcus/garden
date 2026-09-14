# Retrospective: context-garden/phase-10

_2026-09-14T00:06:03+00:00 · hard tier (gpt-6-astra)_

## What changed

Phase 10 completed 20 tasks and cancelled two fixture-repair tasks, delivering Git-backed coordination, installation-bound execution authority, acknowledged handoff, inherited phase ownership, automatic permitted username startup, personal Inbox and public projection boundaries, concurrency-only operating profiles, Mark done, quieter task pages and sidebar project selection. Substantive review repaired ownership bypasses and cancellation hazards; CG-657 also reduced procedural author send-backs. Supplied evidence records release 0.4.3, passing ordinary hosted CI and isolated installation exercises, not production multiplayer activation. Read-only inspection confirmed the principal persona findings in source 7d5d6a56 and verified that release 0984b5d2 did not alter those paths. Equivalent repeated friction reports are grouped below; harvested-friction.md explicitly contains none, while Reported and marked-comment sources were inspected. No files were changed, no tests were rerun, and closure preserves the recorded outcomes without claiming migration or live rollout readiness.

## Numbers

- recorded phase run/model costs: $251.74 partial known spend (historical phase cohort, separate from the current AWS worker budget)
- operator: unavailable — no operator turns were captured by this metric; this does not mean zero operator effort or cost
- recorded total: $251.74 partial known spend; operator costs and unpriced runs are incomplete
- accepted cohort: 20 tasks (10 priced, 10 unpriced); cost/accepted: unavailable
- cohort rule: completion in the phase window; all task runs through acceptance
- hand merges: 0 (of 20 merged PRs)
- tick duration: mean 22.55s, max 617.33s (3809 ticks)

### Outcomes by tier

| tier | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| hard | — | — | 0% |

### Outcomes by model

| model | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| gpt-5.6-luna | $0.05 | — | — |
| gpt-5.6-sol | — | — | 0% |
| gpt-5.6-terra | $0.98 | $4.69 | 0% |
| unknown | — | — | 0% |

### Outcomes by harness

| harness | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| codex | — | — | 0% |
| unknown | — | — | 0% |

### Outcomes by pool member

| pool member | mean/run | cost/accepted task | first-pass approval |
|---|---:|---:|---:|
| unknown | $0.34 | $12.59 | 0% |

## Verdict

**Close with follow-ups.**
Nothing blocks closing context-garden/phase-10. The follow-ups below become draft tasks in phase-11.

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Missing multiplayer specification in dispatched context | CG-629 | CG-640 / PR530 | fixed | PR530 created and indexed the previously absent specification; the repeated reports from CG-630, CG-631, CG-632, CG-634, CG-638 and CG-639 describe earlier snapshots, although reliable context delivery remains separately unresolved. |
| Missing specification in the integration task's parent checkout | CG-640 | CG-640 / PR530 | fixed | The merged integration task added specs/multiplayer.md, which exists in the inspected source, although its architecture text is now stale. |
| No configured static typecheck command | CG-629 | – | still true | The inspected pyproject.toml configures pytest and Ruff without mypy or pyright, confirming the equivalent reports from CG-630, CG-631, CG-633, CG-635, CG-636, CG-638 and CG-639. |
| Incorrectly pluralized focused-test filenames | CG-629 | – | outdated | The report records correction and rerunning with actual paths, so the failed collection command is historical rather than an outstanding test failure. |
| Scheduler test paths omitted their scheduler directory | CG-633 | – | outdated | The actual suites are under tests/scheduler and later accepted scheduler validation used the existing suites. |
| Nonexistent remote-worker test filename | CG-633 | – | outdated | The worker explicitly corrected the command to tests/test_remote_worker.py and continued validation. |
| Workers could not retrieve authenticated GitHub diagnostics | CG-629 | – | still true | Equivalent reports recur through CG-630 to CG-640 and CG-688, CG-690 and CG-691, with supplied failing nodes and local reproductions providing workarounds but no demonstrated repair to diagnostic delivery. |
| Missing GH_TOKEN and unusable public PR metadata | CG-640 | – | still true | The preserved report records unavailable PR530 metadata and no later evidence establishes worker-readable authenticated diagnostics; this calls for scoped evidence delivery rather than copying controller credentials. |
| Workers cannot push or independently produce hosted CI | CG-630 | – | disputed | The equivalent CG-632, CG-637 and CG-639 reports describe the intentional controller-owned publishing and CI boundary, not a worker capability that should be enabled. |
| Stale exact-head CI evidence treated as an implementation revision | CG-632 | CG-657 / PR540 | fixed | CG-657 separates non-implementation recovery from author corrections and preserves accepted evidence across proven patch-identical rebases while retaining current-head merge gates. |
| Pending CI in the handoff review | CG-634 | – | outdated | The task subsequently merged as PR521 and supplied release evidence records passing ordinary CI, superseding this pending-review snapshot. |
| Migration review carried a stale CI SHA | CG-639 | – | outdated | PR529 merged and release CI subsequently passed, although neither event resolves the independently observed Git migration defect. |
| Project-neutral views leaked unauthorized project data | CG-629 | CG-629 / PR504 | fixed | The final accepted review verifies project authorization, transport enforcement and fail-closed scheduler and worker boundaries rather than retaining the initial visibility finding. |
| Whole-phase persona dispatch omitted phase-owner authority | CG-630 | CG-630 / PR511; CG-633 / PR519 | fixed | The final ownership and scheduler reviews accept explicit phase-operation authority and lifecycle fencing. |
| Lifecycle fixture lacked assignment and immutable checkout identity | CG-630 | CG-630 / PR511 | fixed | The worker records correcting the fixture and passing the member suite, and the final inventory explicitly retains accepted outcomes after the test-double correction. |
| Coordinator acceptance summary labeled as review friction | CG-631 | – | disputed | The quoted review-loop entry reports satisfied criteria rather than an unresolved defect, and its coordinator architecture was subsequently superseded by the accepted Git implementation. |
| Historical coordinator implementation remains | CG-631 | – | still true | Released migration.py still constructs Coordinator over coordination.db, so the retained implementation is not confined to inert historical evidence. |
| Historical HTTP-coordinator tests remain in client integration | CG-632 | – | still true | tests/test_multiplayer_workflow.py still constructs HTTP/SQLite coordinators for the prominent two-user and phase-owner journeys despite normal startup using Git. |
| Restacked client tests contained duplicates and stale expectations | CG-632 | CG-632 / PR516 | fixed | The final client review accepts the listener, claim-reuse and enrollment-fixture corrections, and supplied final ordinary CI passed. |
| Direct lifecycle controls and user-owned worker binding incomplete | CG-633 | CG-633 / PR519 | fixed | The final review reports 154 passing focused cancellation, manual-control and scheduler-authority tests and accepts runner-aware ownership fencing. |
| Unavailable stacked base ref during scheduler review | CG-633 | – | outdated | The worker inspected the committed revision instead, and the stack has since merged; the missing local ref does not establish an outstanding source defect. |
| Unavailable stacked base refs during handoff review | CG-634 | – | outdated | Both reports concern local comparison refs in intermediate worktrees, superseded by committed revision inspection and merged PR521. |
| Unavailable local project-selector parent branch | CG-636 | – | outdated | The worker used the existing origin tracking ref and PR525 subsequently merged. |
| Startup checkout initially omitted its declared stack parent | CG-635 | – | outdated | The worker rebased its private branch onto CG-634 before implementation, resolving the reported checkout state. |
| Status-only 303 assertion masked authority failure | CG-633 | CG-633 / PR519 | fixed | The revised verification inspects the redirect diagnostic and the final scheduler review accepts the substantive authority behavior. |
| Legacy MemberRegistry fixtures lacked Git enrollment | CG-633 | CG-633 / PR519; CG-632 / PR516 | fixed | Final revisions repaired hosted compatibility and Git enrollment fixtures, with passing focused checks and supplied release CI replacing the earlier exploratory failures. |
| Four legacy fixtures expected pre-Git statuses instead of setup-required 503 | CG-633 | CG-633 / PR519; CG-632 / PR516 | fixed | Merged history includes Git enrollment and authority fixture repairs; the obsolete expectations do not justify weakening setup-required denial or restoring cancelled CG-685. |
| Repeated handoff definitions and stale fixtures after restack | CG-634 | CG-634 / PR521 | fixed | The actual final restores the permit lifecycle guard lost during rebase and reports 64 focused passes, followed by an accepted 80-test coordination and assignment review. |
| Repeated pre-Git commits complicated handoff rebasing | CG-634 | – | outdated | That branch-restoration episode ended in merged Git handoff work, while the broader risk of losing corrections during restack belongs with existing recovery and review drafts. |
| Thirteen supplemental assignment and authorization failures | CG-634 | – | outdated | Later accepted coordination and assignment checks and final release CI supersede this intermediate stacked-head result; cancelled CG-686 is not evidence of a remaining failure. |
| No supported command starts the required coordinator | CG-635 | – | outdated | The owner-selected Git architecture and merged CG-631/CG-632 explicitly remove the coordinator-service requirement, although current setup and migration guidance still needs correction. |
| Browser history restoration broadened polling scope | CG-636 | CG-636 / PR525 | fixed | The final project-scoping review explicitly accepts repaired history-restored polling, and CG-692 preserves the same boundary in the sidebar. |
| Inbox snapshot scan expectation observed eight instead of two | CG-637 | CG-637 / PR527 | fixed | The report records restoring the legacy projection path, with functional Inbox assertions and later accepted integration evidence. |
| Inbox restacks reintroduced duplicate tests, indentation and checkout-identity errors | CG-637 | CG-637 / PR527 | fixed | The final Inbox implementation merged with accepted administrative isolation and current-assignment authorization, and final ordinary CI passed. |
| Administrative cards leaked into non-admin Team Inbox | CG-637 | CG-637 / PR527 | fixed | The final review explicitly accepts administrative isolation and stable recipient projections. |
| Public-viewer approval recorded as a blocking review-loop finding | CG-638 | – | disputed | The quoted entry says the isolated viewer satisfies its contract with no blocking defects, consistent with the security persona's source assessment. |
| Migration restack duplicated methods and tests | CG-639 | – | outdated | The historical restack cleanup reached accepted merged source and passing release CI; the current SQLite migration mismatch is a separate substantive finding. |
| Complete workflow lacked restart and phase-owner lifecycle verification | CG-640 | – | still true | Later commits added those journeys for the old coordinator, but source inspection and both engineering and project-management reports show the complete supported Git journey remains insufficiently demonstrated. |
| Review-round diagnosis missing from dispatched context | CG-657 | – | still true | The diagnosis exists in current product context but its availability to the original worker was not repaired or proven, and CG-683 remains the existing context-delivery draft. |
| Inherited Git tests conflicted with acknowledged handoffs | CG-687 | CG-634 / PR521; CG-687 / PR547 | fixed | The actual finals update stale handoff expectations and verify inherited ownership against accepted Git authority. |
| Pending phase-owner handoff bypassed accepted ownership | CG-687 | CG-687 / PR547 | fixed | The final revisions unify accepted ownership across web, Inbox, scheduler and remote claims and retain the old effective owner until guarded handoff completes. |
| Windows Edge unavailable for requested captures | CG-690 | – | disputed | The equivalent CG-691 report concerns a documented legacy WSL fallback, while current policy permits Linux Chromium or credible alternate evidence and final reviews accepted the delivered outcomes. |
| Git enrollment fixture used full installation records | CG-690 | CG-690 / PR557 | fixed | The worker corrected the fixture to installation-to-member mappings while adding the assignment journey. |
| Automatic identity acceptance recorded as review friction | CG-690 | – | disputed | The quoted review-loop summary accepts coherent identity and ownership behavior, and the final review intentionally preserves the installation-bound 403 denial. |
| Every review round represents the same repeated defect | – | – | disputed | Actual finals distinguish permit deletion, claim-identity replacement, unconfirmed cancellation, a guard lost during rebase, fixture drift and the accepted CG-690 403 correction, so lifetime counts cannot establish one repeated cause. |
| Unmapped acceptance rows appear as missing verification | – | – | still true | The project-manager report contrasts generated missing-evidence labels with substantive supplied finals; existing CG-682 covers this distinction. |
| Required retrospective walkthrough inaccessible to personas | – | – | still true | All four supplied reports disclose denied walkthrough access, and existing CG-683 addresses readable sanitized context without expanding private-data access. |
| Git migration and standalone reversal use obsolete authority | – | – | still true | migration.py requires coordinator_url, initializes coordination.db and checks only local runs and old coordinator obligations before export, unchanged between inspected 7d5d6a56 and release 0984b5d2. |
| Git transport can wait indefinitely | – | – | still true | git_coordination.py calls subprocess.run without deadlines in _run and _push, preventing bounded recovery when Git or authentication helpers stall. |
| Authority refresh revalidates all retained history | – | – | still true | GitStateStore._validate_history walks rev-list from the root and reads every commit on refresh; this is a source-derived scaling risk, not a measured production incident. |
| Automatic local authentication accepts unknown Host values | – | – | still true | OriginCheck grants the ambient local principal without Host validation and applies Origin checks to mutations; the security persona reproduced private GET access in memory, without claiming a browser exploit. |
| Multiplayer specification contradicts the Git operating guide | – | – | still true | Released specs/multiplayer.md describes a single authoritative coordinator and server-timed claims while docs/multiplayer.md rejects that service. |
| Closed phase must be reopened solely for retrospective | – | – | still true | The current owner scope explicitly records temporary reopening for the native retro workflow, distinct from authorizing further implementation. |

## What the personas said

Staff engineer scored 6/10, valuing Git ownership safeguards while identifying obsolete migration authority, unbounded transport, history growth and legacy integration journeys. Security supported the cooperative Git trust boundary and isolated public projection but reproduced an unknown-Host private-read gap in production middleware using synthetic in-memory requests; browser exploitability was not demonstrated. Project manager scored 7/10, accepted the delivery record while requiring explicit disposition of Git migration and integrated acceptance before activation, and recommended reusing CG-661 and CG-682 for review classification. User scored 8/10, welcomed inherited ownership and simpler controls, and requested coherent Git guidance and retrospectives without reopening completed work. All disclosed unavailable walkthrough access; the supplied walkthrough represents an older runtime and cannot establish the released UI's live appearance.

## Still open

- Git-only migration, resumable cutover and standalone reversal must consult accepted shared obligations.
- Unknown HTTP hosts can receive ambient local identity for private reads.
- Git fetch, push and credential-helper stalls lack bounded recovery.
- The complete two-installation scheduler and phase-owner acceptance journey still uses obsolete coordinator fixtures.
- Authority refresh cost grows with retained history; production performance has not been measured.
- Released multiplayer documentation contradicts the accepted architecture and lacks a coherent setup and recovery procedure.
- Closed-phase retrospectives require misleading temporary reopening.
- Required context and controller-owned diagnostics are not reliably readable by workers; reuse CG-683 without distributing credentials.
- Review summaries and repeated-defect classification still need existing CG-682 and CG-661; restack recovery remains covered by CG-659.
- No static typechecker is configured; verification instructions should acknowledge actual configured checks rather than demand a nonexistent command.

## Recorded question and decision

- **Should the Git migration and reversal defect be prioritized for correction before any multiplayer pilot, or should migration and reversal remain explicitly unsupported pending a later correction?** — decision card `retro-reconcile-283e581e06844b96b5105874a8c99cd1-q0`
  - The released commands still use obsolete authority; this is a future activation and support decision, while the current retrospective-only closure and Phase 11 freeze can remain intact.
  - options: Prioritize the frozen corrective draft before considering activation, Defer correction and explicitly withhold migration and reversal support

## Findings from persona reviews

### High

- **staff-engineer** — Migration still initializes SQLite authority, and standalone export does not check accepted Git claims or unresolved effects. → CG-695 [draft; consolidated]
- **staff-engineer** — Git coordination subprocesses have no timeout, so a stalled remote or credential helper can indefinitely block authority refresh and handoff progress. → CG-697 [draft; consolidated]
- **project-manager** — The supported migration commit initializes SQLite coordinator authority and records completion without initializing the accepted Garden Git state. → CG-695 [draft; consolidated]

### Medium

- **staff-engineer** — Every Git refresh walks and decodes the entire state history even when its head is unchanged, while each transaction retains an expanding operations table. → CG-700 [draft; consolidated]
- **staff-engineer** — The headline two-user recovery and phase-owner journeys still inject the obsolete HTTP/SQLite coordinator rather than exercising the configured Git client. → CG-698 [draft; consolidated]
- **security** — Automatic local authentication grants private read access under arbitrary Host headers, leaving a DNS-rebinding confidentiality gap. → CG-696 [draft; consolidated]
- **project-manager** — CG-640's complete-workflow evidence still uses the historical HTTP/SQLite coordinator, leaving the complete delivered Git journey insufficiently demonstrated. → CG-698 [draft; consolidated]
- **project-manager** — Acceptance summaries lose substantive supplied evidence, while lifetime revision counts combine real defects, restack regressions and fixture or instruction corrections. → CG-682 and CG-661 [existing drafts; consolidated]
- **user** — I followed the multiplayer documentation and found conflicting descriptions of what I must operate, without the promised setup and recovery instructions. → CG-699 [draft; consolidated]
- **user** — I had to treat a finished phase as open again solely to obtain its retrospective, according to the supplied owner scope. → CG-701 [draft; consolidated]

## Features for the next phase

1. **Repair Git migration and standalone reversal** — CG-695 [draft]
   - size: hard
   - why now: The supported recovery boundary must agree with the architecture before users entrust existing work to multiplayer.
   - User value: move an existing garden into or out of multiplayer without losing authority or duplicating work. Why now: released migration still initializes SQLite and export misses other installations' Git obligations. Size: hard. Dependencies: delivered CG-631, CG-632 and CG-634; correct the implementation delivered by CG-639 without duplicating its historical task. Cover resumable commit, preserved ownership/history, Git-backed startup and refusal under unresolved work.
2. **Validate hosts before automatic local authentication** — CG-696 [draft]
   - size: medium
   - why now: This closes a concrete confidentiality gap without adding another login interaction.
   - User value: retain effortless local startup while protecting private reads. Why now: the security reproduction and source show ambient identity under unknown Host values. Size: medium. Dependencies: CG-690 and web trust middleware. Use explicitly configured listener names, reject unknown hosts for GET and HEAD, and preserve permitted localhost behavior and mutation checks.
3. **Bound Git transport and recover ambiguous pushes** — CG-697 [draft]
   - size: hard
   - why now: The existing recovery protocol cannot help until stalled transport returns control.
   - User value: a slow remote produces a recoverable state instead of a frozen scheduler. Why now: Git subprocesses have no deadlines. Size: hard. Dependencies: CG-631 and CG-632. Apply total operation deadlines, noninteractive authentication and descendant cleanup; reconcile interrupted pushes through their existing operation IDs before permitting effects.
4. **Verify the supported Git multiplayer journey** — CG-698 [draft]
   - size: hard
   - why now: A bounded integrated journey connects strong protocol tests to the product users actually start.
   - User value: confidence that normal migration, startup and two independent schedulers work together. Why now: CG-640's headline journeys still inject HTTP/SQLite authority. Size: hard. Dependencies: Git migration repair and delivered CG-631 through CG-640. Use independent roots and a disposable bare remote through supported configuration and scheduler entry points, covering contention, restart, partition, late results, acknowledged handoff and phase closure.
5. **Publish coherent Git setup and recovery guidance** — CG-699 [draft]
   - size: medium
   - why now: Clear operating instructions are necessary to make the delivered simplifications usable.
   - User value: administrators can admit users, assign work and resolve blocked handoffs without choosing between contradictory instructions. Why now: the released specification describes a rejected coordinator. Size: medium. Dependencies: accepted Git contracts and the migration repair for executable migration examples; architecture corrections can proceed earlier. Preserve automatic username binding, explicit unassignment and installation-bound authority.
6. **Reuse validated Git coordination history** — CG-700 [draft]
   - size: medium
   - why now: Addressing demonstrable history-dependent work early avoids changing the coordination architecture later.
   - User value: authority checks remain responsive as the garden accumulates operations. Why now: every refresh validates history from its root. Size: medium. Dependencies: CG-631 and bounded transport. Cache immutable validated ancestry, batch reads and retain rewrite detection; define checkpoint and retention constraints that preserve ambiguous-operation resolution.
7. **Run retrospectives without reopening closed phases** — CG-701 [draft]
   - size: medium
   - why now: Reflection should not implicitly authorize another implementation cycle.
   - User value: learn from released work while its completion status stays accurate. Why now: this retrospective required temporary reopening. Size: medium. Dependencies: existing phase-owner authorization and CG-684's publication-policy preservation. Permit an authorized retrospective claim on a closed phase, suppress implementation dispatch and retain draft follow-ups in the frozen destination.
8. **Distinguish unmapped acceptance rows from missing evidence** — _skipped: flagged by the retro as a duplicate of CG-682_
   - size: medium
   - why now: Accurate summaries reduce unnecessary review work while preserving real failures.
   - User value: completion reports accurately reflect substantive accepted verification. Why now: Phase 10 summaries lose evidence present in actual finals. Size: medium. Dependencies: existing criteria and review rendering; coordinate with CG-661 for substantive defect classification. Reuse the existing draft and add Phase 10 examples without reopening accepted implementations.

## Operator review and task consolidation

The delegated operator reviewed the four original persona reports and the independent reconciliation. The close-with-follow-ups verdict is retained. Migration still initializes the obsolete coordinator, and the Git transport helper has no subprocess timeout; both were corroborated in the reviewed source. The Host finding retains the security reviewer's synthetic middleware evidence and its explicit limit: no browser exploitation was demonstrated. Production multiplayer remains unactivated.

Seventeen generated drafts are consolidated into seven distinct proposals plus the existing review-evidence tasks. Original reports and the native generated commit remain preserved. No finding, failed run or lifetime counter was erased, and no additional persona or author round was requested. Missing required walkthrough access continues to belong to CG-683; publication-policy preservation belongs to CG-684.

| Generated draft(s) | Retained task |
| --- | --- |
| CG-702, CG-707 | CG-695: Git migration and reversal |
| CG-706 | CG-696: automatic-session Host validation |
| CG-703 | CG-697: bounded Git transport |
| CG-705, CG-708 | CG-698: configured Git integration journey |
| CG-710 | CG-699: setup and recovery guidance |
| CG-704 | CG-700: incremental history validation |
| CG-711 | CG-701: closed-phase retrospective |
| CG-709 | Existing CG-682 and CG-661: evidence mapping and defect classification |

The migration question was answered under delegated owner authority: prioritize its frozen corrective draft before considering activation. This grants no implementation or pilot authority. Phase11's actual frozen frontmatter and previous goals are preserved, each retained draft has concrete reading and acceptance outcomes, and the original persona reports are included with working relative links.

## Persona reports

- [staff-engineer](reviews/staff-engineer-2026-09-13.md)
- [security](reviews/security-2026-09-13.md)
- [project-manager](reviews/project-manager-2026-09-13.md)
- [user](reviews/user-2026-09-13.md)

## Answers

- **Should the Git migration and reversal defect be prioritized for correction before any multiplayer pilot, or should migration and reversal remain explicitly unsupported pending a later correction?** — answered: Prioritize the frozen corrective draft CG-695 before considering any multiplayer activation. Migration and standalone reversal are not supported for production use until the Git authority and unresolved-obligation corrections are verified. Keep Phase11 frozen and all proposed tasks unapproved; this prioritization does not authorize implementation, a pilot, runtime promotion, additional spending or an extension of the worker deadline. Phase10 remains closed with follow-ups. (by delegated operator (owner authority) at 2026-09-14T00:08:32+00:00)
