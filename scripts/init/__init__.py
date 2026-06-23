"""
open-teams init — Workspace initialization package.

Architecture:
    ui.py        — Terminal styling (Style) + output helpers (print_*, prompt, etc.)
    templates.py — Template skeleton data (directories, files, content)
    workspace.py — Core initialization logic (init_workspace, run_interactive)
    cli.py       — CLI argument parsing + main entry point

Design principles:
    - Zero external dependencies (stdlib only)
    - ANSI color detection (NO_COLOR / FORCE_COLOR support)
    - Idempotent: safe to run multiple times
    - Testable: pure functions where possible
"""

from init.cli import main
from init.workspace import init_workspace, run_interactive

__all__ = ["main", "init_workspace", "run_interactive"]
__version__ = "1.0.0"
