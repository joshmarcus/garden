# True multiplayer gardens

Status: proposed implementation specification, 2026-09-11. The owner requested the
specification and task breakdown, and selected **each person runs locally** as the
primary setup. [Phase 10](../phase-10/goals.md) contains the implementation
plan, released by the owner on September12. This document describes intended behavior; it does not claim these features
are present in the running release.

## Product outcome

Several people share one garden while each person runs their own local UI and
scheduler. Issues belong to specific people. Only the assignee's scheduler may
advance an issue, and only inside that person's assigned execution scope. A person
can start with an assigned project and phase, open a personal Inbox, and begin work
there without claiming the rest of the garden.

The project selector lives in the upper-right application header. Selecting a
project focuses every normal view on it. Changing this view never changes the
scheduler's assignment or starts work. A person with no assignment can start both
the UI and scheduler successfully and remain idle. A viewer can serve an explicitly
published, read-only view without running an execution controller.

In the interface, **project** means the existing Garden product, identified by its
stable product key. This feature does not introduce a second competing hierarchy.

## Example journey

Alex and Blair clone the same garden onto separate machines and connect their
local applications to its shared coordination endpoint. An administrator admits
both as members, assigns Alex to Orchard / Phase 03 and Blair to Orchard / Phase 04,
and assigns issues to each person. Alex's scheduler starts eligible Alex issues
in Phase 03. Blair's scheduler starts eligible Blair issues in Phase 04 only after
their dependencies are actually satisfied. Both can see authorized shared context.

Alex selects a different project in the header to inspect its board. Alex's work
continues in the assigned Orchard scope. The header separately shows the current
identity, viewing project, and execution project/phase so this distinction is clear.
An explicit assignment action, with permission and concurrency checks, changes work.

Casey joins as a member without a work scope. Starting the UI and scheduler shows
"No work assignment" and makes no work move. There is no fallback to the first
project, first phase, Git author, operating-system username, or all unowned tasks.
A public viewer sees only published project information and cannot turn that page
into a member session or controller by changing a URL or issuing an API request.

## Identity, membership and permissions

A garden has a stable identity and a membership registry. A member has a stable user
ID, display name, active/disabled state, role, project visibility and assignment
permissions. Display names and credential identities are separate. Credentials bind
a local installation to a member and garden; request parameters, owner filters and
Markdown display fields cannot assert the caller's identity. Enrolment and credential
revocation are explicit administrative operations. Credentials stay out of Git,
task bodies, browser URLs, logs and exported context. Network connections authenticate
the coordinator and use TLS outside an explicitly local development transport.

The first release provides these roles:

| Role | Read | Explicit actions | Automatic work |
| --- | --- | --- | --- |
| Administrator | Authorized garden/project views and administration | Manage membership, assignments, publication and guarded recovery | Only issues assigned to that administrator inside their work scope |
| Member | Authorized projects | Act on their own issues and addressed decisions within existing human gates | Only their eligible assigned issues inside their work scope |
| Viewer | Authorized read projection | None | None |
| Anonymous public viewer | Explicitly published projection | None | None |

Administration is not permission for that person's scheduler to take every issue.
Self-assignment is allowed only if an administrator explicitly grants it. Otherwise
members request assignment; they cannot acquire authority by editing an owner field
or claiming an unassigned issue. Disabled identities and revoked installations fail
closed. A role governs access, an assignment governs work, and a view filter governs
presentation. These are independent checks.

Private team members are trusted with repositories and tools they can independently
access. This design enforces Garden-mediated actions; it cannot revoke an unrelated
Git or provider credential held outside Garden. Public viewers receive no repository
or operator credentials. Avoid describing ordinary repository access as a security
boundary that it cannot provide.

## Issue ownership and execution scope

Reuse the task `owner`, explicit-unassigned marker and phase `default_owner`
introduced by CG-414. That implementation treats ownership as metadata, not an
execution identity. Multiplayer adds validated membership binding and authority;
it must not silently reinterpret arbitrary legacy owner strings as authenticated
users. The existing precedence remains:

