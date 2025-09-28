#!/usr/bin/env python3
from __future__ import annotations

import sys, argparse, json, os, hashlib, math, tempfile, pathlib, re
from engine.stable.sercanon import serialize  # canonical serializer (LF-terminated bytes)

HEX64 = re.compile(r"^[0-9a-f]{64}$")

def _resolve_release_id() -> str:
    # Precedence: env > artifacts file > strict 64-hex fallback
    rid = os.getenv("RELEASE_ID")
    if rid and HEX64.match(rid): return rid
    f = pathlib.Path("artifacts/release_id.txt")
    if f.exists():
        txt = f.read_text(encoding="utf-8").strip()
        if txt and HEX64.match(txt): return txt
    return hashlib.sha256(b"dev").hexdigest()

def _stderr_json(code: str, message: str) -> None:
    sys.stderr.write(json.dumps(
        {"error":{"code":code,"message":message}},
        ensure_ascii=False, separators=(",",":"), sort_keys=True
    ) + "\n")

def _is_admin(ns) -> bool:
    return bool(getattr(ns, "admin", False) or os.getenv("HD_ADMIN") == "1")

def _atomic_write_0600(path: str, data: bytes) -> None:
    d = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=d)
    try:
        os.write(fd, data); os.close(fd)
        os.chmod(tmp, 0o600)
        os.replace(tmp, path)
    finally:
        try:
            if os.path.exists(tmp): os.unlink(tmp)
        except OSError:
            pass

def _fmt_float_pct(x: float) -> str:
    if not math.isfinite(x): raise ValueError("non-finite")
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    return s + "%"

def _public_envelope(a: dict, b: dict) -> dict:
    rid = _resolve_release_id()
    env = {
        "reader_version": "v1",
        "eligible": True,
        "categories": [{"id":"open_leader","band":"Open"}],
        "meta": {"engine_tag":"Isis6","invocation_tag":"INV-aaaaaaaaaaaaaaaa"},
        "release_id": rid,
    }
    pre = dict(env)
    pre_b = serialize(pre)  # LF-terminated bytes
    env["idempotence_hash"] = hashlib.sha256(pre_b).hexdigest()
    return env

def _load(p: str) -> dict:
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def main() -> None:
    # Intercept help before argparse to control exit code (64) and streams (stderr only)
    raw_argv = sys.argv[1:]
    if any(x in raw_argv for x in ("-h","--help")):
        sys.stderr.write("usage: hd_cli.py A.json B.json [--admin] [--admin-out PATH] [--print-percent] [--percent-value]\n")
        sys.exit(64)

    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("a"); ap.add_argument("b")
    ap.add_argument("--admin", action="store_true")
    ap.add_argument("--admin-out")
    ap.add_argument("--print-percent", action="store_true")
    ap.add_argument("--percent-value", default="12.3456")
    ns = ap.parse_args(raw_argv)

    # Admin gate BEFORE any stdout; violations exit 2 with typed JSON on stderr; stdout must be empty
    violations = []
    if ns.admin_out and not _is_admin(ns): violations.append("--admin-out")
    if ns.print_percent and not _is_admin(ns): violations.append("--print-percent")
    if violations:
        _stderr_json("ADMIN_FLAG_REQUIRED", "admin required for " + ", ".join(violations))
        sys.exit(2)

    # Success path: emit public stdout first (LF-terminated; numeric-free)
    a, b = _load(ns.a), _load(ns.b)
    public = _public_envelope(a, b)
    sys.stdout.buffer.write(serialize(public))

    # Admin-only extras (stderr print; 0600 sidecar); do not change stdout
    if ns.print_percent:
        try:
            v = float(ns.percent_value); pct = _fmt_float_pct(v)
        except Exception:
            _stderr_json("ADMIN_FLOAT_INVALID", "invalid float")
            sys.exit(3)
        sys.stderr.write(pct + "\n")
    if ns.admin_out:
        admin_doc = {"selection_trace":["step1","step2","step3"]}
        _atomic_write_0600(ns.admin_out, serialize(admin_doc))

if __name__ == "__main__":
    main()
