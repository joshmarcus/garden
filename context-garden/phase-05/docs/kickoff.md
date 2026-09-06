# Kickoff: context-garden/phase-05

_2026-09-06T00:07:47+00:00 · hard tier (claude-opus-4-8)_

**Verdict:** not ready yet

The reopen blockers are in motion (CG-243/244/245 running, CG-239 in review), but the phase is not ready to approve its headline work. Two reopen blockers, CG-246 and CG-247, carry no acceptance criteria or reading lists and cannot pass the approve gate, and each duplicates a follow-up draft (CG-291, CG-292/CG-282). The OpenRouter headline (CG-213) needs one design decision — which CLI/adapter and whether it is a new harness or codex+base_url — before it or CG-230 can be built. Goal 2's failure-driven escalation has no owning task. And the drafts need the pruning the owner's own rule expects: the config-reload-hold is filed twice (CG-242 vs CG-288) and ~30 vocabulary/trust/mark_done drafts overlap running or blocker tasks. Once CG-246/247 get briefs, the OpenRouter shape is settled, and the duplicates are pruned, the phase is ready to take runs on its adoption goals.

## Design needed

- **OpenRouter harness shape and adapter CLI** — CG-302 [draft, spike]
  - Goal 2 mandates an adapter around an existing OpenAI-compatible CLI (not a garden-owned loop), but CG-213's body still leaves built-in-loop vs adapter open and names no concrete CLI, while the spec frames it as the codex harness pointed at OpenRouter; whether it is a new `harnesses.openrouter` or codex+base_url is unsettled and shapes the fake stub and the member syntax CG-230 reuses.
  - blocks: CG-213, CG-230
  - spike: Pick the concrete adapter (a named CLI, or codex exec with an OpenRouter base_url) and whether it is a distinct openrouter harness or codex configured with base_url; define fake_openrouter.py's request/response contract and GARDEN_RESULT parsing.
- **CG-246/CG-247 blocker briefs and overlap with CG-291/CG-292** — CG-303 [draft, spike]
  - Both reopen blockers are back to draft with no acceptance criteria and empty reading lists so they cannot pass the approve gate, and their scope duplicates follow-up drafts CG-291 (worker fence/config dir) and CG-292/CG-282 (mark_done/unapprove via _transition).
  - blocks: CG-246, CG-247, CG-291, CG-292, CG-282
  - spike: Complete CG-246/CG-247 criteria and reading lists and fold or cancel CG-291 and CG-292/CG-282 so each fix has one owner.

## Goals without a measurable outcome

- **Goal 2: any model routed by difficulty with failure-driven escalation** — No task owns difficulty routing or the failure-driven escalation policy (retry at a higher tier on failed verification, per the spec's phase-1 acceptance); CG-213 is the harness, CG-230 is pooling, CG-251 is measurement, and no escalation code exists. (added to goals.md under '## Open')

## Questions for the owner

- **Do a named second team and repository exist for CG-215 and CG-216 acceptance, or are fixtures/a throwaway host the claim?** — decision card `20260906T000310Z-kickoff-q0`
  - Goal 1 and Goal 4 acceptance both hinge on 'a named second team's machine if one exists, a throwaway host otherwise'; it changes what done means and is already open in the goals.
  - options: A named team/repo is the acceptance target, Fixtures/throwaway host are the acceptance claim
- **Is the config-reload-hold shipped as reopen blocker CG-242 or as follow-up CG-288, given they are the same fix?** — decision card `20260906T000310Z-kickoff-q1`
  - The joined retro made CG-242 the third reopen blocker while CG-288 refiles the identical fix as a phase-05 follow-up; keeping both risks two workers on one change.
  - options: Ship CG-242 as blocker, cancel CG-288, Ship CG-288, drop the blocker framing
- **Which of each near-duplicate draft pair ships, so the approve queue can be pruned before dispatch?** — decision card `20260906T000310Z-kickoff-q2`
  - Per the prune-at-approval rule, several fixes are covered by both a running/blocker task and a follow-up: planner-env (CG-245 vs CG-271/CG-290), concurrency+dup-ids (CG-243/CG-244 vs CG-289), inline criteria editing (CG-256 vs CG-284), and vocabulary where CG-296 subsumes CG-255,257-263,266-270,285-287.
- **Does codex stay in bypass-permissions mode once CG-239 and CG-242 land?** — decision card `20260906T000310Z-kickoff-q3`
  - Listed open in the goals; both retro judges asked and it sets the fence's threat model for the remaining trust tasks.
  - options: Keep bypass-permissions, Drop it
- **Do a named second team and repository exist for CG-215 and CG-216 acceptance, or are fixtures/a throwaway host the claim?** — answered: No named team or repository yet. Fixtures and a throwaway host are the acceptance claim until the owner names one; the goals text says so. CG-215 is built against a fresh clone of a public, well-documented repository; the day a real repository is named, onboarding it becomes the phase's exit criterion (operator, per the retro answer of 2026-09-05). (by cli at 2026-09-06T00:19:17+00:00)
- **Is the config-reload-hold shipped as reopen blocker CG-242 or as follow-up CG-288, given they are the same fix?** — answered: CG-242 ships as the reopen blocker (its work run is in flight); CG-288 is cancelled as the same fix. (by cli at 2026-09-06T00:19:17+00:00)
- **Which of each near-duplicate draft pair ships, so the approve queue can be pruned before dispatch?** — answered: One owner per fix, pruned at approval with a reason: CG-243/CG-244 (running) own concurrency and duplicate ids, CG-289 cancelled; CG-245 (running) owns the planner environment, CG-271 and CG-290 cancelled; CG-242 owns the reload hold, CG-288 cancelled; the worker-fence and mark_done fixes keep one owner each after the operator compares CG-246/CG-247 with CG-291/CG-292/CG-282; CG-256 owns inline criteria editing, CG-284 cancelled; CG-296 owns vocabulary and lists the items it subsumes, which are cancelled with that reason. (by cli at 2026-09-06T00:19:18+00:00)
- **Does codex stay in bypass-permissions mode once CG-239 and CG-242 land?** — answered: Keep bypass-permissions until CG-242 lands (CG-239 is merged), then return codex to sandboxed execution with .git writes in its own worktree and network for gh allowed, and annotate the change on the costs page (decided 2026-09-05 on the owner's instruction). (by cli at 2026-09-06T00:19:18+00:00)

## Docs that need attention

- **`docs/architecture.md`** — CG-304 [draft]
  - Module map omits kickoff.py, scheduler/kickoff.py, profiles.py, runner/ssh.py, runner/manual.py and web/pages/api.py; CG-216 must add the remote runner and runs API to an already-stale map.
  - needed by: CG-216, CG-295, CG-275
- **`docs/worker-protocol.md`** — CG-305 [draft]
  - Line 68 already says 'Remote runners skip this; the host makes its own' though runner: remote and the claim/heartbeat/finish flow do not exist yet; a dangling forward reference CG-216 must reconcile.
  - needed by: CG-216
- **`docs/design.md`** — CG-306 [draft]
  - design.md and roadmap.md still list 'automatic merging' as a non-goal though the loop automerges; stale.
  - needed by: CG-295, CG-265, CG-275
