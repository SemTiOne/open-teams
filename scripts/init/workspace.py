"""
init/workspace.py — Core workspace initialization logic.

Provides:
    init_workspace()     — main workspace creation flow (interactive or automated)
    run_interactive()    — guided interactive mode with user prompts
    _create_directory_structure()  — create template directories
    _write_template_files()        — write template files with substitutions
    _clean_git_history()           — remove existing .git
    _init_git_repo()               — initialize fresh git repo
    _validate_workspace()          — validate created workspace structure

All functions are pure (no side effects outside explicit I/O) and
testable — they receive Path objects and return predictable results.
"""

from __future__ import annotations

import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from init.ui import (
    Style,
    print_error,
    print_header,
    print_info,
    print_progress,
    print_separator,
    print_success,
    print_warning,
    prompt,
    prompt_choice,
)
from init.templates import TEMPLATE_SKELETON


# ---------------------------------------------------------------------------
# Core helpers (no I/O side effects beyond filesystem writes)
# ---------------------------------------------------------------------------


def _create_directory_structure(target: Path) -> int:
    """Create the template directory structure.

    Args:
        target: The target workspace directory.

    Returns:
        Number of directories created.
    """
    count = 0
    for dir_path in TEMPLATE_SKELETON["directories"]:
        full_path = target / dir_path
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            count += 1
    return count


def _write_template_files(
    target: Path, team_name: str, team_description: str
) -> int:
    """Write all template files with substituted values.

    Args:
        target: The target workspace directory.
        team_name: The team name for substitution.
        team_description: The team description for substitution.

    Returns:
        Number of files written.
    """
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    count = 0

    for rel_path, content_template in TEMPLATE_SKELETON["files"].items():
        full_path = target / rel_path
        if full_path.exists():
            continue  # Don't overwrite existing files

        full_path.parent.mkdir(parents=True, exist_ok=True)
        content = content_template.format(
            team_name=team_name,
            team_description=team_description,
            timestamp=timestamp,
        )
        full_path.write_text(content, encoding="utf-8")
        count += 1

    return count


def _clean_git_history(target: Path) -> bool:
    """Remove existing git history and reinitialize if needed.

    Args:
        target: The target workspace directory.

    Returns:
        True if git reinitialization was performed, False otherwise.
    """
    git_dir = target / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)
        return True
    return False


