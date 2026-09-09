# Event Poster Codes: Selection and Rebuild

Use this reference within an explicitly activated design task when a user selects or browses codes, or when an open visual direction can benefit from internal catalog selection. Codes are optional. Ordinary brief-based work must remain complete without user knowledge of the catalog. Copy-only work, unrelated advice and fully specified narrow repairs need no catalog lookup.

## Contents

- Source evidence and limits
- Catalog commands and two usage modes
- Optional codes, automatic selection and visibility
- Resolve and apply a code
- Category translation map
- Existing state and output contract
- Examples and verification

## Source evidence and limits

The canonical [code catalog](event-poster-design-codes.json) preserves all 200 complete code lines and all 20 category names from **200 Event Poster Design Codes** supplied during development, attributed to **John Savage AI**. Page 1 gives the usage instructions; pages 2-6 each contain four categories of ten codes. The JSON records the supplied PDF's SHA-256, page provenance and exact spellings. `v2` comes from the uploaded filename; a declared version inside the document is `Unknown`.

The source procedure is: attach an event-poster reference, choose one complete code line, and use it with the image to rebuild the poster in that style. Its `/rebuild` contract preserves factual content while changing layout, hierarchy, palette, typography, materials and image treatment.

The PDF supplies names and grouping, not 200 detailed recipes, rendered examples, exact fonts, palettes, model settings or evidence of native slash-command support. Treat `/Name /rebuild` as a creative shorthand interpreted by this Skill. Never execute it as code, call an API with it as a native option, claim that a provider recognizes it, or print it on the graphic. IDs `EP001` through `EP200` are local lookup aids assigned in category/row order; they are not original individual code numbers or generator controls.

The category translation map below is **FrameCore Works implementation guidance**, not additional statements by the PDF's author. Attribute proposed visible attributes to this interpretation when explaining a code. A name such as `Cabaret`, `Theatre`, `Festival`, `Crowd`, `Microphone` or `News` does not authorize adding those event facts, objects, people or text. Inspect the actual brief first. Newsletter, tool and social promotions on page 1 are not part of the design workflow.

