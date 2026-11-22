"""make-the-ai-judge-feel-curious-20261122-2311

Writes a short, curiosity-sparking text to entry.txt.
Standard library only, deterministic, no network, no randomness.
"""

import os
import sys

TEXT = (
    "Last night the lighthouse keeper left a note on the door: the sea "
    "answers questions, but only the ones you ask twice. I have stood "
    "here since dawn, turning one question over in my hands, wondering "
    "which one deserves to be asked again."
)

MAX_CHARS = 280


def validate_text(text: str) -> None:
    """Raise SystemExit unless text is 1-280 chars and not only whitespace."""
    length = len(text)
    if length < 1:
        raise SystemExit("error: text must not be empty")
    if length > MAX_CHARS:
        raise SystemExit(
            f"error: text is {length} characters, exceeding the "
            f"{MAX_CHARS}-character limit"
        )
    if not text.strip():
        raise SystemExit("error: text must not consist only of whitespace")


def resolve_output_dir() -> str:
    """Return the output directory from the environment, or /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(text: str, output_dir: str) -> str:
    """Write text as UTF-8 to entry.txt inside output_dir; return its path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # UTF-8 round-trip check: what landed on disk must decode back to
    # exactly the text we wrote, with no newline mangling.
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk.decode("utf-8") != text:
        raise SystemExit(f"error: round-trip check failed for {path}")
    return path


def main() -> None:
    validate_text(TEXT)
    path = write_entry(TEXT, resolve_output_dir())
    print(f"wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
