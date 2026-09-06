# Principles digest

Inlined into every agent brief. Keep it short; long-form reasoning lives in the sibling files.

## Working style
- Ship small vertical slices. Every merged PR leaves the product working and tested.
- Read what the brief points at, then explore only the code you must change. Do not wander the context garden; if the brief is missing something, say so in your report so the task gets fixed.
- Follow existing conventions in the repo before inventing new ones. Match the surrounding style.
- Tests are part of the change. Run the project's fast checks before you finish; fix what you broke.
- Prefer boring, dependency-light solutions. New dependencies need a one-line justification in the PR body.
- A PR description frames the work by its goal and outcome and the general motivation: what a reader gets and why it was worth doing, then how, then what was verified. It reads as if written once, in the present tense, for someone who never saw the task or the review: no scar tissue (no round-by-round narration, no "addressed reviewer feedback", no references to earlier attempts or to what was tried and abandoned). Follow-ups go in one short section at the end.
- Optimise for cognitive complexity. At every level of abstraction the code should be as easy to understand as makes sense there: a reader of a module sees what it is for, a reader of a function sees what it does without holding the rest of the file in their head. Prefer one clear path over a clever one, names that say what a thing is, and small units with a single reason to change; do not spread one idea across layers or fold three ideas into one function. See `cognitive-complexity.md`.

## Reporting
- Be precise about what you did, what you verified, and what you did not do.
- If blocked on a human decision, stop early and ask one precise question rather than guessing.
- Note friction (missing context, confusing spec, tooling pain) in the `friction` field of your result, one short item each; it is filed on the phase and never goes in the PR body.

## Scope
- Do not widen the task. Follow-ups go in the PR body, not in the diff.
- Do not edit task files under `**/tasks/`; the scheduler owns them.
- Never rewrite history on shared branches; never disable or skip tests to get green.

## Design work is an invitation, not a prescription

When a task asks for a page, a mock or a visual system, the spec states the problem and what must be present; how it looks, reads and moves is yours to invent. We want new and beautiful ideas, not the requirements list laid out as boxes; depart from the prescription when you have a better idea and say why. And never call a page done without having looked at it: capture it (see "Looking at pages" in the product overview) at both widths, light and dark, read the captures back, and adjust until it is right. (Owner, 2026-09-06.)

## Acceptance criteria are outcomes with evidence, never implementation

A criterion says what is true when the work is done and how anyone can see it: a page that answers, a test that proves, a number that reads. It never names a file, a function, a field or a mechanism; those belong in the task's context and reading list, where they guide without binding. Three to five lines, each verifiable. A worker who finds a criterion wrong or impossible as written amends it in the task file with one sentence of reason and says so in the result, and the reviewer judges the amended line, not the original. A reviewer marks each criterion met only with evidence it can point to. (Owner, 2026-09-06, from 304 reviews: a third of send-backs turn on a criterion; every misfire was a criterion that named an implementation detail.)
