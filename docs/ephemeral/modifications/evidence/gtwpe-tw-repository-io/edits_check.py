#!/usr/bin/env python3
"""Consistency check of edits.json for MODIFICATION-20261005-gtwpe-tw-repository-io, §P.

    PYTHONDONTWRITEBYTECODE=1 python3 edits_check.py [edits.json] [--decision-record PATH] [--inject FAULT]

It reads edits.json and GTWPE's decision record only, and writes nothing. It never reads a prompt body:
whether each `old` occurs once in its member's page is checked by reading, in the dry run (P3) and at
X1.0, never by this script. Exit 0 when every check passes; 1 otherwise, naming each failure by its code.
--inject applies one named fault in memory, to show that its check fails (the dry run's P2).

  SHAPE     every edit has its fields; IDs are unique and numbered in file order within each member
  ONELINE   no `old` holds a newline; a `new` holds one only when the edit is marked blocks
  DIFFER    every `new` differs from its `old`
  VALUES    «V» occurs only in the two identity edits of each member, once in each `new`
  SHARED    edits under one rule key carry the same `old` and `new` in every member
  OVERLAP   within a member, no `old` occurs in another edit's `old`, or in any edit's `new`
  ABSENT    each absent_after phrase occurs in some `old` of its member and in no `new` of it
  COUNTS    counts_before minus the `old` texts plus the `new` texts is never negative; the result is printed
  PROOF     the bound members' `new` texts hold GTWPE-D1's requirement and its eight minimum items, as the
            decision record words them, and edits.json's copy of the items equals the record's
  EXCLUDED  no `new` holds the PE Metaprompt's excluded vocabulary as a whole word (model, effort, reasoning,
            workload, strength, assess, Ultra, Astra, GPT, surface)
"""
import copy
import json
import re
import sys
from pathlib import Path

# Whole words, so that "ChatGPT Library", a destination the new texts name in order to ban it, is not read as
# "GPT" the model family.
EXCLUDED = [r"\bmodels?\b", r"\beffort\b", r"\breasoning\b", r"\bworkload", r"\bstrength", r"\bassess",
            r"\bultra\b", r"\bastra\b", r"\bgpt\b", r"\bsurface\b"]
CHECK_PHRASES = ["GTWPE-MGMT-10", "`docs/pfcanon/` on `main`", "`docs/ephemeral/`", "as a pass", "separate proof log",
                 "`.proof-log` before `.md`", "attached files or repository paths", "attached file or a repository path",
                 "opened if none is", "stop and ask for it", "by repository path", "Prompt Version: «V»", "— «V»"]


