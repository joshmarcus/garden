# retro-editor review of context-garden/phase-05

**Persona:** retro-editor · **Score:** 7/10 · 2026-09-10T05:33:00+00:00

Both historical judges correctly chose reopen, and the joined phase-04 verdict retains CG-238, CG-239 and CG-242 while respecting the owner's disposition of the remaining work. Fable supplies the clearer owner-facing narrative; Astra adds a justified reload blocker and useful accounting and recovery distinctions. Both generated retros contradict the operator's $195 spend record, and neither model comparison establishes general superiority. The phase-05 goals preserve named work and apply later owner decisions, including accepted stabilization evidence and review before closure. Historical ID, ledger and comparison-run defects have merged remedies and are not filed again. This was a read-only review with no file changes, commits or test runs.

## Joined retro

_Joined from the two September 5 phase-04 retrospectives, checked against their original reports; later owner decisions govern the phase-05 goals below._

### Verdict

**Reopen phase 04 with CG-238, CG-239 and CG-242.** Both judges chose reopen. Fable named two blocker tasks; Astra named eight.

- **CG-238:** close the approval bypasses and prevent duplicate dispatch. Usability demonstrated a placeholder draft starting twice.
- **CG-239:** contain reading paths and protect scheduler Git execution. Security demonstrated arbitrary-file inlining and shared Git configuration executing with scheduler credentials.
- **CG-242:** prevent worker-written executable configuration taking effect before fence recovery **(astra)**. Security identified this as a third high; Fable incorrectly placed it among phase-05 follow-ups.

CG-240 and CG-241 duplicate CG-238 and CG-239. Cancel them with reasons. Preserve CG-243–247 as the first phase-05 work: concurrent task saves, ID reservation, planner isolation, protected worker/control state and truthful completion. Astra was right that these were substantive defects; the owner’s recorded disposition determines their phase.

This is the historical phase-04 verdict. It does not reopen phase 05. The owner accepted phase-05 stabilization evidence on September 10; phase-05 closure still requires its closing review and resolution of that review’s blockers.

### Answers to the retro’s questions

- **Headline:** adoption, with accepted-task measurement preceding routing experiments.
- **Draft volume:** every finding stays at its severity; no cap. Prune at approval and record cancellations. Both judges’ third-ranked feature is rejected.
- **Targets:** accepted easy-task cost ≤$4 and first-pass approval ≥90%, using the sonnet-era baseline.
- **Historical operating choices:** merge commits, four review rounds, easy-tier reviews and the luna/terra/sol tier map were ratified. The eight queue-rotation hand merges were a CG-176 defect, not policy.
- **Ledger:** `context-garden/docs/operator-spend.jsonl`.
- **Notifications:** CG-206 remains cancelled; browser notifications first, unattended phone delivery parked **(astra)**.
- **Adoption evidence:** the September 7 decision accepts a repeatable non-Python fixture; an external maintainer is not required.
- **Independent self-product review:** Astra raised security’s separate-second-opinion concern; phase 05 subsequently addressed it in CG-299.
- **Bypass permissions:** the historical question remains unresolved in the supplied Decisions record. Do not manufacture an answer.

### What the phase set out to do and delivered

Phase 04 aimed to make the loop leaveable, complete briefs before spending runs, align trust with execution, expose lifecycle states and consolidate writers.

CG-182 detached checks and rebases; CG-197 split the CLI and consolidated rebase handling. CG-192 supplied live configuration, CG-198 restart recovery, CG-212/217/227 quota and authentication recovery, and CG-220 origin-head starts and leased pushes. CG-191 enabled hard-tier queue merges, while CG-228 distinguished a stacked merge from completion on the final base.

The phase also delivered Costs, operator accounting, observation, profiles, browser notifications, backlog movement, trials, kickoff and retrospective decisions. The README improved the first-run journey.

These mechanisms did not establish universal approval, safe shared-state writes or achieved cost targets. The security demonstrations and approval bypasses outweigh the operator’s earlier broad completion claims.

### Numbers

Use the operator’s internally consistent snapshot; do not combine different reporting windows into a new total.

