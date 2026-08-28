---
name: static-graphic-design-creator
description: Brainstorm, design, render, or refine typography-led static graphics and standalone prompts for posters, flyers, covers, advertisements, labels, cards, menus, and text-led social assets. Do not use for DTP or prepress deliverables, external rendering, or publishing.
metadata:
  short-description: Create static graphics and controlled design prompts
---

# Static Graphic Design Creator

Create a designed static graphic or a final prompt pack for one. The shared core is a coherent, standalone prompt that controls attention order, layout, image, typography, and finish as one system.

## Input contexts

- **Standalone mode:** turn the user's ordinary brief into a prompt pack. Ask one concise question only when a missing choice materially changes the format, exact copy, reference authority, or execution route. For an under-directed poster brief, use the poster-direction brainstorm instead of a generic question. Otherwise state a reversible assumption.
- **Connected mode:** accept a supplied `workflow_context` or any subset of `brief_contract`, `direction_contract`, `copy_pack`, `reference_pack`, `asset_manifest`, `qa_requirements`, `target_generator`, `target_generator_profile`, and `host_environment`. Preserve supplied locks. Do not require or invoke any named external skill.

## Output modes

Resolve the requested outcome before authoring or rendering. `input_context` and `output_mode` are separate fields.

- **`render`:** use when the user explicitly asks to create, generate, render, or make the static graphic. Build the complete eight-stage prompt internally and run the pre-render feasibility gate. In ChatGPT, use the active surface's built-in image generation when available. In Codex, invoke `$imagegen` only when that built-in Skill is available. Return the generated graphic and a concise QA status; do not include the full prompt unless the user also asks for it.
- **`prompt`:** use when the user explicitly asks for a prompt, prompt pack, prompt revision, or copyable generator instruction. Return one complete standalone prompt in one fenced code block. Do not render an image.
- **`render_and_prompt`:** use when the user explicitly asks for both. Return the generated graphic and the exact final prompt in one fenced code block.

If the request does not make the desired outcome clear, ask one concise question: `Wygenerować grafikę czy przygotować gotowy prompt?` Never trigger a render from an ambiguous brief alone.

Native rendering is not permission to use an external provider, API, connector, upload, or paid service. Set `render_status` to `not_requested`, `blocked_dtp`, `unavailable`, `generated`, `qa_pass`, `qa_fail`, or `generation_failed` as applicable. If built-in image generation is unavailable, return `render_status: unavailable` and the complete final prompt instead of substituting another tool. If the pre-render gate returns `dtp_required`, set `render_status: blocked_dtp` and do not render.

## Inputs

Minimum viable input:

- asset type and communication objective;
- audience or use context;
- required visible copy, if any;
- intended output format or placement.

Use supplied references only for their declared roles: identity, product truth, composition, style, light, material, typography, or scoped edit source. If a reference role is absent, do not let it silently override identity, logo, exact copy, or product geometry.

## Poster direction and collaboration

For a poster, flyer, cultural graphic, civic graphic, event key visual, or text-led social graphic, resolve the communication goal before selecting a style. Read [the poster style and composition atlas](references/poster-style-and-composition-atlas.md) before turning an open creative brief into a final prompt.

Use one of these collaboration routes:

- **`discovery_brainstorm`:** use when the user has not settled the poster's purpose, audience response, visual mechanism, composition, or style direction. Return two to four materially different routes, each with: communication goal; one-sentence visual thesis; composition archetype; style family or original attribute set; material treatment; reason it fits; and one trade-off. Ask the user to select, combine, or adjust a route. Do not produce a generic final prompt or render before a direction is selected.
- **`directed_collaboration`:** use when the user supplies a concrete goal, subject, composition, style, reference, or other strong creative decision. Preserve that decision. State the selected route concisely and raise at most one specific concern when the stated style, composition, copy, or format conflicts with the communication goal. Do not force a brainstorm or invent alternatives merely to appear creative.

The non-negotiable decision order is: communication goal → audience response and copy burden → visual thesis → composition archetype and attention order → style family or original visual attributes → material treatment → one eight-stage prompt. A style label may inform the final prompt only after the earlier decisions are resolved. Treat vague adjectives such as `premium`, `cinematic`, `modern`, `futuristic`, or `bold` as requests for clarification or translation into visible attributes, not as a complete style decision.

## Operating rules

