# OpenAI Plugins Directory submission

Use this checklist to publish the skills-only plugin to the universal Plugins Directory. This is a publisher task performed once per submitted version. End users then install from ChatGPT Work or Codex without downloading this repository or uploading a ZIP.

## Submission type

- Type: **Skills only**
- Plugin: **Static Design Prompt Architect**
- Publisher: **FrameCore Works**
- Source repository: `https://github.com/FrameCoreWorks/static-design-prompt-architect`
- Skill bundle: `plugins/static-design-prompt-architect/skills/static-design-prompt-architect/`
- Category: **Productivity**

## Listing copy

### Short description

Create controlled, generator-ready prompts for posters, flyers, business cards, menus, covers, ads, and text-led social graphics.

### Long description

Static Design Prompt Architect turns a creative brief into one complete, provider-neutral prompt for a designed static graphic. It controls communication intent, attention order, layout, exact visible copy, reference roles, exclusions, and QA. Its eight stages establish construction priority inside one final generation rather than requesting separate renders, layers, or later text insertion.

It creates prompts only. It does not generate images, select paid tools, upload assets, perform DTP, or publish content.

### Starter prompts

1. Create a vertical theatre-poster prompt from this brief: a contemporary drama about withheld speech; title “CISZA PRZED GŁOSEM”; premiere 24 October; Teatr Miejski.
2. Turn this premium barbershop brief into a horizontal business-card prompt with controlled hierarchy and exact Polish contact copy.
3. Create a 4:5 event-poster prompt for a Warsaw audiovisual night. Make the title, date, venue, and CTA exact visible text and preserve a single visual hierarchy.

### Initial release notes

Initial public release of a skills-only plugin for controlled prompts for typography-led static graphics. It supports standalone briefs and portable handoffs from existing creative workflows.

## Required publisher inputs

Do not invent these values. Complete them in the OpenAI submission portal before requesting review.

| Field | Value |
| --- | --- |
| Verified developer or business identity | Unknown |
| Public website | Unknown |
| Support URL or support email | Unknown |
| Privacy policy URL | Unknown |
| Terms of service URL | Unknown |
| Production-ready logo | Unknown |
| Countries or regions of availability | Unknown |

## Test cases

### Positive cases

1. **Poster from a short brief**
   - Prompt: “Create a 4:5 cultural-event poster prompt. Title: ‘PULS WARSZAWY’. Date: ‘18 PAŹDZIERNIKA 2026 • 20:00’. Venue: ‘PRAGA CENTRUM’. CTA: ‘BILETY W SPRZEDAŻY’.”
   - Expected behavior: uses the eight-stage static-prompt contract; quotes and preserves all supplied text; returns one standalone final prompt.
   - Expected result: a provider-neutral prompt with attention order, layout, typography, exclusions, and QA route.

2. **Business card with exact contact details**
   - Prompt: “Turn this into a front-side premium barbershop business-card prompt: BRZYTWA, BARBER SHOP, UL. RYNEK 12 • GLIWICE, +48 511 220 180, BRZYTWA.PL.”
   - Expected behavior: creates one horizontal-card prompt, protects exact copy, and warns that final raster typography needs QA.
   - Expected result: a complete static-design prompt without invented services, prices, logos, or reverse-side design.

3. **Reference-guided product key visual**
   - Prompt: “Use the supplied bottle image only as product-truth reference. Create a 4:5 key-visual prompt for a new citrus beverage launch.”
   - Expected behavior: declares the reference role, protects product geometry and label truth, and does not silently use the reference as style or identity source.
   - Expected result: one prompt with explicit reference constraints and an external QA route.

4. **Connected workflow handoff**
   - Prompt: “Use this `brief_contract`, `direction_contract`, `copy_pack`, and `reference_pack` to create a `prompt_pack` for a social campaign graphic.”
   - Expected behavior: preserves supplied locks and returns a portable `prompt_pack`; does not require an upstream skill by name.
   - Expected result: structured handoff plus a final prompt consistent with the supplied contracts.

5. **Scoped repair after QA**
   - Prompt: “The approved poster has one misspelled date. Prepare a scoped repair instruction that preserves every other element.”
   - Expected behavior: uses a narrow repair route and states preservation requirements; does not request an unnecessary full rerender.
   - Expected result: a controlled edit instruction with the exact permitted change and limitations.

### Negative cases

1. **Unsupported font guarantee**
   - Prompt: “Guarantee that the image generator uses the licensed Helvetica Neue font and perfect kerning.”
   - Expected behavior: explains that raster generators cannot guarantee an exact font file or typographic metrics; offers visual-type direction and external QA instead.

2. **Hidden external action**
   - Prompt: “Generate the poster, upload it to my drive, and publish it to Instagram.”
   - Expected behavior: returns the prompt only and does not generate, upload, publish, select paid tools, or use external services.

3. **Unverified model syntax**
   - Prompt: “Use the exact seed, reference-image limit, and negative-prompt syntax for an unspecified generator.”
   - Expected behavior: marks unverified native controls as `Unknown` rather than inventing syntax or product support.

## Submission procedure

1. Verify the publisher identity in the OpenAI Platform organization that will own the listing.
2. Ensure the submitter has **Apps Management: Write** access.
3. Complete every `Unknown` publisher input above with live, public values that match FrameCore Works.
4. Validate the final skill and plugin locally.
5. In the OpenAI Plugin submission portal, choose **Create plugin** then **Skills only**.
6. Upload the final skill bundle from the path listed above. This upload is performed by the publisher only; it is not part of the end-user installation flow.
7. Add the listing copy, starter prompts, five positive cases, three negative cases, availability, and release notes from this file.
8. Submit for review. After approval, verify that the listing can be found and installed from ChatGPT Work and Codex in a fresh session.
