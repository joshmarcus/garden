# phase-03 goals

## Why this phase

Phase 02 proved the loop runs on itself: 89 tasks done, 94 PRs merged, $547. It also showed where the code fights the loop. Two files took 20 of 22 conflicts. The caps counted rebases. Fifteen finished runs were lost to the sweep. The scheduler tests drive subprocess workers and flaked four times. The staff-engineer and security personas found state, accounting and trust holes. This phase changes structure and non-functional properties only. No user-visible feature enters it; features wait for phase 04. The retro that produced this list is in `../phase-02-friction/docs/retro.md` and `../phase-02-friction/docs/retro/`.

## Goals

1. **Structure.** The scheduler split by tick phase, the web actions as a registry, tests by area, the fake harness as a table (CG-137). This runs first and alone: nothing else is dispatched until it merges.
2. **Rebase as its own mode, and a merge queue.** Mechanical rebase first, an agent only on a real conflict, no re-review when the diff is unchanged, one PR rebased at a time right before it merges; caps count only worker rounds (CG-141, CG-139).
3. **State and accounting are correct.** The dirty-on-read rule no longer clobbers a concurrent write; a resumed reap does not double-count cost; a superseded or dead run record is closed (CG-144); actions refuse terminal tasks (CG-142); a freeze is phase state (CG-148).
4. **Trust at the edges.** PR feedback becomes a worker prompt only from trusted authors; workers run with a scrubbed environment; the web UI sanitises rendered HTML and checks the origin of POSTs.
5. **Testability.** An in-process runner for scheduler tests so nothing drives a subprocess worker; the walkthrough and the QA agent so the pages are tested, not pictured (CG-134, CG-135).
6. **Operability.** A config change takes effect without a restart; `notify.command` is configured, documented and tested; every clone gets a git identity (CG-147); the retro waits for its reports (CG-145); briefs are inlined from the target checkout with the fixed brief cost measured per phase.

## Non-goals

- Any new user-facing feature: the new-task form, the retro page, plates content. Phase 04.
- Hosted or multi-user operation.
- Changing the herbarium look.

## Definition of done

Measured with `garden metrics` against phase 02's numbers.

- conflict rebase rounds per merge under 0.2 (phase 02 after 20:00: 0.59).
- description-only revise rounds: none (phase 02: 12).
- first-pass review approval at 90% or better on easy and medium (phase 02: 83% and 84%).
- cost per easy task at or under $4 (phase 02: about $6).
- no module over 800 lines under `src/garden/scheduler/` or `src/garden/web/`; `task_action` is a registry lookup.
- no test drives a subprocess worker; the QA agent passes every flow on the demo garden.
- the three trust items in goal 4 merged.
- a `garden.yaml` change takes effect within one tick, no restart.
- every task shipped through `garden tick`; exceptions listed in the closing document.

## Carried over from phase 02

Drafts moved here with their "deferred by the freeze" notes: CG-125, CG-134, CG-135, CG-137, CG-139, CG-141, CG-142, CG-143, CG-144, CG-145, CG-147, CG-148. Drafts filed from the retro's open list carry `discovered_from: retro:context-garden/phase-02-friction`. Features moved to phase 04: CG-030, CG-132, CG-146, CG-156 (vocabulary and help), CG-158 (manual-task ergonomics).
