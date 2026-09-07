# Pluggable remote host provisioning, starting with EC2

Status: active phase-05 implementation, explicitly promoted by Josh on 2026-09-07. Spec retained at this stable path to preserve reading links. CG216 and CG345–348 are now phase05 tasks. Preserve the bounded plan/enable boundary for live provisioning and all validation requirements.

## Outcome

An operator can declare an AWS worker pool, preview its resources and estimated cost, enable it, and let the garden provision capacity, execute work, recover interrupted runs and retire idle instances without manually configuring each host. The laptop remains responsive and the operator can explain where each run executes and what the pool costs.

Start with one on-demand Ubuntu x86-64 worker with 4 vCPUs, 16 GiB RAM and disk-backed temporary storage. These are initial sizing suggestions, not fixed product requirements. Increase concurrency only after measuring aggregate worker, review, check and setup memory. Then add Spot with interruption recovery. The scheduler remains on a durable host outside the disposable pool.

## Relationship to existing work

CG-216 owns the portable claim/lease/result/transcript protocol. Use that protocol for managed EC2 workers, including checks and reviews; do not introduce an AWS-specific execution protocol. Existing SSH support remains useful for a manual experiment, but is not proof that replaceable EC2 workers recover correctly. CG-338 owns admission across all execution paths. Integrate it rather than counting only writer processes. Model-provider routing and quotas remain separate concerns from machine capacity.

## Reusable host lifecycle and adapters

Owner clarification, 2026-09-06: the same model must support provisioning remote development hosts at work, not only garden workers. EC2 is the first infrastructure provider, and garden execution is the first workload integration. Keep the shared lifecycle independently usable without a garden scheduler, task IDs, model credentials or worker protocol.

Separate three responsibilities with versioned, documented contracts:

- Infrastructure provider: plan, provision, discover/reconcile, inspect, stop/start where supported, and destroy hosts and attached resources. Advertise capabilities such as Spot, persistent disks and stop/start rather than pretending all providers implement them. EC2 owns AWS-specific IAM, image, subnet, instance and pricing details. Support another implementation without editing the shared lifecycle or garden scheduler.
- Environment profile: declare image/bootstrap, CPU/memory/disk needs, secret references, health checks and connection information. A garden-worker profile installs and enrolls the portable worker. A remote-dev profile installs the chosen development tools and repositories and exposes approved SSH/editor connection details; it does not require a garden worker daemon or model account.
- Consumer integration: garden reconciles queue demand into worker capacity and attaches task/result metadata; an independent CLI/API lets a person or a work platform request, inspect, connect to, suspend/resume and release a development host. The shared layer reports host facts and lifecycle events, not task decisions. Give policy and credential resolvers replaceable interfaces so a workplace can use its account boundaries, images, network rules, SSO and secret store without embedding company-specific behavior in the core.

Use stable host IDs, owner/purpose labels and an extensible provider reference for durable reconciliation. Keep the core declarative schema portable while validating namespaced provider options explicitly; reject unsupported requested capabilities before provisioning. A small local fake provider and contract tests establish the extension seam; do not build another paid-cloud backend just to demonstrate abstraction.

Remote development differs from disposable workers: default to on-demand hosts and persistent workspaces, detect active sessions before idle shutdown, distinguish stopping compute from deleting disks, and require an explicit destructive release choice to remove unsaved workspace storage. Explain storage costs while stopped. Spot development hosts are opt-in only with verified workspace recovery. Connection/authentication policy belongs to the workplace integration; normal garden workers still need only outbound HTTPS. Never infer a public SSH rule from selecting the dev profile.

Acceptance must demonstrate two consumers of the same lifecycle: one garden worker and one standalone dev host created without importing or booting garden scheduling. Document a minimal custom provider/profile example, contract compatibility/versioning, and how a work deployment injects its policies and credentials. A disposable fixture project proves the example works; a real workplace integration requires its own named environment and acceptance, never implied by this prototype.

## Pool declaration and lifecycle

Configuration describes AWS account/region, allowed instance types and zones, purchase policy (on-demand first; Spot optional), minimum/maximum instances, per-host concurrency/resource reserve, idle timeout, maximum instance age, disk allocation, network placement, worker image/version, credential references, and spend limits. Default minimum capacity is zero, maximum is one, and paid on-demand fallback from Spot is disabled unless explicitly configured.

