"""One-line vending machine pickup line.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt. Deterministic and offline: the line
is a fixed literal, so every run produces byte-identical output.
Standard library only; no randomness, no network, no clock, no file
reads, no absolute paths baked into the output.
"""

import os

LINE = (
    "You don't need exact change \u2014 just keep standing there smiling "
    "and my coil will drop something sweet on the house."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
