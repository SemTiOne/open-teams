#!/usr/bin/env python3

from pathlib import Path
import sys


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "workspace-assets-index.md",
    "task-completion-checklist.md",
    "docs/README.md",
    "skills/README.md",
    "skills/_templates/project/scene-template/SKILL.md",
    "skills/_templates/project/scene-template/examples.md",
    "skills/_templates/project/scene-template/references/README.md",
    "workspace-config/code-sources.yaml",
    "workspace-config/README.md",
    "references/README.md",
    "scripts/init_project_skills.py",
    "task-plans/TEMPLATE.md",
    "change-history/TEMPLATE.md",
    "sources/README.md",
]


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    missing = [item for item in REQUIRED_PATHS if not (root / item).exists()]
    if missing:
        print("missing required paths:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("Template layout validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
