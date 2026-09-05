---
plant: poppy
latin: Papaver rhoeas
plate: V
---

# phase-05 goals

_Stub written by the operator on 2026-09-05 when the user placed the first tasks here; the phase-04 retro rewrites it._

**In one sentence: the garden runs in someone else's environment, not only in this one.** Phase 03 made the loop leaveable and phase 04 gave it its features; phase 05 is about adoption: a team points it at a project they already have, on models and machines they already pay for.

## Why this phase

A second team cannot use the garden today: setting it up means writing product.md, principles and the setup block by hand, its workers only run on the scheduler's own machine or over ssh from it, and every model call goes through two vendor accounts that both hit their quota on 2026-09-05.

## Goals

1. **Onboarding.** `garden onboard` and the `garden-onboard` skill read an existing project and its environment and draft the garden for it (CG-215).
2. **Any model, at the right price.** An OpenRouter harness with per-tier models and cost from the response (CG-213), routed by difficulty with failure-driven escalation and measured by cost per accepted task, per `specs/cost-aware-model-routing.md`.
3. **Shared quotas.** A tier can name several harness and model options and dispatch spreads runs across them, skipping a paused or exhausted account (the pool task filed with this line).
4. **Any machine.** Workers on independent remote hosts that claim runs over HTTP and push results back (the remote-worker task filed with this stub).
5. What the phase-04 retro adds.

## Non-goals

- Hosted or multi-user operation of the garden itself.
- New UI beyond what the three goals need.

## Definition of done

- A non-Python fixture project is onboarded to a passing `garden validate` with no hand-written files.
- One task each completes through OpenRouter and through a remote worker on a throwaway host, reviewed and merged by the loop.
