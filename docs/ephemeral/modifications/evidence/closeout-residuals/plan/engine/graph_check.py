#!/usr/bin/env python3
"""PART-16 gate (P-64): QA-110's and QA-80's landed text states the graph's branches (D13).

  graph_check.py --qa110 <PAGE_ID> --qa80 <PAGE_ID> [--since-minutes 30] [--simulate]

--simulate (PLAN rehearsal): apply the engine's edits in memory to the unedited bodies before checking them.

The graph side is read from docs/graph/parts/prompts/QA-110.json and QA-80.json. The body side is the newest fetch of
each page in this session's harness files (dryrun.latest_body; D22), read in memory. Output: booleans, and the harness
file each body was read from (D22 condition 5).

QA-110: the graph's ACCEPT branch goes to QA-120 and names "a completed failing run"; ESCALATION_REQUIRED goes to ESC-10.
        The landed body carries R-ITEM34's sentence ("a completed failing run is `ACCEPT` and continues to QA-120").
QA-80:  the graph gives WRONG_ROUTE_APPROVED_BASE exactly two branches, a terminal one and one to QA-70. The landed body
        points to *Required result and routing* (R-ITEM35), and that section's WRONG_ROUTE_APPROVED_BASE paragraph names
        both QA-70 and a terminal return.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import canon as C  # noqa: E402
import closeout_rules as R  # noqa: E402
import dryrun as D  # noqa: E402

PARTS = C.REPO / "docs/graph/parts/prompts"


def branches(pid):
    d = json.loads((PARTS / f"{pid}.json").read_text(encoding="utf-8"))
    return [(b["branch_id"], tuple(b["applicable_states"]), e.get("to"), b["condition"])
            for e in d["edges"] for b in e["route_branches"]]


def section(text, heading_words):
    m = re.search(r"(?m)^#+[^\n]*" + heading_words + r"[^\n]*\n(.*?)(?=^#+ |\Z)", text, re.S)
    return m.group(1) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qa110", required=True)
    ap.add_argument("--qa80", required=True)
    ap.add_argument("--since-minutes", type=int, default=30)
    ap.add_argument("--simulate", action="store_true")
    ap.add_argument("--harness-root", default=D.ROOT)
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    D.ROOT = a.harness_root
    out, sources = {}, {}
    b110 = branches("QA-110")
    acc = [b for b in b110 if b[1] == ("ACCEPT",)]
    esc = [b for b in b110 if b[1] == ("ESCALATION_REQUIRED",)]
    out["graph_QA-110_accept_to_QA-120_with_completed_failing_run"] = (
        len(acc) == 1 and acc[0][2] == "QA-120" and "completed failing run" in acc[0][3])
    out["graph_QA-110_escalation_to_ESC-10"] = len(esc) == 1 and esc[0][2] == "ESC-10"
    _, body = D.latest_body(a.qa110)
    sources["QA-110"] = D.SOURCE
    if a.simulate:
        body, _ = R.apply("QA-110", body)
    out["body_QA-110_states_accept_route"] = C.collapse(R.ITEM34_NEW.strip()) in C.collapse(body)
    b80 = [b for b in branches("QA-80") if b[1] == ("WRONG_ROUTE_APPROVED_BASE",)]
    out["graph_QA-80_wrong_route_two_branches"] = (
        len(b80) == 2 and {b[2] for b in b80} == {"QA-70", "NATHAN_TERMINAL_RETURN"})
    _, body = D.latest_body(a.qa80)
    sources["QA-80"] = D.SOURCE
    if a.simulate:
        body, _ = R.apply("QA-80", body)
    out["body_QA-80_pointer"] = R.ITEM35_NEW in body
    sec = section(body, r"Required result and routing")
    paras = [p for p in re.split(r"\n\s*\n|\n(?=- )", sec) if "`WRONG_ROUTE_APPROVED_BASE`" in p]
    out["body_QA-80_section_states_both_branches"] = any("QA-70" in p and "terminal" in p for p in paras) or (
        any("QA-70" in p for p in paras) and any("terminal" in p for p in paras))
    out["pass"] = all(out.values())
    print(json.dumps({**out, "source_files": sources}, indent=1))
    raise SystemExit(0 if out["pass"] else 1)


if __name__ == "__main__":
    main()
