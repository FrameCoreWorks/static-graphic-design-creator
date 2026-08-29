# Contributing and Release Gate

## Scope

Keep changes focused on the standalone `static-graphic-design-creator` Skill and its declared source contract. Do not add external providers, background sync, automatic publishing, or unrelated repository bundles.

## Before a candidate commit

1. Update the Skill source and any directly affected documentation, templates, fixtures, or examples.
2. Run `python3 tests/test_skill.py` and `python3 tests/check_source_anchors.py --check-inventory`.
3. Build the immutable Skill source commit first.
4. In a following release-lock commit, set `immutable_source_commit` to that source commit and ensure every manifest `raw_url` uses it.
5. Run the local validation suite again. Do not edit declared source files after the immutable source commit; make a new source commit and lock if they change.

## Stable-release gate

Do not publish or tag a candidate as stable until all of the following are true:

- local contract validation passes;
- the scheduled or manual reference-anchor check has a current passing result;
- all twenty host cases in `EVALUATION.md` have been executed in real ChatGPT Work and Codex sessions;
- the dated result file under `reports/host-evaluations/` records the version, immutable source commit, host availability, and each observed outcome;
- OpenAI-specific statements have been rechecked against official documentation and their verification date updated in `README.md`.

If a host capability is unavailable, record that as `blocked`, not as a passing result. A release candidate may remain public for review; it is not a stable release until this gate is complete.
