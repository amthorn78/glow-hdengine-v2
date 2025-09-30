#!/usr/bin/env python3
"""
Minimal CLI stub with explicit --admin gate.

Public stdout is unchanged (MVP bands-only). Sidecar writes ONLY when:
  --showmath --admin-out <path> AND ( --admin OR HD_ADMIN=1 ).
"""

from __future__ import annotations
import argparse, json, os, pathlib, sys
from typing import Any

# Ensure project root on sys.path
_this = pathlib.Path(__file__).resolve()
_root = _this.parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

def sercanon(obj: Any) -> bytes:
    b = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return b if b.endswith(b"\n") else b + b"\n"

def write_or_stdout(b: bytes, out: str | None) -> None:
    if out:
        p = pathlib.Path(out); p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "wb") as f: f.write(b)
    else:
        sys.stdout.buffer.write(b)

def write_sidecar(data: Any, out_path: str) -> None:
    p = pathlib.Path(out_path); tmp = p.with_name(p.name + ".tmp")
    p.parent.mkdir(parents=True, exist_ok=True)
    b = sercanon(data)
    with open(tmp, "wb") as f:
        f.write(b); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, p)
    os.chmod(p, 0o600)
    dfd = os.open(str(p.parent), os.O_DIRECTORY); os.fsync(dfd); os.close(dfd)

# ====== MVP stubs (same behavior as your current script) ======
def load_chart_or_stub(label: str, birthdate: str, birthtime: str, place: str, tz: str) -> dict:
    return {"person": label, "birthdate": birthdate, "birthtime": birthtime, "place": place, "tz": tz, "gates": []}

def compat_public_stub(a: dict, b: dict) -> dict:
    # Preserve MVP public shape (bands-only, "Open")
    band = "Open"
    return {"band": band, "categories": [{"id": "harmony", "band": band}]}

# ====== Commands ======
def cmd_read_singlebg(ns: argparse.Namespace) -> None:
    obj = load_chart_or_stub("A", ns.birthdate, ns.birthtime, ns.place, ns.tz)
    write_or_stdout(sercanon(obj), ns.out)

def cmd_showcompat(ns: argparse.Namespace) -> None:
    a = {"birthdate": ns.birthdate1, "birthtime": ns.birthtime1, "place": ns.place1, "tz": ns.tz1}
    b = {"birthdate": ns.birthdate2, "birthtime": ns.birthtime2, "place": ns.place2, "tz": ns.tz2}

    # Public output unchanged
    public = compat_public_stub(a, b)
    write_or_stdout(sercanon(public), ns.out)

    # Admin-gated sidecar (new)
    if ns.showmath and ns.admin_out:
        hd_admin = str(os.environ.get("HD_ADMIN", "")).strip().lower() in {"1", "true", "yes", "on"}
        admin_gate = bool(ns.admin) or hd_admin
        if admin_gate:
            from engine.compat.type_strategy_v0 import compute_fingerprint
            fp_a = compute_fingerprint([1, 2, 3])
            fp_b = compute_fingerprint([4, 5, 6])
            pair_order = ",".join(sorted([fp_a, fp_b]))
            sidecar = {
                "rule_version": "ts_v0",
                "engine_tag": os.environ.get("ENGINE_TAG", ""),
                "invocation_tag": os.environ.get("INVOCATION_TAG", "INV-TEST"),
                "release_id": os.environ.get("RELEASE_ID", "0"*64),
                "correlation_id": os.environ.get("CORRELATION_ID", "CID-TEST"),
                "pair_order": pair_order,  # harmless placeholder in MVP
                "a": {},
                "b": {},
                "features": {},
                "decision": [],
                "band": public.get("band", "Open"),
            }
            write_sidecar(sidecar, ns.admin_out)

def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    ap = argparse.ArgumentParser(prog="hdctl", add_help=True)
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_read = sub.add_parser("read", help="read operations")
    ap_read_sub = ap_read.add_subparsers(dest="what", required=True)
    ap_bg = ap_read_sub.add_parser("singlebg", help="print a normalized chart (MVP stub)")
    for a in ["--birthdate", "--birthtime", "--place", "--tz"]:
        ap_bg.add_argument(a, required=True)
    ap_bg.add_argument("--out")
    ap_bg.set_defaults(func=cmd_read_singlebg)

    ap_comp = sub.add_parser("showcompat", help="print public compat JSON (MVP stub)")
    ap_comp.add_argument("--birthdate",  dest="birthdate1",  required=True)
    ap_comp.add_argument("--birthtime",  dest="birthtime1",  required=True)
    ap_comp.add_argument("--place",      dest="place1",      required=True)
    ap_comp.add_argument("--tz",         dest="tz1",         required=True)
    ap_comp.add_argument("--birthdate2", dest="birthdate2",  required=True)
    ap_comp.add_argument("--birthtime2", dest="birthtime2",  required=True)
    ap_comp.add_argument("--place2",     dest="place2",      required=True)
    ap_comp.add_argument("--tz2",        dest="tz2",         required=True)
    ap_comp.add_argument("--out")
    ap_comp.add_argument("--showmath", action="store_true", help="include admin sidecar when permitted")
    ap_comp.add_argument("--admin", action="store_true", help="enable admin-gated outputs")
    ap_comp.add_argument("--admin-out", dest="admin_out", help="path to write admin sidecar")
    ap_comp.set_defaults(func=cmd_showcompat)

    try:
        if str(os.environ.get("SAFE_MODE", "1")).strip() != "1":
            print("SAFE_MODE must be 1 for this MVP card", file=sys.stderr)
            return 2
        ns = ap.parse_args(argv)
        ns.func(ns)
        return 0
    except SystemExit as e:
        return e.code
    except Exception as e:
        print(f"ERROR:{type(e).__name__}:{e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())