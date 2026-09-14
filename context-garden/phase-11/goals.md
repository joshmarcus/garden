---
plant: oak
latin: Quercus robur
plate: XI
frozen: '2026-09-13'
---

# Task requirements and worker capability routing

## Implementation approval

Owner explicitly approved Phase 11 implementation on September 12. All eight tasks are approved for remote execution within the existing two-worker envelope. On September13 the owner released all merge freezes and re-enabled automatic merging through the ordinary review, CI and merge queue gates. Develop as a single-parent stack CG645 -> CG646 -> CG647 -> CG648 -> CG649 -> CG650 -> CG651 -> CG652, preserving the original prerequisites transitively. Independent review and CI remain required; worker capacity, spending limits, cutoff and non-merge data-access restrictions remain unchanged.

## Outcome

Tasks declare capability and hardware requirements; trusted reusable worker configurations provide them. Every execution activity routes to an authorized compatible worker with atomic enforceable resource reservations. Restricted enterprise data work stays within its approved identity and evidence boundary. See the [product specification](../specs/worker-capability-routing.md).

## Coordination architecture amendment, September13

Shared multiplayer reservations now follow the owner-selected
[Garden Git coordination protocol](../specs/git-coordination.md), with local
host/device enforcement and staged recovery between the two. There is no shared
coordinator service requirement. Existing source/review history stays intact; this
specification amendment does not claim that completed tasks already implement the
Git backend, resume held Phase10 work or change the separate storage deferral.

## Sequence and acceptance

Schema → trusted profiles → shared matching → atomic admission → activity propagation → restricted-data boundary. Routing explanations can follow matching; integrated acceptance follows all implementation. Reuse existing contracts and independently verify real limitations; synthetic GPU/data checks are not live-environment proof.

| Task | Outcome | Original prerequisites (preserved through the stack) |
| --- | --- | --- |
| [CG-645](tasks/CG-645-model-task-capability-requirements-and-resource.md) | Model task capability requirements and resource reservations | None |
| [CG-646](tasks/CG-646-define-trusted-worker-configurations-and-verifie.md) | Define trusted worker configurations and verified capability grants | CG-645 |
| [CG-647](tasks/CG-647-route-task-activities-through-one-capability-and.md) | Route task activities through one capability and capacity matcher | CG-645, CG-646 |
| [CG-648](tasks/CG-648-reserve-and-enforce-worker-cpu-memory-and-gpu-ca.md) | Reserve and enforce worker CPU memory and GPU capacity atomically | CG-647 |
| [CG-649](tasks/CG-649-preserve-capability-requirements-across-executio.md) | Preserve capability requirements across execution review and recovery | CG-648 |
| [CG-650](tasks/CG-650-bind-restricted-data-routing-to-workload-identit.md) | Bind restricted-data routing to workload identity and evidence policy | CG-646, CG-649 |
| [CG-651](tasks/CG-651-expose-task-requirements-worker-profiles-and-rou.md) | Expose task requirements worker profiles and routing explanations | CG-647 |
| [CG-652](tasks/CG-652-verify-capability-routing-across-heterogeneous-w.md) | Verify capability routing across heterogeneous workers and schedulers | CG-648, CG-649, CG-650, CG-651 |


## Deferred transcript storage

On September13 the owner moved [CG-506: Return complete worker transcripts for server-side storage and analysis](tasks/CG-506-return-complete-worker-transcripts-for-server-si.md) from Phase07 into this existing Phase11. This is a separately deferred work item alongside the eight capability-routing tasks above.

Preserve the owner storage-design hold: reconsider bounded controller storage versus external storage before resuming implementation. The existing PR and all review findings, including recovery between transcript finalization and durable run completion, remain attached to CG-506. Its placement does not approve implementation, provisioning, new storage spending, or activation. CG-506 is outside Phase07 closure scope.


## PR explanation reports

