# Walkthrough of the live web app — context-garden/phase-03, 2026-09-05

Screenshots were not captured (Playwright is not installed (pip install 'context-garden[walkthrough]' && playwright install chromium).). Each page below has its purpose, one line on what to look at, the served HTML and a plain-text rendering (tags stripped, in document order) that reads roughly as the page does top to bottom.

Read the `.txt` for the words and the order; read the `.html` for structure, controls, forms, empty states and error text.

## Inbox: `/inbox` (HTTP 200, 88 KB)

What needs a decision and what is only a notice; the rail badge counts decisions only.

Look at: Is the split between a decision and a notice clear, and is the empty state designed?

Files: `inbox.txt`, `inbox.html`

## Board (columns): `/board` (HTTP 200, 73 KB)

The board in columns, one per status in the loop's order.

Look at: Do the columns read left to right as the loop moves work?

Files: `board.txt`, `board.html`

## Board (list): `/board?view=list` (HTTP 200, 70 KB)

The board as a list grouped by status, with a per-state fact on each row.

Look at: Does each row say enough to act without opening the task?

Files: `board-list.txt`, `board-list.html`

## Trellis: `/trellis` (HTTP 200, 91 KB)

The dependency and stacking graph with growth-stage glyphs and the hide-done control.

Look at: Can you follow what blocks what, and what the glyphs mean?

Files: `trellis.txt`, `trellis.html`

## Phase: `/phases/context-garden/phase-03` (HTTP 200, 122 KB)

The phase page: goals, the task table, budget and cost, persona reviews.

Look at: Is the important thing (what needs you) above the fold?

Files: `phase.txt`, `phase.html`

## Task: `/tasks/CG-125` (HTTP 200, 68 KB)

A task page: state, tier and priority controls, runs, the live log, the actions.

Look at: Are the controls and the run history legible, and is it clear what happens next?

Files: `task.txt`, `task.html`

## Run: `/runs/CG-125/20260905T053852Z-rebase` (HTTP 200, 51 KB)

A run page: the transcript, the brief, the final message and stderr.

Look at: Can you tell what the worker did and why it ended as it did?

Files: `run.txt`, `run.html`

## Runs: `/runs` (HTTP 200, 175 KB)

Every run with its cost and tokens.

Look at: Is cost easy to total and attribute?

Files: `runs.txt`, `runs.html`

## Herbarium: `/herbarium` (HTTP 200, 52 KB)

A plate per phase; closed phases live here.

Look at: Does a closed phase read as a finished, catalogued thing?

Files: `herbarium.txt`, `herbarium.html`

## Closed phase: `/phases/context-garden/phase-01-bootstrap` (HTTP 200, 63 KB)

A closed phase's header: the record of what it did, with no working controls.

Look at: Is it obviously a record, not a live board?

Files: `closed-phase.txt`, `closed-phase.html`

## Config: `/config` (HTTP 200, 52 KB)

Configuration: pause and resume, live overrides, the tier map.

Look at: Are the live controls and their effect clear?

Files: `config.txt`, `config.html`

## Trials: `/trials` (HTTP 200, 51 KB)

The model leaderboard from every trial.

Look at: Does the ranking say which model to pick and why?

Files: `trials.txt`, `trials.html`

## Events: `/events` (HTTP 200, 151 KB)

The event timeline.

Look at: Can you reconstruct what happened from the timeline alone?

Files: `events.txt`, `events.html`
