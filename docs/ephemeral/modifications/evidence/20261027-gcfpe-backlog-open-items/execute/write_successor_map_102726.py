#!/usr/bin/env python3
"""X3 (C2): write the successor map of MODIFICATION-20261027-gcfpe-backlog-open-items once.

    write_successor_map_102726.py rows --logs <x2 log ...> --out <rows json>
        collect X2's duplication logs (the scratch JSON log of the first three rows and the JSONL lane logs) into one
        rows file {"rows": [{"prompt", "source", "duplicate", "parent", "title"}]} for page_facts_102726.py x2;
        refuses a prompt duplicated twice, a row never titled, a missing or extra prompt (56 rows: the 54 runtime
        successors, PE and CL-05).
    write_successor_map_102726.py write --rows <rows json> --fetched-after T
        write execute/successor-pages-102726.1.json from those rows, W8's candidate_publication.members (title,
        reason, planned parent) and the newest fresh read of each duplicate after T (its revision is the map's pin,
        its parent the map's parent_id). GCFPE-MGMT-10 is KEPT at its 100926.1 page with the revision and parent of
        its newest read after T. Refuses to write if the map already exists (values are recorded once, D26-C).

Ids are never typed: they come from the X2 logs, and every revision and parent from a fetch. Run with
PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
sys.path.insert(0, str(PLAN))
sys.path.insert(0, str(HERE))
import successor_map_102726 as sm  # noqa: E402
import page_facts_102726 as pf  # noqa: E402

MAP = HERE / "successor-pages-102726.1.json"
MGMT = "GCFPE-MGMT-10"
MGMT_PAGE = "3f74590a05eb81b69bd8c27106f7a59d"


def w8_members() -> dict:
    w8 = json.loads((PLAN / "work/W8.json").read_text(encoding="utf-8"))
    return {m["prompt"]: m for m in w8["transaction"]["candidate_publication"]["members"]}


def collect(logs: list) -> dict:
    w8 = w8_members()
    dup, titled, errs = {}, set(), []
    for path in logs:
        text = Path(path).read_text(encoding="utf-8")
        if path.endswith(".json"):
            for r in json.loads(text)["rows"]:
                if r.get("duplicated"):
                    dup.setdefault(r["prompt"], []).append((r["source"], r["duplicate"]))
                if r.get("titled"):
                    titled.add((r["prompt"], r["duplicate"]))
            continue
        for line in text.splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if r.get("step") == "duplicated":
                dup.setdefault(r["prompt"], []).append((r["source"], r["duplicate"]))
            elif r.get("step") == "titled":
                titled.add((r["prompt"], r["duplicate"]))
            else:
                errs.append(f"STEP:{r.get('prompt')}:{r.get('step')}")
    want = {p for p, m in w8.items() if m["disposition"] != "KEPT"}
    rows = []
    for p in sorted(set(dup) | want):
        got = dup.get(p, [])
        if len(got) != 1:
            errs.append(f"DUPLICATIONS:{p}:{len(got)}")
            continue
        src, d = got[0]
        if p not in w8 or w8[p]["duplicate_from"] != src:
            errs.append(f"SOURCE:{p}")
            continue
        if (p, d) not in titled:
            errs.append(f"NOT_TITLED:{p}")
        rows.append({"prompt": p, "source": src, "duplicate": d, "parent": w8[p]["parent"],
                     "title": w8[p]["successor_title"]})
    return {"rows": rows, "rows_total": len(rows), "errors": errs, "ok": not errs and len(rows) == 56}


def write(rows_path: str, fetched_after: str, root: str, session: str) -> dict:
    if MAP.exists():
        return {"ok": False, "error": "MAP_EXISTS: the successor map is written once (D26-C)"}
    rows = json.loads(Path(rows_path).read_text(encoding="utf-8"))["rows"]
    w8 = w8_members()
    doc = {"release": sm.RELEASE, "version_family": sm.VERSION, "baseline": sm.BASELINE, "stand_in": False,
           "written_by": "execute/write_successor_map_102726.py (X3, C2)", "fetched_after": fetched_after,
           "members": {}, "pe": None}
    errs = []
    for r in rows:
        f = pf.facts(r["duplicate"], root, session, 600, fetched_after)
        if f.get("error") or not f.get("as_of"):
            errs.append(f"NO_READ:{r['prompt']}")
            continue
        if r["prompt"] == "PE":
            doc["pe"] = {"page_id": r["duplicate"], "predecessor_page_id": r["source"], "title": sm.PE_TITLE,
                         "created_last_edited_at": f["as_of"]}
            continue
        added = r["prompt"] == sm.ADDED
        doc["members"][r["prompt"]] = {
            "disposition": "ADDED" if added else "SUCCESSOR",
            "reason": w8[r["prompt"]]["reason"],
            "page_id": r["duplicate"], "title": r["title"],
            "predecessor_page_id": None if added else r["source"],
            "duplicated_from": r["source"], "parent_id": f.get("parent"),
            "created_last_edited_at": f["as_of"]}
    k = facts_kept = pf.facts(MGMT_PAGE, root, session, 600, fetched_after)
    if k.get("error"):
        errs.append("NO_READ:GCFPE-MGMT-10")
    doc["members"][MGMT] = {"disposition": "KEPT", "reason": w8[MGMT]["reason"], "page_id": MGMT_PAGE,
                            "title": w8[MGMT]["successor_title"], "predecessor_page_id": None,
                            "duplicated_from": None, "parent_id": facts_kept.get("parent"),
                            "created_last_edited_at": facts_kept.get("as_of")}
    doc["members"] = dict(sorted(doc["members"].items()))
    check = sm.errors(doc, sm.members_tsv(str(PLAN / "members-100926.1.tsv")), False)
    if errs or check:
        return {"ok": False, "errors": errs, "map_check_errors": check}
    MAP.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"ok": True, "written": str(MAP.relative_to(HERE.parents[5])), "members": len(doc["members"]),
            "pe": doc["pe"]["page_id"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["rows", "write"])
    ap.add_argument("--logs", nargs="*", default=[])
    ap.add_argument("--out")
    ap.add_argument("--rows")
    ap.add_argument("--fetched-after", default="")
    ap.add_argument("--harness-root", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    a = ap.parse_args()
    if a.mode == "rows":
        res = collect(a.logs)
        if res["ok"] and a.out:
            Path(a.out).write_text(json.dumps({"rows": res["rows"]}, ensure_ascii=False, indent=1) + "\n",
                                   encoding="utf-8")
        print(json.dumps({k: v for k, v in res.items() if k != "rows"}, ensure_ascii=False, indent=1))
        return 0 if res["ok"] else 1
    res = write(a.rows, a.fetched_after, a.harness_root, a.session)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
