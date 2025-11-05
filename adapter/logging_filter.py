import time, uuid, json
from datetime import datetime, timezone
import logging
from flask import request, g

# Canonical logger
_LOG = logging.getLogger("engine.app")

# Allowlisted short route names
_ALLOWED_ROUTES = {"reader","aux_narrative","internal_readyz","startup"}

def _now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00","Z")

def _route_name():
    ep = (request.endpoint or "")
    short = ep.split(".", 1)[0] if "." in ep else ep
    return short if short in _ALLOWED_ROUTES else short or "unknown"

def _emit_line(app, line: str):
    # Append to app-configured sink list if present
    sink = app.config.get("LOG_SINK")
    if isinstance(sink, list):
        sink.append(line)
    _LOG.info(line)

def install(app):
    @app.before_request
    def _start_timer_and_cid():
        g._t0 = time.perf_counter()
        g._cid = request.headers.get("X-Correlation-Id") or uuid.uuid4().hex

    @app.after_request
    def _keys_only_after(resp):
        # Echo correlation id
        resp.headers["X-Correlation-Id"] = g.get("_cid", "")
        # Keys-only JSON line (no bodies, no headers mirrored)
        duration_ms = int((time.perf_counter() - g.get("_t0", time.perf_counter())) * 1000)
        obj = {
            "at": _now_iso(),
            "route": _route_name(),
            "status": resp.status_code,
            "duration_ms": duration_ms,
            "idempotence_hash": getattr(g, "_idempotence_hash", ""),
            "release_id": app.config.get("RELEASE_ID", ""),
        }
        line = json.dumps(obj, separators=(",",":"), sort_keys=True)
        _emit_line(app, line)
        return resp

def log_startup_line(app, status: int = 0):
    """Emit one keys-only line during startup checks (no bodies)."""
    obj = {
        "at": _now_iso(),
        "route": "startup",
        "status": status,
        "duration_ms": 0,
        "idempotence_hash": "",
        "release_id": app.config.get("RELEASE_ID", ""),
    }
    line = json.dumps(obj, separators=(",",":"), sort_keys=True)
    _emit_line(app, line)