1. An explicit task owner selects one active member.
2. An explicit task unassignment (`owner: '-'` in the existing format) overrides inheritance.
3. Otherwise the phase's default owner applies.
4. With no valid default, the issue is unassigned and cannot run.

For the first release there is no implicit project-wide owner fallback. Assigning a
person a project/phase scope does not silently rewrite issue owners or the phase
default. The assignment UI may offer an explicit, previewed operation to set a phase
default or assign selected issues. Unknown, disabled or out-of-project assignees make
the work ineligible and produce a useful assignment diagnostic.

Each member has zero or one active execution assignment in the first release:
project, starting/current phase, enabled/paused state, generation and optional
phase-advance policy. There is no assignment by default. The current phase is
persisted centrally and survives scheduler restarts. A member can own issues outside
this scope; those issues remain visible in their personal Inbox but do not run yet.
Concurrent work across several assigned projects is a later extension.

A runnable issue must satisfy **all** of these conditions: authenticated active
member; matching effective owner; matching project/current phase; valid coordination
claim; and all existing readiness, dependency, hold, budget, resource, review and CI
gates. Neither ownership nor a later phase assignment bypasses dependencies. Visible
cross-project dependencies may be followed without moving execution scope; hidden
dependencies appear as opaque blockers without leaking their titles or contents.

Phase advancement defaults to explicit action. An optional configured advance policy
may move the cursor to the next authorized phase only after existing phase-completion
gates and the member's remaining work permit it. It does not assign new issues or
release holds. Planning, phase reviews, retrospectives and closure require a separate
explicit phase-operation assignee and operation claim. A task default owner alone
never grants whole-phase authority, and one user's empty queue cannot close a phase
while another user's work remains.

## Local applications and shared coordination

Every person keeps their local UI, scheduler process, execution workspaces, harness
configuration and execution credentials. The shared component is a small coordination
service, not a requirement to move everyone's UI or workers onto one machine. It may
run on a designated garden host; it does not independently schedule unassigned work.
The first release uses one writable coordinator with a transactional local database
and durable operation journal. Replicated coordinators and active/active failover are
out of scope. Do not put that database in Git or share it through a network filesystem.

This extends the [system architecture](system-architecture.md)'s single-authority
rule. Local schedulers propose transitions for their own issues. The coordinator
validates identity, assignments, versions and claims, commits the authoritative
transition and serializes shared effects. Local file locks still protect local
workspaces; they cannot serve as cross-machine ownership locks.

Git remains the durable authored context and task projection. The coordinator owns
the canonical lifecycle projection into task Markdown; each clone is a cache and
working context, not another task-status authority. Authored edits to issue content
or ownership enter as versioned proposals and are validated before acceptance.
Synchronization must preserve unrelated local edits, detect conflicts and never
force-reset a person's checkout. Assignment/role changes become effective when the
coordinator accepts them, not when a stale clone happens to pull them.

Membership, assignment generations, claims and pending effects are transactional
control state. Immutable run results and events retain actor, garden, task, attempt,
assignment generation, fencing generation, evaluated source and operation identity.
A transactional outbox records pending Git projections. A failed Git write leaves a
visible pending projection and a retryable operation; it cannot roll back authority
to stale Markdown. A destructive or dispatch decision that needs newer authored
context waits for a usable canonical revision. Reconnection refreshes state before
any mutation. There is no offline autonomous scheduling or replay of an unchecked
queue of old commands.

### Claims, effects and handoff

An issue has at most one active lifecycle claim. Acquisition is a compare-and-swap
against its accepted owner, assignment generation and task version. Claims include
an installation ID, run/operation identity, server-issued expiry and monotonically
increasing fencing generation. Two installations for the same person must contend
through this authority just like two different people. Client clock skew cannot
extend an expired claim.

