# Layered asset integration: v0.11.0-rc.1

Date: 2026-09-10. Scope: the public repository source only. No installed Skill was edited, no duplicate created, and at the initial implementation-review checkpoint, no source commit, push or publication had been performed. The owner approved implementation with a stop before commit/push, including sequential asset review and individual/ZIP delivery choice, then separately approved commit and push after manifest verification.

## Source and release boundary

- Verified published baseline: `v0.10.0-rc.1`.
- Published source commit: `c778236b9f10e28276b2048fc78b689ac5739376`.
- Published manifest/main commit: `c1c3e7888220283d793bd80c4a5ee8235f27343d`.
- Manifest SHA-256: `8e234cc5051ae282092fc7e6c02db145cad378d0f556ff61b5527ebc91b235fd`.
- The remote main and manifest were read and compared with the clean checkout before this extension. The current draft source identifies the proposed `v0.11.0-rc.1`; it is not an available release.
- The discovery configs, release history, published reports and release helper remain unchanged until an authorized real source commit allows a new immutable lock. Do not install the edited working tree as if it were the currently pinned release.

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
| `tests/test_skill.py --working-tree` | pass | 28 pinned baseline files, 13 three-way digest cases, draft document links and new plan validation; not a new release lock |
| `tests/test_design_contracts.py` | pass | Existing 70 cases and two actual templates, plus 3 layered handoff checks |
| `tests/test_lifecycle.py` | 15 pass | Includes actual draft source update/no-op with preserved personal files and a colliding layered reference that blocks mutation |
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

Added 11 raw-task scenarios in `tests/fixtures/layered-assets-eval-cases.json`, with corresponding host cases 56-66 in `EVALUATION.md`. The existing published candidate report retains its original 55-case inventory; it is historical evidence, not a stale file to rewrite. The release helper will generate the new candidate's 66-case pending report after the source commit is approved and exists.

Still untested for this candidate: actual native generation and correction of a complete asset sequence; cutout/overlay visual quality; actual Canva/Illustrator import and blending; real archive creation/delivery through each host; new candidate installation, native save/update and continued work across chats in ChatGPT Work and Codex. Actual candidate source commit, manifest commit, CI and public availability are `Unknown` until separately authorized and observed. Synthetic tests or prior user tests of other releases cannot pass these cases.

Current official capability references were reviewed on 2026-09-10 and are linked with scoped claims in the layered workflow. No model identifier, editor blend feature or API-only setting is promoted into a guaranteed native control.

## Commit and release handoff

Commit/push approval was received on 2026-09-10 after the implementation report. Before committing, recheck the owner-selected version and public refs, preserve any concurrent changes, and verify this complete patch. Commit the source first, derive both configs/history and the pending host report using `scripts/release.py lock --source <actual-source-commit>`, run default release validation plus affected suites, and commit the lock. Publish only the complete source-plus-lock history if authorized. If a connector assigns a different source commit ID, verify its complete tree and regenerate against that actual public source before changing discovery.

After publication, use `scripts/release.py verify-public` or equivalent authorized read-only GitHub checks: exact public refs, source ancestry, both configs, complete source inventory/hashes and successful latest CI for the published main commit. Do not move an existing published version ref, copy project registries or personal files into the release, or edit an installed Skill as a side effect. Before publication, rollback is limited to reverting this draft patch relative to the baseline while preserving unrelated changes; later correction requires a new release.
