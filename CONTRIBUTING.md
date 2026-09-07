# Contributing and release validation

Develop only the standalone `static-graphic-design-creator` and its source contract. Preserve its identity and integrated copy-development-and-human-voice asset. Personal installed copies are separate targets: never overwrite them from a source checkout without the update contract and approved Delta.

## Working draft

Install test dependencies with `python3 -m pip install -r tests/requirements.txt`. Run `python3 -B tests/test_skill.py --working-tree` while source files are being edited. This verifies the previously pinned source and draft structure; it deliberately does not certify the edited bundle as a release. Run the design-contract tests when present and `python3 -B tests/check_source_anchors.py --check-inventory`.

## Candidate lock

1. Finish the bounded source patch, examples and tests. Choose an unpublished candidate version and update its source-release record. Never rewrite published source commits or move published release refs.
2. Commit the Skill source first. In a following lock commit, enumerate every source file from that exact Git tree, calculate SHA-256 from its bytes, and set matching source IDs and immutable URLs in both configs. The source-release record does not claim its own Git commit.
3. Create the candidate host report with the exact release ID and source commit. Unexecuted cases stay `pending`; a changed source invalidates previous host evidence for that candidate. Preserve historical reports.
4. Run default `python3 -B tests/test_skill.py` to verify both the working bundle and pinned Git source. Run all affected contract/fixture checks. Commit the lock and report metadata together.
5. `main` is release discovery, never source identity. When publication is separately authorized, publish only the fully validated source-plus-lock history. A version tag/ref must target the lock commit containing its own matching manifest. Do not publish an intermediate source commit alone to the discovery branch. Recheck the remote ref/manifest agreement after publishing.

Local commit IDs and tests do not prove public URL availability. A locally locked, unpublished candidate must be reported as such. Do not repair historical public refs by moving them without a separate owner decision; current update contracts reject their mismatching manifests.

## Stable gate

A candidate is not stable until deterministic validation passes, all required host cases in EVALUATION.md have actual dated evidence for ChatGPT Work and Codex, and critical outcomes pass. `blocked`, `pending` and unsupported capabilities never count as passes. Justified `not_applicable` must explain why the requirement does not apply. A fresh reachability check must distinguish blocked/unknown links from reached links, and historical claims still require source review. Recheck OpenAI-surface statements against current official documentation.

The repository-owner controls in SECURITY.md are a separate publication prerequisite. Do not change permissions, publish, push or install a candidate merely because local tests pass.
