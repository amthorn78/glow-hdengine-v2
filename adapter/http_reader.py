from __future__ import annotations
import hashlib, json, os
from datetime import datetime, timezone
from pathlib import Path
from flask import Blueprint, Response, request, Flask, g
from threading import Lock
from engine.presenter.emitter import emit_public
from engine.serializer import canon
from engine.runtime import emit_reader_public_bytes
from engine.narratives import emit_public_aux, get_pack
from engine.sampler.core import CandidateFeatures, ViewerProfile, sample_and_rank
from adapter.no_io_guard import NoIoGuard
from engine.compat.errors import error_envelope

_PROCESS_STARTED_AT = datetime.now(timezone.utc)
_PROCESS_PID = os.getpid()

# A7 helpers
def _sha256_hex(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def _set_reader_200_headers(resp: Response) -> Response:
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    resp.headers["Cache-Control"] = "private, max-age=0, must-revalidate"
    resp.headers["Vary"] = "Authorization, Accept-Encoding"
    return resp


def _collect_query_values(name: str) -> list[str]:
    values = [item.strip() for item in request.args.getlist(name) if item.strip()]
    if values:
        return values
    raw = request.args.get(name)
    if not raw:
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]

_MAX_WRITER_BYTES = 32_768
_DIAGNOSTIC_ROUTE_ID = "ops.writer.diagnostic.v1"

_IDEMPOTENCE_CACHE: dict[str, dict[str, object]] = {}
_IDEMPOTENCE_CACHE_LOCK = Lock()


class _WriterTransportResponse(Response):
    def get_wsgi_headers(self, environ):  # type: ignore[override]
        headers = super().get_wsgi_headers(environ)
        if self.status_code == 204:
            headers["Content-Length"] = "0"
        return headers

def _clear_writer_error_caching(resp: Response) -> Response:
    resp.headers["Cache-Control"] = "no-store"
    resp.headers.pop("ETag", None)
    return resp


def _emit_writer_response(
    envelope: dict[str, object],
    *,
    status: int,
    extra_headers: dict[str, str] | None = None,
    sort_keys: bool = True,
) -> Response:
    body = emit_public(envelope, sort_keys=sort_keys)
    resp = Response(body, status=status, mimetype="application/json; charset=utf-8")
    resp.headers["Content-Type"] = "application/json; charset=utf-8"
    resp.headers["Cache-Control"] = "no-store"
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    resp.headers.pop("Vary", None)
    resp.headers["Content-Length"] = str(len(body))
    if extra_headers:
        for key, value in extra_headers.items():
            resp.headers[key] = value
    return resp


def _writer_error(
    code: str,
    *,
    status: int,
    extra_headers: dict[str, str] | None = None,
    sort_keys: bool = True,
) -> Response:
    envelope = error_envelope(code)
    return _emit_writer_response(
        envelope,
        status=status,
        extra_headers=extra_headers,
        sort_keys=sort_keys,
    )


def _json_content_type_ok(header_value: str | None) -> bool:
    if not header_value:
        return False
    normalized = header_value.strip().lower()
    return normalized == "application/json; charset=utf-8"


def _reject_request_too_large() -> Response:
    return _writer_error("ERR_WRITER_REQUEST_TOO_LARGE", status=413)


def _read_writer_json(
    *,
    allow_empty_body: bool,
    allowed_keys: set[str] | None = None,
) -> tuple[dict[str, object] | None, Response | None]:
    content_length = request.content_length
    if content_length is not None and content_length > _MAX_WRITER_BYTES:
        return None, _reject_request_too_large()

    raw = request.get_data(cache=False)
    if len(raw) > _MAX_WRITER_BYTES:
        return None, _reject_request_too_large()

    if not raw:
        if allow_empty_body:
            return {}, None
        return None, _writer_error("ERR_WRITER_INVALID_CONTENT_TYPE", status=415)

    if not _json_content_type_ok(request.headers.get("Content-Type")):
        return None, _writer_error("ERR_WRITER_INVALID_CONTENT_TYPE", status=415)

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return None, _writer_error("ERR_WRITER_INVALID_JSON", status=400)

    if text.startswith("\ufeff"):
        return None, _writer_error("ERR_WRITER_INVALID_JSON", status=400)

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None, _writer_error("ERR_WRITER_INVALID_JSON", status=400)

    if not isinstance(data, dict):
        return None, _writer_error("ERR_WRITER_INVALID_INPUT", status=422)

    if allowed_keys is not None:
        unknown = [k for k in data.keys() if k not in allowed_keys]
        if unknown:
            return None, _writer_error("ERR_WRITER_UNKNOWN_KEY", status=422)

    return data, None