| Measure | Phase-04 evidence |
|---|---|
| Worker/operator/total spend | Approximately $474 / $195 / $669 |
| Operator effort | 673 turns; 29% of total, versus 50% previously |
| Merge attribution | 41 queue merges and 16 hand merges out of 57 |
| Easy-task cost | $5.04 over 29 completed tasks |
| First-pass approval | Easy 79%; medium 71%; previous phase 93% |
| Rebase rounds per merge | 1.02 mechanical plus 0.55 agent; 31 conflicts across 56 merges, costing $17.46 |
| Timing | Responsive operation reported after CG-182; no aggregate evidence establishes the timing thresholds |
| Walkthrough | No phase-04 capture established the promised closing journey |

Both generated retros report $477.34 worker spend and **$0 operator spend**. The latter contradicts the operator report. The worker-total difference remains a snapshot difference, not a reconciled phase total.

After the 14:50Z routing change, mean work-run cost fell from $4.56 to $2.53. Easy-task cost rose from $3.67, n=16, to $5.88, n=12; medium cost moved from $10.97, n=22, to $10.62, n=5. Different task mixes and small samples prevent a causal model ranking. The easy-era samples also total 28, not the headline 29: retain that denominator difference.

### Friction reconciled against merged work

| Underlying friction | Disposition |
|---|---|
| Empty, nonexistent or incomplete reading lists | Repeated after CG-193; carry into CG-293. CG-231 explicitly received “not found when the brief was built” **(fable)**. |
| Dirty README content inlined before recovery | CG-234 documents the wrong starting source; CG-293 addresses brief provenance. |
| Generic revision instructions without criteria or diagnostics | Repeated in CG-193/194/163/220; preserve concrete feedback in CG-293. |
| Unmerged sibling contracts and parallel question mechanisms | CG-225 resolved the duplicate implementation; planning prevention remained for CG-294/325. |
| Authentication broken by private HOME | CG-217/218 restored authentication; sharing writable configuration remained a separate security defect, later addressed by CG-291. |
| Quota failures, dirty retries and competing branch rewrites | CG-198/212/220 supplied recovery mechanisms. This is stronger evidence than merely observing that the affected branch eventually merged. |
| A review apparently inspected an older head | Unresolved at phase-04 review; phase 05 supplied head-aware collection and recovery through CG-343/438. |
| Trial/manual PRs waiting for review | CG-236 addressed trials; universal coverage remained a separate requirement. |
| Lost concurrent task edits and colliding retro IDs | Confirmed design hazards; the previous editor also recorded an actual collision. CG-243/244 subsequently addressed them. |
| Shared persona identity and unsafe footer lookup | Carried into CG-298; four reports also required manual parser recovery, addressed by CG-237. |
| Misleading capture text and omitted new pages | Preserve the renderer defect and phase-level coverage requirement; CG-297/253 subsequently addressed them. |
| Direct status writes and Mark done bypass | Preserve as one completion/integrity concern, addressed by CG-292. |
| Check continuation loss and scheduler coupling | Astra retained the staff engineer’s specific failure mode; keep durable continuation recovery and maintainability work distinct **(astra)**. |
| Stale operating guidance, vocabulary and counts | Merge overlapping persona reports into coherent work; CG-295/296 and later attention work provide relevant dispositions. |
| CG-220 supposedly needed three new guards | Two already existed: the brief’s premise was disputed, not three implementation defects **(astra)**. |
| CG-235 exit 143 | The interruption happened; two reruns passed. Resource contention was suspected, not proven. Preserve bounded interruption recovery without claiming a continuing source regression. |
| Doctor wrapping and ambient configuration | The individual tests were repaired; broader isolation remained useful follow-up, not proof those same tests still failed. |
| Resolved command spelling and test-location ambiguities | Historical lessons for future briefs; do not reopen completed implementation solely to rewrite its original instructions. |

All seven original personas contribute: security supplies the attack chains; staff engineering supplies concurrency and continuation hazards; project management identifies unowned goals; product management supplies outcome measures; designer, usability and user reports supply observed control failures and repair paths. Preserve original severities separately from the editor’s closure priorities.

