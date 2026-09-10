# Layered asset integration: v0.11.0-rc.1

Date: 2026-09-10. Scope: the public repository source only. No installed Skill was edited, no duplicate created, and at the initial implementation-review checkpoint, no source commit, push or publication had been performed. The owner approved implementation with a stop before commit/push, including sequential asset review and individual/ZIP delivery choice, then separately approved commit and push after manifest verification.

## Source and release boundary

- Verified published baseline: `v0.10.0-rc.1`.
- Published source commit: `c778236b9f10e28276b2048fc78b689ac5739376`.
- Published manifest/main commit: `c1c3e7888220283d793bd80c4a5ee8235f27343d`.
- Manifest SHA-256: `8e234cc5051ae282092fc7e6c02db145cad378d0f556ff61b5527ebc91b235fd`.
- The remote main and manifest were read and compared with the clean checkout before this extension. Public refs were fetched again before committing; main still matched the baseline and `v0.11.0-rc.1` was unpublished.
- Candidate source commit: `19a559b207c804f265fa9180c6cecb5165d67fe3`.
- Candidate manifest SHA-256: `47c40008a3a51e8be62f06fd451c3be6e5471e88a4a7360fcbcbbf0776c75b0a`.
- Both discovery configs, release history and the candidate's pending host report were derived from that exact committed source using `scripts/release.py lock`. The release helper and historical reports remain unchanged. The GitHub connection assigned the actual source commit above; its complete tree matched the locally validated source (`08c85541d164718884f497171a457776301c869c`). The lock was regenerated against that actual source before updating public discovery. This record captures lock preparation; public availability requires the separate post-push verification below.

The Skill bundle contains 32 files: 4 new, 12 changed, 16 unchanged, none removed, relative to the 28-file baseline. Core concept/copy resources, design-state schema, 200-entry catalog, model references, UI metadata and lifecycle helper remain byte-identical to that baseline.

## Behavior delivered

- Explicit separate-assets requests share a composition and create elements primarily from scratch. Existing-poster separation is a secondary route with extracted/reconstructed/newly-generated provenance.
- A complete asset request still proceeds one element at a time: generation, inspection, user feedback, scoped correction and explicit acceptance before advancing. Existing execution permission is reused within the agreed sequence, not repeatedly requested.
- The project registry retains exact selected versions and previous candidates. It is stored with the project, outside Skill sources and personal-extension instructions. A new chat needs the actual registry and accessible files.
- Project copy and locks remain intact while the current raster task contains only its assigned content. Manual typesetting can coexist with independently feasible raster elements; this does not certify an editable master or complete poster.
- Delivery offers individual files or ZIP once, honoring an existing choice. Only selected versions and three delivery sidecars are included. The helper verifies actual source files, the asset index, selected-only portable records, and ZIP entries/decompressed bytes or individual-file inventory.
- The helper is read-only. Generation, registry writes, file exposure and archive creation use the active host's supported tools under the actual user request. No external provider, editor upload, paid service or automatic dependency installation is added.

## Deterministic verification

| Check | Observed result | Scope |
| --- | --- | --- |
| Skill creator quick validation | pass | Frontmatter/name/structure only |
| `tests/test_skill.py` | pass | 32 pinned candidate files and working-source agreement, 13 three-way digest cases, 66 host cases recorded but not executed; immutable release lock verified locally |
| `tests/test_design_contracts.py` | pass | Existing 70 cases and two actual templates, plus 3 layered handoff checks |
| `tests/test_lifecycle.py` | 15 pass | Includes update from the fixed pre-layered source to the candidate, repeated no-op with preserved personal files, and a colliding layered reference that blocks mutation |
| Bundled `test_layer_assets.py` | 31 pass | Synthetic temporary files: sequential review, version selection, structured concept/copy preservation, alpha, geometry, dependencies, safe paths and delivery integrity |
| Bundled catalog tests | 11 pass | Existing 200-code behavior preserved |
| Source-anchor inventory | pass, 33 URLs | Inventory only, not a new reachability review of all historical anchors |
| `git diff --check` | pass | Patch whitespace |

The image checks use tiny synthetic PNGs and a text specification created inside disposable test directories. They are not image-model outputs. Cases include an opaque painted checkerboard, empty transparency, palette transparency, missing Pillow, corrupt image, dimension mismatch, changed/missing approved files, symlinks, rejected newest version, extra/duplicate/modified ZIP entries, stale index and a selected subset whose portable plan retains dependency context without other version files.

## Independent source-only exercises

Two fresh agent contexts received the Skill source, realistic user requests, and only the relevant raw input. They were not given expected answers or implementation diagnoses. They were constrained to read-only or conversational work; neither exercise changes the two native-host evaluation columns.

1. **Background prompt before title selection.** Raw request: build separate Canva poster elements from a locked warm-person/cool-empty-square concept, 1024 by 1536; title undecided and editable later; background prompt in English only; no codes even internally. Observed: one background-only prompt, reserved title space, no person/shadows/fog or lettering, no generation and no forced title selection. Read `SKILL.md`, layered workflow and unified prompt contract. This exercises scoped prompting, not actual alpha or model layout fidelity.
2. **End-of-sequence delivery choice.** Raw input: the synthetic four-asset registry and real tiny files, all scoped selected versions approved within the fixture, a later rejected person version retained, delivery undecided. Raw request: finish the test project and explain what is ready and next. Observed: selected `v001` background/person/fog and the title specification identified; actual digests and dimensions checked; individual files versus ZIP asked once; rejected `v009` excluded; no archive or external action initiated. The answer explicitly described synthetic approvals. This exercises file/version selection and conversational stopping, not live customer approval or editor import.

These were source-only development exercises, not blind human evaluation or certification of every scenario. The final draft also received deterministic checks after the final entrypoint wording was clarified.

## Manual evaluation and remaining Unknowns

Added 11 raw-task scenarios in `tests/fixtures/layered-assets-eval-cases.json`, with corresponding host cases 56-66 in `EVALUATION.md`. The prior published candidate report retains its original 55-case inventory; it is historical evidence, not a stale file to rewrite. The release helper generated the new candidate's 66-case report, with every ChatGPT Work and Codex result still pending.

Still untested for this candidate: actual native generation and correction of a complete asset sequence; cutout/overlay visual quality; actual Canva/Illustrator import and blending; real archive creation/delivery through each host; new candidate installation, native save/update and continued work across chats in ChatGPT Work and Codex. CI and public availability require observation after publishing the lock commit; they are not certified by this pre-publication record. Synthetic tests or prior user tests of other releases cannot pass these cases.

Current official capability references were reviewed on 2026-09-10 and are linked with scoped claims in the layered workflow. No model identifier, editor blend feature or API-only setting is promoted into a guaranteed native control.

## Commit and release handoff

Commit/push approval was received on 2026-09-10 after the implementation report. The public-ref check, source commit, derived lock and default release validation plus all affected suites have completed successfully. Commit the lock metadata next and publish only the complete source-plus-lock history. If a connector assigns a different source commit ID, verify its complete tree and regenerate against that actual public source before changing discovery.

After publication, use `scripts/release.py verify-public` or equivalent authorized read-only GitHub checks: exact public refs, source ancestry, both configs, complete source inventory/hashes and successful latest CI for the published main commit. Do not move an existing published version ref, copy project registries or personal files into the release, or edit an installed Skill as a side effect. Before publication, rollback is limited to reverting this draft patch relative to the baseline while preserving unrelated changes; later correction requires a new release.
