# Changelog

This file records user-visible changes to the standalone Skill. Stable, versioned release refs remain the source of truth for published versions.

## [0.5.0] - 2026-08-28

### Added

- repository-assisted update contracts for ChatGPT Work and Codex, each using a user-pasted update request rather than automatic repository monitoring;
- an installed `source-release.json` record that identifies the repository, Skill name, release version, and ref used as an update baseline;
- manifest-based file delta classification for changed, new, removed, unchanged, and locally modified source files;
- explicit update states for no-op, unrecorded origin, source mismatch, integrity mismatch, unavailable comparison, and local conflict;
- regression fixtures and manual forward tests that require review and user approval before replacing any existing installed Skill.

## [0.4.0] - 2026-08-28

### Added

- objective-first poster direction, with `discovery_brainstorm` for open briefs and `directed_collaboration` for users who already know their intended route;
- a poster style and composition atlas covering goal classes, composition archetypes, historical visual families, material treatments, and original-attribute translation;
- an anti-slop composition gate that rejects decorative effect stacks without a visual thesis, hierarchy, or functional role;
- behavioral regression fixtures and manual forward tests for brainstorm, directed collaboration, and named-artist translation.

## [0.3.1] - 2026-08-28

### Changed

- renamed the public repository address to `FrameCoreWorks/static-graphic-design-creator` and updated installation documentation and source manifests to use the canonical URL directly.

## [0.3.0] - 2026-08-28

### Changed

- renamed the Skill to `Static Graphic Design Creator` with the canonical identifier `static-graphic-design-creator`;
- updated its native ChatGPT Work and Codex installation contracts, UI metadata, and source manifest for the new identity;
- added the FrameCore Works repository banner.

## [0.2.0] - 2026-08-28

### Added

- explicit `render`, `prompt`, and `render_and_prompt` output modes, with native image generation limited to a direct user request;
- native-render fallback to a complete prompt when the active surface cannot generate an image;
- separate `input_context`, `output_mode`, `render_status`, and QA-route contracts;
- a `production_intent` decision that distinguishes a concept raster, digital final, and a DTP-only production master;
- likeness authority, reference precedence, and original-style-treatment rules;
- compactness guidance that preserves the eight-stage logic without forcing verbose prompts;
- a stable, release-pinned source manifest at `v0.2.0` with manual user-approved updates;
- optional Codex compatibility profile for text-bearing static graphics;
- mandatory pre-approval onboarding for ChatGPT Work installation;
- strengthened ChatGPT Work installation around the active native `@skill-creator` creation workflow and real creation evidence;
- eight-stage to six-section handoff crosswalk without changing the standalone default;
- copy-feasibility and brand-identity authority gates;
- SHA-256 mismatch recovery in both install contracts;
- policy regression fixtures and a GitHub Actions validation workflow.

### Changed

- prompt packs now carry rendering context, generator prompt format, copy feasibility, and brand identity policy.
- Codex native image routing now uses `execution_surface: codex_builtin_imagegen`, `generator_provider: openai`, and `target_generator: gpt-image-2` instead of a nonstandard provider-qualified model string.
- ChatGPT Work continues from the declared source manifest when SHA-256 calculation is unavailable, while a computed mismatch remains a blocking integrity failure.
- the repository-assisted creation route is documented as a source contract, not an automatic package registry or update mechanism.
