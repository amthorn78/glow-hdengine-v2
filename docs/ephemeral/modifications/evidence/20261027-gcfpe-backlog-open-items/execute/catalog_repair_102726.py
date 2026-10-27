#!/usr/bin/env python3
"""X9's catalog repair under AM-7, for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items.

    catalog_repair_102726.py plan --parts P --fetched-after T [--catalog ID]

On the newest fetch of the catalog after T it calls activation_render_102726.catalog_repair_payload, which refuses
unless the read is exactly the page C-CAT created, and prints the one replace_content payload on stdout only:
{"page_id", "command": "replace_content", "new_str"} (the catalog's AM-4 template, catalog_text). The write's
readback is checked by execute/x9_catalog_probe_102726.py (the read must equal as_fetched(catalog_text), and the
candidate and P1 catalog checks pass). Run with PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
sys.path.insert(0, str(PLAN))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("plan",))
    ap.add_argument("--parts", required=True)
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--catalog", default="4064590a05eb8113ae7de73041631c00")
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location("ar", PLAN / "activation_render_102726.py")
    ar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ar)
    ctx = ar.Ctx(str(HERE / "successor-pages-102726.1.json"), a.parts,
                 {"@CATALOG_PAGE_ID": a.catalog, "@CONTROLS_PR": "770", "@PUBLICATION_DATE": "2026-10-27"}, False)
    got = ar.C.latest(a.catalog, os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"],
                      600, a.fetched_after)
    if got is None:
        print(json.dumps({"ok": False, "error": "NO_FETCH_FOUND"}))
        return 1
    new_str = ar.catalog_repair_payload(got[3], ctx)
    print(json.dumps({"ok": True, "page_id": a.catalog, "as_of": got[1], "command": "replace_content",
                      "markers_left": len(ar.MARKER.findall(new_str)), "new_str": new_str}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
