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

Record the observed output mode, render status, QA route, and any deviation. A release passes only when all eight cases match the contract or an intentional contract change updates both the behavior fixture and this document.
