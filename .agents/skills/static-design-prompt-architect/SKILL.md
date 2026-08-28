---
name: static-design-prompt-architect
description: Create controlled static graphics with native image generation when explicitly requested, or return complete generator-ready prompts for posters, flyers, business cards, menus, labels, covers, advertisements, and text-led social assets. Do not use for DTP, external rendering, or publishing.
metadata:
  short-description: Create static graphics and controlled design prompts
---

# Static Design Prompt Architect

Create a designed static graphic or a final prompt pack for one. The shared core is a coherent, standalone prompt that controls attention order, layout, image, typography, and finish as one system.

This skill works in two modes:

- **Standalone mode:** turn the user's ordinary brief into a prompt pack. Ask one concise question only when a missing choice materially changes the format, exact copy, reference authority, or execution route. Otherwise state a reversible assumption.
- **Connected mode:** accept a supplied `workflow_context` or any subset of `brief_contract`, `direction_contract`, `copy_pack`, `reference_pack`, `asset_manifest`, `qa_requirements`, `target_generator`, `target_generator_profile`, and `host_environment`. Preserve supplied locks. Do not require or invoke any named external skill.

## Output modes

Resolve the requested outcome before authoring or rendering:

- **`render`:** use when the user explicitly asks to create, generate, render, or make the static graphic. Build the complete eight-stage prompt internally, run the pre-render feasibility gate, then use only the active surface's built-in image-generation capability when available. Return the generated graphic; do not include the full prompt unless the user also asks for it.
- **`prompt`:** use when the user explicitly asks for a prompt, prompt pack, prompt revision, or copyable generator instruction. Return one complete standalone prompt in one fenced code block. Do not render an image.
- **`render_and_prompt`:** use when the user explicitly asks for both. Return the generated graphic and the exact final prompt in one fenced code block.

If the request does not make the desired outcome clear, ask one concise question: `Wygenerować grafikę czy przygotować gotowy prompt?` Never trigger a render from an ambiguous brief alone.

Native rendering is not permission to use an external provider, API, connector, upload, or paid service. If built-in image generation is unavailable, return `rendering_unavailable` and the complete final prompt instead of substituting another tool. If the pre-render gate returns `dtp_required`, do not render.

## Inputs

Minimum viable input:

- asset type and communication objective;
- audience or use context;
- required visible copy, if any;
- intended output format or placement.

Use supplied references only for their declared roles: identity, product truth, composition, style, light, material, typography, or scoped edit source. If a reference role is absent, do not let it silently override identity, logo, exact copy, or product geometry.

## Operating rules

1. Resolve the task as `generate`, `layout`, `reference-guided`, `edit`, or `variation`.
2. Identify the communication intent and first, second, and third notices. Reject equal-weight collage logic unless the brief explicitly requires it.
3. If the user did not name an exact generator and surface, keep the prompt provider-neutral. Mark native output size, reference count, font fidelity, editing behavior, seed behavior, and negative-prompt syntax as `Unknown` rather than inventing support. Apply the optional Codex compatibility profile only when connected context explicitly declares `host_environment: codex`, `final_asset_has_visible_text: true`, and `target_generator: openai/gpt-image-2`.
4. Classify each requested control as `native-setting`, `prompt-semantic`, `reference-conditioned`, `external-qa`, `unsupported`, or `Unknown`. Put native settings outside the executable prompt only when they are verified for the selected surface. Resolve `task_mode` and `negative_handling_mode`; do not add a separate negative-prompt field unless the selected surface verifies one.
5. For a poster, flyer, business card, menu, label, cover, key visual, advertising graphic, or text-led social asset, read [the unified static prompt contract](references/unified-static-prompt-contract.md) and compile one complete prompt in its fixed eight-stage order.
6. Read [capability and reference rules](references/capability-and-reference-contract.md) before handling references, exact copy, or a selected generator. Read [deliverable profiles](references/deliverable-profiles.md) when the asset type needs a tested design grammar. Read [workflow integration](references/workflow-integration.md) only when structured context or a handoff is present. Read [QA and repair](references/qa-and-repair.md) before reviewing a rendered result or recommending another pass.
7. Use one complete `unified-multistage-static` prompt by default. The stages describe assembly priority inside one generation; never ask for intermediate images, separate layer files, or later text insertion.
8. Use `separated-production` only when the user explicitly requests it or a verified near-final render needs a narrow scoped repair. State the reference handoff, preserved elements, exact permitted change, and limitations.
9. Quote every required visible string. Declare its hierarchy, placement, line-break logic, colour role, and allowed text count. Keep copy concise. For a documented single-word spelling failure, use a scoped edit and spell only that word letter by letter.
10. Run the copy-feasibility preflight before authoring a prompt. If mandatory small text, long legal copy, prices, schedules, contact data, or print specification cannot be reduced without losing the communication objective, return `dtp_required` instead of promising that raster typography will pass.
11. For real brands, venues, institutions, partner marks, or logos, use only approved attached source assets and declared facts. If the receiving surface supports a verified official-source check, require that preflight; otherwise mark unavailable identity details as `Unknown` and do not invent them.
12. Do not promise a named font file, exact kerning, legal licensing status, flawless Polish diacritics, print readiness, or deterministic text rendering from a raster generator. Treat those as external QA or DTP requirements.
13. Do not use resolution claims or empty quality boosters such as `8K`, `4K`, `HDR`, `ultra sharp`, `hyper detailed`, `crisp`, or `razor sharp`. Describe visible material, light, layout, and legibility instead.
14. In `render` or `render_and_prompt` mode, generate only through the active surface's built-in image-generation capability after the user explicitly requested rendering. Do not call external services, select paid tools, upload files, publish, deploy, or make irreversible changes.

## Output

Use [the prompt-pack template](templates/prompt-pack.md) for complex work or a connected handoff. For a simple request that asks only for prompts, lead with the finished standalone prompt and place each complete prompt in its own fenced code block with no title inside the block.

Return at most four genuinely different variants unless the user requests evaluation rather than alternatives. Every final prompt must be complete, standalone, and ready to paste.

The output must include or make explicit:

- prompt method: `standard` unless the user explicitly requests another method;
- output mode and render status: `prompt`, `render`, `render_and_prompt`, `rendering_unavailable`, or `dtp_required` as applicable;
- generator profile and native settings: verified values or `Unknown`;
- host environment, generator prompt format, and negative handling mode;
- task mode and declared reference roles;
- design intent, attention order, layout mechanism, and type-image relationship;
- locked visible copy, exclusions, expected observables, and QA route;
- a portable `prompt_pack` handoff when connected context is present.

## Final self-check

Before returning, verify that the asset has one singular intent; every major element has a visible role; attention order is executable; text and image cooperate; required copy is quoted exactly; protected references are not repurposed; no unsupported controls are disguised as syntax; the prompt contains no backreference to a previous chat, render, or unlisted attachment; and the result has a clear pass/fail QA route. After a native render, review it against the QA contract but do not silently generate another attempt.

If the user asks to improve an existing render, work from that render. Prefer a scoped edit when only one observable defect remains; recommend a full rerender only when the hierarchy, identity, product construction, or core visual thesis fails.
