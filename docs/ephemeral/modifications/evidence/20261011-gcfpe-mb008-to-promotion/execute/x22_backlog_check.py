#!/usr/bin/env python3
"""X22: the backlog writes (MB-003 and MB-008 closed, MB-011 added for P-L8), checked on a fresh read as Notion
stores them. Transient read of this session's harness records; prints counts and booleans only.
Usage: x22_backlog_check.py <fetched-after ISO>"""
import json, os, sys
from pathlib import Path
sys.dont_write_bytecode = True
E = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(E / "plan"))
import control_check as C
PAGE = "3e54590a05eb81eb818fd0f42045167a"
PRESENT = [
    "<td>CLOSED — ITEM-09 of `MODIFICATION-20261011-gcfpe-mb008-to-promotion`, installed 2026-10-12</td>",
    "<td>CLOSED — `MODIFICATION-20261011-gcfpe-mb008-to-promotion`, promoted 2026-10-12</td>",
    "<td>MB-011</td>\n<td>PE Metaprompt 100926.1 keeps three passages scoped to the 20260914 repair</td>\n<td>S3</td>\n<td>OPEN</td>",
    "## MB-003 — The governance audit's Epic re-engineering reference still describes an Analyzer and model advice — CLOSED",
    "**Closed, 2026-10-12.** Taken as ITEM-09 (PART-06) of `MODIFICATION-20261011-gcfpe-mb008-to-promotion`.",
    "## MB-008 — The candidate's package repairs (F02, F04, F05, F07) and F06 have no Modification yet — CLOSED",
    "**Closed, 2026-10-12.** `MODIFICATION-20261011-gcfpe-mb008-to-promotion` repaired the packages and promoted GCFPE-20261009.1 / 100926.1 / 55.",
    "## MB-011 — PE Metaprompt 100926.1 keeps three passages scoped to the 20260914 repair — OPEN",
    "<td>2026-10-12, PLAN of `MODIFICATION-20261011-gcfpe-mb008-to-promotion` (P-L8), recorded at its X22</td>",
    "**What closing it involves.** A Modification that edits PE: mark the three passages historical or restate them for the current release, then re-read PE and check its frontmatter with `control_check.py`.",
]
ABSENT = ["— IN ANALYZE", "OPEN — proposed as ITEM-09", "advice — OPEN"]
got = C.latest(PAGE, os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"], 120, sys.argv[1])
if got is None:
    print(json.dumps({"ok": False, "error": "NO_FETCH_FOUND"})); sys.exit(1)
text = got[3]
res = {"record_type": "MB008_X22_BACKLOG", "page": PAGE, "as_of": got[1], "present": sum(s in text for s in PRESENT), "expected": len(PRESENT),
       "missing": [s[:80] for s in PRESENT if s not in text], "absent_violations": [s for s in ABSENT if s in text],
       "headings_closed": [l for l in text.split("\n") if l.startswith("## MB-") and l.endswith("— CLOSED")]}
res["ok"] = not res["missing"] and not res["absent_violations"]
print(json.dumps(res, indent=1, ensure_ascii=False))
sys.exit(0 if res["ok"] else 1)
