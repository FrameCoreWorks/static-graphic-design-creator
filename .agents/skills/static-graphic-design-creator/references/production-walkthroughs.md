# Production Walkthroughs

These compact examples show the decision chain, not reusable event facts. Substitute the user's objective, copy, rights-cleared references, and production constraints. Each example preserves the rule: one complete final prompt describes staged construction priority inside one final generation, not separate image layers or outputs.

## 1. Discovery brainstorm: community night market poster

### Brief

Create a vertical social poster for an evening neighbourhood market. Required copy: `NOCNY TARG SĄSIEDZKI`, `14 CZERWCA • 18:00–23:00`, `SKWER PRZY RZECE`, and `WSTĘP WOLNY`. The organiser wants local warmth, not a generic festival graphic. No visual direction is supplied.

### Routes

| Route | Visual thesis | Composition and language | Trade-off |
| --- | --- | --- | --- |
| `A — shared table` | One long illuminated table makes participation visible. | Asymmetric editorial layout; photograph-like still life as hero; warm letterpress-like ink texture as a restrained treatment. | Feels intimate, not high-energy. |
| `B — market constellation` | Stalls become a single route of light that leads to the information. | Diagonal wayfinding composition; original geometric civic-poster language; one screenprint separation treatment. | More abstract, so the food cue must be clear. |
| `C — hand-made invitation` | The title behaves like a hand-stamped invitation from the neighbourhood. | Centre-weighted broadside composition; vernacular-signage type treatment; one halftone portrait-free ingredient image. | Requires very compact copy to stay legible. |

### Selected route and strategy

Select route `B` because the primary audience response is orientation and welcome at a glance. `must_read`: title, date/time, venue. `should_read`: free entry. Visual mechanism: one vermilion route crosses a nocturnal field and terminates at a glowing market-table silhouette. Primary poster language: original geometric civic poster. Secondary treatment: two-colour screenprint simulation with intentional overprint only at the route intersection.

### Final eight-stage prompt

```text
Create one finished vertical 4:5 social poster, not a mockup, collage, grid of variants, device frame, or separate-layer plan. Its communication objective is to make a neighbourhood evening market feel easy to find and worth joining. Reading mode: glance. First notice “NOCNY TARG SĄSIEDZKI”, second notice the illuminated route and market-table silhouette, third notice the date, venue, and free-entry line. Use one visual thesis: a single route of light gathers neighbours and carries the eye to the information.

Build a near-black midnight-blue field with generous negative space, warm uncoated-paper tactility, and a protected upper title zone plus a protected lower information zone. Use warm off-white, midnight blue, vermilion, and one muted apricot accent only.

Set an asymmetric diagonal composition: the title anchors the upper left; a vermilion route begins at the left edge, crosses the centre once, and guides toward the lower information block. Keep wide safe margins and a large-to-small reading rhythm. The route must never cross readable copy.

Use one central, simplified night-market table silhouette with practical lamps as the only hero. It is warm, physical, and recognisably communal without people, logos, city landmarks, or stock-event staging. Keep its scale secondary to the title and directly connected to the route.

Add only functional supports: two small geometric stall-light shapes along the route and one restrained cobalt alignment rule that stabilises the lower information block. Every mark must guide attention or reinforce the route; no particles, smoke, neon UI, arbitrary icons, or decorative collage fragments.

Render only these exact visible Polish strings: “NOCNY TARG SĄSIEDZKI”, “14 CZERWCA • 18:00–23:00”, “SKWER PRZY RZECE”, and “WSTĘP WOLNY”. Set the title as a bold, compact geometric display treatment in warm off-white. Set date/time and venue as precise functional sans-serif text in warm off-white. Set “WSTĘP WOLNY” as a small vermilion CTA. Preserve every diacritic, word order, and punctuation; render no other readable text.

Integrate the palette with two-colour screenprint logic: flat midnight-blue and off-white fields, vermilion route, and a small intentional apricot overprint only where route meets hero light. Simulate paper absorption and controlled registration without generic damage, noise, or vintage filtering. Protect all copy through contrast and space, not glow boxes.

Finish with optical alignment, restrained ink texture, intact safe margins, and an observable hierarchy. Reject the result if the title, route, and practical information do not read in that order, if any copy is misspelled, or if the poster could be reused for an unrelated event without changing the central route-and-gathering idea. If one local text defect remains, use a scoped edit; if the hierarchy or route mechanism fails, fully rerender from this complete prompt.
```

## 2. Directed collaboration and Codex crosswalk: bookshop membership card

### Brief and preserved direction

The user asks for a minimalist horizontal membership card with a supplied monochrome bookshop logo, the exact name `KARTA CZYTELNIKA`, a member number, and a quiet Swiss-grid influence. The goal is efficient recognition, not an expressive poster. Preserve the logo as an identity reference and do not turn a named style into a substitute for the card's information architecture.

### Six-section compatibility profile

| Crosswalk section | Resolved decision |
| --- | --- |
| Intent | Digital membership-card concept, brief-scan reading mode, professional and calm. |
| Canvas and layout | Horizontal 3:2 card, generous margin, three-column grid; exact number treated as metadata. |
| References | Attached logo is identity truth only; Swiss reference translates to grid discipline, not copied artwork. |
| Visual system | Off-white field, black type, one deep-red registration mark; no fake embossing or glass effects. |
| Text system | Name is must-read, number is metadata, no extra text. |
| QA and limits | Raster concept only; exact final card, font licensing, barcode, and print production route to DTP. |

## 3. QA repair: scoped edit

### Observed render

The approved poster has correct hierarchy, route, hero, colours, and all text except `CZERWCA`, rendered without the final `A`.

### Decision

`scoped_edit`, because exactly one observable spelling defect remains and the rest is approved.

```text
Change only the visible date string from “14 CZERWC” to “14 CZERWCA”. Preserve the approved poster exactly: its composition, crop, scale, title, route, hero, colour system, light, texture, all other visible text, text positions, safe margins, and hierarchy. Do not add, remove, translate, restyle, or reposition any other element.
```

## 4. QA repair: full rerender

### Observed render

The title is readable but the hero is an unrelated neon skyline, date and venue compete with the title, and the route is absent. The central thesis failed, so appending exclusions would not repair it.

### Decision

`full_rerender`. Rebuild the complete prompt from the selected route. Preserve only verified source facts and locked copy; restate the route-as-wayfinding mechanism, one hero, reading order, and every exact text string. Do not treat the old render as an approved reference.
