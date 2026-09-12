# Friction

_No friction reported yet._

## Reported

### 2026-09-09 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260909T022741Z-revise

- No configured mypy or pyright executable is present, so no project typecheck could be run.

### 2026-09-09 · reported by CG-349 (Centralize editable configuration metadata and enforce project overrides and locks) in run 20260909T095617Z-work

- No mypy or pyright command is configured in the prepared environment, so there was no project typecheck to run.

### 2026-09-09 · review loop for CG-349 (Centralize editable configuration metadata and enforce project overrides and locks)

- Review loop: 4 rounds, $10.46 cumulative work/revise/review cost; head lineage a53465f7968951e93fd9aae23ffd55283235f28c, 47587f7427ae5c8c6f22c924fc3f763c92f1e0b6, b75e5a7a55e91d533c7431a3796f5584b19857ac, 828a57a621bb9d525410dee64b31d12389359999; cause: unknown; actionable evidence: Project-aware scheduler and workflow behavior is consistent, but plain inherited locks required by the policy contract are rejected rather than enforced.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-349 (Centralize editable configuration metadata and enforce project overrides and locks) in run 20260909T112042Z-revise

- The repository has no configured typecheck command, so no separate typecheck could be run.
- Declined review improvement: Add UI scope mapping changes for api.py, phase.py, task.py, and trellis.py. — Inspection showed all four consumers already route affected stack status/readiness behavior through project-aware scheduler helpers; there is no remaining rendered behavior to change.

### 2026-09-09 · reported by CG-349 (Centralize editable configuration metadata and enforce project overrides and locks) in run 20260909T122050Z-revise-2

- Declined review improvement: Add optional UI scope mapping for api.py, phase.py, task.py, and trellis.py. — This head-bound revision has no rendered behavior change, and the approved configuration-policy implementation should not be widened or inaccurately labeled as a visual change.

### 2026-09-09 · reported by CG-349 (Centralize editable configuration metadata and enforce project overrides and locks) in run 20260909T125257Z-revise

- Declined review improvement: Add optional UI scope mapping or captures for api.py, phase.py, task.py, and trellis.py — Inspection confirmed these modules only consume the already-shared stack policy and this revision changes no rendered HTML, CSS, or interaction behavior.

### 2026-09-09 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260909T133530Z-revise

- No type-check command is configured in pyproject.toml; the repository dev dependencies define pytest and Ruff only.

### 2026-09-09 · review loop for CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one)

- Review loop: 4 rounds, $11.66 cumulative work/revise/review cost; head lineage 06a910e68da108b42c73b07d344028dc5b446739, cd297caa8ca5d97d6e1fc885904ac491f6359a4d; cause: unknown; actionable evidence: Core pool routing passes focused tests, but operating-profile pools are ignored and pooled persona completion events lose member attribution.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-351 (Compare total cost with average cost per task and activity counts on the Costs page) in run 20260909T135706Z-work

- No configured type-check command or type-checker executable was present in the prepared environment.

### 2026-09-09 · reported by CG-349 (Centralize editable configuration metadata and enforce project overrides and locks) in run 20260909T151343Z-revise

- An unrelated pre-existing docs/design/snapshot.json modification remained in the worktree and was intentionally excluded from the commit.

### 2026-09-09 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260909T142016Z-revise

- Three required context-garden reading-list paths were absent from this checkout: context-garden/product.md, context-garden/phase-06/goals.md, and context-garden/phase-05/specs/cost-aware-model-routing.md.
- Declined review improvement: Optional UI scope mapping for src/garden/web/pages/task.py and src/garden/web/templates/costs.html — No rendered behavior changed in this revision, and the frozen validation plan identifies no visual paths; additional UI mapping or captures would not verify the reported backend defects.

### 2026-09-09 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260909T173302Z-revise

- Three reading-list paths under context-garden/ were absent from this worktree; their relevant content was supplied inline in the task brief.

### 2026-09-09 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260909T175722Z-revise-2

- The referenced context-garden files were absent from this worktree, though their substantive content was included in the task brief.
- The GitHub Actions status check lacked gh authentication; local repository checks were used to distinguish this from a branch regression.

