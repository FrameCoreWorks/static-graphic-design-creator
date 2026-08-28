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

Record `task_mode`, `target_generator`, `negative_handling_mode`, and `source_check_status` in the prompt pack. If the target generator or surface is not verified, use `Unknown` or `unknown`; do not imitate a different generator's syntax.

When the connected Codex text-bearing static profile is explicitly selected through `host_environment: codex`, `final_asset_has_visible_text: true`, and `target_generator: openai/gpt-image-2`, use `negative_handling_mode: integrated_constraints`. Put brief, concrete exclusions in the main prompt, such as no extra words or no duplicate text. Do not create a separate `Negative Prompt` or `negative_prompt` block. This is a format rule only; it does not execute generation.

Every prompt must stand alone outside this conversation. Do not refer to previous prompts, earlier renders, rejected outputs, chat history, or attachments not listed for the current request. Name each attached reference by its current-request alias and role.

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

For an edit, name only the permitted change, then list protected state separately. For a variation, name the allowed variation range and preserve every unchanged lock. Repeated prompt wording does not create deterministic continuity across separate generations.

## Brand and identity authority

For real brands, venues, institutions, partner marks, or logos, record an authority policy before prompt writing. Use only approved attached source assets and verified facts. If the receiving surface supports a verified official-source check, request it as a preflight. If it does not, or if the check cannot be performed, mark the missing identity detail as `Unknown`; do not invent a logo, official name, partner, claim, certification, price, date, or mark.

## Raster typography limits

Quote required strings. Keep them short, declare their count and location, and use external QA for spelling, diacritics, line breaks, spacing, and contrast. Raster generators can approximate visual type behaviour but cannot be assumed to use a specific font file or to provide print-safe kerning, ligatures, font licensing, or flawless small text.

Use a separated production route only when the user explicitly asks for it or when a verified render needs a narrow repair. It must preserve the approved result and introduce only the locked text or one named change. It is not a guarantee of correct spelling.

## Copy-feasibility preflight

Classify required visible copy before authoring a raster prompt:

- `compact`: a short headline and limited functional text with enough protected reading space;
- `at_risk`: multiple strings, important dates or contact details, or small text that must receive explicit QA;
- `dtp_required`: mandatory dense schedules, menus, legal copy, price lists, long contact data, exact print typography, licensed named fonts, or prepress requirements.

For `dtp_required`, explain the reason and route to an approved non-generative layout workflow. Do not suggest a text-free background or a later manual overlay as the default workaround.