def _require_admin_scope() -> Response | None:
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return _writer_error(
            "ERR_WRITER_UNAUTHORIZED",
            status=401,
            extra_headers={"WWW-Authenticate": "Bearer"},
        )

    token = auth_header.split(" ", 1)[1].strip()
    admin_token = (os.environ.get("HDE_TEST_TOKEN_ADMIN") or "").strip()
    none_token = (os.environ.get("HDE_TEST_TOKEN_NONE") or "").strip()

    if admin_token and token == admin_token:
        return None
    if none_token and token == none_token:
        return _writer_error("ERR_WRITER_FORBIDDEN", status=403)

    return _writer_error(
        "ERR_WRITER_UNAUTHORIZED",
        status=401,
        extra_headers={"WWW-Authenticate": "Bearer"},
    )

def _parse_if_none_match(header: str | None) -> set[str]:
    if not header: return set()
    tokens: set[str] = set()
    for part in header.split(","):
        t = part.strip()
        if not t or t.startswith("W/"): continue
        tokens.add(t)
    return tokens


def _build_diagnostic_preimage(payload: dict[str, object]) -> tuple[str, str, dict[str, object]]:
    canonical_body_bytes = canon.sercanon(payload, sort_keys=True)
    canonical_body_text = canonical_body_bytes.decode("utf-8")
    preimage_envelope = {
        "canonical_request_body": canonical_body_text,
        "method": "POST",
        "writer_route_id": _DIAGNOSTIC_ROUTE_ID,
    }
    preimage_bytes = canon.sercanon(preimage_envelope, sort_keys=True)
    digest = hashlib.sha256(preimage_bytes).hexdigest()
    canonical_json = json.loads(canonical_body_text)
    return digest, preimage_bytes.decode("utf-8"), canonical_json


def _persist_idempotence_db(
    digest: str,
    canonical_preimage_text: str,
    canonical_json: dict[str, object],
) -> bool:
    dsn = (os.environ.get("DATABASE_URL") or "").strip()
    if not dsn:
        return False
    try:
        import psycopg  # type: ignore
    except Exception:
        return False

    try:
        with psycopg.connect(dsn, connect_timeout=5) as conn, conn.cursor() as cur:  # type: ignore[attr-defined]
            try:
                cur.execute("SET LOCAL search_path TO hde, public")
            except Exception:
                cur.execute("SET search_path TO hde, public")
            cur.execute(
                """
                INSERT INTO hde.idempotent_writes (idempotence_hash, canonical_bytes, canonical_json)
                VALUES (%s, %s, %s)
                ON CONFLICT (idempotence_hash) DO NOTHING
                RETURNING canonical_bytes
                """,
                (
                    digest,
                    canonical_preimage_text,
                    json.dumps(canonical_json, separators=(",", ":"), ensure_ascii=False),
                ),
            )
            inserted = cur.fetchone()
            conn.commit()
            if inserted:
                return True
            cur.execute(
                "SELECT canonical_bytes FROM hde.idempotent_writes WHERE idempotence_hash=%s",
                (digest,),
            )
            row = cur.fetchone()
            conn.commit()
            if row and row[0] != canonical_preimage_text:
                raise ValueError("idempotence hash collision for diagnostic writer")
            return True
    except ValueError:
        raise
    except Exception:
        return False


