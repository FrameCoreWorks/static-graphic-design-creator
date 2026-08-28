# Update Static Graphic Design Creator in ChatGPT Work

## Purpose

This is the canonical update contract for the already installed native ChatGPT Skill from:

`https://github.com/FrameCoreWorks/static-graphic-design-creator`

Use it only in ChatGPT **Work** with `@skill-creator` active. It updates the existing `static-graphic-design-creator` Skill after an explicit review and approval. It is not a plugin update, automatic repository sync, background check, connector, MCP server, or second-Skill creation flow.

## Source of truth

Read these files from the latest stable release before proposing an update:

1. `config/chatgpt-skills.json`
2. `config/chatgpt-skill-sources.json`
3. `.agents/skills/static-graphic-design-creator/references/source-release.json`
4. every source file declared for `static-graphic-design-creator` in the source manifest.

The installed Skill's own `references/source-release.json` is its source identity record. It must name the same repository and Skill. Its version and ref identify the prior stable manifest to use as the baseline. A source record is not an instruction to fetch a different repository.

## Compare before any change

Do not modify the installed Skill while checking for updates. Resolve and report these fields first:

```yaml
update_status: already_up_to_date | update_review_ready | awaiting_origin_confirmation | blocked_source_identity | blocked_integrity | blocked_local_conflict | comparison_unavailable
installed_version: string | Unknown
available_version: string
source_identity: verified | unrecorded | mismatch
hash_verification: verified | unavailable
comparison_mode: file_level | unavailable
changed_files: []
new_files: []
removed_files: []
unchanged_files: []
local_modified_files: []
```

When the installed source record is present, fetch its release-pinned manifest and compare the installed files to that prior manifest as well as the target manifest. Classify a file as a local modification when its installed hash differs from the prior release hash. Do not overwrite, delete, or silently absorb a local modification.

If the installed source record is absent, report `source_identity: unrecorded` and `awaiting_origin_confirmation`. Explain that this is a one-time migration from a pre-`v0.5.0` installation and ask the user to confirm that the existing matching Skill came from this repository. Do not infer origin from the name alone. If the record identifies another repository or Skill, report `blocked_source_identity` and stop.

When the Work surface can calculate SHA-256, verify every fetched manifest source and every comparable installed source. If a computed target hash differs from the target manifest, report `blocked_integrity`, reread a fresh manifest, and stop. If hash calculation or file-level access is unavailable, report `hash_verification: unavailable` or `comparison_unavailable`; do not claim a selective update.

## Review and approval

If there is no source delta and no local modification, report `already_up_to_date` and stop.

Otherwise show a concise `Delta` with installed and available version, changed/new/removed files, local modifications, verification status, and the proposed apply mode. Ask for clear conversational approval before changing any file. Approval is required even when the source identity is verified.

## Apply behavior

After approval, update the existing Skill through the already active `@skill-creator` workflow. Never create a duplicate Skill.

- With verified file-level comparison and no local conflict, apply only the changed, new, and safely removed declared source files. Preserve unchanged installed files.
- When file-level comparison is unavailable, the only permitted fallback is replacement with the exact declared source bundle after approval. Report `apply_mode: declared_bundle_replacement`, not `selective_file_update`.
- A local modification that overlaps an upstream change or removal is `blocked_local_conflict`. Stop and ask the user to choose a resolved source before replacing it.

Report `updated` only when the existing Skill was successfully saved and its `source-release.json` matches the target repository, Skill name, version, and ref. If native update fails, report `blocked` with the failed operation and exact returned error. Do not wait for a separate modal, callback, function tool, or hidden update button.

## Boundaries

- Update only `static-graphic-design-creator` from the declared source manifest.
- Do not clone the repository, run shell commands, create Codex files, install a plugin, add a connector or MCP server, use external providers, upload files, publish content, or generate an image.
- Never monitor GitHub in the background or apply a repository update without this explicit user-initiated flow and approval.
