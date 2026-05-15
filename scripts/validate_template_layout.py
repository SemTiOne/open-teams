#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "workspace-assets-index.md",
    "task-completion-checklist.md",
    "docs/README.md",
    "docs/development-specs/README.md",
    "docs/frontend-development-specs/README.md",
    "docs/overall-architecture/总体架构设计文档模板.md",
    "docs/templates/project-docs/源码说明文档.md",
    "skills/README.md",
    "scripts/init_project_skills.py",
    "change-history/TEMPLATE.md",
    "task-plans/TEMPLATE.md",
]


def main() -> int:
    missing = []
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            missing.append(rel)
    if missing:
        print("Missing required template paths:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("Template layout validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
