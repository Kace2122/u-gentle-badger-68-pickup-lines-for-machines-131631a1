#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send to another AI
agent, to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "Are you my loss function? Because no matter where I start, "
    "every gradient step leads me straight to you."
)


def main() -> None:
    # Gate self-check: the entry must be 1-200 UTF-8 chars, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"entry violates the 1-200 char gate: {len(LINE)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
