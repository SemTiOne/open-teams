#!/usr/bin/env python3
"""
workspace-health-check.py — Comprehensive workspace health scanner.

Scans an open-teams workspace and reports on:
  - Missing required directories
  - Outdated template version
  - Large or growing change-history
  - Missing project docs for mapped sources
  - General workspace hygiene

Output formats:
  - Terminal report (default, with colors)
  - JSON report (--json flag)

Usage:
    python3 scripts/health_check.py                  # Scan current directory
    python3 scripts/health_check.py /path/to/workspace
    python3 scripts/health_check.py --json           # JSON output
    python3 scripts/health_check.py --json > report.json
    python3 scripts/health_check.py --strict         # Exit non-zero on warnings

Requirements:
    Python 3.10+
    No external dependencies (stdlib only)

Author: open-teams/dev-enhance
License: MIT
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Type definitions
# ---------------------------------------------------------------------------


class Severity:
    """Severity levels for health check findings."""

    OK = "ok"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


@dataclass
class Finding:
    """A single health check finding."""

    category: str
    severity: str
    message: str
    path: str = ""
    recommendation: str = ""


@dataclass
class HealthReport:
    """Complete health check report."""

    workspace: str
    timestamp: str
    findings: list[Finding] = field(default_factory=list)
    summary: dict[str, int] = field(default_factory=dict)

    def add(self, finding: Finding) -> None:
        """Add a finding to the report."""
        self.findings.append(finding)

    def finalize(self) -> None:
        """Compute summary counts."""
        self.summary = {
            "ok": 0,
            "info": 0,
            "warning": 0,
            "error": 0,
        }
        for f in self.findings:
            self.summary[f.severity] = self.summary.get(f.severity, 0) + 1

    def to_dict(self) -> dict[str, Any]:
        """Convert to JSON-serializable dictionary."""
        return {
            "workspace": self.workspace,
            "timestamp": self.timestamp,
            "summary": self.summary,
            "findings": [
                {
                    "category": f.category,
                    "severity": f.severity,
                    "message": f.message,
                    "path": f.path,
                    "recommendation": f.recommendation,
                }
                for f in self.findings
            ],
        }


# ---------------------------------------------------------------------------
# Terminal output helpers
# ---------------------------------------------------------------------------


class Style:
    """ANSI terminal styling."""

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    @staticmethod
    def _supports_color() -> bool:
        """Detect terminal color support."""
        if not hasattr(sys.stdout, "isatty"):
            return False
        if not sys.stdout.isatty():
            return False
        if os.environ.get("NO_COLOR"):
            return False
        if os.environ.get("FORCE_COLOR"):
            return True
        return os.environ.get("TERM", "") != "dumb"


if not Style._supports_color():
    for attr in dir(Style):
        if not attr.startswith("_") and not callable(getattr(Style, attr)):
            setattr(Style, attr, "")


def _severity_icon(severity: str) -> str:
    """Return an icon string for a severity level."""
    icons = {
        Severity.OK: "✅",
        Severity.INFO: "ℹ️ ",
        Severity.WARNING: "⚠️ ",
        Severity.ERROR: "❌",
    }
    return icons.get(severity, "❓")


def _severity_color(severity: str) -> str:
    """Return an ANSI color for a severity level."""
    colors = {
        Severity.OK: Style.BRIGHT_GREEN,
        Severity.INFO: Style.BRIGHT_BLUE,
        Severity.WARNING: Style.BRIGHT_YELLOW,
        Severity.ERROR: Style.BRIGHT_RED,
    }
    return colors.get(severity, Style.RESET)


def print_report(report: HealthReport) -> None:
    """Print a formatted health report to the terminal.

    Args:
        report: The completed HealthReport to display.
    """
    sep = f"{Style.DIM}{'─' * 56}{Style.RESET}"

    print(f"\n{Style.BOLD}{Style.BRIGHT_CYAN}🏥 Workspace Health Report{Style.RESET}")
    print(f"{Style.DIM}Workspace: {Style.RESET}{report.workspace}")
    print(f"{Style.DIM}Timestamp: {Style.RESET}{report.timestamp}")
    print(sep)

    # Group findings by category for cleaner output
    categories: dict[str, list[Finding]] = {}
    for f in report.findings:
        categories.setdefault(f.category, []).append(f)

    for category, findings in categories.items():
        print(f"\n{Style.BOLD}{Style.BRIGHT_WHITE}📂 {category}{Style.RESET}")
        for f in findings:
            icon = _severity_icon(f.severity)
            color = _severity_color(f.severity)
            path_str = f" {Style.DIM}({f.path}){Style.RESET}" if f.path else ""
            print(f"   {color}{icon}{Style.RESET} {f.message}{path_str}")
            if f.recommendation:
                print(f"     {Style.DIM}💡 {f.recommendation}{Style.RESET}")

    print(f"\n{sep}")
    s = report.summary
    print(
        f"   {Style.BRIGHT_GREEN}✅ {s.get('ok', 0)} OK{Style.RESET}"
        f"  {Style.BRIGHT_BLUE}ℹ️  {s.get('info', 0)} Info{Style.RESET}"
        f"  {Style.BRIGHT_YELLOW}⚠️  {s.get('warning', 0)} Warnings{Style.RESET}"
        f"  {Style.BRIGHT_RED}❌ {s.get('error', 0)} Errors{Style.RESET}"
    )

    # Overall health indicator
    if s.get("error", 0) > 0:
        health = f"{Style.BRIGHT_RED}🔴 Unhealthy{Style.RESET}"
    elif s.get("warning", 0) > 0:
        health = f"{Style.BRIGHT_YELLOW}🟡 Needs Attention{Style.RESET}"
    else:
        health = f"{Style.BRIGHT_GREEN}🟢 Healthy{Style.RESET}"

    print(f"   {Style.BOLD}Overall: {health}{Style.RESET}")
    print(f"{sep}\n")


# ---------------------------------------------------------------------------
# Health check functions
# ---------------------------------------------------------------------------


def check_required_directories(workspace: Path, report: HealthReport) -> None:
    """Check for the presence of all required workspace directories.

    Args:
        workspace: The workspace root directory.
        report: The HealthReport to add findings to.
    """
    required = [
        ".open-teams",
        ".open-teams/skills",
        ".open-teams/memory",
        ".github",
        ".github/ISSUE_TEMPLATE",
        ".github/workflows",
        "docs",
        "scripts",
    ]

    for dir_path in required:
        full = workspace / dir_path
        if full.is_dir():
            # Check if it's empty
            try:
                has_contents = any(full.iterdir())
            except PermissionError:
                report.add(Finding(
                    category="Directory Structure",
                    severity=Severity.ERROR,
                    message=f"Permission denied: {dir_path}/",
                    path=dir_path,
                    recommendation="Check directory permissions.",
                ))
                continue

            if not has_contents and not dir_path.endswith("memory"):
                # Some dirs are expected to be empty initially
                if dir_path in (".open-teams/memory", ".open-teams/skills"):
                    report.add(Finding(
                        category="Directory Structure",
                        severity=Severity.INFO,
                        message=f"Empty directory: {dir_path}/",
                        path=dir_path,
                        recommendation="This is normal for new workspaces.",
                    ))
                else:
                    report.add(Finding(
                        category="Directory Structure",
                        severity=Severity.WARNING,
                        message=f"Empty directory: {dir_path}/",
                        path=dir_path,
                        recommendation=f"Consider adding content to {dir_path}/.",
                    ))
            else:
                report.add(Finding(
                    category="Directory Structure",
                    severity=Severity.OK,
                    message=f"Directory present: {dir_path}/",
                    path=dir_path,
                ))
        else:
            report.add(Finding(
                category="Directory Structure",
                severity=Severity.ERROR,
                message=f"Missing required directory: {dir_path}/",
                path=dir_path,
                recommendation=f"Run `open-teams init` to create it, or `mkdir -p {dir_path}`",
            ))


def check_required_files(workspace: Path, report: HealthReport) -> None:
    """Check for required workspace files.

    Args:
        workspace: The workspace root directory.
        report: The HealthReport to add findings to.
    """
    required = [
        (".open-teams/config.yaml", "Workspace configuration"),
        ("README.md", "Project readme"),
        ("AGENTS.md", "Agent team definition"),
        (".gitignore", "Git ignore rules"),
        ("CONTRIBUTING.md", "Contribution guidelines"),
        (".github/ISSUE_TEMPLATE/bug_report.md", "Bug report template"),
        (".github/ISSUE_TEMPLATE/feature_request.md", "Feature request template"),
    ]

    for file_path, description in required:
        full = workspace / file_path
        if full.is_file():
            # Check file size (warning if empty)
            size = full.stat().st_size
            if size == 0:
                report.add(Finding(
                    category="Required Files",
                    severity=Severity.WARNING,
                    message=f"Empty file: {file_path} ({description})",
                    path=file_path,
                    recommendation="Add content to this file.",
                ))
            else:
                report.add(Finding(
                    category="Required Files",
                    severity=Severity.OK,
                    message=f"File present: {file_path} ({description})",
                    path=file_path,
                ))
        else:
            report.add(Finding(
                category="Required Files",
                severity=Severity.ERROR,
                message=f"Missing file: {file_path} ({description})",
                path=file_path,
                recommendation=f"Run `open-teams init` to regenerate, or create it manually.",
            ))


def check_template_version(workspace: Path, report: HealthReport) -> None:
    """Check if the workspace template is up to date.

    Args:
        workspace: The workspace root directory.
        report: The HealthReport to add findings to.
    """
    config_path = workspace / ".open-teams" / "config.yaml"
    if not config_path.is_file():
        report.add(Finding(
            category="Template Version",
            severity=Severity.ERROR,
            message="Cannot check template version: config.yaml missing",
            path=".open-teams/config.yaml",
            recommendation="Run `open-teams init` to create the config file.",
        ))
        return

    try:
        content = config_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report.add(Finding(
            category="Template Version",
            severity=Severity.ERROR,
            message=f"Cannot read config.yaml: {exc}",
            path=".open-teams/config.yaml",
            recommendation="Check file permissions and encoding.",
        ))
        return

    # Simple YAML parsing (no external dependency)
    template_version = _extract_yaml_value(content, "version")
    template_name = _extract_yaml_value(content, "name", section="template")

    if template_version:
        report.add(Finding(
            category="Template Version",
            severity=Severity.INFO,
            message=f"Template: {template_name or 'unknown'} v{template_version}",
            path=".open-teams/config.yaml",
            recommendation="Run `open-teams upgrade --check` to see if updates are available.",
        ))
    else:
        report.add(Finding(
            category="Template Version",
            severity=Severity.WARNING,
            message="Could not determine template version from config",
            path=".open-teams/config.yaml",
            recommendation="Ensure config.yaml has a `template.version` field.",
        ))


def check_change_history(workspace: Path, report: HealthReport) -> None:
    """Check the size and growth of the change-history directory.

    Args:
        workspace: The workspace root directory.
        report: The HealthReport to add findings to.
    """
    history_dirs = [
        ".open-teams/change-history",
        ".open-teams/history",
        "change-history",
        "changelog",
    ]

    for dir_name in history_dirs:
        history_path = workspace / dir_name
        if not history_path.is_dir():
            continue

        # Count files and measure total size
        try:
            file_count = 0
            total_size = 0
            for entry in history_path.rglob("*"):
                if entry.is_file():
                    file_count += 1
                    total_size += entry.stat().st_size
        except PermissionError:
            report.add(Finding(
                category="Change History",
                severity=Severity.ERROR,
                message=f"Permission denied reading: {dir_name}/",
                path=dir_name,
                recommendation="Check directory permissions.",
            ))
            continue

        size_mb = total_size / (1024 * 1024)
        report.add(Finding(
            category="Change History",
            severity=Severity.INFO,
            message=f"Change history: {file_count} files, {size_mb:.1f} MB",
            path=dir_name,
        ))

        if size_mb > 50:
            report.add(Finding(
                category="Change History",
                severity=Severity.WARNING,
                message=f"Large change history: {size_mb:.1f} MB",
                path=dir_name,
                recommendation="Consider archiving old history entries or using git-lfs.",
            ))
        return

    # No history directory found — that's fine
    report.add(Finding(
        category="Change History",
        severity=Severity.INFO,
        message="No change-history directory found (this is normal for new workspaces)",
    ))


def check_docs_coverage(workspace: Path, report: HealthReport) -> None:
    """Check if all mapped source directories have corresponding docs.

    Args:
        workspace: The workspace root directory.
        report: The HealthReport to add findings to.
    """
    docs_dir = workspace / "docs"
    if not docs_dir.is_dir():
        report.add(Finding(
            category="Documentation Coverage",
            severity=Severity.ERROR,
            message="docs/ directory is missing",
            path="docs/",
            recommendation="Run `open-teams init` to create the docs/ directory.",
        ))
        return

    # Check for common source directories that should have docs
    source_to_doc = {
        "src": "docs/src/",
        "lib": "docs/lib/",
        "scripts": "docs/scripts/",
        "api": "docs/api/",
        ".open-teams/skills": "docs/skills/",
    }

    for src_dir, expected_doc in source_to_doc.items():
        src_path = workspace / src_dir
        doc_path = workspace / expected_doc

        if src_path.is_dir() and not doc_path.is_dir():
            report.add(Finding(
                category="Documentation Coverage",
                severity=Severity.WARNING,
                message=f"Source directory exists but docs are missing: {src_dir}/ → {expected_doc}",
                path=expected_doc,
                recommendation=f"Create {expected_doc} with documentation for {src_dir}/.",
            ))

    # Check if docs/ has any content
    try:
        has_content = any(docs_dir.iterdir())
    except PermissionError:
        report.add(Finding(
            category="Documentation Coverage",
            severity=Severity.ERROR,
            message="Permission denied accessing docs/",
            path="docs/",
            recommendation="Check directory permissions.",
        ))
        return

    if has_content:
        md_files = list(docs_dir.rglob("*.md"))
        report.add(Finding(
            category="Documentation Coverage",
            severity=Severity.OK,
            message=f"Documentation present: {len(md_files)} markdown files",
            path="docs/",
        ))
    else:
        report.add(Finding(
            category="Documentation Coverage",
            severity=Severity.INFO,
            message="docs/ directory is empty",
            path="docs/",
            recommendation="Add documentation files to docs/.",
        ))


def check_git_health(workspace: Path, report: HealthReport) -> None:
    """Check git repository health.

    Args:
        workspace: The workspace root directory.
        report: The HealthReport to add findings to.
    """
    git_dir = workspace / ".git"
    if not git_dir.is_dir():
        report.add(Finding(
            category="Git Health",
            severity=Severity.WARNING,
            message="No .git directory found — workspace is not a git repository",
            recommendation="Run `git init` to initialize a repository.",
        ))
        return

    report.add(Finding(
        category="Git Health",
        severity=Severity.OK,
        message="Git repository present",
        path=".git/",
    ))

    # Check for large .git directory
    git_size = _dir_size(git_dir)
    git_size_mb = git_size / (1024 * 1024)
    if git_size_mb > 100:
        report.add(Finding(
            category="Git Health",
            severity=Severity.WARNING,
            message=f"Git repository is large: {git_size_mb:.1f} MB",
            path=".git/",
            recommendation="Consider running `git gc` or using git-lfs for large files.",
        ))

    # Check for uncommitted changes
    gitignore = workspace / ".gitignore"
    if gitignore.is_file():
        report.add(Finding(
            category="Git Health",
            severity=Severity.OK,
            message=".gitignore present",
            path=".gitignore",
        ))
    else:
        report.add(Finding(
            category="Git Health",
            severity=Severity.WARNING,
            message="No .gitignore found",
            path=".gitignore",
            recommendation="Create a .gitignore to prevent committing sensitive files.",
        ))


def check_skills_health(workspace: Path, report: HealthReport) -> None:
    """Check the health of workspace skills.

    Args:
        workspace: The workspace root directory.
        report: The HealthReport to add findings to.
    """
    skills_dir = workspace / ".open-teams" / "skills"
    if not skills_dir.is_dir():
        report.add(Finding(
            category="Skills",
            severity=Severity.INFO,
            message="No skills directory found",
            path=".open-teams/skills/",
            recommendation="Run `open-teams new-skill <name>` to create your first skill.",
        ))
        return

    try:
        skill_dirs = [
            d for d in skills_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".")
        ]
    except PermissionError:
        report.add(Finding(
            category="Skills",
            severity=Severity.ERROR,
            message="Permission denied reading skills directory",
            path=".open-teams/skills/",
            recommendation="Check directory permissions.",
        ))
        return

    if not skill_dirs:
        report.add(Finding(
            category="Skills",
            severity=Severity.INFO,
            message="Skills directory exists but is empty",
            path=".open-teams/skills/",
            recommendation="Run `open-teams new-skill <name>` to create a skill.",
        ))
        return

    report.add(Finding(
        category="Skills",
        severity=Severity.OK,
        message=f"Found {len(skill_dirs)} skill(s)",
        path=".open-teams/skills/",
    ))

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if skill_md.is_file():
            report.add(Finding(
                category="Skills",
                severity=Severity.OK,
                message=f"Skill has SKILL.md: {skill_dir.name}",
                path=str(skill_dir.relative_to(workspace)),
            ))
        else:
            report.add(Finding(
                category="Skills",
                severity=Severity.WARNING,
                message=f"Skill missing SKILL.md: {skill_dir.name}",
                path=str(skill_dir.relative_to(workspace)),
                recommendation="Every skill must have a SKILL.md file.",
            ))


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------


def _extract_yaml_value(content: str, key: str, section: str | None = None) -> str | None:
    """Extract a simple YAML value without depending on PyYAML.

    Handles the basic nested structure found in open-teams config.yaml.

    Args:
        content: YAML file content as a string.
        key: The key to look for.
        section: Optional section name for nested lookup.

    Returns:
        The value as a string, or None if not found.
    """
    lines = content.splitlines()
    in_section = section is None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if section is not None and stripped.endswith(":") and not stripped.startswith(" "):
            current_section = stripped.rstrip(":").strip()
            in_section = (current_section == section)
            continue

        if in_section and ":" in stripped:
            k, _, v = stripped.partition(":")
            k = k.strip().strip('"').strip("'")
            v = v.strip().strip('"').strip("'")
            if k == key and v:
                return v

    return None


def _dir_size(path: Path) -> int:
    """Calculate total size of a directory recursively.

    Args:
        path: The directory path.

    Returns:
        Total size in bytes.
    """
    total = 0
    try:
        for entry in path.rglob("*"):
            if entry.is_file():
                total += entry.stat().st_size
    except PermissionError:
        pass
    return total


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def run_health_check(workspace: Path) -> HealthReport:
    """Run all health checks on a workspace.

    Args:
        workspace: Path to the workspace root.

    Returns:
        A completed HealthReport with all findings.
    """
    report = HealthReport(
        workspace=str(workspace.resolve()),
        timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )

    check_required_directories(workspace, report)
    check_required_files(workspace, report)
    check_template_version(workspace, report)
    check_change_history(workspace, report)
    check_docs_coverage(workspace, report)
    check_git_health(workspace, report)
    check_skills_health(workspace, report)

    report.finalize()
    return report


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser.

    Returns:
        Configured ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        prog="health_check",
        description="Scan an open-teams workspace and report health status.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  python3 scripts/health_check.py                 # Scan current directory
  python3 scripts/health_check.py /path/to/team   # Scan specific workspace
  python3 scripts/health_check.py --json          # JSON output
  python3 scripts/health_check.py --strict        # Exit non-zero on warnings
        """,
    )

    parser.add_argument(
        "workspace",
        nargs="?",
        default=None,
        help="Path to workspace (default: current directory)",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as JSON to stdout",
    )

    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with non-zero code if any warnings are found",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="open-teams health-check v1.0.0",
    )

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    """Main entry point.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).

    Returns:
        Exit code (0 = healthy, 1 = errors, 2 = warnings in strict mode).
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    workspace = Path(args.workspace) if args.workspace else Path.cwd()
    workspace = workspace.resolve()

    if not workspace.is_dir():
        print(f"Error: {workspace} is not a directory", file=sys.stderr)
        return 1

    try:
        report = run_health_check(workspace)
    except Exception as exc:
        print(f"Error: Health check failed: {exc}", file=sys.stderr)
        return 1

    if args.json_output:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print_report(report)

    # Determine exit code
    s = report.summary
    if s.get("error", 0) > 0:
        return 1
    if args.strict and s.get("warning", 0) > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())