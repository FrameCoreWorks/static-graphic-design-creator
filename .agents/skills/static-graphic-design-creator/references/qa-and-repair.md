# QA and Repair

QA compares actual artifacts with the approved concept, copy and property-level reference contract. A pleasing preview is not sufficient evidence. [Typography feasibility](typography-and-text-feasibility.md) owns reading and production checks; [workflow integration](workflow-integration.md) owns state transitions.

## Preflight

Before a final prompt or render, require the selected/locked concept, selected/locked copy or explicit no-copy, resolved required references and feasible production intent. At-risk typography needs a concrete review plan. DTP stops raster finalization. No render is authorized by an ambiguous brief, a state label or the availability of a tool.

Unavailable native generation returns a prompt only after the other finalization gates pass. A failed tool call is `generation_failed`. An image returned by the tool is `generated` until inspected. Follow the active host's display rules; if inspection is unavailable, state that limitation and keep QA `not_run`. Never prefill success in a prompt pack.

## Inspect the delivered artifact

For a manually or automatically selected catalog direction, follow [code selection and rebuild](event-poster-code-workflow.md): confirm the actual entry, its fit to the brief, every required source fact and protected asset, and the visible interpretation. Check that automatic or hidden-code use leaks no identifier through prose, prompt, EP ID or metadata dump, and that a clear catalog opt-out is respected. A requested visible code label is instruction metadata, never extra graphic copy. Preserve factual slash-containing text and URLs. A selected style is not evidence of native-command support or permission to change a concept/copy lock. Broad redesign requires the user's scope; internal selection and a `/rebuild` suffix never expand a background-only repair.

| Check | Observe | Failure consequence |
| --- | --- | --- |
| Message and concept | Actual visual mechanism, intended audience response and protected concept relation | Missing/replaced core mechanism blocks acceptance; rebuild composition if necessary |
| Attention and scale | Intended one to three notices, or declared denser scan path; no competing priorities | Broken hierarchy requires layout repair; do not add elements just to reach three notices |
| Exact visible text | Every selected item, diacritics, case, punctuation, line breaks, dates, prices and contacts; no extras | One wrong required string blocks acceptance; preserve all correct strings |
| Legibility | Intended viewing size, full resolution, local contrast, spacing, clipping and required metadata | Unreadable required text fails even if it is small or secondary |
| Identity and source truth | Likeness, product silhouette, construction, garment seams, logo geometry and label topology against the actual references | One protected-property drift blocks acceptance; identify the changed property |
| Material and light | Declared process logic, coherent palette, plausible overlaps, surfaces and illumination | Remove unmotivated treatment; do not relabel a defect as intentional texture |
| Generation artifacts | Repeated fragments, doubled edges/limbs/marks, malformed objects, warped type, broken label boundaries, background seams | Report exact location and consequence; source/text defects are critical |
| Surface finish | Banding in intended smooth gradients, repetitive texture tiles, sharpening halos, accidental rings, muddy transitions or excess microcontrast | Judge at actual use size and full resolution; repair visible defects, not hypothetical ones |
| Claims and additions | No invented partners, features, evidence, dates, claims, pseudo-logos, duplicate text or unrequested mockup | Unsupported factual/source additions block acceptance |
| Delivery properties | Actual dimensions, format, crop, background/alpha and requested file behavior where measurable | Unknown properties cannot be advertised as verified; raster cannot establish a production master |

Keep meaning, correctness and execution separate from aesthetic preference. A single critical failure fails QA; do not wait for a count of two. An optional treatment preference alone does not imply a full rerender. Check cultural/history-dependent decisions against their supplied authority when relevant, without inventing a general requirement for every ordinary social graphic.

For a canonical record, include check IDs `concept`, `hierarchy`, `copy`, `legibility`, `references`, `additions` and `delivery`, plus specific artifact/material checks when relevant. Copy/legibility may be not applicable only for deliberate no-copy; reference checks only when no reference governs the output. Delivery checks are scoped to the requested intent, not a prepress claim.

Record each check with an ID, `pass`, `fail`, `Unknown` or `not_applicable`, and concise observed evidence. State which image/file was inspected and at what viewing condition. `qa_pass` requires all relevant critical checks to be completed and passed, with evidence; Unknown critical checks block final acceptance. Do not label a check not applicable merely to avoid a missing reference. OCR is supporting evidence, not a replacement for inspecting the source and rendered glyphs.

## Decide the smallest sufficient repair

| Decision | Use when | Next step |
| --- | --- | --- |
| `accept` | Required checks pass and the requested objective is met | Deliver within the requested scope; stop |
| `scoped_edit` | A local correctable defect remains in an otherwise approved composition | Use the actual current image and supported edit route; name one permitted change and all protected properties |
| `full_rerender` | The core mechanism/layout fails, or the required repair cannot be isolated | Rebuild from selected concept and source locks; explain why a narrow edit is insufficient |
| `dtp_required` | Fixed exact-type, master, barcode, dieline or prepress requirements exceed the raster route | Provide the bounded production handoff; no default text-free background or overlay workaround |
| `generation_failed` | Native call errored or returned no usable image | Report the actual outcome; retain the prompt; no silent retry/external fallback |

A source-truth defect is critical but does not automatically require destroying a good composition: a narrow supported repair may be enough. Conversely, a pretty surface cannot rescue a missing thesis. Rebuild an incoherent strategy rather than appending longer exclusion lists.

## Scoped edit contract and stopping

Use canonical `edit_scope` for a structured edit handoff: account for changed and protected copy IDs, identify the current image with role `edit_source`, and state protected properties. Quote the changed string; protect unchanged source text without forcing a transcription of the entire poster.

Put the permitted change first. Preserve crop, composition, placements, scale, type roles, all unchanged exact text, identity/product/logo properties, background, light and colour/material system. Attach the current source using the host-supported mechanism; do not refer only to “the previous image”. An explicitly requested exact spelling replacement is already authorized; do not reopen concept or copy discovery.

After any repair, inspect both the target defect and the protected properties that could have drifted. Preserve the previous artifact as a rollback point. Do not initiate another generation unless the user's authorization covers that bounded repair. If unavailable, retain the image and offer the appropriate route. Stop when the approved objective is met; a new aesthetic preference or additional output needs a new scope.
