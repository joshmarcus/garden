---
plant: poppy
latin: Papaver argemone
plate: V
closed: '2026-09-11'
---

# phase-05 goals

_Stub written by the operator on 2026-09-05; rewritten by the phase-04 retro (joined from two reconcile runs) with the owner's decisions under Decisions._

**In one sentence: the garden runs in someone else's environment, not only in this one, and it can say what a merged task costs.** Phase 03 made the loop leaveable and phase 04 gave it its features and made the leaveability mechanism true; phase 05 is about adoption: a team points it at a project they already have, on models and machines they already pay for, and the tier map is set from cost per accepted task rather than from a price list.

## Owner scope update: AWS remote workers

2026-09-07: Bring remote AWS workers into phase05 now, without waiting for a failed local stabilization attempt. CG216 portable protocol and CG345–348 provisioning, execution, Spot recovery, cost/control work are included. Preserve the pluggable host lifecycle for non-garden dev hosts and existing PR221. Model pools/PR222 and other phase06 features remain deferred. The existing stabilization evidence remains required; remote execution can contribute to proving it. See [EC2 spec](../phase-06/specs/ec2-workers.md). This supersedes remote-worker deferral below.

## Current priority: stabilization before expansion

Owner decision, 2026-09-06: complete and demonstrate the dependable core loop before starting additional features. [The stabilization gate](specs/stabilization.md) is mandatory for phase closure and phase-06 unfreezing. Onboarding remains the adoption demonstration. OpenRouter, remote workers, model pools, operating presets and Now consolidation are deferred; existing branches and PRs are retained. The earlier expansion goals below are historical intent, not permission to dispatch deferred work.

## Why this phase

A second team cannot use the garden today: setting it up means writing product.md, principles and the setup block by hand, its workers only run on the scheduler's own machine or over ssh from it, and every model call goes through two vendor accounts that both hit their quota on 2026-09-05. Phase 04 also left three numbers pointing the wrong way (hand merges 16 of 57, cost per easy task $5.04, first-pass approval 71 to 79%) and no metric that would tell a routing experiment apart from noise: sonnet halved the run price and did not lower the bill per task. And the security review of the phase-04 build found three new highs and three mediums in the worker fence, two of which block phase 04's close and the rest of which land here first.

## Goals

1. **Onboarding.** `garden onboard` and the `garden-onboard` skill read an existing project and its environment and draft the garden for it (CG-215). Its output passes `garden doctor` on a non-Python fixture with no hand edits, its planner runs in the scrubbed environment, and every draft it writes passes the approve gate.
2. **Deferred to phase 06 — any model, at the right price.** An OpenRouter harness with per-tier models and cost from the response (CG-213), as an adapter around an existing OpenAI-compatible CLI rather than a garden-owned tool-calling loop, routed by difficulty with failure-driven escalation and measured by cost per accepted task, per `specs/cost-aware-model-routing.md`. It dispatches only after the measurement in goal 5 has merged.
3. **Deferred to phase 06 — shared quotas.** A tier can name several harness and model options and dispatch spreads runs across them, skipping a paused or exhausted account and recording the member on each run (CG-230).
4. **Deferred to phase 06 — any machine.** Workers on independent remote hosts that claim runs over HTTP and push results back (CG-216); last in dispatch order, and its acceptance test is a named second team's machine if one exists, a throwaway host otherwise.
5. **What the phase-04 retro adds.**
   - *The numbers exist before the experiments.* Cost per accepted task and first-pass approval per model, tier and harness in `garden metrics`, the Costs page and the retro's Numbers; hand merges and tick duration in metrics and the rail; the retro captures its own walkthrough before the personas run and its Numbers section reads the operator ledger at `context-garden/docs/operator-spend.jsonl`.
   - *Trust, round three.* The planner and the synchronous kickoff run in the worker environment; a worker cannot rewrite state.json, a task file or the harness config dir without it being restored and attributed; notify.command runs scrubbed. These follow CG-239 and CG-242 from the reopen.
   - *One writer, no lost writes.* Task files get optimistic concurrency and a duplicate id is a validate problem, not a fatal exception; retro-filed drafts reserve ids that cannot collide; every status write goes through `_transition` (Scheduler.mark_done and unapprove exist, with a source-grep test); Mark done honours the base-branch rule.
   - *Every PR reaches the queue.* Any PR with no review recorded for its head is queued on the next tick, on every runner (widen CG-236); resume means the same on the manual runner; a review whose head moved is discarded and a review whose task went terminal is cancelled.
   - *Briefs are right the first time.* No brief ships with an empty or unresolved reading list; inlined files come from the task's base, not a dirty worktree; a revise brief restates the criteria and the concrete blocker; dependent tasks are sequenced at planning; retro evidence is inlined; a missing or false criterion is a mechanical changes_requested.
   - *Hand steps become commands.* redispatch kills the superseded worker; pin runs the canary, installs and restarts after a tick; a reopen verdict carries through approve, dispatch and close without hand steps (CG-250).
   - *The surfaces say one thing.* One word for the operating point and stops that name a tier per harness; no task ids in copy; one needs-you predicate; a draft's criteria and reading list editable inline; the scaffolded operate skill, design.md, roadmap.md and the architecture map match the product.