def record_items(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
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


def inject(doc, fault):
    e = doc["edits"]
    def first(key, member=None):
        return next(x for x in e if x["rule_key"] == key and (member is None or x["member"] == member))
    if fault == "excluded":
        first("OUT-A")["new"] += " Choose a stronger model."
    elif fault == "proof":
        x = first("PL-B", "DRAIN-10")
        x["new"] = x["new"].replace("- Any validation or verification performed\n", "")
    elif fault == "overlap":
        first("OUT-C", "DRAIN-10")["new"] += " TW-MGMT-10 maintains this prompt."
    elif fault == "absent":
        doc["absent_after"]["TRIAGE"].append("Read the current")
    elif fault == "counts":
        doc["counts_before"]["APPLY-10"][4] = 2
    elif fault == "values":
        first("MNT-A", "TRIAGE")["new"] += " «V»"
    elif fault == "oneline":
        first("CAN-B", "TRIAGE")["new"] = "Google Drive copy,\nmemory"
    elif fault == "shared":
        first("CAN-A", "APPLY-10")["new"] = "from `docs/pfcanon/` on `main`"
    elif fault == "differ":
        x = first("OUT-B", "RECORD-20"); x["new"] = x["old"]
    elif fault == "shape":
        e[3]["id"] = e[2]["id"]
    else:
        raise SystemExit(f"unknown fault {fault!r}")


def check(doc, items_from_record):
    fails = []
    edits = doc["edits"]
    members = list(doc["members"])
    need = {"id", "member", "rule_key", "item", "rule", "where", "old", "new", "blocks"}
    ids = [x.get("id") for x in edits]
    if len(set(ids)) != len(ids):
        fails.append("SHAPE: duplicate edit IDs")
    for m in members:
        mine = [x for x in edits if x.get("member") == m]
        want = [f"{m}-{n:02d}" for n in range(1, len(mine) + 1)]
        if [x.get("id") for x in mine] != want:
            fails.append(f"SHAPE: {m}'s IDs are not numbered in file order")
    for x in edits:
        if not need <= set(x):
            fails.append(f"SHAPE: {x.get('id')} lacks {sorted(need - set(x))}")
        if x.get("member") not in members:
            fails.append(f"SHAPE: {x.get('id')} names an unknown member")
        if "\n" in x["old"]:
            fails.append(f"ONELINE: {x['id']}'s old holds a newline")
        if "\n" in x["new"] and not x["blocks"]:
            fails.append(f"ONELINE: {x['id']}'s new holds a newline but is not marked blocks")
        if x["new"] == x["old"]:
            fails.append(f"DIFFER: {x['id']}'s new equals its old")
        is_id = x["item"] == "identity"
        if ("«V»" in x["new"]) != is_id or (is_id and x["new"].count("«V»") != 1):
            fails.append(f"VALUES: {x['id']} misplaces «V»")
    for m in members:
        if sum(1 for x in edits if x["member"] == m and x["item"] == "identity") != 2:
            fails.append(f"VALUES: {m} has not exactly two identity edits")
    by_key = {}
    for x in edits:
        by_key.setdefault(x["rule_key"], set()).add((x["old"], x["new"]))
    for k, v in by_key.items():
        if len(v) != 1:
            fails.append(f"SHARED: rule {k} has {len(v)} different texts")
    for m in members:
        mine = [x for x in edits if x["member"] == m]
        for a in mine:
            for b in mine:
                if a is b:
                    continue
                if a["old"] in b["old"]:
                    fails.append(f"OVERLAP: {a['id']}'s old occurs in {b['id']}'s old")
                if a["old"] in b["new"]:
                    fails.append(f"OVERLAP: {a['id']}'s old occurs in {b['id']}'s new")
            if a["old"] in a["new"]:
                fails.append(f"OVERLAP: {a['id']}'s old survives in its own new")
        olds = [x["old"] for x in mine]
        news = [x["new"] for x in mine]
        for p in doc["absent_after"][m]:
            if not any(p in o for o in olds):
                fails.append(f"ABSENT: {m}: {p!r} occurs in no old, so no edit removes it")
            if any(p in n for n in news):
                fails.append(f"ABSENT: {m}: {p!r} occurs in a new text")
    terms = doc["counts_before"]["TERMS"]
    after = {}
    for m in members:
        mine = [x for x in edits if x["member"] == m]
        row = []
        for t, before in zip(terms, doc["counts_before"][m]):
            tl = t.lower()
            gone = sum(x["old"].lower().count(tl) for x in mine)
            added = sum(x["new"].lower().count(tl) for x in mine)
            if gone > before:
                fails.append(f"COUNTS: {m}: {t!r} occurs {gone} times in the old texts but {before} times in the body")
            row.append(before - gone + added)
        after[m] = row
    req = doc["gtwpe_d1"]["requirement"]
    if doc["gtwpe_d1"]["items"] != items_from_record:
        fails.append("PROOF: edits.json's eight items differ from the decision record's")
    for m in doc["gtwpe_d1"]["bound"]:
        text = "\n".join(x["new"] for x in edits if x["member"] == m).lower()
        for p in [req] + items_from_record:
            if p.lower() not in text:
                fails.append(f"PROOF: {m}'s new texts lack {p!r}")
    for x in edits:
        for w in EXCLUDED:
            if re.search(w, x["new"], re.IGNORECASE):
                fails.append(f"EXCLUDED: {x['id']}'s new holds {w!r}")
    return fails, after


def main(argv):
    args = argv[1:]
    fault = None
    rec = None
    if "--inject" in args:
        i = args.index("--inject"); fault = args[i + 1]; del args[i:i + 2]
    if "--decision-record" in args:
        i = args.index("--decision-record"); rec = args[i + 1]; del args[i:i + 2]
    here = Path(__file__).resolve().parent
    path = Path(args[0]) if args else here / "edits.json"
    if rec is None:
        rec = here.parents[3] / "prompt_ecosystem_management" / "gtwpe" / "gtwpe.decision-record.md"
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    if fault:
        doc = copy.deepcopy(doc)
        inject(doc, fault)
    items = record_items(rec)
    fails, after = check(doc, items)
    print(f"edits: {len(doc['edits'])}; GTWPE-D1 items read from the decision record: {len(items)}")
    olds = sorted(doc["edits"], key=lambda x: len(x["old"]), reverse=True)
    print(f"longest old: {olds[0]['id']} ({olds[0]['rule_key']}), {len(olds[0]['old'])} characters; next: "
          f"{olds[1]['id']} ({olds[1]['rule_key']}), {len(olds[1]['old'])}")
    print("counts after (" + ", ".join(doc["counts_before"]["TERMS"]) + "):")
    for m, row in after.items():
        print(f"  {m}: {row}")
    print("check phrases, occurrences in each member's new texts:")
    for m in doc["members"]:
        mine = [x["new"] for x in doc["edits"] if x["member"] == m]
        print(f"  {m}: " + "; ".join(f"{p} {sum(n.count(p) for n in mine)}" for p in CHECK_PHRASES
                                     if sum(n.count(p) for n in mine)))
    for f in fails:
        print("FAIL  " + f)
    print("PASS: every check" if not fails else f"{len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