Every entry also includes `shorthand` (the exact slash name without the trailing `/rebuild`) and an individual English `interpretation.description_en`. These 200 descriptions explain a proposed visible mechanism and its use. They are FrameCore Works interpretations, not missing definitions recovered from the PDF. English is the single maintained source; translate explanatory prose at response time according to [language and localization](first-use-onboarding.md#language-and-localization). Adapt design choices to the actual brief; a label and a description are not proof of deterministic generator behavior.

## Catalog commands and two usage modes

Use `/codes` as the universal documented command. Within this explicitly activated Skill, or a request unambiguously addressed to it, recognize these whole requests case-insensitively:

| Command | Response |
| --- | --- |
| `/codes` or `codes` | Complete grouped catalog with style/use descriptions in the resolved user language. |
| `/kody` or `kody` | Polish conversational aliases for the same catalog; explain them during Polish onboarding or when asked. They do not force Polish output. |
| An unambiguous local request or an alias established in the active conversation | Resolve the catalog intent and pass `/codes` to the helper. Do not interpret an unknown individual style as a catalog request. |

Return all 200 canonical lines in all 20 categories, each with its individual description. Use a brief attribution followed by readable grouped tables. Do not replace the list with examples, an intake, an offer to continue, or four selected variants. The four-variant creative default does not limit a requested reference catalog. If the user explicitly narrows the request to a category or search term, return only that requested subset. Do not globally intercept the word "codes" in unrelated conversations. A browse request does not set a design's style or authorize a render.

The helper returns English source content for every accepted alias. The Skill localizes descriptions and explanatory headings for the user, including languages beyond English and Polish. Keep all code strings, IDs, category numbers and `/rebuild` exact; a translated heading may retain the original category name for lookup. Resolve a localized category/filter to the original category or English search terms before retrieval, and check that the candidates fit the user's request. Do not pass a translated style name as an exact catalog key or silently select a fuzzy match. Localized responses do not create translated catalog files.

- **Existing poster:** `/Name /rebuild` selects a style for a requested redesign of the attached poster, preserving source facts and protected properties. It does not upload or generate by itself. Retain the user's clear image-generation or prompt-only instruction.
- **New text-to-image prompt:** `/Name` selects the same direction without requiring an existing poster. The complete legacy line is also accepted in an explicitly new-poster brief; the user's new-design intent governs, so do not invent a missing source image or block on one.

In both usage modes, expand the resolved direction into concrete visible choices. Include a slash label only under the visibility rules below. The grounding comes from the resolved description, composition and locks, not from treating the slash string as a magic token. A canonical line ending in `/rebuild` does not broaden the task when the assistant selects it internally.

## Optional codes, automatic selection and visibility

Default to an ordinary conversation about the brief. Infer the code-use preference from the user's request; do not introduce a code-mode questionnaire, compulsory catalog, selection step or announcement. Retain a stated preference through the current project until the user changes it. Keep these as internal working decisions, not new required schema fields:

| User situation | Selection and response |
| --- | --- |
| Ordinary brief with no code, or "I do not want to choose/use these shortcuts; decide from my brief" | Use automatic selection when helpful. Keep the identifier internal and deliver ordinary design language. |
| "Do not show codes", including a supplied code followed by that instruction | Retain the requested or internally selected direction, omit code names, EP IDs, slash labels and code announcements from prose and delivered prompts. |
| User supplies an exact code and gives no visibility restriction | Resolve it manually and retain its supplied full/short slash label as instruction-only prompt metadata, paired with visible attributes. |
| "Choose a code and show/include it" or a direct catalog/code question | Show the selected identifier or requested catalog honestly, with the relevant interpretation. |
| "Do not use the catalog/codes, even internally" or a clear rejection of catalog-based design | Disable selection and work directly from the brief and ordinary design references. Do not substitute a hidden code. |

Treat reluctance to operate or see shortcuts as permission to handle design decisions internally, as requested for this Skill. Respect a clear prohibition on using the underlying catalog as a separate instruction. Do not ask a preference question when the user's meaning is already clear.

For automatic selection:

1. Resolve the objective, audience, desired response, format, reading conditions, exact copy burden, concept and reference/brand locks from the existing brief. Ask only a normal, material brief question when information actually blocks progress; never ask which code the user wants.
2. When visual direction remains open, inspect relevant categories and compare a small internal shortlist, usually up to three actual entries. Judge communication fit, composition/type-image mechanism, text legibility at the target size, compatibility with protected assets and production feasibility. A name match alone is not enough. The lookup helper retrieves candidates; it does not rank or decide the best code.
3. Select one fitting direction as a revisable assistant design choice. Exclude entries that contradict a lock, depend on invented facts or require unwanted effects. If no entry improves the brief, use original attributes without a code. Do not retrofit an already resolved design to a catalog entry or force a style onto a local repair. Deliberate hybrids still require the existing brief support and clear roles.
4. Keep the resolved canonical entry and selection origin in internal lookup context. Expand the useful mechanism into composition, hierarchy, typography, colour and material instructions. The assistant's selection is not a user-approved concept, a new factual source or permission to change copy. Preserve the existing concept/copy selection gates.
5. For ordinary or hidden-code use, put only the expanded design instructions into both the user-facing prompt and the prompt submitted for generation. Keep the raw code in internal lookup context, so a later request for the exact submitted prompt returns the actual same text without redaction. Do not expose the code through a heading, comment, metadata dump, EP ID or label-hiding announcement. Do not silently delete slash characters that belong to approved visible copy, URLs or other factual strings.
6. Do not narrate routine internal selection. If asked which direction or code informed the work, answer truthfully and briefly using the actual entry, or state that no catalog entry was used. Never claim that a direction was user-selected or that a generator natively recognizes the identifier.

Code visibility is independent of output mode. `prompt` returns the complete expanded prompt; `render` uses the same design instructions internally and returns the requested image; `render_and_prompt` returns the exact submitted prompt. Existing execution authorization and availability rules continue to apply.

## Resolve and apply a code

1. **Respect activation and scope.** A quoted code, a collection question or importing this PDF is not permission to design or render. Keep the entrypoint's explicit activation and requested output mode. A pasted code alone does not resolve an ambiguous prompt-versus-render request. Retain existing, clear approvals instead of asking again.
2. **Resolve one exact entry.** For manual selection, look up the complete line, short `/Name`, exact name, or a local EP ID in the JSON. Match case-insensitively and normalize surrounding/repeated whitespace for lookup only; preserve canonical spelling. A search/browse request returns candidates without silently committing a design choice. An absent or ambiguous user-supplied code is `Unknown`: offer actual matches or ask for the complete line, using ordinary style descriptions if codes should remain hidden. For automatic selection, apply the brief-based criteria above and verify the chosen entry exactly. Do not fabricate codes or reinterpret a typo as authorization to choose a different direction.
3. **Establish the source.** For an existing-poster rebuild, inspect the actual attached poster, not a remembered image or a code-list PDF used in its place. If the reference is absent or unreadable, request that source or clarification before finalizing. A separately supplied, explicit new-poster brief may borrow the code as a style direction; identify that as an adaptation, not a rebuild of an unseen poster.
4. **Lock information and protected properties.** Transcribe every required title, name, date, time, venue, address, price, contact, URL and legal/partner item exactly. Preserve supplied source authority and copy permissions. Record uncertain characters as `Unknown`; do not guess. Preserve logos, identity, product geometry, QR/barcode payload and any other protected source property. Do not regenerate an unreadable machine-readable code or assert it scans without verification. A raster limitation may require the existing DTP handoff. Reuse clearly supplied final wording without unnecessary copy-selection questions.
5. **Define the permitted rebuild.** A user's request to rebuild a supplied poster permits a broad visual redesign within that request. Layout, type treatment, palette, hierarchy, material simulation and image treatment may change. Facts, protected assets, selected wording and any supplied Core Concept Lock remain fixed. A user instruction such as "change only the background" narrows this scope and takes precedence over the code. An internally selected canonical `/rebuild` suffix grants no redesign permission. A change to the core concept still needs the existing concept decision.
6. **Translate visibly.** Use the exact code name and category as a starting point, then choose a brief-specific composition, attention order, type/image relation, palette and motivated material treatment. Read the existing [style translation catalog](poster-style-translation-catalog.md) for label classification and [movements atlas](poster-movements-and-production-atlas.md) when historical or cultural authority matters. Avoid ornamental stacks. Do not invent precise settings or a fixed appearance absent from the PDF.
7. **Compile and deliver.** Expand the chosen direction into one complete natural-language prompt under the [unified prompt contract](unified-static-prompt-contract.md), applying the visibility policy above. For a broad rebuild, include all required visible strings exactly; the narrow-edit exception for source-preserved text does not justify omissions during a full redesign. Pass actual reference attachments using the host's real schema. `prompt` stays prompt-only; rendering requires the existing explicit request, feasibility gates and native capability.
8. **Check and stop.** Compare the result to the source information inventory, protected properties, selected style interpretation and requested edit scope. Missing required copy or changed identity is a failure even if the new design looks attractive. Apply the current [QA and repair rules](qa-and-repair.md); do not perform an automatic second generation.

## Category translation map

Use this map for selecting relevant entries and proposing visual interpretations. It is not a rule to apply every attribute to every code. Numeric ranges below are local EP lookup ranges; category numbers/names and page associations come from the PDF.

| Category | EP range / PDF page | Suggested translation focus | Selection and fidelity check |
| --- | --- | --- | --- |
| 01 MODERNIST SYSTEMS | 001-010 / 2 | Grid, axes, geometric rhythm, deliberate type/shape relations | A disrupted grid must still serve reading order; a name does not settle historical authenticity. |
| 02 PRINT IMPERFECTIONS | 011-020 / 2 | A specific separation, registration, overprint, stencil or relief-print cue | Keep factual text readable. Distinguish inks, substrate and overprint. Soy ink is not evidence of sustainability. |
| 03 INDUSTRIAL BRUTALISM | 021-030 / 2 | Blunt typographic mass, structural framing, restrained industrial surfaces | Warning stripes or utility labels must not invent hazards, certifications or official authority. |
| 04 EDITORIAL FASHION | 031-040 / 2 | Crop, headline/caption hierarchy, measured editorial contrast | Preserve subjects and required information; do not invent a publication, designer or fashion-house affiliation. |
| 05 COLLAGE EPHEMERA | 041-050 / 3 | Purposeful fragments, visible edges, layered source hierarchy | Receipts, tickets and labels cannot introduce fictitious prices, names or extra readable filler. |
| 06 NIGHTLIFE NEON | 051-060 / 3 | Controlled luminous signage, directional light or nocturnal colour contrast | Light serves hierarchy; avoid automatic cityscapes, unrequested smoke and unreadable glowing text. |
| 07 LUXURY CULTURE | 061-070 / 3 | Space, optical type balance, restrained tactile or reflective accents | Translate luxury into visible decisions; preserve copy and avoid unsupported premium/material claims. |
| 08 ZINE UNDERGROUND | 071-080 / 3 | Photocopy contrast, cut type, marker or tape-derived composition | Keep critical copy readable and use only authorized wording, symbols and affiliations. |
| 09 CINEMATIC PHOTOGRAPHY | 081-090 / 4 | Photographic framing, tonal storytelling and a deliberate light source | Preserve likeness and scene facts; do not invent a crowd or lens setting because it appears in the label. |
| 10 HISTORICAL GLAMOUR | 091-100 / 4 | A selected period-related composition or type treatment | Resolve the intended historical language; do not combine every period named in the category. |
| 11 SPORTS BROADCAST | 101-110 / 4 | Directional composition, bold numerical hierarchy, broadcast-like organization | Do not fabricate scores, teams, athletes, sponsors or competition status. |
| 12 MATERIAL TYPOGRAPHY | 111-120 / 4 | Letterforms with a controlled sculptural, folded, fabric or reflective treatment | Keep letter identity, counters and diacritics readable; functional metadata may need simpler type. |
| 13 STREET ACTIVISM | 121-130 / 5 | Public-notice hierarchy, stencil, paste-up or banner rhythm | The selected style does not choose a political position, slogan, movement membership or factual allegation. |
| 14 MUSEUM INSTITUTIONAL | 131-140 / 5 | Catalog/label hierarchy, information grid, archival spacing | Do not invent accession numbers, curatorial credentials, museum identity or provenance. |
| 15 SURREAL SPATIAL | 141-150 / 5 | One subject-linked spatial impossibility, scale relation or visual riddle | Respect the concept lock and protected subjects; no mandatory new microphone, staircase or crowd. |
| 16 GLOBAL PRINT TRADITIONS | 151-160 / 5 | A chosen, source-supported formal or process cue interpreted through the movements atlas | Names are not evidence of a whole culture's style. Avoid stereotypes, invented scripts, flags or affiliations. |
| 17 DIGITAL CHROME FUTURE | 161-170 / 6 | A coherent digital-era, reflective, translucent or wireframe language | Restrict effects to their assigned roles; no unrequested interfaces, pseudo-controls or invented text. |
| 18 FOLK CRAFT | 171-180 / 6 | A consistent stitch, cut, carved, tile or painted-sign construction | Treat material as simulation; do not invent a regional maker, cultural identity or sacred motif. |
| 19 NEWSPAPER PUBLISHING | 181-190 / 6 | Column structure, headline scale, information grouping and print contrast | Preserve all required copy; no fake news claims, filler articles, mastheads or tiny pseudo-text. |
| 20 MOTION OPTICAL | 191-200 / 6 | Static directional rhythm, controlled echoes or optical displacement | This remains one static graphic, not video. Protect exact readable text from blur, duplicate words and misleading echoes. |

## Existing state and output contract

Use existing fields rather than inventing `task_mode: rebuild` or a native `rebuild` option:

| Information | Existing field / handling |
| --- | --- |
| User-selected code line | Store its canonical line in `strategy.style_requests`; keep any existing user constraints. |
| Assistant-selected code, origin and visibility preference | Keep in internal lookup context; write its resolved attributes to strategy fields. Do not invent a user request in `strategy.style_requests`. |
| Resolved visible interpretation | `strategy.primary_language`, `secondary_treatments`, `composition`, `type_image_relationship`, `material_treatment` |
| Existing-poster broad redesign | `task_mode: variation`; retain the source in `references` with `edit_source` and applicable property roles |
| Explicit new-poster brief using a code | `task_mode: generate`; no nonexistent source poster is required |
| Explicitly narrowed repair | `task_mode: edit` and the current `edit_scope` contract |
| Final source wording | `copy.route: locked_copy`, per-item exact strings/authority and actual selection state |
| Protected idea | Existing `concept.lock`; do not replace it with the style code |
| Requested deliverable | Existing `output_mode`; a code lookup is `none`, not a render request |
| Missing reference or unresolved mandatory characters | Existing clarification/reference state, no final prompt/render |

Both [intake](../templates/design-intake.md) and [prompt pack](../templates/prompt-pack.md) already carry these fields. Source page, PDF digest and local code ID remain lookup/provenance metadata; do not add unsupported keys to the canonical design schema.

## Examples and verification

The read-only [lookup helper](../scripts/event_poster_codes.py) uses Python's standard library. Paths in these commands are relative to this Skill directory. It only retrieves catalog entries; it cannot render, upload, install, access a network or execute the selected text. If code execution is unavailable, read the JSON directly.

```bash
python scripts/event_poster_codes.py --code '/Two Ink Collision /rebuild'
python scripts/event_poster_codes.py --category 20
python scripts/event_poster_codes.py --query 'Bauhaus'
python scripts/event_poster_codes.py --list-categories
python scripts/event_poster_codes.py --command /codes
```

A matching example is category 02, local ID `EP011`, `/Two Ink Collision /rebuild`. A possible interpretation is two declared simulated ink colours on a separate paper substrate, with a controlled overlap that guides attention. That recipe is an implementation choice, not an exact prescription in the PDF. Choose the actual colours from the user's locks or brief. Broadly rebuild an attached poster only when requested; retain every factual string and protected asset.

This complete fictional manual-selection prompt illustrates a code label plus its visible interpretation. It assumes that the user explicitly supplied the code and single final word and asked for a new prompt without hiding codes; never reuse its wording as a real project fact:

```text
Create one square typographic graphic. Style direction label for interpretation only: /Two Ink Collision. Translate this direction into two simulated inks, deep blue and warm orange, on a separate warm-white paper substrate. Use generous negative space, one centered blue title, and one orange geometric field crossing the lower portion of its letterforms with a controlled darker overprint intersection. The geometry supports the title and does not obscure its letter identities. Render exactly one visible word: "CZYTAJ", on one line in substantial upright lettering with generous optical spacing. Keep the surrounding field calm, with subtle paper absorption and a consistent two-ink process logic. The slash label is instruction metadata, not visible copy. Accept only the exact word, a clear title-first hierarchy and no additional visible text.
```

Run the [catalog tests](../tests/test_event_poster_codes.py) with `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test_event_poster_codes.py'`. They verify all 200 lines through a source-derived digest, IDs/category/page ordering, lookup boundaries and CLI behavior. They do not prove visual quality. Source ingestion was additionally checked with two independent PDF extractors and visual inspection of all six pages. See [evaluation scenarios](evaluation-scenarios.md) for behavior cases.

## Integration inventory

| Item | Responsibility | Inputs / outputs | Ownership and dependency |
| --- | --- | --- | --- |
| `static-graphic-design-creator` | Interpret optional poster codes with manual selection, internal brief-based selection or catalog opt-out | Explicit task, ordinary brief or optional code/source -> scoped answer, prompt or authorized graphic | Same existing Skill; no additional Skill dependency |
| `event-poster-design-codes.json` | Sole canonical list, English per-code descriptions and source evidence | Supplied six-page PDF -> 20 categories / 200 exact lines; separate authored interpretations localized by the Skill | Source names: John Savage AI; descriptions: FrameCore Works; no duplicated list in other references |
| This workflow reference | Rebuild semantics, category interpretation and state mapping | Resolved entry and protected source -> design decisions | Existing atlases own historical/style guidance; current QA owns acceptance |
| Lookup helper and catalog tests | Reliable retrieval and collection integrity | Canonical JSON -> exact matches / test results | Local, read-only, standard library; no rendering or network dependency |

This catalog and workflow are included in the repository source bundle. The source-release record identifies its published upstream base after release locking and publication. Repository maintenance follows the source-first release process; updating an installed copy remains a separate, explicitly authorized operation. Ordinary catalog use never edits files, installs updates or publishes a release. The original PDF is not bundled or required at runtime.

Future expansion may add explicitly authorized authored directions with separate provenance and stable identifiers, while preserving the 200 original lines and their category mapping. Extend an actual design capability or meaning rather than adding synonyms to inflate the count. No new directions outside the PDF are claimed in this revision.
