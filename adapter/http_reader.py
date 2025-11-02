from __future__ import annotations
import hashlib, json, os
from pathlib import Path
from flask import Blueprint, Response, request, Flask
from engine.presenter.emitter import emit_compact_json
from engine.runtime import emit_reader_public_bytes

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

def get_reader_bp(emit_fn=None):
    """
    Factory: returns a Blueprint exposing /reader (to be mounted under /api).
    emit_fn(a,b,engine_tag,invocation_tag,release_id) -> bytes
    """
    if emit_fn is None:
        emit_fn = emit_reader_public_bytes
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

        body = emit_fn(
            a,
            b,
            engine_tag=engine_tag,
            invocation_tag=invocation_tag,
            release_id=release_id,
        )
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

_SERVICE_IDENTITY_PATH = Path("artifacts/identity/service_identity.json")


# === EPIC-005 /internal/version (Blueprint: bp) ===
# 'bp', 'Response', and 'request' are already imported above
# /internal/version stays DB-decoupled; no DB resolver imports or connections here.

def _read_release_id() -> str:
    try:
        return Path("artifacts/math/release_id.txt").read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        manifest = Path("catalog/manifest.json").read_bytes()
        return hashlib.sha256(manifest).hexdigest()


def _load_service_identity() -> dict[str, str]:
    try:
        raw = _SERVICE_IDENTITY_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def _build_internal_version_payload() -> dict[str, str]:
    identity = _load_service_identity()
    engine_tag = identity.get("engine_tag") or os.environ.get("ENGINE_TAG", "hdengine-alpha")
    release_id = identity.get("release_id") or _read_release_id()
    invocation_tag = identity.get("invocation_tag") or os.environ.get("PRODUCT_INVOCATION_TAG", "INV-UNKNOWN")
    build_commit = identity.get("build_commit") or os.environ.get("BUILD_COMMIT", "unknown")
    emitter_sha256 = identity.get("emitter_sha256") or os.environ.get("EMITTER_SHA256", "unknown")
    return {
        "engine_tag": engine_tag,
        "release_id": release_id,
        "invocation_tag": invocation_tag,
        "build_commit": build_commit,
        "emitter_sha256": emitter_sha256,
    }


# --- ensure blueprint exists for internal routes ---
try:
    bp
except NameError:
    bp = Blueprint("reader_v1", __name__)


@bp.route("/internal/version", methods=["GET", "HEAD"])
def internal_version():
    # deny identity overrides in prod
    if request.headers.get("X-Identity-Override"):
        body_bytes, _ = emit_compact_json({"error": "override_denied", "detail": "identity overrides disabled in prod"})
        r = Response(body_bytes, status=400, mimetype="application/json; charset=utf-8")
        r.headers["Cache-Control"] = "no-store"
        return r  # NO ETag

    payload = _build_internal_version_payload()
    body_bytes, _ = emit_compact_json(payload, sort_keys=False)

    if request.method == "HEAD":
        # HEAD parity: same type; no body; CL equals GET body size
        r = Response(b"", status=200, mimetype="application/json; charset=utf-8")
        r.headers["Content-Length"] = str(len(body_bytes))
    else:
        r = Response(body_bytes, status=200, mimetype="application/json; charset=utf-8")

    r.headers["Cache-Control"] = "no-store"  # deliberately NO ETag
    r.headers.pop("ETag", None)
    return r

# === EPIC-005: app factory ===
def create_app():
    app = Flask(__name__)
    # register internal reader blueprint at root
    try:
        app.register_blueprint(bp, url_prefix="")
    except Exception as _e:
        # if bp is not defined yet, raise a clear error for operator
        raise RuntimeError("Blueprint 'bp' not found in adapter/http_reader.py") from _e

    @app.after_request
    def _strip_etag_on_internal(resp):
        # governance: no ETag on /internal/* surfaces
        try:
            if resp.headers.get("ETag") and resp.request and resp.request.path.startswith("/internal/"):
                del resp.headers["ETag"]
        except Exception:
            # safest behavior: ensure no ETag
            if "ETag" in resp.headers: del resp.headers["ETag"]
        return resp

    return app


app = create_app()

if __name__ == "__main__":
    # dev runner (Railway uses gunicorn via Procfile)
    import os
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT","8000")))

