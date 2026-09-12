# Enterprise environment capabilities and configuration

## Purpose

This specification defines the capabilities and configuration boundaries for using
context-garden in an enterprise development environment. It uses generic contracts
for source control, managed workspaces, identity, execution and evidence. Deployment
configuration supplies the private details required by a particular installation.

The [product-level enterprise architecture](../../specs/enterprise-environment.md)
places these capabilities within the overall system design. Configuration examples
describe contracts; supported configuration must validate the selected capabilities.

## Scope

An enterprise deployment may combine private source control, large repositories,
managed development environments, restricted network paths, custom CI, centralized
identity, and organization-specific approval policies. These are optional deployment
characteristics; an installation should enable only the capabilities it needs.

The objective is to integrate with those systems while preserving task isolation,
review provenance, bounded execution, recoverability, and explicit authority for
merges and deployment. This specification does not authorize infrastructure
creation, access changes, spending, or production writes.

## 1. Integration configuration

Configuration should separate shareable project policy from private connection and
identity settings.

| Area | Configuration that may be necessary |
|---|---|
| Source control | Provider, web/API endpoints, repository identity, base branch, credential reference, required checks |
| Workspace | Product root, checkout strategy, reconciliation adapter, setup and per-run preparation |
| Execution | Local or remote runner, transport adapter, logical worker pool, readiness requirements |
| Resources | Global and per-host concurrency, CPU/memory/disk limits, heavy-check admission, absolute expiry |
| Identity | Workload identity provider, permitted scopes, credential lifetime, approved tool access |
| CI | Status adapter, exact-source identity, required jobs, log adapter, timeout and recovery policy |
| Governance | Review policy, branch ownership, protected paths, merge and deployment authority |
| Evidence | Storage destination, access control, retention, redaction, integrity and provenance |
| Notifications | Approved destination reference, event policy, delivery timeout and retry bounds |

Private endpoints, physical host identifiers, account identities, access-group
names and credential material belong in access-controlled local configuration or
a secret store. Committed examples should use synthetic values and logical aliases.
Diagnostic output should identify the effective policy and its origin without
printing sensitive values.

Configuration validation must reject unsupported settings and incompatible
combinations rather than silently falling back to a broader permission or a
less isolated execution mode.

## 2. Source-control integration

Support configurable hosted or self-managed source-control services, including
separate web and API endpoints. Repository discovery, API clients, CLI adapters,
login diagnostics and generated links must consistently target the configured
service rather than an ambient CLI default.

Requirements:

- Configure the repository and base branch independently for each product.
- Resolve credential references for the intended endpoint and operation.
- Support enterprise certificate authorities and network proxies without disabling
  certificate verification.
- Bind check and review evidence to the exact proposed source revision.
- Preserve atomic head guards and recheck conflicts immediately before a merge.
- Make automated merge eligibility an explicit project policy; support human-only
  approval and merge workflows where required.
- Allow organization-specific PR templates and protected paths.

Acceptance: disposable repositories and provider fakes demonstrate endpoint
selection, authentication failure, branch discovery, stale-head rejection and
correct link generation without contacting private infrastructure.

## 3. Managed worker lifecycle and transport

Support reusable or ephemeral workers behind a configurable lifecycle adapter.
Worker provisioning and other long operations must not block scheduler polling or
web requests. Each operation needs durable identity and resumable state.

A lifecycle should distinguish requested, provisioning, verifying, ready, busy,
draining, failed and retired states. Readiness requires the intended checkout,
runtime, tools, permissions and resource capacity. Probes must be bounded and
read-only; formatting or other source-mutating checks are unsuitable as probes.

Requirements:

- Prefer a compatible, reconciled, ready worker before creating another.
- Enforce pool size, spending authorization and absolute expiry independently of
  retries, reconnects and controller restarts.
- Treat provisioning and readiness failures as environment failures without
  consuming an author implementation attempt.
- Support controller-originated communication where worker-to-worker connections
  are unavailable; do not require unrestricted inbound network access.
- Allow direct transports or managed-access adapters with explicit argv, stdin,
  stdout, exit-code, timeout and cancellation contracts.
- Identify workers by logical aliases in shareable records. Resolve physical
  connection information only at the execution boundary.
- Drain active work safely and preserve its source and results before release.

Acceptance: offline lifecycle and transport exercises cover interrupted
provisioning, duplicate requests, failed readiness, safe reuse, resource exhaustion,
expiry and cleanup. Live cloud exercises are optional and require separate authority.

## 4. Repository and workspace strategies

Some repositories support independent worktrees; others require a canonical
checkout or a managed filesystem. Make the strategy a per-product capability,
with an explicit compatibility check for the build system.

For a canonical-checkout strategy:

- Acquire exclusive ownership of the actual checkout, including protection against
  concurrent runs using different aliases for the same workspace.
- Refuse conflicting unrelated edits and preserve them for reconciliation.
- Verify repository, branch and source identity before execution and publication.
- Support a bounded per-run reconciliation adapter when required by the filesystem.
- Scope setup-cache validity to the lifetime and identity of the prepared workspace;
  recreating a checkout must invalidate environment preparation associated with it.
- Keep scheduler state, approval records, credentials and unrelated products outside
  the worker's writable boundary.
- Recover interrupted work without discarding the previous attempt's implementation.

A configuration flag must not silently weaken isolation. If the requested strategy
cannot satisfy the execution boundary, fail with an actionable configuration error.

Acceptance: disposable checkouts cover dirty-workspace refusal, concurrent admission,
workspace recreation, branch changes, interrupted recovery and attempted writes
outside the authorized subtree.

## 5. External CI and check evidence

A CI status adapter should describe the state of applicable checks for a requested
repository and source revision. Normalize provider states while retaining the
original result and a private evidence reference when appropriate.

