# Web configuration with project policy

Status: proposed, phase-06 freeze applies. Requested by Josh on 2026-09-06: web editing for every option listed on Configuration, clear meanings/tooltips, and project-based overrides that can prohibit configuring an option.

## Outcome

A person can understand and edit the settings listed on the Configuration page without hand-editing YAML. They can see the effective value, where it came from, the scope being edited, and when a change takes effect. A project can override a setting and can lock it against changes. Locked settings remain visible with an explanation.

Interpretation of project: an existing garden product/project configuration scope, not a new organizational hierarchy. Distinguish a project value override from a project policy that prohibits editing. Existing value inheritance remains authoritative; do not silently change precedence to implement the UI.

## Coverage and presentation

Inventory every setting and nested collection displayed by the current Configuration page and map each to an editable control or an explicit policy/derived-value explanation. Include operating/observation profiles, worker and review limits, dispatch/revision switches, review settings/ladder, budgets, timing, GitHub options and any other displayed configurable key. Computed summaries are explained, not edited as if independent settings. Use shared configuration metadata for type, valid range/choices, default, scope support, units, explanation and application semantics, avoiding a second divergent schema in templates.

Every setting needs plain-language help stating what it controls and the practical effect of changing it. For example, distinguish requested parallelism from total process/resource limits; explain costs of review rounds and time units. Show important consequences inline; tooltips or expandable help must work with keyboard, touch and screen readers and cannot be the only place a critical constraint appears. Lists/maps need structured add/remove/edit flows with useful validation. Preserve unknown extension keys when editing known settings.

## Scopes, overrides and locks

Show global and selected-project scopes explicitly. Display stored and effective values with provenance (default, config file/environment overlay, project override, profile or runtime override as applicable), plus inheritance/reset controls. Offer a project override only where the engine actually supports project scope; explain global-only fields rather than saving an override the engine ignores.

A project policy can mark named settings non-editable and optionally enforce a value. Explain the lock reason and policy source. Locked inherited settings must not change indirectly through global edits, profile selection, bulk updates, reset-to-default, API calls or runtime overrides. Reject an upstream change that would alter a project's locked effective value unless policy defines a permitted resolution. Validate that initial policy installation is internally consistent; stale overrides cannot win over an enforced policy value.

Policy management is a distinct trusted operation; an ordinary configuration edit cannot remove its own lock. Integrate the existing trusted-author/config-fence model rather than inventing an unrequested enterprise role system. Document who may change project policy and how a legitimate policy owner restores editability. Enforce locks and schema validation at the shared mutation boundary so web, API, CLI, profiles and reloads cannot disagree; a disabled HTML control alone is insufficient. Direct policy-file changes remain controlled by existing filesystem/repository trust.

## Saving and application

Preview changed values, scope and effect, save atomically through the existing configuration mechanisms, and prevent stale browser forms overwriting newer edits. Invalid or forbidden changes make no partial mutation. Distinguish saved, effective now, pending safe reload, restart required and held by an in-flight fence. Preserve the existing fence/reload protections (CG-242/288/291) and never restart active checks implicitly. Give an actionable next step when a valid change cannot yet take effect. Resets remove an allowed override rather than copying today's inherited value.

Do not expose secret values through the page, help, diffs, validation, logs or API responses. Edit secret references where appropriate; represent configured secrets without sending existing plaintext to the browser. Record a redacted audit entry with changed keys, scope, provenance and actor information available under the current trust model.

## Evidence

A coverage inventory connects each current Configuration option to a control, help and validation, or a justified derived/global-only/locked presentation. Backend tests prove project isolation, enforced-value precedence, indirect profile/global/API bypass rejection, atomic invalid saves, conflict handling and safe reload behavior. Browser journeys on an isolated actual app create a project override, save/reload it, reset inheritance, inspect help with keyboard, encounter a project lock, attempt its API bypass and observe a restart-required/held change without disrupting a run. Record before/after effective values and outcomes; screenshots alone do not establish correctness. Missing browser evidence remains UNPROVEN.

## Scope and scheduling

Keep the existing Configuration information architecture where useful; design is an invitation, not a prescribed layout. This feature does not unblock phase-05 stabilization by itself. File and preserve it in frozen phase 06; do not dispatch until the gate passes or Josh explicitly lifts the hold.

## Tracking

- CG-349: Centralize editable configuration metadata and enforce project overrides and locks
- CG-350: Edit every Configuration setting in the web app with clear help and project policy feedback
