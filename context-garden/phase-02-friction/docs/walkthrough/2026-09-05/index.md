# Walkthrough of the live web app, 2026-09-05, end of phase 02

Captured from the running garden at 127.0.0.1:8765 as it was served, with the phase's real data: 89 tasks done, 94 PRs merged. HTML only: no screenshots, because the headless Chromium on this machine lacks system libraries (`libnspr4` and friends) that need an administrator to install. Each page below has its purpose, one line on what to look at, the served HTML and a plain-text rendering (tags stripped, in document order) that reads roughly as the page does top to bottom.

Read the `.txt` for the words and the order; read the `.html` for structure, controls, forms, empty states and error text.

## inbox: `/inbox` (HTTP 200, 84 KB)

The Inbox: what needs a decision and what is only a notice; the rail badge counts decisions only.

Files: `inbox.txt`, `inbox.html`

## board: `/board` (HTTP 200, 100 KB)

The Board in columns, one per status in the loop's order.

Files: `board.txt`, `board.html`

## board-list: `/board?view=list` (HTTP 200, 92 KB)

The Board as a list grouped by status.

Files: `board-list.txt`, `board-list.html`

## trellis: `/trellis` (HTTP 200, 153 KB)

The Trellis: the dependency graph with growth-stage glyphs and the hide-done control.

Files: `trellis.txt`, `trellis.html`

## phase: `/phases/context-garden/phase-02-friction` (HTTP 200, 260 KB)

The phase page: goals, the task table, budget, persona reviews.

Files: `phase.txt`, `phase.html`

## task: `/tasks/CG-111` (HTTP 200, 81 KB)

A task page: state, tier and priority pulldowns, runs, the live log, the actions.

Files: `task.txt`, `task.html`

## run: `/runs/CG-111/20260905T022217Z-revise` (HTTP 404, 0 KB)

A run page: transcript, brief, final message and stderr tabs.

Files: `run.txt`, `run.html`

## runs: `/runs` (HTTP 200, 142 KB)

All runs with cost and tokens.

Files: `runs.txt`, `runs.html`

## herbarium: `/herbarium` (HTTP 200, 50 KB)

The Herbarium: a plate per phase; closed phases live here.

Files: `herbarium.txt`, `herbarium.html`

## config: `/config` (HTTP 200, 52 KB)

Configuration: pause and resume, live overrides, the tier map.

Files: `config.txt`, `config.html`

## trials: `/trials` (HTTP 200, 51 KB)

Model trials.

Files: `trials.txt`, `trials.html`

## events: `/events` (HTTP 200, 145 KB)

The event timeline.

Files: `events.txt`, `events.html`

