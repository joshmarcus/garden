# phase-02-friction goals

## Feature freeze (2026-09-05 00:35 UTC)

No new features enter this phase. Approved from here on: only fixes needed to merge what is already built and to keep the loop honest (CG-129, CG-126, CG-131). New feature ideas go to phase 03; discovered features are filed as drafts with "deferred by the freeze" in the log. The wrap-up order: open PRs merge, the manual items close (CG-113, then CG-029), persona reviews run against the finished phase, then CG-029 writes the friction document and the next goals and the phase closes.

## Why this phase

The bootstrap loop works on paper. This phase runs the tool on itself: every task here is
executed by the garden, and every worker is asked to report friction. The output is a
tool that is smoother to operate and a first read on where tokens actually go.

## Goals

1. Close the loop on review: make the automated review pass (shipped in bootstrap) earn its keep, and
   review comments that are addressed without a human re-dispatching anything.
2. Make waiting visible: live worker output in the web UI, and a notification when a
   task needs a human.
3. Collect friction from worker PR bodies into a phase document so the next planning
   round sees it.
4. Keep the fixed cost of a brief flat while the garden grows.

## Non-goals

- Hosted or multi-user operation.
- Automatic merging (still a human decision).

## Definition of done

- Every task in this phase shipped through `garden tick`, not by hand.
- `docs/friction.md` in this phase lists what workers reported and what was changed.
