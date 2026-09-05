# Optimise for cognitive complexity

Asked for by the user on 2026-09-05: "always optimise for cognitive complexity; code at each level
of abstraction should be appropriately as easy as makes sense to understand." The digest carries
the one-line rule; this file is the reasoning and the tests to apply.

## What it means

Cognitive complexity is how much a reader must hold in their head to understand a piece of code:
nesting, branches, non-local state, indirection, and names that hide rather than say. It is not
the same as cyclomatic complexity or line count; a long flat function can be easier than a short
one that calls five helpers whose names do not say what they do.

"At each level of abstraction" means the test is applied where the reader is:

- **A module** should read as one idea: its name and its first docstring say what it is for and
  what it does not do; a reader can find the function they need from the names alone.
- **A function** should be understandable from its signature and body without opening other
  files: what it takes, what it returns, what it changes, what it refuses. If understanding it
  needs the caller's context, the boundary is in the wrong place.
- **A line** should say one thing. A conditional that needs a comment to explain what it tests is
  a name waiting to be extracted.

"As easy as makes sense" is the escape hatch for real complexity: a merge queue, a rebase with
verdict-keeping, an environment scrub. Those are complex because the problem is. The rule there
is to spend the complexity once, in one place, behind a name that says what it is, with the
reasons written beside it, and to keep everything around it simple.

## Tests to apply while writing and reviewing

- Could a new reader say what this function does after reading only its signature and first
  three lines? If not, rename or split.
- Does this file have more than one reason to change? If two features would both edit it, it is
  two files.
- Is there one path through this code, or several that a reader must trace? Prefer early returns
  and flat structure; prefer a small table over a chain of `elif`.
- Is a piece of state read far from where it is written? Pass it, or put reader and writer in one
  place.
- Would deleting this abstraction make the code easier to follow? Then delete it; indirection is a
  cost paid on every read.
- Is the clever version (a comprehension that does three things, a decorator that changes control
  flow, a metaclass) easier to understand than the plain one? Almost never; write the plain one.

## What it is not

- Not a licence for long functions: a function that stays flat but does five things is five
  things a reader must hold.
- Not a ban on abstraction: a well-named abstraction that hides genuine complexity lowers the
  cognitive load of everything that uses it. The test is whether the reader is better off.
- Not style for its own sake: match the repo's conventions first (the digest's rule), then apply
  this within them.

## For reviewers

Raise it when a change makes a module, function or line harder to understand than the problem
requires, and say which of the tests above it fails. Do not raise it for code that is complex
because its problem is, when the complexity is in one place with its reasons beside it.
