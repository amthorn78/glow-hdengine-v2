#!/usr/bin/env python3
"""X25, P6, the sweep by literal, for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN §5 X25; activation-ops.json
sweep.P6-SWEEP).

  x25_sweep_102726.py triage --fetched-after T --pages ID ... --out R
  x25_sweep_102726.py notes  --fetched-after T --notes N --out R

On this session's newest read after T of each page: control_check_102726.py's sweep test (this release's 57 archive
ids, 100926.1, GCFPE-(PCR-)20261009.1 and an unmarked v5.0.0 binding, outside historical sections and predecessor
markers, child-page blocks counted), plus the P6-SWEEP member-count statements ("55 members", "55-member",
"exactly 55", "all 55") outside historical sections. A selected member's page (the successor map's 56) is reported
by counts only and is a stop if it has a finding (P6-SWEEP: a selected member body is never edited here); every
other page is reported with each finding's section and an 80-character excerpt (control and record pages, not
prompt bodies, D22).

`notes` checks the dated notes P6 wrote on record pages (N: {"rows": [{"id", "command", "note", "anchor"}]}, the
notes as sent): on the newest read after T, each note occurs exactly once (as written or with Notion's underscore
escaping), an update_content note's anchor occurs exactly once and directly follows its note after one blank line,
and an insert_content note at the start is the body's first paragraph. Counts and booleans only. Read-only; writes
only R. Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID set.
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
import activation_render_102726 as R  # noqa: E402
import control_check_102726 as C  # noqa: E402
import page_facts_102726 as PF  # noqa: E402

MAP = HERE / "successor-pages-102726.1.json"
COUNT = re.compile(r"(?<![\d.])55 members|55-member|exactly 55\b|all 55\b")


def count(text: str, s: str) -> int:
    return R.occ(text, s) + (R.occ(text, R.esc(s)) if R.esc(s) != s else 0)


def notes(a, root: str, session: str) -> int:
    rows = []
    for n in json.loads(Path(a.notes).read_text(encoding="utf-8"))["rows"]:
        got = PF.newest(n["id"], root, session, 900, a.fetched_after)
        if not got:
            rows.append({"id": n["id"], "error": "NO_FETCH_FOUND", "ok": False})
            continue
        m = PF.CONTENT.search(got[2])
        text = m.group(1) if m else ""
        row = {"id": n["id"], "as_of": got[1], "command": n["command"], "note_count": count(text, n["note"])}
        if n["anchor"] is not None:
            row["anchor_count"] = count(text, n["anchor"])
            row["note_then_anchor"] = count(text, n["note"] + "\n\n" + n["anchor"])
            row["ok"] = row["note_count"] == 1 and row["anchor_count"] == 1 and row["note_then_anchor"] == 1
        else:
            body = text.lstrip("\n")
            row["first_paragraph"] = body.startswith(n["note"] + "\n") or body.startswith(R.esc(n["note"]) + "\n")
            row["ok"] = row["note_count"] == 1 and row["first_paragraph"]
        rows.append(row)
    rec = {"record_type": "GCFPE_102726_X25_NOTES_READBACK", "fetched_after": a.fetched_after, "notes": len(rows),
           "all_ok": len(rows) > 0 and all(r["ok"] for r in rows), "rows": rows}
    Path(a.out).write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(rec, indent=1, ensure_ascii=False))
    return 0 if rec["all_ok"] else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["triage", "notes"])
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--pages", nargs="+")
    ap.add_argument("--notes")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    if a.mode == "notes":
        return notes(a, root, session)
    ctx = C.context(str(MAP))
    members = ctx["all_members"]
    rows = []
    for pid in dict.fromkeys(p.replace("-", "") for p in a.pages):
        got = PF.newest(pid, root, session, 900, a.fetched_after)
        if not got:
            rows.append({"id": pid, "error": "NO_FETCH_FOUND"})
            continue
        f = PF.facts(pid, root, session, 900, a.fetched_after)
        m = PF.CONTENT.search(got[2])
        text = m.group(1) if m else ""
        found = C.findings(text, ctx, "sweep", sweep_page=True)
        counts = []
        for path, raw, _ in C.sections(C.fold(text)):
            line = C.unescape(raw)
            if C.historical(path) or not COUNT.search(line):
                continue
            counts.append({"section": path[-1] if path else "<top>", "excerpt": line.strip()[:80]})
        member = pid in members
        row = {"id": pid, "title": f.get("title"), "as_of": got[1], "parent": f.get("parent"), "selected_member": member,
               "findings": len(found), "count_statements": len(counts)}
        if not member:
            row["finding_rows"] = found
            row["count_rows"] = counts
        rows.append(row)
    rec = {"record_type": "GCFPE_102726_X25_SWEEP_TRIAGE", "fetched_after": a.fetched_after, "pages": len(rows),
           "member_pages_with_findings": [r["id"] for r in rows if r.get("selected_member") and (r["findings"] or r["count_statements"])],
           "pages_with_findings": [r["id"] for r in rows if not r.get("selected_member") and (r.get("findings") or r.get("count_statements"))],
           "missing": [r["id"] for r in rows if r.get("error")], "rows": rows}
    Path(a.out).write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in rec.items() if k != "rows"}, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