### What to change

Measure accepted outcomes before changing routing. Make recurring recovery a bounded command, and make reviews follow every PR-producing path. Build briefs from the actual source and feedback.

Use one filing authority for a comparison. CG-244, CG-250, CG-300 and CG-301 subsequently addressed historical ID collisions, incomplete reopen briefs, ledger resolution and repeated-question/comparison behavior; do not file those defects again.

Judge functional outcomes proportionately. Historical missing-field findings must not become new blanket artifact, screenshot or checklist requirements under the owner’s September 9 policy.

### Features for the next phase

Historical ranking, retaining existing task ownership; later scope decisions control admission.

| Rank | Task-sized title | User value | Size | Dependencies |
|---|---|---|---|---|
| 1 | Measure accepted-task cost and first-pass approval — CG-251 | Compare delivered work, including unsuccessful effort and unpriced usage **(astra)** | Medium | CG-233/214; final-base acceptance |
| 2 | Queue every eligible unreviewed PR — widen CG-236 | Remove hand presses across runners | Medium | Current-head review identity and deduplication |
| 3 | Make the retro report its own measurements — CG-253 | Read timing, interventions and operator share together | Medium | CG-182/201/223; ledger correction CG-300 |
| 4 | Safely replace workers and install a pin — CG-254 | Eliminate the CG-234 two-worker collision and recurring restart sequence | Medium | CG-180/198/220; two sequenced operations |
| 5 | Repair draft briefs inline — CG-256 **(fable)** | Correct an approval refusal without paying for an edit run | Medium | CG-193/190 |
| 6 | Onboard an existing repository — CG-215 | Reach a useful accepted change from a non-Python project | Hard | Planner isolation CG-245; approval gate |
| 7 | Make operating profiles harness-aware — CG-255 | Avoid sending Claude model names to Codex | Medium | CG-221; measured routing outcomes |
| 8 | Share quota across model options — CG-230 | Continue through an exhausted account | Medium | CG-212/251; compatible model attribution |
| 9 | Add an OpenRouter CLI adapter — CG-213 | Evaluate another model route by accepted cost | Hard | CG-251; compatibility and escalation ownership |
| 10 | Execute on independent hosts — CG-216 | Use another machine without a shared filesystem | Hard | Authentication, leases and durable result transport |

## Next goals

### phase-05 goals

*Plant: poppy · Papaver argemone · Plate V.*

### Why this phase

**The garden runs in someone else’s environment and can say what a merged task costs.** Adoption remains the headline. Dependable execution, meaningful decisions and measured operator effort make adoption credible.

This draft preserves the owner’s goals and task identities while applying later decisions. It is a phase-05 document, not a newly invented phase-06 plan.

### Goals

1. **Onboarding — CG-215.** `garden onboard` and `garden-onboard` draft context from an existing repository. A non-Python fixture passes validate and doctor without hand-written configuration and reaches a useful accepted change. Drafts remain subject to approval; planning runs scrubbed.
2. **Any model at the right price — CG-213, deferred to phase 06.** Preserve the OpenRouter adapter, configurable tiers, response-based accounting and failure-driven escalation goal. Measurement precedes evaluation. CG-437 now supplies substantive-revision escalation, but does not alone prove the complete OpenRouter policy.
3. **Shared quotas — CG-230, deferred to phase 06.** Preserve multiple harness/model options, paused-account avoidance and per-run member attribution. Retain PR222.
4. **Any machine — CG-216, admitted by the September 7 override.** Preserve the portable protocol and PR221, plus CG-345–348 provisioning, execution, Spot recovery and cost/control scope. Preserve provider-neutral host lifecycle support. CG-423 supplies the later resumable scaling operation. Historical “last” ordering does not reinstate the superseded remote-worker deferral.
5. **Complete the dependable core and its accounting.**
   - CG-251 measures accepted cost and first-pass approval by model, tier and harness. CG-253 reports hand merges, tick timing and phase evidence using the product ledger.
   - Preserve CG-239/242 containment, scrubbed planning and notifications, private harness configuration and attributed control-state protection. Recovery must preserve legitimate concurrent evidence.
   - Preserve concurrent task saves, durable ID reservation, `_transition` ownership, Mark done’s final-base rule and explicit exceptional completion.
   - Widen CG-236 across runners; retain current-head review checks, consistent manual resume and retirement of obsolete reviews.
   - Keep reading context resolvable and source-correct; revision briefs retain criteria and concrete feedback; sequence dependent planning and inline retro evidence. Actual unmet outcomes block; optional evidence formatting does not.
   - CG-254 makes redispatch and pin safe; CG-250 carries reopen through approval, dispatch and closure under applicable phase gates.
   - CG-255 preserves harness-aware operating terminology; CG-256 permits inline brief repair. Counts, controls and scaffolded documentation agree with product behavior.

