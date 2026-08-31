# Changelog

This file records user-visible changes to the standalone Skill. Stable, versioned release refs remain the source of truth for published versions.

## [0.7.0-rc.3] - 2026-08-31

### Added

- a Codex personal-extension prompt beside the ChatGPT Work route, so an installed local Skill can be tailored through a guided, approval-gated discovery flow.

### Changed

- README now separates fresh installation, source update, and personal extension for both supported surfaces.

### Pending before stable

- all twenty live host evaluations in ChatGPT Work and Codex must be recorded as passing for this candidate;
- repository-owner branch rules must be enabled for `main` and release branches before publishing a stable release.

## [0.7.0-rc.2] - 2026-08-31

### Added

- one internal `Copy Development and Human Voice` asset that develops anti-generic poster wording from objective, audience, source truth, and a concrete message thesis;
- explicit `locked_copy`, `copy_discovery`, and `copy_refinement` routes, with a selected-copy gate before final prompting or rendering;
- structured `copy_pack` fields for copy authority, source truth, selected wording, claim status, copy locks, and copy fit.

### Changed

- the Skill now develops and humanises visible poster copy as one integrated internal layer rather than routing the user through separate copywriting and humanisation steps;
- intake, portable handoff, prompt pack, README, and host evaluation all record the copy-selection decision.

### Pending before stable

- all twenty live host evaluations in ChatGPT Work and Codex must be recorded as passing for this candidate;
- repository-owner branch rules must be enabled for `main` and release branches before publishing a stable release.

## [0.7.0-rc.1] - 2026-08-29

### Added

- an immutable-source release model: the release manifest resolves every declared Skill file through one Git commit and records its SHA-256 value;
- a complete popular-style translation catalog and compact production walkthroughs for discovery, directed collaboration, scoped edits, and full rerenders;
- a security boundary document, host-evaluation result record, stable-release gate, curated-source anchor checker, and scheduled link-check workflow;
- explicit Codex fresh-install guidance through `$skill-installer` and language-adaptive user-facing clarifications.

### Changed

- hash-unavailable installation now reports `declared_unverified`, making the lower-trust state explicit while preserving host compatibility;
- installation and update contracts resolve immutable source commits before retrieval, rather than treating a mutable release branch as source identity;
- README banner now uses a 1983×793 WebP derivative to reduce repository display weight while preserving the original PNG source.

### Pending before stable

- all twenty live host evaluations in ChatGPT Work and Codex must be recorded as passing for this candidate;
- repository-owner branch rules must be enabled for `main` and release branches before publishing a stable release.

## [0.6.2] - 2026-08-29

### Fixed

- rewrote the ChatGPT Work setup and update contracts as native Skill-only flows, without unrelated terminology;
- requires the active `@skill-creator` managed-personal-Skills save path after the source bundle validates, rather than treating source verification as an installation result;
- permits only the host-managed personal-Skills storage required for that native save and continues to prohibit writes into the user's project workspace.

## [0.6.1] - 2026-08-29

### Fixed

- aligned the ChatGPT Work repository-source contract with the proven FrameCore Works Skill-kit format;
- separated each remote `repository_path` from its relative native Skill-bundle `path`, so every retrieved source file has one unambiguous destination inside the single Skill;
- made the Work handoff explicit: after all declared files resolve, the active `@skill-creator` must create and save the one native Skill rather than ending at source verification;
- added release-pinned raw bootstrap and manifest URLs to the Work configuration and copy-paste setup path.

## [0.6.0] - 2026-08-28

### Added

- a detailed poster movements and production atlas that separates historical record, design synthesis, generator constraints, and editorial rules;
- function-first profiles for film, theatre, social, political, cultural, commercial, informational, flyer, key-visual, and cover work;
- evidence-grounded historical-language cards, including Sachplakat, distinct New Typography and Bauhaus entries, a narrowly scoped Polish Poster School, and process-aware contemporary methods;
- process-fit guidance for lithography, screenprint, Risograph, letterpress, photomontage, collage, offset, and halftone;
- a four-level visible-information hierarchy (`must_read`, `should_read`, `metadata`, `decoration`), reading modes, and explicit intentional-legibility-friction review;
- regression and forward-evaluation cases for process logic, dense information, political confirmation, historical-language stereotype avoidance, and psychedelic legibility conflicts.

### Changed

- the prompt contract, intake, prompt-pack, deliverable profiles, and QA now carry text hierarchy, image/type roles, material-process logic, and human-review requirements;
- social and political briefs now require explicit user confirmation for position, claims, cultural representation, and charged historical symbols;
- material treatments must follow an identifiable process logic rather than generic vintage, damage, noise, or effect filters.

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
