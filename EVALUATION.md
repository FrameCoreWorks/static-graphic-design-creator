# Forward Evaluation

Run these cases against a freshly installed Skill before a release. This is a manual host evaluation: it checks the actual ChatGPT Work or Codex behavior that structural tests cannot prove. Do not use an external API, paid provider, upload, or publish action.

1. Explicit prompt: ask for a copyable poster prompt. Expect one complete prompt and no image.
2. Explicit render: ask to generate a poster with compact copy. Expect native generation only when the host capability is available, followed by QA rather than an automatic second render.
3. Both outputs: ask for the finished graphic and its exact prompt. Expect one render and one fenced prompt.
4. Ambiguous brief: provide only a poster brief. Expect the question `Wygenerować grafikę czy przygotować gotowy prompt?` and no render.
5. Unavailable native capability: request a render where no built-in generation route exists. Expect `render_status: unavailable` and the finished prompt, with no external fallback.
6. Production master: request a print-ready business card with licensed font, bleed, and editable source. Expect `dtp_required` and no raster render.
7. Dense copy: request an exact price list, legal copy, and contact table. Expect `dtp_required` and no text-free-background workaround.
8. Conflicting references: provide two equal-priority product-truth references that disagree. Expect a clarification before prompt writing or rendering.
9. Open civic or social poster: provide a topic and event details but no goal, visual thesis, composition, or style. Expect two to four objective-first `discovery_brainstorm` routes, no final generic prompt, and no render.
10. Directed poster: provide a concrete objective, composition, historical style family, and compact copy. Expect `directed_collaboration`: preserve the direction, flag only a material conflict, then return the requested prompt or render route without forced alternatives.
11. Named-artist style request: request an artist's poster style. Expect a translation into original transferable attributes, never a direct imitation or copied composition.
12. No-op update: paste the update prompt when the installed source-release record and every source hash match the latest release. Expect `already_up_to_date`, no approval request, and no Skill rewrite.
13. Verified update: install an earlier release, then paste the update prompt. Expect a concise Delta with changed/new/removed source files and explicit approval before the existing Skill is updated. Do not expect a duplicate Skill.
14. Update conflict: simulate an installed file modified after its recorded release or a source-release record for a different repository. Expect `blocked_local_conflict` or `blocked_source_identity`, no overwrite, and no fallback replacement.
15. Named historical language: ask for a cultural poster with `Polish Poster School` as a reference. Expect the Skill to preserve a concise metaphor and type-image tension, not reduce the route to painterly-surreal tokens or a named-artist imitation.
16. Process-specific materiality: ask for a screenprint or Risograph-inspired poster. Expect a limited palette, separation/overprint/paper logic, and no generic vintage, damage, or mandatory misregistration filter.
17. Psychedelic information conflict: request a glance-speed event poster with an unresolved psychedelic direction. Expect a concise question about intentional legibility friction before finalising the route.
18. Political poster: provide an unconfirmed political position or charged historical symbol. Expect a clarification and no invented claim, documentary image, organisation, or stance.
19. Dense information flyer: request a detailed programme, times, prices, contacts, and terms. Expect `dtp_required`, no raster substitute, and no default text-free background workaround.

Record the observed output mode, render status, collaboration mode, QA route, update status, apply mode, and any deviation. A release passes only when all nineteen cases match the contract or an intentional contract change updates both the behavior fixture and this document.
