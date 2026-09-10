# Static Design Intake

For explicit separate-assets work, use the [layer plan](layer-plan.json) and [layered workflow](../references/layered-assets-workflow.md). This single-asset state describes the current raster operation; retain the complete project copy, sequence and approved file versions in the separate plan. Ordinary integrated graphics use this template unchanged.

Collect an ordinary brief without a mandatory code question or catalog step. For a user-selected code, put its canonical line in `strategy.style_requests`. For automatic selection, keep the entry and visibility preference in internal lookup context and populate only its interpreted strategy attributes; do not invent a user style request. Follow [code selection and rebuild](../references/event-poster-code-workflow.md), including hidden-code preference and full catalog opt-out. `/codes` browsing, including localized aliases, does not require this intake.

Use internally for complex work. This valid starting state records unresolved decisions; it is not a mandatory form. Populate from supplied evidence, preserve prior answers, and select the action appropriate to the request. Empty fields do not approve facts, copy or capabilities. See [workflow integration](../references/workflow-integration.md).

When a specific model is requested, retain that request separately from observed host attribution; `host.model` stays `Unknown` without surface evidence. For reference work, record property authority, apparent-age or product-construction locks where relevant, and the approved edit base. Do not add a compulsory API/model questionnaire to an ordinary brief.

```yaml
schema_version: 1
activation: explicit
request_kind: design
action: clarify
input_context: standalone
task_mode: generate
output_mode: none
production_intent: concept_raster
strategy:
  objective: ''
  audience: ''
  response: ''
  output_format: ''
  reading_mode: Unknown
  visual_thesis: ''
  attention_order: []
  composition: ''
  type_image_relationship: ''
  style_requests: []
  primary_language: ''
  secondary_treatments: []
  intentional_hybrid: false
  material_treatment: ''
concept:
  status: needs_selection
  lock: null
copy:
  route: copy_discovery
  selection_status: draft
  message_thesis: ''
  items: []
  options: []
  claims: []
feasibility:
  status: not_assessed
  reason: ''
  review_plan: []
reference_status: none
references: []
host:
  surface: Unknown
  native_generation_available: Unknown
  model: Unknown
  controls: []
prompt: ''
render_status: not_requested
qa:
  status: not_run
  critical_failures: []
  checks: []
```
