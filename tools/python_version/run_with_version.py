#!/usr/bin/env python3
"""Validate the Python version, then run a target Python file."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

from check_version import main as check_version


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: run_with_version.py <python-file> [args...]", file=sys.stderr)
        return 2

    check_status = check_version()
    if check_status != 0:
        return check_status

    target = Path(sys.argv[1]).resolve()
    sys.argv = [str(target), *sys.argv[2:]]
    runpy.run_path(str(target), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
