# Static Design Prompt Pack

This fictional, valid prompt-only example demonstrates [the canonical state](../references/design-contract.schema.json). Replace its facts with the supplied brief; never reuse example wording automatically. The native model and controls are Unknown. A real render requires an authorized state transition and observed QA.

```yaml
schema_version: 1
activation: explicit
request_kind: design
action: return_prompt
input_context: standalone
task_mode: generate
output_mode: prompt
production_intent: concept_raster
strategy:
  objective: Announce the supplied title clearly
  audience: Readers of this announcement
  response: Read the title
  output_format: square digital concept
  reading_mode: glance
  visual_thesis: The single title is the complete visual event
  attention_order:
  - Title
  composition: typographic_engine
  type_image_relationship: Type is the image
  style_requests: []
  primary_language: reduced typographic composition
  secondary_treatments: []
  intentional_hybrid: false
  material_treatment: flat field
concept:
  status: locked
  lock:
    premise: Supplied one-word announcement
    mechanism: One word with protected surrounding space
    distinctive_hook: The entire composition is the title
    allowed_adaptations:
    - Optical spacing
    forbidden_substitutions:
    - Additional imagery or copy
copy:
  route: locked_copy
  selection_status: locked
  message_thesis: The supplied title is the announcement
  items:
  - id: title
    text: CZYTAJ
    language: pl
    role: must_read
    required: true
    authority: user_locked
    source: Fictional example brief supplies this final title
    line_breaks: []
    allowed_changes: layout_only
  options: []
  claims: []
feasibility:
  status: compact
  reason: One word in a high-contrast field
  review_plan:
  - Inspect exact spelling and spacing if rendered
reference_status: none
references: []
host:
  surface: Unknown
  native_generation_available: Unknown
  model: Unknown
  controls: []
prompt: 'Create one flat square digital concept graphic. The supplied title is the complete visual event. Use a
  warm off-white field and generous negative space; center one large black typographic anchor with optical spacing
  and wide margins. The word itself is the hero; add no image or supporting ornament. Render exactly one visible
  string: “CZYTAJ”, in a substantial upright sans-serif treatment on one line. Use flat colour without material
  effects. Accept only the exact word, the clear title-first hierarchy and intact surrounding space; no other text,
  logo, mockup or variants.'
render_status: not_requested
qa:
  status: not_run
  critical_failures: []
  checks: []
```
