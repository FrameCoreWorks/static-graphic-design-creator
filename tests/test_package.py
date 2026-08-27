#!/usr/bin/env python3
"""Local structural and contract validation for the standalone skill package."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "static-design-prompt-architect"
SKILL = PLUGIN / "skills" / "static-design-prompt-architect"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    required_paths = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "submission" / "openai-plugin-directory.md",
        ROOT / ".agents" / "plugins" / "marketplace.json",
        PLUGIN / ".codex-plugin" / "plugin.json",
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

    manifest = json.loads(read(PLUGIN / ".codex-plugin" / "plugin.json"))
    require(manifest["name"] == "static-design-prompt-architect", "Plugin name mismatch")
    require(manifest["version"] == "0.1.0", "Unexpected initial version")
    require(manifest["license"] == "Apache-2.0", "License must be Apache-2.0")
    require(manifest["skills"] == "./skills/", "Plugin must expose its skills directory")
    require(manifest["author"]["name"] == "FrameCore Works", "Author metadata mismatch")
    require(len(manifest["interface"]["defaultPrompt"]) <= 3, "Too many starter prompts")

    marketplace = json.loads(read(ROOT / ".agents" / "plugins" / "marketplace.json"))
    entry = marketplace["plugins"][0]
    require(entry["name"] == manifest["name"], "Marketplace and plugin names diverge")
    require(entry["source"]["path"] == "./plugins/static-design-prompt-architect", "Marketplace source path mismatch")
    require(entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Unexpected marketplace policy")

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

    prohibited_private_paths = ["/root/.codex", "/workspace/scratch", "CODEX_HOME"]
    distributable_files = [ROOT / "README.md", ROOT / "LICENSE"] + list(PLUGIN.rglob("*"))
    for path in distributable_files:
        if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".py"}:
            content = read(path)
            for private_path in prohibited_private_paths:
                require(private_path not in content, f"Private path leaked into {path.relative_to(ROOT)}")
            require("[TODO:" not in content, f"Unfinished placeholder in {path.relative_to(ROOT)}")

    print("static-design-prompt-architect: package contract passed")


if __name__ == "__main__":
    main()
