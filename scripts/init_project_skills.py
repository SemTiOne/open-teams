#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

SCENES_BY_TYPE = {
    "frontend": [
        "new-feature-dev",
        "bugfix",
        "security-fix",
        "feature-refactor",
        "performance-tuning",
    ],
    "backend": [
        "new-feature-dev",
        "bugfix",
        "security-fix",
        "api-refactor",
        "feature-refactor",
        "performance-tuning",
    ],
    "task": [
        "new-feature-dev",
        "bugfix",
        "security-fix",
        "api-refactor",
        "feature-refactor",
        "performance-tuning",
    ],
}


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_skill(project_slug: str, project_type: str, scene: str) -> str:
    return f"""---
name: {project_slug}-{scene}
description: 面向 {project_slug} 的 {scene} 场景 skill 模板。
---

# {project_slug} {scene}

请将本文件替换为该项目的真实场景约束，并至少补充：

- 事实源文档
- 推荐代码阅读顺序
- 稳定约束
- 验证要求
- 输出要求
"""


def render_examples(project_slug: str, scene: str) -> str:
    return f"""# {project_slug} {scene} 示例

- “看 `skills/{project_slug}/{scene}/`，基于真实代码处理当前任务。”
"""


def render_reference(title: str) -> str:
    return f"# {title}\n\n- 待补充\n"


def init_project(project_slug: str, project_type: str) -> None:
    scenes = SCENES_BY_TYPE[project_type]
    for scene in scenes:
        scene_dir = SKILLS_DIR / project_slug / scene
        write_file(scene_dir / "SKILL.md", render_skill(project_slug, project_type, scene))
        write_file(scene_dir / "examples.md", render_examples(project_slug, scene))
        write_file(
            scene_dir / "references" / "input-checklist.md",
            render_reference("输入检查清单"),
        )
        write_file(
            scene_dir / "references" / "execution-playbook.md",
            render_reference("执行手册"),
        )
        write_file(
            scene_dir / "references" / "acceptance-checklist.md",
            render_reference("验收检查清单"),
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize skill templates for a project.")
    parser.add_argument("project_slug")
    parser.add_argument(
        "--project-type",
        choices=sorted(SCENES_BY_TYPE.keys()),
        required=True,
    )
    args = parser.parse_args()
    init_project(args.project_slug, args.project_type)


if __name__ == "__main__":
    main()
