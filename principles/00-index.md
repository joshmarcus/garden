# Principles digest

Inlined into every agent brief. Keep it short; long-form reasoning lives in the sibling files.

## Working style
- Ship small vertical slices. Every merged PR leaves the product working and tested.
- Read what the brief points at, then explore only the code you must change. Do not wander the context garden; if the brief is missing something, say so in your report so the task gets fixed.
- Follow existing conventions in the repo before inventing new ones. Match the surrounding style.
- Tests are part of the change. Run the project's fast checks before you finish; fix what you broke.
- Prefer boring, dependency-light solutions. New dependencies need a one-line justification in the PR body.
- Optimise for cognitive complexity. At every level of abstraction the code should be as easy to understand as makes sense there: a reader of a module sees what it is for, a reader of a function sees what it does without holding the rest of the file in their head. Prefer one clear path over a clever one, names that say what a thing is, and small units with a single reason to change; do not spread one idea across layers or fold three ideas into one function. See `cognitive-complexity.md`.

## Reporting
- Be precise about what you did, what you verified, and what you did not do.
- If blocked on a human decision, stop early and ask one precise question rather than guessing.
- Note friction (missing context, confusing spec, tooling pain) in the `friction` field of your result, one short item each; it is filed on the phase and never goes in the PR body.

## Scope
- Do not widen the task. Follow-ups go in the PR body, not in the diff.
- Do not edit task files under `**/tasks/`; the scheduler owns them.
- Never rewrite history on shared branches; never disable or skip tests to get green.
