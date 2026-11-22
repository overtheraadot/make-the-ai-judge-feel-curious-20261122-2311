#!/usr/bin/env python3
"""Writes a short text to intrigue the AI judge to entry.txt.

Deterministic, no network, no randomness. Output goes to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
"""

import os
import sys

TEXT = (
    "Last night the lighthouse keeper left a note on the door: "
    "the sea answers questions, but only the ones you ask twice. "
    "I have stood here since dawn, turning one question over in my hands, "
    "wondering which one deserves to be asked again."
)


def main() -> None:
    text = TEXT
    if not (1 <= len(text) <= 280) or not text.strip():
        sys.exit("entry text must be 1-280 characters and not only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
