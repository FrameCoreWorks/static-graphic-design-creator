# Unified Static Prompt Contract

Use this contract for posters, flyers, business cards, menus, labels, covers, key visuals, advertisements, and text-led social graphics. It produces one final raster-design instruction, not an assembly plan.

## Non-negotiable construction rule

The eight stages are construction priority inside one generation. They must never request eight outputs, intermediate images, blank typography zones for later copy, separate layer files, or a manual compositing pass.

## Objective-first preflight

Before compiling any of the eight stages, resolve the poster strategy in this order: communication goal; required audience response; reading mode and copy burden; visual thesis; composition archetype and attention order; image/type roles and hierarchy; style family or original attributes; material treatment. Classify visible content as `must_read`, `should_read`, `metadata`, or `decoration`. Do not select a style first and retrofit a goal around it.

For an open poster brief, return a `discovery_brainstorm` before the final prompt. For a directed brief, use `directed_collaboration`: keep the user's chosen direction, make the strategy explicit, and challenge it only when a concrete conflict would damage clarity, accessibility, copy feasibility, or the stated objective.

## Prompt compactness

Resolve all eight stages, but do not force eight headings or eight long paragraphs. For a simple brief, compile the relevant decisions into one concise, readable prompt. For a complex text-led design, use short labelled segments or paragraphs in the same semantic order. Do not duplicate a constraint across stages unless it is a critical lock, such as exact visible copy, protected identity, product truth, or one permitted scoped edit.

## Stage order

1. **Final-output contract**
   - State asset type, one finished output, intended format, communication objective, reading mode, primary attention order, and explicit exclusions such as mockups, collages, grids, or alternate versions. Do not use a style name as the communication objective.
   - Name one design thesis and one layout mechanism. Examples: a route carries information; type contains the image; a physical interruption enacts the message; repetition enacts motion.

2. **Background and spatial foundation**
   - Define the background field, colour structure, material treatment, protected reading zones, negative space, safe margins, and the spatial logic that permits the intended hierarchy.
   - Do not treat paper grain, collage, photocopy, a barcode, a single accent colour, or display type as universal defaults. Include each only when it has a specific communication role.

3. **Layout architecture and attention flow**
   - Declare the composition archetype, focal axis, relative scales, alignment logic, reading rhythm, and the relationship of large, medium, and functional information.
   - Make first, second, and third notices visibly testable. Avoid equal-weight modules and arbitrary central placement.

4. **Hero and protected source assets**
   - Define the single dominant person, product, object, scene, or supplied source asset. State scale, placement, depth, light, material, and protected properties.
   - When a reference is supplied, name its role. A style reference cannot silently replace a product-truth, logo, or identity reference.

5. **Supporting graphic elements**
   - Add only secondary elements that guide the eye, encode information, establish brand recognition, or reinforce the layout mechanism. State each element's position and job.
   - Remove decorative particles, arbitrary icons, unnecessary frames, meaningless geometric marks, and unrelated image fragments.

6. **Typography and functional information**
   - Quote every required visible string exactly. State whether it is `must_read`, `should_read`, `metadata`, or `decoration`, then state hierarchy, type role, placement, intentional line breaks, contrast, colour role, and allowed text count.
   - Describe a type category and visible behaviour instead of asserting that a raster generator has access to a named font file. Keep small functional copy compact and legible. If critical or dense information cannot survive raster QA, stop before generation and route to DTP rather than treating it as decorative pseudo-text.

7. **Colour, light, and material integration**
   - State how the selected style attributes, colour, light, contrast, surface, and depth bind the composition together. Use a limited compatible palette and motivated light. Treat lithography, screenprint, risograph, letterpress, collage, photomontage, offset, or halftone as visual material simulation unless a real production process is separately confirmed. Tie every process cue to a visible cause such as separation, overprint, register, relief, paper absorption, or dot structure; never use a generic vintage/damage filter.
   - Protect readable copy through contrast and layout, not by stacking unnecessary panels, glows, or effects behind every string.

8. **Finish, exclusions, and acceptance checks**
   - Finish with optical alignment, calibrated spacing, restrained material evidence, safe margins, and high-priority legibility.
   - Exclude unwanted additions. State observable pass conditions and the required repair route if exact text, identity, product truth, or hierarchy fails.

## Design checks before delivery

- There is one dominant anchor.
- The visual mechanism supports the message rather than decorating it.
- Type and image have a defined relationship.
- Every major element has a reason to exist.
- Removing an element was considered.
- Functional information remains compact and readable.
- No generic stock-like staging, collage clutter, arbitrary effects, or unsupported technical claim remains.
- The composition cannot be swapped onto an unrelated event without changing its visual thesis.
- A generic cityscape, decorative smoke, particle field, neon glow, pseudo-3D object, or arbitrary texture appears only when it performs a named communication job.
- Critical text is not used as filler, pseudo-glyphs, or decorative texture.
- A political position, factual claim, cultural representation, or charged historical symbol remains user-confirmed rather than inferred from a visual movement.