### Non-goals

No hosted multi-user garden, new garden-owned tool loop, default TUI parity programme or unrelated UI expansion. The 20–50-task routing evaluation remains phase 06. Preserve deferred operating-preset work; the supplied merged record shows Now consolidation subsequently completed as CG-319.

Do not cap retrospective drafts. Preserve every finding and prune at approval. Do not infer permission for new AWS spending, production fault injection or extension of a fleet deadline.

### Definition of done

- A repeatable non-Python onboarding fixture validates, passes doctor and demonstrates a useful accepted result without hand-written garden configuration.
- Preserve the four-hour productive window, at least ten representative completions, recovery/application journeys and resource accounting in `specs/stabilization.md`. Separate required owner actions from delegated operator interventions and include both in the historical account.
- **The owner accepted stabilization evidence on September 10. Do not require another soak.** Preserve failures and measured misses; acceptance is not a claim every historical metric passed.
- Report easy accepted-task cost against ≤$4, first-pass approval against ≥90%, hand merges against zero, agent rebases against <0.3 per merge and operator share against <29%. Include cohort sizes and unpriced usage. The sonnet easy baseline is $5.88, n=12; $5.04 is the broader historical average.
- Record tick timing in metrics and the rail, and preserve the phase walkthrough captured before its persona reviews.
- Every normal approval/dispatch path honours the shared gate; reading paths resolve; status transitions and final-base completion remain consistent.
- Account for the **three original security highs correctly:** reading containment and shared Git execution under CG-239, and unsafe reload under CG-242. Account separately for the planner, fence exemptions and shared harness directories—the security report’s three mediums. Close them or record explicit accepted risk; no unresolved new high.
- List outside-tick work, hand merges, operator repairs and release-source differences truthfully.
- After CG-423’s merge, complete closing review and resolve its blockers before closing phase 05. Publish a versioned release only after actual closure, with applicable exact-source CI and independent review. Live canaries are optional.
- Keep CG-213/230 deferred and preserve explicit CG-402/403/407/408 holds. Reuse prior evidence where valid; do not equate a merged implementation with deployment.

### Carried over

Retain the historical phase-04 blockers CG-238, CG-239 and CG-242; cancel duplicate CG-240/241. Preserve the initial phase-05 order CG-243, CG-244, CG-245, CG-246, CG-247 and their delivered successors CG-291/292.

Keep the CG-251–299 refiled follow-up record: briefs, planning, status ownership, documentation, vocabulary, capture rendering, interrupted checks, persona provenance, substantive criterion review, harness classification, obsolete reviews, continuation recovery, scheduler structure, notification/kickoff behavior and small accessibility/test-isolation items.

Retain CG-213, CG-215, CG-216, CG-230, CG-236, CG-237 and CG-250. CG-222 remains in phase 06; CG-206 remains cancelled. Preserve CG-189’s replacement by CG-225, CG-234’s manual termination, CG-176’s eight rotation merges, all sixteen hand merges, the historical routing changes, four restored persona reports and the CG-251–299 refiling intervention.

Group only coherent unstarted work. Preserve in-flight implementation, reviews and recovery independently; the withdrawn four-track proposal stays withdrawn.

### Features for the next phase

Retain the owner’s named list: CG-215 onboarding; CG-251 accepted outcomes; widened CG-236 review coverage; CG-253 retrospective measurements; CG-254 redispatch/pin; CG-255 operating profiles; CG-256 inline repair; CG-230 pools; CG-213 OpenRouter; CG-216 independent workers.

