#!/usr/bin/env python3
"""X22, P3, for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN §5 X22, §7).

  x22_install_102726.py <installed-skills-root> --out R

After Nathan's install report: docs/prompt_ecosystem_management/freeze.py on each of the nine installed trees (the
four packages and the five unchanged skills; freeze.py tests both D28 name-line forms and prints no digest if they
differ) against the digest execute/PROMOTION-PACKET.md's §2 states, read from its tables by x19_p0_102726.py's
reader. Read-only outside R; digests and counts only. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("p0", HERE / "x19_p0_102726.py")
P0 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P0)


def main() -> int:
    installed = Path(sys.argv[1])
    out = Path(sys.argv[sys.argv.index("--out") + 1])
    want = P0.packet_values()
    rows = []
    for s in P0.PACKAGES:
        d = P0.freeze(installed / s)
        rows.append({"skill": s, "kind": "package", "installed": d, "packet": want["packages"][s]["tree"],
                     "ok": d == want["packages"][s]["tree"]})
    for s in P0.UNCHANGED:
        d = P0.freeze(installed / s)
        rows.append({"skill": s, "kind": "unchanged", "installed": d, "packet": want["unchanged"][s], "ok": d == want["unchanged"][s]})
    rec = {"record_type": "GCFPE_102726_X22_INSTALL", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "step": "X22, P3", "installed_root": str(installed), "packet_sha256": hashlib.sha256(P0.PACKET.read_bytes()).hexdigest(),
           "skills": rows, "nine_equal": len(rows) == 9 and all(r["ok"] for r in rows)}
    rec["ok"] = rec["nine_equal"]
    out.write_text(json.dumps(rec, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": rec["ok"], "skills": [(r["skill"], r["ok"]) for r in rows]}))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
