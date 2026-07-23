"""BodyGraph resolution control-flow primitives for CLI and ops surfaces."""

from __future__ import annotations

import os
from dataclasses import dataclass, replace
from typing import Mapping, MutableMapping, Optional
from uuid import UUID

from engine.db import DBAccess
from engine.db.errors import AdapterError

from .ingest import (
    IngestOutcome,
    VendorInputs,
    gather_inputs_from_env,
    ingest_vendor_bodygraph,
    resolve_db_user_id,
)
from .v2_adapter import V2ChartAdapterContext, adapt_v2_chart_payload
from .mapped_cache import MappedCacheError, persist_mapped_bodygraph
from .vendor_client import HdApiClient, VendorError, classify_bg_resolve_route_policy, route_auth_posture

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


@dataclass(frozen=True)
class _ResolvedUserIdentity:
    database_user_id: str
    person_uid_seed: str


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
    """Resolve BodyGraph data within the selected source and rail posture."""

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
    vendor_env = _vendor_config_env(env)
    database_env = dict(vendor_env)
    # DB selection is key-presence-sensitive; restore scoped None entries
    # that the vendor configuration overlay intentionally treats as removal.
    if env is not None:
        database_env.update(env)
    try:
        route_policy = _classify_env_route_policy(vendor_env)
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
        user_identity = _resolve_user_identity(vendor_inputs.user_id)
    except VendorError as exc:
        return _vendor_error(exc, resolver_meta)
    except Exception as exc:  # pragma: no cover - defensive guardrail
        unexpected = VendorError(
            "PROVIDER_INPUT_INVALID",
            "user_id normalization failed",
            details={"error": exc.__class__.__name__},
        )
        return _vendor_error(unexpected, resolver_meta)
    vendor_inputs = replace(vendor_inputs, user_id=user_identity.database_user_id)
    if route_policy["route_family"] == "recommended_v2_chart":
        return _resolve_vendor_v2_chart(
            user_identity,
            resolver_meta,
            vendor_inputs,
            vendor_env=vendor_env,
            database_env=database_env,
            upsert=upsert,
            dry_run=dry_run,
            route_policy=route_policy,
        )
    try:
        outcome = ingest_vendor_bodygraph(
            vendor_inputs,
            env=database_env,
            dry_run=dry_run,
        )
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


def _resolve_vendor_v2_chart(
    user_identity: _ResolvedUserIdentity,
    resolver_meta: MutableMapping[str, object],
    vendor_inputs: VendorInputs,
    *,
    vendor_env: Mapping[str, object],
    database_env: Mapping[str, object],
    upsert: bool,
    dry_run: bool,
    route_policy: Mapping[str, object],
) -> ResolveBodygraphResult:
    db: DBAccess | None = None
    if not dry_run and not upsert:
        error = VendorError(
            "PROVIDER_WRITE_UNSUPPORTED",
            "v2 chart-backed mapped-cache persistence requires explicit upsert intent",
            details={
                "route_family": route_policy["route_family"],
                "payload_posture": "adapter_mapped_no_raw_vendor_payload",
            },
        )
        return _vendor_error(error, resolver_meta)
    requested_app_env = str(vendor_env.get("APP_ENV") or vendor_env.get("ENGINE_ENV") or "").strip().lower()
    database_app_env = str(os.environ.get("APP_ENV") or os.environ.get("ENGINE_ENV") or "").strip().lower()
    if not dry_run and {requested_app_env, database_app_env} & {"prod", "production", "live"}:
        return _vendor_error(
            VendorError("PROVIDER_WRITE_UNSUPPORTED", "mapped-cache persistence is refused in production-like environments"),
            resolver_meta,
        )
    if not dry_run:
        try:
            db = DBAccess.for_current_env(environ=database_env)
        except AdapterError as exc:
            return _vendor_error(
                VendorError("DB_WRITER_UNAVAILABLE", "mapped-cache database target unavailable", details={"code": exc.code}),
                resolver_meta,
            )
    try:
        client = HdApiClient.from_env(env=vendor_env)
        request = client.build_contract_route_request(
            path="charts",
            request_fields=("birthdate", "birthtime", "location"),
            geocode_required=True,
            birthdate=vendor_inputs.birthdate,
            birthtime=vendor_inputs.birthtime,
            location=vendor_inputs.location,
        )
        vendor_result = client.fetch(request)
    except VendorError as exc:
        return _vendor_error(exc, resolver_meta)
    context = V2ChartAdapterContext(
        person_uid=_person_uid(user_identity.person_uid_seed),
        user_id=user_identity.database_user_id,
        vendor="hdapi",
        vendor_version=2,
        input_fingerprint=request.input_fingerprint,
        route_family=str(route_policy["route_family"]),
        route=request.route,
        payload_family="ChartResult",
    )
    adapter = adapt_v2_chart_payload(vendor_result.payload, context).as_dict()
    request_posture = _redacted_request_posture(request, route_policy)
    resolver_meta = {**resolver_meta, "request": request_posture}
    if adapter["status"] != "mapped":
        error = VendorError(
            str(adapter["code"]),
            "v2 chart adapter could not map vendor payload into BodyGraph posture",
            details={
                "adapter_status": adapter["status"],
                "payload_family": adapter["payload_family"],
                "missing_internal_contract_fields": adapter["missing_internal_contract_fields"],
                "missing_vendor_detail_fields": adapter["missing_vendor_detail_fields"],
            },
        )
        return _vendor_error(error, resolver_meta)
    if not dry_run:
        assert db is not None
        try:
            cache_result = persist_mapped_bodygraph(db, adapter["cache"])
        except MappedCacheError as exc:
            return _vendor_error(VendorError(exc.code, str(exc)), resolver_meta)
        payload = {
            "status": "ok",
            "resolver": resolver_meta,
            "adapter": {"status": adapter["status"], "code": adapter["code"], "payload_family": adapter["payload_family"]},
            "cache": {
                "input_fingerprint": adapter["cache"]["input_fingerprint"],
                "payload_posture": adapter["cache"]["payload_posture"],
                "user_id": adapter["cache"]["user_id"],
                "vendor": adapter["cache"]["vendor"],
                "vendor_version": adapter["cache"]["vendor_version"],
            },
            "ingest": cache_result.as_dict(),
        }
        return ResolveBodygraphResult(status="ok", payload=payload, exit_code=0)
    payload = {
        "status": "ok",
        "resolver": resolver_meta,
        "adapter": {
            "status": adapter["status"],
            "code": adapter["code"],
            "payload_family": adapter["payload_family"],
        },
        "resolved": adapter["resolved"],
        "cache": {
            "input_fingerprint": adapter["cache"]["input_fingerprint"],
            "payload_posture": adapter["cache"]["payload_posture"],
            "user_id": adapter["cache"]["user_id"],
            "vendor": adapter["cache"]["vendor"],
            "vendor_version": adapter["cache"]["vendor_version"],
        },
        "ingest": {
            "rows_written": 0,
            "db_rows_after": 0,
            "payload_posture": "adapter_mapped_no_raw_vendor_payload",
        },
    }
    return ResolveBodygraphResult(status="ok", payload=payload, exit_code=0)


