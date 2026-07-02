"""BodyGraph resolution control-flow primitives for CLI and ops surfaces."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Mapping, MutableMapping, Optional

from .ingest import (
    IngestOutcome,
    VendorInputs,
    gather_inputs_from_env,
    ingest_vendor_bodygraph,
    resolve_db_user_id,
)
from .vendor_client import VendorError, classify_bg_resolve_route_policy

def _truthy(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    if isinstance(value, (int, float)):
        return bool(value)
    return bool(value)


@dataclass(frozen=True)
class ResolveBodygraphResult:
    """Envelope returned by :func:`resolve_bodygraph`."""

    status: str
    payload: MutableMapping[str, object]
    exit_code: int


def resolve_bodygraph(
    user_id: str,
    *,
    source: str,
    upsert: bool,
    dry_run: bool,
    env: Mapping[str, object] | None = None,
    birthdate: str | None = None,
    birthtime: str | None = None,
    location: str | None = None,
) -> ResolveBodygraphResult:
    """Return a deterministic placeholder resolution envelope for Phase S8a.

    This function intentionally avoids network and database effects. It only
    captures the control-flow decisions required for the CLI/ops surfaces while
    the rails remain closed.
    """

    env = env or {}
    requested_source = (source or "auto").lower()
    if requested_source not in {"auto", "db", "vendor"}:
        raise ValueError(f"unsupported source '{requested_source}'")

    safe_mode_closed = _truthy(env.get("SAFE_MODE"))
    allow_network = _truthy(env.get("ALLOW_NETWORK"))
    snapshot = {
        "user_id": user_id,
        "requested_source": requested_source,
        "upsert": bool(upsert),
        "dry_run": bool(dry_run),
        "safe_mode": safe_mode_closed,
        "allow_network": allow_network,
    }

    if requested_source == "vendor":
        return _resolve_vendor(
            user_id,
            snapshot,
            upsert=upsert,
            dry_run=dry_run,
            env=env,
            birthdate=birthdate,
            birthtime=birthtime,
            location=location,
        )

    # Phase S8a treats "auto" as "db" while avoiding real IO.
    payload = {
        "status": "ok",
        "resolver": {
            **snapshot,
            "resolved_source": "db",
            "note": "BodyGraph DB resolution is stubbed for Phase S8a; no IO performed.",
        },
    }
    return ResolveBodygraphResult(status="ok", payload=payload, exit_code=0)


def _resolve_vendor(
    user_id: str,
    snapshot: MutableMapping[str, object],
    *,
    upsert: bool,
    dry_run: bool,
    env: Mapping[str, object] | None,
    birthdate: str | None,
    birthtime: str | None,
    location: str | None,
) -> ResolveBodygraphResult:
    safe_mode_closed = bool(snapshot.get("safe_mode"))
    allow_network = bool(snapshot.get("allow_network"))
    resolver_meta = {**snapshot, "resolved_source": "vendor"}
    if safe_mode_closed:
        payload = {
            "status": "error",
            "error": {
                "code": "PROVIDER_REFUSED",
                "message": "Vendor source is refused under SAFE rails (SAFE_MODE=1).",
            },
            "resolver": resolver_meta,
        }
        return ResolveBodygraphResult(status="error", payload=payload, exit_code=1)
    if not allow_network:
        payload = {
            "status": "error",
            "error": {
                "code": "PROVIDER_NETWORK_BLOCKED",
                "message": "Network disabled under current rails.",
            },
            "resolver": resolver_meta,
        }
        return ResolveBodygraphResult(status="error", payload=payload, exit_code=1)
    try:
        route_policy = _classify_env_route_policy(env)
    except VendorError as exc:
        return _vendor_error(exc, resolver_meta)
    resolver_meta = {**resolver_meta, "route_policy": route_policy}
    if not route_policy["supported"]:
        error = VendorError(
            str(route_policy["error_code"]),
            "bg:resolve vendor route unsupported for configured base",
            details={
                "classification": route_policy["classification"],
                "configured_base_version": route_policy["configured_base_version"],
                "route_family": route_policy["route_family"],
                "resource_path": route_policy["resource_path"],
            },
        )
        return _vendor_error(error, resolver_meta)
    try:
        vendor_inputs = _resolve_inputs(user_id, birthdate, birthtime, location)
    except VendorError as exc:
        return _vendor_error(exc, resolver_meta)
    try:
        normalized_user_id = resolve_db_user_id(vendor_inputs.user_id)
    except VendorError as exc:
        return _vendor_error(exc, resolver_meta)
    except Exception as exc:  # pragma: no cover - defensive guardrail
        unexpected = VendorError(
            "PROVIDER_INPUT_INVALID",
            "user_id normalization failed",
            details={"error": exc.__class__.__name__},
        )
        return _vendor_error(unexpected, resolver_meta)
    vendor_inputs = replace(vendor_inputs, user_id=normalized_user_id)
    try:
        outcome = ingest_vendor_bodygraph(vendor_inputs, env=env, dry_run=dry_run)
    except VendorError as exc:
        return _vendor_error(exc, resolver_meta)
    ingest_section = {
        "provider": outcome.vendor,
        "vendor_version": outcome.vendor_version,
        "input_fingerprint": outcome.input_fingerprint,
        "idempotency_key": outcome.idempotency_key,
        "rows_written": outcome.rows_written,
        "db_rows_after": outcome.db_rows_after,
        "duration_ms": round(outcome.duration_ms, 3),
        "payload_sha256": outcome.payload_sha256,
        "db_emitted_sha256": outcome.db_emitted_sha256,
        "parity_match": outcome.parity_match,
    }
    payload = {
        "status": "ok",
        "resolver": resolver_meta,
        "ingest": ingest_section,
    }
    return ResolveBodygraphResult(status="ok", payload=payload, exit_code=0)


def _classify_env_route_policy(env: Mapping[str, object] | None) -> Mapping[str, object]:
    source = env or {}
    canonical = str(source.get("HD_API_BASE_URL") or "").strip().rstrip("/")
    legacy = str(source.get("HDAPI_BASE_URL") or "").strip().rstrip("/")
    if canonical and legacy and canonical != legacy:
        raise VendorError("PROVIDER_CONFIG_INVALID", "ambiguous HD API base URL configuration")
    base_url = canonical or legacy
    if not base_url:
        raise VendorError(
            "PROVIDER_CONFIG_MISSING",
            "missing vendor configuration",
            details={"missing": ["HD_API_BASE_URL"]},
        )
    return classify_bg_resolve_route_policy(base_url)


def _resolve_inputs(user_id: str, birthdate: str | None, birthtime: str | None, location: str | None) -> VendorInputs:
    provided = [birthdate, birthtime, location]
    if all(isinstance(value, str) and value.strip() for value in provided):
        return VendorInputs(
            user_id=user_id,
            birthdate=birthdate.strip(),
            birthtime=birthtime.strip(),
            location=location.strip(),
        )
    env_inputs = gather_inputs_from_env()
    return VendorInputs(
        user_id=user_id,
        birthdate=env_inputs.birthdate,
        birthtime=env_inputs.birthtime,
        location=env_inputs.location,
    )


def _vendor_error(error: VendorError, resolver: Mapping[str, object]) -> ResolveBodygraphResult:
    payload = {
        "status": "error",
        "error": error.as_payload(),
        "resolver": dict(resolver),
    }
    return ResolveBodygraphResult(status="error", payload=payload, exit_code=1)
