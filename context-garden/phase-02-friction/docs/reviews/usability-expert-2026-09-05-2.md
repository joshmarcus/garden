# usability-expert review of context-garden/phase-02-friction

**Persona:** usability-expert · **Score:** 6/10 · 2026-09-05T03:03:34+00:00

The phase shipped real usability wins: attention cards that name the decision and describe each button, won't-do decision cards, flash messages instead of 500s, per-run transcript pages, a Board list view, and the discuss prompt. But the two surfaces a person meets first still mislead them. On the captured Inbox, thirteen of the fourteen 'need you' items are drafts the operator already deferred and the one task that needs a person is filed under 'no action needed'; in the CLI a new user following the Quick start can dispatch a paid worker on a template-bodied draft with no warning, doctor ends with 'see above' instead of a fix, and the notification hook the phase built is documented nowhere a new user can find it. Done tasks keep live state-changing controls, transcript rows are cut at 160 characters with no way to expand, and 64 flat commands hide inbox at position fifty.

## High

- **Inbox count** — Thirteen of fourteen 'need you' items are drafts already deferred by the freeze, while the manual close-the-phase task that does need a person sits under 'Auto-retrying, no action needed'.
  - suggestion: Count a draft as a decision only until it has been acted on once (deferred or given a target phase), and classify runner:manual tasks as decisions, never as retries.
- **First run** — garden dispatch starts a real paid worker on a draft whose body is still the scaffold template, with no warning and without --force.
  - suggestion: Refuse drafts without --force and have dispatch, approve and validate flag bodies that still contain the scaffold placeholders.
- **Discoverability** — The notify hook is undocumented in this repo (README, docs, init template) and doctor only says 'notify: not configured'.
  - suggestion: Restore the notify: block to the README config sample and the garden init template, and make doctor's line name the key to set and the env vars the command receives.

## Medium

- **Doctor** — A missing git identity is reported in red and the run ends with 'see above' and no command to fix it.
  - suggestion: Print the two git config commands and end doctor with the first failing check's fix instead of 'see above'.
- **Task page actions** — Done and cancelled tasks still show reset-revisions, submit-on-change tier and priority pulldowns, persona review and suggest controls.
  - suggestion: Hide state-changing controls on terminal tasks and require an explicit apply for the pulldowns.
- **Run page transcript** — Tool results are truncated at 160 characters with no expansion and rate_limit_event renders as a bare word.
  - suggestion: Make each transcript row expandable to its full text and render rate-limit events with what happened and how long the wait was.
- **CLI help and status** — garden --help is 64 ungrouped commands with inbox at position fifty, and garden status at 80 columns truncates every header to two letters with two both reading 're…'.
  - suggestion: Group help by verb with inbox, status and doctor first; drop low-value status columns at narrow widths instead of truncating headers.

## Low

- **Broken links** — Running-now and the Runs table link retro and persona runs to /tasks/_retro-… and /tasks/_persona, which 404.
  - suggestion: Link those rows to their run page or render them without a link.
- **Stale copy** — The Trials empty state describes a free-text contender field replaced by pulldowns in CG-087, and the README's result-line example and TUI key list are out of date.
  - suggestion: Update the Trials empty state to point at the pulldowns and refresh the README's GARDEN_RESULT statuses and TUI keys.
- **Scaffold next steps** — garden init prints its next-step line after nine wrapped absolute paths and garden new-phase prints only the plate name.
  - suggestion: Print the next command first and have new-phase say to edit goals.md then run garden plan --dry-run.
- **Task page summary** — Timeline and Log repeat the same events and nothing summarises why a task took nine runs.
  - suggestion: Add one line above the runs table with run counts by mode, rebase rounds and hand interventions.

_garden persona run 20260905T025716Z-persona_
