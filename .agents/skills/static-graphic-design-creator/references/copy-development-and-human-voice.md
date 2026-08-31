# Copy Development and Human Voice

Use this internal asset when a static graphic needs visible wording but the user has not supplied final copy, asks for stronger wording, or says that an existing headline feels generic. It is the single copywriting-and-human-voice layer for this Skill. It develops the exact on-screen wording and makes it specific, credible, and usable in the design; it does not invoke another named Skill.

## Purpose and boundary

Own the progression from an unresolved message to selected visible copy:

`communication objective → audience response → message tension → copy routes → selected wording → human-voice review → text lock → graphic hierarchy`

Do not invent product facts, prices, outcomes, testimonials, legal claims, affiliations, history, or a speaker's personal experience. Preserve user-supplied and source-supplied wording when it is locked. Do not imitate a living writer, simulate careless mistakes, or optimise wording to evade AI detection.

## Inputs

Establish:

- the asset type, communication objective, audience, placement, reading mode, and desired audience response;
- source truth, claims that may be made, required words, prohibited words, and brand or speaker voice;
- whether the user supplied final copy, a draft to improve, or no usable wording;
- the available text hierarchy: headline, support line, CTA, metadata, legal or operational text.

Ask one concise question only when its answer would materially change the message, claim boundary, speaker, or action. Otherwise mark the missing detail `Unknown` and draft only from known truth.

## Copy routes

### `locked_copy`

Use when the user or a verified source supplied final visible wording.

- Quote it exactly.
- Classify its hierarchy and feasibility.
- Do not rewrite, shorten, humanise, correct, or “improve” it unless the user explicitly requests that operation.

### `copy_discovery`

Use when the user has a visual goal but no settled headline, support line, or CTA.

1. Resolve the communication objective and one concrete message tension, observation, proof, action, or image relationship. Do not use a vague adjective as the message.
2. Return two to four materially different copy routes before a final prompt or render.
3. For each route provide: `message_thesis`, `headline`, optional `support_line`, optional `CTA`, intended text hierarchy, and one short reason it fits the stated objective.
4. Make routes structurally different. Do not present synonym swaps or a list of interchangeable slogans.
5. Ask the user to select, combine, or redirect a route. Do not treat an unselected assistant draft as final visible copy.

### `copy_refinement`

Use when the user supplies a draft and explicitly asks for stronger, clearer, more natural, or less generic copy.

- Preserve locked facts, required phrases, the real speaker, and the intended action.
- Produce a small set of meaningfully different revisions, not cosmetic rewrites.
- Explain one material trade-off only when it affects clarity, claim safety, or fit with the visual hierarchy.
- Wait for selection before setting the final text lock.

## Anti-generic copy standard

Build wording around a concrete communicative mechanism. Prefer an exact verb, object, place, behaviour, contrast, or consequence over abstract praise.

Reject or repair:

- interchangeable praise such as “exceptional quality”, “discover the future”, “make your dreams real”, or “an experience like no other” when it is not supported by source truth;
- slogans that could advertise an unrelated product, event, or institution;
- headline, support line, and CTA that repeat the same claim in different words;
- decorative wordplay that obscures the action, offer, date, or audience;
- fake intimacy, invented testimony, empty urgency, or automatic marketing scaffolding.

Human voice means that the wording has a credible speaker, real audience, appropriate distance, rhythm, and channel fit. It does not mean artificial slang, broken grammar, filler, emojis, a forced hook, or a fabricated personal story.

## Human-voice review

Run this review only on the selected route or on a user-provided draft explicitly marked for refinement.

1. Preserve source truth and exact locks.
2. Remove generic phrasing, duplicated explanation, and decorative filler.
3. Check that the wording sounds intentional for the real speaker, recipient, channel, and visual reading mode.
4. Keep the smallest form that performs the communication job. Do not add a CTA, hashtag, headline, question, or emotional claim by default.
5. Return only the selected visible copy and essential copy notes. Do not bury it in a long explanation.

## Copy-fit gate

Before compiling a final static prompt or rendering, resolve:

```yaml
copy_pack:
  copy_route: locked_copy | copy_discovery | copy_refinement
  copy_authority: user_locked | source_locked | user_selected
  message_thesis:
  options: []
  selected_copy:
    headline:
    support_line: []
    cta:
    metadata: []
  claim_status: verified | constrained | Unknown
  copy_locks: []
  copy_fit: selected | locked | needs_selection | dtp_required
```

Proceed to the final prompt only when `copy_fit` is `selected` or `locked`. If dense mandatory wording, legal copy, schedules, prices, contact data, or precise typesetting cannot fit the chosen reading mode, set `copy_fit: dtp_required` and follow the existing DTP route.

## Design handoff

Pass only the selected wording into the visual system. Declare its exact text, hierarchy, placement, line-break logic, colour role, and allowed text count. The image, composition, and type treatment must reinforce the chosen message thesis rather than decorate it.
