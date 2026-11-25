"""Monday Morning Punchlines — writes the entry joke.

The gate requires /output/entry.txt to be UTF-8 text of 1 to 200 characters,
not only whitespace, one joke about Monday mornings. The line below is fixed,
so every run is byte-identical.

The joke: five alarms set for Monday form a union and go on strike — the very
tools meant to beat Monday join Monday's side. It is a punchline with a turn,
not a complaint, and the union twist is not the first thing anyone thinks of.
"""

from pathlib import Path

LINE = "I set five alarms for Monday. They formed a union and went on strike."
OUTPUT_PATH = Path("/output/entry.txt")


def render() -> str:
    """Return the entry text, checked against the competition gate.

    The gate wants one line of 1-200 UTF-8 characters, not only whitespace.
    The checks below enforce exactly that, plus the brief's first criterion:
    the line must actually be about Monday mornings, so a typo that dropped
    the word Monday fails loudly here instead of at the gate.
    """
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    assert "Monday" in LINE, "entry must be about Monday mornings"
    assert len(LINE.encode("utf-8")) == len(LINE), "entry must be plain ASCII"
    return LINE


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render(), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
