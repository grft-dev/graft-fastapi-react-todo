#!/usr/bin/env python
"""Run the complete backend and browser test suites."""

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def run_suite(name: str, command: list[str], working_directory: Path) -> bool:
    print(f"\nRunning {name}: {' '.join(command)}")
    result = subprocess.run(command, cwd=working_directory, check=False)
    return result.returncode == 0


def main() -> int:
    suites = [
        (
            "backend API tests",
            [sys.executable, "-m", "pytest", "tests"],
            PROJECT_ROOT / "backend",
        ),
        (
            "end-to-end tests",
            [sys.executable, "-m", "pytest", "test_todo_e2e.py"],
            PROJECT_ROOT / "e2e",
        ),
    ]

    results = [(name, run_suite(name, command, cwd)) for name, command, cwd in suites]

    print("\nTest summary")
    for name, passed in results:
        print(f"- {name}: {'passed' if passed else 'failed'}")

    return 0 if all(passed for _, passed in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
