# phase-05 goals (draft)

_Drafted by `garden retro` from context-garden/phase-04; edit before planning._

# phase-05 goals

_Drafted by `garden retro` from context-garden/phase-04 on 2026-09-05. The owner's answers to the retro's questions go under Decisions._

## Why this phase

**In one sentence: make the numbers readable, then spend on what they say.** Phase 04 finished the leaveability mechanism (a non-blocking tick, live config, harness pauses, restart recovery, hard-tier queue merges) and the operator's share of spend fell to under a third. But hand merges rose to 16 of 57, cost per easy task rose to $5.04, rebase rounds sit at 1.57 per merge, first-pass approval fell to about 75%, and three definition-of-done lines were never measured because nothing in the tool measures them. The personas agree the surfaces drifted behind the mechanism and that the brief gate and the fence both have open doors. Phase 05 first makes the garden report cost per accepted task and first-pass approval per model, tier and harness, closes the trust gaps the security review verified, then takes the routing and onboarding features that depend on those numbers.

## Goals

1. **The numbers exist before the experiments.** Cost per accepted task and first-pass approval per model, tier and harness in garden metrics, the Costs page and the retro's Numbers section; hand merges and tick duration in metrics and the rail; the retro captures its own walkthrough before the personas run and refuses to run them without it. CG-213 and CG-230 dispatch only after this merges.

2. **Every PR reaches the queue and every status write is one writer.** Any PR with no review recorded for its head is queued on the next tick, on every runner (widen CG-236); resume means the same on the manual runner; Scheduler.mark_done and unapprove exist and a source-grep test forbids status assignment elsewhere; task files get optimistic concurrency and a duplicate id degrades to a validate problem; retro-filed drafts cannot collide with live ids.

3. **Trust matches the mechanism, round three.** The brief-gate and git-config items from the reopen are in; the config reload holds while an in-flight fence manifest disagrees; notify.command runs scrubbed; the planner and kickoff run in the worker environment; each worker gets a private harness config dir with only credentials; state.json is restored and task files are attributed rather than exempt.

4. **Briefs are right the first time.** No brief ships with an empty or unresolved reading list; inlined files come from the task's base, not a dirty worktree; revise briefs restate the criteria and the concrete blocker; dependent tasks are sequenced at planning; retro evidence is inlined. Per-criterion evidence is enforced: a reviewer met:false or missing evidence is a mechanical changes_requested.

5. **The retro leaves a list the owner can triage in one sitting.** Only high findings become drafts; the rest render on the retro page with file-as-task; the retro reports what it held back. One vocabulary across rail, Config, CLI and Inbox; no task ids in copy; one needs-you predicate; the scaffolded operate skill, design.md, roadmap.md and the architecture map match the product.

6. **The features.** Onboarding from an existing repository (CG-215) as the headline; harness-aware profile stops; redispatch and pin commands; inline editing of a draft's criteria and reading list; a tier that names several harness and model options (CG-230) once goal 1 can read it; OpenRouter only as an adapter around an existing CLI (CG-213 option b) and only after goal 1.

## Non-goals

- Workers on independent remote hosts over HTTP (CG-216) until a named second team asks.
- A garden-owned tool-calling loop for OpenRouter.
- TUI parity tasks filed by default.
- Changing the operating point before goal 1 lands.

## Definition of done

Measured with `garden metrics` against phase 04, by the tool.

- cost per accepted easy task at or under $4 (phase 04: $5.04); first-pass approval at or above 90% (phase 04: about 75%); both reported per model, tier and harness.
- hand merges zero on every tier and runner (phase 04: 16 of 57); rebase rounds per merge under 0.5 (phase 04: 1.57).
- a phase-05 walkthrough committed by the retro before the personas run; tick duration and hand merges visible in the rail.
- no task reaches ready or a run without Scheduler.approve, on any surface; no brief ships with an empty or unresolved reading list.
- the security persona's three phase-04 highs closed and no new high.
- the retro files no more drafts than the owner's cap and reports what it held back.
- a garden doctor pass from garden onboard on a non-Python fixture with no hand edits.
- operator share of spend below phase 04's.

## Carried over from phase 04

Blocking the phase-04 close: the approve-gate bypasses and the reading-list and git-config fence. Follow-ups filed by the retro: config-reload hold, task-file concurrency and duplicate ids, the scrubbed planner, the private harness config dir, one writer for status, brief completeness, planning sequencing, docs drift, vocabulary, the walkthrough renderer and check retry, per-phase persona runs, and the small items. Drafts already in phase 05: CG-213, CG-215, CG-216, CG-230, CG-236, CG-237; CG-222 sits in phase 06. Cancelled: CG-206 (notify.command in the driving garden is an operator edit, not a product task). Exceptions for the phase-04 closing document: sixteen hand merges (eight queue-rotation), reviews moved to the easy tier at 14:40, mediums to sonnet at 14:50, automerge_method merge, review.max_rounds 4, codex in bypass-permissions mode, and four persona runs discarded and restored by hand after CG-237.

## Features for the next phase

- CG-240: Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs page and the retro
- CG-241: The retro files only high findings as drafts and keeps the rest on the retro page with a one-press file-as-task
- CG-242: The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail
- CG-243: redispatch kills the superseded worker, and pin runs the canary, installs and restarts after a tick
- CG-244: Operating-profile stops name a tier per harness, and user-facing copy drops task ids
- CG-245: A draft's acceptance criteria and reading list can be edited inline on the task page

## Follow-ups carried from the retro verdict

- CG-277: Live config reload holds while any in-flight worker's fence manifest disagrees with garden.yaml on disk
- CG-278: Task files get optimistic concurrency and a duplicate id is a validate problem, not a fatal exception
- CG-279: The planner and synchronous kickoff run in the worker environment
- CG-280: Each worker gets a private harness config dir holding only credentials, and the fence covers state.json and task files
- CG-281: Every status write goes through _transition: Scheduler.mark_done and unapprove, and a source-grep test
- CG-282: A brief never ships with an empty or unresolved reading list, and a revise brief restates the criteria and the concrete blocker
- CG-283: Planning sequences dependent tasks and inlines retro evidence into the brief
- CG-284: Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and the architecture module map
- CG-285: One vocabulary and one place for each fact across rail, Config, CLI and Inbox
- CG-286: The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal exit
- CG-287: Persona runs are recorded per phase and the retro validates the run id it reads
- CG-288: Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests, a second opinion for self products
