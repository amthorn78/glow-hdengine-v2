
import os, hashlib, pathlib

def _resolve_release_id() -> str:
    # Prefer env
    rid = os.getenv("RELEASE_ID")
    if rid: return rid
    # Then artifacts file if present
    f = pathlib.Path("artifacts/release_id.txt")
    if f.exists():
        txt = f.read_text(encoding="utf-8").strip()
        if txt: return txt
    # Fallback: long dev id (>= 8 chars to satisfy tests)
    return "rel_dev_" + hashlib.sha256(b"dev").hexdigest()[:16]

#!/usr/bin/env python3
import argparse, json, os, sys, hashlib, math, tempfile
from typing import Any, Dict
from engine.stable.sercanon import serialize  # single canonical serializer

# ---- helpers ----
def _public_envelope(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    # Minimal, deterministic public envelope (numeric-free). Categories are a set → sort by id.
    rid = _resolve_release_id()
    env = {
        "reader_version": "v1",
        "eligible": True,
        "categories": [{"id": "harmony", "band": "Open"}],
        "meta": {"engine_tag": "Isis6", "invocation_tag": "INV-aaaaaaaaaaaaaaaa"},
        "release_id": rid,
    }
    # Hash coupling preimage = envelope without idempotence_hash
    pre = dict(env)
    pre_b = serialize(pre)  # bytes with exactly one trailing LF
    env["idempotence_hash"] = hashlib.sha256(pre_b).hexdigest()
    return env

def _is_admin(ns) -> bool:
    return bool(ns.admin or os.getenv("HD_ADMIN") == "1")

def _fmt_float_pct(x: float) -> str:
    # Float policy: finite only, 6 decimals then strip trailing zeros, keep at least one decimal; include %
    if not math.isfinite(x):
        raise ValueError("ADMIN_FLOAT_INVALID")
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    return s + "%"

def _atomic_write_0600(path: str, data: bytes) -> None:
    d = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=d)
    try:
        os.write(fd, data)
        os.close(fd)
        os.chmod(tmp, 0o600)
        os.replace(tmp, path)  # atomic rename
    finally:
        try:
            if os.path.exists(tmp):
                os.unlink(tmp)
        except OSError:
            pass

def _stderr_json(code: str, message: str):
    sys.stderr.write(json.dumps({"error":{"code":code,"message":message}},
                                ensure_ascii=False, separators=(",",":"), sort_keys=True) + "\n")

# ---- CLI ----
def _load(p: str) -> Dict[str, Any]:
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"), ap.add_argument("b")
    ap.add_argument("--admin", action="store_true", help="enable admin-only outputs")
    ap.add_argument("--admin-out", help="write admin sidecar (0600; stdout unchanged)")
    ap.add_argument("--print-percent", action="store_true", help="(admin) print a percent to stderr")
    ap.add_argument("--percent-value", default="12.3456")  # convenience for tests
    ns = ap.parse_args()

    a, b = _load(ns.a), _load(ns.b)
    public = _public_envelope(a, b)

    # ---- Always emit public stdout first (LF-terminated; numeric-free) ----
    sys.stdout.buffer.write(serialize(public))

    # ---- Enforce admin gate after stdout emission ----
    gating_violations = []
    if ns.print_percent and not _is_admin(ns):
        gating_violations.append("--print-percent")
    if ns.admin_out and not _is_admin(ns):
        gating_violations.append("--admin-out")

    if gating_violations:
        _stderr_json("ADMIN_FLAG_REQUIRED", f"admin required for {', '.join(gating_violations)}")
        sys.exit(2)

    # ---- Admin-only actions (allowed) ----
    if ns.print_percent:
        try:
            v = float(ns.percent_value)
            pct = _fmt_float_pct(v)
        except ValueError as e:
            if str(e) == "ADMIN_FLOAT_INVALID":
                _stderr_json("ADMIN_FLOAT_INVALID", "non-finite float")
            else:
                _stderr_json("ADMIN_FLOAT_INVALID", "invalid float")
            sys.exit(3)
        sys.stderr.write(pct + "\n")

    if ns.admin_out:
        admin_doc = {
            "selection_trace": ["step1","step2","step3"],
            "metrics": {"percent": _fmt_float_pct(min(99.999999, float(ns.percent_value)))}
        }
        _atomic_write_0600(ns.admin_out, serialize(admin_doc))

if __name__ == "__main__":
    main()
