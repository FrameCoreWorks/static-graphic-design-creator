# Security and Integrity Model

## What a release manifest verifies

The release manifest lists the exact Skill files, their relative bundle paths, SHA-256 values, and one immutable Git commit. Every `raw_url` must retrieve the source from that commit.

When the receiving host can calculate SHA-256, a matching digest verifies that the retrieved bytes match the release manifest. This catches transfer corruption and a manifest/file mismatch. A digest mismatch blocks creation or update.

## When hashing is unavailable

Some hosts cannot calculate SHA-256 during repository-assisted setup. In that case the installer records:

```text
hash_verification: declared_unverified
```

The Skill may still be created because the repository is intended to work on such surfaces, but it is not a cryptographically verified installation. Documentation and installation output must never relabel this state as `verified`.

## Trust boundary

Commit-pinned source URLs make the resolved Skill bundle immutable within Git history. They do not create an independent root of trust for the initial repository bootstrap. A party able to change the discovery branch or repository ownership could point a later bootstrap manifest at a different commit and matching hashes.

This repository therefore claims **manifest-verified file integrity when hashing is available**, not full supply-chain provenance. Stronger assurance would require protected branches or rulesets, signed tags or commits, and an independent release-attestation channel.

## Repository-owner controls

Before publishing a stable release, enable GitHub rules for `main` and release branches that at minimum:

- disallow force pushes and branch deletion;
- require pull requests for changes to protected branches;
- require the validation workflow to pass;
- use signed commits or signed tags when the maintainer's workflow supports them.

For a solo repository, the no-force-push and required-status-check controls provide the highest practical value without creating an artificial reviewer requirement.

## Reporting

Do not include secrets, credentials, private prompts, or personal data in a public issue. This repository does not currently publish a separate private vulnerability-reporting channel. Report non-sensitive integrity problems through a GitHub issue with the affected release ID and immutable source commit.

## Baseline and recovery

Record the immutable manifest commit and digest as host-supported installation evidence, separate from the canonical bundle and its self-referential source identity. Resolve legacy baselines only after matching the requested release ID. A mutable version branch carrying another release is not a valid baseline.

The release-history index supplies immutable locators, not an independent trust root or an exemption from verification. Check the retrieved manifest digest, release/source identity and every source hash before using it. The reserved `local/` extension namespace must not be included in a public source release. Host metadata and personal assets remain recorded local differences; never ignore whole files to make verification pass.

Before an approved update, preserve a recoverable snapshot, recheck installed/target bytes, and stage the expected complete result. Verify saved bytes, safe deletions, local additions and metadata. Failed or unverifiable saves must not be reported as updated. Restore and verify the snapshot when supported; report a failed rollback explicitly.

A source record identifies an upstream base; local differences are personal changes, not proof of source corruption or an authentic new release. Never use unavailable comparison as a reason to delete unknown personal files.
