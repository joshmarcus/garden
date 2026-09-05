# usability-expert review of context-garden/phase-03

**Persona:** usability-expert · **Score:** 6/10 · 2026-09-05T10:21:05+00:00

The operator-facing text this phase touched is strong: every new refusal names the state and the next command, doctor and the scripted QA report clearly, and the loop needs the button less. But the pages a person opens first regressed in ways the walkthrough makes plain: eight of thirteen Inbox rows carry a stray '] Tests…' fragment from an acceptance checkbox, the Board flags done tasks as needing you while the Inbox disagrees, and the new rebase run kind has a page that says it recorded a claude-json result with no message, no brief and no statement of what git did. Add that the Config page still implies a live edit while the closing doc admits most keys need a restart, and the phase reads as mechanically sound but under-explained to the person watching it.

## High

- **Inbox** — Draft rows on the home page show 'planned, not yet approved · ] Tests cover …' because the last-log-line helper picks the final acceptance checkbox from the task body.
  - suggestion: Make the helper read only dated log entries (lines matching the log's timestamp prefix) and fall back to nothing; add a walkthrough or unit test that a fresh draft with acceptance checkboxes renders no fragment.

## Medium

- **Run page** — A mechanical rebase run page reads 'recorded a single claude-json result … (no final message) (no brief recorded)' with header 'rebase · harness · $0.00', so nothing says a no-model git rebase happened or what it did.
  - suggestion: Give rebase runs their own summary block from the run record and task log: base, mechanical or agent, pushed or not, checks result, verdict kept or review dispatched; hide the transcript and brief tabs when no harness ran.
- **Board and task page** — Done tasks CG-164 and CG-142 show a hot 'needs you' badge and CG-125 shows 'automerge held' after merging, contradicting the Inbox which lists none of them.
  - suggestion: Gate the board badge and the automerge fact on a non-terminal status, and have one tick backfill by dropping needs_human, pending_feedback and automerge_blocked from every terminal task's state entry.
- **Config page** — The page says 'edit the underlying YAML files to change them' while the closing doc admits only budgets and max_parallel are live and everything else needs a restart.
  - suggestion: Say on the Config page which keys are live and that the rest take effect on the next `garden serve`; or finish goal 6 so a garden.yaml edit is re-read each tick and the page can say so.
- **Timeline** — Rebase events render as bare 'rebase' rows with empty text on the task timeline and the Events page.
  - suggestion: Emit a one-line note on each rebase event (e.g. 'mechanical onto main, pushed, verdict kept' or 'conflict in tests/…, agent dispatched') and render it in the events template's default branch.
- **CLI first run** — `garden new-phase` succeeds for a product that was never registered, and the next command fails with only "no product 'widget2'" and no pointer to `garden new-product`.
  - suggestion: Refuse new-phase for an unregistered product with a message naming new-product, and append the same hint to every 'no product' error.

## Low

- **CLI exit codes** — `garden approve` prints the frozen-phase refusal and exits 0, while `garden dispatch` exits 1 for the same refusal.
  - suggestion: Exit 1 from approve when any target was refused or nothing was approved.
- **doctor** — The new 'git identity: missing user.name or user.email' line has no fix, and the report ends with 'see above'.
  - suggestion: Add the fix inline (git.user_name/user_email in garden.yaml or git config) and replace 'see above' with a one-line count of failed checks.
- **Runs table** — A superseded review run is labelled 'open run · error' in the task's runs table.
  - suggestion: Label it 'superseded' with the newer run id, and keep 'error' for runs with an error field.
- **Herbarium** — The closed phase-01 plate reads '19 of 19 tasks done · 0 PR(s) merged · spent $0.00', which looks like missing data rather than a record.
  - suggestion: Render 'no PRs tracked' and 'cost not recorded' when the phase predates PR and cost tracking, so the plate reads as deliberate.

_garden persona run 20260905T101601Z-persona_
