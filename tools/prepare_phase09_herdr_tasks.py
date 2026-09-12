"""Prepare/import the owner-requested Herdr phase through native Garden APIs.

Defaults to validation only. --apply creates drafts under the scheduler tick lock.
This is a planning utility, not a runtime installer or deployment command.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


SPEC = "context-garden/phase-09/specs/herdr-execution.md"
ARCH = "context-garden/specs/execution-runtimes.md"
EVIDENCE = "context-garden/phase-09/docs/concept-and-evidence.md"


def item(key, title, goal, scope, criteria, deps=(), reading=(), difficulty="hard", priority=2):
    return {
        "title": title,
        "difficulty": difficulty,
        "priority": priority,
        "depends_on": [{"id": d, "after": "merge"} for d in deps],
        "reading": [SPEC, *reading],
        "body": "\n\n".join([
            "## Goal\n\n" + goal,
            "## Context\n\nOwner-requested Phase 09: Garden orchestrates and Herdr executes. "
            "Follow the product execution contract and the phase specification. "
            "This task changes the context-garden product repository; do not edit the live driving Garden.",
            "## Scope\n\n" + scope,
            "## Acceptance criteria\n\n" + "\n".join("- [ ] " + c for c in criteria),
            "## Verification\n\nUse proportionate focused checks for the changed ownership boundary. "
            "Use fake harnesses and disposable local runtimes where actual protocol behavior matters; "
            "paid model/cloud canaries are optional. Preserve actual failures and report environments tested. "
            "Do not change active fleet allocation, limits, expiry, deployment or unrelated phase holds.",
            "owner_request_key: herdr-execution-phase-20260910\nherdr_phase_task_key: " + key,
        ]) + "\n",
    }


TITLES = {
    "probe": "Prove the pinned Herdr execution contract with a disposable fake job",
    "lifecycle": "Add runtime-aware execution identity and lifecycle hooks to Garden runners",
    "client": "Add a bounded Herdr client with validated runtime configuration and health checks",
    "envelope": "Enforce Garden isolation and resource limits around Herdr-launched jobs",
    "local": "Run local Garden attempts in owned Herdr terminals",
    "recovery": "Reconcile and cancel Herdr attempts without duplicate execution",
    "results": "Collect durable Herdr run results and source through Garden acceptance paths",
    "modes": "Route auxiliary model work and owned checks through the execution runtime contract",
    "remote": "Compose Herdr execution with existing remote worker claims and result delivery",
    "human": "Preserve Garden question and intervention ownership for Herdr runs",
    "views": "Show Herdr execution state and recovery diagnostics across Garden views",
    "cost": "Attribute Herdr run usage and runtime overhead without duplicate charges",
    "ops": "Support safe Herdr adoption draining retention and rollback",
    "accept": "Verify Herdr execution conformance and publish the integration readiness account",
}


TASKS = [
    item("probe", TITLES["probe"],
         "Establish a tested Herdr release/API baseline and a minimal non-model execution proof before the adapter depends on upstream behavior.",
         "Inspect v0.9.0 / b99002ac99b09e00b4ca692436cb15a6b0d676f1 first. Use a disposable private server and fake command. "
         "Deliver a small reusable fixture/probe plus docs/herdr-compatibility.md in the product. This is a bounded compatibility experiment, not an upstream fork or production rollout.",
         [
             "Record the tested binary source/version and schema capabilities for workspace.create, layout.apply direct argv, session.snapshot, event subscription, pane identity and close; separate current website claims from the tested release.",
             "Demonstrate exact argv/cwd/env input and raw stdout/stderr/exit capture for a fake process, including spaces, Unicode and shell metacharacters; inspect initial workspace shell startup and replacement-tab behavior.",
             "Show client detach versus full server restart behavior and determine how restored/moved/reused panes can be distinguished from the original execution owner. Do not treat done/idle or pane.exited as an exit result.",
             "Prototype a durable generation start guard that suppresses repeated launch delivery; demonstrate lost-response reconciliation or record the exact unsupported identity gap that blocks launch.",
             "Assess Herdr control-socket exposure, inherited daemon environment and automatic native session restore. Document a viable isolation boundary and exact follow-up requirements for the envelope task.",
         ], reading=(ARCH, EVIDENCE, "src/garden/runner/base.py"), priority=1),
    item("lifecycle", TITLES["lifecycle"],
         "Let Garden observe, stop and reconcile an execution without assuming the runner's launcher PID is the worker.",
         "Extend the existing runner contract only where necessary. Introduce backward-compatible persisted execution bindings; retain existing task statuses and shared RunStore mutation coordination. Herdr transport belongs to the client task.",
         [
             "Record runtime, logical endpoint, attempt generation, launch fingerprint, remote claim relationship and validated external locators separately from task ID and harness session ID; old Run records load without invented history.",
             "Add explicit semantic hooks for observing, cancelling and reconciling backend executions, with safe defaults preserving local/SSH/manual/remote behavior and trusted adapter registration.",
             "Audit process_finished/no_process/stop/reap and startup resource accounting so absent local PID, expired client process or restored terminal cannot imply completion or release an unresolved owner.",
             "Persist updates through the accepted cross-process mutation boundary and recheck generations after external work; do not hold the tick lock during runtime waits.",
             "Focused fake-adapter regressions cover old records, launch pending, unknown execution, actual completion and cancellation without changing model selection or task acceptance.",
         ], deps=(TITLES["probe"], "CG-584"), reading=("src/garden/runner/base.py", "src/garden/runs.py", "src/garden/scheduler/reap.py")),
    item("client", TITLES["client"],
         "Provide one bounded, typed Herdr protocol client and explicit configuration that cannot retarget a run silently.",
         "Use the prototype's pinned operation set and schema. Prefer direct socket layout.apply for argument-vector launch; CLI JSON is a diagnostic surface. Reuse shared configuration metadata and the accepted adapter registry.",
         [
             "Validate supported runtime scope, logical endpoint/session, protected state path, version/capability policy, timeout/backoff and retention settings. Existing execution remains the default and the effective selection is recorded per run.",
             "Implement bounded structured requests/responses, schema/error handling and sanitized diagnostics for create/layout/snapshot/pane lookup/process-info/observe/close operations. Support pane.send_keys only if the tested soft-interrupt path uses it; Garden's verified wrapper control channel owns process cancellation. Task text cannot choose an executable client, endpoint or adapter.",
             "Treat RPC IDs as correlation only. Mark uncertain mutations explicitly and return them for reconciliation rather than retrying workspace creation or launch blindly.",
             "For live events, subscribe/ack before snapshot, buffer appropriately and resnapshot after disconnect; missed events never become durable completion claims.",
             "Read-only health checks distinguish missing binary, incompatibility, unavailable endpoint and permission failure. They never install/update/stop a server, run an authentication dialog or submit model work.",
         ], deps=(TITLES["probe"], "CG-415"), reading=("src/garden/config.py", "src/garden/runner/__init__.py", "src/garden/runner/base.py")),
    item("envelope", TITLES["envelope"],
         "Make every Herdr-launched job obey Garden's identity, sandbox, storage, resource and deadline policy before untrusted code executes.",
         "Reuse accepted scoped-identity, sandbox and supervision code; compose with CG-528 after its actual merge. Implement the trusted wrapper and durable start guard. Result ingestion belongs to the results task.",
         [
             "Enforce admission and the shared storage reserve before private HOME, setup, input staging or Herdr terminal creation; account for preparation and runtime overhead under existing caps.",
             "Launch through a trusted argument vector with a minimal safe daemon/shell environment. Resolve only scoped secrets; prevent inherited profiles/hooks/plugins from running with operator credentials before sandbox entry.",
             "Prevent the model/setup/check child from using the Herdr control socket or another attempt's completion channel with an actual OS/sandbox boundary or narrow broker. Prove that hiding an environment variable is not the only protection.",
             "Apply existing filesystem/network restrictions, resource/validation leases and absolute deadlines to actual runtime-created descendants, including nested checks; controller disconnection cannot disable enforcement. Expose a protected generation-bound wrapper/supervisor control channel for cancellation and child-identity queries; a runtime close event alone cannot confirm descendant termination.",
             "Atomically claim the execution generation before child launch, retain honest uncertain-start state, and write durable raw streams and an atomic terminal receipt after output persistence. Correctly capture replaced final files and real signals/nonzero exits.",
             "Focused adversarial fake jobs verify cross-run/socket denial, credential containment, hostile arguments, duplicate submission suppression and descendant cleanup; report any unsupported host capability before execution.",
         ], deps=(TITLES["probe"], "CG-516", "CG-518", "CG-528"), reading=("src/garden/runner/base.py", "src/garden/run_supervisor.py", "src/garden/validation.py")),
    item("local", TITLES["local"],
         "Execute an admitted local Garden attempt inside Herdr while preserving its existing harness and worktree contract.",
         "Integrate the client, lifecycle and execution envelope through the trusted runner registry. One owned pane per attempt initially; Garden creates and owns the worktree. Do not add a second task scheduler.",
         [
             "For selected local work/revise/resume, record the binding before side effects, create the owned runtime context at the existing worktree and use layout.apply to launch the trusted wrapper directly.",
             "Pass the exact selected mode, harness, model, difficulty, session, source and brief through existing harness APIs. Task text and secrets are file/stdin inputs, not shell interpolation or interactive prompt pastes.",
             "Capture returned runtime IDs without predicting them; verify wrapper ownership before reporting running. CLI request exit and agent idle/done are not completion.",
             "A duplicate or ambiguous launch is handed to reconciliation, never silently rerun or moved to another backend. Existing local execution and manual workflows remain available when unselected.",
             "A disposable fake-harness attempt demonstrates launch, separate raw outputs and terminal receipt with the actual pinned runtime; verify that the initial/replacement terminal creates no unaccounted job.",
         ], deps=(TITLES["lifecycle"], TITLES["client"], TITLES["envelope"]), reading=("src/garden/runner/local.py", "src/garden/harness.py", "src/garden/scheduler/dispatch.py")),
    item("recovery", TITLES["recovery"],
         "Reconnect, recover and cancel the original Herdr execution without manufacturing success or starting another owner.",
         "Build on the accepted local adapter and CG-501 recovery principles. Own cancellation/reconciliation and generation fencing; collection interpretation remains in the results task.",
         [
             "Controller/adapter restart and lost launch replies reconcile durable receipts with exact runtime identities before sending commands; repeated requests cannot duplicate the execution.",
             "Distinguish unreachable runtime, exited child, moved pane, reused locator, server replacement and restored shell. Preserve uncertain ownership; do not reclaim merely because a lease display or PID is absent.",
             "Disable independent native agent auto-restore for managed jobs unless it is proven generation-safe. Preserve original attempts, dirty source and output before any separately recorded replacement.",
             "Persist cancellation intent for the expected generation, signal verified descendants, use bounded escalation and confirm termination. Repeated cancel and cancel-versus-final races retain an honest disposition and partial evidence.",
             "Use bounded polling/event hints without network waits under state locks; late obsolete results cannot mutate the current attempt. Tests cover controller crash, server loss, delivery ambiguity and generation reuse.",
         ], deps=(TITLES["local"], "CG-501"), reading=("src/garden/runs.py", "src/garden/scheduler/reap.py", "src/garden/managed_worker.py")),
    item("results", TITLES["results"],
         "Feed actual Herdr execution evidence into Garden's existing result, source and acceptance pipeline exactly once.",
         "Consume the wrapper's durable files and receipts. Retain raw evidence before redaction, parser provenance and existing staged-source validation. Terminal screens are diagnostic only.",
         [
             "Validate the completion's run/generation, launch fingerprint, actual exit/signal, output references and source relationship before interpretation; reject/quarantine conflicting or cross-run evidence.",
             "Use existing harness parsing for final text, typed questions, errors, usage and cost; generic check results retain command/exit/output. Nonzero, timeout and partial evidence remain truthful even when some source was produced.",
             "Collect final files by their actual completed path after replacement, persist raw stdout/stderr separately, and retain immutable original receipts when retries or redaction produce derived views.",
             "Keep successful execution, source publication, review, applicable CI and task completion distinct. Reuse accepted current-head and remote staging checks; no pane state or receipt bypasses source acceptance.",
             "Concurrent/repeated collection and lost acknowledgments yield one accepted outcome through shared mutation coordination, retaining recovery data until delivery is acknowledged.",
         ], deps=(TITLES["recovery"], "CG-584"), reading=("src/garden/harness.py", "src/garden/runs.py", "src/garden/scheduler/reap.py")),
    item("modes", TITLES["modes"],
         "Make runtime selection cover all advertised Garden execution modes with the correct ownership and policy.",
         "Audit actual launch sites, especially direct harness subprocess paths. Apply the same execution component to auxiliary runs and controller-owned checks; do not move controller-only inputs to a remote worker.",
         [
             "First produce a complete launch-site matrix with the owner and inputs of each boundary; then implement routing for work/revise/resume/rebase, review, plan/kickoff, edit/investigation, persona/retro, trial/compare, probes and checks. Propose a bounded split if the inventory reveals independent implementations; explicit unsupported capabilities fail before dispatch.",
             "Preserve task or auxiliary owner, mode, selected model/difficulty, feedback, source and phase attribution on every run. Planner and reviewer work retains its existing sandbox/read-only policy.",
             "Use existing phase/resource/budget admission for auxiliary work and nested validation. No direct invocation path bypasses the configured runtime, while controller publication/CI-provider operations retain their authority.",
             "Checks run where their inputs exist; remote implementation does not relocate a controller-owned replay or source operation. Probes remain bounded and cheap without a paid model exercise.",
             "Focused parameterized fake-harness/command coverage verifies each distinct launch boundary and preserves existing unselected backends and manual completion.",
         ], deps=(TITLES["recovery"], TITLES["results"]), reading=("src/garden/planner.py", "src/garden/checkrun.py", "src/garden/scheduler/aux.py", "src/garden/runner/base.py")),
    item("remote", TITLES["remote"],
         "Run an existing Garden remote claim on that host's Herdr runtime with the same authenticated lease and delivery guarantees.",
         "Compose with the existing worker/host transport; Herdr remote TUI attach is not a replacement fleet or claim protocol. Use existing supported Linux workers and fake transport for deterministic tests.",
         [
             "Advertise supported Herdr capabilities in the existing readiness/admission path and select runtime per claimed attempt. Persist worker/claim and runtime identities separately.",
             "Execute the same trusted envelope on the claim host, using its local configured socket and Garden-owned checkout. Controller paths, privileged credentials and direct runtime sockets are not exported to model workers.",
             "Retain claim-generation staging refs, authenticated heartbeats/final delivery and source promotion checks. Reconcile active ownership and pending result delivery before accepting another claim.",
             "Controller/network disconnect, worker restart, lost final acknowledgment, expired/replaced claim and Herdr loss preserve original source/results and cannot start a duplicate or accept stale output.",
             "Host capacity, storage admission, absolute expiry, sandbox policy and descendant limits remain enforced with no new provisioning, budget or silent backend fallback. Exercise these boundaries using existing fake transports/disposable environments.",
         ], deps=(TITLES["recovery"], TITLES["results"], "CG-501"), reading=("src/garden/runner/remote.py", "src/garden/remote_worker.py", "src/garden/managed_worker.py")),
    item("human", TITLES["human"],
         "Let operators inspect and answer Herdr-hosted work without duplicating input or confusing runtime blockage with a product decision.",
         "Keep Garden's typed question/answer semantics and add guarded diagnostic attachment. A new browser terminal implementation is not required; a verified authorized attach route or command can be sufficient.",
         [
             "Typed Garden questions enter the existing waiting/decision flow once; generic Herdr blocked/unknown states produce an attributed diagnostic condition without automatically approving permissions.",
             "Answers are bound to the expected run/generation/question and persisted before delivery. Ambiguous delivery is reconciled rather than sending the same answer twice.",
             "Provide authorized inspection/attach guidance using current runtime locators and safe worker labels. Verify endpoint/occupant before input; never infer a global identity from a pane name.",
             "Separate observation from writable intervention, with one input owner and a durable intervention record before automatic input resumes. Direct terminal action cannot approve a PR or complete the task.",
             "Focused flow tests cover headless questions/resume, runtime permission blockage, stale pane, competing input and uncertain answer delivery; unsupported platform attachment has a clear fallback.",
         ], deps=(TITLES["recovery"], TITLES["results"]), reading=("src/garden/scheduler/human.py", "src/garden/inbox.py", "src/garden/web/actions/tasks.py")),
    item("views", TITLES["views"],
         "Make Herdr runs understandable in Runs, Now, Inbox and CLI without presenting terminal status as task acceptance.",
         "Extend CG-592's existing location/attribution work and shared presentation paths. Keep protocol calls off page-render hot paths and avoid a separate Herdr dashboard.",
         [
             "Display recorded runtime and logical host, attempt mode/source, observed state with freshness, and distinct running, awaiting input, reconciling, cancelling and completed meanings.",
             "Show useful runtime locators/attach guidance only to authorized operators; preserve private endpoint/credential disclosure policy and readable historical values when the host disappears.",
             "Explain scoped unavailability and recovery actions with the exact unresolved fact; terminal done/idle and stale events cannot turn into accepted completion or a generic user-decision card.",
             "Read cached/durable observations rather than blocking pages on sockets or scanning all terminal history. Preserve list filtering, pagination and existing check/outcome views.",
             "Use proportionate view/behavior checks for old records, missing runtime, stale identity and current completion; assess changed layouts for readable long labels and narrow windows.",
         ], deps=(TITLES["recovery"], TITLES["results"], TITLES["human"], "CG-592"), reading=("src/garden/web/pages/runs.py", "src/garden/now1.py", "src/garden/inbox.py"), difficulty="medium"),
    item("cost", TITLES["cost"],
         "Keep usage and accepted-outcome costs truthful when a run is collected, reattached or resumed through Herdr.",
         "Reuse CG-536's canonical cohort/delta logic. Runtime telemetry may describe known overhead but is not a substitute for actual model usage or an infrastructure bill.",
         [
             "Attribute harness usage once to the actual Garden run and phase using the durable result. Duplicate events, collection retries and reconnects cannot duplicate charges.",
             "Preserve unknown token/price values as unknown and distinguish zero known cost from absent pricing. Retained terminal history or idle duration cannot manufacture model cost.",
             "Separate known host/runtime overhead from model charges using existing accounting conventions; avoid double counting the same worker allocation and disclose unavailable overhead measurements.",
             "Keep failed/replaced attempts and intervention costs in their proper cohorts, and ensure Costs/Now/CLI agree through shared aggregation.",
             "Focused fixtures cover duplicate finals, conversation resume as a new attempt, unknown cost and phase filtering across cumulative records.",
         ], deps=(TITLES["results"], "CG-536"), reading=("src/garden/costs.py", "src/garden/outcomes.py", "src/garden/runs.py"), difficulty="medium"),
    item("ops", TITLES["ops"],
         "Provide a safe operator lifecycle for enabling, draining, retaining and retiring Herdr execution.",
         "Complete supported configuration/docs and runtime-owned terminal cleanup after integration paths exist. Do not deploy it or delete existing worktrees/history as part of this task.",
         [
             "Document and support explicit scoped enablement, version/capability checks and changes affecting only new admission; existing attempts retain their original backend until collection finishes.",
             "Provide runtime drain and rollback semantics that preserve active work, source, evidence and pending result delivery while new attempts can use an existing backend.",
             "Retain terminals for configurable inspection, then close only proven owned inactive terminal state after accepted collection. Reuse CG-527's separate worktree/history policy and never stop a shared server to cancel one run.",
             "Make upgrades/restarts accountable to active work; health checks never install or replace a live server. Prevent independent native restore from starting unmanaged attempts.",
             "Publish verified setup, inspect/answer/cancel, recovery, compatibility and rollback documentation for the actually supported platforms. Replace proposed setting names with real tested configuration and label limitations.",
         ], deps=(TITLES["modes"], TITLES["remote"], TITLES["human"], TITLES["views"], TITLES["cost"], "CG-527"), reading=("src/garden/config.py", "src/garden/runner/base.py", "docs/architecture.md"), difficulty="medium"),
    item("accept", TITLES["accept"],
         "Validate the composed integration and publish a truthful readiness account for the Phase 09 closing review.",
         "Reuse earlier focused tests and the pinned disposable runtime fixture. This task owns integration gaps and a product docs/herdr-readiness.md account, not a second implementation of existing components or automatic phase closure.",
         [
             "Exercise fake model/check work through local and simulated remote claims with actual runtime coverage where required: launch, source/result capture, question/resume, completion and guarded collection.",
             "Demonstrate uncertain launch, lost event/final acknowledgment, controller restart, Herdr loss, cancellation race, stale generation and pending delivery without duplicate execution or fabricated success.",
             "Verify socket/credential containment and resource/deadline enforcement across actual runtime-created descendants, plus adoption/drain/rollback preserving in-flight work.",
             "Record accepted Garden source, tested Herdr build/schema, supported modes/platforms, applicable checks and unresolved limitations. Compare available startup/recovery effort and known cost evidence without claiming unmeasured savings.",
             "File only concrete residual defects with precise owners; retain historical failures. Give the existing closing review a go/no-go account without declaring closure, deploying, requiring a paid live canary or inventing a soak/count gate.",
         ], deps=(TITLES["ops"],), reading=(ARCH, "context-garden/phase-09/docs/operator-guide.md", "src/garden/runner/base.py", "docs/architecture.md")),
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    p.add_argument("--root", type=Path, default=Path.cwd())
    args = p.parse_args()
    from garden.brief import brief_gaps
    from garden.graph import validate
    from garden.model import Status, Task
    from garden.planner import import_plan, parse_plan
    from garden.scheduler import Scheduler
    from garden.store import Store

    store = Store(args.root.resolve())
    scheduler = Scheduler(store)
    with scheduler.tick_lock():
        store.invalidate_tasks()
        existing = store.tasks()
        phase = store.phase("context-garden", "phase-09")
        if phase.closed or phase.frozen:
            raise SystemExit("Phase 09 must be open and unfrozen for this import")
        items = parse_plan(json.dumps(TASKS))
        titles = {t.title.casefold(): t for t in existing.values()}
        proposed_ids = {x["title"]: titles[x["title"].casefold()].id if x["title"].casefold() in titles
                        else f"HERDR-PREVIEW-{i}" for i, x in enumerate(items, 1)}
        errors = []
        preview = dict(existing)
        for x in items:
            old = titles.get(x["title"].casefold())
            if old and (old.phase != "phase-09" or "herdr_phase_task_key:" not in old.body):
                errors.append(f"ambiguous existing title: {x['title']}")
                continue
            deps = []
            for dep in x["depends_on"]:
                name = dep["id"]
                resolved = name if name in existing else proposed_ids.get(name)
                if not resolved:
                    errors.append(f"unknown dependency: {name}")
                else:
                    deps.append(resolved)
            if old:
                old_core = old.body.split("\n## Log", 1)[0].strip()
                if (old_core != x["body"].strip() or old.depends_on != deps
                        or old.reading != x["reading"]
                        or any(old.dependency_after.get(d) != "merge" for d in deps)):
                    errors.append(f"existing brief differs from this plan; review instead of skipping: {old.id}")
            task = Task(path=phase.path / "tasks" / f"{proposed_ids[x['title']]}.md",
                        id=proposed_ids[x["title"]], title=x["title"], status=Status.DRAFT,
                        product="context-garden", phase="phase-09", depends_on=deps,
                        priority=x["priority"], difficulty=x["difficulty"],
                        reading=x["reading"], body=x["body"])
            errors.extend(f"{task.title}: {e}" for e in brief_gaps(store, task))
            preview[task.id] = task
        errors.extend(validate(preview))
        if errors:
            raise SystemExit("Validation failed:\n" + "\n".join(errors))
        if not args.apply:
            print(json.dumps({"tasks": len(items), "brief_gaps": [], "graph_errors": [],
                              "existing": len([x for x in items if x["title"].casefold() in titles])}))
            return
        created = import_plan(store, "context-garden", "phase-09", items, status="draft")
        store.invalidate_tasks()
        tasks = store.tasks()
        phase_tasks = sorted((t for t in tasks.values() if t.phase == "phase-09" and t.product == "context-garden"), key=lambda t: t.id)
        errors = validate(tasks)
        for t in phase_tasks:
            errors.extend(f"{t.id}: {e}" for e in brief_gaps(store, t))
        receipt = {
            "created_ids": [t.id for t in created],
            "phase": "context-garden/phase-09", "open": not phase.closed, "frozen": bool(phase.frozen),
            "tasks": [{"id": t.id, "title": t.title, "status": t.status.value,
                       "path": store.rel(t.path), "depends_on": t.depends_on,
                       "dependency_after": t.dependency_after} for t in phase_tasks],
            "validation_errors": errors,
        }
        out = phase.path / "docs" / "task-import.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(receipt, indent=2))
        if errors:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
