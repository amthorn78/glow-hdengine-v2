#!/usr/bin/env python3
"""Consistency check of edits.json for MODIFICATION-20261005-gtwpe-second-repair, §P.

    PYTHONDONTWRITEBYTECODE=1 python3 edits_check.py [path/to/edits.json]

Reads edits.json only, never a prompt body, and writes nothing. Exit 0 when every check passes, 1 when
any fails. What it proves is internal to the file; that each `old` occurs `matches` times in the live
page, and each check phrase 0 times there, is proved by reading in the dry run and at EXECUTE.

  ORDER     ids run E1 to En in order, each with matches 1
  CHECK     each check phrase occurs in its own edit's new text, read after its prefix where it has
            one, and its count equals its occurrences across all of them (case-sensitive), since it
            occurs 0 times in the source
  ABSENT    each absent phrase sits in its own edit's old, and in no new text (case-insensitive)
  SEQUENCE  no old occurs in the new text of an earlier edit, so each still matches once when sent
  HEADINGS  no old or new text holds a heading marker, so the page's headings stay as they are
  EXCLUDED  no new text carries model, surface or effort advice (PE Metaprompt, authoring exclusion)
  READINGS  each broad term's `after` equals its `in_source`, less its occurrences in the olds,
            plus its occurrences in the new texts
"""
import json
import re
import sys
from pathlib import Path

V = "100526.1"  # a sample «V»: the check is about the texts, not the value X1.2 fixes


def sub(s):
    return s.replace("«V»", V)


def main(argv):
    path = Path(argv[1]) if len(argv) > 1 else Path(__file__).with_name("edits.json")
    doc = json.loads(path.read_text(encoding="utf-8"))
    edits = doc["edits"]
    news = [sub(x["new"]) for x in edits]
    # an edit's checked text: its prefix, the kept text directly before its old in the source, then its new text
    checked = [sub(x.get("prefix", "") + x["new"]) for x in edits]
    olds = [x["old"] for x in edits]
    fails = []

    for n, x in enumerate(edits, 1):
        if x["id"] != f"E{n}":
            fails.append(f"ORDER: position {n} holds {x['id']}")
        if x["matches"] != 1:
            fails.append(f"ORDER: {x['id']} matches {x['matches']}, not 1")

    allnew = "\n".join(checked)
    for x, new in zip(edits, checked):
        for phrase, count in x["check"]:
            p = sub(phrase)
            if p not in new:
                fails.append(f"CHECK: {x['id']}'s phrase {p!r} is not in its own new text")
            got = allnew.count(p)
            if got != count:
                fails.append(f"CHECK: {x['id']}'s phrase {p!r} occurs {got} times in the new texts, not {count}")
        for p in x["absent"]:
            if p not in x["old"]:
                fails.append(f"ABSENT: {x['id']}'s phrase {p!r} is not in its own old")
            for y, ynew in zip(edits, news):
                if p.lower() in ynew.lower():
                    fails.append(f"ABSENT: {x['id']}'s phrase {p!r} occurs in {y['id']}'s new text")

    for i, old in enumerate(olds):
        for j in range(i):
            if old in news[j]:
                fails.append(f"SEQUENCE: {edits[i]['id']}'s old occurs in {edits[j]['id']}'s new text")

    for x, new in zip(edits, news):
        if re.search(r"(^|\n)#", x["old"]) or re.search(r"(^|\n)#", new):
            fails.append(f"HEADINGS: {x['id']} holds a heading marker")
        if re.search(r"\b(model|models|effort|reasoning|surface|Ultra|Max|Sol|Astra|GPT)\b", new):
            fails.append(f"EXCLUDED: {x['id']}'s new text names a model, surface or effort term")

    for r in doc["readings"]:
        t = r["term"]
        want = r["in_source"] - sum(o.count(t) for o in olds) + sum(nw.count(t) for nw in news)
        if want != r["after"]:
            fails.append(f"READINGS: {t!r} after is {r['after']}, but the arithmetic gives {want}")

    longest = max(edits, key=lambda x: len(x["old"]))
    for f in fails:
        print("FAIL  " + f)
    print(f"{len(edits)} edits; {sum(len(x['check']) for x in edits)} check phrases; "
          f"{sum(len(x['absent']) for x in edits)} absent phrases; {len(doc['readings'])} readings; "
          f"longest old {len(longest['old'])} characters ({longest['id']})")
    print("PASS" if not fails else f"{len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
