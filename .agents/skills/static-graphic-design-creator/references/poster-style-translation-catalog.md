# Poster Style Translation Catalog

Use this reference when a user names a popular style label, asks what visual direction fits a poster, or requests an open style brainstorm. It converts broad labels into a usable poster strategy. It does not replace the goal-first sequence in [the poster style and composition atlas](poster-style-and-composition-atlas.md) or the historical and process guidance in [the poster movements and production atlas](poster-movements-and-production-atlas.md).

## Core rule

Treat a requested label as evidence, not as a finished instruction. Resolve this order before using it in a prompt:

`communication goal → audience response → reading mode and copy burden → visual thesis → composition and attention order → primary poster language → compatible rendering or material treatment`

Choose at most **one primary poster language** and **one compatible secondary treatment**. Do not create a stack of unrelated labels such as `Swiss + cyberpunk + glassmorphism + Victorian + risograph` unless the user explicitly asks for a deliberate hybrid and every part has a named job. A colour palette, a texture, a 3D rendering method, or a type treatment is not by itself a poster strategy.

## Label classes

| Class | What it controls | Examples | Decision rule |
| --- | --- | --- | --- |
| `historical_language` | form, type-image relation, composition, cultural context | Art Nouveau, Art Deco, Constructivist, Swiss, Victorian | Read the movements atlas; translate transferable attributes, never reproduce a work or a named designer |
| `contemporary_visual_language` | a recognisable contemporary visual system | cyberpunk, Y2K, brutalist, punk-zine, solarpunk | State what message and audience make it useful; do not use it as a generic effect pack |
| `composition_stance` | degree of reduction, density, order, or disruption | minimalism, maximalism, editorial | Pair it with a concrete composition archetype |
| `image_construction` | how the image or spatial field is built | vector, collage, pixel, clay, photomontage | Define source hierarchy, scale, and image role before rendering |
| `material_or_surface_treatment` | local visible material behaviour | screenprint, halftone, aurora gradient, glass surface | Use only when it reinforces hierarchy, subject, or medium; it cannot replace a thesis |
| `type_treatment` | expressive character of lettering | handwritten, graffiti-derived, blackletter-derived | Protect exact copy and keep functional information in a separate readable level |
| `ambiguous_mood_label` | a feeling with no fixed visual system | retro, bohemian, premium, futuristic | Ask for a period, use context, or visible attribute set; do not invent one |

## Screenshot labels: translation cards

The labels below are supported as requests, but they must be translated through the decision order above.