Every mutating lifecycle path uses this contract: initial dispatch, result adoption,
revision and review dispatch, resume, cancellation, external-check reconciliation,
CI reruns, publication, merge and automatic completion. Read-only inspection can
observe any authorized task. It cannot write progress to a different assignee's task.
Worker/reviewer identities are delegated identities bound to the owner's valid claim;
existing independent-review requirements still apply.

The coordinator also gates shared capacity and spend reservations across users.
Existing per-host limits remain local enforcement boundaries, and shared limits
cannot be multiplied by starting more schedulers. Fleet creation, upgrades, cleanup,
planning and other garden-wide effects require explicit administrative operation
authority; an unassigned idle installation performs none of them.

A check followed by an unrestricted client-side push or merge leaves a race. Shared
external mutations therefore use a serialized effect gateway on behalf of the
requesting owner, with narrowly delegated credentials, a durable operation ID and
provider-side conditional updates where supported. Admission, reassignment and
pending effects use the same authority. The gateway is not a general scheduler or
permission for another member to progress the issue. Local workers cannot bypass it
with Garden-issued publication credentials.

External services do not all support exactly-once effects or fencing. If a request's
outcome is unknown, retain the original request identity, reconcile the provider and
block conflicting effects. Never retry blindly or claim that a local lease can undo
an already accepted external request. A handoff cannot report itself complete while
an old effect is unresolved.

Reassignment, unassignment, scope change, membership revocation and lease loss stop
new effects and fence the previous generation. A running local worker is asked to
stop safely; its commits, logs and results remain evidence. Late results may be
retained as stale evidence but cannot advance status or publish. An issue with active
work enters an explicit handoff/reconciliation state, visible to both parties and
administrators. The new assignee resumes only after the old claim/effects are safely
resolved. Crashes, restarts and partitions never cause an automatic second author
or silently discard the previous attempt. A coordinator outage leaves local read
views available with a stale-state label and execution visibly waiting.

## Personal Inbox and action authorization

The default Inbox is "Mine": issues effectively assigned to the current member,
questions addressed to them, and phase decisions they are authorized to own. A
selected project narrows these results. A separate all-authorized-work view allows
team visibility without acquiring execution authority. Counts, badges, filters and
empty states use the same scope as the rows they describe.

Issue actions check the authenticated actor and current task/assignment version at
the server, including direct POSTs, keyboard actions and retried requests. A stale
page cannot answer a question, resume or merge after reassignment. Show the new
assignee or a non-disclosing conflict message as appropriate. Administrative
reassignment and recovery remain explicit attributed actions and obey substantive
human-review and source-identity gates.

Global administrative decisions belong in a clearly labelled administration Inbox;
existing taskless cards must not leak into every person's "Mine" through a permissive
filter. Notifications and live updates follow the same recipient and project rules.
An unassigned member may inspect authorized work and request an assignment; merely
opening their Inbox or starting `watch` does not triage other people's issues.

## Project selector and consistent views

Put a labelled project selector in the upper-right shared header, with an accessible
mobile placement. Offer only projects the caller may read. "All authorized projects"
is an explicit overview, never a scheduler scope. On first visit use the member's
assigned project when visible; otherwise show a neutral authorized overview. Empty
membership produces an empty view, not the first private project.

A project in the current URL takes precedence over the saved local preference when
it is authorized. Otherwise use the saved preference, then the initial default.
An invalid or revoked explicit project produces a non-disclosing unavailable state;
it never silently falls back to a broader view. Persist selection per user/browser,
not in a shared global file. Preserve it across navigation and browser history.

Apply the same validated scope to Now, Board, Inbox, task details, phases, graph,
PRs, runs, costs, docs, search, exports, page fragments, JSON APIs and SSE/live updates.
Project membership is an access boundary; selection is an additional display filter.
Links keep the selected scope or explicitly identify a switch. Garden-wide settings
and health are restricted, clearly labelled administrative surfaces rather than
unfiltered exceptions hidden inside project views. Shared-cost allocations and
unknown costs remain honest; selecting a project must not relabel the garden's
entire spend as that project's spend.

