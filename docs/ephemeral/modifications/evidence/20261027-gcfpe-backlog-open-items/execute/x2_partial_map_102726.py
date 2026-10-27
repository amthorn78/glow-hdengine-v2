#!/usr/bin/env python3
"""Scratch successor map for an in-memory X4 check on some real duplicates, for EXECUTE of
MODIFICATION-20261027-gcfpe-backlog-open-items (Nathan's addition after the X2 stop: run X4's plan check on the
CF-C-10, PE and CL-05 duplicates before duplicating the rest).

    x2_partial_map_102726.py --x2 <x2 log json> --fetched-after T --out <scratch map>

It starts from binding_pass.probe() of the PLAN stand-in map (a distinct synthetic id for every successor), sets
each duplicated row of the X2 log to its real page id, parent and revision (the newest fetch after T, read with
page_facts_102726.py), gives every other row its W8 parent and its PLAN pin (edits.json) so that the map validates
(those pages are not under test: run body_check.py with --prompts naming only the real rows), and writes the map
with "stand_in": false and "scratch_partial": true. It is never the
successor map (X3 writes that once, at execute/successor-pages-102726.1.json): it refuses that path and any path
inside the repository. Run with PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
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
REPO = HERE.parents[5]
sys.path.insert(0, str(PLAN))
sys.path.insert(0, str(HERE))
import binding_pass as bp  # noqa: E402
import page_facts_102726 as pf  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--x2", required=True)
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--harness-root", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    a = ap.parse_args()
    out = Path(a.out).resolve()
    if out.is_relative_to(REPO.resolve()):
        sys.exit("refusing a scratch map inside the repository")
    base = json.loads((PLAN / "successor-map-standin.json").read_text(encoding="utf-8"))
    smap = bp.probe(base)
    smap["stand_in"], smap["scratch_partial"] = False, True
    smap["stand_in_rule"] = "scratch: real ids for the duplicated rows of the X2 log; probe ids for the rest"
    w8 = json.loads((PLAN / "work/W8.json").read_text(encoding="utf-8"))
    parents = {m["prompt"]: m.get("parent") for m in w8["transaction"]["candidate_publication"]["members"]}
    parents["GCFPE-MGMT-10"] = "3db4590a05eb81de9736ea69bac61016"
    pins = {k: v["expected_last_edited"] for k, v in
            json.loads((PLAN / "edits.json").read_text(encoding="utf-8"))["pages"].items()}
    for k, m in smap["members"].items():
        m["parent_id"] = parents.get(k)
        m["created_last_edited_at"] = pins.get(k)
    smap["pe"]["created_last_edited_at"] = pins.get("PE")
    rows = []
    for r in json.loads(Path(a.x2).read_text(encoding="utf-8"))["rows"]:
        f = pf.facts(r["duplicate"], a.harness_root, a.session, 600, a.fetched_after)
        target = smap["pe"] if r["prompt"] == "PE" else smap["members"][r["prompt"]]
        target["page_id"] = r["duplicate"]
        target["created_last_edited_at"] = f.get("as_of")
        if r["prompt"] != "PE":
            target["parent_id"] = f.get("parent")
        rows.append({"prompt": r["prompt"], "page_id": r["duplicate"], "as_of": f.get("as_of"),
                     "parent": f.get("parent"), "error": f.get("error")})
    out.write_text(json.dumps(smap, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "rows": rows, "ok": all(not r["error"] and r["as_of"] for r in rows)},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
