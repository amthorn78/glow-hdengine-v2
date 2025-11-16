"""HTTPS bridge DB provider."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Mapping, Sequence
import json
import time
from urllib.parse import urlparse
import urllib.error
import urllib.request

from ..errors import BridgeUnavailable, BridgeUnsupported, IntrospectionError, SqlExecError, TxError
from ...ops.http_log import log_http_call

Params = Sequence[Any] | Mapping[str, Any] | None


@dataclass
class BridgeResponse:
    status: int
    body: bytes
    headers: Mapping[str, Any]


RequestFunc = Callable[[str, str, bytes | None, Mapping[str, str]], BridgeResponse]


def _default_request(url: str, method: str, data: bytes | None, headers: Mapping[str, str]) -> BridgeResponse:
    req = urllib.request.Request(url, data=data, method=method)
    for key, value in headers.items():
        req.add_header(key, value)

    parsed = urlparse(url)
    path = parsed.path or "/"
    route = f"db_bridge.{method.lower()}:{path}"
    start = time.monotonic()
    status: int | str = "error"
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:  # type: ignore[arg-type]
            status = getattr(resp, "status", resp.getcode())
            response = BridgeResponse(
                status=status,
                body=resp.read(),
                headers={k.lower(): v for k, v in resp.headers.items()},
            )
    except urllib.error.HTTPError as exc:  # pragma: no cover - network behavior mocked
        status = exc.code
        response = BridgeResponse(status=exc.code, body=exc.read(), headers=dict(exc.headers or {}))
    finally:
        duration = (time.monotonic() - start) * 1000.0
        log_http_call(route=route, status=status, duration_ms=duration)

    return response


class BridgeProvider:
    """Provider that talks to the DB bridge over HTTPS."""

    name = "bridge"

    def __init__(self, base_url: str, *, request: RequestFunc | None = None):
        cleaned = (base_url or "").strip()
        if not cleaned:
            raise BridgeUnavailable(
                "missing_bridge_url",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="missing_bridge_url",
            )
        parsed = urlparse(cleaned)
        if parsed.scheme != "https":
            raise BridgeUnsupported(
                "bridge_requires_https",
                attempts=["DB_BRIDGE_URL"],
                code="bridge_requires_https",
            )
        self._base_url = cleaned.rstrip("/")
        self._request = request or _default_request

    def _json_request(self, method: str, path: str, payload: Mapping[str, Any] | None = None) -> tuple[Dict[str, Any], int]:
        url = f"{self._base_url}{path}"
        data: bytes | None = None
        headers = {"Content-Type": "application/json"}
        if payload is not None:
            data = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
        try:
            response = self._request(url, method, data, headers)
        except urllib.error.URLError as exc:
            raise BridgeUnavailable(
                "bridge_network_error",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_network_error",
            ) from exc
        except TimeoutError as exc:
            raise BridgeUnavailable(
                "bridge_network_timeout",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_network_timeout",
            ) from exc
        except OSError as exc:
            raise BridgeUnavailable(
                "bridge_network_error",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_network_error",
            ) from exc
        try:
            payload_obj = json.loads(response.body.decode("utf-8"))
        except Exception as exc:
            raise BridgeUnavailable(
                "bridge_invalid_json",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_invalid_json",
            ) from exc
        return payload_obj, response.status

    def health(self) -> None:
        data, status = self._json_request("GET", "/health")
        if status != 200 or data.get("status") != "ok":
            raise BridgeUnavailable(
                "bridge_health_failed",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_health_failed",
            )

    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]:
        payload: Dict[str, Any] = {"sql": sql}
        if params is not None:
            payload["params"] = params
        data, status = self._json_request("POST", "/query", payload)
        if status != 200:
            detail = str(data.get("detail") or data.get("error") or "bridge_query_failed")
            raise SqlExecError(
                detail,
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_query_failed")),
            )
        if data.get("status") != "ok":
            detail = str(data.get("detail") or data.get("error") or "bridge_query_failed")
            raise SqlExecError(
                detail,
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_query_failed")),
            )
        rows = data.get("rows", [])
        return [tuple(row) if isinstance(row, list) else tuple(row) for row in rows]

    def exec(self, sql: str, params: Params = None) -> None:
        payload: Dict[str, Any] = {"sql": sql}
        if params is not None:
            payload["params"] = params
        data, status = self._json_request("POST", "/exec", payload)
        if status != 200:
            detail = str(data.get("detail") or data.get("error") or "bridge_exec_failed")
            raise SqlExecError(
                detail,
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_exec_failed")),
            )
        if data.get("status") != "ok":
            detail = str(data.get("detail") or data.get("error") or "bridge_exec_failed")
            raise SqlExecError(
                detail,
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_exec_failed")),
            )

    def tx(self, statements: Sequence[Any]) -> List[Sequence[Any] | None]:
        serialised = []
        for stmt in statements:
            entry: Dict[str, Any] = {
                "sql": getattr(stmt, "sql"),
                "fetch": bool(getattr(stmt, "fetch", False)),
            }
            params = getattr(stmt, "params", None)
            if params is not None:
                entry["params"] = params
            serialised.append(entry)
        data, status = self._json_request("POST", "/tx", {"statements": serialised})
        if status != 200:
            detail = str(data.get("detail") or data.get("error") or "bridge_tx_failed")
            raise TxError(
                detail,
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_tx_failed")),
            )
        if data.get("status") != "ok":
            detail = str(data.get("detail") or data.get("error") or "bridge_tx_failed")
            raise TxError(
                detail,
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_tx_failed")),
            )
        results: List[Sequence[Any] | None] = []
        for entry in data.get("results", []):
            if entry is None:
                results.append(None)
            else:
                results.append([tuple(row) if isinstance(row, list) else tuple(row) for row in entry])
        return results

    def introspect(self, kind: str) -> Any:
        if kind == "version":
            return self._introspect_version()

        data, status = self._json_request("GET", f"/introspect/{kind}")
        if status != 200 or data.get("status") != "ok":
            raise IntrospectionError(
                "bridge_introspect_failed",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_introspect_failed")),
            )

        payload = data.get("payload")
        if payload is None:
            payload = data

        return self._normalize_introspect(kind, payload)

    def _normalize_introspect(self, kind: str, payload: Any) -> Any:
        if kind == "search_path" and isinstance(payload, str):
            return {"status": "ok", "search_path": payload}

        if isinstance(payload, dict):
            normalised = dict(payload)
            normalised.setdefault("status", "ok")
            if kind == "grants":
                grants = normalised.get("grants", [])
                if isinstance(grants, list):
                    converted: List[Any] = []
                    for entry in grants:
                        if isinstance(entry, list):
                            converted.append(tuple(entry))
                        else:
                            converted.append(entry)
                    normalised["grants"] = converted
            return normalised

        return payload

    def _introspect_version(self) -> Mapping[str, Any]:
        try:
            rows = self.query("SELECT current_setting('server_version')", [])
        except SqlExecError as exc:
            raise IntrospectionError(
                "bridge_version_failed",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_version_failed",
            ) from exc

        version = ""
        if rows and rows[0]:
            first = rows[0]
            version = str(first[0]) if first else ""

        return {"status": "ok", "version": version}