### 2026-09-09 · review loop for CG-352 (Make the sidebar operating profile a clear Economy-to-Fast slider)

- Review loop: 4 rounds, $5.86 cumulative work/revise/review cost; head lineage 3e417887deca8bed63e250f61437a9ca0ade55be, 9a4db7a9594cab1969677851432f29d878270267, 782c488048862834ac36d9630fbbbacb70be1db7, ea6622e93d385e497db1a06001cc7e332ae87c30; cause: unknown; actionable evidence: The slider behavior is broadly covered and the focused checks pass, but the successful plain-config transition renders an inaccurate meaning line.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-350 (Edit every Configuration setting in the web app with clear help and project policy feedback) in run 20260909T222919Z-work

- The referenced phase specification context-garden/phase-06/specs/web-configuration.md was absent from the supplied branch, so the task goal and CG-349 shared metadata contract served as the design source.
- The configured Playwright browser executable was unavailable locally; running-page inspection used the documented Windows Edge fallback.

### 2026-09-09 · reported by CG-350 (Edit every Configuration setting in the web app with clear help and project policy feedback) in run 20260909T224324Z-revise

- No typecheck command or configured type checker was found in pyproject.toml, docs/test-suites.md, scripts, or a Makefile.

### 2026-09-09 · reported by CG-350 (Edit every Configuration setting in the web app with clear help and project policy feedback) in run 20260909T225408Z-revise

- No mypy or pyright executable/typecheck configuration is available in the prepared environment.

### 2026-09-10 · review loop for CG-350 (Edit every Configuration setting in the web app with clear help and project policy feedback)

- Review loop: 4 rounds, $5.31 cumulative work/revise/review cost; head lineage e9aaa2b10ca1d2d7fda54dbfc1127205bbed1b23, 78bd4ae1cda599bde0041b7e5ab8c1ddece59528, 2633e911264a685fbe163c0fa3a9e509b34f847f, b00d5a619e0b585090d48a1121ed5354fd8c4620; cause: unknown; actionable evidence: Most editor behavior is covered, but scalar string-or-list values still do not round-trip safely.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260910T023139Z-revise

- The brief-listed context-garden/product.md and context-garden/phase-06/goals.md files were absent from this product checkout.

### 2026-09-10 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260910T031241Z-revise

- The listed context-garden/product.md and context-garden/phase-06/goals.md files were absent from this product checkout; their relevant contents were included in the supplied brief.

### 2026-09-10 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260910T041105Z-revise

- The two context-garden reading-list paths were absent from this worktree; the supplied inlined product and phase context was used instead.

### 2026-09-10 · review loop for CG-417 (Reuse a fresh task snapshot within one controller operation)

- Review loop: 4 rounds, $5.27 cumulative work/revise/review cost; head lineage 2cdbfdb0ca2eea272f06785bf3d4e932518a029f, 2eee4c8b9bd7114ac4e386ad62f977d505fc87e3, 922e89c826ec0a992b0f430cd24eb3c74f684b6d, 4ab1310c2465e2bf88e14c5dddf7012aa6671317; cause: unknown; actionable evidence: The snapshot reuse and freshness behavior are correctly implemented and proportionately verified.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260910T050124Z-revise

- The listed context-garden/product.md and context-garden/phase-06/goals.md files were absent from the assigned product checkout; their relevant contents were available inline in the task brief.

### 2026-09-10 · reported by CG-350 (Edit every Configuration setting in the web app with clear help and project policy feedback) in run 20260910T054801Z-revise

- The review diagnosis suggested combining the profile imports, but the repository's Ruff configuration requires separate import lines plus a blank line before the class.

### 2026-09-10 · reported by CG-515 (Support provider-neutral source control with scoped certificate and proxy policy) in run 20260910T113703Z-work-3

- The stacked parent currently has a failing `tests/scheduler/test_poll.py::test_manual_pr_refresh_records_current_head_conflict_without_action`; its fake PR mutation is replaced during repository refresh. The source-control-focused suites are clean.

### 2026-09-10 · reported by CG-518 (Enforce filesystem and network sandboxes for planning and approved tools) in run 20260910T113702Z-work-2

