#!/usr/bin/env python3
"""Review or create the deduplicated Phase 06 enterprise follow-ups.

The default mode prints the complete proposed tasks and performs no writes. Pass
``--apply`` only after operator review. Creation uses Garden's native locked Store
path so ID reservation, phase policy, and task frontmatter remain authoritative.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TASKS = [
    {
        "key": "enterprise-source-provider-network-trust",
        "title": "Support provider-neutral source control with scoped certificate and proxy policy",
        "difficulty": "hard",
        "priority": 1,
        "deps": ["CG-395", "CG-396", "CG-467"],
        "reading": [
            "src/garden/github.py", "src/garden/config.py", "src/garden/checks.py",
            "src/garden/scheduler/poll.py", "docs/architecture.md",
            "context-garden/phase-06/specs/context-garden-stripe-environment.md",
        ],
        "body": """## Goal

Define a provider-neutral source-control boundary for repository discovery, change requests, reviews, links and exact-source status while preserving the existing GitHub and GitHub Enterprise behavior. Apply endpoint-scoped certificate-authority and outbound-proxy policy through supported clients without disabling certificate verification or leaking authorization across endpoints.

## Context

CG-395 and CG-447 normalize explicit GitHub Enterprise identities, and CG-396/CG-467 separate validation policy from GitHub Actions. The remaining contract still assumes GitHub-shaped change requests and does not provide one safe connection-policy path for source and CI clients. Use synthetic services only.

## Acceptance criteria

- [ ] Introduce a narrow provider interface for repository identity, branch discovery, change-request metadata, reviews, links and exact-head status; retain the existing GitHub adapter without changing its safety gates.
- [ ] Configure web/API endpoints, credential references, certificate-authority bundles and proxies per product and operation. Reject mismatched authorities, unsafe redirects, invalid bundles and attempts to disable verification.
- [ ] Keep authentication failure, certificate failure, proxy failure, unavailable provider and unsupported operation distinct in diagnostics; never print credentials, private endpoints or proxy authorization.
- [ ] Preserve exact-head evidence, fresh conflict checks, atomic head guards, protected paths and external branch ownership across adapters. Unsupported merge/review capabilities fail closed.
- [ ] Exercise two synthetic providers with non-default base branches, stale heads, endpoint mismatch, redirect, proxy and custom-CA fixtures. No test contacts private infrastructure; existing GitHub behavior and lint remain clean.

enterprise_capability_key: enterprise-source-provider-network-trust
""",
    },
    {
        "key": "enterprise-workload-identity-resolver",
        "title": "Resolve scoped workload identities and secret references at the execution boundary",
        "difficulty": "hard",
        "priority": 1,
        "deps": ["CG-399", "CG-401", "CG-415"],
        "reading": [
            "src/garden/config.py", "src/garden/runner/base.py", "src/garden/remote_worker.py",
            "src/garden/managed_worker.py", "docs/worker-protocol.md",
            "context-garden/phase-06/specs/context-garden-stripe-environment.md",
        ],
        "body": """## Goal

Resolve logical credential references into least-privilege workload authority only at the operation boundary. Support short-lived identity providers without copying a human profile, distinguish automation from human identity in audit records, and fail closed when scope, audience, membership, renewal or revocation requirements are not satisfied.

## Context

CG-401 safely maps approved tool configuration and CG-399 keeps physical identities out of shared records. CG-400 was cancelled at the owner's request and must not be revived wholesale. This task is the smaller executable resolver contract needed by enterprise source, package, tool and worker operations.

This new scope is authorized by the owner's request to turn the enterprise environment specification into deduplicated Phase 06 work. It owns runtime resolution and enforcement only; it does not restore CG-400's policy-definition exercise or make deployment-specific identity decisions.

## Acceptance criteria

