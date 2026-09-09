# Contributing and release validation

Develop only the standalone `static-graphic-design-creator` and its source contract. Preserve its identity and integrated copy-development-and-human-voice asset. Personal installed copies are separate targets: never overwrite them from a source checkout without the update contract and approved Delta.

Maintain repository sources first. Prepare and validate the source and release-lock commits, then publish only when authorized. The owner can subsequently update installed Skills through the documented update flow. A repository task never authorizes editing an installed ChatGPT Work or Codex Skill.

## Working draft

Install test dependencies with `python3 -m pip install -r tests/requirements.txt`. Run `python3 -B tests/test_skill.py --working-tree` while source files are being edited. This verifies the previously pinned source and draft structure; it deliberately does not certify the edited bundle as a release. Run the design-contract tests when present and `python3 -B tests/check_source_anchors.py --check-inventory`.

Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s .agents/skills/static-graphic-design-creator/tests -p 'test_event_poster_codes.py'` for the bundled catalog. Preserve all 200 original lines and category mappings, separate authored interpretations from source attribution, and keep future authored additions under distinct provenance. The PDF is a development source, not a runtime dependency or bundled attachment.

Maintain documentation and catalog descriptions in English, using `/codes` in public usage descriptions. Localize onboarding and explanatory responses at runtime; localized fixture inputs and exact artwork/source strings are intentional test or provenance data. Keep language-specific catalog aliases in the internal workflow instead of advertising separate language editions.

## Repository description

Use this English text for GitHub's repository About / Description field, which appears on profile cards:

> Standalone skill for ChatGPT Work and Codex: concepts, copy, posters, ads and key visuals, with optional style codes, multilingual onboarding, reference-guided redesign and complete image prompts.

This is repository metadata, separate from the Skill's frontmatter. A commit to this file does not update the live About field. Set it through an authorized GitHub metadata operation and verify the saved field; report it as pending if the available connection cannot edit repository metadata.

## Candidate lock

1. Finish the bounded source patch, examples and tests. Choose an unpublished candidate version and update its source-release record. Never rewrite published source commits or move published release refs.
2. Fetch current public refs, confirm the chosen version is unpublished, and commit the Skill source first. Run `python3 -B scripts/release.py lock --source <exact-source-commit>` against that committed working bundle. It enumerates the exact Git tree, derives every SHA-256 and immutable URL, updates both configs without changing their structure, preserves verified historical baseline locators in `config/release-history.json`, and creates the matching pending host report. It rejects mixed working source, reserved personal paths and fetched published release refs. The single per-file inventory belongs in `config/chatgpt-skill-sources.json`; do not duplicate it in the bootstrap config. The source record does not claim its own Git commit.
3. Unexecuted host cases stay `pending`; changed source invalidates prior candidate evidence. The lock helper refuses to replace observed host results. Preserve historical reports and published refs; if existing host evidence belongs to another source, choose a new candidate version. Do not search-and-replace old release IDs across historical reports or changelog entries: those are necessary baseline evidence, not stale active files.
4. Run default `python3 -B tests/test_skill.py` to verify both the working bundle and pinned Git source. Run all affected contract/fixture checks. Commit the lock and report metadata together.
5. `main` is release discovery, never source identity. When publication is separately authorized, publish only the fully validated source-plus-lock history. If an authenticated GitHub tool creates a different source commit ID from the locally prepared commit, compare its complete source tree, fetch/check out that actual source and regenerate the lock against it before publishing discovery. A version tag/ref must target the lock commit containing its own matching manifest. Never publish an intermediate source commit alone to `main`, use a local-only SHA in public URLs, force-move an existing version ref, or describe an unpublished candidate as available.
6. Run `python3 -B scripts/release.py verify-public --lock <published-lock-commit> --release-ref <release-id>` after publication and completion of CI. It verifies both public refs, both configs, source ancestry and full tree inventory, every public raw file's SHA-256, and successful latest validation for that exact `main` commit. Recheck refs at the end. If the host cannot run network reads, perform the same read-only checks through the GitHub connector. A network error, pending/failed CI or mismatched ref is not a successful publication check.

Run `python3 -B -m unittest discover -s tests -p 'test_lifecycle.py'` as a required local and CI gate. It covers the existing-Skill update cycle and release preparation with deliberate failure cases. The tests do not save a native Skill or authorize publication. Verify About metadata separately when it is in scope; a source commit cannot update that GitHub field.

Local commit IDs and tests do not prove public URL availability. A locally locked, unpublished candidate must be reported as such. Do not repair historical public refs by moving them without a separate owner decision; current update contracts reject their mismatching manifests.

## Stable gate

A candidate is not stable until deterministic validation passes, all required host cases in EVALUATION.md have actual dated evidence for ChatGPT Work and Codex, and critical outcomes pass. `blocked`, `pending` and unsupported capabilities never count as passes. Justified `not_applicable` must explain why the requirement does not apply. A fresh reachability check must distinguish blocked/unknown links from reached links, and historical claims still require source review. Recheck OpenAI-surface statements against current official documentation.

The repository-owner controls in SECURITY.md are a separate publication prerequisite. Do not change permissions, publish, push or install a candidate merely because local tests pass.
