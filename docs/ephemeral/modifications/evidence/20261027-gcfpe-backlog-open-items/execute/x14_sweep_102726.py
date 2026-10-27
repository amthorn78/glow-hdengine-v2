#!/usr/bin/env python3
"""The read-only sweep after X14's stop (D26-B), for MODIFICATION-20261027-gcfpe-backlog-open-items.

  x14_sweep_102726.py <fetched-after> <out>

On this session's reads after <fetched-after> of the ten control pages and PE: plan/control_check_102726.py check
--phase candidate (the register, the Flow Index, the five hubs, the HDE Change Flow Overview, the catalog, PE), each
revision against X9's control check; and the Glow Operations Hub, whose newest read is compared with its read at X8's
revision (equal or not, and the revisions). D22: transient reads of this session's harness records; counts, ids,
headings and revisions only. Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
E = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(E / "plan"))
import body_check as B  # noqa: E402

MAP = E / "execute/successor-pages-102726.1.json"
CATALOG = "4064590a05eb8113ae7de73041631c00"
OPS_HUB, OPS_HUB_X8 = "3ce4590a05eb814f8892f88ff8539308", "2026-10-27T13:31:40.011Z"


def main(argv: list) -> int:
    fetched_after, out = argv[0], Path(argv[1])
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    r = subprocess.run([sys.executable, str(E / "plan/control_check_102726.py"), "check", "--successor-map", str(MAP),
                        "--phase", "candidate", "--catalog", CATALOG, "--with-pe", "--fetched-after", fetched_after],
                       capture_output=True, text=True, env=env)
    cc = json.loads(r.stdout)
    x9 = {p["page"]: p["as_of"] for p in json.load(open(E / "execute/x9-control-check-102726.1.json"))["pages"]}
    pages = [{"page": p["page"], "as_of": p.get("as_of"), "x9_as_of": x9.get(p["page"]),
              "unchanged_since_x9": x9.get(p["page"]) == p.get("as_of") if p["page"] in x9 else None,
              "ok": p.get("ok"), "findings": p.get("findings"),
              **{k: v for k, v in p.items() if k.endswith("_ok")}} for p in cc["pages"]]
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    reads = B.all_fetches(OPS_HUB, root, session, 100000)
    by_rev = {rev: body for _cap, rev, body in reads}
    newest = [x for x in reads if x[0] >= fetched_after]
    hub = {"page": OPS_HUB, "x8_revision": OPS_HUB_X8, "revisions_read": [rev for _c, rev, _b in reads],
           "newest_revision": newest[-1][1] if newest else None,
           "newest_body_equals_x8_read": (newest[-1][2] == by_rev.get(OPS_HUB_X8)) if newest and OPS_HUB_X8 in by_rev
           else None}
    del reads, by_rev, newest
    rec = {"record_type": "GCFPE_102726_X14_SWEEP", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "step": "X14 stop (D26-B)", "fetched_after": fetched_after,
           "control_check": {"exit": r.returncode, "phase": cc["phase"], "ok": cc["ok"],
                             "findings_total": cc["findings_total"], "failed_checks_total": cc["failed_checks_total"],
                             "pages": pages},
           "glow_operations_hub": hub,
           "ok": cc["ok"] is True and all(p["unchanged_since_x9"] is not False for p in pages)
                 and hub["newest_body_equals_x8_read"] is True,
           "d22": "transient reads of this session's harness records; counts, ids, headings and revisions only"}
    out.write_text(json.dumps(rec, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": rec["ok"], "control_check_ok": cc["ok"], "hub": hub}))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
