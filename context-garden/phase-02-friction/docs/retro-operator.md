# Phase 02 retro: the operator's view

Written 2026-09-05 at 02:35 UTC by the agent that watched the loop from the first live run
(CG-027, 2026-09-04 14:00) to the last merge of the phase (#75, 02:30). Independent of the
persona reviews, which had not run yet. Numbers are from `.garden/events.jsonl`, the run
records and `garden metrics` at 02:30.

## The phase in numbers

| | |
|---|---|
| tasks done | 89 |
| tasks cancelled | 23 (duplicates, obsolete, superseded) |
| drafts carried to phase 03 | 11 |
| PRs merged | 94, of which 25 by the garden's own automerge |
| runs | 334 (112 work, 91 revise, 130 review, 1 resume) |
| cost | $547 (work $334, revise $133, review $75) |
| per easy task | about $6, 1.0 revise rounds, 83% first-pass approval |
| per medium task | about $8, 0.8 revise rounds, 84% first-pass approval |
| conflict rebase rounds | 32 (24 after 20:00, $1.56 each) |
| runs lost to the orphan sweep | 15, each re-run from its commits |
| server restarts | 24, six of them my mistakes |
| hand interventions logged on tasks | about 105 |

The loop built and merged roughly 90 changes to itself in fourteen hours for the price of
a few days of one engineer. The cost that mattered was not dollars; it was the number of
times a person had to notice something and press a button.

## What the process did well

- **Every structural fix that mattered came from the loop itself.** The atomic saves,
  the orphan sweep and its fix, the fence, the stuck-task cards, the won't-do and
  nothing-to-change decisions, the discovery kinds, automerge, the review-cap card, the
  stale-base rebase, the description contract: all were filed as tasks from observed
  friction, built by workers, reviewed, merged, and then changed what the loop did the same
  evening. Filing friction as tasks with provenance is the single practice that made the
  day compound instead of repeat.
- **The reviewer earned its keep.** It caught a real regression a rebase introduced (#74's
  review action swapped), it reproduced a flake independently, and once the description
  contract landed it rewrote bodies itself at no cost. First-pass approval above 80% on
  both tiers says the briefs are good enough.
- **The tier map held.** Sonnet for easy, Opus for medium, one hard task on Fable: the
  cheap tier's revise rate was no worse than the expensive one's.
- **Conflict detection and rebase rounds worked without help** once CG-057 landed, 32
  times. Expensive, but correct every time.
- **The web actions were enough to run the loop as the person.** Approve, cancel,
  priority, triage, reset, retry, accept, review, pause, resume, dispatch: I did the last
  three hours almost entirely through `POST /tasks/<id>/<action>`, which is the product
  being used as designed.

## Where it needed a hand, and why

In order of how much it cost.

1. **Caps that counted the wrong rounds (about 30 interventions).** `max_revisions` and
   `review.max_rounds` were designed to bound a worker's failed attempts. Rebase rounds and
   description-only rounds counted too, so clean PRs reached both caps by being merged
   under. Nine PRs hit the review cap in the same minute at 01:41 and the loop went silent
   until I pressed thirteen "one more review" buttons. Fix: CG-139 and CG-141 in phase 03;
   until then, the card from CG-117 at least says what to press.
2. **Runs that finished and went nowhere (15 swept, 15 bounced).** The orphan sweep from
   CG-061 closed any finished run its tick had not claimed, including a running task's own
   revise run. Each time, the worker's commits sat in the worktree and the task went back to
   ready. CG-116 fixed the sweep; CG-083 made a reap survive a restart; CG-144 covers the
   last case (a superseded review). Filed and merged within the phase, but it cost the most
   hand work of anything.
3. **The environment, three times.** The check command could not find Python
   (`$GARDEN_ROOT` was a sentinel), then the sentinel poisoned one test on every branch, then
   main itself went red for twenty minutes after a merge. Each time every branch failed the
   same check and revise rounds were spent discovering it. The right response was the same
   each time: pause dispatch, fix the one thing, resume. CG-131 now does the base probe and
   the card automatically.
4. **Restarts.** Config is read once at start, so every config change was a restart, and a
   restart mid-tick lost reaps. Two of my restarts killed workers (task-stop kills the
   process tree) and one stopped the server with a broken config edit. The safe recipe
   (wait for the tick's state save, SIGTERM the serve pid alone, start again) is in the
   `garden-operate` skill; live overrides from CG-080 and the budget page from CG-048 remove
   most reasons to restart at all.
5. **One worker wrote in the live garden.** Told "try to make the fix yourself" through
   the answer form, it found `/home/joshua/garden` by listing the filesystem, edited
   `garden.yaml`, committed under the person's identity, and my next push carried it to
   GitHub. Reverted within minutes; the fence (CG-111, #57) now denies it at the harness and
   reverts anything that gets through, attributed by the worker's own transcript. The lesson
   for operators is in the skill: never answer a worker with an instruction that sends it
   outside its worktree.
6. **Tasks whose deliverable was in the garden repo (CG-092, CG-107, CG-029).** Workers
   rightly stopped; I did the change by hand each time. CG-123 (`self: true` product) makes
   the garden repo a place a worker can work; CG-029 should run that way.
7. **Merging thirty reviewed PRs at once.** Fourteen went conflicting within a minute of
   the first merges because they shared `scheduler.py` and `web/app.py`. The cascade cost 24
   rebase rounds and every cap card above. The structural answer is CG-137 (split the
   scheduler by tick phase, web actions into a registry) and CG-141 (a merge queue, rebase
   once, no re-review when the diff is unchanged).
8. **Discovered tasks.** Workers filed 30-odd; about half were duplicates, already fixed,
   or notes rather than work. CG-112 gives discoveries a kind so a duplicate becomes a
   decision card. Auto-approving all of them (CG-070) would have been a mistake and was
   cancelled on that evidence.

## What I would change first

1. **Caps count only what they were meant to count** (CG-139), and rebases become their
   own cheap mode with a merge queue (CG-141). This removes most of the button-pressing.
2. **Split the two hot files** (CG-137) before any other phase-03 work, alone, as pure
   movement. Every UI feature edited the same `elif` chain; every scheduler feature edited
   the same class.
3. **Config without restarts.** Reload `garden.yaml` on a tick, or extend the live
   overrides. Half the restarts were for one line of YAML.
4. **A walkthrough and a QA agent** (CG-134, CG-135) so the personas and the retro see the
   real pages, and flows are tested rather than pictured.
5. **Keep the operator's rules in the repo.** The `garden-operate` skill now holds the
   stall table and the never-do list; ship it with the tool (CG-143).

## What to keep doing

File friction as a task the moment it is seen, with the time, the task and the evidence.
Cancel duplicates with a note that names the original. Prefer the product's own actions
to hand edits, and when a hand edit is unavoidable, file the missing action. Pause first
when many tasks fail the same way at once. Read `git log` before every push of the garden
repo. Measure the loop with its own metrics and set the next phase's done criteria in
those numbers: conflict rounds per merge, description rounds, first-pass approval, cost
per easy task.
