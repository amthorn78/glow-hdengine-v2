#!/usr/bin/env python3
"""Consistency check of edits.json for MODIFICATION-20261006-gtwpe-tw-document-rules, §P.

    PYTHONDONTWRITEBYTECODE=1 python3 edits_check.py [edits.json] [--decision-record PATH] [--inject FAULT]

It reads edits.json and GTWPE's decision record only, and writes nothing. It never reads a prompt body:
whether each `old` occurs once in its member's page is checked by reading, in the dry run and at X1.0,
never by this script. Exit 0 when every check passes; 1 otherwise, naming each failure by its code.
--inject applies one named fault in memory, to show that its check fails (the dry run).

  SHAPE     every edit has its fields; IDs are unique and numbered in file order within each member
  ONELINE   no `old` holds a newline; a `new` holds one only when the edit is marked blocks
  DIFFER    every `new` differs from its `old`
  VALUES    «V» occurs only in the two identity edits of each member, once in each `new`
  SHARED    edits under one rule key carry the same `old` and `new` in every member
  OVERLAP   within a member, no `old` occurs in another edit's `old`, or in any edit's `new`, its own included,
            so each still matches once when sent and is absent after
  ABSENT    each absent_after phrase occurs in some `old` of its member and in no `new` of it
  PROOF     the record prompts' `new` texts hold GTWPE-D1's requirement and its eight minimum items, as the
            decision record words them, and edits.json's copy of the items equals the record's
  EXCLUDED  no `new` holds the PE Metaprompt's excluded vocabulary as a whole word (model, effort, reasoning,
            workload, strength, assess, Ultra, Astra, GPT, surface)
  GATE      every member whose edits set the Last Update Gate (APPLY-10 and the record prompts) holds Nathan's
            form of 2026-10-06 in its `new` texts: `BN` with the PF10 version, a non-PF10 source's filename
            alone, never another PF as a source, and not a citation; and no `new` anywhere holds the superseded
            form, `BN` and the source filename
  NODRAFT   every member's `new` texts hold the no-Draft rule, by its phrase "unresolved drafting note"
"""
import copy
import json
import re
import sys
from pathlib import Path

EXCLUDED = [r"\bmodels?\b", r"\beffort\b", r"\breasoning\b", r"\bworkload", r"\bstrength", r"\bassess",
            r"\bultra\b", r"\bastra\b", r"\bgpt\b", r"\bsurface\b"]
GATE_SETTERS = ["APPLY-10", "RECORD-10", "RECORD-20"]
GATE_PHRASES = ["`BN 13.5`", "the version number of the PF10 file used",
                "A PF document other than PF10 is never a source", "it is not a citation of HDE Build Notes"]
GATE_FILENAME = {"APPLY-10": "its filename alone, without `BN`", "RECORD-10": "the approved specification's filename",
                 "RECORD-20": "the approved specification's filename"}
SUPERSEDED = [r"`?BN`? and the source filename", r"BN \+ the source filename"]
NODRAFT = "unresolved drafting note"


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
        first("DC-AUTH", "DRAIN-10")["new"] += " Choose a stronger model."
    elif fault == "proof":
        x = first("REC-FIELDS-PF20")
        x["new"] = x["new"].replace("- Any validation or verification performed\n", "")
    elif fault == "overlap":
        first("REC-READ", "RECORD-10")["new"] += " section delivery is the normal endpoint."
    elif fault == "absent":
        doc["absent_after"]["APPLY-10"].append("Report old/new values")
    elif fault == "values":
        first("AP-DATE")["new"] += " «V»"
    elif fault == "oneline":
        first("REC-PATH", "RECORD-10")["new"] = "each output's repository path,\nwith the commit that holds it"
    elif fault == "shared":
        first("REC-CHECK", "RECORD-20")["new"] = "and absence of source-administration chatter; then check it."
    elif fault == "differ":
        x = first("DC-SUB", "DRAIN-20"); x["new"] = x["old"]
    elif fault == "shape":
        e[3]["id"] = e[2]["id"]
    elif fault == "gate":
        x = first("AP-GATE"); x["new"] = x["new"].replace("its filename alone, without `BN`", "`BN` and the source filename")
    elif fault == "nodraft":
        x = first("AP-VERIFY"); x["new"] = x["new"].replace("unresolved drafting note", "drafting remark")
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
            continue
        if x["member"] not in members:
            fails.append(f"SHAPE: {x['id']} names an unknown member")
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
        if sum(1 for x in edits if x.get("member") == m and x.get("item") == "identity") != 2:
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
                if a is not b and a["old"] in b["old"]:
                    fails.append(f"OVERLAP: {a['id']}'s old occurs in {b['id']}'s old")
                if a["old"] in b["new"]:
                    fails.append(f"OVERLAP: {a['id']}'s old occurs in {b['id']}'s new")
        olds = [x["old"] for x in mine]
        news = [x["new"] for x in mine]
        for p in doc["absent_after"][m]:
            if not any(p in o for o in olds):
                fails.append(f"ABSENT: {m}: {p!r} occurs in no old, so no edit removes it")
            if any(p in n for n in news):
                fails.append(f"ABSENT: {m}: {p!r} occurs in a new text")
    req = doc["gtwpe_d1"]["requirement"]
    if doc["gtwpe_d1"]["items"] != items_from_record:
        fails.append("PROOF: edits.json's eight items differ from the decision record's")
    for m in doc["gtwpe_d1"]["bound_new"]:
        text = "\n".join(x["new"] for x in edits if x["member"] == m)
        for p in [req] + items_from_record:
            if p not in text:
                fails.append(f"PROOF: {m}'s new texts lack {p!r}")
    for x in edits:
        for w in EXCLUDED:
            if re.search(w, x["new"], re.IGNORECASE):
                fails.append(f"EXCLUDED: {x['id']}'s new holds {w!r}")
        for s in SUPERSEDED:
            if re.search(s, x["new"]):
                fails.append(f"GATE: {x['id']}'s new holds the superseded gate form {s!r}")
    for m in GATE_SETTERS:
        text = "\n".join(x["new"] for x in edits if x["member"] == m)
        for p in GATE_PHRASES + [GATE_FILENAME[m]]:
            if p not in text:
                fails.append(f"GATE: {m}'s new texts lack {p!r}")
    for m in members:
        text = "\n".join(x["new"] for x in edits if x["member"] == m)
        if NODRAFT not in text:
            fails.append(f"NODRAFT: {m}'s new texts lack {NODRAFT!r}")
    return fails


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
    fails = check(doc, items)
    print(f"edits: {len(doc['edits'])}; GTWPE-D1 items read from the decision record: {len(items)}")
    print("per member: " + ", ".join(f"{m} {sum(1 for x in doc['edits'] if x['member'] == m)}" for m in doc["members"]))
    olds = sorted(doc["edits"], key=lambda x: len(x["old"]), reverse=True)
    print("longest old: " + "; ".join(f"{x['id']} ({x['rule_key']}) {len(x['old'])}" for x in olds[:3]) + " characters")
    for f in fails:
        print("FAIL  " + f)
    print("PASS: every check" if not fails else f"{len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
