#!/usr/bin/env python3
"""X24, P5, archival by move, for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN §5 X24, §7; adapted from
docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/x19_pages.py).

  x24_archive_102726.py inspect  --fetched-after T --out R
        before the move, on this session's reads after T of the 57 archive-set pages (control_check_102726.py's
        archive_102726, from the successor map): each page's title against its expected title (the predecessor
        titles of plan/members-100926.1.tsv, PE Metaprompt 100926.1, the 100926.1 catalog; the CL-05 candidate's
        title is recorded as read), its parent, its child pages (children checked first: a page with a child page
        stops the move), its revision and its body's line count; and none already under the archive
  x24_archive_102726.py archived --fetched-after T --premove R --out R2
        after the move, on reads after T: the archive page's child pages include all 57, and each of the 57,
        re-read, sits under the archive with the title, revision and body line count R recorded

Metadata only (page_facts_102726.py's reader): ids, titles, revisions, parents and counts; no body text is printed,
hashed or written (D22). Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
sys.path.insert(0, str(E / "plan"))
sys.path.insert(0, str(HERE))
import control_check_102726 as C  # noqa: E402
import page_facts_102726 as PF  # noqa: E402

ARCHIVE = "3c94590a05eb811cb145cd010e3b3fcf"
MAP = HERE / "successor-pages-102726.1.json"
CHILD_ID = re.compile(r'<page url="https://[^/\s"]+/p/([0-9a-f]{32})')


def expected_titles() -> dict:
    ctx = C.context(str(MAP))
    tsv = {page: title for _, page, title, _ in C.tsv_rows()}
    out = {}
    for pid in ctx["archive_102726"]:
        if pid in tsv:
            out[pid] = tsv[pid]
        elif pid == C.OLD_CATALOG:
            out[pid] = "Glow HDE Complete Prompt Set — GCFPE-20261009.1 — 100926.1"
        elif pid == C.CL05_CANDIDATE:
            out[pid] = None   # recorded as read
        else:
            out[pid] = "PE Metaprompt 100926.1"
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["inspect", "archived"])
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--premove")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    want = expected_titles()
    if a.mode == "inspect":
        rows, missing = [], []
        for pid, title in want.items():
            f = PF.facts(pid, root, session, 900, a.fetched_after)
            if f.get("error"):
                missing.append(pid)
                continue
            rows.append({"id": pid, "as_of": f["as_of"], "title": f["title"], "title_ok": title is None or f["title"] == title,
                         "parent": f["parent"], "child_pages": f["child_pages"], "body_lines": f["body_lines"]})
        parents = {}
        for r in rows:
            parents[r["parent"]] = parents.get(r["parent"], 0) + 1
        rec = {"record_type": "GCFPE_102726_X24_PREMOVE", "mode": "inspect", "fetched_after": a.fetched_after,
               "archive_set": len(want), "read": len(rows), "missing": missing,
               "titles_ok": sum(r["title_ok"] for r in rows), "pages_with_children": [r["id"] for r in rows if r["child_pages"]],
               "already_under_archive": [r["id"] for r in rows if r["parent"] == ARCHIVE], "parents": parents, "rows": rows}
        rec["ok"] = (len(want) == 57 and not missing and rec["titles_ok"] == 57 and not rec["pages_with_children"]
                     and not rec["already_under_archive"])
    else:
        pre = {r["id"]: r for r in json.loads(Path(a.premove).read_text(encoding="utf-8"))["rows"]}
        arch = PF.newest(ARCHIVE, root, session, 900, a.fetched_after)
        if not arch:
            raise SystemExit("x24: no read of the archive page after the cutoff")
        content = PF.CONTENT.search(arch[2])
        under = set(CHILD_ID.findall(content.group(1) if content else ""))
        rows = []
        for pid in want:
            f = PF.facts(pid, root, session, 900, a.fetched_after)
            p = pre.get(pid, {})
            rows.append({"id": pid, "read": not f.get("error"), "as_of_before": p.get("as_of"), "as_of_after": f.get("as_of"),
                         "under_archive": pid in under, "parent_after": f.get("parent"),
                         "title_unchanged": f.get("title") == p.get("title"),
                         "body_lines_unchanged": f.get("body_lines") == p.get("body_lines"),
                         "child_pages_after": f.get("child_pages")})
        rec = {"record_type": "GCFPE_102726_X24_ARCHIVED", "mode": "archived", "fetched_after": a.fetched_after,
               "archive": ARCHIVE, "archive_as_of": arch[1], "archive_children": len(under), "archive_set": len(want),
               "present_under_archive": sum(r["under_archive"] for r in rows),
               "reread": sum(r["read"] for r in rows),
               "parent_not_archive": [r["id"] for r in rows if r["read"] and r["parent_after"] != ARCHIVE],
               "title_changed": [r["id"] for r in rows if r["read"] and not r["title_unchanged"]],
               "body_lines_changed": [r["id"] for r in rows if r["read"] and not r["body_lines_unchanged"]],
               "revision_changed": [r["id"] for r in rows if r["read"] and r["as_of_after"] != r["as_of_before"]],
               "rows": rows}
        rec["ok"] = (rec["present_under_archive"] == 57 and rec["reread"] == 57 and not rec["parent_not_archive"]
                     and not rec["title_changed"] and not rec["body_lines_changed"])
    Path(a.out).write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in rec.items() if k != "rows"}, indent=1, ensure_ascii=False))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
