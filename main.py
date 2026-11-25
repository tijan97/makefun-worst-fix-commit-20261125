"""Worst Fix Ever: Funniest Commit Message.

Prints the entry line to stdout and writes it to entry.txt in the
output directory the grader provides (MAKEFUN_OUTPUT_DIR, OUTPUT_DIR,
or /output). The line is a single commit message, at most 100
characters, for a bug fix that made everything worse.
"""

import os
import sys

ENTRY = "fix: speed up the slow query by caching the wrong answer forever"


def main() -> int:
    if not ENTRY.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if len(ENTRY) > 100:
        print("error: entry is %d characters, over the 100 limit" % len(ENTRY),
              file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            print("error: written entry does not match", file=sys.stderr)
            return 1
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
