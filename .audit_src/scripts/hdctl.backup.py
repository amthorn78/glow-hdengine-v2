#!/usr/bin/env python3
import sys, argparse
import pathlib as _p
sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])), json, os, hashlib, pathlib
from engine.compat import ts_v0

# ---- serializer ----
def sercanon(obj) -> bytes:
    b = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return b if b.endswith(b"\n") else b + b"\n"

# ---- CLI surface ----
def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="hdctl", allow_abbrev=False)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sc = sub.add_parser("showcompat", help="print public compat JSON (bands-only)")
    sc.add_argument("--a", required=True, help="path to normalized chart A (JSON)")
    sc.add_argument("--a-tz", required=False, help="IANA timezone for A if not in file")
    sc.add_argument("--b", required=True, help="path to normalized chart B (JSON)")
    sc.add_argument("--b-tz", required=False, help="IANA timezone for B if not in file")
    sc.add_argument("--showmath", action="store_true", help="enable admin sidecar math (stdout invariant)")  # sidecar later
    sc.add_argument("--admin", action="store_true", help="admin gate switch")
    sc.add_argument("--admin-out", required=False, help="path to write admin sidecar (strict gate required)")
    return ap

# ---- helpers ----
def _read_json_or_die(path: str) -> dict:
    try:
        data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"INVALID_PATH:{path}", file=sys.stderr); sys.exit(4)
    except Exception:
        print(f"INVALID_INPUT:{path}", file=sys.stderr); sys.exit(3)
    if not isinstance(data, dict):
        print(f"INVALID_INPUT:{path}", file=sys.stderr); sys.exit(3)
    return data

def _require_tz_or_die(chart: dict, label: str, tz_flag: str | None) -> str:
    tz = chart.get("tz")
    if isinstance(tz, str) and tz.strip():
        return tz
    if tz_flag:
        return tz_flag
    print(f"MISSING_TZ_{label}", file=sys.stderr); sys.exit(3)

def compute_band_and_features(a_chart: dict, b_chart: dict):
    a_ts = ts_v0.extract_ts(a_chart)
    b_ts = ts_v0.extract_ts(b_chart)
    feats = ts_v0.compute_features(a_ts, b_ts)
    band = ts_v0.band_v0(feats)
    return band, {"a": a_ts, "b": b_ts, "features": feats}

def build_public_envelope(band: str, *, engine_tag: str, invocation_tag: str, release_id: str) -> dict:
    env = {
        "eligible": True,
        "categories": [{"id": "harmony", "band": band}],
        "meta": {"engine_tag": engine_tag, "invocation_tag": invocation_tag},
        "release_id": release_id,
    }
    pre = sercanon(env)
    env["idempotence_hash"] = hashlib.sha256(pre).hexdigest()
    return env

# ---- command ----
def run_showcompat(ns) -> int:
    a = _read_json_or_die(ns.a)
    b = _read_json_or_die(ns.b)
    _require_tz_or_die(a, "A", ns.a_tz)
    _require_tz_or_die(b, "B", ns.b_tz)

    engine_tag = os.environ.get("ENGINE_TAG", "hdengine-alpha")
    invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-UNKNOWN")
    release_id = os.environ.get("RELEASE_ID", "0"*64)

    band, _ = compute_band_and_features(a, b)
    env = build_public_envelope(band, engine_tag=engine_tag, invocation_tag=invocation_tag, release_id=release_id)
    sys.stdout.buffer.write(sercanon(env))
    return 0

# ---- main ----
def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    ap = build_parser()
    ns = ap.parse_args(argv)
    if ns.cmd == "showcompat":
        return run_showcompat(ns)
    return 64

if __name__ == "__main__":
    sys.exit(main())
