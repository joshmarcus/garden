# Incident protocol: interrupted basic operation

Owner-requested 2026-09-06. This protocol is active whenever people or agents cannot reliably use a basic garden capability. The operator owns recovery under Josh's standing authority; do not wait for a person to diagnose routine failures or explicitly declare an incident. This is an operating procedure, not a claim of automatic product enforcement.

## Declare and contain

Enter an incident for an unavailable or repeatedly timing-out application, unsafe host pressure, broken main preventing ordinary work, inability to launch/reconcile tasks, or unreliable state that risks lost/duplicate work. One credible owner report is enough to investigate immediately. Distinguish degraded service from data-integrity/host-safety emergencies; do not wait for a complete root cause before containment.

1. Record the incident, start time, user-visible impact, last known working build and incident lead (current operator). Tell the owner what is affected and what containment is happening.
2. Pause ordinary admission through the product. Preserve phase holds and resource caps. Pause alone may still allow checks/reviews/rebases: inventory actual processes and confirm what continues. If full quiescence is required, use the existing service's documented no-watch override after accounting for active work; never start a competing scheduler.
3. Give recovery a real execution slot. A priority-0 task sitting behind unrelated work is insufficient. Allow short bounded work to drain or preempt lower-priority work deliberately, preserving branch/head, dirty edits, transcript, feedback and a recovery note. Verify descendants and escaped tests, not just the harness PID. Stop only identified processes. Do not create an extra uncapped worker to evade admission limits.
4. Hold work whose acceptance depends on the failed capability, including browser journeys when the application is unavailable. Independent bounded work may continue only if it does not delay recovery or threaten resources. Interrupted checks are environmental interruptions, not evidence of a code defect.

## Diagnose with a small evidence budget

Check service health, a cheap endpoint and the actual failing journey from the user's access path (Windows as well as WSL here). Record response time and result, not just HTTP status. Inspect current CPU/memory/swap/temp, cgroup events, process identity and recent logs. Sample a stack/profile when the service is alive but unresponsive. Compare a few time-separated measurements; cumulative memory.high events are not proof of a current OOM.

Avoid repeated expensive probes, full suites and polling storms. A timeout does not cancel server-side work. Before retrying any dispatch or other mutation, inspect run IDs, process identity and server progress. Do not duplicate an action merely because its HTTP client timed out. A running label without a worker PID/output is startup, not active repair.

Create one priority-0 recovery task with observed evidence, impact and measurable recovery criteria. Split long-term prevention or optional redesign from the smallest effective restoration when scope threatens recovery. Link related admission, restart and history work instead of opening duplicate fixes. An archive must preserve costs, identities, evidence and recovery references; do not move/delete active or referenced history as an improvised performance fix.

## Restore service promptly

Prefer a reversible, measured action: remove the immediate pressure, restart the unhealthy service, roll back a verified regression, or install a narrowly validated repair. Do not spend repeated cycles on speculative hot patches while the basic service remains unusable. After an ineffective attempt, reassess and choose a different recovery path. Keep temporary changes explicit, bounded, reversible and recorded, with removal instructions; a local experiment is not a shipped fix.

For a restart:

- First inventory workers, checks, startup/setup children and the current scheduler pass. Prefer a drained boundary. Confirm service KillMode and process groups rather than assuming all work will survive.
- Under the owner's standing recovery authority, a blocked service may be restarted after preserving/accounting for in-flight work and deliberately quiescing anything that cannot safely survive. An explicit owner restart request is authorization; do not ask again. Never blindly kill the whole cgroup or repeatedly restart without checking the outcome.
- Restart the existing service only; retain admission pause, resource limits and phase holds. Reinstallation also requires this accounting and verified source/build.
- Verify surviving workers by process identity and fresh output, reap/reconcile completed work through supported actions, and recover interrupted startup exactly once. Record any lost check as interrupted and retain its worktree. Check both basic HTTP connectivity and the actual failing user journey.

If normal web control is unavailable, use supported state-only CLI actions. Heavy recovery work must run in a bounded service/scope; never silently bypass caps. Do not race scheduler state writes. If a tool does not support a needed action, record the narrow recovery method and its verification instead of inventing a command.

## Verify recovery before resuming

Move from active incident to observing only after the failing journey succeeds with representative data, the urgent repair is actually installed when required, state reflects real processes, and resource measurements show headroom. A static asset, clock endpoint, screenshot, green unit test or merged PR alone does not prove recovery.

Use incident-specific acceptance criteria. Default for an availability incident: three successful representative journey checks over at least ten minutes, including one under the intended resumed workload, with measured latency and no renewed pressure or duplicate work. Restore one bounded work item first while observing, then the previously authorized concurrency if evidence supports it. Reopen containment immediately on recurrence. This short recovery observation does not replace phase 05's separate four-hour stabilization/adoption gate.

Close only after recording restored behavior, verification times/results, deployed build, remaining limits and deferred follow-ups. Remove temporary overrides/experiments intentionally, reconcile preempted tasks, and resume their preserved work in priority order. Keep freezes intact. Update the same operator automation back to ordinary duties; do not leave stale incident prompts or duplicate monitors.

## Ownership, updates and handoff

Maintain one current incident record under `context-garden/docs/incidents/` and link it from AGENTS.md. Replace obsolete current-state claims instead of appending contradictory instructions. Include: impact, containment, recovery task/run, live process evidence, paused/preempted work and recovery locations, experiments and dispositions, installed build, next concrete action, verification and exit decision.

During an incident, use five-minute operator follow-ups by default; increase lightweight resource sampling if pressure warrants it. Do useful recovery work at each check, not repeated status narration. Notify on impact/containment changes, a real recovery worker starting, failed recovery, verified restoration or a required owner decision. Keep unchanged progress quiet. Distinguish "requested", "starting", "running", "merged", "installed" and "verified working".

After recovery, record cause versus hypothesis, why existing checks missed the failure, and prevention tasks. Preserve evidence, report unknowns honestly, and count operator intervention against unattended stabilization. This protocol supplements normal operation and does not activate fast-forward PR clearance.
