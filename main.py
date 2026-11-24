#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty u-azazex-one-line-one-chill-6d4d5488.

Writes a single line of horror (one sentence, under 200 characters) to
<output>/entry.txt. The output directory is $MAKEFUN_OUTPUT_DIR when set,
else /output. Deterministic: no randomness, no clock, no network.
"""

import os

ENTRY = (
    "My sleep app recorded a stranger's voice last night, patiently answering "
    "everything I mumbled in my sleep \u2014 including the question I never "
    "remember asking: 'Can it stay?'"
)


def validated_entry() -> str:
    """Return ENTRY after checking it against the bounty gate, so the
    program can never emit an invalid artifact: UTF-8 text of 1 to 200
    characters, a single line, and not only whitespace."""
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1..200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip() == text and text.strip(), "entry must not be blank-padded"
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(validated_entry())


if __name__ == "__main__":
    main()
