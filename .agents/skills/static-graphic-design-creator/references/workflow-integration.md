# Workflow Integration Contract

This package is self-contained. It can exchange structured information with any existing workflow without requiring that workflow to expose a particular skill name, filesystem layout, connector, or proprietary schema.

## Standalone mode

Accept natural-language input. Derive only what the user supplied or what can be safely treated as a reversible assumption. Mark unresolved generator-sensitive capability as `Unknown`.

## Connected mode

Accept either `workflow_context` or individual fields:

```yaml
brief_contract:
  objective:
  audience:
  deliverable:
  constraints: []
direction_contract:
  visual_thesis:
  attention_order: []
  layout_mechanism:
  type_image_relationship:
poster_strategy:
  collaboration_mode: directed_collaboration
  communication_goal:
  required_audience_response:
  reading_mode: Unknown
  text_hierarchy:
    must_read: []
    should_read: []
    metadata: []
    decoration: []
  composition_archetype:
  image_type:
  type_role:
  style_family:
  transferable_attributes: []
  material_treatment:
  production_process: Unknown
  intentional_legibility_friction: Unknown
  human_review_required: []
copy_pack:
  locked_strings: []
reference_pack:
  references: []
asset_manifest:
  approved_assets: []
qa_requirements:
  acceptance_criteria: []
target_generator_profile:
  surface:
  verified_controls: []
host_environment: Unknown
execution_surface: Unknown
generator_provider: Unknown
target_generator: Unknown
final_asset_has_visible_text: Unknown
input_context: connected
output_mode: prompt
native_generation_available: Unknown
production_intent: concept_raster
```

Preserve an upstream value when it is more specific than the brief. Do not rewrite approved copy, source authority, brand constraints, or suppression rules. If contracts conflict, surface the conflict before authoring a prompt.

When `poster_strategy` is supplied, preserve its resolved communication goal and composition archetype. A supplied style family remains subordinate to those fields; if it conflicts with copy feasibility or the stated objective, explain the conflict and request a choice rather than silently replacing the style or the strategy.

## Optional Codex text-bearing static compatibility profile

This profile is selected only when connected context explicitly declares:

```yaml
host_environment: codex
execution_surface: codex_builtin_imagegen
generator_provider: openai
final_asset_has_visible_text: true
target_generator: gpt-image-2
```

It is a prompt-format handoff, not permission to render, upload, call an API, or select a paid service. When `output_mode` is explicitly `render` or `render_and_prompt`, Codex may invoke `$imagegen` only if that built-in Skill is available. In this profile:

- keep the explicitly declared `execution_surface: codex_builtin_imagegen`, `generator_provider: openai`, and `target_generator: gpt-image-2`;
- set `task_mode` from the request and `negative_handling_mode: integrated_constraints`;
- place short, concrete constraints inside the one main prompt; do not return a separate `Negative Prompt` or `negative_prompt` field;
- place every final visible string in the one prompt and do not reserve a later text overlay;
- name only references attached to the same request and their declared roles.

The public eight-stage contract remains canonical. A receiving Codex workflow that uses a six-section static contract maps it as follows:

| Public semantic stage | Codex six-section placement |
| --- | --- |
| 1. Final-output contract | Final-output contract |
| 2. Background and spatial foundation + 3. Layout architecture and attention flow | Background and spatial foundation |
| 4. Hero and protected source assets | Hero and source-locked assets |
| 5. Supporting graphic elements | Supporting graphic elements |
| 6. Typography and functional information | Typography and functional information |
| 7. Colour, light, and material integration | Integrate into the relevant background, hero, supporting, and typography sections without adding a second prompt |
| 8. Finish, exclusions, and acceptance checks | Finish and exclusions |

When a named target surface, its current behavior, or its supported controls are uncertain, set `source_check_status: required_not_done` and keep generator-specific controls `Unknown`. A provider-neutral prompt with no named target may use `source_check_status: not_required`. Do not infer a Codex profile from a product name or host environment alone.

## Portable handoff

Return this minimum payload when another workflow will render or review the result:

```yaml
prompt_pack:
  prompt_delivery_form: unified-multistage-static
  input_context: connected
  output_mode: prompt
  rendering_route:
    native_generation_requested: false
    native_generation_available: Unknown
    render_status: not_requested
    qa_route: not_applicable
  task_mode:
  production_intent: concept_raster
  rendering_context:
    host_environment: Unknown
    execution_surface: Unknown
    generator_provider: Unknown
    target_generator: Unknown
    final_asset_has_visible_text: Unknown
  generator_prompt_format:
    negative_handling_mode: unknown
    source_check_status: not_required
    separate_negative_prompt_allowed: Unknown
  native_settings:
  prompt:
  reference_roles: []
  required_request_references: []
  poster_strategy:
    communication_goal:
    reading_mode: Unknown
    text_hierarchy:
      must_read: []
      should_read: []
      metadata: []
      decoration: []
    composition_archetype:
    image_type:
    type_role:
    style_family:
    material_treatment:
    production_process: Unknown
    intentional_legibility_friction: Unknown
    human_review_required: []
  copy_locks: []
  copy_feasibility:
  brand_identity_policy:
  protected_elements: []
  expected_observables: []
  acceptance_criteria: []
  unknown_capabilities: []
  repair_route:
```

Do not automatically call a renderer, reviewer, publisher, or external service. A receiving workflow may use its built-in image-generation capability only when the user explicitly requested `render` or `render_and_prompt`; otherwise it returns the prompt handoff only. It never substitutes an external service when native rendering is unavailable, blocked by DTP, or fails.
