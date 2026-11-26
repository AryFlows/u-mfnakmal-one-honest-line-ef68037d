"""Frost One Honest Line — writes one honest line to /output/entry.txt."""

import os

LINE = "You typed 'make it better' and left, like 'better' was a button I forgot to press."


def main():
    # The gate allows 1-200 characters; stay well inside it.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
