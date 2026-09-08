# First-use onboarding

Explain the Skill's optional interaction paths once so a new user can choose a comfortable way to work. This orientation supports both ChatGPT Work and Codex, using only capabilities actually present in the current host.

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
2. **Activation and catalog.** Explicitly invoke `static-graphic-design-creator` first, using the host's actual Skill selector or an unambiguous instruction such as "Use static-graphic-design-creator". Then `/kody`, `kody`, `/codes` or `codes` returns the full 200-entry catalog in 20 categories with individual descriptions. A category or a need can narrow the list. These are conversational shortcuts interpreted within this Skill, not registered global chat commands or guaranteed native generator controls.
3. **New design or prompt.** Copy an actual listed short code such as `/Two Ink Collision` into a brief and specify whether the desired result is a prompt or a graphic. The Skill translates the direction into layout, hierarchy, typography, colour and material choices. A new design requires no existing poster.
4. **Improve an existing poster.** Attach an available poster in the current host, including one generated earlier, then select a complete catalog line such as `/Two Ink Collision /rebuild` and state the permitted change. In Codex, an accessible local image path may supply the reference. Inspect the actual image before editing. A broad requested redesign may change layout, composition and style while preserving exact factual text and protected assets. "Change only the background" or another narrow instruction limits the edit. A slash label alone neither uploads an image nor authorizes generation.
5. **Work without codes.** The user may describe the objective, audience, content, format and desired changes in ordinary language. Develop the concept together through brief clarification or brainstorming when useful, then produce the requested complete prompt or authorized image. Do not force brainstorm variants onto a resolved concept or replace approved copy. Explain that automatic internal catalog selection is optional and can be disabled explicitly.

The source PDF is not attached to the Skill and is not required from the user. Use the installed structured catalog. In ChatGPT Work and Codex, actual image reading/generation availability and existing execution gates still apply; never promise that an image has been edited merely because the code was accepted.

## Compact Polish introduction

Use this as an adaptable example, not a mandatory script. Keep its capabilities accurate for the active host; translate it for other conversation languages:

> Możesz pracować ze mną przez zwykły brief i rozmowę. Kody stylów są opcjonalne.
>
> Po wywołaniu tego Skilla wpisz `/kody`, `kody`, `/codes` lub `codes`, aby zobaczyć 200 kierunków w 20 kategoriach wraz z opisami. Możesz też poprosić o konkretną kategorię lub kierunek pasujący do zadania.
>
> Przy nowym projekcie dodaj do briefa wybrany kod, np. `/Two Ink Collision`, i określ, czy chcesz prompt, czy grafikę.
>
> Możesz też wgrać gotowy plakat, również wcześniej wygenerowany, wybrać z listy pełny kod, np. `/Two Ink Collision /rebuild`, i opisać zakres przebudowy. Zmienimy układ, hierarchię lub styl w wybranym kierunku, zachowując treść i wskazane elementy. Polecenie „zmień tylko tło” ogranicza edycję do tła.
>
> Bez kodów również możemy przejść przez brief, brainstorming i poprawki. Mogę dobrać kierunek w tle i podać prompt bez oznaczeń. Jeśli nie chcesz korzystania z katalogu nawet wewnętrznie, wystarczy to powiedzieć.

After the introduction, continue the supplied task. Ask what the user wants to create or improve only when no task has been provided. Do not display the entire catalog until requested.

## Verification cases

- A new user requests onboarding with no brief: explain all five routes and ask one ordinary task question, with no render or compulsory code choice.
- A known first-use message already includes a resolved brief: introduce briefly, then complete the requested scope without repeating supplied questions.
- A returning user, unknown first-use status, or skipped onboarding: no repeated introduction.
- A hidden-code user asks to improve a poster: explain ordinary brief/reference handling without exposing identifiers; keep factual and edit locks.
- A Codex user supplies an actual local image: use the available image-reading path and observed tools; do not invent an upload widget or a native slash-command API.
