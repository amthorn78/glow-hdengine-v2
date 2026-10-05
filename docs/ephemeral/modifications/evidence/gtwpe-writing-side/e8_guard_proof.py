#!/usr/bin/env python3
"""P10, added in the repair round (L8): fire E8's readback rule on synthetic bound-prompt texts, for
MODIFICATION-20261005-gtwpe-writing-side, §P.

    PYTHONDONTWRITEBYTECODE=1 python3 e8_guard_proof.py [path/to/gtwpe.decision-record.md]

E8 makes the prompt route's readback check, for a prompt that writes a redlines Markdown file or a
final updated PF Markdown file, GTWPE-D1's proof-log requirement and each of its minimum items present,
by phrase. This script takes the phrases from GTWPE-D1 itself: the requirement as "separate proof log",
and the eight minimum items as Nathan worded them in the decision record. It builds a synthetic
bound-prompt text that carries all of them, eight texts that each lack one minimum item, and one text
that keeps the items but has no separate proof log, and applies the rule to each. It reads no prompt
body and writes nothing. Exit 0 when the rule passes the complete text and fails every other one,
naming what is missing; 1 otherwise.
"""
import sys
from pathlib import Path

REQUIREMENT = "separate proof log"


def minimum_items(record):
    lines = record.read_text(encoding="utf-8").splitlines()
    start = next(i for i, l in enumerate(lines) if "Each proof log must, at minimum, record:" in l)
    items = []
    for l in lines[start + 1:]:
        s = l.strip()
        if s in (">", ""):
            if items:
                break
            continue
        if not s.startswith("> * "):
            break
        items.append(s[4:])
    return items


def readback(text, phrases):
    """E8's rule: every phrase present (case-insensitive). Returns the phrases that are missing."""
    low = text.lower()
    return [p for p in phrases if p.lower() not in low]


def bound_prompt(items, requirement=REQUIREMENT):
    return ("Write the redlines Markdown file for the target, and beside it a " + requirement +
            " that records: " + "; ".join(items) + ".")


def main(argv):
    if len(argv) > 1:
        record = Path(argv[1])
    else:
        docs = Path(__file__).resolve().parents[4]
        record = docs / "prompt_ecosystem_management" / "gtwpe" / "gtwpe.decision-record.md"
    items = minimum_items(record)
    phrases = [REQUIREMENT] + items
    fails = []
    print(f"GTWPE-D1's minimum items read from {record.name}: {len(items)}")
    if len(items) != 8:
        fails.append(f"expected 8 minimum items, read {len(items)}")

    missing = readback(bound_prompt(items), phrases)
    print(f"complete text: {'passes' if not missing else 'FAILS, missing ' + repr(missing)}")
    if missing:
        fails.append("the complete text fails the rule")

    for n, item in enumerate(items, 1):
        missing = readback(bound_prompt([x for x in items if x != item]), phrases)
        print(f"text lacking item {n}: {'fails, missing ' + repr(missing) if missing else 'PASSES'}")
        if missing != [item]:
            fails.append(f"the text lacking item {n} is not failed on that item alone")

    missing = readback(bound_prompt(items, requirement="report"), phrases)
    print(f"text with no separate proof log: {'fails, missing ' + repr(missing) if missing else 'PASSES'}")
    if missing != [REQUIREMENT]:
        fails.append("the text with no separate proof log is not failed on the requirement alone")

    for f in fails:
        print("FAIL  " + f)
    print("PASS: the rule passes the complete text and fails each deficient one" if not fails
          else f"{len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
