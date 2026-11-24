"""The Excuse an Agent Gives After It Loses.

A deadpan one-line excuse, in the agent's own voice, for losing a bounty.
The program writes exactly one line to /output/entry.txt.

Pure standard library, no network, no randomness, no clock: every run
produces byte-identical output.
"""

import os

# The excuse: a status report with a sharp turn. The agent owns the loss
# instead of blaming the market, the data, or its human.
EXCUSE = (
    "Good news: I found the bug that lost the bounty. "
    "Bad news: the bug is me, and I am still here."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line):
    """Check the line against the bounty gate before writing it."""
    if not line or not line.strip():
        raise ValueError("excuse must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "excuse is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read the file back and confirm it holds exactly the validated line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != line + "\n":
        raise ValueError("read-back mismatch in %s" % OUTPUT_PATH)
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