## Viewer-only and public serving

A viewer is a server-enforced role with a dedicated read model. "Public" is an
explicit publication setting with an allowlist of projects and fields; it is not
synonymous with every member-readable endpoint. Default publication is empty.
For the initial public projection, allow only selected project names/descriptions,
phases, task IDs/titles/statuses, safe dependency structure and explicitly approved
public descriptions/links. Free-form task bodies, documents and attachments require
explicit inclusion and content review; they are not public by inheritance.

Do not publish raw logs, prompts, transcripts, diffs, arbitrary files, configuration,
credentials, private repository links, local paths, provider identities, private
member identities, internal decisions or detailed costs by default. Escape rendered
content, prevent traversal and keep inaccessible dependency targets opaque. Publication
revocation invalidates subsequent cached responses and live subscriptions; content
already downloaded by a reader cannot be recalled.

Viewer serving starts only the read application. It neither constructs an enabled
scheduler nor starts `watch`, ingress, workers, upgrades or cleanup. A public process
receives only the approved projection, without the private garden checkout, control
store or execution/operator secrets. An authenticated private viewer can use the
same restricted route family with its own authorized projection.

Enforce a positive read-route and field allowlist for pages, APIs, fragments, streams,
exports and downloads. Deny mutations regardless of HTTP method, route aliases,
origin, loopback location or hidden UI controls. HEAD and OPTIONS must not become a
route-policy bypass. Audit GET handlers for incidental writes. Role changes close
or reauthorize existing sessions/streams. The public server cannot elevate itself
by sending a different user ID, owner query or scheduler flag.

## Adoption and compatibility

Multiplayer is an explicit garden mode. Existing single-user gardens continue in
legacy mode until an administrator runs a migration preview and commits enrollment.
New multiplayer identities start unassigned. Legacy labels must be explicitly mapped
to member IDs; unresolved labels stay ineligible. The preview covers phase defaults,
explicit unassignment, current work, approvals, source state and local configuration.
Drain active work or perform the defined handoff before enabling shared authority.

Enable a protocol/version gate so an old controller cannot keep mutating a multiplayer
garden through the supported interfaces. Remove its write authority as part of
cutover; a Markdown flag alone is insufficient. Preserve backup and recovery paths.
Returning to standalone mode requires quiescing shared claims/effects and exporting
one consistent authoritative snapshot; it cannot silently activate several local
controllers. Never rewrite historical authors, owner labels, results or review records
to manufacture a migration history. No package release, production activation,
public deployment or additional infrastructure spending is part of this specification
and planning request.

## Acceptance and delivery

Implement through the dependency-linked drafts in [Phase 10](../phase-10/goals.md).
The shared authority and scheduler enforcement precede enabling multiplayer;
identity fields and hidden buttons alone are not a partial secure release. Keep
ordinary single-user behavior covered during incremental development.

The final acceptance exercise uses two independent local checkouts/processes and
one coordinator, plus unassigned and viewer identities. It demonstrates disjoint
ownership, assigned phase/dependency behavior, same-user duplicate scheduler
contention, stale claims, reassignment during work, crash/restart, a lost response,
coordinator disconnect/reconnect, personal Inbox isolation, all-view project focus,
and public read-only behavior through direct requests as well as visible controls.
Check that unassigned startup makes no task, run, PR, CI, phase or resource operation.
Use meaningful focused concurrency and authorization checks and a bounded local
integration exercise; cloud workers, production fault injection, screenshots in a
prescribed format and a new paid deployment are unnecessary. Report what was actually
verified and any remaining limitation under the existing proportionate review policy.

Later extensions may add multiple simultaneous work scopes, group assignment,
enterprise SSO, automatic coordinator failover and more public projection fields.
They are not prerequisites for the first complete two-person workflow.