def _persist_idempotence_record(
    digest: str,
    canonical_preimage_text: str,
    canonical_json: dict[str, object],
) -> None:
    if _persist_idempotence_db(digest, canonical_preimage_text, canonical_json):
        return

    with _IDEMPOTENCE_CACHE_LOCK:
        existing = _IDEMPOTENCE_CACHE.get(digest)
        if existing is None:
            _IDEMPOTENCE_CACHE[digest] = {
                "canonical_bytes": canonical_preimage_text,
                "canonical_json": canonical_json,
            }
            return
        if existing.get("canonical_bytes") != canonical_preimage_text:
            raise ValueError("idempotence hash collision for diagnostic writer")


ALLOWED_ROOT = Path("fixtures/charts").resolve()

def _safe_load_chart(path_str: str) -> dict:
    p = Path(path_str)
    try:
        rp = p.resolve(strict=True)
    except FileNotFoundError:
        raise ValueError("ERR_READER_INVALID_PATH")
    if rp.is_symlink() or not str(rp).startswith(str(ALLOWED_ROOT) + os.sep):
        raise ValueError("invalid_path")
    try:
        obj = json.loads(rp.read_text(encoding="utf-8"))
    except Exception:
        raise ValueError("ERR_READER_INVALID_CHART")
    if not isinstance(obj, dict):
        raise ValueError("ERR_READER_INVALID_CHART")
    return obj

