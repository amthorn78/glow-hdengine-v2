from __future__ import annotations
import os, json
from flask import Flask, Response, request
from engine.emit_public import emit_public_envelope
from pathlib import Path

app = Flask(__name__)

@app.get("/health")
def health():
    # Minimal deterministic body with a single LF
    return Response("ok\n", mimetype="text/plain; charset=utf-8"), 200


def _error(token: str, code: int = 400):
    """
    One-line, LF-terminated JSON error body.
    A5 transport: content-type only; no ETag/Cache-Control.
    """
    body = json.dumps({"error": token}, ensure_ascii=False, separators=(",", ":")) + "\n"
    return Response(body, mimetype="application/json; charset=utf-8"), code

ALLOWED_ROOT = Path("fixtures/charts").resolve()

def _safe_load_chart(path_str: str) -> dict:
    """
    Dev harness loader:
    - resolve path (no symlinks)
    - must live under fixtures/charts
    - JSON -> dict
    """
    p = Path(path_str)
    try:
        rp = p.resolve(strict=True)
    except FileNotFoundError:
        raise ValueError("invalid_path")
    # deny symlinks and traversal/outside-root
    if rp.is_symlink() or not str(rp).startswith(str(ALLOWED_ROOT) + os.sep):
        raise ValueError("invalid_path")
    try:
        obj = json.loads(rp.read_text(encoding="utf-8"))
    except Exception:
        raise ValueError("invalid_json")
    if not isinstance(obj, dict):
        raise ValueError("invalid_json")
    return obj

def _require_tz_or_raise(chart: dict, label: str, tz_flag: str | None) -> None:
    """
    Ensure chart has tz; else, if tz_flag present, set it; otherwise raise with exact token.
    """
    tz = chart.get("tz")
    if isinstance(tz, str) and tz.strip():
        return
    if isinstance(tz_flag, str) and tz_flag.strip():
        chart["tz"] = tz_flag
        return
    raise ValueError(f"missing_tz_{label}")


def _read_json_dict(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if not isinstance(obj, dict):
        raise ValueError("invalid_json")
    return obj


@app.get("/api/reader")
def reader_v1():
    # A5: v=1 only. APP_ENV must be dev for harness; otherwise 403 with no parsing/FS.
    if request.args.get("v") != "1":
        return _error("invalid_version")

    if os.environ.get("APP_ENV", "dev") != "dev":
        return _error("forbidden", 403)

    a_path = request.args.get("a")
    b_path = request.args.get("b")
    a_tz  = request.args.get("a_tz")
    b_tz  = request.args.get("b_tz")

    if not a_path or not b_path:
        return _error("missing_param")

    # Path-safe loads under fixtures/charts
    try:
        a = _safe_load_chart(a_path)
        b = _safe_load_chart(b_path)
    except ValueError as ve:
        return _error(str(ve))

    # Tz requirements (exact tokens missing_tz_A / missing_tz_B)
    try:
        _require_tz_or_raise(a, "A", a_tz)
        _require_tz_or_raise(b, "B", b_tz)
    except ValueError as e:
        return _error(str(e))

    engine_tag    = os.environ.get("ENGINE_TAG", "hdengine-alpha")
    invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-UNKNOWN")
    release_id    = os.environ.get("RELEASE_ID", "0" * 64)

    body = emit_public_envelope(a, b, engine_tag, invocation_tag, release_id)
    return Response(body, mimetype="application/json; charset=utf-8"), 200
if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    app.run(host=host, port=port, debug=False)
