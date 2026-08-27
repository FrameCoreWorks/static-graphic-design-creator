# Static Design Prompt Architect

**Static Design Prompt Architect** is one standalone skill for ChatGPT and Codex. It turns a creative brief into a complete, controlled prompt for designed static graphics: posters, flyers, business cards, menus, book covers, labels, key visuals, advertisements, and text-led social graphics.

Install it when you want ChatGPT or Codex to prepare generator-ready visual prompts with a deliberate communication goal, attention order, layout, exact visible copy, reference roles, exclusions, and QA. It is not an image generator or a DTP tool: it authors the prompt and marks generator-sensitive limits as `Unknown` when they are not verified.

By default, the skill creates one standalone, provider-neutral prompt. Its eight stages describe construction priority inside a single final generation; they do not request intermediate renders, separate layer files, or later text insertion.

This repository contains no plugin, connector, marketplace, MCP server, or app integration.

## What it does

- converts a short brief or a structured workflow handoff into a generator-ready static-design prompt;
- protects exact visible copy, attention order, layout zones, references, and exclusions;
- separates verified native controls from prompt-semantic controls and post-render QA;
- supports standalone use and optional integration with an existing workflow;
- treats font fidelity and dense raster text as QA risks rather than guarantees.

## Repository structure

```text
.
├── skills/static-design-prompt-architect/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── templates/
├── tests/test_skill.py
├── LICENSE
└── README.md
```

## Install the standalone skill

### Codex: install from the public GitHub skill address

In a Codex chat, paste this one instruction. The built-in skill installer downloads and installs the skill for the current user; no ZIP, manual clone, or file copy is needed.

```text
$skill-installer install https://github.com/FrameCoreWorks/static-design-prompt-architect/tree/main/skills/static-design-prompt-architect
```

The skill is available on the next turn as `$static-design-prompt-architect`. Codex installs it into the user's personal skills location, so it is available across repositories.

### ChatGPT Work: create and install the standalone skill from this source

ChatGPT Work has no native “install standalone skill from a GitHub URL” control. It can create, upload, share, and install individual skills. To avoid a ZIP and manual file transfer, open a Work chat and paste the following assisted-import instruction:

```text
@skill-creator

Create and install one standalone personal skill named `static-design-prompt-architect` from this public GitHub skill directory:
https://github.com/FrameCoreWorks/static-design-prompt-architect/tree/main/skills/static-design-prompt-architect

Read `SKILL.md`, every directly linked file in `references/` and `templates/`, and `agents/openai.yaml`. Preserve the source instructions, trigger conditions, output contract, and safety boundaries. Do not convert it into a plugin and do not add apps, connectors, MCP servers, scripts, paid tools, uploads, publishing, or generation actions. If the source cannot be accessed, say so and stop instead of reconstructing missing files from memory.
```

After the skill is created, use it with `@static-design-prompt-architect` or describe a static-design prompt task normally. The resulting ChatGPT skill is a snapshot: changes in this repository do not update it automatically. Re-run the import instruction or update it in the Skills editor when a newer repository version is released.

For supported skill behavior, see the official [Build skills guide](https://learn.chatgpt.com/docs/build-skills) and [Skills in ChatGPT guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

## Use modes

**Standalone mode** accepts an ordinary brief. Missing generator-sensitive controls remain `Unknown`; the skill does not invent support for model versions, font files, reference limits, or output settings.

**Connected mode** accepts supplied workflow fields such as `brief_contract`, `direction_contract`, `copy_pack`, `reference_pack`, `asset_manifest`, `qa_requirements`, and `target_generator_profile`. It preserves supplied locks and returns a portable `prompt_pack` for the caller's existing workflow. It never requires a particular upstream skill by name.

## Validate

```bash
python3 tests/test_skill.py
```

The test verifies the standalone skill structure, portable workflow boundary, and required eight-stage static-design contract. It performs no network activity.

## Scope and limits

This skill authors prompts; it does not generate graphics, call external services, select paid tools, upload assets, publish content, or perform DTP. For print production, use the rendered output as art direction and verify exact copy, legal text, font licensing, spacing, bleed, and prepress requirements in an appropriate layout tool.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE).
