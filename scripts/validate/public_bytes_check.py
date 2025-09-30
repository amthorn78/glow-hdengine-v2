#!/usr/bin/env python3
from __future__ import annotations
import binascii, os, subprocess, sys, tempfile

def run_bytes() -> bytes:
    cmd = [
        sys.executable, "scripts/hdctl.py", "showcompat",
        "--birthdate","2000-01-01","--birthtime","12:00","--place","Tallinn, EE","--tz","Europe/Tallinn",
        "--birthdate2","2001-02-03","--birthtime2","13:30","--place2","Paris, FR","--tz2","Europe/Paris",
    ]
    return subprocess.check_output(cmd)

def main() -> int:
    os.environ["SAFE_MODE"] = "1"
    b1 = run_bytes()
    b2 = run_bytes()
    if b1 != b2:
        print("BYTES_DIFFER")
        return 2
    if not (b1.endswith(b"\n") and b2.endswith(b"\n")):
        print("LF_MISSING")
        return 2
    # print last 4 hex just as a tiny trace
    print("BYTES_OK", "TAIL1", binascii.hexlify(b1[-4:]).decode(), "TAIL2", binascii.hexlify(b2[-4:]).decode())
    print("LF_OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
