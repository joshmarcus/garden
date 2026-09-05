# The two judges

| judge | model | cost (list) | duration | retro words | goals words | friction rows | verdict | blocking filed |
|---|---|---|---|---|---|---|---|---|
| fable | claude-fable-5-1 | $2.68 | 5 min 43 s | 5,233 | 1,251 | 36 | reopen | CG-238, CG-239 |
| astra | gpt-6-astra | $0.99 | 7 min 04 s | 6,475 | 1,039 | 79 | reopen | CG-240 to CG-247 |

## Where they agreed

Both said reopen, both named the brief-gate closure and the reading-path and git-config fence as the reasons, and both drew the same numbers from the operator retro (16 of 57 hand merges, $5.04, 1.57, first-pass approval down from 93%). Their "Findings from persona reviews" sections are identical because the tool generates them from the same seven reports; each judge filed the same 31 findings as drafts under different ids. Their feature lists share the top seven items in nearly the same order: cost per accepted task first, widen CG-236 second, a draft cap third, redispatch and pin, the retro's own walkthrough, harness-aware profiles, onboarding as CG-215. Both asked the owner the same six questions, and both marked the CG-181 retro-page item, the CG-194 HOME item and the CG-224 parallel-questions item fixed by the same PRs.

## What each caught that the other did not

**Fable** read the merged work and the live garden closely and its friction verdicts name a mechanism. It cited garden.yaml line 34 still saying "once CG-207 lands" (true in this checkout), CG-231 and CG-232 shipping "not found when the brief was built" entries after CG-193 merged (so the builder annotates a missing path rather than refusing it), CG-233 finding nine unlisted call sites at 20:30Z, the brief being built from the worktree before CG-198's stash runs, the reason no test isolates CLAUDE_CONFIG_DIR, and the accounting that CG-222 sits in phase 06. Its follow-up drafts (CG-288 to CG-299) are twelve items with titles a task could carry, and its next-goals draft kept the stub's shape. It was right on all of these; astra reached the same "still true" verdicts on the reading-list items but with evidence of the form "no supplied evidence establishes that briefs now require a populated list", which is absence of evidence stated as a finding.

**Astra** was right on three things fable missed or placed lower. It argued the config-reload window (the security persona's third high) blocks the close because phase 04 created the path; the joined retro adopts that. It promoted the staff engineer's two data-integrity highs to blockers, and its own run then demonstrated the second one: the retro branch now holds CG-248, CG-249 and CG-250 twice and CG-240 to CG-250 collide with live files. It marked two friction items "disputed" (CG-220's brief claiming three missing guards when two existed; CG-221's attempt assuming no Costs page), which is the correct verdict and a category fable lacks. It also asked two questions fable did not: whether CG-206's cancellation means unattended notification is no longer wanted (the owner answered), and whether a self product's second round should be an independent reviewer (still open). Where astra was wrong: it marked the 55-commits-behind branch "outdated" because the branch merged, when CG-212 and CG-220 fixed the cause; it marked CG-235's exit 143 "outdated" because reruns passed, when no retry on a signal exit exists; and eight blockers including three hard tasks would hold phase 04 open for a week to fix hazards that have hand workarounds.

## Verdict and ranking

Same verdict, different blast radius: two blockers against eight. Fable's set matches what the owner then chose; astra's set was over-inclusive by five but under-inclusive by zero. On features the only ranking difference is that astra folds CG-230 in as an eighth item and treats every feature as "reuse the existing draft"; fable filed six new drafts and marked two as duplicates. Both ranked a draft cap third, and the owner overruled both.

## Friction and persona findings

Fable kept 36 rows, one per cause, dropping nothing of substance and marking eight outdated. Astra kept 79 rows, one per report, so the missing-reading-list complaint appears fifteen times with the same verdict; it merged nothing and dropped nothing. Both carried every persona finding into a draft because the tool does that. Fable's "What the personas said" paragraph reads as a summary of the reports with the specifics kept (the three disagreeing needs-you counts, forty drafts, git 2.53); astra's is a paragraph of categories ("admission control", "closure evidence") and includes a line about which task list it trusted, which is process narration the retro should not carry.

## Writing

Fable is specific: task ids, timestamps, line numbers, a number per claim, and no history of its own making. Its weakest part is the Numbers section, which the tool rendered wrong for both ($0 operator). Astra is a quarter longer and reads as a compliance report: abstract nouns, verdict evidence phrased as what was not supplied, and a next-goals draft that abandoned the stub's structure (no Goals, Non-goals, Definition of done, Carried over headings) and reframed the stub's four named goals as "entry conditions" and prose sections. Neither has scar tissue in the PR-description sense. On the raw counts astra costs 37% of fable and takes 24% longer.

## Which judge next time

Use fable as the judge that writes the document and files the tasks. Its friction verdicts point at the PR or the line that settles them, its drafts are tasks, and its goals draft is the owner's stub with the retro's additions rather than a new document. Astra's run earned its $0.99 in one place, the blocking set, where its stricter reading of three security and integrity findings was the better call and the joined retro adopts one of them; it also proved a staff-engineer finding by reproducing it. That is worth a second run when the verdict is reopen, and not otherwise, and only in a mode that files nothing: two judges drawing ids from one counter cost the operator a hand renumbering of the retro branch, and a second copy of every persona finding. Once CG-244 reserves ids, a second judge run on the cheaper model as a check on the blocking set is a reasonable standing practice for a reopen; for a close-with-follow-ups verdict one judge is enough.
