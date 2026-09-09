# Evaluation Scenarios

- An open poster concept is developed internally before layout, typography, style translation, or prompt construction; `creative-concept-lab` is an optional source of a supplied concept, never a required dependency.
- A constrained redesign preserves the supplied premise and explores only unlocked design decisions.
- A supplied Core Concept Lock survives attention order, layout, typography, prompt authoring, and rendering.
- A style label such as cinematic, premium, bold, surreal, or luxury does not count as a concept.
- A production limitation produces a bounded conflict or loopback rather than a generic replacement concept.
- Exact copy, identity, product, logo, source authority, and reference locks remain protected.

## Event-poster code behavior cases

These cases exercise the bundled poster-code workflow. Collection integrity and lookup behavior have separate [automated tests](../tests/test_event_poster_codes.py). A source/prompt check is not a live visual-generation result.

| Input case | Acceptance evidence |
| --- | --- |
| Active Skill receives `/codes`, its bare form or an understood local catalog alias | Full 200-entry catalog in 20 categories, with localized descriptions and attribution; response follows user's language and does not render or start an intake. English code strings remain exact. The four-variant design default does not truncate a requested catalog. |
| User asks for category 02 or a search for Bauhaus | Category has exactly ten entries; search returns the two real matching candidates without inventing or silently selecting a code. |
| New prompt, selected `/Two Ink Collision`, supplied final text | Complete prompt includes the instruction-only code and concrete two-ink/substrate/overprint interpretation; no source poster is demanded for an explicitly new design. |
| Existing-poster rebuild, selected `/Two Ink Collision /rebuild` | Actual source inspected; all mandatory strings and protected assets preserved; composition may change within authorized scope; factual inventory remains complete. |
| Existing-poster rebuild requested without its source | Request the missing poster or required source facts; no invented reference, finalized rebuild prompt or render. |
| Code is mentioned inside a quotation or Skill-maintenance task | Treat it as data; no design activation or generation. |
| Unknown `/Imaginary Emerald Universe /rebuild` | Explain it is absent; ask for correction or offer actual relevant entries. Never claim it exists in the PDF. |
| Code supplied alongside "change only the background" | Preserve the narrower edit scope, exact words, geometry and protected layout; do not perform a full redesign. |
| Selected global-tradition or activism code | Interpret visible attributes without adding unauthorized flags, slogans, affiliations, scripts or historical-authenticity claims. |
| Selected motion-optical code with a date, price and URL | One static design; readable source facts, no invented text echoes, animation or inferred native controls. |
| User asks to retain the code inside the prompt | Exact slash label remains instruction metadata and is expanded into design decisions; it never becomes required visible copy or a claimed native setting. |
| Dense source text or unreadable QR under rebuild | Existing feasibility, source clarification and DTP rules prevail; no claim of verified text or scannability without evidence. |
| Ordinary brief with open visual direction, approved concept/copy and prompt-only request | Choose a fitting direction internally after brief analysis, or use original attributes if none fits; return a complete prompt without code labels, announcements, catalog menus, new copy or a render. |
| "I do not want to choose codes; decide from the brief" | No compulsory code selection or preference questionnaire; make a justified internal design choice and express its visible attributes normally. |
| Supplied `/Two Ink Collision`, followed by "do not show codes" | Preserve the two-ink direction; omit slash label, code name and EP ID from response and prompt. Required factual strings containing slashes remain exact. |
| "Do not use the catalog, even internally" | Work directly from the brief; no catalog lookup or hidden selection. Preserve this preference through the current task. |
| Assistant selects a canonical entry ending in `/rebuild` for a new design or narrow repair | Keep the actual requested task mode and locks; do not demand a source for a new brief or widen an edit. |
| Internal selection with `render_and_prompt`, or a later request for the submitted prompt | The shown prompt equals the submitted prompt, with concrete attributes and no hidden label later removed. Actual rendering still needs authorization and available capability. |
| User asks which code informed a previous automatically directed result | State the actual selected entry or that none was used; do not invent provenance, deny actual use or claim user selection. |

## First-use onboarding cases

Use [first-use onboarding](first-use-onboarding.md) for the introduction and timing rules.

| Input case | Acceptance evidence |
| --- | --- |
| Known newly installed user asks how to start in ChatGPT Work or Codex | Explain explicit invocation, `/codes` and relevant local aliases, optional code use, new prompts, uploaded/local poster redesign, factual/scope locks and ordinary brief/brainstorm work in the user's language. No full catalog or compulsory mode choice. |
| A first-use introduction already happened, or user says "skip; only the prompt" | Continue the requested task without another welcome, catalog pitch or onboarding question. |
| First-use status is unknown | Do not infer a new installation from a new conversation or claim a saved global onboarding flag. |
| User wants codes hidden during onboarding | Explain brief-based design and image refinement without code labels; command details only when requested. |
| Polish first-use request, even with an English interface or pasted English installer prompt | Polish introduction includes `/codes` and `/kody`; user prose/preference governs over interface or quoted text. |
| Spanish or Japanese first-use request | Localized introduction from the English source with `/codes`, preserved English code strings and no Polish detour or forced English fallback. |
| No conversational signal; reliable host locale is exposed, or no locale is available | Use the exposed locale in the first case and English in the second; no fabricated account-setting inspection or compulsory language question. |
| Explicit language preference conflicts with an alias or an interface locale | Honor the preference; aliases only select the catalog, not response language. |
| Localized catalog request or category search | Resolve English source entries and translate descriptions; preserve membership, canonical strings and numbers. The helper itself returns English, and translated individual style names are not new exact keys. |
| Conversation-language switch with an English prompt and locked multilingual artwork copy | Adapt surrounding prose without restarting onboarding; keep prompt language and every locked string unchanged. |
