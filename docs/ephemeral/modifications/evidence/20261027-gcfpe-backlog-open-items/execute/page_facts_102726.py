#!/usr/bin/env python3
"""Page facts from this session's own notion-fetch records, for EXECUTE of
MODIFICATION-20261027-gcfpe-backlog-open-items (X2's duplicate check, X24's pre-move check).

For each page id it takes the newest fetch captured at or after --fetched-after (body_check.py's D22 reader: the
session's harness records, subagents included) and reports only header facts: the "as of" revision, the title from
the fetch's properties, the first parent in its ancestor path, whether the body's first line equals an expected head
line, and the number of child-page tags in the body. No body text is printed, hashed or written.

    page_facts_102726.py facts --fetched-after T [--since-minutes N] ID [ID ...]
    page_facts_102726.py x2 --fetched-after T --x2 <x2 results json> --x0-receipt <execute/x0-dry-run.json>
    page_facts_102726.py dupready --fetched-after T --source-after T0 DUPLICATE SOURCE

`dupready` is X2's wait for an asynchronous duplicate: on the newest fetch of DUPLICATE after T and of SOURCE after
T0 it reports the duplicate's parent and title, and `ready` when both bodies have the same character count and the
same first line (counts and booleans only).

`x2` reads the duplication results ({"rows": [{"prompt", "source", "duplicate", "parent", "title"}]}) and checks,
on the newest fetch of each duplicate and each source after T: the duplicate's parent is the planned parent, its
title is exact, its body's first line equals the source's first line, it has no child page, and the source's
revision equals its X0 read (from the X0 dry-run receipt's N2 rows, or edits.json's pin). Run with
PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
PLAN = Path(__file__).resolve().parents[1] / "plan"
sys.path.insert(0, str(PLAN))
import body_check as bc  # noqa: E402

HEAD = re.compile(r'Here is the result of "fetch" for the Page with URL https://[^/\s]+/p/([0-9a-f-]{32,36}) '
                  r'as of (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z):')
PARENT = re.compile(r'<parent-page url="https://[^/\s"]+/p/([0-9a-f]{32})[^"]*"')
PROPS = re.compile(r"<properties>\n?(.*?)\n?</properties>", re.S)
CONTENT = re.compile(r"<content>\n?(.*)</content>", re.S)
CHILD = re.compile(r'<page url="')


def newest(page_id: str, root: str, session: str, since: int, fetched_after: str):
    page = page_id.replace("-", "")
    cutoff = time.time() - since * 60
    if fetched_after:
        cutoff = max(cutoff, datetime.strptime(fetched_after, "%Y-%m-%dT%H:%M:%S.%fZ")
                     .replace(tzinfo=timezone.utc).timestamp())
    cutoff_iso = datetime.fromtimestamp(cutoff, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    import glob
    base = os.path.join(root, "*", session)
    files = glob.glob(base + ".jsonl") + glob.glob(base + "/tool-results/*") \
        + glob.glob(base + "/subagents/**/*.jsonl", recursive=True) \
        + glob.glob(base + "/subagents/**/tool-results/*", recursive=True)
    best = None
    for f in files:
        if os.path.getmtime(f) < cutoff:
            continue
        if f.endswith(".jsonl"):
            entries = bc._recent_lines(f, cutoff_iso)
        else:
            try:
                raw = open(f, encoding="utf-8").read()
                entries = [json.loads(raw)] if page in raw else []
            except (OSError, ValueError):
                continue
        for obj in entries:
            ts = obj.get("timestamp") if isinstance(obj, dict) else None
            for t in bc._texts(obj):
                inner = t
                if not inner.startswith("Here is the result of"):
                    try:
                        inner = json.loads(t)["text"]
                    except (ValueError, KeyError, TypeError):
                        continue
                h = HEAD.match(inner)
                if not h or h.group(1).replace("-", "") != page:
                    continue
                captured = ts if f.endswith(".jsonl") else datetime.fromtimestamp(
                    os.path.getmtime(f), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                if not captured or captured < cutoff_iso:
                    continue
                if best is None or captured > best[0]:
                    best = (captured, h.group(2), inner)
    return best


def facts(page_id: str, root: str, session: str, since: int, fetched_after: str) -> dict:
    got = newest(page_id, root, session, since, fetched_after)
    if not got:
        return {"page_id": page_id, "error": "NO_FETCH_FOUND"}
    captured, as_of, inner = got
    pm = PARENT.search(inner)
    title = None
    m = PROPS.search(inner)
    if m:
        try:
            title = json.loads(m.group(1)).get("title")
        except ValueError:
            title = None
    c = CONTENT.search(inner)
    body = c.group(1) if c else ""
    first = body.split("\n", 1)[0] if body else ""
    return {"page_id": page_id, "captured": captured, "as_of": as_of, "title": title,
            "parent": pm.group(1) if pm else None, "child_pages": len(CHILD.findall(body)),
            "body_chars": len(body), "_first": first}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["facts", "x2", "dupready"])
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--fetched-after", default="")
    ap.add_argument("--since-minutes", type=int, default=600)
    ap.add_argument("--x2")
    ap.add_argument("--source-after", default="")
    ap.add_argument("--x0-receipt")
    ap.add_argument("--harness-root", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    a = ap.parse_args()
    if not a.session:
        sys.exit("set CLAUDE_CODE_SESSION_ID")
    if a.mode == "dupready":
        d = facts(a.ids[0], a.harness_root, a.session, a.since_minutes, a.fetched_after)
        s = facts(a.ids[1], a.harness_root, a.session, a.since_minutes, a.source_after)
        ready = (not d.get("error") and not s.get("error") and d.get("body_chars") == s.get("body_chars")
                 and d.get("_first") == s.get("_first"))
        print(json.dumps({"mode": "dupready", "duplicate": a.ids[0], "source": a.ids[1], "duplicate_as_of": d.get("as_of"),
                          "parent": d.get("parent"), "title": d.get("title"), "child_pages": d.get("child_pages"),
                          "chars_equal": d.get("body_chars") == s.get("body_chars"),
                          "head_equal": d.get("_first") == s.get("_first"),
                          "errors": [x.get("error") for x in (d, s) if x.get("error")], "ready": ready},
                         ensure_ascii=False))
        return 0 if ready else 1
    if a.mode == "facts":
        rows = [facts(i, a.harness_root, a.session, a.since_minutes, a.fetched_after) for i in a.ids]
        for r in rows:
            r.pop("_first", None)
        print(json.dumps({"mode": "facts", "rows": rows}, indent=1, ensure_ascii=False))
        return 0
    x2 = json.loads(Path(a.x2).read_text(encoding="utf-8"))
    pins = {p: m["expected_last_edited"] for p, m in bc.EDITS["pages"].items()}
    if a.x0_receipt:
        rec = json.loads(Path(a.x0_receipt).read_text(encoding="utf-8"))
        for r in (rec.get("gates", {}).get("N2_body_rehearsal", {}).get("pages") or []):
            if r.get("prompt") and r.get("as_of"):
                pins[r["prompt"]] = r["as_of"]
    out, ok = [], True
    seen = set()
    for row in x2["rows"]:
        d = facts(row["duplicate"], a.harness_root, a.session, a.since_minutes, a.fetched_after)
        s = facts(row["source"], a.harness_root, a.session, a.since_minutes, a.fetched_after)
        r = {"prompt": row["prompt"], "duplicate": row["duplicate"], "source": row["source"],
             "duplicate_as_of": d.get("as_of"), "source_as_of": s.get("as_of"),
             "parent_ok": d.get("parent") == row["parent"],
             "title_ok": d.get("title") == row["title"],
             "head_ok": bool(d.get("_first")) and d.get("_first") == s.get("_first"),
             "no_child_page": d.get("child_pages") == 0,
             "source_revision_unchanged": s.get("as_of") is not None and s.get("as_of") == pins.get(row["prompt"]),
             "distinct": row["duplicate"] not in seen and row["duplicate"] != row["source"],
             "errors": [x.get("error") for x in (d, s) if x.get("error")]}
        seen.add(row["duplicate"])
        r["ok"] = all(r[k] for k in ("parent_ok", "title_ok", "head_ok", "no_child_page",
                                      "source_revision_unchanged", "distinct")) and not r["errors"]
        ok &= r["ok"]
        out.append(r)
    print(json.dumps({"mode": "x2", "rows": out, "rows_total": len(out), "rows_ok": sum(1 for r in out if r["ok"]),
                      "ok": ok, "d22": "header facts only; no body text"}, indent=1, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