| User label | Correct classification | Translate it into | Strong fit | Guardrail |
| --- | --- | --- | --- | --- |
| `minimalism` | composition stance | one dominant sign or word, severe element reduction, protected negative space, limited palette, two-level type hierarchy | premium product, cultural title, civic signal, cover | Minimal is not empty. The remaining object, word, or datum must carry the message. |
| `maximalism` | composition stance | intentional density, controlled collisions, multiple authored micro-systems, a strict reading path, one stabilising datum | festival, youth culture, fashion, experimental culture | It is not equal-weight clutter. Preserve title, date, and CTA as a quiet hierarchy. |
| `futuristic` | ambiguous mood label | first choose a direction: historical Futurist force, speculative industrial, clean scientific, retrofuturist, cyberpunk, or solarpunk | technology, music, innovation, science fiction | Ask or state the chosen future. Do not default to chrome, neon, or generic city lights. |
| `vector art` | image construction | clean silhouette, flat colour regions, deliberate contour, scalable icon/object logic, simple spatial layers | public information, family event, product diagram, campaign system | Vector is an image method, not a mood. Avoid stock-icon sameness and unmotivated gradients. |
| `collage art` | image construction | selected material contrast, purposeful crop edges, source hierarchy, one governing spatial relation | editorial, theatre, civic, cultural event | Every fragment needs a semantic job. Do not create a scrapbook of equal-weight pieces. |
| `retro` | ambiguous mood label | name a period and mechanism: interwar travel, mid-century object poster, 1970s print, 1990s rave, early-web Y2K, etc. | nostalgia, product storytelling, period event | Reject generic old paper, sepia, scratches, and era mixing without purpose. |
| `cyberpunk` | contemporary visual language | dense night infrastructure, hard artificial light, information fragmentation, high/low-tech contrast, compressed perspective | speculative fiction, gaming, nightlife with a narrative reason | Neon and rain are not enough. Protect functional copy and avoid default dystopian cityscape. |
| `pop art` | historical/formal language | repetition or enlargement, flat spot colour, halftone tied to reproduction, commercial-code tension, graphic irony | retail, youth activation, cultural commentary | Do not reduce it to comic bubbles and dots; use a real message-image tension. |
| `glassmorphism` | digital surface treatment | restrained translucent panel, edge refraction, soft depth plane, legible opaque text layer, controlled background blur | digital-first social announcement, technology, app-adjacent event | Not a print-first language. Never put essential long copy on transparent or low-contrast glass. |
| `clay style` | image construction / 3D treatment | tactile simplified sculptural forms, soft studio light, clear object geometry, deliberately toy-like scale | family event, education, playful product, children’s culture | Do not let cute 3D replace event information. Preserve product geometry and avoid generic mascot clutter. |
| `pixel art` | image construction | intentional pixel grid, limited palette, authored resolution, crisp cluster logic, bitmap-type compatibility | game event, retro-tech, youth activation | State the intended pixel scale. Do not apply a pixel filter to an otherwise unrelated realistic image. |
| `editorial` | composition stance | clear hierarchy, purposeful crop, headline/deck/caption roles, image as evidence or argument, measured grid | talk, exhibition, magazine-led culture, public information | Editorial does not mean a fashion photo plus tiny text. Define the argument and reading order. |
| `Y2K` | contemporary visual language | early-digital optimism, translucent plastic or chrome used sparingly, inflated curves, bright optimistic contrast, interface-era geometry | music, fashion, nostalgia, youth event | Distinguish from cyberpunk: Y2K is usually bright and optimistic. Avoid a random 2000s icon dump. |
| `Swiss design` | historical language | measured grid, objective hierarchy, restrained sans-serif type behaviour, image-type precision, deliberate white space | information, conference, design culture, campaign system | Read the movements atlas. A grid must improve reading, comparison, or repeatability. |
| `surreal design` | conceptual visual language | one improbable but exact relation, altered scale, visual riddle, restrained supporting field | theatre, literary work, awareness, art-house film | The riddle must deepen the subject. Avoid random dream fragments and generic melting imagery. |
| `bohemian` | ambiguous mood label | translate to a chosen authored quality such as artisan material contrast, informal rhythm, botanical or textile-derived colour, or travel-journal collage | craft, intimate community, independent culture | It is not a historical school and can stereotype cultures. Name the actual material or regional authority if relevant. |
| `Victorian style` | period language | engraved or wood-type-informed contrast, ornamental border logic, display/utility type distinction, controlled dense framing | heritage, gothic literature, theatre, historical event | Specify a subdirection where needed: industrial broadside, botanical illustration, gothic revival, or late-Victorian advertisement. Do not add generic grime. |
| `graffiti` | type treatment / street visual language | original marker, stencil, wheatpaste, or spray-derived gesture; scale and placement with a specific expressive role | youth event, urban culture, music, activism with approval | Do not imitate living writers, invent tags, or imply vandalism. Keep critical information outside the expressive gesture. |
| `aurora` | surface treatment | one ambient colour field with slow chromatic transition, light-like depth, controlled dark-to-light contrast | wellness, music, technology, nocturnal culture | Aurora is a background behaviour, not the hero. It must not lower text contrast or become generic AI glow. |
| `handwritten` | type treatment | one authored display gesture, documented line-break rhythm, contrast-protected functional type in a separate system | personal invitation, community, food, craft, intimate culture | Handwriting cannot carry dense dates, addresses, prices, or legal text without external typesetting QA. |

## Additional curated directions for posters

Offer these only when their mechanism fits the brief. They are not a menu that must be exhausted during a brainstorm.