Provide a reviewable plan with estimated compute, storage, IPv4 and transfer assumptions before enabling a pool. Do not provision merely by loading a configuration or viewing status. Reconcile desired capacity against provider state using stable ownership tags and idempotent operation identifiers. A scheduler restart, duplicate request or delayed AWS response must not create duplicate instances. States distinguish provisioning, bootstrapping, ready, busy, draining, interrupted, failed and terminated. Retry transient provider failures with bounded backoff; explain exhausted capacity instead of looping indefinitely.

Bootstrap a pinned worker version and product environment on a supported image. The worker initiates an authenticated outbound connection to a reachable HTTPS garden endpoint; no public SSH is needed for normal operation. Validate endpoint reachability and registration before making capacity schedulable. Use instance roles for AWS access, scoped worker enrollment and narrowly scoped repository/model credentials retrieved at runtime. Secrets must not appear in user-data, AMIs, tags, claim payloads, logs or snapshots. Isolate provider-management credentials from task processes and prevent task code from obtaining the controller role through instance metadata. Pin image/tool versions and report them with runs.

## Execution and resource boundaries

Apply host-level memory/CPU limits and admission to setup, writers, reviewers, checks, base probes and cleanup helpers together. Temporary test files live on EBS-backed storage by default. Report actual process groups, memory and disk headroom; requested slots are not evidence of actual concurrency. Results, transcript and branch changes must reach durable storage through the worker protocol before a run is accepted. Cross-host tests must prove no dependence on the scheduler filesystem or local harness credentials.

## Spot and recovery

Use interruption notices and rebalance recommendations when available to stop claiming new runs, drain or checkpoint current work, upload available transcript and preserve recoverable edits. Notices are an optimization: abrupt loss with no notice must also recover through lease expiry and replacement. Fence stale workers from publishing accepted results or mutating the canonical task branch after reassignment; recover through attempt-specific artifacts and validated promotion as appropriate to CG-216.

Recovery may retry execution, but must not double-accept results, double-merge, or count the same usage twice. Record repeated model cost and lost work separately from instance savings. Preserve unfinished work according to an explicit retention policy; test retrieving it after the originating instance and root disk are gone. Failed tests caused by host interruption are environment failures, not findings against product code. Spot shortage must respect maximum capacity/spend and the configured fallback policy.

## Cost, teardown and operator experience

Estimate costs using current regional rates and an explicit runtime assumption; do not bake today's Spot price into configuration. Separate estimated accrued cost from delayed provider billing, and machine cost from model spend. Capacity/runtime limits provide prompt controls; AWS billing alerts alone are not a hard spending bound. At a threshold, stop new launches and drain according to policy; disclose unavoidable pending charges and limits of any guarantee.

Show pool health, ready/busy capacity, executing tasks, resource pressure, interruption history, pending recovery and estimated spend. Human cards ask about an actual tradeoff (for example an explicitly priced on-demand fallback), not routine lease transitions. Pool disable drains without losing active work; emergency stop is separately named. Cleanup reconciles owned instances, EBS volumes, IPs and other created resources after normal shutdown, bootstrap failure and controller restart. Never delete unrelated resources or silently destroy retained recovery artifacts. Report retained resources and their continuing costs.

## Delivery and evidence

1. Provider/profile contracts and independently usable host lifecycle, with EC2 as the first adapter and one on-demand instance.
2. End-to-end execution through CG-216 with aggregate admission and durable recovery artifacts.
3. Spot replacement and abrupt-loss exercises, with fencing and bounded fallback.
4. Operator controls, cost attribution, teardown, a standalone remote-dev consumer and independently repeatable acceptance runs for both uses.

Use provider fakes for deterministic lifecycle/error coverage, then a separately enabled, budgeted AWS canary. Evidence includes one work-to-review/check-to-result cycle on an independent host, intentional interruption during work and check, controller restart mid-provision, unavailable Spot capacity, and teardown inventory showing no unexplained billed resources. Record actual cost, retry/model cost, elapsed time and peak memory. A simulated AWS API proves simulation behavior only. Missing live evidence is UNPROVEN. Feature completion does not itself pass phase-05 stabilization or unfreeze phase 06.

## References

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html
- https://aws.amazon.com/ec2/spot/pricing/

## Tracking

- CG-345: Provision and retire an EC2 worker pool from a bounded declarative configuration
- CG-346: Run work reviews and checks on managed EC2 hosts with shared resource admission
- CG-347: Recover EC2 Spot interruptions without losing accepted work or exceeding pool limits
- CG-348: Make EC2 pool cost health draining and teardown understandable and verifiable
