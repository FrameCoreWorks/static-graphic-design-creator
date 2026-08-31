#!/usr/bin/env python3
"""Local structural and contract validation for the standalone skill."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "static-graphic-design-creator"
SOURCE_MANIFEST = ROOT / "config" / "chatgpt-skill-sources.json"
POLICY_FIXTURES = ROOT / "tests" / "fixtures" / "policy-regression-cases.json"
BEHAVIOR_FIXTURES = ROOT / "tests" / "fixtures" / "behavior-eval-cases.json"
POSTER_STRATEGY_FIXTURES = ROOT / "tests" / "fixtures" / "poster-strategy-eval-cases.json"
POSTER_RESEARCH_FIXTURES = ROOT / "tests" / "fixtures" / "poster-research-eval-cases.json"
UPDATE_FIXTURES = ROOT / "tests" / "fixtures" / "update-eval-cases.json"
MANUAL_EVALUATION = ROOT / "EVALUATION.md"
CHATGPT_UPDATE = ROOT / "CHATGPT_UPDATE.md"
CODEX_UPDATE = ROOT / "CODEX_UPDATE.md"
SOURCE_RELEASE = SKILL / "references" / "source-release.json"
SECURITY = ROOT / "SECURITY.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"
HOST_EVALUATION = ROOT / "reports" / "host-evaluations" / "v0.7.0-rc.2.md"
SOURCE_ANCHOR_CHECKER = ROOT / "tests" / "check_source_anchors.py"
SOURCE_ANCHOR_WORKFLOW = ROOT / ".github" / "workflows" / "reference-links.yml"
PRODUCTION_WALKTHROUGHS = SKILL / "references" / "production-walkthroughs.md"
COPY_DEVELOPMENT = SKILL / "references" / "copy-development-and-human-voice.md"

OUTPUT_MODES = {"prompt", "render", "render_and_prompt"}
RENDER_STATUSES = {
    "not_requested",
    "blocked_dtp",
    "unavailable",
    "generated",
    "qa_pass",
    "qa_fail",
    "generation_failed",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_policy_fixtures() -> None:
    fixtures = json.loads(read(POLICY_FIXTURES))
    require(fixtures["schema_version"] == 1, "Unexpected policy fixture schema")
    require(fixtures["cases"], "Policy fixture cases are required")
    for case in fixtures["cases"]:
        document = ROOT / case["document"]
        require(document.is_file(), f"Fixture document is missing: {case['document']}")
        content = read(document)
        for required_term in case["required_terms"]:
            require(
                required_term in content,
                f"Policy regression {case['id']} is missing: {required_term}",
            )


def resolve_behavior_case(signals: dict[str, object]) -> dict[str, object]:
    """Reference decision model for release regression cases.

    This deliberately covers only deterministic routing decisions. Visual quality
    remains a manual forward-test concern because it requires a real host render.
    """

    clarity = signals["request_clarity"]
    requested_output = signals["requested_output"]
    native_available = signals["native_generation_available"]
    production_intent = signals["production_intent"]
    copy_feasibility = signals["copy_feasibility"]
    reference_conflict = signals["reference_conflict"]

    if reference_conflict:
        return {
            "response_action": "clarify_reference_conflict",
            "output_mode": None,
            "render_status": "not_requested",
        }
    if clarity == "ambiguous":
        return {
            "response_action": "clarify_output_mode",
            "output_mode": None,
            "render_status": "not_requested",
        }
    if production_intent == "production_master" or copy_feasibility == "dtp_required":
        return {
            "response_action": "route_dtp",
            "output_mode": requested_output,
            "render_status": "blocked_dtp",
        }
    if requested_output == "prompt":
        return {
            "response_action": "return_prompt",
            "output_mode": "prompt",
            "render_status": "not_requested",
        }
    if native_available is True:
        return {
            "response_action": "native_render_then_review",
            "output_mode": requested_output,
            "render_status": "generated",
        }
    return {
        "response_action": "return_prompt_fallback",
        "output_mode": requested_output,
        "render_status": "unavailable",
    }


def validate_behavior_fixtures() -> None:
    fixtures = json.loads(read(BEHAVIOR_FIXTURES))
    require(fixtures["schema_version"] == 1, "Unexpected behavior fixture schema")
    require(fixtures["cases"], "Behavior fixture cases are required")
    required_signal_keys = {
        "request_clarity",
        "requested_output",
        "native_generation_available",
        "production_intent",
        "copy_feasibility",
        "reference_conflict",
    }
    for case in fixtures["cases"]:
        signals = case["signals"]
        expected = case["expected"]
        require(required_signal_keys == set(signals), f"Unexpected signals in {case['id']}")
        require(signals["requested_output"] in OUTPUT_MODES, f"Invalid output mode in {case['id']}")
        require(expected["render_status"] in RENDER_STATUSES, f"Invalid render status in {case['id']}")
        require(
            resolve_behavior_case(signals) == expected,
            f"Behavior regression mismatch: {case['id']}",
        )


def resolve_poster_strategy_case(signals: dict[str, object]) -> dict[str, object]:
    """Reference decision model for objective-first poster direction."""

    direction_status = signals["direction_status"]
    copy_feasibility = signals["copy_feasibility"]
    style_reference_type = signals["style_reference_type"]

    if copy_feasibility == "dtp_required":
        interaction_mode = "route_dtp_before_brainstorm"
    elif direction_status == "open":
        interaction_mode = "discovery_brainstorm"
    else:
        interaction_mode = "directed_collaboration"

    return {
        "interaction_mode": interaction_mode,
        "goal_first": True,
        "composition_before_style": True,
        "direct_imitation": False,
        "style_translation_required": style_reference_type == "named_artist",
    }


def validate_poster_strategy_fixtures() -> None:
    fixtures = json.loads(read(POSTER_STRATEGY_FIXTURES))
    require(fixtures["schema_version"] == 1, "Unexpected poster strategy fixture schema")
    require(fixtures["cases"], "Poster strategy fixture cases are required")
    required_signal_keys = {
        "direction_status",
        "user_style_position",
        "copy_feasibility",
        "style_reference_type",
    }
    for case in fixtures["cases"]:
        signals = case["signals"]
        require(required_signal_keys == set(signals), f"Unexpected poster strategy signals in {case['id']}")
        require(
            resolve_poster_strategy_case(signals) == case["expected"],
            f"Poster strategy regression mismatch: {case['id']}",
        )


def resolve_poster_research_case(signals: dict[str, object]) -> dict[str, object]:
    """Reference routing for evidence-backed poster-language decisions."""

    if signals["charged_content"] and not signals["human_review_confirmed"]:
        decision_route = "clarify_human_review"
    elif (
        signals["production_intent"] == "production_master"
        or signals["must_read_density"] == "dense"
    ):
        decision_route = "route_dtp"
    elif (
        signals["historical_language"] == "psychedelic"
        and signals["reading_mode"] == "glance"
        and not signals["intentional_legibility_friction_confirmed"]
    ):
        decision_route = "clarify_legibility_intent"
    else:
        decision_route = "strategy_ready"

    return {
        "decision_route": decision_route,
        "goal_first": True,
        "copy_hierarchy_required": True,
        "composition_before_style": True,
        "process_logic_required": True,
        "direct_imitation": False,
    }


def validate_poster_research_fixtures() -> None:
    fixtures = json.loads(read(POSTER_RESEARCH_FIXTURES))
    require(fixtures["schema_version"] == 1, "Unexpected poster research fixture schema")
    require(fixtures["cases"], "Poster research fixture cases are required")
    required_signal_keys = {
        "asset_function",
        "reading_mode",
        "must_read_density",
        "historical_language",
        "charged_content",
        "human_review_confirmed",
        "intentional_legibility_friction_confirmed",
        "production_intent",
    }
    for case in fixtures["cases"]:
        signals = case["signals"]
        require(
            required_signal_keys == set(signals),
            f"Unexpected poster research signals in {case['id']}",
        )
        require(
            resolve_poster_research_case(signals) == case["expected"],
            f"Poster research regression mismatch: {case['id']}",
        )


def resolve_update_case(signals: dict[str, object]) -> dict[str, object]:
    """Reference decision model for user-approved incremental updates."""

    source_identity = signals["source_identity"]
    target_integrity = signals["target_integrity"]
    comparison_mode = signals["comparison_mode"]
    delta = signals["delta"]
    local_conflict = signals["local_conflict"]
    origin_confirmation = signals["origin_confirmation"]
    user_approval = signals["user_approval"]

    if source_identity == "mismatch":
        return {
            "update_status": "blocked_source_identity",
            "apply_mode": "none",
            "requires_approval": False,
        }
    if target_integrity == "mismatch":
        return {
            "update_status": "blocked_integrity",
            "apply_mode": "none",
            "requires_approval": False,
        }
    if source_identity == "unrecorded" and not origin_confirmation:
        return {
            "update_status": "awaiting_origin_confirmation",
            "apply_mode": "none",
            "requires_approval": True,
        }
    if local_conflict:
        return {
            "update_status": "blocked_local_conflict",
            "apply_mode": "none",
            "requires_approval": False,
        }
    if delta == "none":
        return {
            "update_status": "already_up_to_date",
            "apply_mode": "none",
            "requires_approval": False,
        }
    if not user_approval:
        return {
            "update_status": "update_review_ready",
            "apply_mode": "none",
            "requires_approval": True,
        }
    return {
        "update_status": "ready_for_update",
        "apply_mode": (
            "selective_file_update"
            if comparison_mode == "file_level"
            else "declared_bundle_replacement"
        ),
        "requires_approval": False,
    }


def validate_update_fixtures() -> None:
    fixtures = json.loads(read(UPDATE_FIXTURES))
    require(fixtures["schema_version"] == 1, "Unexpected update fixture schema")
    require(fixtures["cases"], "Update fixture cases are required")
    required_signal_keys = {
        "source_identity",
        "target_integrity",
        "comparison_mode",
        "delta",
        "local_conflict",
        "origin_confirmation",
        "user_approval",
    }
    for case in fixtures["cases"]:
        signals = case["signals"]
        require(required_signal_keys == set(signals), f"Unexpected update signals in {case['id']}")
        require(
            resolve_update_case(signals) == case["expected"],
            f"Update regression mismatch: {case['id']}",
        )


def main() -> None:
    required_paths = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHATGPT_INSTALL.md",
        ROOT / "CODEX_INSTALL.md",
        CHATGPT_UPDATE,
        CODEX_UPDATE,
        ROOT / "CHANGELOG.md",
        SECURITY,
        CONTRIBUTING,
        HOST_EVALUATION,
        ROOT / ".github" / "workflows" / "validate.yml",
        SOURCE_ANCHOR_WORKFLOW,
        ROOT / "config" / "chatgpt-skills.json",
        SOURCE_MANIFEST,
        SOURCE_ANCHOR_CHECKER,
        POLICY_FIXTURES,
        BEHAVIOR_FIXTURES,
        POSTER_STRATEGY_FIXTURES,
        POSTER_RESEARCH_FIXTURES,
        UPDATE_FIXTURES,
        MANUAL_EVALUATION,
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "unified-static-prompt-contract.md",
        SKILL / "references" / "capability-and-reference-contract.md",
        SKILL / "references" / "workflow-integration.md",
        COPY_DEVELOPMENT,
        SKILL / "references" / "qa-and-repair.md",
        SKILL / "references" / "deliverable-profiles.md",
        SKILL / "references" / "poster-style-and-composition-atlas.md",
        SKILL / "references" / "poster-style-translation-catalog.md",
        PRODUCTION_WALKTHROUGHS,
        SKILL / "references" / "poster-movements-and-production-atlas.md",
        SOURCE_RELEASE,
        SKILL / "templates" / "design-intake.md",
        SKILL / "templates" / "prompt-pack.md",
    ]
    for path in required_paths:
        require(path.is_file(), f"Missing required file: {path.relative_to(ROOT)}")

    retired_non_skill_paths = [
        ROOT / ".agents" / "plugins" / "marketplace.json",
        ROOT / "plugins" / "static-design-prompt-architect" / ".codex-plugin" / "plugin.json",
        ROOT / "plugins" / "static-graphic-design-creator" / ".codex-plugin" / "plugin.json",
        ROOT / "submission" / "openai-plugin-directory.md",
    ]
    for path in retired_non_skill_paths:
        require(not path.exists(), f"Standalone skill must not include a retired non-Skill artifact: {path.relative_to(ROOT)}")

    require(not (ROOT / "skills").exists(), "Canonical source must use .agents/skills only")
    validate_policy_fixtures()
    validate_behavior_fixtures()
    validate_poster_strategy_fixtures()
    validate_poster_research_fixtures()
    validate_update_fixtures()

    skill = read(SKILL / "SKILL.md")
    require(skill.startswith("---\nname: static-graphic-design-creator\n"), "SKILL.md frontmatter missing")
    for section in ["## Input contexts", "Standalone mode", "Connected mode", "## Output modes", "## Inputs", "## Output", "## Final self-check"]:
        require(section in skill, f"Skill lacks required workflow boundary: {section}")
    require("never ask for intermediate images" in skill.lower(), "Single-generation constraint missing")
    require("## Output modes" in skill, "Output-mode routing missing")
    require("**`render`:**" in skill, "Native render route missing")
    require("**`prompt`:**" in skill, "Prompt-only route missing")
    require("**`render_and_prompt`:**" in skill, "Combined output route missing")
    require("active surface's built-in image-generation capability" in skill, "Native-render boundary missing")
    require("$imagegen" in skill, "Codex native image route missing")
    require("Never trigger a render from an ambiguous brief alone" in skill, "Ambiguous render guard missing")
    require("copy-feasibility preflight" in skill, "Copy-feasibility gate missing")
    require("production_intent" in skill, "Production-intent gate missing")
    require("likeness authority" in skill, "Likeness-authority gate missing")
    require("Compress irrelevant stages" in skill, "Prompt compactness rule missing")
    require("host_environment: codex" in skill, "Codex compatibility entry condition missing")
    require("execution_surface: codex_builtin_imagegen" in skill, "Codex execution surface missing")
    require("target_generator: gpt-image-2" in skill, "Explicit Codex target generator missing")
    require("## Poster direction and collaboration" in skill, "Poster collaboration routing missing")
    require(
        "communication goal → audience response → reading mode and copy burden" in skill,
        "Objective-first order missing",
    )
    require("`discovery_brainstorm`" in skill, "Poster brainstorm route missing")
    require("`directed_collaboration`" in skill, "Directed poster collaboration route missing")
    for render_status in RENDER_STATUSES:
        require(render_status in skill, f"Skill lacks render status: {render_status}")

    contract = read(SKILL / "references" / "unified-static-prompt-contract.md")
    for stage in range(1, 9):
        require(f"{stage}. **" in contract, f"Missing stage {stage} in unified contract")
    require("one final raster-design instruction" in contract, "Contract must define one final output")
    require("## Prompt compactness" in contract, "Prompt compactness contract missing")
    require("## Objective-first preflight" in contract, "Objective-first prompt preflight missing")

    integration = read(SKILL / "references" / "workflow-integration.md")
    for field in ["brief_contract", "direction_contract", "copy_pack", "reference_pack", "prompt_pack"]:
        require(field in integration, f"Portable workflow field missing: {field}")
    require("Do not automatically call a renderer" in integration, "Integration must not execute work")
    require("explicitly requested `render` or `render_and_prompt`" in integration, "Integration native-render guard missing")
    require("execution_surface: codex_builtin_imagegen" in integration, "Codex execution profile missing")
    require("generator_provider: openai" in integration, "Codex provider profile missing")
    require("target_generator: gpt-image-2" in integration, "Codex target profile missing")
    require("$imagegen" in integration, "Codex built-in image route missing")
    require("negative_handling_mode: integrated_constraints" in integration, "Codex constraint mode missing")
    require("The public eight-stage contract remains canonical" in integration, "Eight-to-six stage crosswalk missing")
    require("separate `Negative Prompt` or `negative_prompt`" in integration, "Negative-prompt boundary missing")
    require("host environment alone" in integration, "Explicit Codex target guard missing")
    require("production_intent" in integration, "Workflow production intent missing")
    require("text_hierarchy" in integration, "Workflow text-hierarchy handoff missing")
    require("production_process" in integration, "Workflow process handoff missing")
    require("human_review_required" in integration, "Workflow human-review handoff missing")

    chatgpt_install = read(ROOT / "CHATGPT_INSTALL.md")
    for phrase in ["@skill-creator", "one native ChatGPT Skill", "repository-assisted native Skill-creation flow", "config/chatgpt-skill-sources.json"]:
        require(phrase in chatgpt_install, f"ChatGPT installation contract missing: {phrase}")
    require("When the Work host can compute SHA-256" in chatgpt_install, "ChatGPT conditional hash verification missing")
    require("hash_verification: declared_unverified" in chatgpt_install, "ChatGPT hash-unavailable status missing")
    require("reread fresh bootstrap manifests" in chatgpt_install, "ChatGPT hash mismatch recovery missing")
    require("## First response and approval" in chatgpt_install, "ChatGPT onboarding contract missing")
    require("What it gives:" in chatgpt_install, "ChatGPT onboarding value missing")
    require("Before reading source files" in chatgpt_install, "ChatGPT onboarding ordering missing")
    require("native Skill-creation flow" in chatgpt_install, "ChatGPT native creation route missing")
    require("Do not simulate installation" in chatgpt_install, "ChatGPT host-availability guard missing")
    require("repository_path" in chatgpt_install, "ChatGPT repository-to-bundle mapping missing")
    require("relative `path`" in chatgpt_install, "ChatGPT relative bundle path missing")
    require("Immediately use the already active `@skill-creator`" in chatgpt_install, "ChatGPT create-and-save handoff missing")
    require("source_resolved` is not a terminal state" in chatgpt_install, "ChatGPT source-resolution continuation missing")
    require("managed-personal-Skills save flow" in chatgpt_install, "ChatGPT native managed save route missing")
    require("only after the actual native save was attempted" in chatgpt_install, "ChatGPT must attempt a native save before created-not-installed")
    require("plugin" not in chatgpt_install.lower(), "ChatGPT installation prompt must stay native-Skill-only")
    require("follow `CHATGPT_UPDATE.md`" in chatgpt_install, "ChatGPT update handoff missing")
    require("user's language" in chatgpt_install, "ChatGPT language-adaptive onboarding missing")
    require("immutable_source_commit" in chatgpt_install, "ChatGPT immutable-source resolution missing")
    readme = read(ROOT / "README.md")
    require("Native Skills must be available" in readme, "README Skill-availability disclosure missing")
    require("$skill-installer" in readme, "README Codex fresh-install mechanism missing")
    require("immutable source commit" in readme, "README immutable-source disclosure missing")
    require("declared_unverified" in readme, "README unverified-hash disclosure missing")
    require("2026-08-29" in readme, "README OpenAI verification date missing")
    require("assets/static-graphic-design-creator-banner.webp" in readme, "README must use WebP banner")

    chatgpt_config = json.loads(read(ROOT / "config" / "chatgpt-skills.json"))
    require(chatgpt_config["schema_version"] == 6, "Unexpected ChatGPT setup schema")
    require(chatgpt_config["version"] == "0.7.0-rc.1", "Unexpected release version")
    require(chatgpt_config["mode"] == "repository-source", "ChatGPT repository-source mode missing")
    require(chatgpt_config["release"]["channel"] == "candidate", "ChatGPT release channel missing")
    require(chatgpt_config["release"]["source_ref_type"] == "immutable_git_commit", "ChatGPT release ref type missing")
    require(
        re.fullmatch(r"[0-9a-f]{40}", chatgpt_config["release"]["immutable_source_commit"]) is not None,
        "ChatGPT immutable source commit missing",
    )
    require("discovery_trust_boundary" in chatgpt_config["bootstrap"], "ChatGPT bootstrap trust disclosure missing")
    require(chatgpt_config["surface"] == "native-chatgpt-skills", "ChatGPT surface missing")
    native_creation = chatgpt_config["native_creation"]
    require(native_creation["creator_invocation"] == "@skill-creator", "ChatGPT creator invocation missing")
    require(native_creation["surface"] == "chatgpt_work", "ChatGPT Work creation surface missing")
    require(native_creation["tool_discovery_required"] is False, "ChatGPT must not discover a separate tool")
    require(native_creation["capability_preflight_required"] is False, "ChatGPT must not preflight creation capability")
    native_save = chatgpt_config["native_save"]
    require(native_save["required"] is True, "ChatGPT native save must be required")
    require(native_save["workflow"] == "active_skill_creator_managed_personal_skills_save", "ChatGPT native save workflow missing")
    require(native_save["after_source_resolution"] == "create_validate_save_verify", "ChatGPT source-resolution follow-through missing")
    require(native_save["host_managed_personal_skills_storage_allowed"] is True, "ChatGPT managed storage must be allowed")
    require(native_save["user_project_workspace_write_allowed"] is False, "ChatGPT must not write into user project workspace")
    require(native_save["created_not_installed_requires_real_save_attempt"] is True, "ChatGPT created-not-installed guard missing")
    confirmation = chatgpt_config["installation_confirmation"]
    require(confirmation["separate_ui_prompt_expected"] is False, "ChatGPT must not wait for separate UI")
    require(confirmation["approval_alone_marks_installed"] is False, "ChatGPT approval must not mark installation")
    require("active_skill_creator_reports_created_and_saved" in confirmation["successful_install_evidence"], "ChatGPT creation evidence missing")
    source_integrity = chatgpt_config["source_integrity"]
    require(source_integrity["hash_algorithm"] == "sha256", "ChatGPT hash algorithm missing")
    require(source_integrity["verify_when_available"] is True, "ChatGPT conditional hash policy missing")
    require(source_integrity["unavailable_blocks_creation"] is False, "ChatGPT unavailable hash check must not block creation")
    require(source_integrity["mismatch_blocks_creation"] is True, "ChatGPT hash mismatch must block creation")
    require(source_integrity["unavailable_status"] == "declared_unverified", "ChatGPT explicit unavailable hash state missing")
    update_contract = chatgpt_config["update_contract"]
    require(update_contract["chatgpt_bootstrap_path"] == "CHATGPT_UPDATE.md", "ChatGPT update bootstrap missing")
    require(update_contract["codex_bootstrap_path"] == "CODEX_UPDATE.md", "Codex update bootstrap missing")
    require(update_contract["mode"] == "manual_incremental_user_approved", "Update approval mode missing")
    require(update_contract["automatic_repository_sync"] is False, "Automatic update must remain disabled")
    require(update_contract["duplicate_skill_creation_allowed"] is False, "Update must not duplicate a Skill")
    require(update_contract["approval_required_before_apply"] is True, "Update approval guard missing")
    require(update_contract["selective_update_requires_file_level_comparison"] is True, "Selective update guard missing")
    require(update_contract["local_conflict_blocks_apply"] is True, "Local conflict guard missing")
    bundle_contract = chatgpt_config["source_bundle_contract"]
    require(bundle_contract["bundle_path_field"] == "path", "ChatGPT bundle path field missing")
    require(bundle_contract["repository_path_field"] == "repository_path", "ChatGPT repository path field missing")
    require(bundle_contract["bundle_path_is_relative_to_skill_source_root"] is True, "ChatGPT bundle paths must be relative")
    require(bundle_contract["preserve_declared_directory_structure"] is True, "ChatGPT bundle structure guard missing")

    codex_install = read(ROOT / "CODEX_INSTALL.md")
    require(".agents/skills/static-graphic-design-creator" in codex_install, "Codex source root missing")
    require("$skill-installer" in codex_install, "Codex fresh-install mechanism missing")
    require("verify its SHA-256 against the manifest" in codex_install, "Codex hash verification missing")
    require("immutable source commit" in codex_install, "Codex immutable release pin missing")
    require("`repository_path`" in codex_install and "`raw_url`" in codex_install, "Codex source retrieval mapping missing")
    require("Follow `CODEX_UPDATE.md`" in codex_install, "Codex update handoff missing")

    chatgpt_update = read(CHATGPT_UPDATE)
    for phrase in [
        "@skill-creator",
        "source-release.json",
        "If there is no source delta",
        "show a concise `Delta`",
        "Never create a duplicate Skill",
        "blocked_local_conflict",
        "declared_bundle_replacement",
        "Never monitor GitHub in the background",
        "relative bundle `path`",
    ]:
        require(phrase in chatgpt_update, f"ChatGPT update contract missing: {phrase}")
    require("managed-personal-Skills save workflow" in chatgpt_update, "ChatGPT update must use native managed save")
    require("plugin" not in chatgpt_update.lower(), "ChatGPT update prompt must stay native-Skill-only")
    require("immutable_source_commit" in chatgpt_update, "ChatGPT update immutable-source guard missing")
    require("declared_unverified" in chatgpt_update, "ChatGPT update unverified-hash disclosure missing")

    evaluation = read(MANUAL_EVALUATION)
    require("managed-personal-Skills flow" in evaluation, "Forward evaluation must exercise the native save path")
    require("created_not_installed` is valid only after an actual native save attempt" in evaluation, "Forward evaluation must guard created-not-installed")
    require("user's chosen language" in evaluation, "Forward evaluation must test language adaptation")
    require("stable release may be published only" in evaluation, "Forward evaluation must gate stable publication")

    codex_update = read(CODEX_UPDATE)
    for phrase in [
        "$skill-installer",
        "source-release.json",
        "If there is no delta",
        "Ask for explicit user approval",
        "blocked_local_conflict",
        "declared_bundle_replacement",
        "Do not update automatically",
        "`repository_path` or `raw_url`",
    ]:
        require(phrase in codex_update, f"Codex update contract missing: {phrase}")
    require("immutable_source_commit" in codex_update, "Codex update immutable-source guard missing")

    qa = read(SKILL / "references" / "qa-and-repair.md")
    require("explicitly requested `render` or `render_and_prompt`" in qa, "QA native-render authorization missing")
    require("do not silently create another render" in qa, "QA rerender guard missing")
    require("likeness authority" in qa, "QA likeness authority missing")
    require("generation_failed" in qa, "QA generation-failure route missing")
    require("## Composition integrity and anti-slop gate" in qa, "Anti-slop QA gate missing")

    atlas = read(SKILL / "references" / "poster-style-and-composition-atlas.md")
    for term in [
        "communication goal → audience response and copy burden",
        "## Collaboration routes",
        "`discovery_brainstorm`",
        "`directed_collaboration`",
        "## Composition archetypes",
        "## Historical and visual style families",
        "## Material and reproduction treatments",
        "## Anti-slop composition gate",
        "style label from replacing a communication decision",
    ]:
        require(term in atlas, f"Poster atlas missing: {term}")

    style_catalog = read(SKILL / "references" / "poster-style-translation-catalog.md")
    for term in [
        "one primary poster language",
        "minimalism",
        "maximalism",
        "futuristic",
        "glassmorphism",
        "Y2K",
        "Victorian style",
        "graffiti",
        "handwritten",
        "brutalist_information",
        "postmodern_memphis",
        "punk_zine",
        "solarpunk",
        "retro`, `bohemian`, and `futuristic` were not left undefined",
    ]:
        require(term in style_catalog, f"Poster style translation catalog missing: {term}")
    require("Treat a requested label as evidence, not as a finished instruction" in style_catalog, "Style catalog must preserve goal-first selection")
    require("not a menu that must be exhausted" in style_catalog, "Style catalog must not turn into a preset menu")
    require("Do not create a stack of unrelated labels" in style_catalog, "Style catalog must block effect stacking")
    require("A colour palette, a texture, a 3D rendering method, or a type treatment is not by itself a poster strategy" in style_catalog, "Style catalog must distinguish design layers")
    require("style_request_labels" in skill, "Skill must carry requested style labels into its workflow")
    require("style_request_labels" in read(SKILL / "templates" / "design-intake.md"), "Intake must record requested style labels")
    require("primary_poster_language" in read(SKILL / "templates" / "prompt-pack.md"), "Prompt pack must record selected poster language")

    copy_asset = read(COPY_DEVELOPMENT)
    for term in [
        "Copy Development and Human Voice",
        "`locked_copy`",
        "`copy_discovery`",
        "`copy_refinement`",
        "Anti-generic copy standard",
        "Human voice means",
        "copy_fit",
        "Do not invent product facts",
    ]:
        require(term in copy_asset, f"Copy-development asset missing: {term}")
    require("copy-development-and-human-voice.md" in skill, "Skill must route unresolved copy through the internal copy asset")
    require("copy_route" in read(SKILL / "templates" / "design-intake.md"), "Intake must record the copy route")
    require("copy_route" in read(SKILL / "templates" / "prompt-pack.md"), "Prompt pack must record the copy route")
    require("copy_route" in read(SKILL / "references" / "workflow-integration.md"), "Workflow handoff must preserve the copy route")

    walkthroughs = read(PRODUCTION_WALKTHROUGHS)
    for term in [
        "## 1. Discovery brainstorm",
        "## 2. Directed collaboration and Codex crosswalk",
        "## 3. QA repair: scoped edit",
        "## 4. QA repair: full rerender",
        "Final eight-stage prompt",
    ]:
        require(term in walkthroughs, f"Production walkthrough is incomplete: {term}")

    research_atlas = read(SKILL / "references" / "poster-movements-and-production-atlas.md")
    for term in [
        "## Decision path",
        "must_read",
        "## Historical and formal language cards",
        "Polish Poster School",
        "Sachplakat",
        "## Production and materiality",
        "## Anti-slop diagnostic",
        "Non-automatic human decisions",
        "process logic",
    ]:
        require(term in research_atlas, f"Poster research atlas missing: {term}")

    manifest = json.loads(read(SOURCE_MANIFEST))
    require(manifest["repository"] == "https://github.com/FrameCoreWorks/static-graphic-design-creator", "Unexpected manifest repository")
    require(manifest["schema_version"] == 3, "Unexpected source manifest schema")
    require(manifest["version"] == "0.7.0-rc.2", "Invalid manifest version")
    require(manifest["release_channel"] == "candidate", "Manifest release channel missing")
    require(manifest["release_ref_type"] == "immutable_git_commit", "Manifest release ref type missing")
    require(
        re.fullmatch(r"[0-9a-f]{40}", manifest["immutable_source_commit"]) is not None,
        "Manifest immutable source commit missing",
    )
    require(manifest["ref"] == manifest["immutable_source_commit"], "Manifest ref must be its immutable source commit")
    require(
        chatgpt_config["release"]["immutable_source_commit"] == manifest["immutable_source_commit"],
        "Bootstrap config and source manifest must resolve the same immutable source commit",
    )
    require(len(manifest["skills"]) == 1, "Manifest must declare exactly one skill")
    declared_skill = manifest["skills"][0]
    require(declared_skill["name"] == "static-graphic-design-creator", "Unexpected manifest skill")
    declared_bundle_paths = []
    declared_repository_paths = []
    for source in declared_skill["files"]:
        bundle_path = Path(source["path"])
        require(not bundle_path.is_absolute(), f"Bundle path must be relative: {source['path']}")
        require(".." not in bundle_path.parts, f"Bundle path escapes skill root: {source['path']}")
        require(source["path"] != "", "Bundle path must not be empty")
        repository_path = source["repository_path"]
        require(
            repository_path == f"{declared_skill['source_root']}/{source['path']}",
            f"Repository path does not map to declared bundle path: {source['path']}",
        )
        path = SKILL / bundle_path
        require(path.is_file(), f"Manifest source is missing: {repository_path}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == source["sha256"], f"Manifest hash mismatch: {repository_path}")
        expected_raw_url = (
            "https://raw.githubusercontent.com/FrameCoreWorks/"
            f"static-graphic-design-creator/{manifest['ref']}/{repository_path}"
        )
        require(source["raw_url"] == expected_raw_url, f"Manifest raw URL mismatch: {repository_path}")
        declared_bundle_paths.append(bundle_path)
        declared_repository_paths.append(repository_path)
    require(len(declared_bundle_paths) == len(set(declared_bundle_paths)), "Manifest bundle paths must be unique")
    require(len(declared_repository_paths) == len(set(declared_repository_paths)), "Manifest repository paths must be unique")
    require(declared_bundle_paths[0] == Path("SKILL.md"), "Skill entrypoint must remain first in the manifest")
    actual_paths = sorted(path for path in SKILL.rglob("*") if path.is_file())
    require(sorted(SKILL / path for path in declared_bundle_paths) == actual_paths, "Manifest must enumerate every skill source file")

    source_release = json.loads(read(SOURCE_RELEASE))
    require(source_release["schema_version"] == 2, "Unexpected source release schema")
    require(source_release["repository"] == manifest["repository"], "Source release repository mismatch")
    require(source_release["skill_name"] == declared_skill["name"], "Source release Skill name mismatch")
    require(source_release["version"] == manifest["version"], "Source release version mismatch")
    require(source_release["release_id"] == manifest["release_id"], "Source release ID mismatch")
    require(source_release["release_channel"] == manifest["release_channel"], "Source release channel mismatch")
    require(
        source_release["source_ref_type"] == "immutable_git_commit_from_release_manifest",
        "Source release must preserve immutable-source handoff",
    )

    prohibited_private_paths = ["/root/.codex", "/workspace/scratch", "CODEX_HOME"]
    distributable_files = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHATGPT_INSTALL.md",
        ROOT / "CODEX_INSTALL.md",
        CHATGPT_UPDATE,
        CODEX_UPDATE,
        SOURCE_MANIFEST,
    ] + list(SKILL.rglob("*"))
    for path in distributable_files:
        if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".py"}:
            content = read(path)
            for private_path in prohibited_private_paths:
                require(private_path not in content, f"Private path leaked into {path.relative_to(ROOT)}")
            require("[TODO:" not in content, f"Unfinished placeholder in {path.relative_to(ROOT)}")

    ci = read(ROOT / ".github" / "workflows" / "validate.yml")
    require("python3 tests/test_skill.py" in ci, "CI does not run the contract test")
    source_anchor_checker = read(SOURCE_ANCHOR_CHECKER)
    require("Expected at least 16 curated source anchors" in source_anchor_checker, "Source-anchor inventory floor missing")
    source_anchor_workflow = read(SOURCE_ANCHOR_WORKFLOW)
    require("schedule:" in source_anchor_workflow, "Source-anchor workflow must be scheduled")
    require("python3 tests/check_source_anchors.py" in source_anchor_workflow, "Source-anchor workflow missing checker")
    security = read(SECURITY)
    require("declared_unverified" in security, "Security document must disclose hash-unavailable state")
    require("independent root of trust" in security, "Security document must disclose bootstrap boundary")
    contributing = read(CONTRIBUTING)
    require("all twenty host cases" in contributing, "Contribution guide must require host evaluation")
    host_evaluation = read(HOST_EVALUATION)
    require("pending_host_evaluation" in host_evaluation, "Candidate host-evaluation state missing")
    require(host_evaluation.count("| pending | pending | Unknown |") == 20, "Candidate must record all pending host cases")

    print("static-graphic-design-creator: package contract passed")


if __name__ == "__main__":
    main()
