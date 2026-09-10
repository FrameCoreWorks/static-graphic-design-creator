# Optional layered assets

Read only for an explicit request to create separate elements, work layer by layer, or assess separation of a flattened graphic. Ordinary graphics still use the integrated prompt contract. A capability question needs an answer, not a project plan or generation. No slash command, editor connection or additional Skill is required.

## Contents

- [Composition and asset scope](#composition-and-asset-scope)
- [Sequential review and approval](#sequential-review-and-approval)
- [Plan and version registry](#plan-and-version-registry)
- [Prompt and execution contract](#prompt-and-execution-contract)
- [Transparency and assembly](#transparency-and-assembly)
- [Existing flattened graphics](#existing-flattened-graphics)
- [Delivery](#delivery)
- [Read-only helper](#read-only-helper)
- [Examples and evidence](#examples-and-evidence)

## Composition and asset scope

The primary workflow creates elements **from scratch** for one coherent design. Establish the communication goal, concept, intended format, copy inventory, reference authority, visual treatment and a useful layer order. Use a brief conversation, not a mandatory form. A plan is sufficient; do not first render a flattened poster unless requested. Work on the single element or sequence the user requested rather than expanding every task into a full package.

Possible elements include background/environment, gradient/texture, person/product, foreground, frames/shapes, overlays, artistic lettering, and editable text specifications. A layout is usually the arrangement in the plan, not a separate raster to generate. Keep an object with its contact shadow, reflection or other coupled detail when separation would reduce realism or portability. Effects need a compositing role; do not add fog or glow merely because they are possible layers.

Keep project-level copy and locks in the composition plan. For each raster operation, use the existing [design contract](design-contract.schema.json) for that **one asset**, with its applicable copy and reference inventory. A text-free background can use `no_copy` at asset scope while the project still retains its required title and metadata. This never deletes project copy or authorizes a text-free replacement for an ordinary complete-poster request. Unresolved decisions block the affected asset: do not require final event wording to create an independent background when its reserved reading space is already agreed. Dependencies or material changes to the concept/layout still need resolution first.

Assess production intent per deliverable. Editable text is a manual typesetting handoff; its DTP requirement does not block a separately requested, feasible raster background. It does block claiming that a finished editable or print master has been delivered. Use `no_copy` for the raster operation only when the element really has no lettering; retain labels on a protected product and approved artistic title text when they belong in that asset.

## Sequential review and approval

The default is **one asset at a time**, including when the user requests a full set. An agreed list is the scope of work, not permission to bypass intermediate review.

1. Establish the next element's role, geometry, references and output request from the agreed plan. Reuse decisions and execution authorization already given. A prompt-only or planning request does not authorize generation.
2. Produce that element only. Present its actual result and a short, honest QA observation. `generated`, technical checks, and user approval are separate facts.
3. Ask whether to keep it or what to change. Stop here until the user responds. Do not generate the next element on the strength of a promising result, silence or the assistant's own QA.
4. A requested correction creates a new candidate version of that asset. Preserve the prior file; do not overwrite the approved version or use a rejected candidate as the next base without an explicit reason and scope. Review the correction and protected properties again.
5. An explicit acceptance selects that exact version. Record the user's confirmation and date when known, the file and actual digest when readable. Acceptance of an idea or prompt is not acceptance of an image that has not been generated. A user may keep a technically limited draft, but that is not a QA pass; delivery must disclose the limitation and cannot call it verified final artwork.
6. After acceptance, continue with the next agreed asset when the existing request authorizes its generation. Do not ask again for the same generation permission. If the user only requested one asset or stops the sequence, honor that scope.

Discuss changes to already approved dependencies before editing them. Replacing a person may require a new shadow; preserve unrelated background bytes. Reassess the affected relation even when both individual assets look good. A newly proposed correction does not silently replace the last approved selection. Resolve or explicitly reject/cancel any outstanding candidate before final delivery.

## Plan and version registry

Use [layer-plan.json](../templates/layer-plan.json) as a fictional worked starting point for complex work or a portable handoff. Replace its example content; it contains no generated files or approvals. Keep the project registry and output assets with the actual project, **outside the Skill source and personal extension instructions**. Do not mutate the Skill to remember a design session.

The separate `schema_version: 1` plan does not add fields to the single-asset design contract:

Retain a supplied structured Core Concept Lock as the complete object, including allowed/forbidden adaptations and extra source context; a simple new brief may use a concise string. Preserve supplied per-copy authority, required status and allowed changes as additional fields alongside the minimum copy inventory. Do not flatten or discard an upstream lock merely to match the short fictional template.

| Field | Meaning |
| --- | --- |
| `project_id`, `revision`, `mode` | Project identity, increasing plan revision, `from_scratch` or `from_flattened` |
| `canvas` | Composition width/height in pixels, top-left origin; unresolved values are `Unknown` during planning |
| `composition` | Goal, concept lock, palette, light, perspective, reserved zones and full copy inventory |
| `sequence` | Ordered asset IDs within the user's current scope; may be a subset of the project |
| `assets` | Stable IDs, role/treatment, output route, geometry, opacity, blend intent, alpha requirement, copy IDs and dependencies |
| `versions` within each asset | Separate candidate files; ID, origin, status, QA evidence and explicit approval evidence |
| `selected_version` | Exact user-approved version, or null; never inferred from newest filename |
| `delivery` | `undecided`, `individual` or `zip`, plus IDs the user chose to receive |

Geometry describes the placed asset rectangle: `x`, `y`, `width`, `height` in composition pixels, rotation in degrees. For `full_canvas`, it is `(0, 0, canvas width, canvas height)` before any rotation; keep rotation zero. A `cropped` file carries its explicit placement and scale; its actual pixel dimensions are recorded separately in each version. Do not stretch a result silently to disguise a dimensional mismatch. Off-canvas placement may be intentional but must be discussed when it clips required content.

`depends_on` lists asset IDs whose changes require reassessing this element, with the reason in `dependency_note`. It is a dependency graph, not the z-order. Use ascending `z_index` for bottom-to-top stacking; avoid ambiguous ties. Keep coupled details in `coupled_elements`. Identify opacity/blend intent and editor support separately: a plan is not proof that an editor implements a blending mode.

Each version records a safe project-relative `file`, actual `sha256` or `Unknown`, actual `pixel_size` or `Unknown`, `status` (`in_review`, `approved`, `rejected`), `qa` (`pass`, `fail`, `Unknown`), `qa_evidence`, `approval` (null or `{evidence, date}`), and `origin` (`newly_generated`, `extracted`, `reconstructed`, `authored_spec`). Origin includes its actual source or `Unknown` and a concise explanation. Keep original source assets separately. For a typesetting handoff, the versioned file is the actual text/layout specification, not an imaginary editable image.

At most one candidate is in review in this sequential workflow. An approved version remains selected while a correction is discussed; the new candidate cannot enter a delivery until separately selected. Retain previous versions and approval evidence. A plan passes structural validation only; arbitrary approval strings or hashes in a JSON document are not evidence of real user consent or measured files.

For a later chat, supply the registry and the referenced files through the receiving host's supported file access. Reconcile accessible bytes before continuing. Do not claim durable memory, preserved attachments, a completed export or cross-chat access merely because an ID exists. Missing approved files require recovery or the user's decision, never silent regeneration presented as the original.

## Prompt and execution contract

Compile one standalone prompt for the current asset, or one corrected prompt when requested. Preserve the common concept and only the project's constraints relevant to that element. State: asset role; content to include; content reserved for other elements; canvas/crop intent; placement and scale; perspective/light/palette; reference roles; exact lettering on this asset; intended alpha/blend behavior; and observable QA criteria. Do not ask the generator for a contact sheet or all layers in one image.

The eight-stage design thinking still informs each asset, compressed to relevant decisions. Read the [unified contract](unified-static-prompt-contract.md) for ordinary integrated output; its prohibition on default layer exports does not override an explicit separated-assets request. Actual native tool settings and supplied references govern execution. In a host exposing only prompt and image inputs, do not invent model, size, quality or alpha fields. Verify material capability claims against current official sources when needed.

Codes remain optional, with the same visibility and opt-out rules in [code selection](event-poster-code-workflow.md). Apply a direction consistently across the composition, then translate only useful attributes for the current asset. A code must not add the whole poster's title to a text-free background, introduce a new concept, override identity, or expand a narrow correction. Reference reuse in image generation may reinterpret pixels; exact assembly belongs to an appropriate deterministic/editor workflow.

A failed tool call stops this asset with the actual failure. Unavailable generation permits a complete asset prompt only after its applicable gates pass. No automatic retry, paid/API fallback, external upload or editor import. Planning, onboarding, package selection and Skill maintenance do not authorize image generation.

## Transparency and assembly

PNG is a practical raster interchange choice; use actual alpha when required and supported. Check the actual file, not a preview checkerboard or extension. Distinguish no transparency, fully transparent/empty output, and usable partial transparency. Inspect edges over light, dark and intended backgrounds; review hair, semitransparent glass, glows and shadows. Numerical alpha checks do not certify a clean cutout or good blending.

For overlays, specify whether the intended result uses ordinary alpha-over or a special blend mode such as Screen. Check that mode in the user's actual editor before relying on it; provide a compatible alternative only with the necessary production scope. Do not promise identical blending across applications or secretly bake effects into an approved background.

Separate artistic raster lettering from editable text. Supply exact copy, reading order, bounds, line breaks, font intent and size/spacing guidance for manual typesetting. Mark unavailable fonts or production specifications `Unknown`. Do not promise font files, editable vector characters, layered PSD/AI files or print readiness from raster assets.

## Existing flattened graphics

Inspect the actual source, transcribe required content and establish what may be reconstructed. Explain feasible separations before production. Label each result by actual method:

- `extracted`: visible content cut out from the supplied pixels; retain source reference and state any processing.
- `reconstructed`: missing/occluded content inferred or repaired; never recovered original pixels.
- `newly_generated`: newly synthesized content, even if strongly guided by the poster.

A generative redraw of a subject is not an extracted cutout. Classify mixed work as reconstructed and describe preserved versus inferred regions. Invisible original text, layers, effects or geometry remain unknown. The same sequential review and per-file acceptance rules apply.

## Delivery

After every asset in the agreed sequence is accepted and outstanding reviews are resolved, ask in the user's language whether they want **separate files or one downloadable ZIP**, unless they already made that choice. Do not ask again or generate a package merely because all assets exist. If the user requested one element, offer delivery of that scope without calling the entire project complete.

Deliver only the explicitly selected versions and requested subset. Include a portable `layer-plan.json` with rejected/unselected version records removed, an `ASSEMBLY.md` with canvas, order, placement, type specifications, blending assumptions and limitations, and an `ASSET_INDEX.json` mapping each delivered asset ID/version to its filename and digest. Preserve complete version history separately in the project. Do not bundle discarded drafts, original private references, unrelated files, the Skill, prompts or a PDF unless requested. Supplied lettering specifications are assets; a preview is optional and must be requested and feasible.

Use the active host's supported file-delivery/archive tools to create a real ZIP or expose the individual files. Creating an archive is file packaging, not permission to re-render, composite, upload to Canva, or publish. Before delivery, re-read selected files, verify their hashes/dimensions and exact inventory, then inspect the actual ZIP entries and decompressed bytes. Retain the sources; no destructive cleanup. Do not claim a download exists before successful creation and availability through the host. If a host cannot package/read back files, report the precise limitation and offer accessible individual files; missing files cannot be supplied as placeholders.

The read-only helper can compute the proposed delivery inventory and verify the result. It does not create files, change approval state or save anything. If Python/Pillow is unavailable, use equivalent observed host checks and disclose Unknown properties; do not silently install dependencies or mark unexecuted tests passed.

## Read-only helper

Run `python3 scripts/layer_assets.py check <project-layer-plan.json>` for structure and the next review/create/delivery decision. `inspect <file>` reports actual raster dimensions, alpha statistics and SHA-256, using Pillow when available. `compare <before.json> <after.json>` reports changed assets, selected versions and composition fields without interpreting the change as approved. `delivery <plan.json> --root <asset-directory>` returns the selected inventory after actual-file checks. `verify-delivery <plan.json> --root <asset-directory> --delivered <directory-or-zip>` verifies only the chosen assets plus the three required sidecars, with exact bytes and selected-only records. All commands return JSON; malformed inputs or failed verification return a nonzero exit code. There are no network calls, retries, credentials or provider costs.

## Examples and evidence

- From scratch: a night-event poster needs an environment, a person with contact shadow, a fog overlay and manual text. Agree on the layout; create the environment first, discuss/revise it, record its acceptance, then continue. A pending title need not block that environment when reading space is fixed. Keep the title in the project copy inventory.
- Replace one element: the accepted person is `v001`. Produce `v002` after a requested wardrobe correction, keep `v001` selected during review, and switch only after explicit approval of `v002`. Recheck the coupled shadow; the background digest remains identical. Never package a rejected `v003` because its filename sorts last.
- Package: when all scoped assets are accepted, offer individual files or ZIP once. Build from selected IDs/versions, verify the delivered inventory, and explain any manual text work still required. Asset-set completion is not certification of the assembled poster.

Official sources checked **2026-09-10**: [OpenAI image generation](https://developers.openai.com/api/docs/guides/image-generation) documents API PNG/WebP transparency and continuing consistency/layout limits; actual host settings still require observation. [Canva upload formats](https://www.canva.com/help/upload-formats-requirements/) supports raster uploads and notes possible flattening of imported AI layers. [Illustrator linked and embedded files](https://helpx.adobe.com/illustrator/using/manage-linked-and-embedded-files.html) describes placed-file management and replacement. These sources support the handoff approach, not a claim that this project's assets have been generated, imported or visually tested.
