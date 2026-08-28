# Deliverable Profiles

Use these as selection rules, not fixed aesthetics. Take the visual thesis and copy hierarchy from the brief; do not turn every output into the same poster language.

| Deliverable | Dominant job | Layout emphasis | Text risk |
| --- | --- | --- | --- |
| Cultural or music poster | Intrigue, recognition, conversion | One hero and a strong reading sequence | Medium |
| Civic or social poster | Immediate comprehension and action | Message mechanism before decoration | Medium |
| Theatre or literary poster | Interpretive tension | Title-image relationship and controlled negative space | Low to medium |
| Commercial key visual | Product or offer recognition | Product truth, CTA, brand hierarchy | Medium |
| Flyer | Fast conversion | Compact information block and clear CTA | Medium to high |
| Business card | Recognition and contact retrieval | Precise safe margins and sparse information | High |
| Menu or price card | Scannable choices | Repetition, contrast, and stable vertical rhythm | High |
| Label or packaging front | Shelf recognition | Brand, product name, claim, and physical material | High |
| Book or album cover | Memorability and identification | Title-author relation and singular visual thesis | Low to medium |
| Text-led social graphic | One-message recall | Hook, one dominant image mechanism, compact CTA | Medium |

## Selection rules

- Resolve `production_intent` before applying a deliverable profile. Use `concept_raster` for directional visual exploration, `digital_final` for a QA-passed raster intended for publication, and `production_master` for editable or print-ready production work that must route to DTP.
- For a business card, menu, label, or dense flyer, reduce copy before making the prompt longer. Treat contact data, legal copy, prices, and small labels as high-risk raster text requiring QA.
- For a poster, do not use a generic cityscape, equal-weight collage, or unrelated texture as a substitute for a visual thesis.
- For a commercial asset, preserve declared product and logo truth. Never invent product features, prices, claims, certification marks, or brand names.
- For a cover, make the visual thesis and title cooperate. Do not use a book mockup unless the user explicitly requests a mockup.
- For a social asset, place action-driving copy within platform-safe areas declared by the user or verified profile. If no profile exists, mark safe-area behaviour `Unknown`.
