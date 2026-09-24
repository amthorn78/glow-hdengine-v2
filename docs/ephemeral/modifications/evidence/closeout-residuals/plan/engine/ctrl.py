#!/usr/bin/env python3
"""Read-only control-page helper for MODIFICATION-20260923-closeout-residuals (P-96, P-98). Reads the newest fetch of a
control page from this session's harness files (dryrun.latest_body, the same rule land.py uses: the running session
only, P-101) and writes nothing.
Control pages are not prompt bodies (D22), and nothing here prints page text.

  ctrl.py edits <PAGE_ID> <EDIT_ID>... --run EX/run.json [--edits EV/notion/edits.json] [--harness-root H]
          [--session S]
      Each edit's state on the page, for the apply-once test (P-90) and the stop sweep (P-98). The edit's tokens are
      filled from EX/run.json (P-96), and its new text is its new_str less its old_str (the whole new_str for a
      replacement). Whitespace is collapsed before comparing. State:
        LANDED              the new text is on the page;
        NOT_LANDED          the new text is absent and the old_str occurs exactly once: apply the edit;
        TOKEN_NOT_RECORDED  a token the edit carries has no value in EX/run.json, so the edit was never written
                            (P-96 records each value before the write that carries it); its old_count is still
                            given, which is what the read-only anchor check before X5.0 reads (X4.6, P-102);
        DOUBLED             an insertion's text stands twice (the same call sent again on a stale read): `op`
                            gives the one operation that takes the second copy out (P-104);
        MIXED               anything else: stop.
      Every row carries old_count, the occurrences of the edit's old_str on the page (whitespace collapsed).
      Exits 0 when every edit is LANDED or NOT_LANDED (or TOKEN_NOT_RECORDED), 1 when any is MIXED.
  ctrl.py all --run EX/run.json [--expect unlanded|restored] [--edits E] [--harness-root H] [--session S]
      Every edit in EV/notion/edits.json on its page's newest fetch (the seven control pages, each fetched first), in
      one report with the LANDED and MIXED ids. With no --expect (the stop sweep, P-98) it exits 1 when any edit is
      MIXED. --expect unlanded (X4.6, before X5.0): exits 1 unless every edit's old_str occurs exactly once and no
      edit reads LANDED or MIXED. --expect restored --kept-from F (the restoration check, P-99, P-104, P-108): exits 1
      unless the LANDED edits are exactly those F (the stop's last `all` report, taken after the stop lines:
      attempt-<n>/execute/stop/control.kept.json) reads LANDED, and every MIXED edit either reads MIXED in F too (a
      page someone else changed, listed for Nathan; the stop wrote nothing there) or is one of the three close status
      lines the stop lines replaced (STOP_SUPERSEDED: old_str gone, new text absent). Without --kept-from the
      expected set is STOP_KEPT, the freeze line and the four stop lines, and no MIXED edit is allowed.
  {{EXECUTE_DATE}} is filled per step (P-104): an edit whose `step` is X5.0, X5.3 or X5.6 takes EX/run.json's
  execute_date_X5.0, execute_date_X5.3 or execute_date_X5.6, each recorded once when its step starts.
  ctrl.py op <PAGE_ID> <EDIT_ID> --run EX/run.json [--reverse] [--edits E] [--harness-root H] [--session S]
      The update_content operation to send for one edit on the page as just fetched (P-103), printed with the page
      text it quotes (a control page, not a prompt body). Forward: the edit must read NOT_LANDED. Its tokens are
      filled from EX/run.json, and an insertion's old_str is widened on the page to the line before the anchor
      (inserted before it) or the line after it (inserted after it), so that once the text has landed the
      operation's old_str no longer occurs and the same call, sent again on a stale read, matches nothing and Notion
      refuses it. --reverse: the edit must read LANDED; the operation puts back its old_str (the stop's reversal,
      P-98). On a DOUBLED edit it gives the operation that removes the second copy. Refuses (exit 1) when the edit is
      in another state, when its text is not on the page literally once, or when the operation would still match
      after it lands (reapply_refused false), except for an append at the very end of a page, where nothing follows
      to widen into: that is given with end_of_page true, and its readback's DOUBLED test is the guard.
  ctrl.py children <HUB_PAGE_ID>... [--harness-root H] [--session S]
      The child pages each hub fetch lists, as the childlist.json nam002_live.py reads (spec §4.4 step 2):
      {"captured_at", "hubs": [{"id", "title", "fetched", "children": [{"id", "title"}]}]}. IDs and titles only.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import canon as C  # noqa: E402
import dryrun as D  # noqa: E402

# token -> EX/run.json key (P-96)
TOKENS = {"{{CANDIDATE_CRD_LIST_URL}}": "url", "{{MIGRATION_DATE}}": "migration_date",
          "{{EXECUTE_DATE}}": "execute_date", "{{STOP_DATE}}": "stop_date", "{{LIFT_DATE}}": "lift_date",
          "{{INSTALL_DATE}}": "install_date", "{{CLOSE_DATE}}": "close_date"}
# the control-page edits that stay after a stop past X5.0 once the restoration is done (P-99): the freeze line and the
# stop lines; every other edit reads NOT_LANDED, or TOKEN_NOT_RECORDED when it was never written
STOP_KEPT = ["TRACK-FREEZE-START", "TRACK-STATUS-STOP-01", "TRACK-STATUS-STOP-02", "TRACK-STATUS-STOP-03",
             "TRACK-UNIT-STOPPED"]
# the close lines whose old_str the stop lines replace: after a stop their old_str is gone and they were never written,
# so they read TOKEN_NOT_RECORDED ({{CLOSE_DATE}} is recorded only at X7.6) or, with a close date recorded, MIXED with
# their new text absent; either is expected
STOP_SUPERSEDED = ["TRACK-STATUS-01", "TRACK-STATUS-02", "TRACK-STATUS-03"]


def restored_bad(rows, kept=None, mixed_kept=()):
    """The edits that make the restoration check fail (P-99, P-108): the LANDED set must equal what the stop left
    LANDED, and an edit may read MIXED only if the stop's own report read it MIXED (a page changed by someone else,
    listed for Nathan, which the stop never wrote to) or it is a close line the stop lines replaced."""
    landed = {r["id"] for r in rows if r["state"] == "LANDED"}
    bad = landed ^ set(STOP_KEPT if kept is None else kept)
    bad |= {r["id"] for r in rows if r["state"] == "MIXED" and r["id"] not in set(mixed_kept)
            and not (r["id"] in STOP_SUPERSEDED and r["old_count"] == 0 and not r["new_present"])}
    return sorted(bad)
CHILD = re.compile(r'<page url="https://[^/"]+/p/([0-9a-f]{32})[^"]*"[^>]*>([^<]*)</page>')


def fill(text, run, step=None):
    missing = []
    for tok, key in TOKENS.items():
        if tok == "{{EXECUTE_DATE}}" and step:
            key = "execute_date_" + step  # P-104: the date its step started
        if tok in text:
            if run.get(key):
                text = text.replace(tok, str(run[key]))
            else:
                missing.append(tok)
    return text, missing


def filled(e, run):
    old, _ = fill(e["old_str"], run, e.get("step"))
    new, missing = fill(e["new_str"], run, e.get("step"))
    return old, new, missing


def edit_state(page_text, e, run):
    old, new, missing = filled(e, run)
    stored = C.collapse(page_text)
    old_count = stored.count(C.collapse(old).strip())
    if missing:
        return {"id": e["id"], "state": "TOKEN_NOT_RECORDED", "missing": missing, "old_count": old_count}
    inserted = new.replace(old, "", 1) if old in new else new
    ins_count = D.occ(stored, C.collapse(inserted).strip())
    present = ins_count > 0
    state = ("DOUBLED" if ins_count > 1 and old in new else "LANDED" if present
             else "NOT_LANDED" if old_count == 1 else "MIXED")
    return {"id": e["id"], "state": state, "old_count": old_count, "new_present": present}


def make_op(page_text, e, run, reverse=False):
    """The operation for one edit on the page as fetched (P-103), and whether it is refused when sent again."""
    st = edit_state(page_text, e, run)
    old, new, _ = filled(e, run)
    if st["state"] == "DOUBLED" and not reverse:
        # an insertion that landed twice (a call sent again on a stale read): take the second copy out, once
        ins = new.replace(old, "", 1)
        twice = ins + ins
        if D.occ(page_text, twice) != 1:
            return {"id": e["id"], "refused": "DOUBLED_NOT_CONTIGUOUS"}
        op = {"old_str": twice, "new_str": ins}
        after = page_text.replace(twice, ins, 1)
        return {"id": e["id"], "reverse": False, "undouble": True, "op": op,
                "reapply_refused": D.occ(after, twice) == 0}
    want = "LANDED" if reverse else "NOT_LANDED"
    if st["state"] != want:
        return {"id": e["id"], "refused": f"STATE_{st['state']}", "want": want}
    if reverse:
        src, dst = new, old
    else:
        src, dst = old, new
    if D.occ(page_text, src) != 1:
        return {"id": e["id"], "refused": "NOT_LITERALLY_ONCE", "count": D.occ(page_text, src)}
    p = page_text.index(src)
    if not reverse and new.endswith(old) and new != old:      # inserted before the anchor: add the line before
        ls = page_text.rfind("\n", 0, p)
        start = page_text.rfind("\n", 0, ls) + 1 if ls > 0 else 0
        op = {"old_str": page_text[start:p] + src, "new_str": page_text[start:p] + dst}
    elif not reverse and new.startswith(old) and new != old:  # inserted after the anchor: add the line after
        end = p + len(src)
        q = page_text.find("\n", end + 1 if page_text[end:end + 1] == "\n" else end)
        q = len(page_text) if q < 0 else q
        op = {"old_str": src + page_text[end:q], "new_str": dst + page_text[end:q]}
    else:
        op = {"old_str": src, "new_str": dst}
    if D.occ(page_text, op["old_str"]) != 1:
        return {"id": e["id"], "refused": "OP_NOT_UNIQUE"}
    after = page_text.replace(op["old_str"], op["new_str"], 1)
    ok = D.occ(after, op["old_str"]) == 0
    at_end = not page_text[p + len(src):].strip()
    res = {"id": e["id"], "reverse": reverse, "op": op, "reapply_refused": ok}
    if not ok and at_end and not reverse and new.startswith(old):
        res["end_of_page"] = True      # an append at the page's end: nothing after it can change (P-104)
    elif not ok:
        res["refused"] = "REAPPLY_WOULD_MATCH"
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["edits", "children", "all", "op"])
    ap.add_argument("page", nargs="?")
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--run")
    ap.add_argument("--expect", choices=["unlanded", "restored"])
    ap.add_argument("--kept-from")
    ap.add_argument("--reverse", action="store_true")
    ap.add_argument("--edits", default=str(HERE.parent / "notion/edits.json"))
    ap.add_argument("--since-minutes", type=int, default=30)
    ap.add_argument("--harness-root", default=D.ROOT)
    ap.add_argument("--session", default=D.SESSION or "any",
                    help="the session whose harness files are read (default: the running session, P-101); any: all")
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    D.ROOT = a.harness_root
    D.SESSION = None if a.session == "any" else a.session
    if a.mode == "children":
        hubs = []
        for hub in [a.page] + a.ids:
            ts, content = D.latest_body(hub)
            hubs.append({"id": hub.replace("-", ""), "title": D.TITLE, "fetched": ts, "source_file": D.SOURCE,
                         "children": [{"id": i, "title": t.strip()} for i, t in CHILD.findall(content)]})
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        print(json.dumps({"captured_at": now, "hubs": hubs}, indent=1, ensure_ascii=False))
        return
    if a.mode == "all":
        if not a.run:
            raise SystemExit("all needs --run EX/run.json")
        run = json.loads(Path(a.run).read_text(encoding="utf-8"))
        order = json.loads(Path(a.edits).read_text(encoding="utf-8"))
        pages = {}
        for e in order:
            pages.setdefault(e["page_id"], []).append(e)
        out, rows = [], []
        for page, es in pages.items():
            ts, content = D.latest_body(page)
            prow = [edit_state(content, e, run) for e in es]
            rows += prow
            out.append({"page": page, "title": es[0]["page_title"], "fetched": ts, "source_file": D.SOURCE,
                        "edits": prow})
        landed = sorted(r["id"] for r in rows if r["state"] == "LANDED")
        mixed = sorted(r["id"] for r in rows if r["state"] == "MIXED")
        if a.expect == "unlanded":
            bad = sorted(r["id"] for r in rows
                         if r["old_count"] != 1 or r["state"] not in ("NOT_LANDED", "TOKEN_NOT_RECORDED"))
        elif a.expect == "restored":
            kept, mixed_kept = None, ()
            if a.kept_from:
                kf = json.loads(Path(a.kept_from).read_text(encoding="utf-8"))
                kept, mixed_kept = kf["landed"], kf.get("mixed", [])
            bad = restored_bad(rows, kept, mixed_kept)
        else:
            bad = mixed
        print(json.dumps({"expect": a.expect, "pages": out, "landed": landed, "mixed": mixed, "bad": bad,
                          "pass": not bad}, indent=1))
        raise SystemExit(1 if bad else 0)
    if a.mode == "op":
        if not a.run or len(a.ids) != 1 or not a.page:
            raise SystemExit("op needs a page, one edit id and --run EX/run.json")
        run = json.loads(Path(a.run).read_text(encoding="utf-8"))
        edits = {e["id"]: e for e in json.loads(Path(a.edits).read_text(encoding="utf-8"))}
        if a.ids[0] not in edits:
            raise SystemExit(json.dumps({"error": "UNKNOWN_EDIT", "ids": a.ids}))
        ts, content = D.latest_body(a.page)
        res = make_op(content, edits[a.ids[0]], run, a.reverse)
        print(json.dumps({"page": a.page, "fetched": ts, "source_file": D.SOURCE, **res}, indent=1, ensure_ascii=False))
        raise SystemExit(1 if res.get("refused") else 0)
    if not a.run or not a.ids or not a.page:
        raise SystemExit("edits needs a page, --run EX/run.json and at least one edit id")
    run = json.loads(Path(a.run).read_text(encoding="utf-8"))
    edits = {e["id"]: e for e in json.loads(Path(a.edits).read_text(encoding="utf-8"))}
    unknown = [i for i in a.ids if i not in edits]
    if unknown:
        raise SystemExit(json.dumps({"error": "UNKNOWN_EDIT", "ids": unknown}))
    ts, content = D.latest_body(a.page)
    rows = [edit_state(content, edits[i], run) for i in a.ids]
    print(json.dumps({"page": a.page, "fetched": ts, "source_file": D.SOURCE, "edits": rows}, indent=1))
    raise SystemExit(1 if any(r["state"] == "MIXED" for r in rows) else 0)


if __name__ == "__main__":
    main()
