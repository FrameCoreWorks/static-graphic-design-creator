#!/usr/bin/env python3
"""Local structural and contract validation for the standalone skill."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "static-design-prompt-architect"
SOURCE_MANIFEST = ROOT / "config" / "chatgpt-skill-sources.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    required_paths = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHATGPT_INSTALL.md",
        ROOT / "CODEX_INSTALL.md",
        ROOT / "config" / "chatgpt-skills.json",
        SOURCE_MANIFEST,
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

    skill = read(SKILL / "SKILL.md")
    require(skill.startswith("---\nname: static-design-prompt-architect\n"), "SKILL.md frontmatter missing")
    for section in ["Standalone mode", "Connected mode", "## Inputs", "## Output", "## Final self-check"]:
        require(section in skill, f"Skill lacks required workflow boundary: {section}")
    require("never ask for intermediate images" in skill, "Single-generation constraint missing")
    require("Do not generate assets, call external services" in skill, "Execution boundary missing")

    contract = read(SKILL / "references" / "unified-static-prompt-contract.md")
    for stage in range(1, 9):
        require(f"{stage}. **" in contract, f"Missing stage {stage} in unified contract")
    require("one final raster-design instruction" in contract, "Contract must define one final output")

    integration = read(SKILL / "references" / "workflow-integration.md")
    for field in ["brief_contract", "direction_contract", "copy_pack", "reference_pack", "prompt_pack"]:
        require(field in integration, f"Portable workflow field missing: {field}")
    require("Do not automatically call a renderer" in integration, "Integration must not execute work")

    chatgpt_install = read(ROOT / "CHATGPT_INSTALL.md")
    for phrase in ["@skill-creator", "one native ChatGPT Skill", "not a plugin", "config/chatgpt-skill-sources.json"]:
        require(phrase in chatgpt_install, f"ChatGPT installation contract missing: {phrase}")

    codex_install = read(ROOT / "CODEX_INSTALL.md")
    require(".agents/skills/static-design-prompt-architect" in codex_install, "Codex source root missing")
    require("not a plugin" in codex_install, "Codex plugin boundary missing")

    manifest = json.loads(read(SOURCE_MANIFEST))
    require(manifest["repository"] == "https://github.com/FrameCoreWorks/static-design-prompt-architect", "Unexpected manifest repository")
    require(manifest["ref"] == "main", "Unexpected manifest ref")
    require(len(manifest["skills"]) == 1, "Manifest must declare exactly one skill")
    declared_skill = manifest["skills"][0]
    require(declared_skill["name"] == "static-design-prompt-architect", "Unexpected manifest skill")
    declared_paths = []
    for source in declared_skill["files"]:
        path = ROOT / source["path"]
        require(path.is_file(), f"Manifest source is missing: {source['path']}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == source["sha256"], f"Manifest hash mismatch: {source['path']}")
        require(source["raw_url"].endswith(source["path"]), f"Manifest raw URL mismatch: {source['path']}")
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

    print("static-design-prompt-architect: package contract passed")


if __name__ == "__main__":
    main()
