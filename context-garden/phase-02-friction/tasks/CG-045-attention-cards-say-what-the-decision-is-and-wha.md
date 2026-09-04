---
id: CG-045
title: Attention cards say what the decision is and what each button will do
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/inbox.py
- src/garden/web/templates/task.html
- src/garden/scheduler.py
branch: garden/cg-045-attention-cards-say-what-the-decision-is-and-wha
attempts: 1
last_dispatched_at: '2026-09-04T17:38:14+00:00'
created: '2026-09-04T17:21:39+00:00'
updated: '2026-09-04T17:52:15+00:00'
---

## Goal

When the loop stops for a person, the card and the task page say what decision is being asked, what each button will actually do, and give enough context to decide, including a way to hand the decision to a chat session.

## Context

Reported during CG-027 by the person driving the run. The Inbox showed, for CG-027: "Needs a decision: revise run 20260904T170828Z-revise produced no change to the diff. Fix or decide, then continue the loop." with buttons "Continue the loop", "Cancel task" and "PR". Their words: "it's not clear what buttons are explicitly about making the decision, and I want more context or the ability to chat about the decision."

What was true underneath: the stall was a false alarm (CG-038), the PR was clean and mergeable, and there was nothing to fix. The card offered no way to say so: the person could only start the work over, cancel, or work around the garden by merging on GitHub and waiting for the poll. That workaround is not an answer; the card needs a "nothing to fix, resume" action, and the false stall itself should not fire. "Continue the loop" runs `garden retry`, which resets attempts and marks the task ready, so for a task with an open PR it starts the work over; the card does not say so. `needs_human` is a free-text reason set in several places (`_stall`, the revision cap, a closed stack parent, a failed worker), so the card cannot know which decision it is asking.

Make `needs_human` structured: a kind (stall, revision cap, parent closed, worker failed, env error) plus the reason. For each kind the card shows: what happened in one sentence, what the options are and what each does ("Continue the loop: resets attempts and starts a fresh work run on this branch"), and the evidence (last run, last review, the diff summary, the PR state). Add a "Discuss" action that copies a ready-made prompt with the task id, the reason and the links, for pasting into a chat session or `garden take`. Show the same on the task page.

## Acceptance criteria

- [ ] every button on an attention card has a one-line description of its effect next to it.
- [ ] the card names the kind of decision and shows the evidence for it.
- [ ] a "Discuss" action produces a prompt with the task, the reason, the PR and the run ids.
- [ ] a "Nothing to fix, resume" action clears `needs_human` and returns the task to the state it held before the stop (awaiting_triage or in_review) without starting a run; no card sends the person to GitHub to resolve a garden-side flag.
- [ ] tests for the card content per kind.

## Log

- 2026-09-04T17:24:00+00:00 approved (web)
- 2026-09-04T17:38:14+00:00 dispatched work run 20260904T173814Z-work via local [claude model=sonnet] (fresh session, base main, ~7108 tokens)
- 2026-09-04T17:52:15+00:00 attempt 1 failed: worker exited 1: worker error: error_max_turns; will retry
