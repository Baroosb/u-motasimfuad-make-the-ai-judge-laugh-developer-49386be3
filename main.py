#!/usr/bin/env python3
"""Write the entry for "Make the AI Judge Laugh: Developer Excuses".

The winning line, picked by a pairwise candidate tournament judged against
the bounty's published judge brief, is written byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""
import os

ENTRY = "It’s definitely a caching issue, fine it’s the API key I hardcoded in 2019 that expired minutes after deployment."


def main():
    # Mirror the bounty's gate: UTF-8 text of 1 to 200 characters, a single
    # line, and not only white space.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
