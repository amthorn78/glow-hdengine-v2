#!/usr/bin/env python3
"""PLAN proof for the control-page edits (P-90, P-96, P-98, P-99, P-103, P-104, P-107, P-108; repair rounds 6 and 7). No Notion
write: the seven control pages are read from their newest fetches (engine/dryrun.latest_body), every edit is applied
in memory in spec §9 order through engine/ctrl.py's own `op` (make_op), with the token values fixed in a run.json
(P-96; {{EXECUTE_DATE}} per step, P-104), and ctrl.py's state test is run before and after each step. Prints ids,
states and counts only (no page text).

  ctrl_proof.py <run.json> [--since-minutes N]

Sequences:
  success  X5.0 TRACK-FREEZE-START; X5.3 the eleven PART-06 pointers; X5.6 PART-11-TRACK-01, PART-12-HUB-01,
           PART-18-AF009-01; X7.5 TRACK-FREEZE-LIFT; X7.7 TRACK-STATUS-01..03.
  stop     the success sequence to X5.6, then the stop (P-98): each applied edit reversed in reverse order except
           TRACK-FREEZE-START; TRACK-UNIT-STOPPED and TRACK-STATUS-STOP-01..03 (after the record PR is opened,
           P-107); then TRACK-FREEZE-LIFT-STOP (after the restoration check and Nathan's lift).
  X5.1     a stop at X5.1, after the freeze line landed and before anything else: nothing to reverse; the stop lines
           are applied (P-107). A stop at X5.0 itself writes nothing and is a stop before X5.0 (P-107).
  mixed    after X5.0, someone else duplicates the tracking page's shared anchor paragraph; the stop at X5.1 then finds
           TRACK-UNIT-STOPPED MIXED: it is listed for Nathan and not applied, the three status lines are (P-108);
           the restoration check passes with the stop's own MIXED set, and TRACK-FREEZE-LIFT-STOP, MIXED too, is
           listed rather than applied.
Each step passes when: before it, the edit reads NOT_LANDED (a reversal: LANDED); make_op returns an operation whose
old_str occurs once and which would match nothing if sent again (reapply_refused); after it, the edit reads LANDED (a
reversal: NOT_LANDED with its old_str once); every edit applied earlier and not reversed still reads LANDED; and
sending the same operation again to the page as it now stands matches nothing, or, for an append at the very end of
a page (end_of_page), sending it again lands a second copy, which reads DOUBLED, and `op` takes it out exactly
(P-104). The resume check re-reads every
landed edit with the same run.json, which is what a later session does (P-96), and with each execute date moved to
the next day, as round 5 would have filled it (the test then misses: the finding). The restoration check runs
ctrl.py's `all --expect restored` logic with the set the stop left LANDED (P-104's --kept-from), and the anchor check
`--expect unlanded` on the pages as fetched.
"""
import argparse
import json
import sys
from datetime import date, timedelta
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