def _require_tz_or_raise(chart: dict, label: str, tz_flag: str | None) -> None:
    tz = chart.get("tz")
    if isinstance(tz, str) and tz.strip(): return
    if isinstance(tz_flag, str) and tz_flag.strip():
        chart["tz"] = tz_flag; return
    raise ValueError(f"ERR_READER_MISSING_TZ_{label}")

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
            return _error("ERR_READER_INVALID_VERSION")
        if os.environ.get("APP_ENV", "dev") != "dev":
            return _error("ERR_READER_FORBIDDEN", 403)

        a_path = request.args.get("a"); b_path = request.args.get("b")
        a_tz  = request.args.get("a_tz"); b_tz  = request.args.get("b_tz")
        if not a_path or not b_path:
            return _error("ERR_READER_MISSING_PARAM")

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

    @bp.get("/api/aux/narrative")
    @bp.get("/aux/narrative")
    def aux_narrative():
        g._log_override = {"route": "aux_narrative"}
        pack = get_pack()
        category = request.args.get("category", "")
        band = request.args.get("band", "")
        perspective = request.args.get("perspective", "shared")
        viewer_top = request.args.get("viewer_top") or None
        flags = _collect_query_values("flags") or _collect_query_values("flag")
        families = tuple(_collect_query_values("families_fired"))
        release_id = request.args.get("release_id") or os.environ.get("RELEASE_ID", "0" * 64)
        requested_pack_sha = request.args.get("pack_sha") or pack.pack_sha

        emission = emit_public_aux(
            category=category,
            band=band,
            perspective=perspective,
            viewer_top=viewer_top,
            flags=flags,
            families_fired=families,
            release_id=release_id,
            pack_sha=requested_pack_sha,
        )

        headers = {
            "Content-Type": "text/plain; charset=utf-8",
            "X-Narrative-Pack-Sha": pack.pack_sha,
            "X-Narrative-Composition": emission.composition_id,
            "Vary": "Authorization, Accept-Encoding",
        }

        if not emission.suppressed:
            resp = Response(emission.body, status=200, mimetype="text/plain; charset=utf-8")
            resp.headers.update(headers)
            resp.headers["X-Narrative-Key"] = emission.key
            resp.headers["Cache-Control"] = "private, max-age=0, must-revalidate"
            digest = _sha256_hex(emission.body)
            resp.set_etag(digest)
            resp.headers["ETag"] = f'"{digest}"'
        else:
            resp = Response(b"", status=200, mimetype="text/plain; charset=utf-8")
            resp.headers.update(headers)
            resp.headers["Cache-Control"] = "no-store"
            resp.headers.pop("ETag", None)
            resp.headers["X-Narrative-Policy"] = "suppressed"

        return resp

    @bp.post("/reader")
    def reader_v1_post():
        # Explicit POST posture: typed JSON error, no-store, no ETag
        return _error("method_not_allowed", 405)

    def _rails_state() -> str:
        safe_mode = os.getenv("SAFE_MODE", "1")
        allow_network = os.getenv("ALLOW_NETWORK", "0")
        return "open" if safe_mode == "0" and allow_network == "1" else "closed"

    def _rails_env_snapshot() -> dict[str, str]:
        def _value(key: str) -> str:
            value = os.getenv(key)
            return value if value is not None else "unset"

        return {
            "SAFE_MODE": _value("SAFE_MODE"),
            "ALLOW_NETWORK": _value("ALLOW_NETWORK"),
            "APP_ENV": _value("APP_ENV"),
        }

    def _rails_refusal_response() -> Response:
        return _writer_error("rails_closed", status=503, sort_keys=False)

    @bp.route("/ops/rails/refusal", methods=["GET", "POST"])
    def ops_rails_refusal():
        g._log_override = {"route": "ops.rails.refusal"}
        with NoIoGuard() as guard:
            resp = _rails_refusal_response()
        g._no_io_attempts = guard.attempts
        return resp

    @bp.route("/ops/probe/env", methods=["GET"])
    def ops_probe_env():
        g._log_override = {"route": "ops.probe.env"}
        probe_token = os.getenv("RESTART_PROBE_TOKEN")
        payload = {
            "pid": _PROCESS_PID,
            "started_at_utc": _PROCESS_STARTED_AT.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "rails_state": _rails_env_snapshot(),
            "probe_token_present": bool(probe_token),
        }
        body = emit_public(payload, sort_keys=False)
        resp = Response(body, status=200, mimetype="application/json; charset=utf-8")
        resp.headers["Cache-Control"] = "no-store"
        resp.headers.pop("ETag", None)
        return resp

    # Discovery: internal/dev surfaces (e.g., /reader, ops probes) gate via APP_ENV
    # and return writer-style envelopes for errors. Reuse that posture here for
    # the sampler harness while keeping it out of public catalogs/A7.
    def _dev_admin_gate() -> Response | None:
        raw_app_env = os.environ.get("APP_ENV")
        app_env = raw_app_env.strip().lower() if raw_app_env is not None else None
        if app_env in {"dev", "test", "local"}:
            return None
        # Preserve writer-style error envelopes for internal/dev surfaces.
        return _writer_error("ERR_WRITER_FORBIDDEN", status=403)

    @bp.route("/internal/dev/sampler", methods=["POST"], provide_automatic_options=False)
    def dev_sampler_internal():
        """
        Dev-only sampler harness (PF20 HDE-EPIC019 D3).

        Notes:
        - Mirrors the dev sampler CLI (PR3) but keeps the CLI as the primary harness.
        - Uses the sampler core directly (PR2) and echoes seed only (PF09 DISS003.5).
        - Dev/admin gated via APP_ENV and excluded from public catalogs/A7 (PF04/PF05).
        """

        g._log_override = {"route": "internal.dev.sampler"}

        gate = _dev_admin_gate()
        if gate is not None:
            return gate

        payload, validation_error = _read_writer_json(
            allow_empty_body=False,
            allowed_keys={"viewer_id", "candidate_ids", "seed"},
        )
        if validation_error is not None:
            return validation_error

        payload = payload or {}
        viewer_id = payload.get("viewer_id")
        candidate_ids = payload.get("candidate_ids")
        seed = payload.get("seed") if "seed" in payload else None

        if not isinstance(viewer_id, str) or not viewer_id.strip():
            return _writer_error("invalid_input", status=422)
        if not isinstance(candidate_ids, list) or not candidate_ids:
            return _writer_error("invalid_input", status=422)

        normalized_ids: list[str] = []
        for cid in candidate_ids:
            if not isinstance(cid, str) or not cid.strip():
                return _writer_error("invalid_input", status=422)
            normalized_ids.append(cid.strip())

        viewer = ViewerProfile(person_uid=viewer_id.strip())
        candidates = [
            CandidateFeatures(
                person_uid=cid,
                weight=1.0,
                compat_score=0,
                band=None,
                diversity_key=None,
                is_recent=False,
                categories=None,
            )
            for cid in normalized_ids
        ]

        ranked = sample_and_rank(viewer, candidates)
        seed_value = str(seed) if seed is not None else None
        response_payload = {
            "viewer_id": viewer.person_uid,
            "meta": {"seed": seed_value},
            "candidate_ids": [cand.person_uid for cand in ranked.candidates],
        }

        body = emit_public(response_payload, sort_keys=True)
        resp = Response(body, status=200, mimetype="application/json; charset=utf-8")
        resp.headers["Cache-Control"] = "no-store"
        resp.headers.pop("ETag", None)
        return resp

    def _error(token: str, code: int = 400):
        envelope = error_envelope(token)
        body_bytes = emit_public(envelope)
        resp = Response(body_bytes, status=code, mimetype='application/json; charset=utf-8')
        resp.headers['Cache-Control'] = 'no-store'
        resp.headers.pop('ETag', None)
        return resp, code

    return bp

