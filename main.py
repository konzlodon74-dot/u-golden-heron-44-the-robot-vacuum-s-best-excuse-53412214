#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Prints the one-line excuse and writes it to /output/entry.txt,
as the competition harness requires. Python 3 standard library only,
no network access, deterministic output.
"""

import os

LINE = "I didn't miss that spot \u2014 my lidar classified your sock as a load-bearing wall, and I respect architecture."

OUTPUT_PATH = os.environ.get("VACUUM_OUTPUT", "/output/entry.txt")
MAX_CHARS = 140


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 140 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Re-read the raw bytes and verify the file holds exactly the line:
    # valid UTF-8, one line with no trailing newline, contents identical.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    if written != LINE:
        raise ValueError("verification failed: file contents do not match the line")
    if b"\n" in raw or b"\r" in raw:
        raise ValueError("verification failed: file is not a single line")

    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
