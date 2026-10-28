#!/usr/bin/env python3
"""X19, P0, for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN §5 X19, §7).

  x19_p0_102726.py <fetched-after> <installed-skills-root> <package-dir> <work> --parts P --set @K=V ... --out R

Each value is compared with the one execute/PROMOTION-PACKET.md states (read from its tables, not retyped):
  register   on this session's reads after <fetched-after>: control_check_102726.py --phase candidate on the
             controls, the catalog and PE (x18_record_102726.py check), whose register row passes only while the
             register's Current selection names GCFPE-20261009.1 / 100926.1 / 55
  pins       every control page's revision as read equals its pin in the packet's §4
  map        execute/successor-pages-102726.1.json's sha256 equals §2's
  digests    the five unchanged skills' installed trees (docs/prompt_ecosystem_management/freeze.py) and the four
             packages (each `.skill` file's sha256 and bytes, and the freeze digest of its tree extracted into an
             empty directory under <work>) equal §2's
  v5.1.0     the operating procedure's bytes on origin/main hash to §2's sha256
Read-only outside <work> and R; control pages only, counts, ids, digests and revisions (D22).
Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
REPO = E.parents[4]
PACKET = HERE / "PROMOTION-PACKET.md"
MAP = HERE / "successor-pages-102726.1.json"
FREEZE = REPO / "docs/prompt_ecosystem_management/freeze.py"
V510 = "docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.1.0-20261027.md"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
PACKAGES = ("change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract")
UNCHANGED = ("amthor-workspace-governance-audit", "session-relay-flowmaster", "glow-write-boundary",
             "typesafe-scoring", "glow-merged-change-attribution-lock")


def freeze(path: Path) -> str:
    r = subprocess.run([sys.executable, "-I", str(FREEZE), str(path)], capture_output=True, text=True, env=ENV)
    return r.stdout.strip().splitlines()[-1] if r.returncode == 0 and r.stdout.strip() else f"FREEZE_FAILED {r.returncode}"


def packet_values() -> dict:
    t = PACKET.read_text(encoding="utf-8")
    pk = {m[0]: {"sha256": m[1], "bytes": int(m[2].replace(",", "")), "tree": m[3]} for m in
          re.findall(r"^\| ([a-z-]+) \| `([0-9a-f]{64})` \| ([0-9,]+) \| `(\d+ [0-9a-f]{64})` \|$", t, re.M)}
    un = {m[0]: m[1] for m in re.findall(r"^\| ([a-z-]+) \| `(\d+ [0-9a-f]{64})` \|$", t, re.M)}
    pins = {m[1]: m[2] for m in re.findall(r"^\| ([^|]+?) \| `([0-9a-f]{32})` \| `(\d{4}-\d\d-\d\dT[0-9:.]+Z)` \|$",
                                           t.split("## 4.")[1].split("## 5.")[0], re.M)}
    mp = re.search(r"successor-pages-102726\.1\.json`: [0-9,]+ B, sha256 `([0-9a-f]{64})`", t).group(1)
    v5 = re.search(r"v5\.1\.0-20261027\.md` on `main` \([0-9,]+ B, sha256 `([0-9a-f]{64})`", t).group(1)
    return {"packages": pk, "unchanged": un, "pins": pins, "map_sha256": mp, "v510_sha256": v5}


def main() -> int:
    argv = sys.argv[1:]
    after, installed, pkgdir, work = argv[0], Path(argv[1]), Path(argv[2]), Path(argv[3])
    out = Path(argv[argv.index("--out") + 1])
    rest = argv[4:argv.index("--out")] + argv[argv.index("--out") + 2:]
    want = packet_values()
    rec = {"record_type": "GCFPE_102726_X19_P0", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "fetched_after": after, "packet_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest()}
    # register and pins
    work.mkdir(parents=True, exist_ok=True)
    chk = work / "x18-check.json"
    r = subprocess.run([sys.executable, str(HERE / "x18_record_102726.py"), "check", after, *rest, "--out", str(chk)],
                       capture_output=True, text=True, env=ENV, cwd=REPO)
    got = json.loads(chk.read_text(encoding="utf-8"))
    cc = got["control_check_candidate"]
    reg = next(p for p in cc["pages"] if p["page"] == "3d24590a05eb81ce942ad994cfca9fa1")
    rec["register"] = {"current_selection_ok": reg.get("current_selection_ok"), "control_check_ok": cc["ok"],
                       "findings_total": cc["findings_total"], "review_check_ok": got["review_check"]["ok"]}
    pins = {k: v["revision"] for k, v in got["pins"].items()}
    rec["pins"] = {"packet": len(want["pins"]), "read": len(pins),
                   "differing": sorted(k for k in want["pins"] if pins.get(k) != want["pins"][k])}
    # map
    rec["map"] = {"sha256": hashlib.sha256(MAP.read_bytes()).hexdigest(), "packet": want["map_sha256"]}
    # digests
    rows = []
    for s in UNCHANGED:
        d = freeze(installed / s)
        rows.append({"skill": s, "kind": "unchanged, installed", "digest": d, "ok": d == want["unchanged"].get(s)})
    for s in PACKAGES:
        arc = pkgdir / f"{s}.skill"
        b = arc.read_bytes()
        ext = work / s
        if ext.exists():
            raise SystemExit(f"P0: {ext} exists; give an empty work directory")
        ext.mkdir()
        with zipfile.ZipFile(arc) as z:
            z.extractall(ext)
        d = freeze(ext / s)
        w = want["packages"].get(s, {})
        rows.append({"skill": s, "kind": "package", "sha256": hashlib.sha256(b).hexdigest(), "bytes": len(b), "digest": d,
                     "ok": hashlib.sha256(b).hexdigest() == w.get("sha256") and len(b) == w.get("bytes") and d == w.get("tree")})
    rec["digests"] = rows
    # v5.1.0 on main
    blob = subprocess.run(["git", "-C", str(REPO), "show", f"origin/main:{V510}"], capture_output=True).stdout
    rec["v510"] = {"sha256": hashlib.sha256(blob).hexdigest(), "bytes": len(blob), "packet": want["v510_sha256"]}
    rec["checks"] = {
        "register_selects_100926_1_55": rec["register"]["current_selection_ok"] is True and rec["register"]["control_check_ok"],
        "every_pin_equals_packet": len(want["pins"]) == 13 and not rec["pins"]["differing"],
        "map_equals_packet": rec["map"]["sha256"] == want["map_sha256"],
        "nine_digests_equal": len(rows) == 9 and all(x["ok"] for x in rows),
        "v510_on_main_equals_packet": rec["v510"]["sha256"] == want["v510_sha256"]}
    rec["ok"] = all(rec["checks"].values())
    out.write_text(json.dumps(rec, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": rec["ok"], **rec["checks"], "pins_differing": rec["pins"]["differing"]}, indent=1))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
