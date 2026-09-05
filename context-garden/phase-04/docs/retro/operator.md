# Phase 04 operator retro

Written by the operator agent (the Claude session that drove the loop) on 2026-09-05, before the
reconciled retro. Numbers from `garden metrics context-garden/phase-04`, the run records and
`tools/operator_spend.py --since 2026-09-05T10:30`. Three tasks (CG-212, CG-227, CG-235) were still
in the merge queue when this was written; the counts below treat them as done.

## In one sentence

Phase 04 turned the loop into something that ran unattended for most of a day, with a merge queue
that rebases and checks before it merges, config that changes without a restart, quota pauses,
model trials, retros that end in a verdict and a kickoff step, at $474 in runs and $195 of
operator time; what it did not do is bring hand merges or the cost of an easy task down.

## Numbers against the definition of done

| measure | goal | phase 03 | phase 04 |
|---|---|---|---|
| hand merges | 0 | 12 of 30 | 16 of 57: 8 in the 05:37 queue rotation (fixed by CG-176), the rest around a stacked branch (CG-189 into CG-178), the pin lagging main, and one manual-runner task (CG-030) |
| web action under a second during a check; tick under ten seconds | yes | no | yes since CG-182 (checks and rebases run detached); tick duration is not yet reported, the page stayed responsive all afternoon |
| garden.yaml live within a tick, Config page names the live keys | yes | partly | yes (CG-192): the tier map, review harness and model, retro difficulty and codex permission mode all changed during the day without a restart |
| no placeholder criteria or unresolved reading path dispatched | 0 | n/a | gate in place since CG-193; nothing refused after it landed |
| rebase rounds per merge, mechanical and agent apart | < 0.2 | 0.70 | 1.57 total: 1.02 mechanical, by design (the queue rebases every head before merging, at $0), and 0.55 agent (31 conflicts in 56 merges, $17.46 in all) |
| cost per easy task | <= $4 | $4.34 | $5.04 over 29 done: $3.67 in the opus era, $5.88 in the sonnet era (see below) |
| no module over 800 lines; cli.py a package | 0 | 1 | 0; the largest is `cli/loop.py` at 722 lines; `cli/` is a package (CG-197) |
| walkthrough: no Inbox fragment, no needs-you badge on a done task, a described rebase run | yes | no | CG-195 and CG-196 shipped these; the retro's walkthrough persona checks the pages |
| security persona's three high findings closed | 3 | 0 | 3 (CG-194): workers get a private HOME, retry_command comes only from config, the fence hash-checks garden.yaml and state.json |
| every task through `garden tick`, exceptions listed | yes | no | exceptions: CG-030 (manual runner, merged by hand), CG-189 (merged into CG-178's branch and dropped, redone as CG-225), the eight queue-rotation merges, CG-234's first run killed by hand |
| operator turns and spend recorded; operator share lower than phase 03 | yes | 50% ($190 of $379, 941 turns) | 29% ($195 of $669, 673 turns), recorded in `docs/operator-spend.jsonl` |

Per tier: easy 31 tasks, 0.32 revisions each, 79% first-pass approval, $146; medium 28 tasks,
0.86 revisions each, 71% first-pass approval, $328. Phase 03 had 93% first-pass approval.

## The spend cut, measured

At 14:50Z the user said tokens were going too fast. The tier map moved from opus 4.8 (medium) and
fable 5.1 (hard) to sonnet 5 for easy and medium, opus 4.8 for hard, and reviews to sonnet 5. The
hourly burn fell from about $114 to $20–34. Per completed task it did not fall:

| era | easy mean | medium mean | work run mean | review mean |
|---|---|---|---|---|
| opus (before 14:50Z) | $3.67 (16) | $10.97 (22) | $4.56 | $0.82 |
| sonnet (after) | $5.88 (12) | $10.62 (5) | $2.53 | $0.69 |

A sonnet work run is half the price of an opus one, but sonnet-era tasks needed more revise and
review rounds (CG-212 alone took six revisions and six reviews). The sample is small and the mix
differs (the sonnet-era easy tasks include the quota pause and the trial plumbing, which were not
easy), so the honest reading is: cheaper models cut the rate, not the bill per task, and the
first-pass approval rate is the number to watch in phase 05.

Codex, tried on four tasks: gpt-5.6-terra beat sonnet 5 in the CG-225 trial (9 to 7) for about
$1.01 against $5.03; astra beat sonnet on CG-158's material (8 to 6) at $3.77 against $4.41; CG-226
(easy, codex) was approved on the first round. Codex runs recorded no cost until CG-233 merged at
21:13Z, so the codex figures above are computed from usage by hand.

## What the phase set out to do, and did

- **The queue.** One head per tick, a mechanical rebase before every merge, the verdict kept when
  the patch id is unchanged (CG-210), checks as detached run records (CG-182), hard-tier merges
  after two rounds (CG-191), stacked children retargeted before a parent branch is deleted, a task
  done only when its commits reach the base branch (CG-228).
- **Live config** (CG-192) and named operating profiles from quiet to fast (CG-221), `garden
  observe` as a configurable operator feed (CG-219).
- **Trust** (CG-194, CG-200, CG-217): no HOME for workers, per-harness config dirs, DNS-rebinding
  resistance, opt-in bot trust.
- **Retros and phases**: a verdict at the end of every retro (CG-178), a Features for the next
  phase section fed by a product-manager persona (CG-181, CG-188), every persona finding kept as a
  draft (CG-187), questions answered as decision cards (CG-225, CG-226), a kickoff step before a
  phase starts (CG-224), retros on the hard tier by default (CG-207), a retro page (CG-146).
- **The UI**: a backlog across phases with drag and drop (CG-163), move a task between phases
  (CG-162), no Set buttons (CG-190), a costs page sliceable by activity, model and difficulty with
  annotation lines (CG-214), operator spend as an activity (CG-223), Chrome notifications for
  decisions (CG-208), a task form (CG-132).
- **Quota**: a spend-limit error pauses the harness and probes it back (CG-212), including the
  retro's own runs (CG-227).
- **Trials**: setup for contender worktrees (CG-229), `--wait` (CG-231), `--again` (CG-232), codex
  cost from usage (CG-233).
- **The README** rewritten as the front door, on fable (CG-234).

## What needed a hand, in order

1. 05:37Z the queue rotated heads and merged nothing for an hour; eight PRs merged by hand with
   scratch-merge tests. CG-176 fixed the rotation; CG-210 later fixed the verdict lost on rebase.
2. 05:59–09:31Z the WSL VM stopped (not this session's doing) and the garden slept for three and a
   half hours. `garden serve` is now a systemd user service with lingering on and the VM idle
   timeout off.
3. The tick held the hub lock while running the test suite, so every web action waited on it. The
   test check was turned off for two hours until CG-182 moved checks out of the tick.
4. 13:12Z a Claude spend limit failed twelve tasks in one pass; all retried by hand. CG-212 is the
   fix.
5. CG-194's private HOME logged every worker out; CLAUDE_CONFIG_DIR and CODEX_HOME in the service
   unit, then CG-217 for the default.
6. Codex under its sandbox could not write `.git` or reach the network; permission mode set to
   bypass. Its contender worktrees got no setup (CG-229). Relaunching a trial took eleven hand steps
   (CG-232).
7. CG-189 was marked done after merging into CG-178's branch, and its code was dropped before that
   branch merged. Cancelled, redone as CG-225 (which codex won), CG-228 for the state.
8. CG-178's revise pushed onto a rewritten branch; the worktree was reset by hand, CG-220 filed.
9. Restarts twice lost the last tick's reaped verdict; CG-198 covers it.
10. Trial winners never queue a review round (CG-225 and CG-030 each waited 45 minutes for a hand
    press); a manual-runner task ignores resume. CG-236 in phase 05.
11. Re-dispatching CG-234 from codex to fable without killing the codex process left two workers in
    one worktree; the first fable run waited on the other and ended without a PR ($4.34).

## What the loop did well

- 57 tasks in twelve hours with five workers, 41 of them merged by the queue without a hand.
- The pre-merge rebase and check meant main never went red in this phase.
- Live config let the spend cut, the review model changes and the codex settings happen mid-phase
  without a restart, and the trial mechanism gave a same-day answer on codex.
- Reviews caught real things: a criterion the code did not meet (CG-212, round 5, which turned out
  to be the criterion's wording), a README that described merging as automatic, a PR description
  narrating a bug that never existed.
- The operator's share of spend fell from half to under a third.

## What to change

- **First-pass approval is the cost lever.** Sonnet at 71–79% first pass costs as much per task
  as opus at 93%. Phase 05's routing work (CG-230, the cost-aware routing spec) should measure cost
  per accepted task, not per run, and the brief should carry the reviewer's usual findings
  (description scar tissue, criteria by name) so the first round passes.
- **Every path that produces a PR ends in the review queue**, including trial winners and manual
  tasks (CG-236). Resume, review and accept should mean the same thing on every runner.
- **Hand steps that recur become commands**: killing a superseded worker when a task is
  re-dispatched, moving the pin, freezing and closing with the retro verdict.
- **Report the tick duration** so the ten-second goal can be measured, not assumed.
- **Retros and judges on the best model, reviews on the review tier** (CG-235) so the tier map
  prices work and nothing else.

## For the user

Phase 04 is closed by its retro's verdict. Phase 05 (adoption: onboarding, any model, shared
quotas, any machine) has five drafts and a kickoff to run. The recommendation stands: run about
ten medium tasks on codex terra with claude reviews and compare cost per accepted task with the
sonnet baseline above.
