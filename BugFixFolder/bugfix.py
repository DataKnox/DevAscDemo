#!/usr/bin/env python3
"""Fix small formatting bugs in Python files."""

from pathlib import Path
import sys


def fix_file(path):
    text = path.read_text(encoding="utf-8")
    lines = [line.rstrip() for line in text.splitlines()]
    fixed = "\n".join(lines)
    if fixed:
        fixed += "\n"

    if fixed != text:
        path.write_text(fixed, encoding="utf-8")
        print(f"Fixed: {path}")
        return 1
    return 0


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    files = [folder] if folder.is_file() else folder.rglob("*.py")
    count = sum(fix_file(path) for path in files if path.is_file())
    print(f"BugFix Buddy cleaned {count} file(s)!")


if __name__ == "__main__":
    main()
