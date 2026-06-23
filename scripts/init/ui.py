"""
init/ui.py — Terminal styling and user interaction helpers.

Provides:
    Style      — ANSI color constants with automatic TTY detection
    print_*()  — Formatted output (header, success, error, warning, info, progress)
    prompt()   — Styled user input with default value support
    prompt_choice() — Numeric selection from a list
    print_separator() — Horizontal rule

Design: zero-dependency, honors NO_COLOR / FORCE_COLOR, handles EOF/KeyboardInterrupt.
"""

from __future__ import annotations

import os
import sys

# ---------------------------------------------------------------------------
# ANSI / Terminal color helpers
# ---------------------------------------------------------------------------


class Style:
    """Terminal styling constants for beautiful output."""

    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    _inited = False

    @classmethod
    def _init(cls) -> None:
        """Detect terminal color support once and strip ANSI if unsupported."""
        if cls._inited:
            return
        cls._inited = True
        if not cls._supports_color():
            for attr in dir(cls):
                if not attr.startswith("_") and not callable(getattr(cls, attr, None)):
                    setattr(cls, attr, "")

    @staticmethod
    def _supports_color() -> bool:
        """Detect whether the terminal supports ANSI color codes."""
        if not hasattr(sys.stdout, "isatty"):
            return False
        if not sys.stdout.isatty():
            return False
        if os.environ.get("NO_COLOR"):
            return False
        if os.environ.get("FORCE_COLOR"):
            return True
        return os.environ.get("TERM", "") != "dumb"


# Run detection on module import
Style._init()

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

SEPARATOR_WIDTH = 52


def print_header(text: str) -> None:
    """Print a bold header with rocket emoji."""
    print(f"\n{Style.BOLD}{Style.BRIGHT_CYAN}🚀 {text}{Style.RESET}\n")


def print_separator() -> None:
    """Print a horizontal separator line."""
    print(f"{Style.DIM}{'─' * SEPARATOR_WIDTH}{Style.RESET}")


def print_step(icon: str, text: str) -> None:
    """Print a step indicator with icon."""
    print(f"   {icon} {text}")


def print_success(text: str) -> None:
    """Print a success message."""
    print(f"   {Style.BRIGHT_GREEN}✅ {text}{Style.RESET}")


def print_warning(text: str) -> None:
    """Print a warning message."""
    print(f"   {Style.BRIGHT_YELLOW}⚠️  {text}{Style.RESET}")


def print_error(text: str) -> None:
    """Print an error message."""
    print(f"   {Style.BRIGHT_RED}❌ {text}{Style.RESET}")


def print_info(text: str) -> None:
    """Print an informational message."""
    print(f"   {Style.BRIGHT_BLUE}ℹ️  {text}{Style.RESET}")


def print_progress(text: str) -> None:
    """Print a progress / in-progress message."""
    print(f"   {Style.BRIGHT_YELLOW}⏳ {text}{Style.RESET}")


def prompt(text: str, default: str = "") -> str:
    """Prompt the user for input with styling.

    Args:
        text: The prompt text.
        default: Default value shown in brackets.

    Returns:
        User input, or default if empty.

    Raises:
        SystemExit(1) on EOF or KeyboardInterrupt.
    """
    prompt_text = f"   {Style.BOLD}{Style.BRIGHT_WHITE}{text}{Style.RESET}"
    if default:
        prompt_text += f" {Style.DIM}[{default}]{Style.RESET}"
    prompt_text += f"\n   {Style.BRIGHT_BLUE}>{Style.RESET} "
    try:
        value = input(prompt_text).strip()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{Style.BRIGHT_YELLOW}⚠️  Operation cancelled.{Style.RESET}")
        sys.exit(1)
    return value if value else default


def prompt_choice(text: str, choices: list[str], default: int = 0) -> str:
    """Prompt the user to select from a list of choices.

    Args:
        text: The prompt text.
        choices: List of choice strings.
        default: Index of the default choice.

    Returns:
        The selected choice string.

    Raises:
        SystemExit(1) on EOF or KeyboardInterrupt.
    """
    print(f"\n   {Style.BOLD}{Style.BRIGHT_WHITE}{text}{Style.RESET}")
    for i, choice in enumerate(choices):
        marker = " (default)" if i == default else ""
        print(
            f"     {Style.BRIGHT_CYAN}[{i + 1}]{Style.RESET}"
            f" {choice}{Style.DIM}{marker}{Style.RESET}"
        )
    try:
        raw = input(f"   {Style.BRIGHT_BLUE}Choice [{default + 1}]:{Style.RESET} ").strip()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{Style.BRIGHT_YELLOW}⚠️  Operation cancelled.{Style.RESET}")
        sys.exit(1)
    if not raw:
        return choices[default]
    try:
        idx = int(raw) - 1
        if 0 <= idx < len(choices):
            return choices[idx]
        print_warning(f"Invalid choice, using default: {choices[default]}")
        return choices[default]
    except ValueError:
        print_warning(f"Invalid input, using default: {choices[default]}")
        return choices[default]