## Non-goals

- Hosted or multi-user operation of the garden itself.
- New UI beyond what the goals need; TUI parity tasks are not filed by default.
- A garden-owned tool-calling loop for OpenRouter; the 20 to 50 task evaluation corpus in the routing spec is phase 06.
- Changing the operating point (workers, tier map) before cost per accepted task can be read.
- A cap on the drafts a retro files (the owner's decision: every finding at its severity, pruned at approval).

## Definition of done

Owner decision, 2026-09-07: named external-project adoption and external maintainer acceptance are removed from phase-05 requirements. The repeatable onboarding/useful-change fixture remains required; all other stabilization, recovery, cost and quality gates remain unchanged.

The required application journey, repeatable non-Python onboarding/accepted-change demonstration, four-hour productive run without required human-owner action (delegated operator actions allowed), resource evidence and intervention accounting in `specs/stabilization.md` must pass. Neither merged task count nor unit-test success can substitute.

Measured with `garden metrics` against phase 04, by the tool, not by hand.

- A non-Python fixture project is onboarded to a passing `garden validate` and `garden doctor` with no hand-written files.
- Deferred to phase 06: one task each completes through OpenRouter and a remote worker. Phase 05 instead requires the repeatable onboarding and sustained-operation evidence in specs/stabilization.md.
- Cost per accepted easy task at or under $4 (phase 04: $5.04) and first-pass approval at or above 90% (phase 04: 79% easy, 71% medium), both reported per model, tier and harness; the sonnet-era figures from the phase-04 operator retro are the baseline.
- Hand merges zero on every tier and runner (phase 04: 16 of 57); agent rebase rounds per merge under 0.3 (phase 04: 0.55, with 1.02 mechanical by design).
- A phase-05 walkthrough committed by the retro before the personas run; tick duration and hand merges visible in the rail and in metrics.
- No task reaches ready or a run without Scheduler.approve on any surface; no brief ships with an empty or unresolved reading list; no status assigned outside `_transition` (a source-grep test).
- The security persona's three phase-04 highs closed (CG-239, CG-242 and the planner) and its three mediums closed or reworded in the goals as accepted risk; no new high.
- The retro's Numbers section reports the operator's spend and share from the ledger; operator share below phase 04's 29%.
- Every task through `garden tick`; exceptions listed in the closing document.

## Decisions

- **Does the reopen carry all three blocking items, or only the brief-gate closure, with the two security fixes moved to phase 05 as its first tasks?** — answered: All of them. With the user's standing authority: CG-238 is merged and CG-239 is in review, so the reopen carries both; nothing moves to phase 05. Astra's reconcile has since filed CG-240 to CG-247 as further blocking items; which of those block and which become phase-05 follow-ups is settled by the joined retro. (by cli at 2026-09-05T23:43:16+00:00)
- **Joined retro on astra's CG-240 to CG-247:** CG-242 (hold a config reload while an in-flight worker's fence manifest disagrees) joins the reopen as its third blocker; CG-240 and CG-241 are duplicates of CG-238 and CG-239 and are cancelled; CG-243, CG-244, CG-245, CG-246 and CG-247 move to phase 05 and dispatch first, in that order.
- **Is phase 05 about adoption or about cost per accepted task?** — answered: Adoption is the headline (CG-215, CG-213, CG-230, CG-216). Cost per accepted task is measured from the phase's first task as a prerequisite, not the headline. (2026-09-05T23:45Z)
- **How many drafts may a retro file, and at what severity?** — answered: Every finding is filed as a draft at its severity, no cap. The kickoff and the operator prune at approval; a finding that is not worth a task is cancelled with a reason, not dropped silently. (2026-09-05T23:45Z)
- **Phase-05 numbers** — answered: at most $4 per accepted easy task and at least 90% first-pass approval, measured per accepted task, from the sonnet-era baseline. (2026-09-05T23:45Z)
- **Decisions made in the owner's name in phase 04** — answered: ratified: automerge by merge commit, review.max_rounds 4, reviews on the easy tier, the codex tier map luna/terra/sol. The eight queue-rotation hand merges were a bug (CG-176), not a policy. (2026-09-05T23:45Z)
- **Where the operator ledger lives** — answered: one ledger at `context-garden/docs/operator-spend.jsonl`, product and phase attribution welcome. The tool's default path must follow. (2026-09-05T23:45Z)
- **CG-206** — answered: cancelled; browser notifications first, unattended delivery to a phone parked. (2026-09-05T23:45Z)
- **Open:** whether codex stays in bypass-permissions mode once CG-239 and CG-242 land; whether a self product's second approving round should be a persona or a person rather than the same reviewer twice.

