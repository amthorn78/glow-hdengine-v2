#!/usr/bin/env python3
from __future__ import annotations
import sys

USAGE_LINE = "usage: hdctl read singlebg | showcompat [flags]  (see --help)\n"

HELP_TEXT = (
    "hdctl — Human Design CLI (alpha)\n"
    "\n"
    "Commands:\n"
    "  read singlebg     # print normalized private chart JSON (one LF)\n"
    "  showcompat        # print public compat JSON (one LF)\n"
    "\n"
    "Flags (inputs):\n"
    "  --birthdate YYYY-MM-DD   --birthtime HH:MM   --place \"City, CC\"   --tz IANA\n"
    "\n"
    "Notes:\n"
    "  - TZ is required for CLI alpha everywhere.\n"
    "  - Use --help for usage. Errors print a single usage line to stderr (exit 64).\n"
)

def _exit_usage_64() -> None:
    # Pinned one-liner to stderr; stdout must remain empty
    sys.stderr.write(USAGE_LINE)
    raise SystemExit(64)

def _exit_help_0() -> None:
    # Help goes to stdout and exits 0
    sys.stdout.write(HELP_TEXT + "\n")
    raise SystemExit(0)

import argparse, json
import tempfile
import os
import hashlib
from engine.util.input_validators import (
    parse_date_yyyy_mm_dd, parse_time_hh_mm, parse_place_city_cc, parse_tz_iana, ensure_cid
)
from engine.charts.loader import load_chart
from engine.stable.sercanon import serialize

def _typed_err(code: str, msg: str, cid: str) -> None:
    import sys
    sys.stderr.write(json.dumps({"error":{"code":code,"message":msg,"correlation_id":cid}},
                                ensure_ascii=False, separators=(",",":"), sort_keys=True) + "\n")
    raise SystemExit(2)

def _parse_singlebg_args(rest: list[str]):
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--birthdate", required=True)
    ap.add_argument("--birthtime", required=True)
    ap.add_argument("--place", required=True)
    ap.add_argument("--tz", required=True)
    ap.add_argument("--correlation-id", dest="cid", default=None)
    # inert labels
    ap.add_argument("--session-label")
    args = ap.parse_args(rest)
    return args

def _cmd_read_singlebg(rest: list[str]) -> int:
    import sys
    args = _parse_singlebg_args(rest)
    cid = ensure_cid(args.cid)

    # Validate inputs (map messages to short actionable strings)
    try:
        parse_date_yyyy_mm_dd(args.birthdate)
    except Exception:
        _typed_err("READER_INVALID_INPUT", "birthdate must be YYYY-MM-DD (real date)", cid)
    try:
        parse_time_hh_mm(args.birthtime)
    except Exception:
        _typed_err("READER_INVALID_INPUT", "birthtime must be HH:MM (24h)", cid)
    try:
        parse_place_city_cc(args.place)
    except Exception:
        _typed_err("READER_INVALID_INPUT", "place must be 'City, CC' (ISO-2 country code)", cid)
    try:
        parse_tz_iana(args.tz)
    except Exception:
        _typed_err("READER_INVALID_INPUT", "timezone must be valid IANA (e.g., Europe/Amsterdam)", cid)

    out = load_chart(args.birthdate, args.birthtime, args.place, tz=args.tz, correlation_id=cid)
    sys.stdout.buffer.write(serialize(out))
    return 0

from engine.compat.compute import compat_public

def _uniq_sorted_int_gates(chart: dict) -> list[int]:
    ints = []
    for g in chart.get("gates", []):
        try:
            ints.append(int(g))
        except Exception:
            # ignore non-numeric
            pass
    return sorted(set(ints))

def _fingerprint_from_chart(chart: dict) -> str:
    gates = _uniq_sorted_int_gates(chart)
    pre = {"gates": gates}
    bs = serialize(pre)  # canonical bytes (trailing LF)
    return hashlib.sha256(bs).hexdigest()

