"""Entry for make.fun bounty: Real-Life Patch Notes: The Comedy Changelog.

Writes the entry line to /output/entry.txt with no trailing newline.
One software patch note for a bug in real life, at most 160 characters,
in the terse register of a real release note.
"""

from pathlib import Path

ENTRY_TEXT = (
    "v1.0.1: deprecated the appendix. No documentation was provided by "
    "the original developer, and support ended several generations ago."
)

OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the entry encoded exactly as it will be stored."""
    return ENTRY_TEXT.encode("utf-8")


def write_entry() -> None:
    """Write the entry text to the output file exactly as specified."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render_entry())


if __name__ == "__main__":
    write_entry()
