#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys, json, pathlib, hashlib, os, stat

def _canonical_bytes(obj) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"

def _latest_norm_path() -> pathlib.Path:
    ndir = pathlib.Path("fixtures/hdapi/normalized")
    candidates = sorted(ndir.glob("*_normalized.json"))
    if not candidates:
        print("No normalized fixtures found under fixtures/hdapi/normalized", file=sys.stderr)
        sys.exit(2)
    return candidates[-1]

def _cmd_fetch_chart(args) -> None:
    p = _latest_norm_path() if args.from_fixture == "latest" else pathlib.Path(args.from_fixture)
    if not p.exists():
        print(f"Fixture not found: {p}", file=sys.stderr); sys.exit(2)
    obj = json.loads(p.read_text(encoding="utf-8"))
    out = _canonical_bytes(obj)
    sys.stdout.buffer.write(out)
    if args.admin_out:
        meta = {
            "source": "fixture",
            "fixture_path": p.as_posix(),
            "sha256": hashlib.sha256(out).hexdigest()
        }
        ap = pathlib.Path(args.admin_out)
        ap.write_text(json.dumps(meta, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
        os.chmod(ap, stat.S_IRUSR | stat.S_IWUSR)  # 0600

def main() -> None:
    parser = argparse.ArgumentParser(prog="hd_cli.py")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_fetch = sub.add_parser("fetch-chart", help="Emit normalized chart JSON (fixture-backed)")
    p_fetch.add_argument("--from-fixture", default="latest", help="'latest' or path to *_normalized.json")
    p_fetch.add_argument("--admin-out", default=None, help="Write admin-only sidecar (0600 perms)")
    p_fetch.set_defaults(func=_cmd_fetch_chart)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
