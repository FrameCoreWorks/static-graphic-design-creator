# Workflow Integration Contract

The Skill is self-contained. Accept natural-language briefs or structured inputs from any workflow. An optional concept handoff, including one from creative-concept-lab, does not create a mandatory dependency or authorize another tool call. Preserve the original handoff and its locks; do not overwrite upstream decisions during normalization.

## One canonical state

Use [design-contract.schema.json](design-contract.schema.json) for a complex design record or portable handoff. The [intake](../templates/design-intake.md) is a valid unresolved state; the [prompt pack](../templates/prompt-pack.md) is a fictional final prompt example. The schema is optional for ordinary conversation but its distinctions govern behavior. It validates data, not user intent, facts, visual quality or actual tool execution. Treat state labels as claims that need evidence from the conversation or tool result.

| Field | Owner and meaning |
| --- | --- |
| `activation`, `request_kind`, `action` | Entrypoint: why the Skill is active, what is requested, what happens next |
| `input_context`, `task_mode`, `output_mode` | Independent axes: standalone/connected, static operation, requested deliverable |
| `strategy` | Objective, audience response, reading mode, format, visual thesis, attention order, composition, type-image relation and visual treatment |
| `concept.status`, `concept.lock` | Concept asset: selected mechanism and protected adaptations |
| `copy.route`, `copy.selection_status`, `copy.items`, `copy.options`, `copy.claims` | Integrated copy asset: writing route, selection, exact strings, draft alternatives and evidence |
| `feasibility` | Typography feasibility asset: risk, reason and intended checks, independent of text selection |
| `references`, `reference_status` | Property-level reference roles, availability and conflicts |
| `host` | Observed surface, native availability, declared/known model and individually evidenced controls |
| `edit_scope` (scoped edits only) | Current image reference, the permitted change, changed/protected copy IDs and protected properties |
| `prompt` | One exact submitted or paste-ready prompt, empty while unresolved |
| `render_status`, `qa` | Actual execution/review state, never an optimistic prefilled result |

Known absence is explicit: a deliberately text-free design uses `copy.route: no_copy`; unavailable image generation is false, unobserved availability is `Unknown`. `concept.lock: null` means no concept is recorded yet. Empty draft text fields are unanswered, not verified facts. Unknown does not mean false or unsupported. Only critical unresolved information blocks the relevant action.

## Transition rules

1. For advice, copy-only, concepts or Skill management, keep `output_mode: none`. Do not enter design production from a quoted mention or casual question.
2. Final prompt, native render and unavailable-render prompt fallback require a selected/locked concept, selected/locked copy or explicit no-copy, compact/at-risk feasibility with a review plan, and no unresolved or unavailable required reference. The user may already have supplied the approved decisions.
3. `offer_concepts`, `offer_copy`, `clarify` and DTP routing contain no final generator prompt. Candidate copy is held in `copy.options`, not appended as extra visible text.
4. `native_render` is the pending permitted action: `render_status` is still `not_requested` before the call. It requires a direct render request and positively observed built-in availability. After a returned image, move to `review` with `generated`. Only actual inspection can produce `qa_pass` or `qa_fail`. A failed review records `qa.status: fail` and `render_status: qa_fail` together. If the tool failed, use `report_generation_failed`; if unavailable/undiscoverable, `report_unavailable` only after other finalization gates pass.
5. A failed critical QA item blocks acceptance. A proposed repair is not an automatic second tool call; preserve the prior artifact and obtain or reuse authorization for that bounded edit.
6. An exact user-specified replacement is already approved. Other lexical changes to selected copy invalidate that item's selection. A changed core mechanism returns concept selection to the user unless explicitly included in allowed adaptations.
7. Required text is independent of role: legal detail may be mandatory metadata. Claim verification is per claim, not inferred from `source_locked` wording.

## Scoped-edit state

Before finalizing `task_mode: edit`, provide `edit_scope.source_reference_id`, `change`, `changed_copy_ids`, `protected_copy_ids` and `protected_properties`. A missing source may remain an unresolved clarification state without a final edit scope. Before execution, the source must be an available current-request reference with role `edit_source`. Changed and protected copy IDs are disjoint and together account for the known copy inventory. Quote every changed string in the edit prompt; unchanged strings may be preserved through the actual image source and explicit protection instead of repeating the whole poster. Do not use this exception for a fresh render or omit a changed string. A declared scope is not evidence of authorization; validate it against the user's actual request.

## Legacy input mapping

| Legacy field | Canonical destination and guard |
| --- | --- |
| `workflow_context`, `brief_contract`, `direction_contract`, `poster_strategy` | Normalize supplied objective and design fields into `strategy`; preserve the original source values and report conflicts |
| `concept_lock` / Core Concept Lock | `concept.lock`; map core premise, creative rule and hook; retain other supplied concept context in `source_context` when present |
| `copy_pack.locked_strings`, `visible_copy.locked_strings` | Stable `copy.items` only when upstream explicitly identifies final wording; preserve exact strings and actual authority |
| `copy_pack.selected_copy` | Items for headline, support, CTA and metadata; no optional field may be invented or silently omitted |
| `copy_fit: selected / locked / needs_selection` | `copy.selection_status`; assess typography feasibility separately |
| `copy_fit: dtp_required` | `feasibility.status: dtp_required`; it says nothing about whether wording was selected |
| `copy_locks` | Attach permissions and source authority to the corresponding item IDs; resolve ambiguous matches |
| `reference_pack`, `asset_manifest` | Available approved references with role/property mappings; missing files remain unavailable |
| `target_generator_profile`, rendering context | `host`; a declaration is not proof of native controls |

Never merge contradictory exact strings or silently discard unmapped protected fields. Keep the source handoff alongside the normalized record; ask only when an unresolved mapping affects the requested result. Use per-item and per-reference stable IDs; reject duplicate IDs. Preserve source locks across serialization, variants, localization and edits.

## Host compatibility and optional Codex crosswalk

Use actual tool schema and observed host behavior first, then current official surface documentation, then model/API documentation; a user's declared target is intent, not capability evidence. Set unknown controls to `Unknown`. Do not infer a model ID from the ChatGPT/Codex product name. A built-in imagegen Skill can describe a CLI fallback, but this Skill does not authorize that fallback.

A connected handoff explicitly declaring Codex, `codex_builtin_imagegen`, OpenAI, text-bearing output and `gpt-image-2` may retain those declarations as context. It does not enable native settings. Use integrated constraints unless the selected surface actually verifies a separate negative field. Request references must be available in the receiving context; a conversational alias alone is not an attachment.

A receiving workflow's six-section format may map the canonical eight semantic stages without dropping decisions:

| Eight-stage semantics | Six-section destination |
| --- | --- |
| Final-output contract | Final-output contract |
| Background + layout and attention | Background and spatial foundation |
| Hero/protected assets | Hero and source-locked assets |
| Supporting elements | Supporting graphic elements |
| Typography and functional information | Typography and functional information |
| Colour, light, material | Distribute into the relevant preceding sections |
| Finish, exclusions, acceptance | Finish and exclusions |

These are prompt sections, not multiple renders, layer exports or a default later text overlay. For narrow edits, lead with the permitted change and protected properties rather than forcing six or eight headings. Respect the active host's output/save rules and distinguish a local artifact from a saved installed Skill or a published deliverable.
