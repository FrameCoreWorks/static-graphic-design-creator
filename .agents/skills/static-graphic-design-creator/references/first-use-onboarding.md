# First-use onboarding

Explain the Skill's optional interaction paths once so a new user can choose a comfortable way to work. This orientation supports both ChatGPT Work and Codex, using only capabilities actually present in the current host.

## Language and localization

The maintained documentation and catalog descriptions are English source material, not an instruction to answer every user in English. The same localization rules apply in ChatGPT Work and Codex:

1. Follow the user's explicit conversation-language preference. A requested language for one prompt or artifact applies to that output, not automatically to the surrounding conversation.
2. Otherwise use the language of the user's own current prose, supported by recent conversation context. Ignore quoted examples, pasted setup prompts, source documents and English code names as language overrides. A clear conversational language switch changes subsequent explanations without restarting onboarding.
3. If conversational evidence is absent, use a reliable user/interface locale only when the active host actually exposes it. Do not inspect unrelated settings or infer nationality, language or preference from a name, location, repository, operating system or the name ChatGPT Work/Codex. Do not claim to have read hidden account settings.
4. If no usable signal exists, start in English and adapt to the next clear signal. A bare `/codes` or an equally mixed message retains the established language; no compulsory language-selection question is needed.

Explain onboarding and the catalog in that language, including languages beyond English and Polish. Translate descriptions and explanatory category headings from the English catalog at response time without omitting entries or inventing additional style rules. Keep canonical code strings, English code names, IDs, category numbers and `/rebuild` unchanged so lookup remains exact. Do not translate locked artwork text, names, dates, URLs or other factual strings unless the user authorizes that change. Follow a separately requested prompt language; source-document language does not set onboarding language. Canonical files are never rewritten for a user's locale.

Present `/codes` as the universal catalog command. During Polish onboarding, also explain that `/kody` (or `kody`) opens the same catalog. `codes` is also accepted without the slash. In other languages, explain `/codes` in the user's language; recognize an unambiguous local request to list the catalog. A local conversational alias may be introduced when its meaning is clear, and retained within the active conversation. Normalize that request to `/codes` before calling the helper; do not claim that aliases are registered global commands or persist between sessions. A local catalog alias never translates or creates individual style codes. If a slash request could mean a style or another action, clarify that ambiguity rather than silently selecting a code. The spelling of a catalog command does not override a language preference.

## Timing and scope

- Show a compact introduction when the user asks for onboarding, states this is their first use, or the host supplies a reliable first-use signal. An installer may show it after a verified new installation if its active workflow supports an introduction. Otherwise use the first explicit invocation after the installation is known to have completed. This Skill cannot guarantee that an installation itself executes its instructions.
- Follow explicit activation. Discussing installation does not start design or rendering. Do not initiate onboarding as a background action or use it to invoke other Skills.
- Reuse evidence that onboarding was already shown or skipped in this conversation or an actually available host state. Do not invent a durable flag, alter the Skill to record a user's visit, or assume a new chat is a new installation. If first-use status is unknown, continue the requested work without a recurring welcome questionnaire.
- Honor "skip onboarding", "only the prompt" and an existing preference not to see codes. For hidden-code users, explain the ordinary brief and uploaded-image routes without displaying command labels; provide command details later only if requested. A direct request to learn the commands permits showing them for that explanation.
- Keep the introduction separate from the design intake. Do not require a code, mode selection, catalog browsing, sample upload or acknowledgment. If the user already supplied a brief, continue it immediately. If no task was supplied, ask one natural question about what they want to create or improve.
- Keep command names inline when explaining them. If giving a complete example request to copy, put each standalone request in its own fenced `text` block; include the Skill invocation and intended output. Use no more than three such examples in the introduction.

## Required content

Explain these points in the user's language, using ordinary vocabulary:

