#!/usr/bin/env python3

from pathlib import Path
import argparse
import shutil


TASK_PLAN_KEEP_FILES = {
    "README.md",
    "TEMPLATE.md",
}

CHANGE_HISTORY_KEEP_FILES = {
    "README.md",
    "TEMPLATE.md",
}


def remove_path(path: Path, apply: bool) -> None:
    action = "remove"
    print(f"{action}: {path}")
    if not apply:
        return
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def clean_task_plans(root: Path, apply: bool) -> None:
    task_plans = root / "task-plans"
    if not task_plans.exists():
        return
    for path in sorted(task_plans.iterdir()):
        if path.name in TASK_PLAN_KEEP_FILES:
            continue
        remove_path(path, apply)


def clean_change_history(root: Path, apply: bool) -> None:
    change_history = root / "change-history"
    if not change_history.exists():
        return
    for path in sorted(change_history.iterdir()):
        if path.name in CHANGE_HISTORY_KEEP_FILES:
            continue
        remove_path(path, apply)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Preview or remove open-teams template history from a copied workspace."
    )
    parser.add_argument("workspace_root", help="Copied workspace root to clean")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually remove files. Without this flag the script only previews actions.",
    )
    args = parser.parse_args()

    root = Path(args.workspace_root).resolve()
    if not root.exists():
        print(f"workspace root not found: {root}")
        return 1

    mode = "apply" if args.apply else "preview"
    print(f"mode: {mode}")
    print(f"workspace: {root}")

    clean_task_plans(root, args.apply)
    clean_change_history(root, args.apply)

    if not args.apply:
        print("dry run only; rerun with --apply to remove listed paths.")

    print("next: update AGENTS.md, workspace-config/code-sources.yaml, and workspace-config/workspace-version.yaml for your own project.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
