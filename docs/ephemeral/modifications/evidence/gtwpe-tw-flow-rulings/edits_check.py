#!/usr/bin/env python3
"""Consistency check of edits.json for MODIFICATION-20261007-gtwpe-tw-flow-rulings, §P.

    PYTHONDONTWRITEBYTECODE=1 python3 edits_check.py [edits.json] [--decision-record PATH] [--inject FAULT]

It reads edits.json and the GTWPE decision record only, and writes nothing. It never reads a prompt body:
whether each `old` occurs exactly once in its member's live page is checked by reading, in the dry run and at
X1.0, never by this script. Exit 0 when every check passes; 1 otherwise, naming each failure by its code.
--inject applies one named fault in memory, to show that its check fails (the dry run).

  SHAPE     every edit has its fields; IDs are unique and numbered in file order within each member
  ONELINE   no `old` holds a newline; a `new` holds one only when the edit is marked blocks
  DIFFER    every `new` differs from its `old`
  VALUES    «V» occurs only in each member's two identity edits, once in each `new`, and in no `old`
  SHARED    edits under one shared key carry the same `old` and `new` in every member
  OVERLAP   within a member, no `old` occurs in another edit's `old`, or in any edit's `new`, its own included,
            so each still matches once when sent and is absent after
  ABSENT    each absent_after phrase occurs in some `old` of its member and in no `new` of it (D26-E, by phrase)
  PROOF     every GTWPE-D1 phrase an `old` holds, its `new` holds too, so no edit drops or weakens the proof-log
            requirement: "separate proof log", "named after it", and the eight minimum items as the decision
            record words them
  EXCLUDED  no `new` introduces the PE Metaprompt's excluded vocabulary as a whole word, one its `old` lacks
            (model, effort, reasoning, workload, strength, assess, Ultra, Astra, GPT, surface)
  SELECT    no `new` introduces a form of "select" its `old` lacks: no edit adds a selected boundary
  BARE      no `new` introduces a file name outside inline code, such as RUN.md written bare, which Notion
            turns into a link (ledger E-042)
"""
import copy
import json
import re
import sys
from pathlib import Path

EXCLUDED = [r"\bmodels?\b", r"\beffort\b", r"\breasoning\b", r"\bworkload", r"\bstrength", r"\bassess",
            r"\bultra\b", r"\bastra\b", r"\bgpt\b", r"\bsurface\b"]
FIELDS = ["id", "item", "rule", "shared", "old", "new", "blocks"]


def bare_names(text):
    """File names written outside inline code spans."""
    outside = re.sub(r"`[^`]*`", " ", text)
    return set(re.findall(r"\b[\w.-]+\.(?:md|py|json|ya?ml|txt)\b", outside))


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


def check(data, proof_items):
    bad = []
    shared = {}
    for m, spec in data["members"].items():
        edits = spec["edits"]
        short = edits[0]["id"].rsplit("-E", 1)[0] if edits else m
        for n, e in enumerate(edits, 1):
            missing = [f for f in FIELDS if f not in e]
            if missing:
                bad.append(f"SHAPE {m}: edit {n} lacks {missing}")
                continue
            if e["id"] != f"{short}-E{n:02d}":
                bad.append(f"SHAPE {m}: edit {n} has id {e['id']}")
            if "\n" in e["old"]:
                bad.append(f"ONELINE {e['id']}: old holds a newline")
            if "\n" in e["new"] and not e["blocks"]:
                bad.append(f"ONELINE {e['id']}: new holds a newline but is not marked blocks")
            if e["old"] == e["new"]:
                bad.append(f"DIFFER {e['id']}")
            if "«V»" in e["old"]:
                bad.append(f"VALUES {e['id']}: «V» in old")
            if e["item"] == "ID":
                if e["new"].count("«V»") != 1:
                    bad.append(f"VALUES {e['id']}: an identity edit needs «V» once")
            elif "«V»" in e["new"]:
                bad.append(f"VALUES {e['id']}: «V» outside an identity edit")
            if e["shared"]:
                shared.setdefault(e["shared"], set()).add((e["old"], e["new"]))
            for phrase in ["separate proof log", "named after it"] + proof_items:
                if phrase in e["old"] and phrase not in e["new"]:
                    bad.append(f"PROOF {e['id']}: drops {phrase!r}")
            for pat in EXCLUDED:
                if re.search(pat, e["new"], re.I) and not re.search(pat, e["old"], re.I):
                    bad.append(f"EXCLUDED {e['id']}: introduces {pat}")
            if re.search(r"\bselect", e["new"], re.I) and not re.search(r"\bselect", e["old"], re.I):
                bad.append(f"SELECT {e['id']}: introduces a form of select")
            bare_new, bare_old = bare_names(e["new"]), bare_names(e["old"])
            for name in sorted(bare_new - bare_old):
                bad.append(f"BARE {e['id']}: {name} outside inline code")
        if sum(1 for e in edits if e["item"] == "ID") != 2:
            bad.append(f"VALUES {m}: needs exactly two identity edits")
        for e in edits:
            for f in edits:
                if f is not e and e["old"] in f["old"]:
                    bad.append(f"OVERLAP {e['id']}: its old occurs in {f['id']}'s old")
                if e["old"] in f["new"]:
                    bad.append(f"OVERLAP {e['id']}: its old occurs in {f['id']}'s new")
        for phrase in spec["absent_after"]:
            if not any(phrase in e["old"] for e in edits):
                bad.append(f"ABSENT {m}: {phrase!r} is in no old")
            for e in edits:
                if phrase in e["new"]:
                    bad.append(f"ABSENT {e['id']}: new holds {phrase!r}")
    for key, pairs in shared.items():
        if len(pairs) != 1:
            bad.append(f"SHARED {key}: {len(pairs)} different texts")
    return bad


