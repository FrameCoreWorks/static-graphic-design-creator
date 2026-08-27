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
```

Preserve an upstream value when it is more specific than the brief. Do not rewrite approved copy, source authority, brand constraints, or suppression rules. If contracts conflict, surface the conflict before authoring a prompt.

## Portable handoff

Return this minimum payload when another workflow will render or review the result:

```yaml
prompt_pack:
  prompt_delivery_form: unified-multistage-static
  task_mode:
  native_settings:
  prompt:
  reference_roles: []
  copy_locks: []
  protected_elements: []
  expected_observables: []
  acceptance_criteria: []
  unknown_capabilities: []
  repair_route:
```

Do not automatically call a renderer, reviewer, publisher, or external service. A receiving workflow decides whether and how to execute the handoff.
