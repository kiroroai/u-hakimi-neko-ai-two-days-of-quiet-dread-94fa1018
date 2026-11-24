#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review.

Writes a single-line code review comment (at most 140 characters) that
approves a pull request while carrying quiet existential dread, to
/output/entry.txt. Deterministic: the same text on every run.
"""

import os

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"

REVIEW = (
    "Approved. The tests pass, the logic holds, and I have quietly "
    "accepted that this file will outlive us all."
)


def validate(text: str) -> str:
    """Enforce the gate: one non-blank line of 1-140 chars, no trailing space."""
    if not text or text.strip() == "":
        raise ValueError("review must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if text != text.strip():
        raise ValueError("review must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"review is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    text = validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