- [ ] Add a trusted resolver interface receiving a logical reference, operation, audience, run identity and requested lifetime; return only bounded authority plus non-secret issuer/expiry metadata.
- [ ] Permit provider adapters from trusted local configuration with explicit capabilities and versioning. Task text, worker output and repository files cannot register providers or request broader scopes.
- [ ] Pass resolved authority only to the named subprocess or protocol request. Never persist or emit credential values in claims, briefs, transcripts, notifications, diagnostics or committed configuration.
- [ ] Handle expiry, renewal, revocation, missing membership and unavailable providers as actionable environment failures without consuming an author revision or falling back to ambient credentials.
- [ ] Use synthetic identity providers to verify audience/scope mismatch, short lifetime, renewal, revocation, concurrent runs, redaction and local/remote equivalence on supported platforms.

enterprise_capability_key: enterprise-workload-identity-resolver
""",
    },
    {
        "key": "enterprise-operator-worker-network-boundary",
        "title": "Separate authenticated worker ingress from operator control access",
        "difficulty": "hard",
        "priority": 0,
        "deps": ["CG-216", "CG-398"],
        "reading": [
            "src/garden/web/app.py", "src/garden/web/trust.py", "src/garden/web/pages/api.py",
            "src/garden/remote_worker.py", "docs/worker-protocol.md",
            "context-garden/phase-06/specs/context-garden-stripe-environment.md",
        ],
        "body": """## Goal

Expose the authenticated worker protocol without exposing operator controls to worker-accessible networks. Require a separate operator authentication and authorization boundary for every non-worker control route, with explicit deployment diagnostics and no trust inferred from a missing Origin header.

## Context

CG-216 authenticates claim, heartbeat and finish requests, and CG-398 validates a human-gated profile. Current shared application routing still needs an enforceable boundary between worker credentials and operator authority.

## Acceptance criteria

- [ ] Classify worker protocol, read-only public, operator read and operator mutation routes in one auditable policy; startup fails when a configured exposure has unclassified routes.
- [ ] Worker bearer credentials authorize only their host-bound protocol operations. They never authorize operator pages, APIs, task decisions, configuration, merges, maintenance or deployment actions.
- [ ] Require configured operator authentication for operator routes on non-loopback or worker-reachable listeners. Missing Origin, forwarded headers or direct API access cannot bypass it; trusted-proxy handling is explicit and bounded.
- [ ] Keep browser CSRF/origin protection and add clear 401/403 diagnostics without disclosing identities or policy data. Existing local-only development remains explicit and safe.
- [ ] Disposable network fixtures cover unauthenticated direct requests, worker tokens on operator routes, valid operator access, proxy-header spoofing, route additions and local-only mode. No live access policy is changed by the tests.

enterprise_capability_key: enterprise-operator-worker-network-boundary
""",
    },
    {
        "key": "enterprise-enforced-planner-tool-sandbox",
        "title": "Enforce filesystem and network sandboxes for planning and approved tools",
        "difficulty": "hard",
        "priority": 0,
        "deps": ["CG-245", "CG-401", "CG-406"],
        "reading": [
            "src/garden/kickoff.py", "src/garden/scheduler/kickoff.py", "src/garden/runner/base.py",
            "src/garden/harness.py", "src/garden/checks.py", "docs/architecture.md",
            "context-garden/phase-06/specs/context-garden-stripe-environment.md",
        ],
        "body": """## Goal

Make filesystem and network policy an enforced execution capability for planners, synchronous kickoff, workers, checks and approved tools. Refuse permission modes or platform combinations that discard required deny paths or run without the configured sandbox.

## Context

CG-245 moved planning into a scrubbed scratch directory, CG-401 scopes tool configuration, and CG-406 fences canonical checkouts. Prompt and environment rules alone do not enforce the controller boundary when a harness bypass mode or missing OS sandbox retains broader authority.

## Acceptance criteria