- The brief referenced a Stripe environment document that was unavailable; it was not needed for the sandbox implementation.

### 2026-09-10 · reported by CG-517 (Separate authenticated worker ingress from operator control access) in run 20260910T113702Z-work

- The brief requested a final typecheck, but the repository exposes no standalone typecheck configuration or command; focused tests and the required Ruff command were run.

### 2026-09-10 · reported by CG-518 (Enforce filesystem and network sandboxes for planning and approved tools) in run 20260910T115540Z-revise-2

- The brief requested a typecheck, but the repository exposes no configured typecheck command.

### 2026-09-10 · reported by CG-515 (Support provider-neutral source control with scoped certificate and proxy policy) in run 20260910T115540Z-revise

- No project typecheck command is configured.
- A broader scheduler run exposed existing fixture-dependent failures where FakeGitHub overwrites manually assigned heads from an unpushed bare remote; focused changed-area suites remained green.

### 2026-09-10 · reported by CG-520 (Deliver typed notifications through approved destination adapters) in run 20260910T125207Z-work-2

- No project typechecker is configured.

### 2026-09-10 · reported by CG-518 (Enforce filesystem and network sandboxes for planning and approved tools) in run 20260910T132540Z-revise

- No enforcing platform wrapper was installed in the worker environment, so the Linux tests verify rejection of a dishonest wrapper rather than executing an external production wrapper; macOS and WSL were unavailable.

### 2026-09-10 · review loop for CG-518 (Enforce filesystem and network sandboxes for planning and approved tools)

- Review loop: 4 rounds, $10.04 cumulative work/revise/review cost; head lineage 976fbba95708f2bf53ad27d30a0fdf8fd329745d, cecda73229f21ca37415f0868633b0052cb9e1bb, 5f2bc7f57ef02d3e31809fc94bd9e8bfe08b3089, 3649f57481e5d4183823aed2b3906b7e5bed3741; cause: unknown; actionable evidence: Two filesystem-boundary defects prevent required sandboxed execution from working and from being meaningfully validated.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-520 (Deliver typed notifications through approved destination adapters) in run 20260910T140313Z-revise-2

- The full-suite PTY result exposed only its failing node through pytest cache; the isolated node rerun passed.

### 2026-09-10 · review loop for CG-520 (Deliver typed notifications through approved destination adapters)

- Review loop: 4 rounds, $5.17 cumulative work/revise/review cost; head lineage ea22a114fd95913ca2b1351a8e7849cf8b44123f, 5c50a830a417abb4199425336319986acfd69742, d7163a8e69ec328f42b264a229df70b01e5d6895, b5b4ab8b16061b9db85af506e038236ceb97e6bb; cause: unknown; actionable evidence: Typed destination delivery, disclosure filtering, bounded retries, lifecycle classification, durable retry state, and scheduler integration satisfy the task.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-520 (Deliver typed notifications through approved destination adapters) in run 20260910T143019Z-revise

- The full ordinary suite had one unrelated transient web cache-generation assertion failure; its single permitted isolated rerun passed.

### 2026-09-10 · reported by CG-531 (Add an ontologist persona for precise and extensible data models) in run 20260910T150651Z-work

- Focused pytest collection fails before tests run because src/garden/runs.py imports garden.hosts.locking, whose package initializer imports drain.py and re-imports RunStore.

### 2026-09-10 · reported by CG-539 (Show check commands and outcomes on run pages) in run 20260910T150655Z-work

- Focused pytest collection is blocked by an existing circular import in the base checkout.

### 2026-09-10 · reported by CG-539 (Show check commands and outcomes on run pages) in run 20260910T152222Z-revise

- No configured static type checker is declared in pyproject; compilation was used as the available syntax validation.

### 2026-09-10 · reported by CG-540 (Reconcile deferred notices and attention ownership) in run 20260910T153920Z-work

- Focused pytest collection is blocked by the existing garden.runs/garden.hosts.drain circular import.

### 2026-09-10 · reported by CG-539 (Show check commands and outcomes on run pages) in run 20260910T160637Z-revise

- The repository has no configured typecheck command, so separate typecheck validation was not available.

