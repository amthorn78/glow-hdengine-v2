from __future__ import annotations
import hashlib, json, os
from collections import ChainMap
from datetime import datetime, timezone
from pathlib import Path
from flask import Blueprint, Response, request, Flask, g
from threading import Lock
from engine.presenter.emitter import emit_public
from engine.serializer import canon
from engine.runtime import emit_reader_public_bytes, identity_admin, identity_meta
from engine.narratives import emit_public_aux, get_pack
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import conjunction_public_resolved
from engine.compat.identity import dev_compat_identity
from engine.sampler.core import CandidateFeatures, ViewerProfile, sample_and_rank
from adapter.no_io_guard import NoIoGuard
from engine.compat.errors import error_envelope
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.vendor_client import VendorError
from engine.http.compat_handler import compat_blueprint
from engine.db import DBAccess, Statement
from engine.db.errors import AdapterError, PrimaryUnavailable, RetiredBridgeConfiguration

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
_DEV_WRITER_CONJUNCTION_ROUTE_ID = "dev.writer.conjunction.v1"
_DEV_WRITER_CONJUNCTION_SUCCESS_TYPE = "dev.writer.conjunction.success.v1"
_DEV_WRITER_CONJUNCTION_ERROR_TYPE = "dev.writer.conjunction.error.v1"

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
    details: object | None = None,
    extra_headers: dict[str, str] | None = None,
    envelope_type: str | None = None,
    sort_keys: bool = True,
) -> Response:
    envelope = error_envelope(code, details=details)
    if envelope_type:
        envelope["type"] = envelope_type
    return _emit_writer_response(
        envelope,
        status=status,
        extra_headers=extra_headers,
        sort_keys=sort_keys,
    )


