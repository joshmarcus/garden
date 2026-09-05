# product-manager review of context-garden/phase-03

**Persona:** product-manager · **Score:** 7/10 · 2026-09-05T10:17:53+00:00

Phase 03 kept its discipline: no user-visible feature, hand actions down from about a hundred to about twenty-five, first-pass approval at 93%, the trust items merged, and every remaining stall filed or fixed. It missed live config reload entirely, missed the conflict-rounds target, left cli.py at 1,995 lines, and shipped a merge queue whose in-tick checks now make the web UI wait a minute, so the promise to leave the loop running holds for an hour and not a night. Phase 04 should finish that promise first (checks outside the tick, hard-tier merges in the queue, restart-safe reaps, live config) and only then take the features, led by the retro verdict and the new-task form.

## High

- **operability** — The tick runs the product test suite in-process, so pages and button presses wait a minute and the operator turned off the pre-PR test check to cope.
  - suggestion: Ship CG-182 first in phase 04: checks and pre-merge rebases as run records reaped on a later tick, actions that do not share the tick's lock, and a tick duration in the report.
- **merge queue** — Twelve of about twenty-five hand actions were merges of approved green PRs because hard-tier PRs and a rotating queue still needed a person.
  - suggestion: Let the queue merge hard-tier PRs after two approving rounds and its own scratch-merge check, as a config choice the owner turns on.

## Medium

- **config** — Goal 6's live config reload did not ship; only budgets and max_parallel reload, and the Config page tells the user to edit YAML and restart.
  - suggestion: Reload garden.yaml on modification time at the top of the tick, log the changed keys, and rewrite the Config page copy to say which values are live.
- **recovery** — A restart or pin move loses a verdict the old server reaped in its last tick, and nothing checks a new pin before the loop trusts it.
  - suggestion: On start, walk run records of every mode for finished-but-unreaped runs; run the CG-180 canary before moving the pin.
- **planning** — Half the phase's friction is tasks approved with placeholder acceptance criteria and reading lists that point at moved files.
  - suggestion: Approve refuses or flags empty or placeholder criteria and unresolved reading paths, and the Inbox approve card shows the gap; this is a prerequisite for CG-179.

## Low

- **web UI** — A mechanical rebase run page reads '(no brief recorded) (no final message)', a merged task still shows 'automerge held: GitHub reports the PR unknown', and the Timeline digest repeats the review-cap card twenty times.
  - suggestion: Say 'mechanical rebase onto main, no model' on a no-cost rebase run, clear the automerge note on a terminal task, and collapse repeated cap cards in the digest.

_garden persona run 20260905T101440Z-persona_
