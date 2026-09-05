_Persona: product-manager (vision report, a one-off run on claude-fable-5-1 from the persona file, product.md, both retros, the phase-04 drafts and the walkthrough; 2026-09-05 10:20 UTC). The findings-style review is in product-manager-2026-09-05.md._

# Product manager: vision and features for phase 04

## 1. Vision

context-garden turns a repository of written intent into merged pull requests while the person who wrote it is away, and asks that person only for the decisions a person must make.

Three phases from now, "done" looks like this. A developer or a small team points the garden at their repository, writes principles and a phase, approves the planner's tasks from the Inbox, and closes the laptop. In the morning the board shows merged PRs, the Inbox shows only real decisions, and nothing has stalled that a tick could have handled: checks, rebases, merges at every tier, restarts and config changes all happen without a hand. A manager opens the phase page and sees cost per task, cost per phase and progress against the goals without reading a transcript. The retro reads its own inputs, delivers a verdict, files the next phase's tasks and features, and the owner's job is to edit that list rather than write it. The product runs on the team's own machine or one shared server, under the team's own review rules and CI, and the plain interactive session is what you fall back to for the one task in twenty that the loop hands back.

## 2. Where we are

Phase 03 did what it promised and nothing it did not: no user-visible feature, hand actions down from about a hundred to about thirty, first-pass approval at 93%, five trust items merged, and every new stall filed or fixed by the end of the day. The promise holds for an hour and not a night: the tick now runs the test suite in-process so "every action waits on the hub lock the tick holds", hard-tier PRs and a rotating queue accounted for twelve hand merges, a restart still loses the last tick's verdicts, and live config reload did not ship. Phase 04 inherits a clean scheduler and web split that makes each of those fixes small, a cli.py at 1,995 lines that makes every CLI feature collide, and an Inbox that reads "13 need you" where all thirteen are phase-04 drafts waiting on the owner.

## 3. Features for the next phase

Ranked by user value per unit of cost. The first five finish the phase-03 promise; the last three are the features the personas and the stub asked for. Items 1, 7 and 8 already exist as drafts and need only the notes below folded in.

### 1. The tick never blocks the UI: checks and pre-merge rebases run as records, actions do not wait for a tick (CG-182, priority 0)

Today a button press on the Board or Inbox waits up to a minute while the queue runs the suite inside the tick, and the operator turned the in-tick test check off to cope, so the queue now merges without its own check and CI is the only gate. The user value is the whole promise: an operator who cannot press "resume" without a minute's freeze goes back to sitting with the loop. Make a check and a pre-merge rebase a run record like a review, dispatched on one tick and reaped on a later one, and let web actions take a short lock of their own so a tick and an action never share one. Add tick duration to the report so the regression is visible next time. Size: hard. Depends on nothing; the scheduler split and the run-record machinery from CG-141 and CG-144 make it a movement of existing code. Ship it first and alone, as CG-137 was.

### 2. The merge queue merges hard-tier PRs after its own scratch-merge check and a second approving round, as a config choice

Twelve of about twenty-five hand actions in phase 03 were merges of approved, green PRs, because `automerge_tiers` stops at medium and the operator's check was a scratch merge of main plus the branch, lint and the suite. That check is mechanical; make it the queue's step, so a person's merge adds nothing, and let a hard-tier PR merge when the rebased head passes it and the review has approved twice. Keep the default off and name the setting so a team can hold hard-tier merges for a person. Size: medium. Depends on item 1 (the check as a run record) and on CG-176 and CG-177, both merged. The owner decides the policy; see question 1.

### 3. Split cli.py by command family before any CLI-touching task runs

`cli.py` is 1,995 lines, the one module still over the phase-03 limit, and three of phase 04's filed features (CG-156 help and vocabulary, CG-158 manual-task ergonomics, CG-162 move a task) all land in it. Left as is, they will collide the way the scheduler did in phase 02 and spend rebase rounds. Do it the way CG-137 was done: pure movement, one module per command family, a method-parity check by the reviewer, dispatched alone and first among the CLI work. Size: easy to medium. Depends on nothing; blocks CG-156, CG-158 and CG-162.

### 4. Every garden.yaml key reloads within one tick, and the Config page says which values are live

Goal 6 promised a config change without a restart and shipped only budgets and `max_parallel`. Every other change (tiers, automerge, notify, trusted authors, setup commands) still needs a restart, which in phase 03 cost a review verdict, and the walkthrough's Config page still tells the user to edit YAML and restart. Reload on modification time at the top of the tick, log the keys that changed as an event, refuse a file that fails to parse and keep the last good one, and rewrite the Config page copy to state what takes effect and when. Size: easy to medium. Depends on nothing; a prerequisite for item 2's setting to be turned on without a restart.

### 5. On start, the scheduler re-reads finished-but-unreaped runs of every mode, and a canary tick checks a new pin before the loop trusts it

