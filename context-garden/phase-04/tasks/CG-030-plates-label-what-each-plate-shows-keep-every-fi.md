---
id: CG-030
title: 'Plates: label what each plate shows, keep every file public domain, credit Thomé'
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
estimate: S
difficulty: easy
reading:
- src/garden/web/static/plates/SOURCES.md
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-030-plates-label-what-each-plate-shows-keep-every-fi-trial-claude-claude-sonnet-5
pr: https://github.com/joshmarcus/context-garden/pull/177
runner: manual
harness: claude
model: claude-sonnet-5
last_dispatched_at: '2026-09-05T18:16:22+00:00'
created: '2026-09-04T14:36:12+00:00'
updated: '2026-09-05T21:45:10+00:00'
---

## Goal

Make the specimen labels, the licence record and the credits agree with the plates that were actually fetched.

## Context

The twelve plates came in through PR #5 with three substitutions that the fetch code documents but the UI does not: the poppy plate is Thomé's prickly poppy (*Papaver argemone*, Tafel 260) while the label reads *Papaver rhoeas*, corn poppy; the bramble plate is *Rubus thyrsoideus* of the *R. fruticosus* aggregate, filed on Commons as "candidans"; the fern is plate 10 of the Biodiversity Heritage Library scan of the 1903 printing. `SOURCES.md` also records the foxglove file as CC BY-SA 3.0 (the cleaned derivative's own tag; the original plate is public domain) and lists Commons uploaders as artists for the cleaned files.

Everything involved lives in `PLANTS` (`src/garden/plants.py`), `CANDIDATES` and `sources_markdown` (`src/garden/platefetch.py`), and the specimen label in `src/garden/web/templates/phase.html`. Re-fetching is `garden plants --fetch`, which needs access to Wikimedia Commons, so run it on the machine the plates were fetched from (`runner: manual`).

## Acceptance criteria

- [ ] The poppy's `latin` and `common` in `PLANTS` name what the plate shows (*Papaver argemone*, prickly poppy), or the poppy is re-fetched from a Thomé plate of *P. rhoeas* if one exists. Every other place that names the poppy follows: the botanical-theme spec (`context-garden/phase-01-bootstrap/specs/botanical-theme.md`, the seed-packet list) and `tests/test_plants.py`; the README no longer names it.
- [ ] The bramble entry reads *Rubus fruticosus* agg., and the specimen label's plate line names the plate's own species where it differs from the plant's (here Tafel 398, *R. thyrsoideus*).
- [ ] Foxglove comes from the original public-domain scan (`Illustration_Digitalis_purpurea0.jpg`, cropped by the fetch like the others) rather than the CC BY-SA derivative, so that every row of `SOURCES.md` is public domain. This repository is MIT-licensed and carries no share-alike material; keeping the derivative is not an option.
- [ ] `SOURCES.md` records, per plate, the roles as verified on the Commons file page and the work itself: the work and its author (Thomé), the plate's illustrator where the edition names one (the 1903 printing's plates are by Walter Müller, so the fern is not Thomé's own drawing), the scan's source (Commons upload or the Biodiversity Heritage Library), and the editor of a cleaned derivative where one was used. No role is filled in by assumption; uploader names are not listed as artists.
- [ ] Tests updated; `garden plants` and the phase page show the corrected names.

## Out of scope

- Re-cropping or replacing plates that already show the right species.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-04 at the phase-02 close (deferred by the freeze)

- 2026-09-04T17:23:50+00:00 approved (web)
- 2026-09-05T00:34:28+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:00:56+00:00 approved (web)
- 2026-09-05T03:05:56+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T10:31:12+00:00 approved (web)
- 2026-09-05T18:11:02+00:00 dispatched trial run 20260905T181047Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~7188 tokens)
- 2026-09-05T18:11:19+00:00 dispatched trial run 20260905T181103Z-trial via local [codex] (fresh session, base main, ~7222 tokens)
- 2026-09-05T18:11:19+00:00 trial started with claude:claude-sonnet-5, codex
- 2026-09-05T18:12:38+00:00 trial: no contender produced a PR
- 2026-09-05T18:13:35+00:00 reset to ready by hand
- 2026-09-05T18:13:41+00:00 dispatched trial run 20260905T181341Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~7307 tokens)
- 2026-09-05T18:13:42+00:00 dispatched trial run 20260905T181342Z-trial via local [codex] (fresh session, base main, ~7341 tokens)
- 2026-09-05T18:13:42+00:00 trial started with claude:claude-sonnet-5, codex
- 2026-09-05T18:16:16+00:00 reset to ready by hand
- 2026-09-05T18:16:22+00:00 dispatched trial run 20260905T181622Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~7410 tokens)
- 2026-09-05T18:16:22+00:00 dispatched trial run 20260905T181622Z-trial-2 via local [codex] (fresh session, base main, ~7444 tokens)
- 2026-09-05T18:16:22+00:00 trial started with claude:claude-sonnet-5, codex
- 2026-09-05T18:31:55+00:00 trial won by claude:claude-sonnet-5 (scores: claude:claude-sonnet-5=–, codex=–): https://github.com/joshmarcus/context-garden/pull/177
- 2026-09-05T19:22:39+00:00 automated review requested changes: Solid, well-verified plate/licensing fix with passing tests and clean scope, but the poppy criterion's spec-file follow-up lives in a separate repo and is unmet, and the PR description narrates a template bug that never existed on main. cost=$1.27
- 2026-09-05T21:27:10+00:00 automated review: approve — All five acceptance criteria are met and independently verified via the diff, tests, and a rendered image; full suite (867 passed) and ruff are clean, and the description is accurate with no scar tissue. cost=$0.95
- 2026-09-05T21:45:10+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/177
