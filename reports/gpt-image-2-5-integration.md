# GPT Image 2.5 handbook integration

Integration date: **2026-09-09**. Candidate: **v0.10.0-rc.1**. The owner authorized its publication after reviewing the local Delta and checks. Destination: the existing repository Skill source only. Installed ChatGPT Work and Codex copies are separate user-controlled targets.

## Input and evidence boundary

Read all 16 chapters of the user-supplied `GPT_Image_2_5_Master_Knowledge_Base.md`, release 1.0: 1,708 lines, 169,536 bytes; SHA-256 `78b1308d15961fc900554d886b1dcbdbec5aec2bfad701eda323a099ca769f28`. It is development input, not a runtime dependency. Neither the handbook nor original poster PDF is added to the bundle. Authored operational guidance is adapted to the existing Skill rather than importing the handbook's proposed separate architecture.

The handbook reports 126 API outputs from 131 attempts, 15 ChatGPT outputs and one native synthetic fixture. Those counts and outcomes were read, not independently verified: the corresponding original images, raw responses, attempt ledger and companion manifest were not supplied. Two reviews by the same assistant do not provide independent human evaluation. Worked examples are authored and unrendered. No API keys, paid benchmark calls, native renders or installed-Skill writes were used for this integration.

## Coverage and integration decisions

| Handbook chapter | Repository treatment |
| --- | --- |
| 1. Evidence and model/interface map | Dated model/surface reference; distinguish request, product, renderer and conversation model |
| 2. Production operating system | Existing concept/copy gates retained; approved-base and serial-edit checks strengthened |
| 3. Prompt engineering | Concrete spatial/material decisions within the existing single complete prompt |
| 4. Reference engineering | Property authority, age cues, smallest sufficient pack, reference leakage and unseen product limits |
| 5. Editing | One delta, physical dependencies, preserve set, rollback and independent alternatives |
| 6. Artifact diagnosis | New focused reference for observed patterns, original-file limits and retained creative intent |
| 7. Typography, color, print and files | Exact text retained; effective PPI, measured color, actual alpha and production boundaries clarified |
| 8. ChatGPT, Work and Codex | Actual host schema governs; corrected dated feature-eligibility claims |
| 9. Image API | Compact verified control map; full transport runners omitted because native execution remains the Skill's scope |
| 10. Responses API | Submitted versus revised prompt and renderer attribution distinguished; no automatic API pipeline |
| 11. Cost, latency and acceptance | No hardcoded prices or guessed costs; accepted-asset cost requires actual usage and acceptance evidence |
| 12. Benchmark | Retained narrow reported lessons; no model-wide rates, reproduced results or host certification |
| 13. Worked cases | Four adapted poster, identity, product-edit and pixel-art examples; existing card/menu cases retained; no default artwork-only overlay or video scope expansion |
| 14. Troubleshooting and QA | Local defect, target change and protected-property checks; artifact, detail and intent assessed separately |
| 15. Derivation and maintenance | Existing Skill identity and release pipeline retained; no duplicate Skill or full manual import |
| 16. Glossary and sources | Relevant terminology explained where needed; primary sources linked and checked below |

## Primary-source review and corrections

All checks below used official OpenAI pages on 2026-09-09. These are documentation checks, not execution evidence. Changeable facts must be checked again for a later material capability decision.

