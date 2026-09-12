---
plant: quince
latin: Cydonia oblonga
plate: VII
---

# Support enterprise dev environment

## Owner scope update, 2026-09-10

Spot worker support is back in Phase 07: CG-347 covers purchase policy, interruption recovery and replacement; CG-348 covers dependent pool controls and acceptance. Both return from Phase 08 under normal scheduling and existing dependencies. Other Phase 08 work remains frozen. Existing fleet spending limits and deadlines remain in force.

## Intent

Run the garden against enterprise source control, external CI and explicitly provisioned canonical remote checkouts while retaining human authority, narrow credentials and independently verifiable evidence. Phase 07 is unfrozen. Owner approved implementation tasks, then paused evidence gathering: CG-402, CG-403, CG-407 and CG-408 are held as drafts until explicitly released. Other tasks follow their dependency graph and normal resource/review gates; phase-06 holds remain unchanged.

## Outcomes

1. A manual-run pilot demonstrates explicit server routing, exact-head CI, actionable bot feedback and human approval/merge gates.
2. The shared host lifecycle supports command-backed acquisition, real readiness, warm reuse and remote resource admission.
3. An opt-in canonical checkout mode preserves unrelated edits and controller isolation through interruption and recovery.
4. Approved tooling and evidence policies prevent credential/host-identity leaks and distinguish merged from deployed/verified work.

## Completion evidence

Every acceptance task must pass on its reviewed build. The final exercise covers happy paths and recovery, and labels fixtures separately from independently verified environment evidence. Any required policy decision remains explicit until accepted by the designated people/personas. No production deployment or additional cloud spending is authorized by this plan.

## Sequence

Foundations and policy → manual pilot; host adapter/admission and tooling → integrated acceptance. CG-406 proceeds independently on existing local/SSH transports; a manual pilot is not its prerequisite. In-place mode permits only one active task per machine, including its checks and reviews, until checkout ownership is safely released. Reuse CG-216/345/346 and existing configuration rather than rebuilding them.

## Feature inventory

| Task | Feature |
| --- | --- |
| [CG-395](tasks/CG-395-support-explicit-github-enterprise-hosts-across.md) | Support explicit GitHub Enterprise hosts across all repository operations |
| [CG-396](tasks/CG-396-use-pluggable-exact-head-ci-status-for-review-an.md) | Use pluggable exact-head CI status for review and merge eligibility |
| [CG-397](tasks/CG-397-respect-external-branch-stack-ownership-and-conf.md) | Respect external branch-stack ownership and configurable protected paths |
| [CG-398](tasks/CG-398-validate-a-human-gated-enterprise-profile-with-b.md) | Validate a human-gated enterprise profile with bot feedback and private notifications |
| [CG-399](tasks/CG-399-keep-physical-host-identities-out-of-committed-c.md) | Keep physical host identities out of committed context and public evidence |
| [CG-400](tasks/CG-400-define-the-least-privilege-worker-identity-and-i.md) | Define the least-privilege worker identity and internal tooling policy |
| [CG-401](tasks/CG-401-pass-approved-tool-configuration-into-scrubbed-l.md) | Pass approved tool configuration into scrubbed local and remote workers |
| [CG-402](tasks/CG-402-decide-and-implement-a-portable-immutable-evalua.md) | Export immutable run evaluation evidence into context under an approved policy |
| [CG-403](tasks/CG-403-validate-a-manual-run-enterprise-pr-and-exact-he.md) | Validate a manual-run enterprise PR and exact-head CI journey |
| [CG-404](tasks/CG-404-add-command-backed-host-acquisition-readiness-an.md) | Add command-backed host acquisition readiness and warm reuse to the shared lifecycle |
| [CG-405](tasks/CG-405-apply-host-local-resource-admission-and-capabili.md) | Apply host-local resource admission and capability routing to command-backed hosts |
| [CG-406](tasks/CG-406-support-fenced-in-place-canonical-checkouts-with.md) | Support fenced in-place canonical checkouts with safe per-run reconciliation |
| [CG-407](tasks/CG-407-require-content-and-deployment-verification-befo.md) | Require content and deployment verification before describing a change as shipped |
| [CG-408](tasks/CG-408-demonstrate-the-constrained-remote-environment-w.md) | Demonstrate the constrained remote environment with recovery and human gates |
| [CG-409](tasks/CG-409-finish-manual-work-pushed-from-another-machine-w.md) | Finish manual work pushed from another machine without a local authoring checkout |
| [CG-410](tasks/CG-410-show-eligible-manual-work-in-inbox-with-a-safe-t.md) | Show eligible manual work in Inbox with a safe take action |
| [CG-411](tasks/CG-411-adopt-an-existing-pr-with-its-verified-branch-an.md) | Adopt an existing PR with its verified branch and revision identity |
| [CG-412](tasks/CG-412-resolve-check-commands-analyzers-and-timeouts-pe.md) | Resolve check commands analyzers and timeouts per product |
| [CG-413](tasks/CG-413-use-product-specific-execution-timeouts-and-weig.md) | Use product-specific execution timeouts and weighted resource admission |
| [CG-414](tasks/CG-414-assign-owners-to-tasks-and-phases-and-filter-wor.md) | Assign owners to tasks and phases and filter work by owner |
| [CG-415](tasks/CG-415-register-private-runner-adapters-through-trusted.md) | Register private runner adapters through trusted configuration |
| [CG-416](tasks/CG-416-aggregate-brief-size-and-startup-context-regress.md) | Aggregate brief size and startup-context regressions in metrics |

## Publication boundary

Use generic capability descriptions and synthetic examples throughout phase goals, tasks, briefs, PRs and exported evidence. Do not include customer or employer names, private connection details, internal commands or physical host identifiers. The local source survey remains ignored and is not included in reading manifests.

## Specification

[Enterprise remote environments](specs/enterprise-remote-environments.md).
