# Static Design Prompt Architect

**Static Design Prompt Architect is an installable standalone Skill for ChatGPT Work and Codex.** It turns a creative brief into one complete, controlled prompt for static graphics: posters, flyers, business cards, menus, book covers, labels, key visuals, advertisements, and text-led social graphics.

Use this public repository as the source address. ChatGPT Work or Codex can read the declared source files and install the one skill without downloading a ZIP, cloning the repository, or using a plugin.

It is not an image generator or a DTP tool. It authors the prompt and marks generator-sensitive limits as `Unknown` when they are not verified.

## Install from this repository

### ChatGPT Work

1. Open a ChatGPT conversation and switch from **Chat** to **Work**.
2. Paste the prompt below. The repository URL is the only source address; `@skill-creator` selects the native Skill-creation flow.

```text
Use @skill-creator to create and install the standalone Skill from this public repository:
https://github.com/FrameCoreWorks/static-design-prompt-architect

First read and follow CHATGPT_INSTALL.md in that repository. Create only the declared `static-design-prompt-architect` Skill from the checked source manifest. This is a Skill, not a plugin.
```

ChatGPT Work reads the exact file list from `config/chatgpt-skill-sources.json`, then creates one native personal Skill. Approve creation in the conversation when asked. The Skill can then be used as `@static-design-prompt-architect` or by asking normally for a controlled prompt for a static graphic.

### Codex

In a Codex chat, paste:

```text
Install the standalone Skill from this public repository:
https://github.com/FrameCoreWorks/static-design-prompt-architect

Read CODEX_INSTALL.md and install only the declared `static-design-prompt-architect` Skill. Do not clone the repository, create a plugin, or install any unrelated workflow files.
```

The Codex install contract resolves the same source manifest and installs the skill as `$static-design-prompt-architect`. No ZIP or manual file copy is required.

## What the Skill does

- converts a short brief or a structured workflow handoff into a generator-ready static-design prompt;
- protects exact visible copy, attention order, layout zones, references, and exclusions;
- separates verified native controls from prompt-semantic controls and post-render QA;
- supports standalone use and optional integration with an existing workflow;
- treats font fidelity and dense raster text as QA risks rather than guarantees.

By default, the Skill creates one standalone, provider-neutral prompt. Its eight stages describe construction priority inside a single final generation; they do not request intermediate renders, separate layer files, or later text insertion.

## Repository layout

```text
.
├── .agents/skills/static-design-prompt-architect/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── templates/
├── config/
│   ├── chatgpt-skills.json
│   └── chatgpt-skill-sources.json
├── CHATGPT_INSTALL.md
├── CODEX_INSTALL.md
├── tests/test_skill.py
├── LICENSE
└── README.md
```

`.agents/skills/` is a source layout for Skills. This repository contains no plugin, connector, marketplace, MCP server, app integration, or external provider integration.

## Use modes

**Standalone mode** accepts an ordinary brief. Missing generator-sensitive controls remain `Unknown`; the Skill does not invent support for model versions, font files, reference limits, or output settings.

**Connected mode** accepts supplied workflow fields such as `brief_contract`, `direction_contract`, `copy_pack`, `reference_pack`, `asset_manifest`, `qa_requirements`, and `target_generator_profile`. It preserves supplied locks and returns a portable `prompt_pack` for the caller's existing workflow. It never requires a particular upstream Skill by name.

## Validate

```bash
python3 tests/test_skill.py
```

The test verifies the standalone Skill structure, its ChatGPT source manifest, portable workflow boundary, and required eight-stage static-design contract. It performs no network activity.

## Scope and limits

This Skill authors prompts; it does not generate graphics, call external services, select paid tools, upload assets, publish content, or perform DTP. For print production, use the rendered output as art direction and verify exact copy, legal text, font licensing, spacing, bleed, and prepress requirements in an appropriate layout tool.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE).
