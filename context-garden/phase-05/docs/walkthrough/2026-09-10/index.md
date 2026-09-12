# Walkthrough of the live web app — context-garden/phase-05, 2026-09-10

Screenshots were not captured (no browser was available). Each page below has its purpose, one line on what to look at, the served HTML and a plain-text rendering (tags stripped, in document order) that reads roughly as the page does top to bottom.

Read the `.txt` for the words and the order; read the `.html` for structure, controls, forms, empty states and error text.

Run page stderr is omitted (rerun `garden walkthrough` with --include-stderr to capture it); absolute home-directory paths are redacted to `~` throughout.

## Inbox: `/` (HTTP 200, 200 KB)

The first page: everything that needs the operator now.

Look at: Can a person immediately tell what needs action?

Files: `inbox.txt`, `inbox.html`

## Now: `/now` (HTTP 200, 137 KB)

What is running, what is next, where the phase is and the last period, live from the events stream.

Look at: Can you say what the garden is doing and what comes next within five seconds?

Files: `now.txt`, `now.html`

## Board (columns): `/board` (HTTP 200, 173 KB)

The board in columns, one per status in the loop's order.

Look at: Do the columns read left to right as the loop moves work?

Files: `board.txt`, `board.html`

## Board (list): `/board?view=list` (HTTP 200, 161 KB)

The board as a list grouped by status, with a per-state fact on each row.

Look at: Does each row say enough to act without opening the task?

Files: `board-list.txt`, `board-list.html`

## Backlog: `/board?view=backlog` (HTTP 200, 131 KB)

The backlog view of work that is not yet ready to run.

Look at: Can you see what is waiting for approval or dependencies?

Files: `backlog.txt`, `backlog.html`

## Trellis: `/trellis` (HTTP 200, 280 KB)

The dependency and stacking graph with growth-stage glyphs and the hide-done control.

Look at: Can you follow what blocks what, and what the glyphs mean?

Files: `trellis.txt`, `trellis.html`

## Phase: `/phases/context-garden/phase-05` (HTTP 200, 746 KB)

The phase page: goals, the task table, budget and cost, persona reviews.

Look at: Is the important thing (what needs you) above the fold?

Files: `phase.txt`, `phase.html`

## Task: `/tasks/CG-215` (HTTP 200, 115 KB)

A task page: state, tier and priority controls, runs, the live log, the actions.

Look at: Are the controls and the run history legible, and is it clear what happens next?

Files: `task.txt`, `task.html`

## Run: `/runs/CG-215/20260906T161350Z-check` (HTTP 200, 69 KB)

A run page: the transcript, the brief, the final message and stderr.

Look at: Can you tell what the worker did and why it ended as it did?

Files: `run.txt`, `run.html`

## Runs: `/runs` (HTTP 200, 1376 KB)

Every run with its cost and tokens.

Look at: Is cost easy to total and attribute?

Files: `runs.txt`, `runs.html`

## Costs: `/costs` (HTTP 200, 102 KB)

Spend and accepted-task outcomes by activity, tier, model and harness.

Look at: Can you read what an accepted task costs and which route produced it?

Files: `costs.txt`, `costs.html`

## Herbarium: `/herbarium` (HTTP 200, 74 KB)

A plate per phase; closed phases live here.

Look at: Does a closed phase read as a finished, catalogued thing?

Files: `herbarium.txt`, `herbarium.html`

## Closed phase: `/phases/context-garden/phase-01-bootstrap` (HTTP 200, 82 KB)

A closed phase's header: the record of what it did, with no working controls.

Look at: Is it obviously a record, not a live board?

Files: `closed-phase.txt`, `closed-phase.html`

## Config: `/config` (HTTP 200, 78 KB)

Configuration: pause and resume, live overrides, the tier map.

Look at: Are the live controls and their effect clear?

Files: `config.txt`, `config.html`

## Trials: `/trials` (HTTP 200, 75 KB)

The model leaderboard from every trial.

Look at: Does the ranking say which model to pick and why?

Files: `trials.txt`, `trials.html`

## Events: `/events` (HTTP 200, 184 KB)

The event timeline.

Look at: Can you reconstruct what happened from the timeline alone?

Files: `events.txt`, `events.html`

## Retro: `/phases/context-garden/phase-05/retro` (HTTP 200, 68 KB)

The phase retrospective, persona reports and filed follow-ups.

Look at: Can you see what the phase learned and what it carries forward?

Files: `retro.txt`, `retro.html`
