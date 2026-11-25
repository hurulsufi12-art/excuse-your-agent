"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line (the agent's excuse to its human for a shipped bug) to
/output/entry.txt. Stdlib only, deterministic, no network, no model call.
"""
import os
from pathlib import Path

ENTRY_TEXT = (
    "I ran out of context halfway through your code, guessed the rest, "
    "and shipped it anyway - the compiler started it, I just finished it."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def is_valid_entry(text):
    """Mirror of the sealed-scorer gate: UTF-8, 1-200 chars, non-whitespace,
    exactly one line."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not is_valid_entry(ENTRY_TEXT):
        raise SystemExit("ENTRY_TEXT fails the entry gate (1-200 chars, one line)")
    output = Path(os.environ.get("MAKEFUN_OUTPUT", DEFAULT_OUTPUT))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(ENTRY_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
