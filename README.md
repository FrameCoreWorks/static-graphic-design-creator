![FrameCore Works banner for Static Graphic Design Creator](assets/static-graphic-design-creator-banner.webp)

# Static Graphic Design Creator

**Static Graphic Design Creator is a standalone native Skill source for ChatGPT Work and Codex.** It helps turn a brief into either a finished static graphic, when rendering is explicitly requested, or one controlled, generator-ready prompt for posters, flyers, business cards, menus, covers, labels, key visuals, advertisements, and text-led social graphics.

It behaves like a graphic designer, not a style-prompt dispenser: objective and audience response come first; then visual thesis, hierarchy, composition, type/image roles, style language, and material treatment. The final prompt integrates eight semantic construction stages inside a single generation; simple prompts and narrow edits stay concise. It is not a request for separate renders, blank text zones, or manual layer assembly.

## Install from this repository

### ChatGPT Work

Native Skills must be available in the active account and workspace. Work access alone does not guarantee that Skills or `@skill-creator` are available. If the Skills surface is absent, use an eligible workspace or Codex instead; do not simulate a successful installation. OpenAI lists Skills for eligible Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and product availability. [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

In a Work conversation with `@skill-creator` available, paste:

```text
Use @skill-creator to create and save one native ChatGPT Skill from this public repository:
https://github.com/FrameCoreWorks/static-graphic-design-creator

First read and follow CHATGPT_INSTALL.md from this repository. Use its release manifest as bootstrap discovery only: resolve the declared immutable source commit, fetch every declared Skill file only from that commit, and verify every declared SHA-256 when this host supports it.

Create only `static-graphic-design-creator`. Keep the short onboarding and obtain any installation approval not already given. After approval and source resolution, immediately use the active native Skill save flow. Verify the complete saved inventory and source record, record any required host adaptations, and check that comparison against the same release requires no further source update. Report `installed` only after a real save and result verification; a visible entry alone is insufficient. If hashing is unavailable, report `declared_unverified`; never call it verified. Do not create a duplicate Skill.
```

The only external address in the setup is this repository. The contract preserves each declared bundle path, asks for approval before creation, and treats source resolution as preparation rather than installation. It reports a concrete host failure if the native save action cannot run.

### Codex

Codex uses its built-in `$skill-installer` for a fresh third-party Skill install. In a Codex chat, paste:

```text
Use $skill-installer to install the standalone Skill from this public repository:
https://github.com/FrameCoreWorks/static-graphic-design-creator

First read CODEX_INSTALL.md. Resolve the current release manifest, then use its immutable source commit and declared source path to install only `static-graphic-design-creator`. Verify every declared SHA-256 before installation. Do not clone the repository into my project and do not install unrelated files.
```

The installer resolves the public GitHub source and installs the declared directory as `$static-graphic-design-creator`. No ZIP, local clone, or manual file copy is required.

## Update an installed Skill

Updates are manual, compare-only first, and require approval before replacement. They never run in the background or create a second copy.

### ChatGPT Work update

```text
Use @skill-creator to update the existing native ChatGPT Skill from this public repository:
https://github.com/FrameCoreWorks/static-graphic-design-creator

First read CHATGPT_UPDATE.md. Compare the verified previous source, current immutable release and actual installed files. Report installed and available version, changed/new/removed/unchanged files, already-target files, local modifications, verification status, and proposed apply mode. If exact and unchanged, return `already_up_to_date`; preserve personal-only differences as `local_customizations_preserved`. Prepare exact conflict diffs and a complete proposed merge during the read-only comparison without asking permission to analyze. Show the resolved Delta and obtain my approval before any installed-file write. Apply the approved source changes, safe removals and source record together, preserve unrelated local files, verify the actual saved result and repeat comparison to confirm no further update is needed. Update the existing Skill only. Never create a duplicate.
```

### Codex update

```text
Use $skill-creator to update the existing personal Skill from this public repository:
https://github.com/FrameCoreWorks/static-graphic-design-creator

First read CODEX_UPDATE.md. Compare the verified previous source, current immutable release and actual installed files. Prepare exact conflict diffs and a complete proposed merge read-only, without asking permission to analyze. Report the resolved Delta, already-target files, retained personal changes and verification before any write, then obtain my approval. Apply source changes, safe removals and the source record together; verify the saved result and repeat comparison. Update only the existing `$static-graphic-design-creator`; do not overwrite an unresolved conflict, create a duplicate, use a forced fresh install, or clone the repository into my project.
```

## Extend your own installed copy

Use this route when you have ideas for adapting the installed Skill to your own workflow. It is a guided **personal extension**, not a fresh installation or a source-release update. It changes only the existing personal Skill after approval; it never creates a duplicate or changes this public repository. A later source update will still identify any locally changed files and ask for a conflict-safe decision.

Prefer the optional `local/SKILL_EXTENSIONS.md` entry and related `local/` resources for personal behavior; this namespace is reserved and never published in the source bundle. The Skill reads that entry when present after explicit activation. Existing embedded extensions require a reviewed migration; if a canonical file must change, keep it as a recorded personal override rather than pretending it is upstream. The upstream release record stays unchanged during personal extension. See [maintenance and customization](.agents/skills/static-graphic-design-creator/references/skill-maintenance.md).

### ChatGPT Work personal extension

In a Work conversation where both Skills are available, paste:

```text
Use @static-graphic-design-creator together with @skill-creator to help me extend my existing personal native ChatGPT Skill: `static-graphic-design-creator`.

This is a guided personal extension, not a fresh installation, source-release update, repository edit, connector, or duplicate-Skill creation.

First inspect the existing Skill and its directly relevant files. Then begin a short discovery conversation: ask me what I want to add, change, improve, or make more specific to my workflow. Ask only the questions needed to establish the intended behavior, real examples, preserved behavior, boundaries, and any required references or templates.

Before changing anything, return a concise Change Proposal with: evidence or use case; objective; exact files and scope; expected benefit; risks or conflicts; acceptance test; rollback; and a clear stop condition. Wait for my explicit approval.

Prefer `local/SKILL_EXTENSIONS.md` and supporting local resources if this installed version supports that entry. If it does not, include the minimal explicit loading instruction in the proposed patch rather than silently assuming it is supported. Explain and record any unavoidable canonical-file override. After approval, update only the existing `static-graphic-design-creator`, preserve unrelated behavior and the upstream source-release record, validate and save through the active native Skill workflow, and verify every intended saved change and preserved file. Do not create a second Skill or claim that personal changes came from a public release.
```


### Codex personal extension

In a Codex chat where both Skills are available, paste:

```text
Use $static-graphic-design-creator together with $skill-creator to help me extend my existing personal Codex Skill: `static-graphic-design-creator`.

This is a guided personal extension, not a fresh installation, public source-release update, repository edit, plugin, connector, or duplicate-Skill creation.

First inspect the existing installed Skill and its directly relevant files. Then begin a short discovery conversation: ask me what I want to add, change, improve, or make more specific to my workflow. Ask only the questions needed to establish the intended behavior, real examples, preserved behavior, boundaries, and any required references or templates.

Before changing anything, return a concise Change Proposal with: evidence or use case; objective; exact files and scope; expected benefit; risks or conflicts; acceptance test; rollback; and a clear stop condition. Wait for my explicit approval.

Prefer `local/SKILL_EXTENSIONS.md` and supporting local resources if this installed version supports that entry. If it does not, include the minimal explicit loading instruction in the proposed patch rather than silently assuming it is supported. Explain and record any unavoidable canonical-file override. After approval, update only the existing installed Skill in Codex, preserve unrelated behavior and its upstream source-release record, validate and use the actual save workflow, then verify every intended saved change and preserved file. Do not create a second Skill directory, clone the public repository into my project, or claim that personal changes came from a public release.
```

## Activation

Invoke `@static-graphic-design-creator` in ChatGPT Work or `$static-graphic-design-creator` in Codex, or explicitly ask to run the Skill. Codex implicit invocation is disabled. Casual design advice, a quoted Skill name, and a request to maintain its files do not start graphic production. Ideas-only and copy-only requests remain in that scope. A genuine continuation preserves selected concepts and exact copy.

## Optional design codes and first use

The Skill includes **200 poster directions in 20 categories**. After invoking it, use **`/codes`** to see the complete grouped catalog with descriptions. Ask for a category or describe a need to narrow the results. This is a conversational shortcut interpreted by this Skill, not a global application command or native generator setting.

Documentation and catalog descriptions are maintained in English. The Skill uses your conversation language for onboarding, brief questions and catalog explanations, and introduces relevant local aliases during onboarding. It follows an explicit language preference first, then conversation context, using a reliable host locale only when available. The requested prompt language and exact artwork text remain separate. English code names stay unchanged across languages.

For a new user, the installer or a known first-use invocation explains catalog discovery, new prompts, uploaded-poster improvement and ordinary brief/brainstorm collaboration. The introduction can be skipped and does not require a code choice or acknowledgment. An installation does not necessarily execute the Skill, and an unknown first-use status does not justify a recurring welcome. See the [first-use workflow](.agents/skills/static-graphic-design-creator/references/first-use-onboarding.md).

### Browse directions

```text
Use static-graphic-design-creator. /codes
Show the complete grouped catalog with descriptions in English. Do not generate an image.
```

### Create a new prompt with a chosen direction

```text
Use static-graphic-design-creator. Create only a complete English prompt for a square digital graphic using /Two Ink Collision. My approved concept is that the word itself forms the image, with generous surrounding space. The sole final text is CZYTAJ. Use navy and orange simulated inks on cream paper with a controlled local overprint. Do not generate an image.
```

### Rework an existing poster

Attach the actual image in ChatGPT Work, or attach it or provide an accessible local image path in Codex. Previously generated posters can be used when their actual image is available in the active context.

```text
Use static-graphic-design-creator. Inspect the attached poster and prepare only a complete redesign prompt using /Two Ink Collision /rebuild. Rework the layout, hierarchy and colour treatment while preserving all factual text, dates, prices and protected logos exactly. Keep the existing core concept. Flag unreadable required text before finalizing. Do not generate an image yet.
```

A requested full redesign may change layout, typography and material treatment. A narrower instruction such as "change only the background" limits the edit. Selecting a code does not supply an image, change source facts or authorize rendering.

### Work entirely through a brief

```text
Use static-graphic-design-creator. Prepare only a complete English prompt for a square digital graphic. My approved concept is a single dominant word with ample negative space, and my exact final text is CZYTAJ. I want two matte inks, navy and orange, on cream paper with restrained overprinting. Choose the detailed visual treatment from this brief. Do not show code names or labels, and do not generate an image.
```

Codes are optional. With an open visual direction, the Skill may choose a fitting entry internally and compile its visible meaning into the prompt. It does not announce the identifier or force a catalog onto the user. Say "Do not use the catalog, even internally" to opt out completely. If no entry fits, the Skill designs directly from the brief. A user-selected code is retained as instruction-only prompt metadata unless the user asks to hide it. Hidden-code prompts and the corresponding submitted generation prompts contain the same expanded design instructions, preserving later exact-prompt delivery.

The standalone JSON catalog preserves code names and categories from *200 Event Poster Design Codes* by **John Savage AI**. Detailed descriptions and workflow interpretations are by **FrameCore Works**. The original PDF is not attached, installed or required at runtime. Names alone do not guarantee an identical result across generators. See the [catalog workflow](.agents/skills/static-graphic-design-creator/references/event-poster-code-workflow.md).

## What the Skill does

- accepts both a short standalone brief and a structured workflow handoff;
- supports `prompt`, `render`, and `render_and_prompt` modes without rendering from an ambiguous brief;
- develops materially different, paired concept/copy routes for open direction and preserves a supplied concept lock for directed work;
- develops anti-generic poster copy through one internal copy-development-and-human-voice layer when wording is absent or needs refinement, then locks the selected text before visual prompting or rendering;
- uses a poster-movements atlas, style translation catalog, production walkthroughs, and QA routes without turning them into a preset menu;
- protects per-item exact copy and reference properties, including product/garment construction, continuous label boundaries and logo geometry;
- supports type-only minimalism, deliberate hybrids and format-specific commercial, menu, packaging and social decisions;
- offers optional manual or internal poster-code selection, complete catalog browsing localized to the user and first-use guidance for existing-image redesign;
- evaluates actual text burden and required metadata separately from wording selection, with Polish/multilingual checks and explicit digital-versus-production limits;
- fails acceptance on one critical defect and chooses the smallest supported repair, checking texture/gradient and identity drift without automatic rerenders;
- treats named-font fidelity, dense raster type, print-ready deliverables, and prepress as external QA or DTP requirements rather than promises.

The bundle contains worked examples of a discovery brainstorm, a directed Codex compatibility profile, a scoped edit, and a full rerender decision. They are decision models, not generic artwork recipes.

## Integrity model

The release manifest is a **bootstrap document**. It resolves every declared Skill source through one immutable Git commit and lists its SHA-256 value. A matching hash verifies the retrieved bytes against that manifest and catches transfer corruption or manifest/file drift.

When the host cannot calculate SHA-256, installation may continue only with `hash_verification: declared_unverified`. That is an explicit lower-trust state, not a verified install. The mechanism does not independently authenticate a compromised repository bootstrap. See [SECURITY.md](SECURITY.md) for the boundary and the release model.

## Validation and release gates

```bash
python3 -m pip install -r tests/requirements.txt
python3 -B tests/test_skill.py
python3 -B tests/test_design_contracts.py
python3 -B -m unittest discover -s tests -p 'test_lifecycle.py'
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s .agents/skills/static-graphic-design-creator/tests -p 'test_event_poster_codes.py'
python3 tests/check_source_anchors.py --check-inventory
```

The deterministic suite checks exact source inventory and Git/SHA-256 locks, three-way update decisions, duplicate YAML/JSON keys, links, canonical handoff states and protected transitions. Catalog tests verify all 200 exact code lines, category/page mappings, English source descriptions and read-only lookup behavior without the PDF. Both actual templates are validated. The offline schema checker supports only the vocabulary used in this repository and rejects unsupported keywords; it is not a general JSON Schema engine. These tests do not prove model behavior, translation quality, headline quality, or visual fidelity.

Lifecycle tests also exercise an install/update/no-op cycle, personal-extension retention across versions, legacy add/add collisions, reviewed merges, safe deletions, stale records, changed inputs and failed-readback detection on disposable files or in-memory proposals. Release tests verify generated locks and reject mismatched public refs, file bytes, inventories and CI responses using controlled fixtures. Live host saves and live publication checks remain separate evidence. Maintainers use [the release procedure](CONTRIBUTING.md#candidate-lock) to derive manifests from the actual source commit and verify the published result.

Use `python3 -B tests/test_skill.py --working-tree` during editing to check the previous pinned baseline and draft structure. Only default mode certifies the local source lock. Reference-anchor reachability is checked separately; rate limits and authentication barriers are `Unknown`, never passing evidence of the historical claims themselves.

Before a stable release, run every applicable case in [EVALUATION.md](EVALUATION.md) in actual ChatGPT Work and Codex sessions and record evidence under [reports/host-evaluations](reports/host-evaluations). Pending cases remain pending. A local source commit and passing structural checks do not establish remote availability, native installation, or visual performance.

OpenAI-surface assumptions were reviewed against official documentation on **2026-09-07**. The active host's exposed tools and settings determine what can actually execute; API documentation alone does not prove a ChatGPT or Codex control is available.

## Repository layout

```text
.
├── .agents/skills/static-graphic-design-creator/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   ├── scripts/
│   │   ├── event_poster_codes.py
│   │   └── skill_lifecycle.py
│   ├── templates/
│   └── tests/test_event_poster_codes.py
├── assets/
├── config/
├── reports/host-evaluations/
├── scripts/release.py
├── tests/
├── CHATGPT_INSTALL.md
├── CHATGPT_UPDATE.md
├── CODEX_INSTALL.md
├── CODEX_UPDATE.md
├── EVALUATION.md
├── SECURITY.md
└── README.md
```

## Scope and limits

This Skill uses only the active surface's native image generation and only after the user explicitly requests a render. It does not select external providers, use API keys, upload assets, publish work, or perform DTP. A `production_master` always routes to a suitable layout workflow for exact type, licensing, bleed, editable vectors, and prepress.

## License

Repository code and authored documentation are released under the Apache License 2.0. See [LICENSE](LICENSE). The imported catalog retains attribution to John Savage AI for its source names and grouping; the source PDF is not redistributed. The English source interpretations are FrameCore Works' additions and are localized for users during conversation.

Release discovery uses `main` only to locate the current manifest. Pin the manifest's own Git commit before retrieval and record it with the installation evidence. [Release history](config/release-history.json) supplies verified immutable baseline locators when an old installation has no receipt. Historical `v0.7.0-rc.2` and `v0.7.0-rc.3` branches contain an earlier manifest; use their matching immutable lock from the index after verifying its digest, identity and source files. The historical branches are not moved. An unresolvable release mismatch still blocks comparison rather than silently using another baseline.