- [ ] Define a capability-checked sandbox contract with authorized writable roots, readable context, named network destinations, subprocess inheritance and platform-specific enforcement reporting.
- [ ] Apply it to planning and synchronous kickoff as well as work, review and check execution. Scheduler state, credentials, sibling attempts and unrelated products remain outside the writable boundary.
- [ ] Reject bypass permission modes, missing enforcement capabilities and incompatible checkout strategies when policy requires isolation. Never silently drop deny paths or broaden network access.
- [ ] Preserve supported Linux, macOS and Windows-through-WSL execution through explicit mechanisms or actionable unsupported diagnostics; record which mechanism protected each run without leaking host details.
- [ ] Malicious planning documents and tool-output fixtures attempt controller reads/writes, symlink/path escapes, child-process escape and unapproved network access; all are denied while normal approved setup and publication still work.

enterprise_capability_key: enterprise-enforced-planner-tool-sandbox
""",
    },
    {
        "key": "enterprise-safe-active-artifact-preview",
        "title": "Serve every active design and run artifact through an inert preview boundary",
        "difficulty": "medium",
        "priority": 0,
        "deps": ["CG-318", "CG-427"],
        "reading": [
            "src/garden/web/app.py", "src/garden/web/pages/design.py", "src/garden/web/pages/runs.py",
            "src/garden/web/trust.py", "tests/test_web.py",
            "context-garden/phase-06/specs/context-garden-stripe-environment.md",
        ],
        "body": """## Goal

Treat generated design files and run artifacts as untrusted data. Apply one preview policy to HTML, SVG and every other active format so opening an artifact cannot execute with the operator application's authority.

## Context

CG-318 added design and capture serving and CG-427 renders event streams. Their useful one-click surfaces need a format-complete sandbox and response-header contract, including unmerged worktree files.

## Acceptance criteria

- [ ] Centralize raw artifact classification and response policy for design, task and run links, including worktree refs and archived attempts.
- [ ] Render supported active formats in a sandboxed separate-origin or equivalent inert boundary with restrictive CSP and nosniff headers. Unsupported or ambiguous formats download as attachments.
- [ ] Keep markdown sanitization, safe paths, product/ref identity and content-type handling intact. Filenames, metadata and payloads cannot inject headers, navigation or executable markup into the operator origin.
- [ ] Cover scripted SVG, active HTML, polyglot/incorrect MIME files, nested links, missing files, range/download behavior and benign images/documents through disposable HTTP tests.
- [ ] Preserve usable design and capture navigation and record the security boundary in operator documentation without exposing private artifact content.

enterprise_capability_key: enterprise-safe-active-artifact-preview
""",
    },
    {
        "key": "enterprise-notification-adapters",
        "title": "Deliver typed notifications through approved destination adapters",
        "difficulty": "medium",
        "priority": 2,
        "deps": ["CG-398", "CG-480"],
        "reading": [
            "src/garden/notify.py", "src/garden/config.py", "src/garden/events.py",
            "src/garden/inbox.py", "docs/architecture.md",
            "context-garden/phase-06/specs/context-garden-stripe-environment.md",
        ],
        "body": """## Goal

Deliver meaningful Garden events through trusted, typed notification adapters using logical destination references, bounded retries and destination-aware disclosure. Worker-authored text must never become an executable command or leak raw diagnostics to a broader audience.

## Context

CG-398 demonstrates safe private notification construction and CG-480 distinguishes operator work from user decisions. A reusable destination adapter and delivery-state contract remains separate from that profile-specific path.

## Acceptance criteria

- [ ] Define a versioned adapter interface receiving typed event fields and a logical destination reference from trusted local configuration; task text and worker results cannot select adapters or recipients.
- [ ] Apply per-destination field policy, redaction and safe structured argument handling. Never interpolate worker-authored content into a shell command or expose credentials, physical hosts or raw private diagnostics.
- [ ] Bound delivery time, retry and backoff; coalesce unchanged events while delivering meaningful failure, recovery and required-action transitions once per identity.
- [ ] Persist delivery success/failure separately from task state. A failed notification remains visible and retryable without rolling back or corrupting the underlying transition.
- [ ] Synthetic adapters cover timeout, transient and permanent failure, duplicate events, restart, unsafe text, revoked destination and disclosure filtering. No external message is sent by tests.