## Carried over from phase 04

Blocking the phase-04 close: CG-238 (merged), CG-239 (PR #193, in revise), CG-242 (draft). Moved here from astra's blocking set, first in dispatch order: CG-243 task-file concurrency, CG-244 retro id reservation and duplicate ids as a validate problem, CG-245 the planner in the worker environment, CG-246 worker writes to state.json, task files and the harness config dir, CG-247 Mark done through `_transition`. Follow-ups filed by the retro, refiled once as CG-251 to CG-299 (the two reconcile runs had drawn ids from one counter): brief completeness and revise briefs, planning sequencing and retro evidence, one writer for status, docs drift, one vocabulary, the walkthrough renderer and check retry on a signal exit, per-phase persona runs and run-id validation, acceptance evidence enforced at review, harness failures classified from structured errors, obsolete reviews cancelled, typed check continuations, a scheduler interface and a module-size test, browser-driven tests for notifications and kickoff, and the small items (retro_question kind, backlog noscript, the ambient config dir in tests, a second opinion for self products). Drafts already here: CG-213, CG-215, CG-216, CG-230, CG-236, CG-237 (merged as PR #191), CG-250; CG-222 sits in phase 06. Cancelled: CG-206, CG-240, CG-241. Exceptions for the phase-04 closing document: sixteen hand merges (eight from the queue-rotation bug), reviews to the easy tier at 14:40Z, mediums to sonnet at 14:50Z, automerge_method merge, review.max_rounds 4, codex in bypass-permissions mode, CG-189 redone as CG-225, CG-234's first run killed by hand, four persona runs discarded and restored by hand after CG-237, and the retro branch's drafts refiled by hand as CG-251 to CG-299.

## Features for the next phase

- CG-215: Onboarding: garden onboard drafts a garden from an existing repository (the headline)
- Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs page and the retro (CG-251)
- Widen CG-236: every PR with no review recorded for its head is queued on the next tick, on every runner
- The retro captures its own walkthrough, hand merges and tick duration are in metrics and the rail, and the Numbers section reads the product's ledger (CG-253)
- redispatch kills the superseded worker, and pin runs the canary, installs and restarts after a tick (CG-254)
- Operating-profile stops name a tier per harness, one word for the operating point, and user-facing copy drops task ids (CG-255)
- A draft's acceptance criteria and reading list can be edited inline on the task page (CG-256)
- CG-230: A tier can name several harness and model options, after the measurement lands
- CG-213: OpenRouter as an adapter around an existing CLI, after the measurement lands
- CG-216: Workers on independent remote hosts, last

## Open

- **Goal 2: any model routed by difficulty with failure-driven escalation**: No task owns difficulty routing or the failure-driven escalation policy (retry at a higher tier on failed verification, per the spec's phase-1 acceptance); CG-213 is the harness, CG-230 is pooling, CG-251 is measurement, and no escalation code exists.

## Completion organization

[Grouping policy](completion-tracks.md): group only unstarted work with a coherent shared deliverable. In-flight implementation, PRs, reviews, revisions, and recovery work are excluded. The previously proposed four tracks are withdrawn.

## Owner acceptance of stabilization evidence, 2026-09-10

Josh explicitly accepted the stabilization evidence: "i'm happy with the stabilization evidence, but we'll still need closing review". This is owner acceptance of the phase stabilization evidence, not a new test run or a claim that every historic metric passed. Do not require another stabilization run for phase closure. CG-423 is the sole unfinished Phase-05 task as verified at this decision. Once it merges, perform the closing review and address its blocking findings before closing Phase 05. Do not close the phase automatically on merge alone. Preserve original failures, intervention records and measured evidence in the closing account.

## Owner authorizes retro task approval and post-closure release, 2026-09-10

Review and approve eligible new tasks created by the Phase05 closing retro through the normal brief and phase gates, resolving routine gaps and duplicate findings while preserving explicit holds. After the closing review passes, blockers are resolved and Phase05 is actually closed, create and publish a new version and release from the accepted merged source. Preserve exact-source validation, CI, independent review, truthful release notes and existing active work. Live canaries are optional. This authorizes release publication after closure, not premature phase closure or any extra fleet spending/extension.
