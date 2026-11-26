"""Write the entry for make.fun's "One Word, One Username" bounty.

The entry is the entrant's own make.fun username and nothing else: one
word, at most 30 characters. This program writes that username to
entry.txt in the output directory, deterministically: the same word,
byte for byte, on every run. Standard library only; no network.
"""

import os

LINE = "shangenb666"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 30:
        raise ValueError("username must be 1 to 30 characters")
    if not LINE.strip():
        raise ValueError("username must not be only whitespace")
    if LINE.split() != [LINE]:
        raise ValueError("username must be a single word, no spaces or padding")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader owns it and runs
    # this program as a different user, so chmod would fail the run.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # Best effort only: the file is ours, but a permission problem
    # must never fail the run.
    try:
        os.chmod(DESTINATION, 0o644)
    except PermissionError:
        pass
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