INJECT = {
    "shape": lambda d: d["members"]["TW-DRAIN-10"]["edits"][3].__setitem__("id", "DRAIN-10-E99"),
    "oneline": lambda d: d["members"]["TW-APPLY-10"]["edits"][4].__setitem__("old", "a\nb"),
    "differ": lambda d: d["members"]["TW-APPLY-10"]["edits"][4].__setitem__("new", d["members"]["TW-APPLY-10"]["edits"][4]["old"]),
    "values": lambda d: d["members"]["TW-DRAIN-20"]["edits"][5].__setitem__("new", "«V» " + d["members"]["TW-DRAIN-20"]["edits"][5]["new"]),
    "shared": lambda d: d["members"]["TW-RECORD-20"]["edits"][2].__setitem__("new", d["members"]["TW-RECORD-20"]["edits"][2]["new"] + " x"),
    "overlap": lambda d: d["members"]["GTWPE-MGMT-10"]["edits"][5].__setitem__("new", d["members"]["GTWPE-MGMT-10"]["edits"][6]["old"]),
    "absent": lambda d: d["members"]["GTWPE-MGMT-10"]["edits"][4].__setitem__("new", "until G5"),
    "proof": lambda d: next(e for e in d["members"]["TW-RECORD-10"]["edits"] if "separate proof log" in e["old"]).__setitem__("new", "x"),
    "excluded": lambda d: d["members"]["GTWPE-MGMT-10"]["edits"][2].__setitem__("new", d["members"]["GTWPE-MGMT-10"]["edits"][2]["new"] + " Use a strong model."),
    "bare": lambda d: d["members"]["GTWPE-FLOW-10"]["edits"][3].__setitem__("new", d["members"]["GTWPE-FLOW-10"]["edits"][3]["new"] + " See RUN.md."),
    "select": lambda d: d["members"]["TW-APPLY-10"]["edits"][3].__setitem__("new", d["members"]["TW-APPLY-10"]["edits"][3]["new"] + " Nathan may select sections."),
}


def main(argv):
    args = [a for a in argv[1:]]
    path = Path(args[0]) if args and not args[0].startswith("--") else Path(__file__).with_name("edits.json")
    rel = Path("docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md")
    rec = next((b / rel for b in Path(__file__).resolve().parents if (b / rel).is_file()),
               Path("/home/user/glow-hdengine-v2") / rel)
    if "--decision-record" in args:
        rec = Path(args[args.index("--decision-record") + 1])
    data = json.loads(path.read_text(encoding="utf-8"))
    items = record_items(rec)
    if "--inject" in args:
        fault = args[args.index("--inject") + 1]
        data = copy.deepcopy(data)
        INJECT[fault](data)
    bad = check(data, items)
    total = sum(len(v["edits"]) for v in data["members"].values())
    for b in bad:
        print("FAIL", b)
    print(f"{len(data['members'])} members, {total} edits, {len(items)} proof-log items from the decision record: "
          f"{'PASS' if not bad else str(len(bad)) + ' failures'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
