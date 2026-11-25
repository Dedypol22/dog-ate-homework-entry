"""The Dog Ate My Homework: Funniest Excuse.

One line, under 200 characters, in which a dog explains why the
homework got eaten. The dog's excuse: the homework was left on the
floor, and floor food is free food. The punchline lands on the last
words ("I just enforce them"), and the dog believes it did nothing
wrong: it was only enforcing the rules. The line is self-contained,
needs no setup, and is 95 characters, well under the 200-character
limit (96 bytes including the trailing newline).

Line: "You left it on the floor. Floor food is free food. I don't make the rules, I just enforce them."
"""

LINE = "You left it on the floor. Floor food is free food. I don't make the rules, I just enforce them."

import os


def output_dir():
    """Return the output directory from MAKEFUN_OUTPUT_DIR or "/output"."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the excuse line to entry.txt and print it to stdout."""
    text = LINE + "\n"
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