Owner added [CG-662: Explain to me PR reports](tasks/CG-662-explain-a-pull-request-with-an-html-architecture.md) to this phase. The feature generates a readable HTML explanation of a PR, its high-level structure, and annotated highlighted code. It is a new draft alongside the original capability-routing work; no shared coordinator or transcript-storage redesign is a prerequisite.


## Owner freeze, September13

Phase11 is frozen at the owner's explicit request. Priority UI tasks CG688 and CG689 moved to Phase10 after their already-running author work drained. All other Phase11 work remains subject to the freeze and its specific storage/planning/data holds. Earlier implementation approval above is historical for this freeze; do not treat it as a new execution or merge exception.

## Decisions

- **Should the Git migration and reversal defect be prioritized for correction before any multiplayer pilot, or should migration and reversal remain explicitly unsupported pending a later correction?** — answered: Prioritize the frozen corrective draft CG-695 before considering any multiplayer activation. Migration and standalone reversal are not supported for production use until the Git authority and unresolved-obligation corrections are verified. Keep Phase11 frozen and all proposed tasks unapproved; this prioritization does not authorize implementation, a pilot, runtime promotion, additional spending or an extension of the worker deadline. Phase10 remains closed with follow-ups. (by delegated operator (owner authority) at 2026-09-14T00:08:32+00:00)

## Phase10 retrospective additions — September13

These are reviewed planning drafts. Existing goals, freeze, completed outcomes and owner holds above remain in force.

# Task requirements, worker capability routing and dependable Git operation

This is an additive draft for existing Phase 11. Preserve its current frontmatter, including frozen: '2026-09-13', all existing goals, task outcomes, dependencies, exceptions and owner holds. This retrospective grants no implementation, merge, runtime promotion, production cutover, new workers, broader data access or spending authority.

Retain the capability-routing scope and recorded CG-645 through CG-652 outcomes: trusted worker configurations, common matching, atomic resource admission, activity propagation, restricted-data boundaries and useful routing explanations. Do not recreate completed tasks. Preserve the existing CG-506 storage decision, CG-402 evidence-policy hold, CG-642 evaluation-only disposition and other backlog proposals.

Add a focused Git reliability and usability track. First reconcile migration and standalone reversal with accepted Git authority, protect automatic local reads against unknown hosts, and bound Git transport with ambiguity-safe recovery. Then demonstrate the supported two-installation journey through normal migration, startup and scheduler entry points. Align the shipped specification and setup/recovery guide with those behaviors. Improve history validation incrementally while retaining audit and replay guarantees.

Preserve the delivered interaction contract: admitted OS-user binding without routine browser login, inherited accepted phase ownership with explicit overrides and unassignment, installation-bound execution authority, acknowledged active-work handoff, sidebar project selection and concurrency-only operating profiles. Keep substantive security and ownership regressions; do not restore invalid 303 expectations or reject accepted outcomes for cosmetic evidence changes.

Reuse CG-661 for substantive repeated-defect classification, CG-682 for unmapped acceptance evidence, CG-683 for readable sanitized required context and scoped diagnostic delivery, CG-659 for undelivered revision recovery, and CG-684 for policy-preserving retrospective publication. File no duplicate tasks for these findings. Verification guidance should name configured checks and acknowledge that no static typecheck command currently exists. Add closed-phase retrospectives as a distinct workflow improvement coordinated with CG-684.

Acceptance should show coherent Git migration/reversal, retained obligations under uncertainty, bounded transport recovery, protected private reads and an integrated two-installation lifecycle. Use proportionate focused evidence and ordinary independent review and CI. Keep legacy coordinator tests explicitly classified as compatibility coverage. Production multiplayer remains unactivated and requires a separate owner decision after the concrete migration and recovery findings receive disposition.

## Features for the next phase

- CG-695: Repair Git migration and standalone reversal
- CG-696: Validate hosts before automatic local authentication
- CG-697: Bound Git transport and recover ambiguous pushes
- CG-698: Verify the supported Git multiplayer journey
- CG-699: Publish coherent Git setup and recovery guidance
- CG-700: Reuse validated Git coordination history
- CG-701: Run retrospectives without reopening closed phases