def _init_git_repo(target: Path) -> bool:
    """Initialize a fresh git repository in the target directory.

    Args:
        target: The target workspace directory.

    Returns:
        True if successful, False if git is not available.
    """
    try:
        subprocess.run(
            ["git", "init", "--initial-branch=main"],
            cwd=str(target),
            capture_output=True,
            check=True,
            text=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def _validate_workspace(target: Path) -> tuple[int, int]:
    """Run a basic validation of the created workspace.

    Args:
        target: The target workspace directory.

    Returns:
        Tuple of (error_count, warning_count).
    """
    errors = 0
    warnings = 0

    required_dirs = [
        ".open-teams",
        ".open-teams/skills",
        ".open-teams/memory",
        ".github",
        "docs",
        "scripts",
    ]
    for d in required_dirs:
        if not (target / d).is_dir():
            print_error(f"Missing directory: {d}/")
            errors += 1

    required_files = [
        ".open-teams/config.yaml",
        "README.md",
        "AGENTS.md",
        ".gitignore",
        "CONTRIBUTING.md",
    ]
    for f in required_files:
        if not (target / f).is_file():
            print_warning(f"Missing file: {f}")
            warnings += 1

    return errors, warnings


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def init_workspace(
    target: Path,
    team_name: str,
    team_description: str,
    force: bool = False,
    interactive: bool = True,
) -> int:
    """Initialize a new open-teams workspace.

    This is the main entry point for workspace initialization. It handles
    both interactive and non-interactive modes.

    Args:
        target: Path to the target workspace directory.
        team_name: The team name.
        team_description: Short description of the team.
        force: If True, allow initialization in non-empty directories.
        interactive: If True, prompt the user for confirmation/input.

    Returns:
        Exit code (0 = success, 1 = error).
    """
    # ── Step 0: Validate target ──
    target = target.resolve()

    if target.exists() and not target.is_dir():
        print_error(f"Target exists but is not a directory: {target}")
        return 1

    if target.exists() and any(target.iterdir()) and not force:
        print_warning(f"Target directory is not empty: {target}")
        if interactive:
            confirm = prompt(
                "Continue anyway? Existing files will not be overwritten. (y/N)", "N"
            )
            if confirm.lower() not in ("y", "yes"):
                print_info("Operation cancelled.")
                return 0
        else:
            print_error("Target directory is not empty. Use --force to override.")
            return 1

    # ── Step 1: Confirm details ──
    print_separator()
    print(f"   {Style.BOLD}📋 Summary{Style.RESET}")
    print(f"   {Style.DIM}Target:       {Style.RESET}{target}")
    print(f"   {Style.DIM}Team name:    {Style.RESET}{team_name}")
    print(f"   {Style.DIM}Description:  {Style.RESET}{team_description}")
    print_separator()

    if interactive:
        confirm = prompt("Proceed with initialization? (Y/n)", "Y")
        if confirm.lower() not in ("y", "yes", ""):
            print_info("Operation cancelled.")
            return 0

    # ── Step 2: Create directory structure ──
    print_progress("Creating directory structure...")
    target.mkdir(parents=True, exist_ok=True)
    dirs_created = _create_directory_structure(target)
    print_success(f"Created {dirs_created} directories")

    # ── Step 3: Clean git history ──
    print_progress("Cleaning git history...")
    had_git = _clean_git_history(target)
    if had_git:
        print_success("Removed existing .git directory")
    else:
        print_info("No existing git history to clean")

    # ── Step 4: Write template files ──
    print_progress("Writing template files...")
    files_written = _write_template_files(target, team_name, team_description)
    print_success(f"Wrote {files_written} template files")

    # ── Step 5: Write config ──
    print_progress("Writing workspace configuration...")
    # Config is already written by _write_template_files
    print_success("Configuration written")

    # ── Step 6: Initialize git ──
    print_progress("Initializing git repository...")
    if _init_git_repo(target):
        print_success("Git repository initialized (main branch)")
    else:
        print_warning("Git not available — skipping repository initialization")

    # ── Step 7: Validate ──
    print_progress("Validating workspace...")
    errors, warnings = _validate_workspace(target)

    print_separator()
    if errors == 0 and warnings == 0:
        print_success(f"Validation passed — {errors} errors, {warnings} warnings")
    elif errors == 0:
        print_warning(
            f"Validation passed with warnings — {errors} errors, {warnings} warnings"
        )
    else:
        print_error(f"Validation failed — {errors} errors, {warnings} warnings")
    print_separator()

    # ── Step 8: Done ──
    print(f"\n{Style.BOLD}{Style.BRIGHT_GREEN}🎉 Workspace created at {target}!{Style.RESET}\n")
    print(f"   {Style.BOLD}Next steps:{Style.RESET}")
    print(f"     cd {target.name}")
    print(f"     open-teams status")
    print(f"     open-teams new-skill my-first-skill\n")

    return 0 if errors == 0 else 1


def run_interactive(target: Optional[Path] = None) -> int:
    """Run the init command in interactive mode.

    Prompts the user for all required information and guides them
    through the workspace setup process.

    Args:
        target: Optional pre-specified target path.

    Returns:
        Exit code.
    """
    print_header("open-teams — Workspace Initialization")
    print(f"   {Style.DIM}Let's set up your team workspace!{Style.RESET}")

    # ── Target path ──
    if target is None:
        default_path = "./my-open-teams"
        path_str = prompt("Where should we create the workspace?", default_path)
        target = Path(path_str).resolve()
    else:
        print(f"   {Style.BOLD}📁 Target:{Style.RESET} {target}")
        target = target.resolve()

    # ── Team name ──
    default_name = target.name.replace("-", " ").replace("_", " ").title()
    team_name = prompt("Team name:", default_name)
    if not team_name:
        team_name = default_name

    # ── Description ──
    team_description = prompt(
        "Short description:",
        f"A team workspace for {team_name}",
    )

    # ── Template selection ──
    template = prompt_choice(
        "Select a template:",
        ["standard (default)", "minimal", "custom URL"],
        default=0,
    )
    if template.startswith("custom"):
        custom_url = prompt("Custom template URL:")
        if custom_url:
            print_info(f"Would use template at: {custom_url} (not yet implemented)")
        else:
            print_warning("No URL provided, falling back to standard template")

    # ── Force mode ──
    force = False
    if target.exists() and any(target.iterdir()):
        force_str = prompt("Target directory is not empty. Force? (y/N)", "N")
        force = force_str.lower() in ("y", "yes")

    return init_workspace(
        target=target,
        team_name=team_name,
        team_description=team_description,
        force=force,
        interactive=True,
    )
