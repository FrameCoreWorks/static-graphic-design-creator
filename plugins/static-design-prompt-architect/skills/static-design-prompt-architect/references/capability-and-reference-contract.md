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

## Raster typography limits

Quote required strings. Keep them short, declare their count and location, and use external QA for spelling, diacritics, line breaks, spacing, and contrast. Raster generators can approximate visual type behaviour but cannot be assumed to use a specific font file or to provide print-safe kerning, ligatures, font licensing, or flawless small text.

Use a separated production route only when the user explicitly asks for it or when a verified render needs a narrow repair. It must preserve the approved result and introduce only the locked text or one named change. It is not a guarantee of correct spelling.
