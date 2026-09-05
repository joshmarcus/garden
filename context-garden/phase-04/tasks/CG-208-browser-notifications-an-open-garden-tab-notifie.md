---
id: CG-208
title: 'Browser notifications: an open garden tab notifies through Chrome when a decision appears, with
  a one-time permission toggle and one notification per tick'
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 1
difficulty: medium
reading:
- src/garden/web/templates/base.html
- src/garden/web/pages/api.py
- src/garden/inbox.py
- src/garden/events.py
- src/garden/web/pages/inbox.py
branch: garden/cg-208-browser-notifications-an-open-garden-tab-notifie
pr: https://github.com/joshmarcus/context-garden/pull/132
attempts: 1
last_dispatched_at: '2026-09-05T12:04:39+00:00'
created: '2026-09-05T10:36:25+00:00'
updated: '2026-09-05T12:04:39+00:00'
---

## Goal

With the garden open in a browser tab, even a background one, the person gets a Chrome notification when the loop needs them: a worker's question, a won't-do or nothing-to-change card, a discovered-work decision, a review or revision cap, a broken base, a stall, a retro verdict or question, a phase closing. Clicking the notification opens the task or phase it is about. Notices (merges, dispatches, progress) do not notify.

## Context

The user on 2026-09-05, asked which channel `notify.command` should use to reach them: "Let's start with just chrome notifications." Nothing server-side is needed for that: the Web Notifications API works from an open tab (background tabs included) once the person grants permission, and Chrome on Windows shows them as system notifications. The Inbox already separates decisions from notices (CG-096) and counts only decisions in the rail badge; the event log has the kinds. `notify.command` (CG-155) stays available for teams that want a channel; CG-206 (configure it in the live garden) is cancelled in favour of this.

## Design

- `GET /api/decisions?since=<iso>` returns the decision-kind events since a timestamp (kinds: `question`, `decision`, `needs_human`, `discovered` with a decision, `retro_done`, `phase_closed`, `retro_question`), each with task or phase, a one-line title, and the URL to open.
- `base.html` gets a small script: it polls that endpoint every 30 seconds (or on the page's existing refresh), coalesces new items into one notification per poll ("3 decisions need you: CG-201 asks a question, …"), uses a `tag` so repeats replace rather than stack, and opens the URL on click. It runs only when `Notification.permission` is `granted`.
- A toggle in the rail (no Set button, CG-190 rule): "Notify me in this browser". Turning it on calls `Notification.requestPermission()`; the state lives in `localStorage`; the toggle shows "blocked in browser settings" when permission is denied.
- One notification per tick at most; nothing on page load for decisions that already existed; the last-seen timestamp is kept in `localStorage`.

## Acceptance criteria

- [ ] The endpoint returns decision events since a timestamp with title and URL, and nothing for notices; a test covers each decision kind.
- [ ] With the toggle on and permission granted, a new decision produces one Chrome notification within a poll interval, clicking it opens the task page; a test drives the script with a fake `Notification` in the in-process test app (or a scripted QA flow in `garden qa`).
- [ ] The toggle works without a page reload, shows the blocked state, and the page renders identically with JavaScript off.
- [ ] The walkthrough's rail shows the toggle.

## Log

- 2026-09-05T10:36:27+00:00 approved (web)
- 2026-09-05T11:51:26+00:00 dispatched work run 20260905T115118Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou stacked on CG-197, ~13188 tokens)
- 2026-09-05T11:55:55+00:00 parent CG-197 merged; will rebase onto main when the current run finishes
- 2026-09-05T12:00:18+00:00 parent CG-197 merged; rebased onto main and retargeted the PR
- 2026-09-05T12:01:30+00:00 opened https://github.com/joshmarcus/context-garden/pull/132 (base main): Added GET /api/decisions (decision-kind events → title+URL, notices dropped) and a rail 'Notify me in this browser' toggle with a 30s poll that fires one coalesced, tagged Chrome notification per interval and opens the task/phase on click. Server side is fully tested; the JS is progressive enhancement verified structurally. cost=$3.29
- 2026-09-05T12:04:23+00:00 automated review requested changes: Server side (endpoint + mapper) is correct and well-tested, but the untested client re-fires a notification for the most-recent decision on every 30s poll because /api/decisions is inclusive of `since` and the client stores SEEN as the last event's timestamp. cost=$0.76
- 2026-09-05T12:04:39+00:00 dispatched revise run 20260905T120439Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~14711 tokens)