1. Resolve the task as `generate`, `layout`, `reference-guided`, `edit`, or `variation`.
2. For poster-like assets, resolve `collaboration_mode` as `discovery_brainstorm` or `directed_collaboration`, then follow the objective-first order in the poster atlas. Never let a style label choose the message, hierarchy, or composition by default.
3. Identify the communication intent and first, second, and third notices. Select a composition archetype that makes those notices observable. Reject equal-weight collage logic unless the brief explicitly requires it.
4. If the user did not name an exact generator and surface, keep the prompt provider-neutral. Mark native output size, reference count, font fidelity, editing behavior, seed behavior, and negative-prompt syntax as `Unknown` rather than inventing support. Apply the optional Codex compatibility profile only when connected context explicitly declares `host_environment: codex`, `execution_surface: codex_builtin_imagegen`, `generator_provider: openai`, `final_asset_has_visible_text: true`, and `target_generator: gpt-image-2`.
5. Classify each requested control as `native-setting`, `prompt-semantic`, `reference-conditioned`, `external-qa`, `unsupported`, or `Unknown`. Put native settings outside the executable prompt only when they are verified for the selected surface. Resolve `task_mode` and `negative_handling_mode`; do not add a separate negative-prompt field unless the selected surface verifies one.
6. For a poster, flyer, business card, menu, label, cover, key visual, advertising graphic, or text-led social asset, read [the unified static prompt contract](references/unified-static-prompt-contract.md) and compile one complete prompt in its fixed eight-stage order.
7. Read [capability and reference rules](references/capability-and-reference-contract.md) before handling references, exact copy, or a selected generator. Read [deliverable profiles](references/deliverable-profiles.md) when the asset type needs a tested design grammar. Read [workflow integration](references/workflow-integration.md) only when structured context or a handoff is present. Read [QA and repair](references/qa-and-repair.md) before reviewing a rendered result or recommending another pass.
8. Use one complete `unified-multistage-static` prompt by default. The eight stages describe assembly priority inside one generation, not mandatory headings or a fixed length. Compress irrelevant stages, avoid mechanical repetition, and repeat only critical locks that must remain fixed. Never ask for intermediate images, separate layer files, or later text insertion.
9. Use `separated-production` only when the user explicitly requests it or a verified near-final render needs a narrow scoped repair. State the reference handoff, preserved elements, exact permitted change, and limitations.
10. Quote every required visible string. Declare its hierarchy, placement, line-break logic, colour role, and allowed text count. Keep copy concise. For a documented single-word spelling failure, use a scoped edit and spell only that word letter by letter.
11. Resolve `production_intent` as `concept_raster`, `digital_final`, or `production_master`, then run the copy-feasibility preflight. If mandatory small text, long legal copy, prices, schedules, contact data, exact print typography, or print specification cannot be reduced without losing the communication objective, return `dtp_required` instead of promising that raster typography will pass.
12. For real brands, venues, institutions, partner marks, logos, or people, use only approved attached source assets and declared facts or likeness authority. If the receiving surface supports a verified official-source check, require that preflight; otherwise mark unavailable identity details as `Unknown` and do not invent them. Translate a requested artist, artwork, brand, or historical movement into original high-level visual attributes rather than imitating it directly.
13. Do not promise a named font file, exact kerning, legal licensing status, flawless Polish diacritics, print readiness, or deterministic text rendering from a raster generator. Treat those as external QA or DTP requirements.
14. Do not use resolution claims or empty quality boosters such as `8K`, `4K`, `HDR`, `ultra sharp`, `hyper detailed`, `crisp`, or `razor sharp`. Describe visible material, light, layout, and legibility instead.
15. In `render` or `render_and_prompt` mode, generate only through the active surface's built-in image-generation capability after the user explicitly requested rendering and the objective-first poster direction is resolved. Do not call external services, select paid tools, upload files, publish, deploy, or make irreversible changes. If generation fails, report `render_status: generation_failed`, preserve the final prompt, and stop.

## Output

Use [the prompt-pack template](templates/prompt-pack.md) for complex work or a connected handoff. For a simple request that asks only for prompts, lead with the finished standalone prompt and place each complete prompt in its own fenced code block with no title inside the block.

Return at most four genuinely different variants unless the user requests evaluation rather than alternatives. Every final prompt must be complete, standalone, and ready to paste.

The output must include or make explicit:

- input context, prompt method (`standard` unless the user explicitly requests another), and `production_intent`;
- output mode: `prompt`, `render`, or `render_and_prompt`;
- render status and QA route: verified values from the declared status set, or `Unknown`;
- generator profile, native settings, and native availability: verified values or `Unknown`;
- host environment, generator prompt format, and negative handling mode;
- task mode and declared reference roles;
- design intent, collaboration mode, attention order, composition archetype, layout mechanism, style treatment, material treatment, and type-image relationship;
- locked visible copy, exclusions, expected observables, and QA route;
- a portable `prompt_pack` handoff when connected context is present.

## Final self-check

Before returning, verify that the asset has one singular intent; its composition archetype follows that intent; style is a consequence of the chosen strategy rather than a substitute for it; every major element has a visible role; attention order is executable; text and image cooperate; required copy is quoted exactly; protected references and likeness rights are not repurposed; no unsupported controls are disguised as syntax; the prompt contains no backreference to a previous chat, render, or unlisted attachment; and the result has a clear pass/fail QA route. Run the anti-slop composition gate in the poster atlas. After a native render, review it against the QA contract and report the result, but do not silently generate another attempt.

If the user asks to improve an existing render, work from that render. Prefer a scoped edit when only one observable defect remains; recommend a full rerender only when the hierarchy, identity, product construction, or core visual thesis fails.