def _parse_showcompat_args(rest: list[str]):
    ap = argparse.ArgumentParser(add_help=False)
    # A
    ap.add_argument("--a-birthdate", required=True)
    ap.add_argument("--a-birthtime", required=True)
    ap.add_argument("--a-place", required=True)
    ap.add_argument("--a-tz", required=True)
    # B
    ap.add_argument("--b-birthdate", required=True)
    ap.add_argument("--b-birthtime", required=True)
    ap.add_argument("--b-place", required=True)
    ap.add_argument("--b-tz", required=True)
    # inert labels
    ap.add_argument("--session-label")
    ap.add_argument("--a-label")
    ap.add_argument("--b-label")
    # admin display flags
    ap.add_argument("--showband", action="store_true")
    ap.add_argument("--showcat", action="store_true")
    ap.add_argument("--showbg", action="store_true")
    ap.add_argument("--showmath")
    ap.add_argument("--correlation-id", dest="cid", default=None)
    return ap.parse_args(rest)

def _validate_inputs_pair(a: argparse.Namespace, b: argparse.Namespace, cid: str) -> None:
    # A
    try: parse_date_yyyy_mm_dd(a.a_birthdate)
    except Exception: _typed_err("READER_INVALID_INPUT","birthdate must be YYYY-MM-DD (real date)", cid)
    try: parse_time_hh_mm(a.a_birthtime)
    except Exception: _typed_err("READER_INVALID_INPUT","birthtime must be HH:MM (24h)", cid)
    try: parse_place_city_cc(a.a_place)
    except Exception: _typed_err("READER_INVALID_INPUT","place must be 'City, CC' (ISO-2 country code)", cid)
    try: parse_tz_iana(a.a_tz)
    except Exception: _typed_err("READER_INVALID_INPUT","timezone must be valid IANA (e.g., Europe/Amsterdam)", cid)
    # B
    try: parse_date_yyyy_mm_dd(b.b_birthdate)
    except Exception: _typed_err("READER_INVALID_INPUT","birthdate must be YYYY-MM-DD (real date)", cid)
    try: parse_time_hh_mm(b.b_birthtime)
    except Exception: _typed_err("READER_INVALID_INPUT","birthtime must be HH:MM (24h)", cid)
    try: parse_place_city_cc(b.b_place)
    except Exception: _typed_err("READER_INVALID_INPUT","place must be 'City, CC' (ISO-2 country code)", cid)
    try: parse_tz_iana(b.b_tz)
    except Exception: _typed_err("READER_INVALID_INPUT","timezone must be valid IANA (e.g., Europe/Amsterdam)", cid)

def _cmd_showcompat(rest: list[str]) -> int:
    import sys
    ns = _parse_showcompat_args(rest)
    cid = ensure_cid(ns.cid)
    _validate_inputs_pair(ns, ns, cid)

    # Load both charts (internal/fixtures path requires tz)
    ca = load_chart(ns.a_birthdate, ns.a_birthtime, ns.a_place, tz=ns.a_tz, correlation_id=cid)
    cb = load_chart(ns.b_birthdate, ns.b_birthtime, ns.b_place, tz=ns.b_tz, correlation_id=cid)

    # Fingerprints + ordering
    fpa = _fingerprint_from_chart(ca)
    fpb = _fingerprint_from_chart(cb)
    a_first = (fpa <= fpb)
    a_norm, b_norm = (ca, cb) if a_first else (cb, ca)

    # Public compat (numeric-free)
    pub = compat_public(a_norm, b_norm)
    out_bytes = serialize(pub)
    side = getattr(ns, 'showmath', None)
    if side:
        _write_atomic_0600(side, out_bytes)
    sys.stdout.buffer.write(out_bytes)
    return 0

def _write_atomic_0600(path: str, data: bytes) -> None:
    d = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=d)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
        dirfd = os.open(d, os.O_DIRECTORY)
        try: os.fsync(dirfd)
        finally: os.close(dirfd)
        os.chmod(path, 0o600)
    finally:
        try:
            if os.path.exists(tmp): os.unlink(tmp)
        except Exception:
            pass


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        _exit_usage_64()

    # Explicit help path
    if args == ["--help"] or args == ["-h"]:
        _exit_help_0()

    # Minimal routing only for S1 — we just validate command structure;
    # later steps will implement full behavior.
    if args[0] not in {"read", "showcompat"}:
        _exit_usage_64()

    if args[0] == "read":
        if len(args) >= 2 and args[1] == "singlebg":
            return _cmd_read_singlebg(args[2:])
        _exit_usage_64()

    if args[0] == "showcompat":
        return _cmd_showcompat(args[1:])

    _exit_usage_64()

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit as e:
        raise