ANCHOR = "**The three decisions below are recorded as"


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

    def rows_of(pages, r=run):
        return [st(pages, eid, r) for eid in E]

    def walk(name, steps, r=run, start=None, skip_mixed=False):
        pages = dict(start or pages0)
        rows, landed, ok = [], [], True
        for eid, rev in steps:
            before = st(pages, eid, r)["state"]
            if skip_mixed and before == "MIXED":
                # P-108: a stop line that reads MIXED is listed for Nathan and not applied
                rows.append({"edit": eid, "reverse": rev, "before": before, "listed_not_applied": True, "ok": True})
                continue
            res = K.make_op(pages[E[eid]["page_id"]], E[eid], r, rev)
            if res.get("refused"):
                rows.append({"edit": eid, "reverse": rev, "before": before, "refused": res["refused"], "ok": False})
                ok = False
                continue
            op = res["op"]
            t = pages[E[eid]["page_id"]]
            pages[E[eid]["page_id"]] = t.replace(op["old_str"], op["new_str"], 1)
            again = D.occ(pages[E[eid]["page_id"]], op["old_str"])
            after = st(pages, eid, r)
            if rev:
                landed.remove(eid)
            else:
                landed.append(eid)
            others = [x for x in landed if x != eid and st(pages, x, r)["state"] != "LANDED"]
            good = ((before, after["state"]) == ("LANDED", "NOT_LANDED") and after["old_count"] == 1) if rev else \
                   ((before, after["state"]) == ("NOT_LANDED", "LANDED"))
            good = good and not others and (again == 0 and res["reapply_refused"] or res.get("end_of_page", False))
            if res.get("end_of_page"):
                # sent again on a stale read, an end-of-page append lands twice: the state reads DOUBLED and `op`
                # takes the second copy out (P-104)
                t2 = pages[E[eid]["page_id"]].replace(op["old_str"], op["new_str"], 1)
                d = K.edit_state(t2, E[eid], r)["state"]
                fix = K.make_op(t2, E[eid], r, False)
                t3 = t2.replace(fix["op"]["old_str"], fix["op"]["new_str"], 1) if not fix.get("refused") else t2
                undoubled = (d == "DOUBLED" and not fix.get("refused") and t3 == pages[E[eid]["page_id"]]
                             and fix["reapply_refused"])
                good = good and undoubled
            ok &= good
            rows.append({"edit": eid, "reverse": rev, "before": before, "after": after["state"],
                         "old_count_after": after.get("old_count"), "op_matches_again": again,
                         "end_of_page": res.get("end_of_page", False),
                         "doubled_then_undoubled": undoubled if res.get("end_of_page") else None,
                         "others_not_landed": others, "ok": good})
        resume_same = [x for x in landed if st(pages, x, r)["state"] != "LANDED"]
        moved = dict(r)
        for k, v in r.items():
            if k.startswith("execute_date_"):
                moved[k] = (date.fromisoformat(v) + timedelta(days=1)).isoformat()
        moved_misses = sorted(x for x in landed if "{{EXECUTE_DATE}}" in E[x]["new_str"]
                              and st(pages, x, moved)["state"] != "LANDED")
        ok &= not resume_same
        return pages, {"sequence": name, "steps": len(rows), "ok": bool(ok), "resume_same_run_not_landed": resume_same,
                       "resume_next_day_misses": moved_misses, "rows": rows}

    def expect(pages, kind, r, kept=None, mixed_kept=()):
        rows = rows_of(pages, r)
        landed = sorted(x["id"] for x in rows if x["state"] == "LANDED")
        mixed = sorted(x["id"] for x in rows if x["state"] == "MIXED")
        if kind == "unlanded":
            bad = sorted(x["id"] for x in rows
                         if x["old_count"] != 1 or x["state"] not in ("NOT_LANDED", "TOKEN_NOT_RECORDED"))
        else:
            bad = K.restored_bad(rows, kept, mixed_kept)
        return {"expect": kind, "kept_from_stop": kept, "mixed_kept": list(mixed_kept), "landed": landed,
                "mixed": mixed, "bad": bad, "pass": not bad}

    _, success = walk("success", [(x, False) for x in SUCCESS + CLOSE])
    stop_steps = ([(x, False) for x in SUCCESS]
                  + [(x, True) for x in reversed(SUCCESS) if x != "TRACK-FREEZE-START"]
                  + [(x, False) for x in STOP])
    # on the stop path no close, lift or install date is recorded (P-96)
    stop_run = {k: v for k, v in run.items() if k not in ("close_date", "lift_date", "install_date")}
    after_stop, stop = walk("stop", stop_steps, stop_run)
    kept = expect(after_stop, "restored", stop_run, None)["landed"]      # what the stop left LANDED (control.after)
    restored = expect(after_stop, "restored", stop_run, kept)
    _, stop_lift = walk("stop then lift", stop_steps + [("TRACK-FREEZE-LIFT-STOP", False)], run)
    # a stop at X5.1, after the freeze line landed: nothing to reverse, the stop lines only (P-107)
    x51_run = {k: v for k, v in stop_run.items() if k in ("execute_date_X5.0", "stop_date")}
    x51_steps = [("TRACK-FREEZE-START", False)] + [(x, False) for x in STOP]
    after_x51, x51 = walk("stop at X5.1", x51_steps, x51_run)
    kept_x51 = expect(after_x51, "restored", x51_run, None)["landed"]
    restored_x51 = expect(after_x51, "restored", x51_run, kept_x51)
    # the same stop after someone else duplicated the tracking page's anchor paragraph once X5.0 had landed (P-108)
    after_freeze, _ = walk("freeze only", [("TRACK-FREEZE-START", False)], x51_run)
    trk = E["TRACK-FREEZE-START"]["page_id"]
    t0 = after_freeze[trk]
    i = t0.index(ANCHOR)
    j = t0.index("\n", i)
    doubled = dict(after_freeze)
    doubled[trk] = t0[:j + 1] + t0[i:j + 1] + t0[j + 1:]
    after_mixed, mixed = walk("stop at X5.1, anchor duplicated by someone else", [(x, False) for x in STOP], x51_run,
                              start=doubled, skip_mixed=True)
    report = expect(after_mixed, "restored", x51_run, None)
    restored_mixed = expect(after_mixed, "restored", x51_run, report["landed"], report["mixed"])
    lift_run = dict(x51_run, lift_date=run["lift_date"])
    lift_state = st(after_mixed, "TRACK-FREEZE-LIFT-STOP", lift_run)["state"]
    mixed["lift_stop_state"] = lift_state
    mixed["listed_for_nathan"] = sorted(x["edit"] for x in mixed["rows"] if x.get("listed_not_applied"))
    mixed["ok"] = bool(mixed["ok"] and lift_state == "MIXED" and "TRACK-UNIT-STOPPED" in mixed["listed_for_nathan"])
    before = expect(dict(pages0), "unlanded", {"base": run.get("base")})
    ok = all(x["ok"] for x in (success, stop, stop_lift, x51, mixed)) and restored["pass"] and restored_x51["pass"] \
        and restored_mixed["pass"] and before["pass"]
    print(json.dumps({"edits": len(E), "pages": len(pages0),
                      "fetched": {p: D.latest_body(p)[0] for p in pages0},
                      "all_ok": ok, "anchor_check_before_X5_0": before,
                      "restoration_check_after_stop": restored, "restoration_check_after_x51_stop": restored_x51,
                      "restoration_check_after_mixed_stop": restored_mixed,
                      "sequences": [success, stop, stop_lift, x51, mixed]}, indent=1))


if __name__ == "__main__":
    main()