The 05:00 pin move lost a review verdict the old server had reaped in its last tick, and the WSL outage was survived only because the dead runs were retried by hand. A restart should walk the run records for every mode (work, review, rebase, check, persona, retro), reap anything finished and unreaped, and only then tick; and the pin should move only after one tick on a scratch copy of state passes. Take the canary half of CG-180 into this task and leave the fake-GitHub latency modelling for later. Size: medium. Depends on item 1 for the check mode; the reap side can ship before it.

### 6. Approve refuses a task with placeholder acceptance criteria or unresolved reading paths, and the Inbox card shows the gap

Half of phase 03's friction was tasks approved with placeholder criteria and reading lists that pointed at files the split had moved, and the walkthrough shows how little the approve card gives the owner to judge by: CG-162's card reads "planned, not yet approved · ] Tests cover the CLI and the web action, including both refusals." with the criteria's leading bracket leaking into the summary. Validate at approve time in the web action and the CLI: every acceptance criterion non-empty and not the planner's template text, every reading path present at the target checkout; show a red line on the card and refuse until fixed, or allow with a stated override. Size: medium. Depends on nothing; prerequisite for CG-179 (results and reviews speak to each criterion by name), which should not be filed until this merges.

### 7. The retro ends in a verdict and has a page: close the phase, close with follow-ups, or reopen; the page shows the reconciled document, the operator retro, persona reports with scores and the tasks it generated (CG-178 and CG-146, filed as one dependency chain)

Phase 03 closed by hand: the operator wrote the phase-04 goals from a stub, decided the phase was done, and filed the retro's findings as drafts. The retro already reads the reports it waited for (CG-145) and the product-manager persona now produces the features list (CG-181), so the verdict is the missing last step, and the page is where a manager sees a phase's outcome without opening `docs/`. Ship CG-178 first with the verdict as phase state next to freeze (CG-148), then CG-146 reading that state, and let CG-181's features section feed the next phase's stub. Size: medium each. Depends on CG-181 for the features section and on the freeze-as-state structure already merged.

### 8. The web UI can create a task from a form, with the same fields as garden new-task (CG-132)

This is the feature deferred twice; the Inbox card still says "back to draft: approved by mistake during the phase 02 freeze; carried into phase 03". A new user in week one writes their first task in the browser, not the CLI, and today the Inbox's "Suggest a change" and "Report friction" forms exist but "add a task" does not. Same fields as the CLI, the same validation as item 6 at the form so a placeholder cannot be created from here, and the task lands as a draft in the chosen phase. Size: easy. Depends on item 6 for the validation and on the actions registry, already merged. Keep the form working during a freeze, as the cancelled CG-171 asked, so friction can still be filed.

## 4. Not now

- **Backlog view with drag to reorder and move across phases (CG-163).** Defer to phase 05. CG-162 gives the move as an action on the task page and the CLI; a drag surface is the same feature with a client-side layer we have no JS test infrastructure for. File it after CG-162 has been used for a phase and we know whether reordering by hand is a daily act or a monthly one.
- **Plates content (CG-030) and the seedling mark in the header (CG-183).** Decline for phase 04. Both are herbarium look, which phase 03 declared a non-goal and which no user or persona report raised as a reason to stop using the product. They are easy, but easy is not the ranking; keep them as drafts and pick them up when a phase has slack.
- **Fake GitHub latency and base-branch deletion modelling (the first half of CG-180).** Defer. The two real defects it would have caught (CG-173, CG-176) are merged with tests of their own, and the canary tick in item 5 covers the pin-move risk. Model the fake when the next merge-queue defect appears, not before.
- **Raising parallelism to 7, and hosted or multi-user operation.** Not features. Try 7 as a config change once item 1 has merged and the tick is fast again, and revert if the cascade returns. Multi-user stays a non-goal until a second team exists to ask for it.

## 5. Questions for the human

1. **Hard-tier merges.** Should the queue merge hard-tier PRs at all? If yes, is the bar a second approving round plus the queue's own scratch-merge check, or the check alone? Item 2 is written for the first; a "no" makes it a smaller task that only adds the check.
2. **A structure gate at the start of phase 04.** Phase 03 dispatched nothing until the split merged. Do you want the same rule for items 1 and 3, so no feature is dispatched until the tick is unblocked and cli.py is split? It costs about a day of feature work and saves the collisions and freezes we just measured.
3. **Budget and the overnight test.** The garden has spent $791 since the start; phase 03's runs cost about $189. What is phase 04's cap, and is the definition of done "one night unattended with zero hand actions", measured by leaving it running from midnight with the laptop on AC?
4. **Can the retro close a phase without you?** Item 7 lets the retro's verdict freeze and close a phase. Should "close" always wait for your approval in the Inbox, or only "reopen"?
5. **The decisions the operator made in your name** that phase 04 should either ratify or undo: the eight hand merges when the queue rotated, cancelling CG-171, filing CG-162 and CG-163 in phase 04, and leaving hard-tier merges manual. The last one is question 1; the other three need a yes or no in the closing document.