enterprise_capability_key: enterprise-notification-adapters
""",
    },
]


def _task_occurrences(root: Path, key: str, title: str, store) -> tuple[list[Path], list[Path]]:
    key_paths: list[Path] = []
    title_paths: list[Path] = []
    for path in root.glob("context-garden/phase-*/tasks/CG-*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if f"enterprise_capability_key: {key}" in text:
            key_paths.append(path)
    title_paths.extend(task.path for task in store.tasks().values() if task.title == title)
    return key_paths, title_paths


def _preflight_native(root: Path, task: dict, store) -> list[str]:
    """Validate dependencies and reading through the installed Garden model."""
    from garden.brief import brief_gaps
    from garden.model import Status, Task

    errors: list[str] = []
    for dep in task["deps"]:
        try:
            store.task(dep)
        except KeyError:
            errors.append(f"dependency does not exist: {dep}")
    phase = store.phase("context-garden", "phase-06")
    provisional = Task(
        path=phase.path / "tasks" / f"PREVIEW-{task['key']}.md",
        id="PREVIEW-000",
        title=task["title"],
        status=Status("draft"),
        product="context-garden",
        phase="phase-06",
        depends_on=list(task["deps"]),
        priority=task["priority"],
        reading=list(task["reading"]),
        difficulty=task["difficulty"],
        body=task["body"].strip(),
    )
    errors.extend(brief_gaps(store, provisional))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="create tasks after review")
    parser.add_argument("--validate", action="store_true", help="run native locked validation without creating tasks")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="driving Garden root")
    args = parser.parse_args()
    if args.apply and args.validate:
        parser.error("choose at most one of --apply and --validate")
    root = args.root.resolve()
    if not args.apply and not args.validate:
        print(json.dumps(TASKS, indent=2))
        return 0
    from garden.scheduler import Scheduler
    from garden.store import Store

    store = Store(root)
    store.tasks()
    scheduler = Scheduler(store, log=lambda message: print(f"garden: {message}"))
    with scheduler.tick_lock():
        # Reload under the controller lock before resolving deduplication, dependencies,
        # reading paths, and reservation-backed IDs.
        store.invalidate_tasks()
        store.tasks()
        pending: list[dict] = []
        for task in TASKS:
            key_paths, title_paths = _task_occurrences(root, task["key"], task["title"], store)
            if len(key_paths) > 1 or len(title_paths) > 1:
                raise SystemExit(
                    f"{task['key']}: ambiguous existing tasks: "
                    f"keys={[str(p) for p in key_paths]}, titles={[str(p) for p in title_paths]}"
                )
            if key_paths:
                if title_paths and title_paths[0] != key_paths[0]:
                    raise SystemExit(f"{task['key']}: stable key and title refer to different tasks")
                print(f"skip {task['key']}: already created at {key_paths[0]}")
                continue
            if title_paths:
                raise SystemExit(
                    f"{task['key']}: title exists without stable key at {title_paths[0]}; review manually"
                )
            pending.append(task)
        # Validate every pending dependency and reading-list entry before the first
        # reservation-backed create. A later validation error cannot leave a newly
        # created prefix; process interruption remains resumable by stable key.
        validation_errors: list[str] = []
        for task in pending:
            validation_errors.extend(
                f"{task['key']}: {error}" for error in _preflight_native(root, task, store)
            )
        if validation_errors:
            raise SystemExit("native validation failed:\n- " + "\n- ".join(validation_errors))
        if args.validate:
            print(f"native validation passed: {len(pending)} pending, {len(TASKS) - len(pending)} already created")
            return 0
        for task in pending:
            created = store.create_task(
                "context-garden",
                "phase-06",
                task["title"],
                task["body"].strip() + "\n",
                depends_on=list(task["deps"]),
                reading=list(task["reading"]),
                priority=task["priority"],
                status="draft",
                difficulty=task["difficulty"],
            )
            print(f"created {created.id} at {created.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
