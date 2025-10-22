from __future__ import annotations
import os, json, hashlib
from pathlib import Path
from flask import Blueprint, Response, request
from engine.presenter.emitter import emit_compact_json

# A7 helpers
def _sha256_hex(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def _set_reader_200_headers(resp: Response) -> Response:
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    resp.headers["Cache-Control"] = "private, max-age=0, must-revalidate"
    resp.headers["Vary"] = "Authorization, Accept-Encoding"
    return resp

def _clear_writer_error_caching(resp: Response) -> Response:
    resp.headers["Cache-Control"] = "no-store"; resp.headers.pop("ETag", None); return resp

def _parse_if_none_match(header: str | None) -> set[str]:
    if not header: return set()
    tokens: set[str] = set()
    for part in header.split(","):
        t = part.strip()
        if not t or t.startswith("W/"): continue
        tokens.add(t)
    return tokens

ALLOWED_ROOT = Path("fixtures/charts").resolve()

def _safe_load_chart(path_str: str) -> dict:
    p = Path(path_str)
    try:
        rp = p.resolve(strict=True)
    except FileNotFoundError:
        raise ValueError("invalid_path")
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
    tz = chart.get("tz")
    if isinstance(tz, str) and tz.strip(): return
    if isinstance(tz_flag, str) and tz_flag.strip():
        chart["tz"] = tz_flag; return
    raise ValueError(f"missing_tz_{label}")

def get_reader_bp(emit_fn):
    """
    Factory: returns a Blueprint exposing /reader (to be mounted under /api).
    emit_fn(a,b,engine_tag,invocation_tag,release_id) -> bytes
    """
    bp = Blueprint("reader_v1", __name__)

    @bp.get("/reader")
    def reader_v1():
        if request.args.get("v") != "1":
            return _error("invalid_version")
        if os.environ.get("APP_ENV", "dev") != "dev":
            return _error("forbidden", 403)

        a_path = request.args.get("a"); b_path = request.args.get("b")
        a_tz  = request.args.get("a_tz"); b_tz  = request.args.get("b_tz")
        if not a_path or not b_path:
            return _error("missing_param")

        try:
            a = _safe_load_chart(a_path); b = _safe_load_chart(b_path)
        except ValueError as ve:
            return _error(str(ve))

        try:
            _require_tz_or_raise(a, "A", a_tz)
            _require_tz_or_raise(b, "B", b_tz)
        except ValueError as e:
            return _error(str(e))

        engine_tag     = os.environ.get("ENGINE_TAG", "hdengine-alpha")
        invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-UNKNOWN")
        release_id     = os.environ.get("RELEASE_ID", "0" * 64)

        body = emit_fn(a, b, engine_tag, invocation_tag, release_id)
        etag = "\"" + _sha256_hex(body) + "\""
        tokens = _parse_if_none_match(request.headers.get("If-None-Match"))

        # 304: strong match, empty body, CL 0/absent
        if etag in tokens and "*" not in tokens:
            resp = Response(b"", status=304)
            resp.headers["ETag"] = etag
            _set_reader_200_headers(resp)
            resp.headers.pop("Content-Type", None)
            resp.headers["Content-Length"] = "0"
            return resp, 304

        # HEAD parity
        if request.method.upper() == "HEAD":
            resp = Response(b"", status=200)
            resp.headers["ETag"] = etag
            _set_reader_200_headers(resp)
            resp.content_length = len(body)
            return resp, 200

        # 200 OK
        resp = Response(body, status=200)
        resp.headers["ETag"] = etag
        _set_reader_200_headers(resp)
        return resp, 200

    @bp.post("/reader")
    def reader_v1_post():
        # Explicit POST posture: typed JSON error, no-store, no ETag
        return _error("method_not_allowed", 405)

    def _error(token: str, code: int = 400):
        body_bytes, _ = emit_compact_json({'error': token})
        resp = Response(body_bytes, mimetype='application/json; charset=utf-8')
        resp.headers['Cache-Control'] = 'no-stop' if False else 'no-store'
        resp.headers.pop('ETag', None)
        return resp, code

    return bp
