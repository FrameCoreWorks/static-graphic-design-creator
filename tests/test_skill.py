#!/usr/bin/env python3
"""Local structural and contract validation for the standalone skill."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "static-design-prompt-architect"
SOURCE_MANIFEST = ROOT / "config" / "chatgpt-skill-sources.json"
POLICY_FIXTURES = ROOT / "tests" / "fixtures" / "policy-regression-cases.json"
BEHAVIOR_FIXTURES = ROOT / "tests" / "fixtures" / "behavior-eval-cases.json"
MANUAL_EVALUATION = ROOT / "EVALUATION.md"

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


def main() -> None:
    required_paths = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHATGPT_INSTALL.md",
        ROOT / "CODEX_INSTALL.md",
        ROOT / "CHANGELOG.md",
        ROOT / ".github" / "workflows" / "validate.yml",
        ROOT / "config" / "chatgpt-skills.json",
        SOURCE_MANIFEST,
        POLICY_FIXTURES,
        BEHAVIOR_FIXTURES,
        MANUAL_EVALUATION,
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "unified-static-prompt-contract.md",
        SKILL / "references" / "capability-and-reference-contract.md",
        SKILL / "references" / "workflow-integration.md",
        SKILL / "references" / "qa-and-repair.md",
        SKILL / "references" / "deliverable-profiles.md",
        SKILL / "templates" / "design-intake.md",
        SKILL / "templates" / "prompt-pack.md",
    ]
    for path in required_paths:
        require(path.is_file(), f"Missing required file: {path.relative_to(ROOT)}")

    retired_plugin_paths = [
        ROOT / ".agents" / "plugins" / "marketplace.json",
        ROOT / "plugins" / "static-design-prompt-architect" / ".codex-plugin" / "plugin.json",
        ROOT / "submission" / "openai-plugin-directory.md",
    ]
    for path in retired_plugin_paths:
        require(not path.exists(), f"Standalone skill must not include plugin artifact: {path.relative_to(ROOT)}")

    require(not (ROOT / "skills").exists(), "Canonical source must use .agents/skills only")
    validate_policy_fixtures()
    validate_behavior_fixtures()

    skill = read(SKILL / "SKILL.md")
    require(skill.startswith("---\nname: static-design-prompt-architect\n"), "SKILL.md frontmatter missing")
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
    for render_status in RENDER_STATUSES:
        require(render_status in skill, f"Skill lacks render status: {render_status}")

    contract = read(SKILL / "references" / "unified-static-prompt-contract.md")
    for stage in range(1, 9):
        require(f"{stage}. **" in contract, f"Missing stage {stage} in unified contract")
    require("one final raster-design instruction" in contract, "Contract must define one final output")
    require("## Prompt compactness" in contract, "Prompt compactness contract missing")

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

    chatgpt_install = read(ROOT / "CHATGPT_INSTALL.md")
    for phrase in ["@skill-creator", "one native ChatGPT Skill", "not a plugin", "config/chatgpt-skill-sources.json"]:
        require(phrase in chatgpt_install, f"ChatGPT installation contract missing: {phrase}")
    require("When the current Work surface can compute SHA-256" in chatgpt_install, "ChatGPT conditional hash verification missing")
    require("hash_verification: unavailable" in chatgpt_install, "ChatGPT hash-unavailable status missing")
    require("reread a fresh manifest" in chatgpt_install, "ChatGPT hash mismatch recovery missing")
    require("## Mandatory onboarding before approval" in chatgpt_install, "ChatGPT onboarding contract missing")
    require("What it gives:" in chatgpt_install, "ChatGPT onboarding value missing")
    require("Do not begin source-file processing" in chatgpt_install, "ChatGPT onboarding ordering missing")
    require("native Skill-creation workflow" in chatgpt_install, "ChatGPT native creation route missing")
    require("Do not search for or wait for a separate function tool" in chatgpt_install, "ChatGPT separate-tool guard missing")
    require("release-pinned public source" in chatgpt_install, "ChatGPT release pin missing")
    require("short onboarding before requesting approval" in read(ROOT / "README.md"), "README onboarding disclosure missing")
    require("@skill-creator is the native creation workflow in ChatGPT Work." in read(ROOT / "README.md"), "README native creation route missing")

    chatgpt_config = json.loads(read(ROOT / "config" / "chatgpt-skills.json"))
    require(chatgpt_config["schema_version"] == 3, "Unexpected ChatGPT setup schema")
    require(chatgpt_config["version"] == "0.2.0", "Unexpected release version")
    require(chatgpt_config["ref"] == "v0.2.0", "ChatGPT config is not release pinned")
    require(chatgpt_config["release"]["channel"] == "stable", "ChatGPT release channel missing")
    require(chatgpt_config["release"]["ref_type"] == "release_branch", "ChatGPT release ref type missing")
    require(chatgpt_config["surface"] == "native-chatgpt-skills", "ChatGPT surface missing")
    native_creation = chatgpt_config["native_creation"]
    require(native_creation["creator_invocation"] == "@skill-creator", "ChatGPT creator invocation missing")
    require(native_creation["tool_discovery_required"] is False, "ChatGPT must not discover a separate tool")
    require(native_creation["capability_preflight_required"] is False, "ChatGPT must not preflight creation capability")
    confirmation = chatgpt_config["installation_confirmation"]
    require(confirmation["separate_ui_prompt_expected"] is False, "ChatGPT must not wait for separate UI")
    require(confirmation["approval_alone_marks_installed"] is False, "ChatGPT approval must not mark installation")
    require("active_skill_creator_reports_created_and_saved" in confirmation["successful_install_evidence"], "ChatGPT creation evidence missing")
    source_integrity = chatgpt_config["source_integrity"]
    require(source_integrity["hash_algorithm"] == "sha256", "ChatGPT hash algorithm missing")
    require(source_integrity["verify_when_available"] is True, "ChatGPT conditional hash policy missing")
    require(source_integrity["unavailable_blocks_creation"] is False, "ChatGPT unavailable hash check must not block creation")
    require(source_integrity["mismatch_blocks_creation"] is True, "ChatGPT hash mismatch must block creation")

    codex_install = read(ROOT / "CODEX_INSTALL.md")
    require(".agents/skills/static-design-prompt-architect" in codex_install, "Codex source root missing")
    require("not a plugin" in codex_install, "Codex plugin boundary missing")
    require("verify its SHA-256 against the manifest" in codex_install, "Codex hash verification missing")
    require("stable release `v0.2.0`" in codex_install, "Codex release pin missing")

    qa = read(SKILL / "references" / "qa-and-repair.md")
    require("explicitly requested `render` or `render_and_prompt`" in qa, "QA native-render authorization missing")
    require("do not silently create another render" in qa, "QA rerender guard missing")
    require("likeness authority" in qa, "QA likeness authority missing")
    require("generation_failed" in qa, "QA generation-failure route missing")

    manifest = json.loads(read(SOURCE_MANIFEST))
    require(manifest["repository"] == "https://github.com/FrameCoreWorks/static-design-prompt-architect", "Unexpected manifest repository")
    require(re.fullmatch(r"0\.\d+\.\d+", manifest["version"]) is not None, "Invalid manifest version")
    require(manifest["ref"] == f"v{manifest['version']}", "Manifest ref must match versioned release ref")
    require(manifest["release_channel"] == "stable", "Manifest release channel missing")
    require(manifest["release_ref_type"] == "release_branch", "Manifest release ref type missing")
    require(len(manifest["skills"]) == 1, "Manifest must declare exactly one skill")
    declared_skill = manifest["skills"][0]
    require(declared_skill["name"] == "static-design-prompt-architect", "Unexpected manifest skill")
    declared_paths = []
    for source in declared_skill["files"]:
        path = ROOT / source["path"]
        require(path.is_file(), f"Manifest source is missing: {source['path']}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == source["sha256"], f"Manifest hash mismatch: {source['path']}")
        expected_raw_url = (
            "https://raw.githubusercontent.com/FrameCoreWorks/"
            f"static-design-prompt-architect/{manifest['ref']}/{source['path']}"
        )
        require(source["raw_url"] == expected_raw_url, f"Manifest raw URL mismatch: {source['path']}")
        declared_paths.append(path)
    actual_paths = sorted(path for path in SKILL.rglob("*") if path.is_file())
    require(sorted(declared_paths) == actual_paths, "Manifest must enumerate every skill source file")

    prohibited_private_paths = ["/root/.codex", "/workspace/scratch", "CODEX_HOME"]
    distributable_files = [ROOT / "README.md", ROOT / "LICENSE", ROOT / "CHATGPT_INSTALL.md", ROOT / "CODEX_INSTALL.md", SOURCE_MANIFEST] + list(SKILL.rglob("*"))
    for path in distributable_files:
        if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".py"}:
            content = read(path)
            for private_path in prohibited_private_paths:
                require(private_path not in content, f"Private path leaked into {path.relative_to(ROOT)}")
            require("[TODO:" not in content, f"Unfinished placeholder in {path.relative_to(ROOT)}")

    ci = read(ROOT / ".github" / "workflows" / "validate.yml")
    require("python3 tests/test_skill.py" in ci, "CI does not run the contract test")

    print("static-design-prompt-architect: package contract passed")


if __name__ == "__main__":
    main()