Use the ranked values, sizes and dependencies in joined-retro. Link delivered work rather than filing it again; keep deferred work subject to the owner’s phase-release decisions.

## Comparison

Both judges chose reopen, ranked accepted-task measurement first and universal review queueing second, and carried the same central concerns about briefs, trust, hand steps and surface consistency.

**Fable’s advantage is useful compression.** Its 36 friction rows consolidate repeated causes. The post-CG-193 broken reading lists and dirty README explanation are concrete; the operator and friction log support them. Its separate inline-repair feature addresses the user’s observed paid-edit workaround. Astra mentions repair but does not rank it separately.

**Astra’s advantage is sharper distinctions.** It correctly elevates unsafe live reload, retains check-continuation loss and scheduler coupling, distinguishes unpriced usage from zero, and separates independent review from repeated review. Security and staff-engineer reports support those points. Its concurrency blockers were real; the owner chose to carry five into phase 05. Filing CG-240/241 duplicated existing blockers despite Astra’s own advice to reuse them.

Astra correctly disputes CG-220’s “three missing guards” premise. On CG-235, its refusal to infer resource contention from a signal exit is better than Fable’s causal wording; nevertheless, passing reruns do not settle interruption recovery. Fable’s fixed-by-CG-212/220 explanation for the old branch is more useful than Astra’s “outdated because merged.”

Neither judge supports a causal claim that a particular cheap model costs more overall. The operator explicitly identifies small, different task mixes. Neither corrects the generated $0 operator figure.

Fable ranks measurement and capture before redispatch, and inline repair before onboarding. Astra puts redispatch before capture, onboarding seventh and pools eighth. Both rank a draft cap third against the owner’s subsequent no-cap decision. Fable’s goals make high-only filing definite too early; Astra keeps it conditional. Both defer CG-216, a recommendation superseded by the owner.

The generated findings blocks each contain **31 entries from designer, project-manager and user**, not every finding from all seven personas. Their prose and separate follow-ups recover much of the other reports. Repeated generated text is not independent agreement. Fable merges friction aggressively; Astra’s **80 rows**, counted directly, preserve more distinctions but repeatedly classify resolved brief wording as ongoing work. The previous editor’s count of 79 is incorrect.

Fable’s retrospective is shorter and more readable. Astra repeatedly says “no supplied evidence” where a concrete disposition would help. Neither is entirely free of process narration. Fable follows the stub’s headings more closely, but still changes its emphasis; Astra reorganizes it into a different document.

| Model | List cost | Duration | Retro words | Goals words |
|---|---:|---:|---:|---:|
| claude-fable-5-1 | $2.68 | 5m 43s | 5,233 | 1,251 |
| gpt-6-astra | $0.99 | 7m 04s | 6,475 | 1,039 |

Costs and durations come from `judges.md`; words were counted from the supplied files. This was one paired comparison over seven Fable-written persona reports, not a model benchmark.

I would use Fable for the owner-facing draft and Astra as a non-filing challenge to closure-critical claims. The additional $0.99 was worthwhile here because the reload blocker mattered. The pair costs $3.67 before editing and shared persona costs; use both for a disputed trust or closure verdict, not automatically for every routine retro.

## Medium

- **retro input scope** — The phase-05 retro-editor assignment names phase-04 judge inputs and a wildcard that also includes a previous retro-editor synthesis, mixing review scope and dependent evidence.
  - suggestion: Give the editor an explicit source phase, evidence cutoff and manifest of the seven original persona reports; label prior synthesis as historical and keep the requested output phase separate.

## Low

- **security accounting** — The phase-05 goals describe CG-239, CG-242 and planner isolation as the security persona's three original highs, although reading containment and shared Git execution were separate highs and planner isolation was medium.
  - suggestion: Track the original three attack chains and severities accurately: reading containment and shared Git execution under CG-239, unsafe reload under CG-242, and planner isolation separately among the original mediums.

_garden persona run 20260910T052454Z-persona_
