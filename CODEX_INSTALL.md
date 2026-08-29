# Install Static Graphic Design Creator in Codex

## Purpose

This is the canonical assisted-install contract for the public repository:

`https://github.com/FrameCoreWorks/static-graphic-design-creator`

Install only the standalone `static-graphic-design-creator` Skill from the release-pinned source manifest. This is not a plugin, workspace kit, agent roster, connector, marketplace item, MCP server, or automatic update mechanism.

## Source of truth

Read `config/chatgpt-skill-sources.json`, confirm stable release `v0.6.1`, and use the entry named `static-graphic-design-creator`. The canonical source directory is:

`.agents/skills/static-graphic-design-creator`

Read every listed file before installation and verify its SHA-256 against the manifest. Retrieve each file through `repository_path` or `raw_url`, then preserve its relative bundle `path` inside the installed Skill. If any source differs, stop, reread a fresh manifest, and restart the complete source check. Preserve the directory structure, source name, `SKILL.md`, UI metadata, references, and templates.

## Install boundary

- Install one personal skill available as `$static-graphic-design-creator`.
- Do not clone the full repository into the user's project or copy unrelated repository files.
- Do not create a plugin or install apps, connectors, MCP servers, API keys, paid tools, uploads, publishing, or background tasks. Do not generate an image during installation.
- If the declared source cannot be read or installation fails, report the failed operation and stop. Do not claim success without a real installed-skill result.

## Update behavior

If the skill already exists, follow `CODEX_UPDATE.md`: compare the recorded source identity and manifest delta, show `Delta`, and ask before replacing it. A later repository update is not applied automatically.
