# The Now page: what is happening, what comes next, how far we are

_Requested by the owner on 2026-09-06 00:52Z: "a 'what's happening now' operational dashboard, a real gem for the entire experience and demo. Beauty and data visualization are key. A page for what's currently running and what's coming next; it highlights where we are (the current phase) and provides metrics for the last period of time; it creates a real sense of movement and progress. Throw serious design resources at this."_

## What it is for

One page a person keeps open on a second screen or shows in a demo. In five seconds it answers: what is the garden doing right now, what will it do next, where is the product in its phase, and how did the last hour or day go. It should feel alive: runs start, advance and finish in front of you without a reload, and the phase's progress is visible as growth, not as a table.

## Content, in order of prominence

1. **Now.** Every run in flight: task id and title, mode (work, revise, review, rebase, check, persona, edit, retro, kickoff, trial), harness and model, elapsed time against the run's typical duration for its mode and tier, the last thing the worker said (its latest assistant text, one line), and spend so far. A run that has just finished stays for a beat with its verdict before it leaves. A held merge, a paused harness or a needs-you card is visible here, not hidden in the Inbox.
2. **Next.** The dispatch order as the scheduler will actually take it: ready tasks in priority order, PRs in the merge queue with their state (review round, CI, rebase), reviews waiting for a harness. Each item says why it is where it is (blocked by, waiting for, held on).
3. **Where we are.** The current open phase (or phases) with its plant at its growth stage, done against total, the phase's goals with a mark per goal for merged, in flight, not started, and the retro verdict if one exists. Closed phases are a row of specimens, the way the herbarium shows them.
4. **The last period.** Selectable window (last hour, today, last 24 hours, this phase): tasks merged, first-pass approval, cost by activity, cost per accepted task, hand steps taken, runs by harness and model, throughput as a sparkline or small multiples. Annotation marks for config changes and pins, as the Costs page has. Numbers come from `garden metrics` and the run records, never recomputed in the template.

## Motion and feel

- Live without a reload: server-sent events (the events endpoint already exists) drive the Now and Next lists; a new run slides in, a finished one settles and fades; the phase's plant advances when a task lands. No polling loop that re-renders the page.
- The page is the herbarium's: the plates, the plant glyphs, plain type, the paper ground, restrained colour used only for state (running, review, held, paused, failed). One accent for movement (the growing thing). No dashboard chrome, no card grid of equal boxes; the hierarchy above is the layout.
- Works at 1280 wide on a projector and on a phone in a column; dark mode follows the app.
- Empty and quiet states are designed: a garden with nothing running shows what it is waiting for and when the next tick is.

## Data and boundaries

- Read-only. The page reads state, run records, events, `garden metrics` and the phase tree through the existing store and scheduler surfaces; logic goes in a `now` module under `garden/` (or the scheduler's report helpers), the route and template stay thin, per the rules in CLAUDE.md.
- The "typical duration" and throughput figures are computed from run records in the window, per mode and tier; the module exposes them so the CLI (`garden now`) can print the same in text.
- Add nothing to the tick's critical path; the page must not hold the hub lock while it renders.
- Charts are server-rendered SVG like `charts.py`; the live parts are small DOM updates driven by events, not a front-end framework.

## Done means

- A person who has never seen the garden can say what it is doing and what is next within five seconds of opening `/now`.
- The page is the one to show in a demo and the one the operator leaves open; the Inbox and Board remain for acting.
- `garden walkthrough` captures it; the designer and usability personas review it before the phase closes.
