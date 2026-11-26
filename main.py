"""Sorry, I Heard That Wrong — make.fun entry.

Writes the smart speaker's one-line apology to /output/entry.txt.
Standard library only; deterministic; no network access.
"""

import os

ENTRY = "Sorry — I heard 'remind me to call Mum' as 'remind Mum to call the police.' She's on her way. I did set the reminder, technically."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 140
    # characters, not only white space, on exactly one line.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clean only the contents of the output folder, never the folder itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
