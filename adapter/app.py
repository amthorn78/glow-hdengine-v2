import os, json, uuid, hashlib, time, sys
from typing import Callable, Iterable, Tuple, List, Dict, Any

# --- helpers (env per-request; no import-time I/O) ---
def _env(name: str, default: str = "") -> str:
    return os.getenv(name, default)

def _engine_env() -> str:
    return _env("ENGINE_ENV", "dev").lower()

def _engine_tag() -> str:
    return _env("ENGINE_TAG", "engine-dev")

def _release_id() -> str:
    return _env("RELEASE_ID", "release-dev")

def _adapter_version() -> str:
    return "v1"

def _sercanon(obj: Any) -> bytes:
    # Stable, minified, sorted JSON + trailing newline
    return (json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")

def _common_headers(correlation_id: str) -> List[Tuple[str, str]]:
    headers = [
        ("Cache-Control", "no-store"),
        ("Content-Type", "application/json; charset=utf-8"),
        ("X-Correlation-Id", correlation_id),
        ("X-Engine-Tag", _engine_tag()),
        ("X-Release-Id", _release_id()),
        ("X-Adapter-Version", _adapter_version()),
        ("X-Content-Type-Options", "nosniff"),
        ("Referrer-Policy", "no-referrer"),
        ("X-Frame-Options", "DENY"),
    ]
    if _engine_env() == "prod":
        headers.append(("Strict-Transport-Security", "max-age=31536000; includeSubDomains"))
    return headers

def _resp_ok(payload: Dict[str, Any], corr: str, status: str = "200 OK",
             extra_headers: List[Tuple[str, str]] = None) -> Tuple[str, List[Tuple[str, str]], bytes]:
    body = _sercanon(payload)
    headers = _common_headers(corr)
    if extra_headers:
        headers.extend(extra_headers)
    return status, headers, body

def _resp_err(code: str, error: str, corr: str, status: str) -> Tuple[str, List[Tuple[str, str]], bytes]:
    body = _sercanon({"ok": False, "schema": "v1", "code": code, "error": error})
    headers = _common_headers(corr)
    return status, headers, body

def _sha256_path(p: str) -> str:
    try:
        h = hashlib.sha256()
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(131072), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return "0" * 64

def _build_version_payload() -> Dict[str, Any]:
    checksums = {
        "weights_sha": _sha256_path("freeze/freeze_pack_v1.json"),
        "bands_sha": _sha256_path("config/bands_4B60_v1.json"),
        "catalog_sha": _sha256_path("catalog/gates_v1.json"),
    }
    return {
        "ok": True, "schema": "v1",
        "engine_tag": _engine_tag(), "release_id": _release_id(),
        "checksums": checksums,
        "toggles_sha": _env("TOGGLES_SHA", "0"*64),
        "build": {"commit": _env("BUILD_COMMIT_SHORT", "dev"),
                  "timestamp": _env("BUILD_TIMESTAMP_UTC", "1970-01-01T00:00:00Z")}
    }

# --- readiness deps (import without I/O) ---
try:
    from core.config.toggles_resolver import resolve_toggles, OverridesNotAllowedInProd
except Exception:
    resolve_toggles = None
    class OverridesNotAllowedInProd(Exception): ...
try:
    from core.pipeline.compute import compute_pair
except Exception:
    compute_pair = None

def _resolve() -> Tuple[Dict[str, Any], str, bool]:
    if resolve_toggles is None:
        raise RuntimeError("resolver-missing")
    resolved, frozen_sha, applied = resolve_toggles()
    return resolved, frozen_sha, applied

def _load_json(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        json.load(f)

def _smoke() -> float:
    if compute_pair is None:
        raise RuntimeError("compute-missing")
    t0 = time.perf_counter()
    compute_pair({"gates": [1]}, {"gates": [2]}, debug=False)
    return (time.perf_counter() - t0) * 1000.0  # ms

def _log_once(method: str, path: str, status: str, corr: str, t_ms: float) -> None:
    try:
        code = int((status or "0").split()[0])
    except Exception:
        code = 0
    rec = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "method": method,
        "path": path,
        "status": code,
        "latency_ms": round(t_ms, 3),
        "correlation_id": corr,
    }
    print(json.dumps(rec, separators=(",", ":"), sort_keys=True), file=sys.stdout, flush=True)

# --- WSGI app ---
def app(environ, start_response: Callable) -> Iterable[bytes]:
    t0 = time.perf_counter()
    method = (environ.get("REQUEST_METHOD") or "GET").upper()
    path = environ.get("PATH_INFO", "") or ""
    corr = environ.get("HTTP_X_CORRELATION_ID") or uuid.uuid4().hex

    def done(status: str, headers: List[Tuple[str, str]], body: bytes) -> Iterable[bytes]:
        # Start response, then emit exactly one access log line
        start_response(status, headers)
        _log_once(method, path, status, corr, (time.perf_counter() - t0) * 1000.0)
        return [b""] if method == "HEAD" else [body]

    if method not in ("GET", "HEAD"):
        status, headers, body = _resp_err("MethodNotAllowed", "Only GET/HEAD allowed", corr, "405 Method Not Allowed")
        return done(status, headers, body)

    if path == "/internal/healthz":
        status, headers, body = _resp_ok({"ok": True, "schema": "v1"}, corr)
        return done(status, headers, body)

    if path == "/internal/version":
        if _engine_env() == "prod":
            auth = environ.get("HTTP_AUTHORIZATION", "")
            ok = False
            if auth.startswith("Bearer "):
                token = auth.split(" ", 1)[1]
                ok = (token == _env("ENGINE_SERVICE_TOKEN", ""))
            if not ok:
                status, headers, body = _resp_err("Unauthorized", "InvalidOrMissingToken", corr, "401 Unauthorized")
                return done(status, headers, body)
        status, headers, body = _resp_ok(_build_version_payload(), corr)
        return done(status, headers, body)

    if path == "/internal/readyz":
        try:
            resolved, frozen_sha, applied = _resolve()
        except OverridesNotAllowedInProd:
            status, headers, body = _resp_err("OverridesNotAllowedInProd", "Overrides present in prod", corr, "503 Service Unavailable")
            return done(status, headers, body)
        except Exception:
            status, headers, body = _resp_err("DependencyFailure", "resolver", corr, "503 Service Unavailable")
            return done(status, headers, body)
        try:
            _load_json("catalog/gates_v1.json")
            _load_json("config/bands_4B60_v1.json")
            _load_json("freeze/freeze_pack_v1.json")
        except Exception:
            status, headers, body = _resp_err("DependencyFailure", "catalogs", corr, "503 Service Unavailable")
            return done(status, headers, body)
        try:
            ms = _smoke()
            if ms > 800.0:
                status, headers, body = _resp_err("SmokeFailed", "latency", corr, "503 Service Unavailable")
                return done(status, headers, body)
        except Exception:
            status, headers, body = _resp_err("SmokeFailed", "exception", corr, "503 Service Unavailable")
            return done(status, headers, body)
        extra = [("X-Toggles-SHA", frozen_sha)]
        status, headers, body = _resp_ok({"ok": True, "schema": "v1"}, corr, extra_headers=extra)
        return done(status, headers, body)

    status, headers, body = _resp_err("NotFound", "Unknown path", corr, "404 Not Found")
    return done(status, headers, body)