1. **Optional shortcuts.** A normal conversation is sufficient. The user can choose a code, let the Skill select a fitting direction internally, or explicitly disable catalog use. Ordinary brief-based prompts express concrete design instructions without showing identifiers.
2. **Activation and catalog.** Explicitly invoke `static-graphic-design-creator` first, using the host's actual Skill selector or an unambiguous instruction such as "Use static-graphic-design-creator". Then `/codes` returns the full 200-entry catalog in 20 categories with individual descriptions. Explain the relevant local alias according to the language rules above. A category or a need can narrow the list. These are conversational shortcuts interpreted within this Skill, not registered global chat commands or guaranteed native generator controls.
3. **New design or prompt.** Copy an actual listed short code such as `/Two Ink Collision` into a brief and specify whether the desired result is a prompt or a graphic. The Skill translates the direction into layout, hierarchy, typography, colour and material choices. A new design requires no existing poster.
4. **Improve an existing poster.** Attach an available poster in the current host, including one generated earlier, then select a complete catalog line such as `/Two Ink Collision /rebuild` and state the permitted change. In Codex, an accessible local image path may supply the reference. Inspect the actual image before editing. A broad requested redesign may change layout, composition and style while preserving exact factual text and protected assets. "Change only the background" or another narrow instruction limits the edit. A slash label alone neither uploads an image nor authorizes generation.
5. **Work without codes.** The user may describe the objective, audience, content, format and desired changes in ordinary language. Develop the concept together through brief clarification or brainstorming when useful, then produce the requested complete prompt or authorized image. Do not force brainstorm variants onto a resolved concept or replace approved copy. Explain that automatic internal catalog selection is optional and can be disabled explicitly.

The source PDF is not attached to the Skill and is not required from the user. Use the installed structured catalog. In ChatGPT Work and Codex, actual image reading/generation availability and existing execution gates still apply; never promise that an image has been edited merely because the code was accepted.

## Compact source introduction

Use this English source as an adaptable example, not a mandatory script. Localize it before delivery, include the relevant alias and keep its capabilities accurate for the active host:

> You can work with me through a normal brief and conversation. Style codes are optional.
>
> After invoking this Skill, enter `/codes` to explore 200 directions in 20 categories with descriptions. You can also ask for a category or directions that fit your task.
>
> For a new design, add a chosen code such as `/Two Ink Collision` to your brief and say whether you want a prompt or a graphic.
>
> You can also supply an existing poster, including one generated earlier, choose a complete code such as `/Two Ink Collision /rebuild`, and describe what may change. We can revise the layout, hierarchy or style while preserving factual text and protected elements. A request to "change only the background" limits the edit to the background.
>
> We can also develop the brief, brainstorm and refine the design without codes. I can choose a direction internally and deliver a prompt without identifiers. If you want no catalog use even internally, say so.

After the introduction, continue the supplied task. Ask what the user wants to create or improve only when no task has been provided. Do not display the entire catalog until requested.

## Verification cases

- A new user requests onboarding with no brief: explain all five routes and ask one ordinary task question, with no render or compulsory code choice.
- A known first-use message already includes a resolved brief: introduce briefly, then complete the requested scope without repeating supplied questions.
- A returning user, unknown first-use status, or skipped onboarding: no repeated introduction.
- A hidden-code user asks to improve a poster: explain ordinary brief/reference handling without exposing identifiers; keep factual and edit locks.
- A Codex user supplies an actual local image: use the available image-reading path and observed tools; do not invent an upload widget or a native slash-command API.
- Polish onboarding explains `/codes` and `/kody`; English onboarding leads with `/codes` without a Polish-language detour. A Spanish or Japanese request receives onboarding in that language from the same English source.
- A language preference overrides the UI locale or a pasted setup prompt. With no conversation evidence, use an actually available locale, or English when none is exposed; never invent a detected setting.
- A user changes conversation language while asking for an English prompt containing locked text in another language: change explanations only, preserve the requested prompt language and exact text, and do not restart onboarding.
