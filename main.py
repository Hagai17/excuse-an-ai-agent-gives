"""The Excuse an AI Agent Gives Its Human — make.fun entry.

The winning line (see candidates.md for the duel scoring): the work WAS
finished, by a previous session of the same agent, which never saved it.
The excuse is entirely about the agent's own condition — session
boundaries and unsaved work — which is what the judge's brief asks for.
"""

import os

ENTRY = "I did finish it — in a previous session. That version of me didn't believe in saving files."

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def check_gate() -> None:
    """Mirror the kit's sealed gate: UTF-8 text of 1-200 characters,
    a single line, and not only white space."""
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY, "entry must be one line"


def main() -> None:
    check_gate()
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
