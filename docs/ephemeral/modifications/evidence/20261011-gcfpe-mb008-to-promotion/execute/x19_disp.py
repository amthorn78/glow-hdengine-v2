#!/usr/bin/env python3
"""X19's one Flow Index operation, FI-X19-DISP (plan/activation-ops.json, key "x19"; amendment PIN-1-A item 3).

  x19_disp.py plan  --fetched-after T --pin TS   on the newest fresh read of the Flow Index: its revision equals
                                                 the pin, the operation is UNTOUCHED and its anchor occurs once
  x19_disp.py check --fetched-after T            after the write: the operation LANDED (body_check.state), and
                                                 control_check.py's archived-phase check passes on the page as it is

Reads are transient reads of this session's harness records; prints counts, states and booleans only.
"""
import argparse, json, os, sys
from pathlib import Path
sys.dont_write_bytecode = True
E = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(E / "plan"))
import body_check as B
import control_check as C

OPS = json.loads((E / "plan/activation-ops.json").read_text(encoding="utf-8"))["x19"]
FI = C.FLOW_INDEX
OP = OPS["pages"][FI]["ops"][0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["plan", "check"])
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--pin", default="")
    ap.add_argument("--catalog", default="3f74590a05eb812db385c2544d7570f7")
    a = ap.parse_args()
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    got = C.latest(FI, root, session, 600, a.fetched_after)
    if got is None:
        print(json.dumps({"mode": a.mode, "ok": False, "error": "NO_FETCH_FOUND"}))
        return 1
    _, as_of, title, text = got
    state = B.state(text, OP)
    res = {"mode": a.mode, "op": OP["id"], "as_of": as_of, "state": state, "anchor_count": B.occ(text, OP["start"]),
           "new_count": B.occ(text, B.expand(OP["new"]))}
    if a.mode == "plan":
        res["pin"] = a.pin
        res["ok"] = as_of == a.pin and state == "UNTOUCHED" and res["anchor_count"] == 1
    else:
        archive, members = C.archive_set(str(E / "execute/candidate-graph-parts")), C.hub_members(str(E / "execute/candidate-graph-parts"))
        row = C.check_text(FI, title, text, archive, members, "archived", a.catalog)
        res["control_check_archived"] = {"ok": row["ok"], "findings": row["findings"], "title_ok": row.get("title_ok"),
                                         "successors_missing": row.get("successors_missing")}
        res["ok"] = state == "LANDED" and row["ok"]
    print(json.dumps(res, indent=1))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
