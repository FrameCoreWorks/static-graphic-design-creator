# Install Static Graphic Design Creator in Codex

## Purpose

Install one personal Skill, `$static-graphic-design-creator`, from:

`https://github.com/FrameCoreWorks/static-graphic-design-creator`

Use Codex's built-in `$skill-installer` for this fresh third-party Skill installation. It resolves a public GitHub source into the personal Skills directory; it must not clone the repository into the user's project.

## Resolve the immutable source

1. Resolve a bootstrap Git commit and read both configs at that same commit; retain it as installation evidence. Read the repository-relative `config/chatgpt-skills.json` and `config/chatgpt-skill-sources.json`.
2. Require both configs to agree on release ID, version and source commit, and any requested release to match. Confirm the manifest declares exactly `static-graphic-design-creator`, `release_ref_type: immutable_git_commit`, and one 40-character `immutable_source_commit` identical to `ref`.
3. Confirm every declared `raw_url` includes that same immutable source commit and every `repository_path` maps to the declared relative bundle `path`.
4. Use `$skill-installer` to install only this source directory from the exact immutable GitHub tree:

```text
https://github.com/FrameCoreWorks/static-graphic-design-creator/tree/<immutable_source_commit>/.agents/skills/static-graphic-design-creator
```

`<immutable_source_commit>` is a manifest value, not a user-supplied placeholder to guess. The installer must resolve it before it requests the source.

## Verify and install

Read every declared source file and verify its SHA-256 against the manifest before installation. If a hash differs, stop with `blocked_integrity`, reread fresh bootstrap manifests, and restart the source check. If the host cannot compute SHA-256, report `hash_verification: declared_unverified`; do not claim that hashes were verified.

Confirm the source directory contains exactly the declared safe relative paths, with no symlinks, traversal, duplicates or undeclared files. Install the relative bundle exactly as declared, including `SKILL.md`, `agents/`, `references/`, `scripts/`, `templates/` and bundled `tests/`. The code catalog is self-contained; do not download or attach its source PDF. Do not install unrelated repository files, create a workspace copy, generate an image, use external services, or make a background update.

If the Skill already exists, do not overwrite it. Follow `CODEX_UPDATE.md`: compare source identity and delta, show `Delta`, and ask for explicit user approval before any replacement.

Verify the entire saved inventory and bytes after installation, including source identity. Retain the manifest commit, source commit, source digests and actual saved digests in host-supported installation evidence outside the canonical bundle. Record any required host metadata/icon adaptation as an exact local deviation; a directory or UI entry alone does not prove correct installation. Compare once more against the same release: expect `already_up_to_date` for an exact copy or `local_customizations_preserved` only for recorded host adaptations, without another save. A stale record or unresolved content conflict fails acceptance. Report success only after the real installed result and complete readback verification. If installation or verification fails, report the actual operation and stop.

## First-use introduction

After a verified installation, use `references/first-use-onboarding.md` from that installed bundle to resolve the user's language and explain explicit invocation, optional catalog commands, new prompts and improvement of an existing poster. Use an explicit language preference first, otherwise the user's own prose and recent context, then a reliable locale actually exposed by the host, or English when no signal exists. A pasted English setup prompt does not override the conversation. Do not infer language from Codex or the operating system, or claim to read hidden account settings.

An accessible local image path or a supported attachment can supply the actual reference. Explain `/codes`, the short `/Name` and the listed `/Name /rebuild`, plus ordinary brief/brainstorm work with no code choice, internal direction selection or complete catalog opt-out. During Polish onboarding also explain `/kody`; introduce local aliases where appropriate rather than giving every user a bilingual command list. Keep canonical code strings and locked artwork text unchanged. Describe factual/reference locks and narrow edits in the user's language.

Skip material already explained, honor requests to hide codes or skip onboarding, and continue a supplied brief. Do not force a catalog choice, render an example or ask for acknowledgment. If the installer cannot provide the introduction, use the first known explicit Skill invocation. Do not invent an install event hook or a durable per-user flag.

Briefly introduce optional separate assets for manual assembly: a shared composition, one element generated and discussed at a time, corrections followed by explicit acceptance, and a project registry of approved versions. After the agreed set is complete, offer individual files or ZIP when supported. Preserve the default integrated graphic and clarify that editable text needs actual typesetting. Do not create an example or register a command during installation.
