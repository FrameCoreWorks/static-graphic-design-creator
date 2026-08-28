# Capability and Reference Contract

## Capability classification

Resolve the exact model version and execution surface before claiming sensitive controls. A model name alone is insufficient because web UI, mobile app, API, and hosted wrappers may expose different fields.

| Status | Use |
| --- | --- |
| `native-setting` | Put it in a verified user-interface or API field, outside the executable prompt. |
| `prompt-semantic` | Express it as visible natural-language direction. |
| `reference-conditioned` | Use it only when the needed image, layout, mask, or source asset is attached to that request. |
| `external-qa` | State it as a post-render acceptance check. |
| `unsupported` | Omit it from the prompt and disclose the limitation. |
| `Unknown` | Do not infer support from another model or product surface. |

Keep native output size, aspect selection, reference count, seed, masks, weights, negative-prompt syntax, and edit fields outside the prompt unless verified for the selected surface. Never put resolution claims, pixel dimensions, megapixels, `8K`, `4K`, `2K`, `UHD`, or `HD` inside a prompt.

## Generator prompt format and portability

Record `task_mode`, `execution_surface`, `generator_provider`, `target_generator`, `negative_handling_mode`, and `source_check_status` in the prompt pack. If the target generator or surface is not verified, use `Unknown` or `unknown`; do not imitate a different generator's syntax.

When the connected Codex text-bearing static profile is explicitly selected through `host_environment: codex`, `execution_surface: codex_builtin_imagegen`, `generator_provider: openai`, `final_asset_has_visible_text: true`, and `target_generator: gpt-image-2`, use `negative_handling_mode: integrated_constraints`. Put brief, concrete exclusions in the main prompt, such as no extra words or no duplicate text. Do not create a separate `Negative Prompt` or `negative_prompt` block. This is a format rule only; it does not execute generation.

Every prompt must stand alone outside this conversation. Do not refer to previous prompts, earlier renders, rejected outputs, chat history, or attachments not listed for the current request. Name each attached reference by its current-request alias and role.

## Native rendering boundary

Use the active surface's built-in image-generation capability only when the user explicitly asks to generate or render the graphic. Build the same complete prompt required by this Skill before invoking that capability. In Codex, invoke `$imagegen` only when it is available as a built-in Skill. Do not render from an ambiguous brief, and do not use an external provider, API, connector, paid service, or upload as a fallback.

If native image generation is unavailable, return `render_status: unavailable` with the complete final prompt. If the copy-feasibility preflight returns `dtp_required`, return `render_status: blocked_dtp` and do not render a raster substitute. If the native call fails, return `render_status: generation_failed`, retain the final prompt, and stop.

## Reference roles

Assign one job to every reference:

- identity;
- product truth;
- composition;
- pose or action;
- style;
- light;
- material;
- typography;
- scoped edit source.

State which properties remain protected. A reference for style does not authorize copying an unrelated person's likeness, a protected logo, product geometry, exact written copy, or the original composition.

Use the smallest reference set that resolves the requested control. Declare a precedence order whenever roles overlap: approved exact copy, identity, product truth, and logo authority take priority over composition; composition takes priority over style, light, and material. If two references conflict at the same priority, surface the conflict before generation.

For an edit, name only the permitted change, then list protected state separately. For a variation, name the allowed variation range and preserve every unchanged lock. Repeated prompt wording does not create deterministic continuity across separate generations.

## Brand, likeness, and style authority

For real brands, venues, institutions, partner marks, logos, or people, record an authority policy before prompt writing. Use only approved attached source assets and verified facts. For a real person, record `likeness_authority` as `user_confirmed`, `approved_source`, or `Unknown`; when the person is required and authority is `Unknown`, ask before generating. If the receiving surface supports a verified official-source check, request it as a preflight. If it does not, or if the check cannot be performed, mark the missing identity detail as `Unknown`; do not invent a logo, official name, partner, claim, certification, price, date, mark, or person.

For an artist, artwork, brand, or product style reference, identify the transferable visual attributes, such as contrast, palette, material, layout rhythm, or historical design movement. Request an original treatment built from those attributes; do not direct imitation of a specific artist, artwork, brand identity, or protected composition.

## Raster typography limits

Quote required strings. Keep them short, declare their count and location, and use external QA for spelling, diacritics, line breaks, spacing, and contrast. Raster generators can approximate visual type behaviour but cannot be assumed to use a specific font file or to provide print-safe kerning, ligatures, font licensing, or flawless small text.

Use a separated production route only when the user explicitly asks for it or when a verified render needs a narrow repair. It must preserve the approved result and introduce only the locked text or one named change. It is not a guarantee of correct spelling.

## Production intent and copy-feasibility preflight

Resolve `production_intent` before classifying copy:

- `concept_raster`: a directional or presentational visual where text still receives QA;
- `digital_final`: a publishable raster asset after all acceptance checks pass;
- `production_master`: an editable, print-ready, licensed-font, bleed, or prepress deliverable.

`production_master` is always `dtp_required`. A business card, label, menu, or flyer may still be `concept_raster` when the user asks for a concept rather than a production file.

Classify required visible copy before authoring a raster prompt:

- `compact`: a short headline and limited functional text with enough protected reading space;
- `at_risk`: multiple strings, important dates or contact details, or small text that must receive explicit QA;
- `dtp_required`: mandatory dense schedules, menus, legal copy, price lists, long contact data, exact print typography, licensed named fonts, or prepress requirements.

For `dtp_required`, explain the reason and route to an approved non-generative layout workflow. Do not suggest a text-free background or a later manual overlay as the default workaround.
