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

## State at 12:45Z

- Phases 01–04 closed. Phase 05 open: ~19 done, 25 ready, several in revise; $340 spent.
- `garden.yaml`: default harness codex (luna/terra/sol by tier), `review.harness: codex`,
  `review.difficulty: hard` (every review on sol until the ladder is pinned), `max_parallel: 5`
  (this 7 GB, 16-CPU box thrashes above 6 because every check builds a venv and runs the full
  11-minute suite; checks and reviews take dispatcher slots, CG-329), check timeouts 1500 s.
- Service: `systemctl --user` unit `garden-serve.service` (linger on). Restarting it kills
  in-flight checks, which then read as failed checks: restart only when no check is running,
  then `garden resume <id>` any task that lost one. Pin: 51f9928 (see CLAUDE.md); main is far
  ahead (ghost-record fix, task-page card, Inbox layout, UI captures check, review ladder,
  worker temp on disk, design serving). Move the pin at a quiet moment:
  `chmod -R u+w .venv/bin .venv/lib && .venv/bin/pip install --force-reinstall --no-deps
  "context-garden[dev,plates] @ git+https://github.com/joshmarcus/context-garden@<sha>" &&
  chmod -R a-w .venv/bin .venv/lib`, then restart, then update the sha in CLAUDE.md.
- Dispatch is PAUSED (`garden pause`, 12:25Z) for the owner's /tmp remount. `garden unpause`
  once the remount is done and `df -h /tmp` shows tmpfs.
- /tmp: was moved to disk at 01:49Z (tmp.mount masked); that made the suite 2.6x slower and
  is being reverted to a 3 GB tmpfs by the owner. CG-310 (merged) points worker TMPDIR under
  the work root on disk; amend it to `/tmp/garden/<run>` with the same per-run cleanup.

## Open PRs and what to do with them

- #227 CG-309 Now 2 build: NOT merged after all (conflicts with main after the 12:30Z merges; the `gh` merge printed a checkout hint). Rebase in `/home/joshua/work/worktrees/CG-309` onto origin/main, push with `--force-with-lease`, `garden set-status CG-309 in_review`, merge. Its open finding (goals show 'Progress not mapped') is in CG-334.
- #218 CG-308 Now 1 build: held on a rebase conflict in `src/garden/web/templates/_runs.html`
  (Now 1's live-clock block vs main's card changes). Resolve in the worktree
  `/home/joshua/work/worktrees/CG-308` (`git rebase origin/main`, keep both), push with
  `--force-with-lease`, `garden set-status CG-308 in_review`, `garden review CG-308`, merge.
  Its one open finding (operator-only periods render empty) is in CG-334.
- #216 CG-215 onboarding: HOLD (owner). Sol's last review: it does not derive conventions and
  can fabricate provenance; a revise on sol was in flight at 12:25Z.
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
