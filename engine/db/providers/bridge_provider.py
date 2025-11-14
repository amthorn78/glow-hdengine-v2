"""HTTPS bridge DB provider."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Mapping, Sequence
import json
from urllib.parse import urlparse
import urllib.error
import urllib.request

from ..errors import BridgeUnavailable, BridgeUnsupported, IntrospectionError, SqlExecError, TxError

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
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:  # type: ignore[arg-type]
            return BridgeResponse(
                status=getattr(resp, "status", resp.getcode()),
                body=resp.read(),
                headers={k.lower(): v for k, v in resp.headers.items()},
            )
    except urllib.error.HTTPError as exc:  # pragma: no cover - network behavior mocked
        return BridgeResponse(status=exc.code, body=exc.read(), headers=dict(exc.headers or {}))


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

    def _json_request(self, method: str, path: str, payload: Mapping[str, Any] | None = None) -> Dict[str, Any]:
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
        if response.status != 200:
            raise BridgeUnavailable(
                "bridge_http_error",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_http_error",
            )
        try:
            return json.loads(response.body.decode("utf-8"))
        except Exception as exc:
            raise BridgeUnavailable(
                "bridge_invalid_json",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_invalid_json",
            ) from exc

    def health(self) -> None:
        data = self._json_request("GET", "/health")
        if data.get("status") != "ok":
            raise BridgeUnavailable(
                "bridge_health_failed",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="bridge_health_failed",
            )

    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]:
        payload = {"sql": sql, "params": params}
        data = self._json_request("POST", "/query", payload)
        if data.get("status") != "ok":
            raise SqlExecError(
                "bridge_query_failed",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_query_failed")),
            )
        rows = data.get("rows", [])
        return [tuple(row) if isinstance(row, list) else tuple(row) for row in rows]

    def exec(self, sql: str, params: Params = None) -> None:
        payload = {"sql": sql, "params": params}
        data = self._json_request("POST", "/exec", payload)
        if data.get("status") != "ok":
            raise SqlExecError(
                "bridge_exec_failed",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_exec_failed")),
            )

    def tx(self, statements: Sequence[Any]) -> List[Sequence[Any] | None]:
        serialised = [
            {
                "sql": getattr(stmt, "sql"),
                "params": getattr(stmt, "params", None),
                "fetch": bool(getattr(stmt, "fetch", False)),
            }
            for stmt in statements
        ]
        data = self._json_request("POST", "/tx", {"statements": serialised})
        if data.get("status") != "ok":
            raise TxError(
                "bridge_tx_failed",
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
        data = self._json_request("GET", f"/introspect/{kind}")
        if data.get("status") != "ok":
            raise IntrospectionError(
                "bridge_introspect_failed",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code=str(data.get("error", "bridge_introspect_failed")),
            )
        payload = data.get("payload")
        return self._normalize_introspect(kind, payload)

    def _normalize_introspect(self, kind: str, payload: Any) -> Any:
        if kind == "grants" and isinstance(payload, dict):
            grants = [tuple(entry) for entry in payload.get("grants", [])]
            normalised = dict(payload)
            normalised["grants"] = grants
            return normalised
        return payload
