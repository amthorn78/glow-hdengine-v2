"""Pure HumanDesignAPI v2 chart-to-HDE BodyGraph adapter helpers."""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any, Mapping
from uuid import UUID

CHART_RESULT_REQUIRED_FIELDS = frozenset(
    {
        "activations",
        "authority",
        "birthDateUtc",
        "centers",
        "channelsLong",
        "channelsShort",
        "circuitries",
        "cognition",
        "definition",
        "determination",
        "distraction",
        "environment",
        "gates",
        "incarnationCross",
        "motivation",
        "notSelfTheme",
        "perspective",
        "profile",
        "signature",
        "strategy",
        "transference",
        "type",
        "variables",
    }
)
SUPPORTED_ROUTE_FAMILIES = frozenset({"recommended_v2_chart"})
SUPPORTED_ROUTES = frozenset({"charts", "charts/coordinates", "/v2/charts", "/v2/charts/coordinates"})
_SHA256_HEX_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class V2ChartAdapterContext:
    """Caller-supplied metadata that raw v2 chart payloads do not provide."""

    person_uid: str
    user_id: str
    vendor: str
    vendor_version: int
    input_fingerprint: str
    route_family: str
    route: str
    payload_family: str


@dataclass(frozen=True)
class V2ChartAdapterResult:
    status: str
    code: str
    payload_family: str
    missing_internal_contract_fields: tuple[str, ...]
    missing_vendor_detail_fields: tuple[str, ...]
    resolved: Mapping[str, Any] | None = None
    cache: Mapping[str, Any] | None = None

    def as_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "code": self.code,
            "missing_internal_contract_fields": list(self.missing_internal_contract_fields),
            "missing_vendor_detail_fields": list(self.missing_vendor_detail_fields),
            "payload_family": self.payload_family,
            "status": self.status,
        }
        if self.resolved is not None:
            payload["resolved"] = dict(self.resolved)
        if self.cache is not None:
            payload["cache"] = dict(self.cache)
        return payload


def _fail(code: str, payload_family: str, *, missing_internal: tuple[str, ...] = (), missing_vendor: tuple[str, ...] = ()) -> V2ChartAdapterResult:
    return V2ChartAdapterResult(
        status="unsupported",
        code=code,
        payload_family=payload_family,
        missing_internal_contract_fields=tuple(sorted(missing_internal)),
        missing_vendor_detail_fields=tuple(sorted(missing_vendor)),
    )