### 2026-09-10 · review loop for CG-539 (Show check commands and outcomes on run pages)

- Review loop: 4 rounds, $4.03 cumulative work/revise/review cost; head lineage 73a3ccac78544886d201ad44455ee7c3cef2cb40, 229364100896c64dd346ce059b260396749bfe91, 4185a63d421a18aeb382aa13805e9633fdeac813, 7c7b2418e03fc93970dea6488904ed5212abc3a4; cause: unknown; actionable evidence: The run-page presentation distinguishes process and validation state well, but setup outcomes are not reliably kept separate from configured commands.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-515 (Support provider-neutral source control with scoped certificate and proxy policy) in run 20260910T163042Z-revise

- The branch had been rebased onto a stale local main and included obsolete stacked CG-396 implementations; isolating the seven provider commits against current origin/main was required.

### 2026-09-10 · review loop for CG-515 (Support provider-neutral source control with scoped certificate and proxy policy)

- Review loop: 4 rounds, $14.86 cumulative work/revise/review cost; head lineage f87232dfebcb732a3d000fb56962167839db5d9e, 5f3d34feb8e816edfb0a0c7ac0d033aaf6c25061, d1ae5ac0a1df7f24e049acaacf180de53cd37560, 0d9f83ce90a132596d5268cabfafd6da7591478d; cause: unknown; actionable evidence: The provider boundary is substantially implemented, but the REST error rewrite regresses GitHub rate-limit and authentication diagnostics.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-516 (Resolve scoped workload identities and secret references at the execution boundary) in run 20260910T163042Z-revise-2

- The supplied missing specification path did not resolve, as already recorded in the brief.

### 2026-09-10 · review loop for CG-516 (Resolve scoped workload identities and secret references at the execution boundary)

- Review loop: 4 rounds, $9.67 cumulative work/revise/review cost; head lineage c528848b5a4a424eadf5002a8c8add44108435f9, 6949a2208f0c2d94607ecf4d8ffa249bb932146b, 8b20ac119d1c8beb3dcf3bbcb10bfb43b72c50a7; cause: unknown; actionable evidence: Managed-remote credential handling still persists raw worker output before redaction, and the focused identity/remote-worker suite fails.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-518 (Enforce filesystem and network sandboxes for planning and approved tools) in run 20260910T165139Z-revise

- The configured GitHub Actions analyser cannot authenticate because this worker has no GH_TOKEN; task rules also prohibit pushing, so the controller must publish and obtain exact-head hosted CI.

### 2026-09-10 · reported by CG-516 (Resolve scoped workload identities and secret references at the execution boundary) in run 20260910T171024Z-revise

- The requested accepted-main execution comparison could not be run without entering or creating another checkout, which the dispatch rules prohibit; accepted-main behavior was compared by source inspection instead.

### 2026-09-10 · review loop for CG-576 (Deliver controller-owned CI diagnostics to isolated workers)

- Review loop: 4 rounds, $4.86 cumulative work/revise/review cost; head lineage a53a22206be1e12fc3369af0c6f7027d64219791, c683354d239dd555df81352fde11c3c7dd130fce, 5d096c66eaa3ef143bf6ff680e57f4e30c19b473, 5367e20050de4ea0ee7562f419b13088385dc961; cause: unknown; actionable evidence: Controller-owned diagnostics are locally isolated, bounded, and head-bound, but authorization headers can still leak credential values into worker briefs.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-542 (Index durable remote claim request identities) in run 20260910T185512Z-revise

- The initially named focused API test path did not exist; the applicable remote API coverage is in tests/test_remote_worker.py.

### 2026-09-10 · reported by CG-580 (Align QA request timeouts with advertised deadlines) in run 20260910T191147Z-revise

- No project type-checker or type-check command is configured in this worktree.

### 2026-09-10 · reported by CG-580 (Align QA request timeouts with advertised deadlines) in run 20260910T192359Z-revise

- No repository typecheck command or configured typechecker was available.

### 2026-09-10 · reported by CG-580 (Align QA request timeouts with advertised deadlines) in run 20260910T194217Z-revise

- No static type-check command is configured or installed in this worktree.
