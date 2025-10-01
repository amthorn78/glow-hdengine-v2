#!/usr/bin/env python3
import sys, argparse, json, os, hashlib
import pathlib as _p
# Make repo root importable so "engine/…" resolves when running from scripts/
sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1]))

from pathlib import Path
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
    sc.add_argument("--showmath", action="store_true", help="enable admin sidecar math (stdout invariant)")
    sc.add_argument("--admin", action="store_true", help="admin gate switch")
    sc.add_argument("--admin-out", required=False, help="path to write admin sidecar (strict gate required)")
    return ap

# ---- helpers ----
def _read_json_or_die(path: str) -> dict:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
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
    _require_tz_or_die(a, "A", getattr(ns, "a_tz", None))
    _require_tz_or_die(b, "B", getattr(ns, "b_tz", None))

    engine_tag = os.environ.get("ENGINE_TAG", "hdengine-alpha")
    invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-UNKNOWN")
    release_id = os.environ.get("RELEASE_ID", "0"*64)

    band, _ = compute_band_and_features(a, b)

    # strict negative gate: if admin_out is present, require showmath AND (admin OR HD_ADMIN=1)
    if getattr(ns, "admin_out", None):
        have_showmath = bool(getattr(ns, "showmath", False))
        have_admin = bool(getattr(ns, "admin", False)) or (os.environ.get("HD_ADMIN") == "1")
        if not (have_showmath and have_admin):
            print("GATE_MISUSE: require --showmath AND --admin-out AND (--admin OR HD_ADMIN=1)", file=sys.stderr)
            return 2

    env = build_public_envelope(band, engine_tag=engine_tag, invocation_tag=invocation_tag, release_id=release_id)

    # positive gate: write TS-v0 sidecar atomically (stdout invariant)
    if getattr(ns, "admin_out", None) and getattr(ns, "showmath", False) and (getattr(ns, "admin", False) or os.environ.get("HD_ADMIN") == "1"):
        sc = build_sidecar_ts_v0(a, b, band=band, engine_tag=engine_tag, invocation_tag=invocation_tag, release_id=release_id)
        write_sidecar_atomic(ns.admin_out, sc)

    sys.stdout.buffer.write(sercanon(env))
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


import tempfile, stat

def write_sidecar_atomic(path: str, obj: dict) -> None:
    """Atomic JSON write: LF-terminated, mode 0600 on POSIX, fsync file + parent dir."""
    data = sercanon(obj)
    d = os.path.dirname(path) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp.", dir=d)
    try:
        os.fchmod(fd, stat.S_IRUSR | stat.S_IWUSR)  # 0600
        with os.fdopen(fd, "wb", closefd=False) as w:
            w.write(data); w.flush(); os.fsync(w.fileno())
        os.replace(tmp, path)
        # fsync parent dir (best-effort)
        try:
            dirfd = os.open(d, os.O_DIRECTORY)
            try: os.fsync(dirfd)
            finally: os.close(dirfd)
        except Exception:
            pass
    finally:
        try: os.close(fd)
        except Exception: pass
        try: os.remove(tmp)
        except FileNotFoundError: pass


import secrets, datetime as _dt

def _fingerprint_gates(chart: dict) -> str:
    gates = chart.get("gates") or []
    uniq_sorted = sorted({int(g) for g in gates})
    body = json.dumps({"gates": uniq_sorted}, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(body).hexdigest()

def build_sidecar_ts_v0(a_chart: dict, b_chart: dict, *, band: str, engine_tag: str, invocation_tag: str, release_id: str) -> dict:
    # Extract TS and features
    a_ts = ts_v0.extract_ts(a_chart)
    b_ts = ts_v0.extract_ts(b_chart)
    feats = ts_v0.compute_features(a_ts, b_ts)

    # Fingerprints and normalized pair order
    fa = _fingerprint_gates(a_chart)
    fb = _fingerprint_gates(b_chart)
    minfp, maxfp = (fa, fb) if fa <= fb else (fb, fa)
    a_node, b_node = (a_ts, b_ts) if fa <= fb else (b_ts, a_ts)

    # Decision list per A3 rule: Warm iff sacral_pair; else empty
    decision = ["sacral_pair"] if (band == "Warm" and feats.get("sacral_pair")) else []

    # Provenance
    cid = "CID-" + secrets.token_hex(8)
    ts_utc = _dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
        "rule_version": "ts_v0",
        "engine_tag": engine_tag,
        "invocation_tag": invocation_tag,
        "release_id": release_id,
        "correlation_id": cid,
        "pair_order": f"{minfp},{maxfp}",
        "a": a_node,
        "b": b_node,
        "features": feats,
        "decision": decision,
        "band": band,
        "timestamp": ts_utc
    }
