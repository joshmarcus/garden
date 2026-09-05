# Phase 03 operator retro

Written by the operator (Claude, acting with the user's authority) on 2026-09-05 at the end of
the phase. The phase ran from 03:22 to about 06:10 UTC, overnight, with the user asleep after
04:00. Companion documents: `../retro.md` (the reconciled retro from `garden retro`),
`../reviews/` (persona reports), `../walkthrough/` (the pages as they were), `../friction.md`.

## In one sentence

The loop can now be left running for an hour at a time; it cannot yet be left running for a
night, because every new mechanism shipped this phase surfaced one more way the loop needs a hand.

## Numbers against the definition of done

| measure | goal | phase 02 | phase 03 |
|---|---|---|---|
| conflict rounds per merge | < 0.2 | 0.59 | 0.48 (13 in 27 merges); after the pin moved at 05:00, 15 of 19 rebases were mechanical and cost $0 |
| description-only rounds | 0 | 12 | 3, all applied as reviewer rewrites, no revise run |
| first-pass approval | >= 90% | 83% | 93% (26 of 28 first verdicts) |
| cost per easy task | <= $4 | ~$6 | $4.39 mean (15 done); medium $6.63; hard $12.20 |
| no module over 800 lines | 0 | 4 | 1: `cli.py` at 1995 lines was outside the split's scope |
| no subprocess-driven tests; QA green | yes | no | in-process runner merged (CG-152); `garden qa --scripted` merged and scheduled in CI (CG-135, CG-169) |
| trust items merged | 3 | 0 | 5 (CG-154, CG-164, CG-165) |
| config live within a tick | yes | partly | unchanged: budgets and `max_parallel` are live, everything else needs a restart |

Run cost for the phase: about $171 across 98 runs (work $119, review $35, revise $15, rebase $1).
Total garden spend passed $770 at 05:45.

## What the phase set out to do, and did

The split (CG-137, fable, alone, 15 minutes) landed as pure movement with a method-parity check
by the reviewer. Every later task touched the new small modules, and the reviewer never asked
for a description again. Rebase became its own mode (CG-141): mechanical first, an agent only
on a conflict, at the easy tier regardless of the task's own; the merge queue rebases once
right before a merge and keeps the verdict when the diff is unchanged. State stopped clobbering
concurrent writes (CG-153). Freeze became phase state (CG-148). Trust closed at the edges
(CG-154): feedback only from trusted authors, a scrubbed worker environment, sanitised HTML,
an origin check. Zombie run records get closed (CG-144), parked tasks un-park themselves
(CG-170), a merged parent retargets its children before its branch goes (CG-173), attaching a
PR by hand resets the cache (CG-174), a finished task drops its stop (CG-175).

## What needed a hand, in order

1. **03:41 hard-tier merges.** Four PRs (CG-137, CG-152, CG-135, CG-154) needed a person because
   `automerge_tiers` stops at medium. Each was checked by hand: a scratch merge of main plus
   the branch, lint, the suite.
2. **04:00 main went red.** I merged CG-152 by hand 24 seconds after automerge landed CG-145.
   Each was green alone; together a test called a helper the other had deleted. Every branch
   parked; three workers filed the same fix as drafts; CG-134 spent a revise round on a CI
   failure that was main's. Fixed by hand in eleven minutes (PR #104). Rule learned: a PR's
   green CI is against the main of its last push, not the main it lands on. The merge queue
   now tests the rebased head before merging, which closes this.
3. **04:12 parked tasks did not un-park.** The `base_broken` stop was correct, but nothing
   re-probed the base when it went green; `retry` would have spent a revise run at the task's
   tier (fable for CG-154). Rebased both by hand, pressed `resume`, filed CG-170. Merged by 04:47.
4. **04:29 a merged parent's branch deletion closed its stacked child's PR.** Automerge deleted
   CG-148's branch before `_restack` retargeted CG-161; GitHub closed #108 and the poll failed
   the task. Restoring the branch did not let GitHub reopen the PR; a fresh PR was needed, and
   then the poll kept reading the cached old PR number (CG-174) until state was edited under
   the lock between ticks. Filed CG-173; merged by 04:57.
5. **04:32 a task fell back to `ready` with its PR open** because its work run had finished
   and its review run was the only active record ("no active run found"). `garden pr` put it
   back. The poll had dispatched a review under a running revise; filed as CG-177.
6. **04:48 and 05:04 review-cap cards on rebases.** Rebase rounds counted as review rounds
   until CG-139 merged at 05:47; each card was cleared with `resume` or one more `review`.
7. **05:00 the pin moved** (aac0c28 to 51ed711) after twelve behaviour-changing merges. The
   restart lost one review verdict that the old server had reaped in its last tick (CG-150);
   a fresh review fixed it. Workers survived, as they did in phase 02.
8. **05:37 the merge queue rotated instead of merging.** With eight approved PRs, each tick
   rebased a different head, the force-push restarted that PR's CI, the pending rollup dropped
   it from the queue, and nothing merged for ten minutes. Merged the eight by hand with scratch
   merges (558 to 584 tests each). Filed CG-176 at priority 0; it is the last task of the phase.

Roughly twenty-five hand actions in three hours, against about a hundred in phase 02's day.
Almost all of them were the loop's new mechanisms meeting a case their tests did not cover,
and each is now a task or a merged fix.

## What the loop did well

- Every worker finished its task; no run hit the turn cap; no worker wrote outside its worktree.
- Stacking on the split branch worked: five dependents started the minute the split's PR
  opened, and all five restacked onto main cleanly when it merged.
- The reviewer's parity check on the split (145 methods before and after, 47 tests) was the
  kind of review a person would not have done at 03:40.
- Discovered work was judged within minutes: eight drafts approved with a dependency on the
  task that found them, nine cancelled with a reason (six were duplicates of one red-main fix).
- After the pin moved, four conflicts were resolved by easy-tier rebase agents for $1.12 in
  total, and fifteen rebases cost nothing.

## What to change

- **Merge queue stickiness (CG-176) and no review under a running task (CG-177)** before phase 04 opens many PRs at once.
- **Hard tier still needs a person to merge.** Either let the queue merge hard-tier PRs after
  two approving rounds, or make the scratch-merge check the queue's own step so a person's
  merge adds nothing. The user should decide this one.
- **Ticks now take a minute** because the queue runs the suite inside the tick before each
  merge and each mechanical rebase. Move checks out of the tick (a check run record, like a
  review) so the poll stays fast.
- **`cli.py` needs the same split** as the scheduler and web app: 1995 lines, and every CLI
  task will collide there.
- **A restart loses in-flight reaps.** The last tick's verdicts should be re-read from the run
  records on start, not only from state.
- **Parallelism stayed at 5.** Raising it would have raised the cascade, not the throughput;
  with CG-176 in, 7 is worth trying in phase 04, whose tasks touch separate pages.

## For the user in the morning

- Nothing is waiting on you. Phase 03 closes once CG-175 and CG-176 merge; phase 04 starts
  from its stub goals plus the retro's draft.
- Decisions I made with your authority that you may want to revisit: hand-merging eight
  approved PRs when the queue rotated; cancelling CG-171 (new-task must keep working during a
  freeze so friction can be filed); filing CG-162 and CG-163 (your two morning requests) in
  phase 04; leaving hard-tier merges manual.
