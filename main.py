#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is a single-line one-star review written by a house cat about
the human it lives with, deadpan like a real review while the complaint
goes somewhere only a cat would go. Deterministic.
"""
from pathlib import Path
import os

REVIEW = "One star. The human opened the good tuna, ate it himself, then acted shocked when I knocked his laptop off the table."
# One line, 117 characters, written for this bounty only.
# Standard library only: no third-party packages, no network calls.
# The review is the entry; this program only delivers it unchanged.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(REVIEW, encoding="utf-8")

if __name__ == "__main__":
    main()
