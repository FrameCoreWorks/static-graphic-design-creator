# Capability and Reference Contract

Read for supplied assets, identity/product/logo fidelity, edits, or any execution-sensitive control. [Workflow integration](workflow-integration.md) owns the canonical host/reference fields; [typography feasibility](typography-and-text-feasibility.md) owns text and production routing.

## Capabilities need surface evidence

Use the actual exposed tool schema and observed behavior first, then current official documentation for that surface. A model/API capability does not establish its availability in ChatGPT Work or Codex. Keep the model `Unknown` if the host does not expose it. A user's requested target is a declaration, not evidence of support.

| Classification | Use |
| --- | --- |
| `native-setting` | Send only through an actually exposed field; record its evidence outside the prompt |
| `prompt-semantic` | Natural-language intent such as a vertical composition or restrained spacing; no guarantee of exact control |
| `reference-conditioned` | Requires the relevant asset attached to the actual request and a supported conditioning/edit route |
| `external-qa` | Check the actual result, such as spelling or exact geometry; not a generation setting |
| `unsupported` | Report the limitation when relevant; do not send fabricated syntax |
| `Unknown` | Unverified, neither false nor supported; do not borrow claims from another surface |

Native size, aspect fields, reference limits, masks, seeds, weights, transparency, negative fields and edit controls require individual verification. Output dimensions belong in supported settings and final-file inspection, not quality incantations such as “8K”. Never claim an alpha channel, editable layers, exact font or repeatable seed from natural-language instructions alone. A declared reference set exceeding actual input limits requires an explicit priority decision, not silently dropped assets.

For GPT Image 2.5, read the [dated model and surface reference](gpt-image-2-5.md). Keep the requested model, observed native renderer and conversation model distinct. Do not fill an absent returned attribution with the request value or assume that a quality/mask field in an API guide exists in Work or Codex.

## One native execution route

Native generation requires a user's render request, selected concept/copy, resolved required references and passed feasibility gate. Use the available built-in image capability under its active tool/Skill instructions. A built-in Skill's CLI or paid API fallback is outside this Skill's authorization. Never substitute an external service, upload, or paid provider when native generation is absent.

If unavailable, use `report_unavailable` and `render_status: unavailable` with the final prompt only when all other finalization gates are satisfied. An open copy choice stays open. A failed call is `generation_failed`, not a render or QA pass. A returned image starts as `generated`; inspect before claiming acceptance. No silent retry or automatic second render.

Use integrated, concrete exclusions unless the active surface verifies a separate negative field. The optional Codex declarations described in [workflow integration](workflow-integration.md) are compatibility context, not executable settings. Each submitted prompt must stand alone with current-request reference aliases and attachments; never rely on an unavailable previous image.

For [separate assets](layered-assets-workflow.md), run the same availability and reference checks per requested element. The composition plan does not guarantee exact alignment across generations. Asset-file inspection, archive creation and editor import are separate capabilities; only the first two belong to an explicitly requested file-delivery task. A requested ZIP never authorizes external upload or regeneration.

## Assign authority by property

One image may have several explicit roles. Use canonical `references` entries with stable ID, actual source, availability, roles and a `properties` map. Record which property each source governs and what may change. Do not give every property to whichever reference happens to be listed first.

| Source role | Typical protected properties | Does not automatically authorize |
| --- | --- | --- |
| Identity / likeness | Recognizable identity and user-specified face, body or hair traits | Another person's identity from a style image |
| Product truth | Silhouette, proportions, construction, closures, count, label boundaries and contents | A redesign to fit a prettier composition |
| Garment | Cut, seam topology, fasteners, print placement and material when specified | Changing brand, garment type or pattern continuity |
| Packaging / logo | Mark geometry, spelling, colours, label topology, panel orientation | Invented marks, certifications, a fake logo or reflowed approved lockup |
| Composition / pose | Placement, scale relations, viewpoint or action within declared scope | Overriding anatomy, product construction or identity |
| Style / artwork | Transferable palette, rhythm, mark-making, type-image relation | Unrequested copying of source text, people, marks or composition |
| Location | Required visible architecture/signage and verified identity | A generic substitute presented as that location |
| Light / material | Lighting or surface appearance allowed by the brief | Altered geometry, added embossing or a new physical material |
| Edit source | Current approved image and protected state | Starting a new composition or silently replacing the image |

Resolve overlap per property: user-approved copy and explicit source locks govern their own property; identity/product/logo truth outranks stylistic convenience. Composition governs arrangement within those locks. Equal-authority disagreement on a required property blocks finalization until resolved. Preserve unresolved references as unavailable/conflicting, rather than treating absence as a creative license. Use the smallest sufficient set while retaining every required authority.

Check apparent age and facial geometry separately from recognizable likeness. A face crop and a wider body/garment view may serve different roles; preserve originals if preparing useful crops. Do not invent unseen product construction. Look for accidental transfer of a style reference's face, garment, text, setting or material into properties that another reference protects.

For example, `product_front` may lock `bottle_shape: cylindrical`, `label_boundary: one continuous closed rectangle`, `cap_count: one`; `lighting_ref` governs soft side light only. Do not turn the label into floating strips, repeat caps, change packaging seams, or replace the product to imitate lighting. Relative topology is often more useful than repeated adjectives such as “exact”.

## Source and brand decisions

Use user-supplied approved assets for their stated task and preserve verified facts. Source approval establishes which asset/wording governs the design; it does not independently prove a factual claim or legal clearance. Record unresolved attribution or required likeness/brand authority as `Unknown` and ask when it affects the requested result. Do not demand a new approval for a source and scope the user already approved.

Never invent an official logo, certification, partner, claim, price, date or product feature. Distinguish faithful use of an approved mark from a brand-inspired visual treatment. If exact mark geometry is mandatory and native conditioning cannot preserve it, route to suitable exact-asset placement with user authorization; do not claim a generated approximation is the official master.

For a named style or artwork, articulate original transferable decisions. Historical movement references guide design language, not factual position or cultural authority. Preserve meaningful cultural context and verify unfamiliar claims before using them; unresolved facts remain Unknown. A context-sensitive question is warranted for an unconfirmed position or charged symbol, not as a blanket obstacle to ordinary civic graphics.

## Edits and variants

Put the one permitted change first and list unchanged properties separately. Preserve the actual source image and all selected copy/concept locks. A variation defines allowed differences; a reference alone cannot guarantee deterministic continuity across generations. Changes to identity, product construction or a protected logo require an explicit new scope. If the required image is missing from the current request context, obtain it before editing.

Account for necessary physical relationships: moving an object can require its contact shadow, reflection or occlusion to change. Resolve a concrete conflict with the preserve set before proceeding. Masks and selections guide scope but do not prove pixel isolation. Retain the original approved base and preceding accepted image; compare both after a serial edit and start independent alternatives from the same base.
