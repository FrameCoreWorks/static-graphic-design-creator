# Install Static Design Prompt Architect in Codex

## Purpose

This is the canonical assisted-install contract for the public repository:

`https://github.com/FrameCoreWorks/static-design-prompt-architect`

Install only the standalone `static-design-prompt-architect` Skill from the declared source manifest. This is not a plugin, workspace kit, agent roster, connector, marketplace item, or MCP server.

## Source of truth

Read `config/chatgpt-skill-sources.json` and use the entry named `static-design-prompt-architect`. The canonical source directory is:

`.agents/skills/static-design-prompt-architect`

Read every listed file before installation. Preserve the directory structure, source name, `SKILL.md`, UI metadata, references, and templates.

## Install boundary

- Install one personal skill available as `$static-design-prompt-architect`.
- Do not clone the full repository into the user's project or copy unrelated repository files.
- Do not create a plugin or install apps, connectors, MCP servers, API keys, paid tools, uploads, publishing, image-generation actions, or background tasks.
- If the declared source cannot be read or installation fails, report the failed operation and stop. Do not claim success without a real installed-skill result.

## Update behavior

If the skill already exists, compare it with the manifest source and ask before replacing it. A later repository update is not applied automatically.
