# Install Static Graphic Design Creator in Codex

## Purpose

Install one personal Skill, `$static-graphic-design-creator`, from:

`https://github.com/FrameCoreWorks/static-graphic-design-creator`

Use Codex's built-in `$skill-installer` for this fresh third-party Skill installation. It resolves a public GitHub source into the personal Skills directory; it must not clone the repository into the user's project.

## Resolve the immutable source

1. Read the repository-relative `config/chatgpt-skills.json` and `config/chatgpt-skill-sources.json`.
2. Confirm the manifest declares exactly `static-graphic-design-creator`, `release_ref_type: immutable_git_commit`, and one 40-character `immutable_source_commit` identical to `ref`.
3. Confirm every declared `raw_url` includes that same immutable source commit and every `repository_path` maps to the declared relative bundle `path`.
4. Use `$skill-installer` to install only this source directory from the exact immutable GitHub tree:

```text
https://github.com/FrameCoreWorks/static-graphic-design-creator/tree/<immutable_source_commit>/.agents/skills/static-graphic-design-creator
```

`<immutable_source_commit>` is a manifest value, not a user-supplied placeholder to guess. The installer must resolve it before it requests the source.

## Verify and install

Read every declared source file and verify its SHA-256 against the manifest before installation. If a hash differs, stop with `blocked_integrity`, reread fresh bootstrap manifests, and restart the source check. If the host cannot compute SHA-256, report `hash_verification: declared_unverified`; do not claim that hashes were verified.

Install the relative bundle exactly as declared, preserving `SKILL.md`, `agents/`, `references/`, and `templates/`. Do not install unrelated repository files, create a workspace copy, generate an image, use external services, or make a background update.

If the Skill already exists, do not overwrite it. Follow `CODEX_UPDATE.md`: compare source identity and delta, show `Delta`, and ask for explicit user approval before any replacement.

Report success only when Codex returns a real installed personal-Skill result. If installation fails, report the failed `$skill-installer` operation and stop.
