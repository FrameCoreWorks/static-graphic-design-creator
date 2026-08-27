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
├── submission/openai-plugin-directory.md
├── tests/test_package.py
├── LICENSE
└── README.md
```

## Install without downloading a ZIP

### Codex: install from this GitHub repository

This is the direct GitHub route. It does not require `git clone`, a downloaded ZIP, or copying files into a project.

1. Paste this command into a terminal with Codex installed:

   ```bash
   codex plugin marketplace add FrameCoreWorks/static-design-prompt-architect --ref main
   ```

2. Start Codex and enter `/plugins`.
3. Open the **Static Design Prompt Architect** marketplace, select **Static Design Prompt Architect**, then choose **Install plugin**.
4. Start a new Codex session. Invoke it with `$static-design-prompt-architect` or describe a static-design prompt task normally.

Codex fetches and tracks the marketplace from GitHub. To refresh it later, run:

```bash
codex plugin marketplace upgrade static-design-prompt-architect
```

### ChatGPT Work: install from the public Plugins Directory

ChatGPT Work does not install a public GitHub repository directly from a pasted URL. The supported no-download route is a public listing in the universal Plugins Directory shared by ChatGPT and Codex. Once this plugin is approved and published there, users install it without a ZIP or manual file transfer:

1. In ChatGPT, open **Plugins**.
2. Search for **Static Design Prompt Architect**.
3. Open the listing and select **Install plugin**.
4. Start a new Work chat. Invoke `@static-design-prompt-architect` or describe the prompt task directly.

The source package in this repository is ready for that submission flow. Publication status is **not yet submitted**: OpenAI requires a verified publisher identity, public listing URLs, a production logo, the final skill bundle, test cases, and review approval. The owner-facing checklist and ready-to-use test cases are in [submission/openai-plugin-directory.md](submission/openai-plugin-directory.md).

For the supported host behavior, see the official [plugin packaging guide](https://developers.openai.com/plugins/build/plugins), [Plugins guide](https://learn.chatgpt.com/docs/plugins), and [public submission guide](https://developers.openai.com/plugins/deploy/submission).

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
