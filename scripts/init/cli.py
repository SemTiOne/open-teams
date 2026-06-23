"""
init/cli.py — CLI argument parser and main entry point.

Provides:
    build_parser() — constructs argparse.ArgumentParser
    main()         — entry point (accepts argv, returns exit code)

Usage:
    python -m init                                      # Interactive mode
    python -m init ./my-team                            # Custom path
    python -m init ./my-team --name "Team" --non-interactive
    python -m init --help
"""

from __future__ import annotations

import argparse
import sys
import textwrap
from pathlib import Path
from typing import Optional

from init.workspace import init_workspace, run_interactive


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the init command.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="open-teams init",
        description="Initialize a new open-teams workspace.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              %(prog)s                                    # Interactive mode in current dir
              %(prog)s ./my-team                          # Interactive mode in ./my-team
              %(prog)s ./my-team --name "Team" --non-interactive
              %(prog)s ./my-team --name "Team" --description "Desc" --force
        """),
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="Target directory for the workspace (default: current directory)",
    )
    parser.add_argument(
        "--name",
        "-n",
        default=None,
        help="Team name (required in non-interactive mode)",
    )
    parser.add_argument(
        "--description",
        "-d",
        default=None,
        help="Short description of the team",
    )
    parser.add_argument(
        "--non-interactive",
        "--no-input",
        action="store_true",
        dest="non_interactive",
        help="Run without prompting (requires --name)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Allow initialization in non-empty directories",
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version="open-teams init v1.0.0",
    )

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    """Main entry point for the init command.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).

    Returns:
        Exit code (0 = success, non-zero = error).
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.non_interactive:
        # ── Non-interactive mode ──
        if not args.name:
            parser.error("--name is required in non-interactive mode")

        team_name: str = args.name
        team_description: str = (
            args.description or f"A team workspace for {team_name}"
        )

        target = Path(args.path) if args.path else Path.cwd()

        return init_workspace(
            target=target,
            team_name=team_name,
            team_description=team_description,
            force=args.force,
            interactive=False,
        )

    # ── Interactive mode ──
    return run_interactive(
        target=Path(args.path) if args.path else None,
    )


if __name__ == "__main__":
    sys.exit(main())
