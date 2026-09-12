---
id: CG-222
title: 'A collective, searchable context: every run leaves structured notes about the codebase, briefs
  search them, and the retro consolidates them'
status: cancelled
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: hard
reading:
- src/garden/brief.py
- src/garden/scheduler/discovered.py
- src/garden/friction.py
- src/garden/retro.py
- principles/00-index.md
- docs/design.md
- context-garden/phase-03/docs/retro.md
created: '2026-09-05T16:58:10+00:00'
updated: '2026-09-07T21:36:25+00:00'
---

## Goal

Speculative, for a future design (the user, 2026-09-05: "agents should add to a collective searchable context, similar to codex's new context strategy"). Every worker, reviewer and persona run leaves a few structured notes about what it learned: where a thing lives, a convention that is not written down, a trap it fell into, a decision it made and why, a command that works. The notes accumulate in one searchable store per product. When a brief is built, the store is searched with the task's title, criteria and reading list and the best few notes are inlined under "What earlier runs learned"; a reviewer's brief gets the notes about the files in the diff. The retro consolidates the store: merges duplicates, marks what merged code has made stale, and promotes durable notes into `principles/` or the product overview for a person to approve.

## Why it might matter

Phase 03's friction said the same things repeatedly: reading lists that omitted the file the fix lived in, briefs that described pre-split code paths, workers rediscovering that `product.md` lives in the driving garden. The persona reports repeat findings across phases. A worker that just spent twenty minutes learning how the merge queue writes state could leave that in three lines for the next one; today that knowledge ends with the transcript. `principles/` is the human-written layer and must stay so; this is the agent-written layer beneath it, searchable rather than inlined whole.

## Design sketch (to be argued with, not built as written)

- **Store:** `<product>/docs/notes/` as markdown files, one per run or per topic, plus an FTS index built with the standard library (`sqlite3` FTS5 in `.garden/notes.db`, rebuilt from the markdown, no new dependency; embeddings only if FTS proves too weak). Each note: `topic`, `paths` it is about, `kind` (location, convention, trap, decision, command), `claim` (one to three sentences), `evidence` (a commit, a test, a file and line), `run`, `task`, `at`, `confidence`.
- **Writing:** the result contract (`GARDEN_RESULT`) gains `notes: [...]`, capped at five per run, and the review brief asks the reviewer for `notes` about the diff's files; discovered work and friction stay what they are. Notes are worker-authored and therefore untrusted input: they are inlined into briefs as quoted claims with provenance, never as instructions, and the trust rules of CG-154 apply to their rendering.
- **Reading:** `brief.py` runs a search (title, criteria, reading paths, the diff's paths for a review) and inlines the top N by relevance and recency under a heading with each note's provenance; a cap on tokens; a task can opt out. `garden notes search <query>` and a notes page in the web UI for people.
- **Consolidation:** the retro (or a `garden notes consolidate` run) merges duplicates, marks notes stale when their `paths` changed after `at` or a merged PR contradicts the claim (the friction reconciliation already does this kind of judgement), and proposes promotions to `principles/` or `product.md` as a PR for a person to approve; nothing agent-written reaches `principles/` without that approval.
- **Relation to friction and discovered work:** friction is what went wrong in the process, discovered work is what should be done, notes are what is true about the code; the three stay separate and the retro reads all three.

## Open questions for the design

- FTS versus embeddings: does keyword search over a few hundred notes find the right ones for a brief, and what does the miss rate cost against always-inlined bloat?
- Staleness: the CG-149 lesson (inlined snippets older than the file) applies; how much of a note's validity can be checked mechanically (paths exist, the evidence commit is an ancestor of main)?
- Volume and noise: five notes per run across a hundred runs a day is a corpus a person cannot read; consolidation frequency and the promotion bar decide whether the store stays useful.
- Trust: a note is a worker's claim; a poisoned note reaches every later brief. Provenance, the untrusted rendering, and consolidation by a review-tier run are the proposed guards; is that enough?
- Where this sits against Codex's approach, which the user named as the reference: read what it does before designing, and steal what fits.

## Acceptance criteria (for a first, small version)

- [ ] A design document under `docs/` answering the open questions with evidence from this garden's own transcripts (which notes would have helped which later task), reviewed by the staff-engineer and security personas.
- [ ] A prototype: `notes` in the result contract, the markdown store, FTS search, and the brief section behind a config flag; a measured trial on one phase comparing revise rounds and first-pass approval with and without it.
- [ ] Consolidation and promotion left for a follow-up task once the trial says the store is worth keeping.

## Log

- 2026-09-05T17:00:33+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-06T03:38:40+00:00 approved (web)
- 2026-09-06T03:38:40+00:00 no kickoff report for context-garden/phase-06
- 2026-09-06T13:13:29+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:22+00:00 reset to ready by hand
- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T21:36:25+00:00 cancelled (web)
