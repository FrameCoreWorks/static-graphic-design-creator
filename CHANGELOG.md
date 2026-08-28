# Changelog

This file records user-visible changes to the standalone Skill. Stable, versioned release refs remain the source of truth for published versions.

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
