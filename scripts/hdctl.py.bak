#!/usr/bin/env python3
import sys, json, argparse, os, pathlib

def sercanon(obj) -> bytes:
    # UTF-8, sorted keys, compact separators, exactly one trailing LF
    b = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return b if b.endswith(b"\n") else b + b"\n"

def load_chart_or_stub(label, birthdate, birthtime, place, tz):
    # Minimal normalized stub for MVP; replace with real loader later
    return {"person": label, "birthdate": birthdate, "birthtime": birthtime, "place": place, "tz": tz, "gates": []}

def compat_public_stub(a, b):
    # Deterministic, numeric-free MVP surface
    return {"band": "Open", "categories": [{"id": "harmony", "band": "Open"}]}

def write_or_stdout(b: bytes, out: str|None):
    if out:
        p = pathlib.Path(out)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "wb") as f:
            f.write(b)
    else:
        sys.stdout.buffer.write(b)

def cmd_read_singlebg(ns):
    obj = load_chart_or_stub("A", ns.birthdate, ns.birthtime, ns.place, ns.tz)
    write_or_stdout(sercanon(obj), ns.out)

def cmd_showcompat(ns):
    a = {"birthdate": ns.birthdate1, "birthtime": ns.birthtime1, "place": ns.place1, "tz": ns.tz1}
    b = {"birthdate": ns.birthdate2, "birthtime": ns.birthtime2, "place": ns.place2, "tz": ns.tz2}
    write_or_stdout(sercanon(compat_public_stub(a, b)), ns.out)

def main(argv=None):
    argv = argv or sys.argv[1:]
    ap = argparse.ArgumentParser(prog="hdctl", add_help=True)
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_read = sub.add_parser("read", help="read operations")
    ap_read_sub = ap_read.add_subparsers(dest="what", required=True)
    ap_bg = ap_read_sub.add_parser("singlebg", help="print a normalized chart (MVP stub)")
    for a in ["--birthdate", "--birthtime", "--place", "--tz"]:
        ap_bg.add_argument(a, required=True)
    ap_bg.add_argument("--out", required=False)
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
    ap_comp.add_argument("--out", required=False)
    ap_comp.set_defaults(func=cmd_showcompat)

    try:
        # Keep CLI path offline for MVP
        if os.environ.get("SAFE_MODE", "1") != "1":
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
