# Operator handoff for this garden (written 2026-09-06 12:40Z by the Claude operator session)

You are the operator of the context-garden loop running from this directory. Read
`.claude/skills/garden-operate/SKILL.md` first: it is the operator's manual (status, inbox,
decisions, restarts, cost). This file is the live handoff: what is true right now and what to do next.

## Standing orders from the owner (Josh)

- Act with the owner's authority: approve tasks, merge PRs, answer decision cards, file gaps as
  tasks at once. Keep developing without stopping. The owner ratifies your decisions.
- Keep the operator thread cheap: observe with `garden status`, `garden inbox`, `garden digest
  --since 25m` every 25 minutes; batch actions; record your spend (`python3 tools/operator_spend.py`
  appends to `context-garden/docs/operator-spend.jsonl`; Claude sessions only, extend it for Codex).
- Reviews run one rung above the writer (the ladder in `review.ladder`, CG-320, merged 11:57Z but
  not yet in the pinned build). Retros and persona judges run on the best model (claude fable via
  `harnesses.claude.retro_model`; flip `review.harness` to `"claude"` for a retro window).
- Design work is an invitation, not a prescription; acceptance criteria are outcomes with
  evidence, optional, never refused for naming a file (principles/00-index.md).
- Priority 1 is the Now page: Now 1 (Fable's design, PR #218) and Now 2 (astra's, PR #227, see below); then the loop-quality tasks filed last night.

## State at 12:58Z (after the tmpfs restart)

- Phases 01–04 closed. Phase 05 open: ~19 done, 25 ready, several in revise; $340 spent.
- `garden.yaml`: default harness codex (luna/terra/sol by tier), `review.harness: codex`,
  `review.difficulty: hard` (every review on sol until the ladder is pinned), `max_parallel: 5`
  (this 7 GB, 16-CPU box thrashes above 6 because every check builds a venv and runs the full
  11-minute suite; checks and reviews take dispatcher slots, CG-329), check timeouts 1500 s.
- Service: `systemctl --user` unit `garden-serve.service` (linger on). Restarting it kills
  in-flight checks, which then read as failed checks: restart only when no check is running,
  then `garden resume <id>` any task that lost one. Pin: b72dbcc since 12:55Z (ghost-record fix, task-page card, Inbox layout, UI captures
  check, review ladder, worker temp under the work root, design serving are live). To move it again:
  `chmod -R u+w .venv/bin .venv/lib && .venv/bin/pip install --force-reinstall --no-deps
  "context-garden[dev,plates] @ git+https://github.com/joshmarcus/context-garden@<sha>" &&
  chmod -R a-w .venv/bin .venv/lib`, then restart, then update the sha in CLAUDE.md.
- /tmp is a 3 GB tmpfs again (WSL restarted ~12:52Z); dispatch was unpaused at 12:58Z; the five runs in flight at the restart died and were reaped by the new build.
- Worker temp: CG-310 points TMPDIR under `/home/joshua/work/tmp`, which is now a symlink to
  `/tmp/garden-work` on the tmpfs (fast, cleaned per run). Keep it that way or amend CG-310.

## Open PRs and what to do with them

- #227 CG-309 Now 2 build: NOT merged after all (conflicts with main after the 12:30Z merges; the `gh` merge printed a checkout hint). Rebase in `/home/joshua/work/worktrees/CG-309` onto origin/main, push with `--force-with-lease`, `garden set-status CG-309 in_review`, merge. Its open finding (goals show 'Progress not mapped') is in CG-334.
- #218 CG-308 Now 1 build: held on a rebase conflict in `src/garden/web/templates/_runs.html`
  (Now 1's live-clock block vs main's card changes). Resolve in the worktree
  `/home/joshua/work/worktrees/CG-308` (`git rebase origin/main`, keep both), push with
  `--force-with-lease`, `garden set-status CG-308 in_review`, `garden review CG-308`, merge.
  Its one open finding (operator-only periods render empty) is in CG-334.
- #216 CG-215 onboarding: HOLD LIFTED by Josh in the Codex operator session on 2026-09-06. Actively revise, review and land it. Address the findings about deriving conventions and provenance; do not reinstate the old hold.
- #221 CG-216 remote workers and #222 CG-230 pools: held, conflicts with main, requested changes.
- #223 CG-324 required evidence: held; a failed persona run would strand the review forever.
- Merged by hand 12:30–12:40Z with reviewer findings still open: #226, #212, #214, #217.
  CG-334 (p1) closes those findings.

## Recipes that were needed repeatedly last night

- A run that ends "successfully" with no GARDEN_RESULT but commits in its worktree (Fable waiting
  for a background test run): `git -C <worktree> push --force-with-lease origin HEAD`,
  `garden set-status <id> in_review`, `garden review <id>`. CG-333 automates this.
- "base branch main is itself broken" with a probe that shows exit 127, SIGTERM or a timeout:
  a load casualty, not a break. `garden retry <id>`. Main passed 1042 tests at 04:30Z.
- "automerge held: the diff touches guarded paths": approved and green, merge by hand with
  `gh pr merge <n> --merge --delete-branch`.
- "4 automated review rounds used": `garden review <id>` for one more, or `garden resume <id>`
  if the last verdict approved.
- A no-change accepted on a revise round lands in waiting_human with no question (CG-328):
  `garden set-status <id> in_review` (or `ready` if it has no PR) and continue.
- A task parked by a harness pause stays ready after the pause lifts (CG-332): `garden
  dispatch <id>`.
- Do not commit to this garden repo while a claude/fable run is in flight until CG-327 lands:
  the fence charges the window's commits to the worker and discards its run.
- Codex workers cannot see pages; the Edge-through-WSL capture recipe is in
  `context-garden/product.md` ("Looking at pages"); captures go to the Windows temp then are
  copied into the worktree.

## Where things are

- Task files: `context-garden/phase-05/tasks/`; specs: `context-garden/phase-05/specs/now-page.md`.
- Retro artefacts for phase 04: `context-garden/phase-04/docs/` (retro.md joined, retro/comparison.md).
- Mocks served locally: http://localhost:8766/now-1/now-1.html and /now-2-mock/now-2.html
  (a `python3 -m http.server 8766` over `/home/joshua/work/design-mocks`; `fuser -k 8766/tcp` to stop).
- The Claude operator's memory (for a Claude session): `~/.claude/projects/-home-joshua-context-garden/memory/`.

## Codex operator update, 2026-09-06 13:21Z

Josh explicitly authorized resolving all attention cards and improving broken process by manual fixes or filed tasks. Do not ask him to interpret routine scheduler states. CG-337 changes no_change into evidence reconciliation and makes true decision cards explain outcomes and consequences. CG-335 covers temp-symlink recovery; CG-336 covers Codex spend attribution (usage unavailable until supported; never substitute Claude usage).

The server remains the existing systemd garden-serve.service. The Codex heartbeat `operate-context-garden` runs in the operator task every 25 minutes; no second server. A service drop-in `~/.config/systemd/user/garden-serve.service.d/worker-temp.conf` creates `/tmp/garden-work` at startup. The missing tmpfs target was restored and its 17 failed dispatches requeued.

All eight initial attention cards were acted on: CG-216/230 returned for substantive revisions; CG-293 resumed after vanished temp fixtures; CG-330 requeued with its interrupted edits preserved in the named worktree stash `operator-recovery-20260906-CG330` and restoration instructions in the task; CG-322/326 approved with clarified briefs; CG-319 approved for evidence-based combination after both builds merge under delegated authority. CG-324's empty question was stale state while pre-PR check 20260906T131533Z-check was running; reconciled to running, preserving the check. Now 1 CG-308 had no live rebase despite a running label; recovered to in_review and started review 20260906T132111Z-review. Neither Now PR was merged at that point. Verify all of this against live state at the next check-in.

## Resource relief override, 2026-09-06 13:27Z

Josh reported high load. Dispatch is paused while existing work drains; the live max_parallel override is now 2. Do not restore 5. The running service and all workers in its cgroup have a temporary systemd runtime CPUQuota=200% and CPUWeight=20, verified via cpu.max=200000 100000; no process was killed or restarted. review_parallel cannot be changed through garden set in this build, so it remains configured at 3.

At the next check-in inspect live workers/checks, memory, swap activity and /tmp space before resuming. Resume dispatch only after the active work drains to at most two workers and temp space has headroom; retain the two-worker limit and CPU cap while assessing stability. The 3GB tmpfs was already 2.2GB full with per-run pytest directories, mostly active. Never delete active-run temp directories. If pressure remains, keep paused and fix the underlying admission/temp problem. The CPU cap slows tests, so distinguish throttling timeouts from code failures.

## Authoritative stabilization policy, owner approved 2026-09-06

This supersedes earlier priority lists. Phase 05 is now a stabilization/adoption milestone governed by `context-garden/phase-05/specs/stabilization.md`. Phase 06 is frozen. CG-213, CG-302, CG-216, CG-230, CG-319 and CG-283 were moved there as drafts; preserve their branches and draft PRs, do not retry/approve/review/merge them until the stabilization gate passes. Onboarding stays active. Already-running bounded work may finish.

First priority: honest no_change/decision handling (CG-337), resource admission (CG-338/329/335), and preserved recovery work (CG-330), with other safety/stability fixes behind them. CG-339 adds actual-application review evidence; CG-340 demonstrates independent-project adoption; CG-341 implements mechanical soak recording and phase-close evidence enforcement. These tasks being merged is not proof that the actual milestone passed. Run the stabilized installed build for eight productive hours with at least ten representative completed tasks, recording every intervention and resource measurement; perform isolated recovery exercises and browser journeys. Real-user adoption needs a named project and acceptance; fixtures only establish fixture compatibility. Missing evidence is UNPROVEN, never pass. Do not unfreeze phase 06 or close phase 05 without the required evidence or a new explicit owner exception.

Apply actual-application review policy to relevant pending PRs and track failures; screenshots alone do not prove an interaction. Record all findings but defer unrelated scope rather than automatically expanding the milestone. Do not claim automatic code enforcement until CG-339/341 are installed and verified.

Dispatch resumption on this pinned version uses POST http://127.0.0.1:8765/resume with a loopback Origin header; `garden resume` requires a task id and is NOT the global resume command. Keep max_parallel=2 and the runtime CPU cap during stabilization.
