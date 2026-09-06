---
frozen: '2026-09-05'
closed: '2026-09-05'
---

# phase-04 goals

_Drafted by `garden retro` from context-garden/phase-03 on 2026-09-05, with the owner's decisions added by the operator._


## Why this phase

**In one sentence: finish making the loop leaveable, then give it the features that waited.** Phase 03 halved hand actions (about a hundred to about twenty-five), reached 93% first-pass approval and merged all its trust items, but two definition-of-done items did not ship: a garden.yaml change still needs a restart, and twelve of thirty merges were by hand because the queue does not merge hard-tier PRs. The tick also runs the product test suite in-process, so the web UI waits a minute per press. The personas agree: the loop runs for an hour, not a night. The first half of this phase closes that; the second half takes the features that were deferred from phase 02 and 03.

## Goals

1. **The loop runs overnight.** Checks and pre-merge rebases as run records outside the tick, actions that do not wait for the tick, a tick duration in the report (CG-182, first and alone). The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check, as a config choice. garden.yaml is re-read each tick on change and the Config page says which keys are live. On start, the scheduler walks run records of every mode for finished-but-unreaped runs, and the canary (CG-180) runs before a pin moves. notify.command is configured in the live garden.

2. **Briefs are complete before they cost a run.** Approve refuses or flags placeholder acceptance criteria and unresolved reading-list paths, and the Inbox approve card shows the gap. Retro evidence is inlined into the brief rather than pointed at by path into the garden repo. Discovered tasks are deduplicated by normalised title and file, and new drafts are held while the base is red. Two tasks that serve one goal are sequenced or scoped at planning. Results and reviews speak to each criterion (CG-179).

3. **Trust claims match the mechanism.** Workers and checks run without HOME or under a sandbox by default; retry_command comes only from config and runs scrubbed; the fence hash-checks garden*.yaml and .garden/state.json across a run; automerge holds when a diff touches garden*.yaml, **/tasks/, .github/ or principles/; POSTs require a loopback Host; only named bots are trusted; the planner runs in the worker environment.

4. **Every state has a surface and every surface is right.** Inbox cards read only the log; terminal tasks drop needs_human and automerge_blocked everywhere with a one-tick sweep; mechanical rebase runs, the new event kinds and the merge queue head are rendered; an in-flight review is cancelled when its PR merges; approve exits 1 on a refusal; new-phase refuses an unregistered product (CG-184, CG-185, CG-156).

5. **One writer per fact.** Scheduler.approve and Scheduler.mark_done go through _transition and phase_refusal from CLI, web and TUI; one recorded _rebase_branch helper replaces the four copies and the metrics rebase block is scoped to the phase; _queue_hold and _queue_leave are the only writers of queue state; dispatch phases are wrapped and state.save() is in a finally; cost is keyed by run id; a GitHubLike protocol is shared by FakeGitHub and MemoryGitHub; cli.py is split by command family.

6. **The features.** The retro ends in a verdict and has a features section (CG-178, CG-181 done); a retro page per phase (CG-146); the new-task form (CG-132); approve into a phase (CG-186); every persona finding becomes a draft (CG-187); move a task between phases and a backlog view (CG-162, CG-163); manual-task ergonomics (CG-158); plates and the seedling mark (CG-030, CG-183).

## Non-goals

- Hosted or multi-user operation.
- Changing the herbarium look beyond CG-184 and CG-183.
- A new runner or harness.

## Decisions

Answered by the owner on 2026-09-05, at the close of phase 03:

- **The merge queue merges hard-tier PRs** after two approving rounds and its own scratch-merge check; the setting defaults on (CG-191).
- **Structure gate:** CG-182 (the tick never blocks the UI) runs first and alone; then CG-197 (the cli.py split); features dispatch only after both merge. Encoded as dependencies on every other phase-04 task.
- **No budget cap** on this phase.
- **The retro's close verdict closes the phase** without waiting for approval; only reopen raises a decision (CG-178).
- **Workers 7** once CG-182 is in and the tick is fast again; back to 5 if the cascade returns.
- **Hard-tier merges by hand** (scratch merge, lint, suite) until CG-191 lands.
- **The operator thread's cost is a goal** (2026-09-05, after the session's own cost was measured at about 60% of the workers'): the observation feed is configurable (CG-219), the operating point is one slider (CG-221), the operator compacts at phase, retro and pin boundaries, and its spend is recorded per session beside the workers' spend.

## Definition of done

Measured with `garden metrics` against phase 03.

- hand merges: zero on easy and medium, zero on hard once the two-round policy is on (phase 03: 12 of 30).
- any web action answers within one second while a check is running; tick duration reported and under ten seconds without a model run.
- a garden.yaml change takes effect within one tick, no restart; the Config page names the live keys.
- no task dispatched with placeholder criteria or an unresolved reading-list path.
- rebase rounds per merge under 0.2 measured on the phase's tasks with mechanical and agent rebases reported separately.
- cost per easy task at or under $4 (phase 03: $4.34).
- no module over 800 lines under src/garden/; cli.py is a package.
- the walkthrough shows no Inbox fragment, no needs-you badge on a done task and a described rebase run.
- the security persona's three high findings are closed.
- every task shipped through `garden tick`; exceptions listed in the closing document.
- operator turns and spend recorded for the phase (`docs/operator-spend.jsonl`), with the operator's share of total spend reported in the retro and lower than phase 03's.

## Carried over from phase 03

Open from the retro: live config reload (no task existed), hard-tier queue merges, the brief-quality gate, discovered-task dedup, worker isolation gaps, the UI hygiene items, the structure items, in-process runner limits (argv[0] fakes, real-harness tests), the qa medium-tier cap, and notify.command configuration in the live garden. Features moved from phase 02 and 03: CG-030, CG-132, CG-146, CG-156, CG-158; drafts already in this phase: CG-162, CG-163, CG-178, CG-179, CG-180, CG-182, CG-183, CG-184, CG-185, CG-186, CG-187. Exceptions to list in the phase-03 closing document: PR #104 (hand fix of main), twelve hand merges, the close-phase route added by CG-135, and CG-181 merging one minute before the freeze.

## Features for the next phase

- CG-191: The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check
- CG-192: garden.yaml is re-read each tick when it changes, and the Config page says which keys are live
- CG-193: Approve refuses placeholder acceptance criteria and unresolved reading-list paths
- CG-194: Workers get no HOME, retry_command comes only from config, and the fence hash-checks garden.yaml and state.json
- CG-195: Inbox cards read only the log, and terminal tasks drop needs-you and automerge notes in every view
- CG-196: Rebase runs, the new event kinds and the merge queue have a surface
- CG-197: Split cli.py into a cli/ package and fold the four rebase copies into one recorded helper
