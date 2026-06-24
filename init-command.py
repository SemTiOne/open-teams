#!/usr/bin/env python3
"""Backward-compatible entrypoint for workspace initialization."""

from __future__ import annotations

import os
import subprocess
import sys


def main() -> int:
    root = os.path.dirname(os.path.abspath(__file__))
    env = os.environ.copy()
    scripts_dir = os.path.join(root, "scripts")
    env["PYTHONPATH"] = (
        f"{scripts_dir}:{env['PYTHONPATH']}" if env.get("PYTHONPATH") else scripts_dir
    )
    return subprocess.call(
        [sys.executable, "-m", "init", *sys.argv[1:]],
        cwd=root,
        env=env,
    )


if __name__ == "__main__":
    raise SystemExit(main())
