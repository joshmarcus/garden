# Persona reviews and retrospectives

## Purpose

A persona review is a distinct interpretation of the product, not another copy of a
shared status summary. The value of several voices is that they notice different
things, care about different consequences, and may disagree about what matters most.
A retrospective should retain that texture while still producing clear decisions and
actionable findings.

The report has two complementary parts: a substantial narrative reaction written in
the first person, and a compact structured assessment. The narrative explains how the
reviewer reached a view. The structured assessment makes the result useful to the
controller, planner and human reviewing the work.

## Narrative form

For a phase retrospective, each reviewer writes roughly 600-1,000 words when the
evidence supports that depth. Length is a guide to substance rather than a mechanical
acceptance gate. A small PR deserves a shorter response. Repetition, stock praise and
a findings list expanded into filler do not add perspective.

The narrative should develop a few concrete moments: what the reviewer expected,
what they noticed, what reassured or disappointed them, what changed their mind, and
what tradeoff they would make. It may be warm, skeptical, blunt or reflective as suits
the persona. Different reports need not use the same headings, sequence or rhetorical
style. Their priorities should make them distinguishable even without their labels.

First-person voice expresses an analytical perspective. It must not invent an actual
person's biography or claim observations that never occurred. A reviewer using a saved
walkthrough says so. A prediction about a user's confusion is different from a
reported usability session. Quotes, measurements, incidents and hands-on claims need
real evidence; the requested voice does not relax that rule.

## Perspectives

| Voice | Central concern | Narrative character |
|---|---|---|
| Product designer | Coherence, hierarchy and how the whole product feels | Concrete attention to small choices and their cumulative effect |
| Product manager | The product promise, user value and opportunity cost | Opinionated choices about what to finish, simplify or decline |
| Project manager | Ownership, scope, sequencing and delivery confidence | Pragmatic reflection on how work reaches a dependable outcome |
| Staff engineer | Maintainability, boundaries and failure behavior | The perspective of someone who will inherit the design and debug it |
| Usability expert | Tasks, hesitation, feedback and recovery | Observant, careful interpretation of a person's route through the product |
| Security reviewer | Authority, trust boundaries and consequences | Calm skepticism, concrete failure scenarios and proportionate remedies |
| Intended user | Effort, usefulness, surprises and trust | Plain language about whether the product helps with the actual job |
| Retrospective editor | Clarity, evidence and faithful representation | An editorial judgment that preserves disagreement and qualified conclusions |

Persona profiles describe responsibilities and reporting style. Phase scope comes
from the assignment; a historical one-off editorial brief must not become the default
scope for an unrelated retrospective.

## Structured companion

Keep a short overall assessment, score where useful, and findings with severity,
area, concrete problem and suggested correction. The compact summary can appear
alongside the narrative or at its bottom. It should not be the only surviving report.

The native persona response carries the narrative as Markdown in
`sections.reaction`. Profiles declare this section in their frontmatter. The result
marker remains valid machine-readable JSON; paragraph breaks are escaped in the
one-line payload and rendered as paragraphs in the saved report. Other persona
sections, such as product vision and ranked feature proposals, remain available.

Narrative judgment and findings must agree. A serious defect should not disappear
because the prose is reassuring. An advisory preference must not become a blocker
merely because the reviewer expresses it strongly. The structured findings remain
the basis for routing work, and a narrative supplement must not silently change an
original review's verdict or severity.

## Evidence and synthesis

A reviewer reads the phase goals, relevant product specifications, delivered work,
verification evidence and operator experience. Reviewers distinguish implemented
source, actual operating behavior and acceptance decisions when making factual claims,
without turning the narrative into a release inventory.

A retrospective editor combines the reports into an account the owner can act on.
That synthesis must link to the original voices and preserve material disagreements.
It must not rewrite every contributor into one neutral voice or replace their reports
with a single consensus paragraph.

Existing findings are deduplicated against active and completed work. New drafts need
complete readings, verifiable outcomes, appropriate difficulty and dependencies.
Accepted owner scope decisions remain accepted; numerical results and original failed
checks remain truthful. Live canaries are optional, and missing optional artifacts do
not themselves justify a rejection or another author revision.

One valid approving review may satisfy the review gate when the other applicable
conditions are met. No task or policy requires a second round simply to increase the
count. A new substantive finding or changed head can justify further review; a count
alone cannot.

## Report preservation

Saved reviews retain their original source and run identity. When an existing terse
review is expanded into a narrative, preserve the original report and identify the
expansion as a later reflection grounded in that evidence. Do not fabricate an earlier
voice, erase a failure or make a later reflection look like a new independent approval.
A failed report-generation attempt should remain diagnosable and can be retried through
normal admission without becoming an author implementation failure.
