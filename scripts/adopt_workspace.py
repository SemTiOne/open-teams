#!/usr/bin/env python3

from pathlib import Path
import argparse
import shutil
import subprocess
import sys


SKIP_DIRS = {
    ".git",
    "__pycache__",
}


def copy_template(source: Path, target: Path) -> None:
    if target.exists() and any(target.iterdir()):
        raise ValueError(f"target directory already exists and is not empty: {target}")
    target.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        if item.name in SKIP_DIRS:
            continue
        destination = target / item.name
        if item.is_dir():
            shutil.copytree(item, destination, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(item, destination)


def write_code_sources(target: Path, project_slug: str, project_name: str, source_path: str, default_branch: str) -> None:
    content = f"""repositories:
  - repo_id: {project_slug}
    repo_name: {project_name}
    category: app
    local_path: {source_path}
    default_branch: {default_branch}
    source_of_truth: local
    notes: 由 AI 对话式初始化写入，请按真实项目继续补充分层、模块和验证说明
"""
    (target / "workspace-config" / "code-sources.yaml").write_text(content, encoding="utf-8")


def write_workspace_version(target: Path, adoption_mode: str) -> None:
    path = target / "workspace-config" / "workspace-version.yaml"
    content = path.read_text(encoding="utf-8")
    content = content.replace("adoption_mode: template", f"adoption_mode: {adoption_mode}")
    content = content.replace("source_strategy: undecided", "source_strategy: external-mapping")
    content = content.replace(
        "- 通用模板仓库，不包含业务线专有事实。",
        "- 基于 open-teams 模板通过 AI 对话式初始化生成，需继续补充业务线本地定制。",
    )
    path.write_text(content, encoding="utf-8")


def run_script(target: Path, script: str, *args: str) -> None:
    command = [sys.executable, str(target / "scripts" / script), str(target), *args]
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy open-teams into a new workspace and perform the AI-guided initial cleanup."
    )
    parser.add_argument("--template-root", default=".", help="open-teams template root")
    parser.add_argument("--target", required=True, help="target workspace directory")
    parser.add_argument("--project-slug", required=True, help="primary project slug")
    parser.add_argument("--project-name", required=True, help="primary project display name")
    parser.add_argument("--source-path", required=True, help="real source repository path or URL")
    parser.add_argument("--default-branch", default="main", help="primary source default branch")
    parser.add_argument(
        "--adoption-mode",
        default="ai-guided",
        choices=["ai-guided", "greenfield", "legacy-adoption"],
        help="workspace adoption mode to write into workspace-version.yaml",
    )
    parser.add_argument(
        "--skip-clean",
        action="store_true",
        help="copy template without removing template task plans and change history",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="skip validate_template_layout.py after initialization",
    )
    args = parser.parse_args()

    template_root = Path(args.template_root).resolve()
    target = Path(args.target).resolve()
    if not (template_root / "workspace-assets-index.md").exists():
        print(f"template root is not an open-teams workspace: {template_root}")
        return 1

    copy_template(template_root, target)
    if not args.skip_clean:
        run_script(target, "prepare_clean_workspace.py", "--apply")
    write_code_sources(
        target,
        args.project_slug,
        args.project_name,
        args.source_path,
        args.default_branch,
    )
    write_workspace_version(target, args.adoption_mode)
    if not args.skip_validation:
        run_script(target, "validate_template_layout.py")

    print(f"created workspace: {target}")
    print("next: ask AI to update AGENTS.md and create docs/projects plus skills for the first project.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