def _retired_db_writer_error(
    exc: RetiredBridgeConfiguration,
    *,
    envelope_type: str | None = None,
) -> Response:
    return _writer_error(
        "ERR_WRITER_RAILS_CLOSED",
        status=503,
        details={
            "adapter_code": exc.code,
            "retired_keys": list(exc.retired_keys),
        },
        envelope_type=envelope_type,
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


def _build_writer_request_preimage(
    *,
    payload: dict[str, object],
    method: str,
    writer_route_id: str,
) -> tuple[str, str, dict[str, object]]:
    canonical_body_bytes = canon.sercanon(payload, sort_keys=True)
    canonical_body_text = canonical_body_bytes.decode("utf-8")
    preimage_envelope = {
        "canonical_request_body": canonical_body_text,
        "method": method,
        "writer_route_id": writer_route_id,
    }
    preimage_bytes = canon.sercanon(preimage_envelope, sort_keys=True)
    digest = hashlib.sha256(preimage_bytes).hexdigest()
    canonical_json = json.loads(canonical_body_text)
    return digest, preimage_bytes.decode("utf-8"), canonical_json


def _build_diagnostic_preimage(payload: dict[str, object]) -> tuple[str, str, dict[str, object]]:
    return _build_writer_request_preimage(
        payload=payload,
        method="POST",
        writer_route_id=_DIAGNOSTIC_ROUTE_ID,
    )


def _persist_idempotence_db(
    digest: str,
    canonical_preimage_text: str,
    canonical_json: dict[str, object],
) -> bool:
    try:
        db = DBAccess.for_current_env()
    except RetiredBridgeConfiguration:
        # Retired configuration is an intentional typed refusal.  It must not
        # be converted into the process-local fallback.
        raise
    except AdapterError:
        return False

    try:
        results = db.tx(
            (
                Statement("SET LOCAL search_path TO hde, public"),
                Statement(
                    """
                INSERT INTO hde.idempotent_writes (idempotence_hash, canonical_bytes, canonical_json)
                VALUES (%s, %s, %s)
                ON CONFLICT (idempotence_hash) DO NOTHING
                RETURNING canonical_bytes
                    """,
                    (
                        digest,
                        canonical_preimage_text,
                        canon.sercanon(canonical_json, sort_keys=True).decode("utf-8"),
                    ),
                    fetch=True,
                ),
                Statement(
                    "SELECT canonical_bytes FROM hde.idempotent_writes WHERE idempotence_hash=%s",
                    (digest,),
                    fetch=True,
                ),
            )
        )
    except AdapterError:
        return False

    if len(results) != 3:
        return False
    inserted = results[1] or ()
    selected = results[2] or ()
    rows = inserted or selected
    if not rows or not isinstance(rows[0], (list, tuple)) or not rows[0]:
        return False
    if rows[0][0] != canonical_preimage_text:
        raise ValueError("idempotence hash collision for diagnostic writer")
    return True


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

        meta = identity_meta()
        body = emit_fn(
            a,
            b,
            engine_tag=meta["engine_tag"],
            invocation_tag=meta["invocation_tag"],
            release_id=meta["release_id"],
        )
        etag = "\"" + _sha256_hex(body) + "\""
        tokens = _parse_if_none_match(request.headers.get("If-None-Match"))

        # 304: strong match, empty body, CL 0/absent
        if etag in tokens and "*" not in tokens:
            resp = Response(b"", status=304)
            resp.headers["ETag"] = etag
            _set_reader_200_headers(resp)
            resp.headers.pop("Content-Type", None)
            resp.headers.pop("Content-Length", None)
            resp.automatically_set_content_length = False
            return resp, 304

        # HEAD parity
        if request.method.upper() == "HEAD":
            resp = Response(b"", status=200)
            resp.headers["ETag"] = etag
            _set_reader_200_headers(resp)
            resp.headers["Content-Length"] = str(len(body))
            return resp, 200

        # 200 OK
        resp = Response(body, status=200)
        resp.headers["ETag"] = etag
        _set_reader_200_headers(resp)
        resp.headers["Content-Length"] = str(len(body))
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
        release_id = request.args.get("release_id") or identity_meta()["release_id"]
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

    @bp.route("/ops/db/unavailable", methods=["GET"])
    def ops_db_unavailable():
        g._log_override = {"route": "ops.db.unavailable"}
        with NoIoGuard() as guard:
            def _raise_primary(_: str):
                raise PrimaryUnavailable(
                    "forced_db_unavailable",
                    attempts=["forced_db_unavailable"],
                    code="forced_db_unavailable",
                )
            # Override the diagnostic DSN without reading or mutating the
            # ambient value.  ChainMap key iteration lets the adapter refuse a
            # present retired key before it accesses any DATABASE_URL value.
            forced_env = ChainMap({"DATABASE_URL": "db://unavailable"}, os.environ)
            try:
                DBAccess.for_current_env(
                    environ=forced_env,
                    psycopg_factory=_raise_primary,
                )
            except AdapterError:
                # This diagnostic route deliberately injects the historical
                # forced-unavailable scenario.  Keep its public bytes stable
                # while the direct-only adapter normalizes the internal
                # provider failure to primary_connect_failed.
                details = {"adapter_code": "forced_db_unavailable"}
                env = error_envelope("ERR_WRITER_RAILS_CLOSED", details=details)
                resp = _emit_writer_response(env, status=503, sort_keys=False)
            else:
                env = error_envelope(
                    "ERR_WRITER_RAILS_CLOSED", details={"adapter_code": "unexpected_db_available"}
                )
                resp = _emit_writer_response(env, status=503, sort_keys=False)
        g._no_io_attempts = guard.attempts
        return resp

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
    # the sampler harness. The route is included in the internal Endpoint
    # Catalog inventory, but excluded from A7 and public contracts.
    def _dev_admin_gate() -> Response | None:
        raw_app_env = os.environ.get("APP_ENV")
        app_env = raw_app_env.strip().lower() if raw_app_env is not None else None
        if app_env in {"dev", "test", "local"}:
            return None
        # Preserve writer-style error envelopes for internal/dev surfaces.
        return _writer_error("ERR_WRITER_FORBIDDEN", status=403)

    def _default_viewer_weights() -> dict[str, int]:
        return {category: 10 for category in CATEGORIES_ORDER_V1}

    def _conjunction_part(prefix: str) -> dict[str, str] | None:
        user_id = (request.args.get(f"{prefix}_user_id") or "").strip()
        if not user_id:
            return None
        part: dict[str, str] = {"user_id": user_id}
        for field in ("birthdate", "birthtime", "location"):
            value = (request.args.get(f"{prefix}_{field}") or "").strip()
            if value:
                part[field] = value
        return part

    def _canonical_conjunction_request(left: dict[str, str], right: dict[str, str]) -> dict[str, object]:
        return {
            "a": left,
            "b": right,
            "query": {
                "a_birthdate": left.get("birthdate", ""),
                "a_birthtime": left.get("birthtime", ""),
                "a_location": left.get("location", ""),
                "a_user_id": left["user_id"],
                "b_birthdate": right.get("birthdate", ""),
                "b_birthtime": right.get("birthtime", ""),
                "b_location": right.get("location", ""),
                "b_user_id": right["user_id"],
            },
        }

    def _emit_dev_writer_conjunction_response() -> Response:
        left = _conjunction_part("a")
        right = _conjunction_part("b")
        if left is None or right is None:
            return _writer_error(
                "ERR_WRITER_INVALID_INPUT",
                status=422,
                envelope_type=_DEV_WRITER_CONJUNCTION_ERROR_TYPE,
            )

        request_payload = _canonical_conjunction_request(left, right)
        digest, canonical_preimage_text, canonical_json = _build_writer_request_preimage(
            payload=request_payload,
            method="GET",
            writer_route_id=_DEV_WRITER_CONJUNCTION_ROUTE_ID,
        )
        g._idempotence_hash = digest
        try:
            _persist_idempotence_record(digest, canonical_preimage_text, canonical_json)
        except RetiredBridgeConfiguration as exc:
            return _retired_db_writer_error(
                exc,
                envelope_type=_DEV_WRITER_CONJUNCTION_ERROR_TYPE,
            )

        response = _emit_conjunction_response(
            left=left,
            right=right,
            envelope_type=_DEV_WRITER_CONJUNCTION_ERROR_TYPE,
        )
        if response.status_code != 200:
            return response

        try:
            conjunction_payload = json.loads(response.get_data(as_text=True))
        except json.JSONDecodeError:
            return _writer_error(
                "ERR_WRITER_INVALID_INPUT",
                status=422,
                envelope_type=_DEV_WRITER_CONJUNCTION_ERROR_TYPE,
            )

        writer_payload = {
            "ok": True,
            "schema": "v1",
            "type": _DEV_WRITER_CONJUNCTION_SUCCESS_TYPE,
            "writer": {
                "idempotence_hash": digest,
                "method": "GET",
                "writer_route_id": _DEV_WRITER_CONJUNCTION_ROUTE_ID,
            },
            "result": conjunction_payload,
        }
        return _emit_writer_response(writer_payload, status=200)

    def _emit_conjunction_response(
        *,
        left: dict[str, str] | None = None,
        right: dict[str, str] | None = None,
        envelope_type: str | None = None,
    ) -> Response:
        left = left if left is not None else _conjunction_part("a")
        right = right if right is not None else _conjunction_part("b")
        if left is None or right is None:
            return _writer_error(
                "ERR_WRITER_INVALID_INPUT",
                status=422,
                envelope_type=envelope_type,
            )

        rails_env = {
            "SAFE_MODE": os.getenv("SAFE_MODE", "1"),
            "ALLOW_NETWORK": os.getenv("ALLOW_NETWORK", "0"),
        }
        local_people: dict[str, dict[str, str]] = {}
        if rails_env["SAFE_MODE"] == "0" and rails_env["ALLOW_NETWORK"] == "1":
            left_uid = resolve_db_user_id(left["user_id"])
            right_uid = resolve_db_user_id(right["user_id"])
            local_people[left_uid] = {"person_uid": left_uid}
            local_people[right_uid] = {"person_uid": right_uid}

        def _local_lookup(user_id: str) -> dict[str, str] | None:
            return local_people.get(user_id)

        compat_identity = dev_compat_identity()
        try:
            payload = conjunction_public_resolved(
                left,
                right,
                viewer_top=CATEGORIES_ORDER_V1[0],
                viewer_weights=_default_viewer_weights(),
                engine_tag=compat_identity["engine_tag"],
                release_id=compat_identity["release_id"],
                invocation_tag=compat_identity["invocation_tag"],
                env=rails_env,
                local_lookup=_local_lookup,
            )
        except VendorError as exc:
            details = {
                "provider_code": exc.code,
                "provider_message": exc.message,
                "rails": rails_env,
            }
            if exc.details is not None:
                details["provider_details"] = exc.details
            envelope = error_envelope("ERR_WRITER_RAILS_CLOSED", details=details)
            if envelope_type:
                envelope["type"] = envelope_type
            return _emit_writer_response(
                envelope,
                status=503,
                sort_keys=True,
            )
        except ValueError:
            return _writer_error(
                "ERR_WRITER_INVALID_INPUT",
                status=422,
                envelope_type=envelope_type,
            )

        body = emit_public(payload, sort_keys=True)
        resp = Response(body, status=200, mimetype="application/json; charset=utf-8")
        resp.headers["Cache-Control"] = "no-store"
        resp.headers.pop("ETag", None)
        return resp

    @bp.route("/internal/dev/sampler", methods=["POST"], provide_automatic_options=False)
    def dev_sampler_internal():
        """
        Dev-only sampler harness (PF20 HDE-EPIC019 D3).

        Notes:
        - Mirrors the dev sampler CLI (PR3) but keeps the CLI as the primary harness.
        - Uses the sampler core directly (PR2) and echoes seed only (PF09 DISS003.5).
        - Dev/admin gated via APP_ENV; internal Endpoint Catalog inventory only,
          excluded from A7 and public contracts (PF04/PF05).
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

    @bp.get("/dev/sampler/conjunction")
    def dev_sampler_conjunction():
        g._log_override = {"route": "dev.sampler.conjunction"}
        gate = _dev_admin_gate()
        if gate is not None:
            return gate
        return _emit_conjunction_response()

    @bp.get("/dev/reader/conjunction")
    def dev_reader_conjunction():
        g._log_override = {"route": "dev.reader.conjunction"}
        gate = _dev_admin_gate()
        if gate is not None:
            return gate
        return _emit_conjunction_response()

    @bp.get("/dev/writer/conjunction")
    def dev_writer_conjunction():
        g._log_override = {"route": "dev.writer.conjunction"}
        gate = _dev_admin_gate()
        if gate is not None:
            return gate
        return _emit_dev_writer_conjunction_response()

    def _error(token: str, code: int = 400):
        envelope = error_envelope(token)
        body_bytes = emit_public(envelope)
        resp = Response(body_bytes, status=code, mimetype='application/json; charset=utf-8')
        resp.headers['Cache-Control'] = 'no-store'
        resp.headers.pop('ETag', None)
        return resp, code

    return bp

bp = get_reader_bp()

# === EPIC-005 /internal/version (Blueprint: bp) ===
# /internal/version stays DB-decoupled and obtains immutable identity from the runtime authority.

def _build_internal_version_payload() -> dict[str, str]:
    return identity_admin()


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
    try:
        _persist_idempotence_record(digest, canonical_preimage_text, canonical_json)
    except RetiredBridgeConfiguration as exc:
        return _retired_db_writer_error(exc)

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

    # compat blueprint (shared with wsgi) -- scoped to compat routes only
    app.register_blueprint(compat_blueprint)

    def _compat_error_response(status: int) -> Response:
        envelope = error_envelope("ERR_NOT_FOUND")
        payload = emit_public(envelope)
        resp = Response(payload, status=status, mimetype="application/json; charset=utf-8")
        resp.headers["Cache-Control"] = "no-store"
        resp.headers.pop("ETag", None)
        resp.headers.pop("Content-Encoding", None)
        resp.headers["Content-Length"] = str(len(payload))
        return resp

    @app.errorhandler(404)
    def _compat_scoped_not_found(err):  # type: ignore[override]
        if request.path.rstrip("/").startswith("/api/compat/v1"):
            return _compat_error_response(404)
        return err

    @app.errorhandler(405)
    def _compat_scoped_method_not_allowed(err):  # type: ignore[override]
        if request.path.rstrip("/").startswith("/api/compat/v1"):
            return _compat_error_response(405)
        return err

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
