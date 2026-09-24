#!/usr/bin/env python3
"""PLAN proof for the control-page edits (P-90, P-96, P-98; repair round 6). No Notion write: the seven control pages
are read from their newest fetches (engine/dryrun.latest_body), every edit is applied in memory in spec §9 order with
the token values fixed in a run.json (P-96), and engine/ctrl.py's state test is run before and after each step.
Prints ids, states and counts only (no page text).

  ctrl_proof.py <run.json> [--since-minutes N]

Sequences:
  success  X5.0 TRACK-FREEZE-START; X5.3 the eleven PART-06 pointers; X5.6 PART-11-TRACK-01, PART-12-HUB-01,
           PART-18-AF009-01; X7.5 TRACK-FREEZE-LIFT; X7.7 TRACK-STATUS-01..03.
  stop     the success sequence to X5.6, then the stop (P-98): each applied edit reversed in reverse order except
           TRACK-FREEZE-START; TRACK-UNIT-STOPPED and TRACK-STATUS-STOP-01..03 (P-99, after the record PR is pushed);
           then TRACK-FREEZE-LIFT-STOP (P-99, after the restoration check and Nathan's lift).
Two checks of ctrl.py all --expect run on the same pages: `unlanded` on the pages as fetched (X4.6: every old_str once,
nothing landed), and `restored` after the stop sequence's reversals and stop lines (P-99: only the freeze line and the
four stop lines read LANDED). Each step passes when: before it, the edit reads NOT_LANDED (a reversal: LANDED); after it, LANDED (a reversal:
NOT_LANDED with its old_str once); and every edit applied earlier and not reversed still reads LANDED. The resume
check re-reads every landed edit with the same run.json, which is what a later session does (P-96), and with the
execute date moved one day, which is what the round-5 plan did (the test then misses: the finding).
"""
import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
EV = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EV / "engine"))
import ctrl as K  # noqa: E402
import dryrun as D  # noqa: E402

SUCCESS = (["TRACK-FREEZE-START"]
           + ["PART-06-HUB-01", "PART-06-HUB-02", "PART-06-HUB-03"]
           + [f"PART-06-ITEM{n}-0{k}" for n in (1, 2, 3, 4) for k in (1, 2)]
           + ["PART-11-TRACK-01", "PART-12-HUB-01", "PART-18-AF009-01"])
CLOSE = ["TRACK-FREEZE-LIFT", "TRACK-STATUS-01", "TRACK-STATUS-02", "TRACK-STATUS-03"]
STOP = ["TRACK-UNIT-STOPPED", "TRACK-STATUS-STOP-01", "TRACK-STATUS-STOP-02", "TRACK-STATUS-STOP-03"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--since-minutes", type=int, default=120)
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    run = json.loads(Path(a.run).read_text(encoding="utf-8"))
    E = {e["id"]: e for e in json.loads((EV / "notion/edits.json").read_text(encoding="utf-8"))}
    pages0 = {}
    for e in E.values():
        if e["page_id"] not in pages0:
            pages0[e["page_id"]] = D.latest_body(e["page_id"])[1]

    def st(pages, eid, r=run):
        return K.edit_state(pages[E[eid]["page_id"]], E[eid], r)

    def apply(pages, eid, reverse=False):
        e = E[eid]
        old, _ = K.fill(e["old_str"], run)
        new, _ = K.fill(e["new_str"], run)
        a_, b_ = (new, old) if reverse else (old, new)
        t = pages[e["page_id"]]
        assert t.count(a_) == 1, (eid, reverse, t.count(a_))
        pages[e["page_id"]] = t.replace(a_, b_, 1)

    def walk(name, steps):
        pages = dict(pages0)
        rows, landed, ok = [], [], True
        for eid, rev in steps:
            before = st(pages, eid)["state"]
            apply(pages, eid, rev)
            after = st(pages, eid)
            if rev:
                landed.remove(eid)
            else:
                landed.append(eid)
            others = [x for x in landed if x != eid and st(pages, x)["state"] != "LANDED"]
            good = ((before, after["state"]) == ("LANDED", "NOT_LANDED") and after["old_count"] == 1) if rev else \
                   ((before, after["state"]) == ("NOT_LANDED", "LANDED"))
            good = good and not others
            ok &= good
            rows.append({"edit": eid, "reverse": rev, "before": before, "after": after["state"],
                         "old_count_after": after.get("old_count"), "others_not_landed": others, "ok": good})
        resume_same = [x for x in landed if st(pages, x)["state"] != "LANDED"]
        moved = {**run, "execute_date": "2099-01-01"}
        resume_moved_misses = sorted(x for x in landed if "{{EXECUTE_DATE}}" in E[x]["new_str"]
                                     and st(pages, x, moved)["state"] != "LANDED")
        ok &= not resume_same
        return {"sequence": name, "steps": len(rows), "ok": bool(ok), "resume_same_run_not_landed": resume_same,
                "resume_moved_date_misses": resume_moved_misses, "rows": rows}

    def expect(pages, kind, r=run):
        """ctrl.py all --expect, on the in-memory pages: the X4.6 anchor check and the P-99 restoration check."""
        rows = [st(pages, eid, r) for eid in E]
        landed = sorted(r["id"] for r in rows if r["state"] == "LANDED")
        mixed = sorted(r["id"] for r in rows if r["state"] == "MIXED")
        if kind == "unlanded":
            bad = sorted(r["id"] for r in rows if r["old_count"] != 1 or r["state"] not in ("NOT_LANDED", "TOKEN_NOT_RECORDED"))
        else:
            bad = K.restored_bad(rows)
        return {"expect": kind, "landed": landed, "mixed": mixed, "bad": bad, "pass": not bad}

    success = walk("success", [(x, False) for x in SUCCESS + CLOSE])
    stop_steps = ([(x, False) for x in SUCCESS]
                  + [(x, True) for x in reversed(SUCCESS) if x != "TRACK-FREEZE-START"]
                  + [(x, False) for x in STOP])
    stop = walk("stop", stop_steps + [("TRACK-FREEZE-LIFT-STOP", False)])
    # the restoration check (P-99) runs after the reversals and the stop lines, before the lift line
    pages = dict(pages0)
    for eid, rev in stop_steps:
        apply(pages, eid, rev)
    # on the stop path no close, lift or install date is recorded (P-96); the check is also run with all of them
    stop_run = {k: v for k, v in run.items() if k not in ("close_date", "lift_date", "install_date")}
    restored = expect(pages, "restored", stop_run)
    restored_all_dates = expect(pages, "restored")
    before = expect(dict(pages0), "unlanded", {k: v for k, v in run.items() if k == "base"})
    before_all_dates = expect(dict(pages0), "unlanded")
    ok = (success["ok"] and stop["ok"] and restored["pass"] and restored_all_dates["pass"] and before["pass"]
          and before_all_dates["pass"])
    print(json.dumps({"edits": len(E), "pages": len(pages0),
                      "fetched": {p: D.latest_body(p)[0] for p in pages0},
                      "all_ok": ok, "anchor_check_before_X5_0": before, "anchor_check_all_dates": before_all_dates,
                      "restoration_check_after_stop": restored, "restoration_check_all_dates": restored_all_dates,
                      "sequences": [success, stop]}, indent=1))


if __name__ == "__main__":
    main()