| Claim | Finding and source |
| --- | --- |
| 2.5 variants and dated snapshots | Confirmed both variants and their 2026-09-08 snapshots. Vendor positioning is not a universal ranking. [Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare), [Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) |
| Product improvements | Launch claims support describing the intended improvements, not guaranteed identity or edit preservation. [Announcement](https://openai.com/index/introducing-chatgpt-images-2-5/) |
| Quality, dimensions and alpha | Confirmed the documented API options and simultaneous dimension constraints. Host exposure still requires its actual schema. [Generation guide](https://developers.openai.com/api/docs/guides/image-generation), [generate endpoint](https://developers.openai.com/api/reference/resources/images/methods/generate) |
| Mask and reference behavior | References have endpoint-specific limits; masks guide rather than guarantee isolation. Detailed transport code is unnecessary for the current native scope. [Edit endpoint](https://developers.openai.com/api/reference/resources/images/methods/edit) |
| Transparency preview wording | The endpoint's preview qualifier applies to GPT Image 2, not a blanket 2.5-family qualifier. Removed that handbook generalization; inspect actual output in either case. [Edit endpoint](https://developers.openai.com/api/reference/resources/images/methods/edit) |
| Images with thinking eligibility | Handbook section 8.1 overstates current Enterprise/Edu availability. Help lists Plus/Pro/Business and says Enterprise/Edu are coming later. Templates are not yet in Work. No universal UI promise is carried into the Skill. [Images in ChatGPT](https://help.openai.com/en/articles/11084440-images-in-chatgpt) |
| Streaming and input fidelity | Model feature badges and endpoint streaming fields disagree; exact 2.5 input-fidelity behavior remains unresolved. Preserve uncertainty, not a fabricated control. [Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare), [edit endpoint](https://developers.openai.com/api/reference/resources/images/methods/edit) |
| Prompt revision | Responses can expose a revised prompt; the submitted prompt remains distinct and absent attribution stays unknown. [Responses image tool](https://developers.openai.com/api/docs/guides/tools-image-generation) |
| Better quality and costing | Compare against actual acceptance criteria when authorized; the GPT Image 2 calculator cannot establish 2.5 consumption. No rates or benchmark conclusions are promoted without supporting evidence. [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting), [Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) |

The native image tool available during development exposes prompt and image-reference inputs, not model, quality, size or mask fields. Its schema is evidence about that session only. No renderer variant was inferred from the tool name or conversation model.

## Verification record

The public source commit is `c778236b9f10e28276b2048fc78b689ac5739376`. Its complete Git tree `0e48fbd56fb2e02b8d7dfea01a7e547fe0d5514a` was verified equal to the tested local source commit `69f67bc705e94f4de039a5d1ed39c35dc66f71e3`. The release helper regenerated both configs against the actual public source, added the verified v0.9.0-rc.2 baseline to the history index and created a pending 55-case host report. Default package validation confirms **28/28** pinned source files and matching working bytes locally. Public refs, raw bytes and CI must additionally pass the post-publication check.

| Check | Observed result | Scope |
| --- | --- | --- |
| Package and release lock | Passed; 28 source files, 13 delta cases, 55 host cases recorded | Exact local source/manifest inventory and hashes; host cases not executed |
| Design contracts | 70 cases and both templates passed | Structured state and transition validation |
| Lifecycle regressions | 13 tests passed | Disposable install/update/proposal and release failure cases |
| Catalog regressions | 11 tests passed | All 200 exact source codes, grouping and helper behavior preserved |
| Creator validation | Passed | Skill structure |
| Source-anchor inventory | Passed; 31 URLs | Offline inventory only; the OpenAI review above is separate from historical link reachability |
| Diff whitespace | Passed | Edited repository text |
| Actual-source update cycle | Passed; no conflicts for clean baseline or tested personal changes | In-memory v0.9.0-rc.2 to candidate proposals and repeat comparison |

The [actual-source cycle record](gpt-image-2-5-source-cycle.json) contains the complete file Delta: **10 changed, 2 new, 0 removed, 16 unchanged**. A clean proposed update equals the complete target and repeats as `already_up_to_date`. A second simulation preserves the personal extension entry, icon and host metadata, and repeats as `local_customizations_preserved`. These simulations never read or write the user's installed Skill and cannot guarantee that an arbitrary personal override will be conflict-free.

New host cases 50–55 cover the added behavior. All actual host cases for the new candidate remain pending until executed in the respective host; historical v0.9.0-rc.2 user-reported save/update and code smoke tests remain in their original report. The independent text-only exercise is recorded separately; it cannot pass the host columns.

The [source-only forward-test record](gpt-image-2-5-forward-test.json) preserves all six raw prompts, actual responses and reported actions. A separate assistant received the candidate Skill sources and raw tasks without conversation history, expected-observable fixtures or these reports. Parent review found all six responses consistent with their text-level observables: native-control boundaries, local material preservation, rejected serial drift, 51.2-PPI calculation and delivery limits, qualified benchmark language, and an integrated English prompt retaining exact Polish text. No image was supplied or generated. The tests exercise instruction use; they do not establish renderer quality or generalize from six responses to all user tasks.

## Publication and remaining metadata

Publication starts from the verified v0.9.0-rc.2 lock `edd761deba7f7f119f998d043b85244e9a0abe63`; the candidate version was absent from fetched remote branches and tags before lock preparation. The owner explicitly approved commit and push. Publish the source-plus-lock history through the existing procedure, then verify public refs, source bytes and exact-commit CI. Preparing this record does not itself establish those post-publication results. Historical release refs remain unchanged.

GitHub's repository metadata was read on 2026-09-09: the About description remains unset. Its intended English text is already in CONTRIBUTING.md. The available GitHub connection has no repository-metadata write operation, so this pending request was not represented as completed by a README change.
