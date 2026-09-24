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
  after X5.3 (P-112) five stops once X5.3's eleven pointers are sent, each ending in the restoration check with the
           sent list (the edits the unit listed before writing them, EX/ctrl/sent.txt; the stop lines are not in it)
           and the report the stop keeps: (a) a pointer DOUBLED is undoubled, then
           reversed, and the check passes; (b) a doubled pointer split by other text cannot be undoubled: it is
           listed for Nathan and the check fails until he restores the row; (c) a sent pointer stored differently
           (MIXED) is listed, and the check fails although the report read it MIXED, until he restores the page,
           or rules that it stays and waives it (--waived);
           (d) a reversal missed, so the report read the pointer LANDED: the check fails; (e) a stop line gone after
           the report: the check fails.
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

    def expect(pages, kind, r, kept=None, mixed_kept=(), sent=(), waived=()):
        rows = rows_of(pages, r)
        landed = sorted(x["id"] for x in rows if x["state"] == "LANDED")
        mixed = sorted(x["id"] for x in rows if x["state"] == "MIXED")
        if kind == "unlanded":
            bad = sorted(x["id"] for x in rows
                         if x["old_count"] != 1 or x["state"] not in ("NOT_LANDED", "TOKEN_NOT_RECORDED"))
        else:
            bad = K.restored_bad(rows, kept, mixed_kept, sent, waived)
        doubled = sorted(x["id"] for x in rows if x["state"] == "DOUBLED")
        return {"expect": kind, "kept_from_stop": kept, "mixed_kept": list(mixed_kept), "sent": len(sent),
                "waived": list(waived),
                "landed": landed, "mixed": mixed, "doubled": doubled, "bad": bad, "pass": not bad}

    _, success = walk("success", [(x, False) for x in SUCCESS + CLOSE])
    stop_steps = ([(x, False) for x in SUCCESS]
                  + [(x, True) for x in reversed(SUCCESS) if x != "TRACK-FREEZE-START"]
                  + [(x, False) for x in STOP])
    # on the stop path no close, lift or install date is recorded (P-96)
    stop_run = {k: v for k, v in run.items() if k not in ("close_date", "lift_date", "install_date")}
    after_stop, stop = walk("stop", stop_steps, stop_run)
    kept = expect(after_stop, "restored", stop_run, None)["landed"]      # what the stop left LANDED (control.after)
    restored = expect(after_stop, "restored", stop_run, kept, (), SUCCESS)
    _, stop_lift = walk("stop then lift", stop_steps + [("TRACK-FREEZE-LIFT-STOP", False)], run)
    # a stop at X5.1, after the freeze line landed: nothing to reverse, the stop lines only (P-107)
    x51_run = {k: v for k, v in stop_run.items() if k in ("execute_date_X5.0", "stop_date")}
    x51_steps = [("TRACK-FREEZE-START", False)] + [(x, False) for x in STOP]
    after_x51, x51 = walk("stop at X5.1", x51_steps, x51_run)
    kept_x51 = expect(after_x51, "restored", x51_run, None)["landed"]
    restored_x51 = expect(after_x51, "restored", x51_run, kept_x51, (), ["TRACK-FREEZE-START"])
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
    restored_mixed = expect(after_mixed, "restored", x51_run, report["landed"], report["mixed"],
                            ["TRACK-FREEZE-START"])
    lift_run = dict(x51_run, lift_date=run["lift_date"])
    lift_state = st(after_mixed, "TRACK-FREEZE-LIFT-STOP", lift_run)["state"]
    mixed["lift_stop_state"] = lift_state
    mixed["listed_for_nathan"] = sorted(x["edit"] for x in mixed["rows"] if x.get("listed_not_applied"))
    mixed["ok"] = bool(mixed["ok"] and lift_state == "MIXED" and "TRACK-UNIT-STOPPED" in mixed["listed_for_nathan"])
    # P-112: three stops after X5.3, with one pointer in a state the unit's own writes can leave
    x53 = ["TRACK-FREEZE-START"] + [x for x in SUCCESS if E[x]["step"] == "X5.3"]
    x53_run = {k: v for k, v in stop_run.items() if k in ("execute_date_X5.0", "execute_date_X5.3", "url",
                                                            "migration_date", "page_id", "stop_date")}

    def send(pages, eid, r, rev=False):
        res = K.make_op(pages[E[eid]["page_id"]], E[eid], r, rev)
        if res.get("refused"):
            return pages, res
        pg = dict(pages)
        pg[E[eid]["page_id"]] = pg[E[eid]["page_id"]].replace(res["op"]["old_str"], res["op"]["new_str"], 1)
        return pg, res

    def unit_stop(name, pages, sent, r):
        """The sweep's list, then stop step 3 (reversals; DOUBLED undoubled first; refused ones listed), the stop
        lines, the report the restoration check keeps, and the check itself (P-98, P-107, P-108, P-112)."""
        swept = expect(pages, "sweep", r)
        listed = sorted(set(swept["landed"]) | set(swept["mixed"]) | set(swept["doubled"]))
        reversed_, for_nathan = [], []
        for x in reversed([s for s in SUCCESS if s in sent and s != "TRACK-FREEZE-START"]):
            state = st(pages, x, r)["state"]
            if state == "DOUBLED":
                pages2, res = send(pages, x, r, True)
                if res.get("refused"):
                    for_nathan.append(x)
                    continue
                pages = pages2
                state = st(pages, x, r)["state"]
            if state == "LANDED":
                pages, res = send(pages, x, r, True)
                reversed_.append(x) if not res.get("refused") and st(pages, x, r)["state"] == "NOT_LANDED" \
                    else for_nathan.append(x)
            elif state == "MIXED":
                for_nathan.append(x)
        for x in STOP:
            if st(pages, x, r)["state"] == "NOT_LANDED":
                pages, _ = send(pages, x, r)
        kept_rep = expect(pages, "sweep", r)
        check = expect(pages, "restored", r, kept_rep["landed"], kept_rep["mixed"], list(sent))
        return pages, {"sequence": name, "listed_by_sweep": listed, "reversed": sorted(reversed_),
                       "listed_for_nathan": sorted(for_nathan), "check_before_nathan": check}

    def through_x53():
        pages, sent = dict(pages0), []
        for x in x53:
            pages, res = send(pages, x, x53_run)
            assert not res.get("refused"), (x, res)
            sent.append(x)
        return pages, sent

    item = "PART-06-ITEM1-02"
    ipage = E[item]["page_id"]
    # (a) the end-of-page pointer sent twice (a lost response, a stale read): DOUBLED, undoubled, then reversed
    pa, sa = dict(pages0), []
    for x in x53:
        pa, res = send(pa, x, x53_run)
        sa.append(x)
        if x == item:                                         # the same call sent again after a lost response
            pa = dict(pa)
            pa[ipage] = pa[ipage].replace(res["op"]["old_str"], res["op"]["new_str"], 1)
    ca_doubled = st(pa, item, x53_run)["state"]
    ins = K.filled(E[item], x53_run)[1].replace(K.filled(E[item], x53_run)[0], "", 1)
    pa, ca = unit_stop("stop after X5.3, a pointer doubled", pa, sa + [item], x53_run)
    ca["state_before_stop"] = ca_doubled
    ca["ok"] = bool(ca_doubled == "DOUBLED" and item in ca["listed_by_sweep"] and item in ca["reversed"] and not ca["listed_for_nathan"]
                    and ca["check_before_nathan"]["pass"])
    # (b) the second copy split from the first by other text: the undouble is refused; listed for Nathan; the check
    # fails until he restores the row from page history
    pb, sb = through_x53()
    pb = dict(pb)
    pb[ipage] = pb[ipage] + "\nA note someone added.\n" + ins
    pb, cb = unit_stop("stop after X5.3, a pointer doubled with text between", pb, sb, x53_run)
    pb[ipage] = pages0[ipage]                                 # Nathan restores the row from page history
    kb = expect(pb, "sweep", x53_run)
    cb["check_after_nathan"] = expect(pb, "restored", x53_run, kb["landed"], kb["mixed"], sb)
    cb["ok"] = bool(item in cb["listed_by_sweep"] and item in cb["listed_for_nathan"]
                    and item in cb["check_before_nathan"]["bad"] and cb["check_after_nathan"]["pass"])
    # (c) a sent replacement that Notion stored differently (MIXED right after the unit's own write): listed, not
    # reversed; the check fails although the stop's report read it MIXED, until Nathan restores the page
    rep_id = "PART-06-HUB-02"
    hpage = E[rep_id]["page_id"]
    pc, sc = through_x53()
    new = K.filled(E[rep_id], x53_run)[1]
    pc = dict(pc)
    pc[hpage] = pc[hpage].replace(new, new[:-1] + " ", 1)
    pc, cc = unit_stop("stop after X5.3, a sent edit stored differently", pc, sc, x53_run)
    kw = expect(pc, "sweep", x53_run)
    cc["check_with_nathans_waiver"] = expect(pc, "restored", x53_run, kw["landed"], kw["mixed"], sc, [rep_id])
    pc[hpage] = pages0[hpage]
    kc = expect(pc, "sweep", x53_run)
    cc["check_after_nathan"] = expect(pc, "restored", x53_run, kc["landed"], kc["mixed"], sc)
    cc["ok"] = bool(rep_id in cc["listed_by_sweep"] and rep_id in cc["listed_for_nathan"]
                    and rep_id in cc["check_before_nathan"]["bad"] and cc["check_after_nathan"]["pass"]
                    and cc["check_with_nathans_waiver"]["pass"])
    # (d) must fail: a reversal the stop missed, so the stop's own report read the pointer LANDED; the report cannot
    # keep it, since only the freeze line and the stop lines are kept
    pd, sd = through_x53()
    pd, cd = unit_stop("stop after X5.3, one reversal missed", pd, sd, x53_run)
    pd, _ = send(pd, rep_id, x53_run)                        # the pointer back, as if its reversal was never sent
    kd = expect(pd, "sweep", x53_run)
    cd["check_with_the_pointer_left"] = expect(pd, "restored", x53_run, kd["landed"], kd["mixed"], sd)
    cd["ok"] = bool(cd["check_before_nathan"]["pass"] and rep_id in kd["landed"]
                    and rep_id in cd["check_with_the_pointer_left"]["bad"])
    # (e) must fail: a stop line gone after the report that kept it
    pe, se = through_x53()
    pe, ce = unit_stop("stop after X5.3, a stop line removed later", pe, se, x53_run)
    ke = expect(pe, "sweep", x53_run)
    pe, _ = send(pe, "TRACK-UNIT-STOPPED", x53_run, True)
    ce["check_with_the_stop_line_gone"] = expect(pe, "restored", x53_run, ke["landed"], ke["mixed"], se)
    ce["ok"] = bool(ce["check_before_nathan"]["pass"]
                    and "TRACK-UNIT-STOPPED" in ce["check_with_the_stop_line_gone"]["bad"])
    before = expect(dict(pages0), "unlanded", {"base": run.get("base")})
    ok = all(x["ok"] for x in (success, stop, stop_lift, x51, mixed, ca, cb, cc, cd, ce)) and restored["pass"] \
        and restored_x51["pass"] and restored_mixed["pass"] and before["pass"]
    print(json.dumps({"edits": len(E), "pages": len(pages0),
                      "fetched": {p: D.latest_body(p)[0] for p in pages0},
                      "all_ok": ok, "anchor_check_before_X5_0": before,
                      "restoration_check_after_stop": restored, "restoration_check_after_x51_stop": restored_x51,
                      "restoration_check_after_mixed_stop": restored_mixed,
                      "sequences": [success, stop, stop_lift, x51, mixed],
                      "stops_after_x53": [ca, cb, cc, cd, ce]}, indent=1))


if __name__ == "__main__":
    main()
