#!/usr/bin/env python3
"""X5 and X6: one page's update_content payload, from X4's plan, for EXECUTE of
MODIFICATION-20261027-gcfpe-backlog-open-items.

    payload_102726.py --prompt P --fetched-after T [--chunk K]

It runs plan/body_check.py plan --successor-map execute/successor-pages-102726.1.json --prompts P
--with-conditional R-P1 R-P2 --fetched-after T on the read in hand (the X4 read: the newest fetch after T) and prints,
to stdout only, {"prompt", "page_id", "ok", "ops", "chunks", "chunk", "content_updates": [{"old_str", "new_str"}]}
in the order body_check.py applied them. It refuses (exit 1, no payload) unless that page's plan row is `ok`.
The Notion tool takes at most 100 operations per call, so a page with more is split into chunks of 100 (--chunk 1,
2, ...), sent in order. The payload is never written to a file (D22: body fragments travel only on stdout). Run with
PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
MAP = HERE / "successor-pages-102726.1.json"
MAX_OPS = 100


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--chunk", type=int, default=1)
    ap.add_argument("--since-minutes", type=int, default=600)
    a = ap.parse_args()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, str(PLAN / "body_check.py"), "plan", "--successor-map", str(MAP),
                        "--prompts", a.prompt, "--with-conditional", "R-P1", "R-P2",
                        "--fetched-after", a.fetched_after, "--since-minutes", str(a.since_minutes)],
                       capture_output=True, text=True, env=env)
    try:
        res = json.loads(p.stdout)
    except ValueError:
        print(json.dumps({"prompt": a.prompt, "ok": False, "error": "BODY_CHECK_OUTPUT", "stderr": p.stderr[-400:]}))
        return 1
    rows = [r for r in res.get("pages", []) if r.get("prompt") == a.prompt]
    if len(rows) != 1 or not rows[0].get("ok"):
        print(json.dumps({"prompt": a.prompt, "ok": False, "error": res.get("error") or "PAGE_NOT_OK",
                          "row": {k: v for k, v in (rows[0] if rows else {}).items()
                                  if k in ("as_of", "revision_matches_plan", "ops_not_applied", "batch_safe",
                                           "guards_failing_after", "check_would_pass", "binding_current_after")}}))
        return 1
    ops = [o for o in res.get("ops_payload_for_execute", [])]
    chunks = max(1, -(-len(ops) // MAX_OPS))
    if not 1 <= a.chunk <= chunks:
        print(json.dumps({"prompt": a.prompt, "ok": False, "error": f"CHUNK_RANGE 1..{chunks}"}))
        return 1
    part = ops[(a.chunk - 1) * MAX_OPS:a.chunk * MAX_OPS]
    print(json.dumps({"prompt": a.prompt, "page_id": part[0]["page_id"] if part else None, "ok": True,
                      "ops": len(ops), "chunks": chunks, "chunk": a.chunk,
                      "content_updates": [{"old_str": o["old_str"], "new_str": o["new_str"]} for o in part]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
