#!/usr/bin/env python3
from __future__ import annotations
import sys as _sys
from pathlib import Path as _P
_sys.path.insert(0, str(_P(__file__).resolve().parents[1]))
import sys, argparse, json, os
from pathlib import Path
from engine.emit_public import emit_public_envelope  # canonical source of truth

def _read_json_or_die(path: str) -> dict:
    p = Path(path)
    try:
        obj = json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"INVALID_PATH:{path}", file=sys.stderr); sys.exit(4)
    except Exception:
        print(f"INVALID_JSON:{path}", file=sys.stderr); sys.exit(3)
    if not isinstance(obj, dict):
        print(f"INVALID_JSON:{path}", file=sys.stderr); sys.exit(3)
    return obj

def _require_tz_or_die(chart: dict, label: str, tz_flag: str | None) -> None:
    tz = chart.get("tz")
    if isinstance(tz, str) and tz.strip():
        return
    if isinstance(tz_flag, str) and tz_flag.strip():
        chart["tz"] = tz_flag
        return
    print(f"MISSING_TZ_{label}", file=sys.stderr); sys.exit(3)

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="hdctl", allow_abbrev=False)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sc = sub.add_parser("showcompat", help="print public compat JSON (bands-only)")
    sc.add_argument("--a", required=True, help="path to normalized chart A (JSON)")
    sc.add_argument("--a-tz", required=False, help="IANA timezone for A if not in file")
    sc.add_argument("--b", required=True, help="path to normalized chart B (JSON)")
    sc.add_argument("--b-tz", required=False, help="IANA timezone for B if not in file")
    return ap

def run_showcompat(ns) -> int:
    a = _read_json_or_die(ns.a)
    b = _read_json_or_die(ns.b)
    _require_tz_or_die(a, "A", ns.a_tz)
    _require_tz_or_die(b, "B", ns.b_tz)

    engine_tag = os.environ.get("ENGINE_TAG", "hdengine-alpha")
    invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-UNKNOWN")
    release_id = os.environ.get("RELEASE_ID", "0"*64)

    out = emit_public_envelope(a, b, engine_tag, invocation_tag, release_id)
    sys.stdout.buffer.write(out)
    return 0

def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    ap = build_parser()
    ns = ap.parse_args(argv)
    if ns.cmd == "showcompat":
        return run_showcompat(ns)
    return 64

if __name__ == "__main__":
    sys.exit(main())