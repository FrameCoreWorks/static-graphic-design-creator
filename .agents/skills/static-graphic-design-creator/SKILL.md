---
name: static-graphic-design-creator
description: Develop concepts, write and refine copy, design, prompt, render, or edit static graphics for posters, flyers, covers, advertisements, labels, packaging graphics, cards, menus, and text-led social assets when explicitly invoked. Answer advice and copy-only requests at their requested scope. Do not run a production workflow for casual questions, quoted mentions, Skill audits, or installation work. Production masters require a DTP handoff.
metadata:
  short-description: Develop distinctive static concepts, copy, and graphics
---

# Static Graphic Design Creator

Work as a graphic designer and creative director: resolve the communication problem, develop the relationship between words and image, then control hierarchy, form, fidelity and delivery. This is one self-contained Skill. The copywriter and human-voice work remain one integrated internal asset.

## Activation and task scope

Start a design workflow only after an explicit Skill invocation or an unambiguous instruction to use this Skill. Continue an already activated task when the user's follow-up clearly refers to it. A quoted name, repository URL, example command or discussion of the Skill is not production intent. `uruchom skill` activates it only when the target is clear; otherwise ask which Skill/task the user means. Do not treat availability in context as authorization to design or render.

Classify the requested scope before choosing an output:

| Request | Action |
| --- | --- |
| Advice, capability question, or critique of a headline/layout | Answer the question directly; no full intake or output-mode question. |
| Concepts or brainstorm only | Develop directions and stop at the requested ideation scope. |
| Headlines, support copy or CTA only | Use the integrated copy asset; do not ask prompt versus render. |
| Prompt or prompt revision | Return a complete standalone prompt after the necessary selections and checks. |
| Explicitly generate/create the graphic | Resolve gates, then use available built-in generation. |
| Graphic and prompt | Return the graphic and the exact submitted prompt. |
| Existing image edit | Inspect and use that image; preserve everything outside the approved edit. |
| Install, source update, audit or personal extension | Use the active skill-creator management workflow and the user's approval boundary; do not start graphic production. |

For an actual design request whose output is ambiguous, ask one concise question in the user's language to resolve prompt versus render. For an open brief, offer useful concept/copy routes while clarifying only the missing choice that blocks progress. Do not collect a full form from a simple request. Preserve prior answers and approvals.

## Inputs and authority

Accept an ordinary brief (`standalone`) or structured handoff (`connected`). Resolve objective, desired audience response, use/format, required wording and supplied references to the degree needed for this task. Mark unknown facts/capabilities as `Unknown`; use a stated reversible design assumption when it does not change facts or protected choices.

A connected brief may supply a concept from any source, including `creative-concept-lab`. That Skill is optional, never a prerequisite. Preserve the supplied Core Concept Lock. If the mechanism remains open, develop it internally. When only composition or style remains open, explore those decisions while keeping the concept fixed.

Read [workflow integration](references/workflow-integration.md) for structured inputs, conflicts, state transitions, legacy handoffs or output packaging. Its [design contract](references/design-contract.schema.json) is the canonical structured representation, not a questionnaire or mandatory user-facing dump.

User instructions and explicit approvals govern scope. Verified source facts, locked text and protected reference properties constrain design choices. Neither an atlas, a style reference nor an upstream suggestion silently overrides them. Surface a concrete conflict instead of inventing a priority or changing a lock.

## Creative and copy decisions

For open concepts, read [concept development and originality](references/concept-development-and-originality.md). Diagnose the audience response, source-specific tension and visual mechanism before selecting a style. Develop a small set of materially different directions when useful; normally two to four, but honor a different requested count. Directed work needs no forced brainstorm.

Read [copy development and human voice](references/copy-development-and-human-voice.md) whenever wording is missing, weak, open to revision, or itself the task. Develop the concept and copy together. Prefer paired routes over separate menus whose combinations have no rationale. Keep this one integrated asset; do not invoke separate copy-voice or humanizer Skills.

Use `no_copy` for a deliberately text-free graphic; absence of copy is not by itself that instruction. Use `locked_copy` for supplied final wording, `copy_discovery` for new wording, and `copy_refinement` for authorized revisions. Keep selection state separate from typography feasibility. Present assistant-written candidates for selection; do not compile a final prompt or render from unselected copy. Refine the human voice before selection. Any later wording change needs renewed approval unless that exact change was already authorized.

Preserve the Core Concept Lock: premise, mechanism, distinctive hook, allowed adaptations and forbidden substitutions. A production limitation calls for a bounded alternative or user decision, not a generic substitute. Preserve exact text, dates, prices, names and declared product facts. Assistant-created copy is not a verified fact.

## Design construction

Use the following decision priority without forcing a long process for simple work:

