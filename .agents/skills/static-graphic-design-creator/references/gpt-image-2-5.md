# GPT Image 2.5: Surface, Prompt and Edit Decisions

Read when the user names GPT Image 2.5, asks about its controls, or needs a model-specific production decision. Keep ordinary design work provider-neutral. This reference supplements the [capability contract](capability-and-reference-contract.md); it does not authorize API calls, switch the host's model or require a technical intake.

## Evidence and attribution

Official documentation was checked on **2026-09-09**. Recheck changeable availability and settings before making a current capability claim. The supplied *GPT Image 2.5 Master Knowledge Base*, release 1.0, informed the operational guidance. Its benchmark images, logs and companion manifest were not supplied for this integration. Treat its numerical results as handbook-reported observations, not independently reproduced Skill tests or general model guarantees.

| Layer | What can be established | What remains separate |
| --- | --- | --- |
| API image model | Requested alias or dated snapshot in a supported request | Independently returned model attribution; leave absent fields `Unknown` |
| ChatGPT Images 2.5 | A product feature identified by that interface | Exact Flare/Sunburst backend, API settings and account eligibility |
| Conversation model | The assistant handling the request | The renderer that produces the pixels |
| Work or Codex tool | Its actual schema, attached inputs and returned result | Capabilities advertised for another surface |

Official model pages identify `gpt-image-2.5-flare` and `gpt-image-2.5-flare-2026-09-08`, and `gpt-image-2.5-sunburst` and `gpt-image-2.5-sunburst-2026-09-08`. Flare is positioned for faster everyday work; Sunburst for more precision with a latency tradeoff. These are vendor positions, not universal task rankings. Requested snapshots improve experiment traceability but do not promise identical pixels. [Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare), [Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst).

The launch describes improved likeness, local edits and iterative consistency; all still need result inspection. Do not infer a native variant from speed or appearance. [Launch announcement](https://openai.com/index/introducing-chatgpt-images-2-5/).

## Use the controls that actually exist

The following is a **dated API reference**, not the parameter set of the active native tool. Apply supported native fields only where the current schema exposes them. Otherwise describe visual intent in prose and report an unavailable exact control only when it affects the task.

| API field | Documented 2.5 values or constraints | Practical implication |
| --- | --- | --- |
| `quality` | `auto`, `low`, `medium`, `high`, `xhigh`, `max` | Higher settings are not proof of better fidelity or accepted output |
| `size` | `auto` or `WIDTHxHEIGHT`; both axes divisible by 16; each at most 3840; longest/shortest at most 3; total 655,360–8,294,400 pixels | Check all constraints together; above 3,686,400 pixels is experimental |
| `background`, `output_format` | Transparency with `transparent` and PNG/WebP | Inspect the returned alpha and edges; JPEG cannot retain alpha |
| Edit references | Up to 16 API inputs; JSON `images` objects or multipart `image` transport | A native host may allow fewer or expose a different attachment mechanism |

Sources: [image generation guide](https://developers.openai.com/api/docs/guides/image-generation), [edit endpoint](https://developers.openai.com/api/reference/resources/images/methods/edit). Exact character, file and transport limits belong to the active endpoint documentation when preparing an explicitly requested API handoff; they are not prompt instructions.

Do not invent seeds, CFG, samplers, denoising strength, numeric reference weights, hard face locks or a separate negative-prompt field. The exact 2.5 behavior of `input_fidelity` is unresolved in the reviewed documentation; do not import the older-model rule as a 2.5 guarantee. Endpoint streaming fields and model-page streaming badges disagree; record that conflict if streaming is relevant instead of promising it. No such controls are needed for a normal native prompt.

Responses API may rewrite instructions and expose `image_generation_call.revised_prompt`. Keep the user's brief, the actual submitted prompt and any returned revision distinct; do not reconstruct a missing field or call a guessed revision the submitted prompt. This does not change the Skill's obligation to return the exact submitted text when requested. [Responses image tool](https://developers.openai.com/api/docs/guides/tools-image-generation).

At the check date, general ChatGPT image access and Images with thinking have different eligibility: the Help article lists thinking for Plus, Pro and Business, with Enterprise/Edu coming later. Templates are not yet supported in Work. Neither product access nor a launch announcement proves a native Skill or particular editing UI is available in the current workspace. Use actual host evidence; recheck availability when needed. [Images in ChatGPT](https://help.openai.com/en/articles/11084440-images-in-chatgpt).

## Build a useful visual specification

Keep the existing [unified prompt](unified-static-prompt-contract.md) and exact-copy gates. GPT Image 2.5 does not require a new prompt format, mandatory English, a long exclusion list or a text-free intermediate. Specify only decisions that affect the requested graphic:

- Anchor left/right to the viewer or subject, and identify the actual hand, object or contact point when ambiguous. Camera/lens language describes appearance unless verified as a control.
- Assign each reference authority over identity, product construction, pose, light or style. A tight face crop can clarify facial geometry and apparent age; a wider view can govern body, hair or garment. Use the smallest sufficient pack and retain the original when making a useful crop. Unseen product surfaces stay unknown.
- State where each material occurs and how its texture should behave at the intended scale. Keep intentional halftone, grain, pixel clusters and patterned cloth when they serve the concept. A generic ban on texture destroys legitimate style cues, including catalog directions.
- Include all locked visible text in the one finished graphic. Do not move copy to a future overlay merely because a handbook example does. Real editable type, exact machine-readable codes and print masters follow the existing feasibility route.

The official prompting guide encourages concrete task and reference decisions rather than relying on a quality setting alone. [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting).

## Edit from an approved base

Use one named base, one permitted delta and an explicit preserve set. If the change physically requires a related shadow, reflection or occlusion change, include that relation in the scope; clarify only a real conflict with the user's locks. A selection or mask is guidance, not proof that surrounding pixels stay fixed. With a supported API mask route, place the edit source first and follow that endpoint's alpha, dimension and format requirements. Do not simulate a mask parameter in native prose. [Mask guidance](https://developers.openai.com/api/docs/guides/image-generation#edit-an-image-using-a-mask).

After an authorized edit, compare the target and protected properties with both the immediately preceding image and the original approved base. Check apparent age separately from general likeness, and product topology separately from attractive lighting. Branch independent alternatives from the same approved base. Reject a local success if protected face, text, garment or material has drifted; retain a rollback point rather than making the damaged result the next base. There is no supported universal edit-count limit or magic context-reset command.

For unwanted repetition, material collapse or smoothing, use [material artifact diagnosis](material-artifact-diagnosis.md). A fresh conversation can be an explicitly scoped experiment when context is the suspected variable, not an automatic cure or permission for another generation.

## Interpret quality, benchmarks and cost narrowly

The handbook reports small screening cells, serial-edit drift and a masked scarf task whose preservation criteria failed at both tested Flare quality levels. Those reports motivate checking the preserve set; they do not establish a failure rate for either variant or prove that `max` always helps or never helps. Original files would be needed to audit those claims. Two reviews by the same assistant are not independent human evaluations.

Only propose model/quality comparisons when they answer a real unresolved requirement and the user authorizes the extra work. Hold source bytes, prompt, dimensions and acceptance criteria fixed; retain failed attempts and actual outputs. A pass requires all critical criteria, not just the requested color change or lower artifact visibility. Track actual reported usage and missing fields honestly if cost is requested. Cost per accepted asset includes failed attempts and repair effort; leave it unknown when cost or acceptance evidence is missing. Do not use the GPT Image 2 calculator to estimate 2.5 consumption. No benchmark or paid retry runs automatically.
