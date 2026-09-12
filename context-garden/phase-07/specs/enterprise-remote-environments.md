# Support enterprise dev environment

Status: proposed phase-07 plan, 2026-09-07. This generic extraction is safe to review independently of the private environment survey. The survey is local-only, is not a worker input, and its environment observations require re-verification before use. Public implementation must use generic adapters and synthetic examples.

## Basis and boundaries

The survey describes a controller-originated remote execution model, enterprise repository hosting, external CI, canonical checkout constraints, ephemeral hosts, narrow tool access and mandatory human gates. Its gap labels G1–G10 are retained only for traceability. Spot checks of product source at b72dbcc and existing tasks confirmed the hardcoded GitHub API default, SSH worktree preparation and rollup-based polling; this is not a complete current-source audit. CG-345/346 remain in progress, so their interfaces must be reconciled before dependent work starts. Proposed configuration names in the survey are design suggestions, not implemented APIs.

## Existing capabilities to reuse

Markdown briefs, independent reviews, per-product setup, manual/SSH execution, human-gated merge configuration, trusted bots, notification commands, ignored local overlays and cost accounting already exist. CG-216 supplies portable execution; CG-345 the generic lifecycle/provider contract; CG-346 remote execution/admission; CG-347/348 cover EC2 recovery and lifecycle visibility. Phase 07 adds the command-backed adapter and constrained-checkout integration. CG-349/350 remain the owners of generic config metadata, locks and web editing; new settings should integrate with that metadata when available without blocking backend support.

## Requirements and task map

| Source area | Task | Deliverable |
| --- | --- | --- |
| G1 | CG-395 | Support explicit GitHub Enterprise hosts across all repository operations |
| G4 | CG-396 | Use pluggable exact-head CI status for review and merge eligibility |
| G6 | CG-397 | Respect external branch-stack ownership and configurable protected paths |
| G7, G9 and existing configuration | CG-398 | Validate a human-gated enterprise profile with bot feedback and private notifications |
| G10 | CG-399 | Keep physical host identities out of committed context and public evidence |
| G8 policy prerequisite | CG-400 | Define the least-privilege worker identity and internal tooling policy |
| G8 | CG-401 | Pass approved tool configuration into scrubbed local and remote workers |
| Evidence policy gap | CG-402 | Decide and implement a portable immutable evaluation checkpoint contract |
| Manual adoption milestone | CG-403 | Validate a manual-run enterprise PR and exact-head CI journey |
| G2 delta over phase-05 lifecycle | CG-404 | Add command-backed host acquisition readiness and warm reuse to the shared lifecycle |
| G5 delta over phase-05 admission | CG-405 | Apply host-local resource admission and capability routing to command-backed hosts |
| G3 highest-risk change | CG-406 | Support fenced in-place canonical checkouts with safe per-run reconciliation |
| Post-merge policy gap | CG-407 | Require content and deployment verification before describing a change as shipped |
| Phase acceptance | CG-408 | Demonstrate the constrained remote environment with recovery and human gates |

## Milestones and safeguards

Owner scheduling update: CG-406 is approved independently of the manual milestone, with a phase freeze exception. It targets existing local/SSH runners and enforces one active task per machine in in-place mode. All other phase-07 tasks remain draft. Host readiness must be non-mutating and separate from code validation. Environment failures do not consume implementation attempts. Checkout exclusivity and branch/path fencing apply to every execution mode. Status providers must prove freshness for the exact SHA. External stack ownership prohibits competing automatic branch rewrites.

Security/Privacy and Quality decisions are real prerequisites: define identity/tool reach and durable evaluation storage before widening access or declaring policy satisfied. Use synthetic or explicitly sanitized data. Preserve human review, merge and deployment authorization. Internal adapters and concrete connection details stay outside public source and committed context.

## Beyond the ten gaps

The plan explicitly includes the two policy gaps: immutable evaluation evidence and post-merge content/deployment verification. Start post-merge support with linked verification tasks. Avoid conflating a merged PR, a live process, a readiness probe or a fixture pass with shipped and verified behavior.


## Additional capability gaps (F1–F9)

Owner review identified prerequisites omitted from the initial manual milestone and multi-product operation. Source locations are observations to recheck, not API guarantees.

| Gap | Task | Outcome |
| --- | --- | --- |
| F1 | CG-409 | Finish manual work pushed from another machine without a local authoring checkout |
| F2 | CG-410 | Show eligible manual work in Inbox with a safe take action |
| F3 | CG-411 | Adopt an existing PR with its verified branch and revision identity |
| F4 | CG-412 | Resolve check commands analyzers and timeouts per product |
| F5 | CG-413 | Use product-specific execution timeouts and weighted resource admission |
| F6 | CG-414 | Assign owners to tasks and phases and filter work by owner |
| F7 | CG-402 | Export immutable run evaluation evidence into context under an approved policy |
| F8 | CG-415 | Register private runner adapters through trusted configuration |
| F9 | CG-416 | Aggregate brief size and startup-context regressions in metrics |

F1–F3 block the manual milestone CG-403. F4–F6 cover independent products and people; F8 permits private adapter packaging; F9 makes startup context growth visible. F7 expands CG-402 rather than duplicating it. Existing CG-362 covers related external-completion verification, CG-381 Inbox ownership, and CG-012/066/149 brief measurements: preserve their work and add only missing behavior.