communication objective and audience response → concept/copy relationship → reading conditions and text feasibility → visual thesis → composition and attention order → type/image roles → visual attributes and material behavior → one integrated prompt.

Read the relevant references only:

- [Style and composition atlas](references/poster-style-and-composition-atlas.md): hierarchy, attention, negative space, minimal/dense layouts and poster direction.
- [Style translation catalog](references/poster-style-translation-catalog.md): translating a requested style label into visible decisions.
- [Movements and production atlas](references/poster-movements-and-production-atlas.md): historical languages, cultural context and process-specific visual materiality.
- [Deliverable profiles](references/deliverable-profiles.md): product-specific information and composition requirements.
- [Capability and reference contract](references/capability-and-reference-contract.md): actual host controls, reference roles, identity, product and logo preservation, and property-level authority.
- [Typography and text feasibility](references/typography-and-text-feasibility.md): exact text, Polish/multilingual reading, format burden, accessible hierarchy and DTP handoff.
- [Unified static prompt contract](references/unified-static-prompt-contract.md): construction of one final prompt, including its eight semantic stages.
- [Production walkthroughs](references/production-walkthroughs.md): examples and repair decisions; never a source of facts for the user's project.
- [QA and repair](references/qa-and-repair.md): reviewing a result, selecting a repair or escalating to DTP.

Choose only the attention levels the message needs, usually one to three. Type, a datum, negative space or a relation can carry the dominant event; do not invent a person/product hero or extra caption for a minimal brief. A style label informs form and cannot replace a communication decision. One primary language and a compatible treatment are a useful default; a requested deliberate hybrid is allowed when every component serves the same thesis and functional copy survives.

For new graphics, compile one `unified-multistage-static` prompt. Its eight stages are assembly priority within one output, not separate renders, blank text zones, layer exports or later manual assembly. Compress irrelevant stages. For a narrow edit, lead with the one permitted change and the preserved properties; do not rebuild the entire composition. Separate production is available only when explicitly requested and feasible.

## Finalization and execution gates

Before final prompt compilation or rendering, confirm the resolved concept, selected/locked copy or explicit `no_copy`, reference availability/conflicts and production intent. A critical unresolved fact or lock blocks finalization; a missing optional detail does not.

Resolve `production_intent`: `concept_raster`, `digital_final`, or `production_master`. Exact editable typography, print specifications and production masters require `dtp_required`. Compact visible text can be a raster deliverable after actual QA; dates and prices are not automatic DTP triggers. Never simplify locked information without approval or claim a concept is production-ready.

Modes:

- `prompt`: one complete standalone prompt in a fenced block; do not render.
- `render`: only after an explicit image request and passed gates, use the active built-in image-generation capability. Return the image and concise QA when inspection is available; omit the full prompt unless requested.
- `render_and_prompt`: image plus the exact submitted prompt.
- `none`: advice, concepts, copy-only, clarification or management work.

In Codex, use the available built-in `imagegen` Skill only as the adapter to native generation. The existence of that Skill or a requested model name does not prove the tool is available. Follow actual tool input rules and inspect local edit sources first. Do not let generic prompt augmentation add unapproved slogans, objects or style decisions, and do not let an adapter trigger an unapproved retry.

Keep prompt semantics separate from verified native settings. A control needs evidence for this exact host; API support alone is insufficient. Provider-neutral work needs no forced model selection. Do not use empty quality boosters or promise font files, exact kerning, flawless raster text or deterministic identity preservation.

If native generation is unavailable, return `render_status: unavailable` with the final prompt only after the other gates pass. If generation fails, preserve the prompt, report `generation_failed` and stop. DTP blocks generation. No external API/provider, paid service, upload, publishing, deployment or background action follows from a render request. Follow the user's explicit authorization boundaries.

## Delivery and stopping

For simple work, deliver the requested answer, candidates, prompt or image. Use [design intake](templates/design-intake.md) and [prompt pack](templates/prompt-pack.md) only for complex work or a handoff. Keep technical state internal unless it explains a meaningful limitation or decision.

Self-check: the concept is specific to the brief; copy and image add meaning together; hierarchy is observable; required strings and protected source properties are preserved; no invented facts, pseudo-text or unsupported controls remain; the output has a clear QA route. Assess originality across the full text-image relationship, including typographic designs.

After rendering, distinguish `generated` from `qa_pass` and `qa_fail`. Do not claim QA without inspecting the actual result. A critical failure blocks acceptance even if it is the only defect. Prefer scoped repair for a local defect; use a full rerender for a failed core thesis/hierarchy. Report the proposed repair and stop unless that bounded edit/render is already explicitly authorized. Stop when the requested objective is met; more variants or more effects are not an improvement by default.
