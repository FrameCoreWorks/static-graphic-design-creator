# Static Design Prompt Architect

**Static Design Prompt Architect** is an installable skill for ChatGPT and Codex. It turns a creative brief into a complete, controlled prompt for designed static graphics: posters, flyers, business cards, menus, book covers, labels, key visuals, advertisements, and text-led social graphics.

Install it when you want ChatGPT or Codex to prepare generator-ready visual prompts with a deliberate communication goal, attention order, layout, exact visible copy, reference roles, exclusions, and QA. It is not an image generator or a DTP tool: it authors the prompt and marks generator-sensitive limits as `Unknown` when they are not verified.

By default, the skill creates one standalone, provider-neutral prompt. Its eight stages describe construction priority inside a single final generation; they do not request intermediate renders, separate layer files, or later text insertion.

## What it does

- converts a short brief or a structured workflow handoff into a generator-ready static-design prompt;
- protects exact visible copy, attention order, layout zones, references, and exclusions;
- separates verified native controls from prompt-semantic controls and post-render QA;
- supports standalone use and optional integration with an existing workflow;
- treats font fidelity and dense raster text as QA risks rather than guarantees.

## Repository structure

```text
.
├── .agents/plugins/marketplace.json
├── plugins/static-design-prompt-architect/
│   ├── .codex-plugin/plugin.json
│   └── skills/static-design-prompt-architect/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       └── templates/
├── tests/test_package.py
├── LICENSE
└── README.md
```

## Install

### ChatGPT Work

The distributable skill is in `plugins/static-design-prompt-architect/skills/static-design-prompt-architect/`. Package that folder as a ZIP with `static-design-prompt-architect/` as its single top-level directory, then upload it in **Plugins → Skills → Create → Upload**. After the scan, invoke it explicitly with `@static-design-prompt-architect` or let the host match its description.

For workspace-wide ChatGPT Work availability, distribute the included plugin through a compatible workspace plugin route. A local repository or ZIP does not itself publish a plugin, and availability depends on the workspace permissions and plan. See the official [Build skills guide](https://learn.chatgpt.com/docs/build-skills) and [Skills in ChatGPT guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

### Codex

For repository-scoped use, copy `plugins/static-design-prompt-architect/skills/static-design-prompt-architect/` to `.agents/skills/static-design-prompt-architect/` in the target project.

For plugin installation, clone this repository, register its marketplace root, then install the plugin according to your local Codex setup. The included marketplace entry resolves `./plugins/static-design-prompt-architect`; no connector, API key, network call, or paid service is required.

## Use modes

**Standalone mode** accepts an ordinary brief. Missing generator-sensitive controls remain `Unknown`; the skill does not invent support for model versions, font files, reference limits, or output settings.

**Connected mode** accepts supplied workflow fields such as `brief_contract`, `direction_contract`, `copy_pack`, `reference_pack`, `asset_manifest`, `qa_requirements`, and `target_generator_profile`. It preserves supplied locks and returns a portable `prompt_pack` for the caller's existing workflow. It never requires a particular upstream skill by name.

## Validate

```bash
python3 tests/test_package.py
```

The test verifies the package structure, manifest contract, portable workflow boundary, and required eight-stage static-design contract. It performs no network activity.

## Scope and limits

This package authors prompts; it does not generate graphics, call external services, select paid tools, upload assets, publish a plugin, or perform DTP. For print production, use the rendered output as art direction and verify exact copy, legal text, font licensing, spacing, bleed, and prepress requirements in an appropriate layout tool.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE).