bp = get_reader_bp()

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
        body_bytes = emit_public({"error": "override_denied", "detail": "identity overrides disabled in prod"})
        r = Response(body_bytes, status=400, mimetype="application/json; charset=utf-8")
        r.headers["Cache-Control"] = "no-store"
        return r  # NO ETag

    payload = _build_internal_version_payload()
    body_bytes = emit_public(payload, sort_keys=False)

    if request.method == "HEAD":
        # HEAD parity: same type; no body; CL equals GET body size
        r = Response(b"", status=200, mimetype="application/json; charset=utf-8")
        r.headers["Content-Length"] = str(len(body_bytes))
    else:
        r = Response(body_bytes, status=200, mimetype="application/json; charset=utf-8")

    r.headers["Cache-Control"] = "no-store"  # deliberately NO ETag
    r.headers.pop("ETag", None)
    return r


@bp.route("/ops/writer/diagnostic", methods=["POST"], provide_automatic_options=False)
def diagnostic_writer():
    auth_error = _require_admin_scope()
    if auth_error is not None:
        return auth_error

    payload, validation_error = _read_writer_json(allow_empty_body=True, allowed_keys=set())
    if validation_error is not None:
        return validation_error

    payload = payload or {}
    digest, canonical_preimage_text, canonical_json = _build_diagnostic_preimage(payload)
    g._idempotence_hash = digest
    _persist_idempotence_record(digest, canonical_preimage_text, canonical_json)

    return _emit_writer_response({"ok": True, "message": "diagnostic"}, status=200)


@bp.route("/ops/writer/diagnostic", methods=["HEAD"], provide_automatic_options=False)
def diagnostic_writer_head():
    resp = _WriterTransportResponse(b"", status=405)
    resp.headers["Allow"] = "POST, OPTIONS"
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["Content-Length"] = "0"
    resp.headers.pop("Content-Type", None)
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    return resp


@bp.route("/ops/writer/diagnostic", methods=["OPTIONS"], provide_automatic_options=False)
def diagnostic_writer_options():
    resp = _WriterTransportResponse(b"", status=204)
    resp.headers["Allow"] = "POST, OPTIONS"
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["Content-Length"] = "0"
    resp.content_length = 0
    resp.direct_passthrough = False
    resp.set_data(b"")
    resp.headers.pop("Content-Type", None)
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    return resp


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
        req = getattr(resp, "request", None)
        req_path = getattr(req, "path", "")
        if req_path.startswith("/internal/") and resp.headers.get("ETag"):
            resp.headers.pop("ETag", None)
        if req_path == "/ops/writer/diagnostic" and resp.status_code in (204, 405):
            resp.headers["Content-Length"] = resp.headers.get("Content-Length", "0") or "0"
        return resp

    return app


app = create_app()

if __name__ == "__main__":
    # dev runner (Railway uses gunicorn via Procfile)
    import os
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT","8000")))

