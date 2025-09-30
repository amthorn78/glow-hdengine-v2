#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, subprocess, sys, tempfile

def main() -> int:
    os.environ["SAFE_MODE"] = "1"
    # deterministic env for provenance
    env = os.environ.copy()
    env.setdefault("ENGINE_TAG", "ENG-DEMO")
    env.setdefault("INVOCATION_TAG", "INV-0123456789abcdef")  # 16 hex
    env.setdefault("RELEASE_ID", "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef")  # 64 hex
    env.setdefault("CORRELATION_ID", "CID-fedcba9876543210")  # CID + 16 hex

    with tempfile.TemporaryDirectory() as td:
        side = os.path.join(td, "sc.json")
        # positive gate (uses --admin)
        cmd = [
            sys.executable, "scripts/hdctl.py", "showcompat",
            "--birthdate","2000-01-01","--birthtime","12:00","--place","Tallinn, EE","--tz","Europe/Tallinn",
            "--birthdate2","2001-02-03","--birthtime2","13:30","--place2","Paris, FR","--tz2","Europe/Paris",
            "--showmath","--admin-out", side, "--admin",
        ]
        r = subprocess.run(cmd, env=env, capture_output=True)
        if r.returncode != 0:
            sys.stderr.write(r.stderr.decode("utf-8", "ignore"))
            print("SIDE_ERR")
            return 2
        if not os.path.exists(side):
            print("SIDE_MISSING")
            return 2

        d = json.loads(open(side, "r", encoding="utf-8").read())
        need = {"rule_version","engine_tag","invocation_tag","release_id","correlation_id","pair_order","a","b","features","decision","band"}
        if not need.issubset(d.keys()):
            print("SIDE_FIELDS_MISSING", sorted(need - set(d.keys())))
            return 2

        if not re.fullmatch(r"INV-[0-9a-f]{16}", d["invocation_tag"]):
            print("INV_BAD", d["invocation_tag"]); return 2
        if not re.fullmatch(r"[0-9a-f]{64}", d["release_id"]):
            print("REL_BAD", d["release_id"]); return 2
        if not re.fullmatch(r"CID-[0-9a-f]{16}", d["correlation_id"]):
            print("CID_BAD", d["correlation_id"]); return 2

        parts = d["pair_order"].split(",")
        if not (len(parts) == 2 and all(re.fullmatch(r"[0-9a-f]{64}", p) for p in parts)):
            print("PAIR_PARTS_BAD", d["pair_order"]); return 2
        if ",".join(sorted(parts)) != d["pair_order"]:
            print("PAIR_CANON_BAD", d["pair_order"]); return 2

        # negative gate: showmath present but admin off
        side2 = os.path.join(td, "neg.json")
        env2 = env.copy(); env2["HD_ADMIN"] = "0"
        cmd2 = [
            sys.executable, "scripts/hdctl.py", "showcompat",
            "--birthdate","2000-01-01","--birthtime","12:00","--place","Tallinn, EE","--tz","Europe/Tallinn",
            "--birthdate2","2001-02-03","--birthtime2","13:30","--place2","Paris, FR","--tz2","Europe/Paris",
            "--showmath","--admin-out", side2
        ]
        r2 = subprocess.run(cmd2, env=env2, capture_output=True)
        if r2.returncode != 0:
            sys.stderr.write(r2.stderr.decode("utf-8", "ignore"))
            print("NEG_ERR")
            return 2
        if os.path.exists(side2):
            print("NEG_LEAK")  # should NOT exist
            return 2

        print("SIDE_OK")
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
