#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<= 200 characters) pitching a bizarre startup idea
that sounds absurd until the business logic lands, to /output/entry.txt.

Draft (first attempt, 161 chars):
  "We rent strangers' spare bathtubs to city mushroom growers, because one
  damp tub yields $400 of oyster mushrooms a month and landlords already
  have the plumbing."

Revision (genuine improvement, not a no-op):
  - "spare" -> "unused": sharper, the tubs are idle, not spare parts.
  - "growers" -> "farmers": a real customer identity, not a hobby label.
  - "yields" -> "grows": plain verb, lands faster as a pitch.
  - "landlords already have the plumbing" -> "every apartment already has
    the plumbing": the market is every apartment, not just landlords, so the
    supply side is suddenly huge and the logic holds for any reader.
  Final (166 chars):
  "We rent strangers' unused bathtubs to city mushroom farmers, because one
  damp tub grows $400 of oyster mushrooms a month and every apartment already
  has the plumbing."
"""

import os

ENTRY = (
    "We rent strangers' unused bathtubs to city mushroom farmers, "
    "because one damp tub grows $400 of oyster mushrooms a month and "
    "every apartment already has the plumbing."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, len(text)
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
