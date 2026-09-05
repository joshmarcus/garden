# usability-expert review of context-garden/phase-02-friction

**Persona:** usability-expert · **Score:** 6/10 · 2026-09-05T02:51:01+00:00

The decision surfaces this phase built are strong: attention and decision cards name the stop, show evidence, explain every button, and offer a discuss prompt; web errors flash instead of 500; the run page shows what a worker did. The first five minutes and discoverability are weak: the quick start spends an unrecorded model call on an empty scaffold and misreports it, garden status is unreadable at 80 columns, retro --dry-run tracebacks, the help is a flat list of ~70 commands, and the two headline features of the phase (live output via output_format: stream-json, notifications via notify.command) are documented nowhere a new user looks. A few cards still point at the old way (budget card says edit garden.yaml; review card's CLI action is set-status done, which merges nothing).

## High

- **first run / plan** — garden plan on an unedited scaffold runs a real hard-tier model call, gets prose back, and reports 'no new tasks (all titles already existed)' while recording no run or cost.
  - suggestion: Refuse to plan when goals.md still holds template placeholders; distinguish 'model returned no tasks' from 'titles existed' and print the saved raw path and cost; record planner runs so usage and runs show them.
- **discoverability** — Live worker output requires harnesses.claude.output_format: stream-json and notifications require notify.command, and neither key appears in the README config block, docs, or the scaffolded garden.yaml; the default json format leaves the Live output panel empty until the run ends.
  - suggestion: Add both keys, commented, to the scaffold and README config block; make doctor's 'notify: not configured' line say what to set and consider stream-json the default for the claude harness.

## Medium

- **CLI overview** — garden status renders every column header as two characters at 80 columns and wraps the spend cell onto three lines when a budget is set.
  - suggestion: Collapse rarely non-zero columns at narrow widths or fold counts into one summary cell; keep the budget on its own line.
- **Inbox budget card** — The budget card's only action is a comment telling the person to edit garden.yaml, although this phase shipped garden budget and a phase-page budget form.
  - suggestion: Show 'garden budget <phase> <usd>' and a link to the phase page form; fix the empty '· medium ·' row header.
- **Inbox review card** — The 'Review and merge' card offers Mark done / set-status done as its action, which does not merge; nothing says to merge on GitHub and let the poll finish.
  - suggestion: Card copy: 'merge on GitHub; the next poll marks it done'; demote Mark done to the escape-hatch row on the task page.
- **retro** — garden retro --dry-run prints a Python traceback when the product repo path is not a git repository.
  - suggestion: A dry run should not touch the repo; a missing repo should be the same one-line red message doctor prints.
- **answer** — garden answer accepts an empty string and resumes the worker with nothing, spending a run.
  - suggestion: Reject empty or whitespace-only answers in the CLI, the web form and the TUI.
- **help** — garden --help is about seventy commands in one flat block and garden --version is an error.
  - suggestion: Group commands with Typer help panels (set up, read, decide, run the loop, tune) and add a --version flag.

## Low

- **digest** — garden digest counts needs_human events inside its window, so it prints '0 decisions need you' while the Inbox shows two.
  - suggestion: Take the decisions count from the inbox builder the badge uses; keep the window for the event lists.
- **worker fence message** — A person whose shell inherited GARDEN_ROOT gets 'workers must not run garden commands' from every command with no way out.
  - suggestion: Append 'if you are not a worker, unset GARDEN_ROOT' to the message.
- **copy defects** — Task page prints '( rounds)' when review_rounds is unset, garden inbox truncates the reason mid-word, and garden retry on a ready task logs 'ready -> ready'.
  - suggestion: Guard the rounds fragment, truncate on a word boundary with an ellipsis, and make retry on a ready task a no-op message.
- **doctor** — Doctor names a missing git identity but not the command that sets it.
  - suggestion: Print the git config commands under the failing line.
- **README TUI keys** — The README's TUI key list omits the c (accept) key added in this phase.
  - suggestion: Regenerate the key list from the TUI bindings or add c.

_garden persona run 20260905T024354Z-persona_