| Direction | Classification | Usable attributes | Strong fit | Guardrail |
| --- | --- | --- | --- | --- |
| `brutalist_information` | contemporary visual language | blunt scale contrast, exposed hierarchy, direct type, raw but intentional spacing, limited palette | manifesto, architecture, music, institutional critique | Not ugliness-by-default. Preserve reading logic and do not use arbitrary browser-interface debris. |
| `postmodern_memphis` | historical/formal language | playful geometry, patterned rhythm, controlled colour disagreement, expressive but repeatable rules | family culture, design event, playful retail | Do not scatter shapes indiscriminately. The composition still needs a dominant anchor. |
| `new_wave_typography` | typographic visual language | expressive scale shifts, intentional baseline disruption, layered type-image relation, asymmetric energy | music, fashion, experimental culture | Declare which words remain immediately readable; avoid for dense schedule information. |
| `punk_zine` | image construction / type treatment | photocopy contrast, cut-and-paste hierarchy, stamped or typewritten energy, one urgent claim | grass-roots action, independent music, small cultural event | Use original text and imagery. Do not fabricate political facts or misuse protest iconography. |
| `vaporwave` | contemporary visual language | deliberate late-digital nostalgia, calm synthetic horizon, limited pseudo-classical or interface sign, controlled colour drift | music, nostalgia, speculative culture | Different from Y2K and cyberpunk. Avoid generic statues, grids, and purple fog without a thesis. |
| `solarpunk` | contemporary visual language | optimistic infrastructure, repair and community cues, daylight, botanical-technical coexistence, readable civic optimism | climate, education, community, speculative future | Do not make unverified environmental claims or use nature as decorative wallpaper. |
| `biomorphic_organic` | formal language | soft asymmetric forms, growth-like rhythm, tactile contour, calm field, living-system analogy | wellness, culture, science, family | Do not collapse it into generic blobs. Give each form a spatial or semantic role. |
| `neo_noir` | narrative visual language | decisive shadow, restricted light source, cropped evidence, tension between concealment and disclosure | film, crime fiction, late-night culture | Readability must remain intentional; it is not simply a black poster with a red glow. |
| `woodcut_linocut` | print-derived visual simulation | carved positive/negative shape, limited colours, pressure-like irregularity, bold contour | heritage, music, literary work, activism | Preserve a plausible mark logic; do not add generic distress. Physical production remains a separate decision. |
| `stencil_broadside` | type treatment / public-message language | cut-letter rhythm, high contrast, modular repeatability, one message carried by the letterform | announcement, community action, street-adjacent culture | Ensure counters and diacritics remain legible. Do not imply official notices or real organisations without approval. |
| `comic_narrative` | image construction | intentional panel logic or one frozen action, speech/caption hierarchy when relevant, clean silhouette, controlled expressive line | youth event, education, entertainment | Do not use speech bubbles as generic decoration or overload a poster with a page of panels. |
| `isometric_system` | spatial construction | measured axonometric view, object-system relation, repeated scale, navigable diagrammatic space | conference, technology, education, service explanation | It is not a substitute for factual accuracy. Dense instruction remains a DTP risk. |
| `monochrome_duotone` | colour system | tonal hierarchy through one or two inks/colours, silhouette or photographic integration, contrast-led emphasis | culture, low-cost print feel, civic signal | A duotone needs a clear information advantage, not merely a fashionable filter. |
| `sports_editorial` | hybrid composition language | athlete/object cut-out with real movement logic, strong directional crop, numerical datum as hierarchy, decisive field | recruitment, tournament, fitness | Protect anatomy, ball/equipment scale, event facts, and team identity. |
| `vernacular_signage` | type and material language | locally authorised sign-painting rhythm, modest display hierarchy, direct object/message relation | food, community, small business, place-based culture | Do not imitate a community’s lettering tradition without authority. Avoid faux-authenticity. |

## Brainstorm use

When a brief is open, offer two to four routes with different mechanisms, not merely different labels. For each route name the selected primary language and optional treatment separately.

```text
ROUTE: [original route name]
Goal: [audience outcome]
Visual thesis: [one original relation]
Composition: [archetype and notice order]
Primary language: [one catalog language]
Secondary treatment: [one compatible material, image, or type treatment; optional]
Readable copy level: [must_read and should_read placement]
Why it fits: [goal-linked reason]
Trade-off: [legibility, production, tone, or complexity cost]
```

If the user supplied a specific label, use `directed_collaboration`: preserve it, translate it into visible attributes, and flag one conflict only when it harms the brief. If the label is broad or internally contradictory, ask one short question or state a reversible interpretation before authoring the final prompt.

## Selection and QA checks

Before delivery, confirm all of the following:

1. The label changed the composition, type-image relationship, and colour/material logic, not just the surface effect.
2. The selected language fits the communication goal and required reading mode.
3. `must_read` information is not carried solely by handwritten, graffiti-derived, warped, transparent, pixelated, or low-contrast type.
4. A historical label has an identified period or mechanism; `retro`, `bohemian`, and `futuristic` were not left undefined.
5. A cultural, political, regional, or street-language reference has the required human authority and does not claim real affiliation, facts, or authorship.
6. A physical-process look has visible process logic and is described as a visual simulation unless physical production is separately confirmed.
7. The design can remove its title without becoming an interchangeable mood image for another event.

If two or more checks fail, return to the poster strategy, not to a longer list of effects or exclusions.

## Source anchors

Use these sources when historical clarification is material to the request. They support the decision logic; routine poster work does not require a live search.

- [V&A: A short history of the poster](https://www.vam.ac.uk/articles/a-short-history-of-the-poster)
- [V&A: Art Nouveau as an international style](https://www.vam.ac.uk/articles/art-nouveau-an-international-style)
- [V&A: An introduction to Art Deco](https://www.vam.ac.uk/articles/an-introduction-to-art-deco)
- [Poster House: The Swiss Grid](https://swissgrid.posterhouse.org/)
- [Poster House: Swiss International Style timeline](https://access.posterhouse.org/exhibition/24th-timeline-cafe/)
- [Cooper Hewitt: psychedelic poster collection and history](https://www.cooperhewitt.org/tag/poster/)
- [MoMA: Central European avant-garde advertising and design](https://post.moma.org/advertisement-as-collaboration-in-the-central-european-avant-garde-magazines-2/)
- [V&A: print and screenprinting](https://www.vam.ac.uk/articles/what-is-print)
