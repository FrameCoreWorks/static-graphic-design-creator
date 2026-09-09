# Skill lifecycle audit for v0.9.0-rc.2

Prepared on 2026-09-08. Scope: repository-backed installation, personal extension,
source update, release locking and publication verification. No installed Skill
was modified, no duplicate was created and this report does not publish a release.

## Observed incident

The reported installation records v0.8.0-rc.1. Public v0.9.0-rc.1 resolves source
commit `aed4bb2566e9b408e2e34d78b35b30a4c07d2348` through lock commit
`ab984adab7958a4fbcbec0a8115e4d9292c497eb`. All 24 declared source files were
verified against their SHA-256 values at publication. The present read-only
inspection reproduced 18 installed files equal to that target, six different
declared paths and one extra icon.

The four add/add collisions differ only in development provenance wording:

| Path | Observed difference |
| --- | --- |
| `references/evaluation-scenarios.md` | Personal-extension description versus bundled-workflow description |
| `references/event-poster-code-workflow.md` | Supplied-source wording, personal integration label and personal-versus-repository maintenance paragraph |
| `references/event-poster-design-codes.json` | Source attribution wording only; code data is identical |
| `scripts/event_poster_codes.py` | Module docstring only; executable behavior is identical |

The other differences are the old upstream record and customized
`agents/openai.yaml`; `assets/icon.svg` is a local addition. These observations
support a reviewed proposal to adopt the four target files and target record
together, preserving metadata and the icon. They do not authorize applying it to
the active installation. A source, lock and host-save commit having different
IDs is expected and is not proof of mismatched source bytes.

## Findings and corrections

| Finding | Correction in the prepared candidate |
| --- | --- |
| The updater stopped before preparing a read-only conflict resolution, creating an unnecessary approval round | Prepare exact diffs and the full proposed merge immediately; obtain approval once for actual installed-file changes |
| A committed personal extension can have a clean working tree and still overlap a later source release | Distinguish uncommitted changes, upstream delta, files already at target and remaining personal differences |
| Personal feature files used future upstream paths, causing add/add collisions | Optional `local/SKILL_EXTENSIONS.md` entry and reserved local resources; record necessary canonical overrides and review migrations |
| Source-record changes can be mistaken for a standalone fix | Build the complete result before saving; unresolved conflicts block every write; verify the record and all contents together |
| Existing installation evidence allowed a visible entry to stand in for content verification | Require actual save plus complete readback, recorded host adaptations and repeat comparison |
| Release locking was manually assembled and vulnerable to pinning a local rather than published source commit | Deterministic lock helper derives source inventory/hashes/configs/report from exact committed bytes; repin after connector-created commit IDs change |
| Package checks did not cover all bootstrap repository/root identity fields or source ancestry | Shared strict bootstrap/manifest validation, one per-file manifest and an ancestry gate |
| Some historical version branches contain another release's manifest | Verified immutable history locators for five releases, including matching rc.2/rc.3 locks, without moving published branches |
| Digest comparisons alone did not exercise a full update cycle | Disposable lifecycle tests cover install/update/no-op, extensions, collisions, deletions, concurrent edits, stale records and failed-readback detection |
| A successful push alone cannot establish a usable public release | Separate public verifier checks discovery/version refs, both configs, source ancestry and inventory, every source hash and exact-commit validation CI |

## Verification evidence

- Thirteen lifecycle/release test methods passed, including the historical
  18-matching-file/four-collision structure and controlled failures for public
  refs, raw bytes, tree inventory and CI results.
- Thirteen existing digest-classification cases, 70 design-state/transition cases,
  both actual design templates, frontmatter/document checks and the 22-URL source
  inventory passed. The catalog retains 200 exact code lines in 20 categories.
- All five indexed historical source bundles and manifest digests were verified
  from immutable Git objects. Their five manifest files were independently fetched
  from public GitHub and matched those exact bytes.
- One independent source-only exercise received disposable baseline/target/installed
  artifacts and the updated contract, without the intended result. It prepared a
  complete five-file proposal, preserved host metadata/icon bytes, requested no
  permission to analyze and performed no save. In-memory recomparison produced
  `local_customizations_preserved`, with only metadata and icon deviations.

These checks do not execute the ChatGPT Work or Codex native save/reconciliation
service. All 49 required host cases remain pending for the final candidate.
Rollback tests establish mismatch detection and snapshot equality; they do not
claim an actual host failure was induced or a live rollback was performed.

## Remaining boundaries

Real personal behavior can conflict with future upstream behavior. Resolving it
requires a reviewed choice or merge, not ignored hashes or automatic replacement.
Older releases absent from the verified history still need a valid baseline;
missing evidence is reported rather than invented. Historical records stay intact
because updates use them as evidence. Obsolete active upstream files are removed
only through the approved file-level update plan.

The repository's English About text is prepared in CONTRIBUTING.md. Updating that
live field remains pending because the available connector has no metadata-edit
operation. The installed Skill remains the owner's separate update target.