def _text(value: object) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _positive_int(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and value > 0:
        return value
    return None


def _uuid_text(value: object) -> str | None:
    raw = _text(value)
    if raw is None:
        return None
    try:
        return str(UUID(raw))
    except ValueError:
        return None


def _sha256_hex(value: object) -> str | None:
    raw = _text(value)
    if raw is not None and _SHA256_HEX_RE.fullmatch(raw):
        return raw
    return None


def _context_missing(context: V2ChartAdapterContext | Mapping[str, Any] | None) -> tuple[str, ...]:
    if context is None:
        return (
            "hde.body_graphs.input_fingerprint",
            "hde.body_graphs.user_id",
            "hde.body_graphs.vendor",
            "hde.body_graphs.vendor_version",
            "person_uid",
            "request.route",
            "request.route_family",
        )
    values = context.__dict__ if isinstance(context, V2ChartAdapterContext) else context
    required = {
        "person_uid": "person_uid",
        "user_id": "hde.body_graphs.user_id",
        "vendor": "hde.body_graphs.vendor",
        "vendor_version": "hde.body_graphs.vendor_version",
        "input_fingerprint": "hde.body_graphs.input_fingerprint",
        "route_family": "request.route_family",
        "route": "request.route",
        "payload_family": "payload_family",
    }
    missing: list[str] = []
    for key, label in required.items():
        value = values.get(key)
        if key == "user_id":
            valid = _uuid_text(value) is not None
        elif key == "input_fingerprint":
            valid = _sha256_hex(value) is not None
        elif key == "vendor_version":
            valid = _positive_int(value) is not None
        else:
            valid = _text(value) is not None
        if not valid:
            missing.append(label)
    return tuple(missing)


def _context_value(context: V2ChartAdapterContext | Mapping[str, Any], key: str) -> str | int:
    values = context.__dict__ if isinstance(context, V2ChartAdapterContext) else context
    raw = values.get(key)
    if key == "user_id":
        value = _uuid_text(raw)
    elif key == "input_fingerprint":
        value = _sha256_hex(raw)
    elif key == "vendor_version":
        value = _positive_int(raw)
    else:
        value = _text(raw)
    if value is None:  # guarded by _context_missing
        raise AssertionError(f"missing context value {key}")
    return value


def _unwrap_payload(payload: Mapping[str, Any], default_family: str) -> tuple[str, Mapping[str, Any] | None, str | None]:
    envelope_keys = {"data", "success", "message", "errorCode", "timestamp"}
    if envelope_keys.intersection(payload):
        family = _text(payload.get("type")) or default_family or "UNKNOWN"
        data = payload.get("data")
        if not isinstance(data, Mapping):
            return family, None, "ADAPTER_MISSING_DATA"
        return family, data, None
    family = _text(payload.get("payload_family")) or default_family or "ChartResult"
    return family, payload, None


def adapt_v2_chart_payload(
    payload: Mapping[str, Any] | object,
    context: V2ChartAdapterContext | Mapping[str, Any] | None,
) -> V2ChartAdapterResult:
    """Map a validated v2 ChartResult plus explicit context into HDE posture.

    This pure helper performs no I/O and intentionally does not wire resolver or
    ingest. Raw ChartResult/ChartSimpleResult data alone remains insufficient.
    """

    if not isinstance(payload, Mapping):
        return _fail("ADAPTER_MALFORMED_PAYLOAD", "UNKNOWN")
    missing_context = _context_missing(context)
    context_family = "UNKNOWN" if context is None else (_text((context.__dict__ if isinstance(context, V2ChartAdapterContext) else context).get("payload_family")) or "UNKNOWN")
    if missing_context:
        return _fail("ADAPTER_CONTEXT_INSUFFICIENT", context_family, missing_internal=missing_context)
    assert context is not None
    if _context_value(context, "route_family") not in SUPPORTED_ROUTE_FAMILIES:
        return _fail("ADAPTER_WRONG_ROUTE_FAMILY", _context_value(context, "payload_family"))
    if _context_value(context, "route") not in SUPPORTED_ROUTES:
        return _fail("ADAPTER_WRONG_ROUTE", _context_value(context, "payload_family"))
    if _context_value(context, "vendor") != "hdapi":
        return _fail("ADAPTER_CONTEXT_INSUFFICIENT", _context_value(context, "payload_family"), missing_internal=("hde.body_graphs.vendor",))

    expected_family = str(_context_value(context, "payload_family"))
    envelope_family, data, envelope_error = _unwrap_payload(payload, expected_family)
    if envelope_error is not None:
        return _fail(envelope_error, envelope_family)
    if envelope_family != expected_family:
        return _fail("ADAPTER_PAYLOAD_FAMILY_MISMATCH", envelope_family)
    if envelope_family == "ChartSimpleResult":
        missing = tuple(sorted(CHART_RESULT_REQUIRED_FIELDS - set(data or {})))
        return _fail("ADAPTER_VENDOR_DETAIL_INSUFFICIENT", envelope_family, missing_vendor=missing)
    if envelope_family != "ChartResult":
        return _fail("ADAPTER_UNSUPPORTED_PAYLOAD_FAMILY", envelope_family)
    assert data is not None
    missing_vendor = tuple(sorted(CHART_RESULT_REQUIRED_FIELDS - set(data)))
    if missing_vendor:
        return _fail("ADAPTER_VENDOR_DETAIL_INSUFFICIENT", envelope_family, missing_vendor=missing_vendor)

    person_uid = _context_value(context, "person_uid")
    resolved = {
        "bodygraph": {
            "authority": data["authority"],
            "birthDateUtc": data["birthDateUtc"],
            "centers": data["centers"],
            "channelsLong": data["channelsLong"],
            "channelsShort": data["channelsShort"],
            "definition": data["definition"],
            "gates": data["gates"],
            "profile": data["profile"],
            "strategy": data["strategy"],
            "type": data["type"],
        },
        "person": {"person_uid": person_uid},
        "person_uid": person_uid,
        "source": "hdapi_v2_chart_adapter",
    }
    cache = {
        "input_fingerprint": _context_value(context, "input_fingerprint"),
        "payload_posture": "adapter_mapped_no_raw_vendor_payload",
        "user_id": _context_value(context, "user_id"),
        "vendor": "hdapi",
        "vendor_version": _context_value(context, "vendor_version"),
    }
    return V2ChartAdapterResult(
        status="mapped",
        code="ADAPTER_MAPPED",
        payload_family="ChartResult",
        missing_internal_contract_fields=(),
        missing_vendor_detail_fields=(),
        resolved=resolved,
        cache=cache,
    )