def _person_uid(user_id: str) -> str:
    normalized = (user_id or "").strip()
    return normalized if normalized.startswith("person-") else f"person-{normalized}"


def _resolve_user_identity(user_id: str) -> _ResolvedUserIdentity:
    database_user_id = resolve_db_user_id(user_id)
    person_uid_seed = (user_id or "").strip()
    try:
        canonical_uuid = str(UUID(person_uid_seed))
    except ValueError:
        return _ResolvedUserIdentity(
            database_user_id=database_user_id,
            person_uid_seed=person_uid_seed,
        )
    return _ResolvedUserIdentity(
        database_user_id=canonical_uuid,
        person_uid_seed=canonical_uuid,
    )


def _redacted_request_posture(request: object, route_policy: Mapping[str, object]) -> Mapping[str, object]:
    headers = getattr(request, "headers", {})
    header_posture = []
    if "Authorization" in headers:
        header_posture.append("Authorization: Bearer <redacted>")
    if "HD-Api-Key" in headers:
        header_posture.append("HD-Api-Key: <redacted>")
    if "HD-Geocode-Key" in headers:
        header_posture.append("HD-Geocode-Key: <redacted>")
    return {
        "route": getattr(request, "route", ""),
        "resource_path": route_policy["resource_path"],
        "route_auth_posture": route_auth_posture(str(route_policy["resource_path"])),
        "header_posture": sorted(header_posture),
        "configured_base_url": "<redacted>",
        "url_posture": "configured_base_url/<resource_path>",
        "input_fingerprint": getattr(request, "input_fingerprint", ""),
        "raw_body_emitted": False,
        "raw_response_body_emitted": False,
    }


def _vendor_config_env(env: Mapping[str, object] | None) -> Mapping[str, object]:
    import os

    merged: dict[str, object] = dict(os.environ)
    if env is not None:
        if "HD_API_BASE_URL" in env or "HDAPI_BASE_URL" in env:
            merged.pop("HD_API_BASE_URL", None)
            merged.pop("HDAPI_BASE_URL", None)
        for key, value in env.items():
            if value is None:
                merged.pop(key, None)
            else:
                merged[key] = value
    return merged


def _classify_env_route_policy(env: Mapping[str, object] | None) -> Mapping[str, object]:
    source = env or {}

    def _config_value(name: str) -> str:
        value = source.get(name)
        return value.strip() if isinstance(value, str) else ""

    canonical = _config_value("HD_API_BASE_URL").rstrip("/")
    legacy = _config_value("HDAPI_BASE_URL").rstrip("/")
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
