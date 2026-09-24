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
        MIXED               anything else: stop.
      Every row carries old_count, the occurrences of the edit's old_str on the page (whitespace collapsed).
      Exits 0 when every edit is LANDED or NOT_LANDED (or TOKEN_NOT_RECORDED), 1 when any is MIXED.
  ctrl.py all --run EX/run.json [--expect unlanded|restored] [--edits E] [--harness-root H] [--session S]
      Every edit in EV/notion/edits.json on its page's newest fetch (the seven control pages, each fetched first), in
      one report with the LANDED and MIXED ids. With no --expect (the stop sweep, P-98) it exits 1 when any edit is
      MIXED. --expect unlanded (X4.6, before X5.0): exits 1 unless every edit's old_str occurs exactly once and no
      edit reads LANDED or MIXED. --expect restored (the restoration check, P-99): exits 1 unless the LANDED edits are
      exactly the freeze line and the four stop lines (STOP_KEPT) and none is MIXED, save the three close
      status lines the stop lines replaced (STOP_SUPERSEDED: old_str gone, new text absent).
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


def restored_bad(rows):
    landed = {r["id"] for r in rows if r["state"] == "LANDED"}
    bad = landed ^ set(STOP_KEPT)
    bad |= {r["id"] for r in rows if r["state"] == "MIXED"
            and not (r["id"] in STOP_SUPERSEDED and r["old_count"] == 0 and not r["new_present"])}
    return sorted(bad)
CHILD = re.compile(r'<page url="https://[^/"]+/p/([0-9a-f]{32})[^"]*"[^>]*>([^<]*)</page>')


def fill(text, run):
    missing = []
    for tok, key in TOKENS.items():
        if tok in text:
            if run.get(key):
                text = text.replace(tok, str(run[key]))
            else:
                missing.append(tok)
    return text, missing


def edit_state(page_text, e, run):
    old, _ = fill(e["old_str"], run)
    new, missing = fill(e["new_str"], run)
    stored = C.collapse(page_text)
    old_count = stored.count(C.collapse(old).strip())
    if missing:
        return {"id": e["id"], "state": "TOKEN_NOT_RECORDED", "missing": missing, "old_count": old_count}
    inserted = new.replace(old, "", 1) if old in new else new
    present = C.collapse(inserted).strip() in stored
    state = "LANDED" if present else "NOT_LANDED" if old_count == 1 else "MIXED"
    return {"id": e["id"], "state": state, "old_count": old_count, "new_present": present}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["edits", "children", "all"])
    ap.add_argument("page", nargs="?")
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--run")
    ap.add_argument("--expect", choices=["unlanded", "restored"])
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
            bad = restored_bad(rows)
        else:
            bad = mixed
        print(json.dumps({"expect": a.expect, "pages": out, "landed": landed, "mixed": mixed, "bad": bad,
                          "pass": not bad}, indent=1))
        raise SystemExit(1 if bad else 0)
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
