# Update Static Graphic Design Creator in Codex

## Purpose

This is the canonical update contract for the existing personal Codex Skill from:

`https://github.com/FrameCoreWorks/static-graphic-design-creator`

Use `$skill-installer` to perform this user-initiated update when that built-in Skill is available. This is a standalone Skill update, not a plugin, automatic repository sync, background task, connector, MCP server, or project-repository clone.

## Source and identity

Read the latest stable `config/chatgpt-skill-sources.json`, the target `references/source-release.json`, and every declared source file. Read the installed Skill's `references/source-release.json` before changing it.

The installed record must identify the same repository and `static-graphic-design-creator`. Its version and ref identify the previous source manifest used for file-level comparison. If it is absent, report `source_identity: unrecorded` and obtain an explicit confirmation that this matching installed Skill originated from this repository before treating it as an update target. If it identifies a different repository or Skill, stop with `blocked_source_identity`.

## Update procedure

1. Resolve the previous and target release-pinned manifests.
2. Verify each target source file against the target SHA-256 when the current environment can calculate it.
3. Compare installed files against the previous manifest and then the target manifest. Report changed, new, removed, unchanged, and locally modified files.
4. If there is no delta, report `already_up_to_date` and stop.
5. Show `Delta`, installed and available version, verification status, and proposed apply mode. Ask for explicit user approval.
6. After approval, update the existing personal `$static-graphic-design-creator` Skill without creating a duplicate.
7. Verify the saved source-release record and report `updated` only after a real installed-Skill result.

Use `apply_mode: selective_file_update` only when the environment can prove the file-level comparison and there are no local conflicts. If individual file comparison is unavailable, report `comparison_unavailable`; after approval, a full replacement with the exact declared source bundle may be used only as `apply_mode: declared_bundle_replacement`.

Do not overwrite or delete a file that differs from its previous release hash when the target also changes or removes it. Report `blocked_local_conflict` and stop for user direction.

## Boundaries

- Install or update only the declared `static-graphic-design-creator` source bundle.
- Do not clone the repository into a user project, install unrelated files, create a plugin, add apps, connectors, MCP servers, API keys, paid tools, uploads, publishing, or background tasks.
- Do not update automatically when the repository changes. Codex may detect local file changes after an approved update, but repository checking and replacement remain user initiated.