The contract should include:

- Requested source revision and actual tested revision or merge-tree identity.
- Required job identities, run/attempt identities and completion states.
- Whether evidence exists for the requested source and whether it is stale.
- Failure classification and access-controlled diagnostic references.

Missing, stale, unknown or incomplete evidence must not count as passing. A passing
result for an earlier revision must not authorize the current revision. Preserve
the distinction between testing a PR head and testing a synthetic merge tree.

Separate status retrieval from failure-log analysis. Diagnose infrastructure failures
before bounded recovery; route implementation failures with exact-source feedback.
Retain original failed results when a later attempt passes.

Acceptance: fake-provider tests cover changed heads, out-of-order results, partial
job completion, inaccessible logs, interrupted checks and mixed pass/fail outcomes.

## 6. Resource admission and execution recovery

Admission must account for the execution host as well as controller-wide limits.
A simple worker count may be insufficient for memory-intensive builds or shared
workspace checks.

Requirements:

- Apply configurable CPU, memory, disk and concurrency constraints per host or pool.
- Coordinate heavy-check admission across processes sharing the constrained resource.
- Reserve and release capacity safely across crashes and reconnects.
- Persist active-claim handoffs and attempt identity for both model work and checks.
- Fence stale generations and stop surviving subprocesses when execution authority
  becomes terminal or an absolute deadline expires.
- Preserve partial output and classified failures without replaying accepted work.

Use capability checks and supported alternatives for platform-specific enforcement.
Support Linux, macOS and Windows through WSL; report any untested platform explicitly.

Acceptance: deterministic and disposable process exercises cover saturation,
restart during execution, expired authority, descendant termination and durable
result collection without duplicate execution.

## 7. Branch, review and approval ownership

Each branch must have one declared owner for restacking, rebasing and publication.
When an external tool owns these operations, context-garden must not race it with
independent branch rewrites. Verify delivered content and provenance rather than
assuming that a merged PR necessarily contains the intended change.

Review integrations should:

- Allowlist trusted automated reviewers by configured identity.
- Distinguish substantive findings from status notices and advisory suggestions.
- Include applicable unresolved feedback from older revisions and discussion bodies
  in the worker's brief, preserving its source and resolution state.
- Avoid author revisions driven only by cosmetic preferences or redundant review counts.
- Retain genuine defects, explicit rejection and failed applicable checks as blockers.
- Keep review attestations separate from immutable original verdicts.

Merge, deployment and phase-closure authority should be independently configurable
and auditable. Credentials or a successful check do not themselves grant approval.

## 8. Identity, tools and execution boundaries

Workers may need approved CLIs, private package registries, tool servers or repository
access. Pass only the specific configuration and authority required for the task.

Requirements:

- Prefer scoped workload identities and short-lived credentials where supported.
- Keep human identity and automation identity distinguishable in audit records.
- Allowlist environment variables and selected configuration files rather than
  copying an entire user profile into a worker environment.
- Apply explicit network and filesystem boundaries to tool execution.
- Protect operator controls from worker credentials and worker-accessible networks.
- Fail closed when credentials, membership or sandbox capabilities are insufficient.
- Treat untrusted tool output and generated artifacts as data, not new authority.
- Prevent active document formats from executing with operator privileges when
  previewed; apply appropriate sandboxing and response headers.

Acceptance: offline permission and boundary tests demonstrate denied out-of-scope
operations, credential isolation, safe previews and actionable configuration errors.
Changes to access policy follow the deployment's normal approval process.

## 9. Confidentiality and artifact handling

Prompts, task logs, reports, notifications, examples and exported evidence should
contain only information approved for their destination and audience.

Requirements:

- Use synthetic or approved sanitized evaluation data.
- Keep private infrastructure names, internal URLs, access-group names, incident
  identifiers and operational command details out of shareable specifications.
- Resolve sensitive connection details from private configuration at runtime.
- Redact credentials and sensitive payloads before persistence and transmission,
  including streamed output crossing chunk boundaries.
- Apply access control, retention and deletion policies to run artifacts and logs.
- Preserve durable attempt-scoped transcripts and acknowledged offsets across
  restarts, with authorized retrieval of superseded partial attempts.
- Check generated and committed artifacts for prohibited information according to
  project policy, including indirect disclosure through links and filenames.

Acceptance: synthetic fixtures verify configuration separation, redaction, access
control and export filtering. Repository history and previously distributed copies
require a separately scoped review when historical removal is necessary.

## 10. Notifications and operational visibility

Notification adapters should use approved destination references, bounded delivery
and safe structured argument handling. Worker-authored text must not be interpolated
into executable shell commands. Avoid sending raw diagnostic output or private
identifiers to notification channels.

The operator view should distinguish queued work, active execution, environment
holds, review findings and intentional deferrals. Surface meaningful failures and
required actions without repeated notifications for unchanged conditions. A failed
notification must remain visible without corrupting task state.

Cost and progress views should state their cohort, time window, source and completeness.
Unknown pricing must remain unknown rather than silently becoming zero. Preserve
measured results when targets are missed, along with any explicit acceptance decision.

## 11. Evidence, completion and adoption

Define evidence storage and retention before deployment. Reviews need stable source,
run, check and artifact identities; access-controlled external storage may satisfy
this requirement without committing sensitive execution logs to a context repository.

Distinguish implementation completion, review approval, merge, deployment and
verification at the deployed boundary. A merged change must not automatically be
reported as deployed or verified. Phase closure must record its actual review verdict,
blocking-finding dispositions and acceptance decision.

Live canaries are optional for acceptance, review, merge, release and phase closure.
Their absence alone is not a blocker. Correctness, security, recovery, deadline and
resource requirements still need proportionate validation.
