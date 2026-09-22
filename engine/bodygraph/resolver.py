"""BodyGraph resolution control-flow primitives for CLI and ops surfaces."""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass, replace
from typing import Any, Callable, Mapping, MutableMapping, Optional
from uuid import UUID

from engine.compat.error_tokens import CompatBoundaryError
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
from .mapped_cache import MappedBodyGraphRow, MappedCacheError, persist_mapped_bodygraph
from .projection import (
    BodyGraphProjectionError,
    accepted_identity_labels,
    bind_projection_identity,
    canonical_uuid,
    is_gate_ingress_code,
    project_bodygraph,
)
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


# ---------------------------------------------------------------------------
# HDE-EPIC040-PR04: complete chart-bearing resolution seam for the Magic-10
# application boundary.  Every consumer (CLI, compat route, conjunction, Reader)
# obtains a complete mapped BodyGraph with a verified canonical identity here,
# never a UID-only stand-in, a synthesized chart or a hash identity.
# ---------------------------------------------------------------------------

SOURCE_POLICIES = frozenset({"local", "vendor"})
_PROJECTION_KEYS = frozenset({"bodygraph", "person", "person_uid", "source"})
_CLOSED_RAILS_ENV: Mapping[str, object] = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}


@dataclass(frozen=True)
class ResolvedCompatChart:
    """Private, source-neutral result of :func:`resolve_compat_chart`."""

    canonical_person_id: str
    mapped_chart: Mapping[str, Any]
    source: str
    user_id: str | None
    vendor: str | None
    vendor_version: int | None
    input_fingerprint: str | None


def _birth_fields(raw: object) -> tuple[str | None, str | None, str | None]:
    if not isinstance(raw, Mapping):
        return None, None, None
    birthdate = raw.get("birthdate")
    birthtime = raw.get("birthtime")
    location = raw.get("location")
    values: list[str | None] = []
    for value in (birthdate, birthtime, location):
        if isinstance(value, str) and value.strip():
            values.append(value.strip())
        else:
            values.append(None)
    return values[0], values[1], values[2]


def _derived_birth_uid(raw: object) -> str | None:
    birthdate, birthtime, location = _birth_fields(raw)
    if not (birthdate and birthtime and location):
        return None
    preimage = f"birth|{birthdate}|{birthtime}|{location}".encode("utf-8")
    digest = hashlib.sha256(preimage).hexdigest()[:32]
    return f"birth-{digest}"


def projection_refusal(exc: BodyGraphProjectionError) -> CompatBoundaryError:
    """Map a projection refusal to the stable boundary reason and tokens."""

    code = exc.code
    if code == "GATES_EMPTY" or (code == "MISSING_FIELD" and exc.field_path == "root.bodygraph.gates"):
        reason = "gates_missing"
    elif is_gate_ingress_code(code):
        reason = "gates_invalid"
    elif code == "MISSING_FIELD":
        reason = "chart_incomplete"
    elif code in {"IDENTITY_CONFLICT", "PERSON_UID_MISMATCH"}:
        reason = "identity_conflict"
    elif code == "IDENTITY_INVALID":
        reason = "identity_invalid"
    else:
        reason = "chart_invalid"
    return CompatBoundaryError(reason, detail=code)


def _text(value: object) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _trusted_identity(raw: Mapping[str, Any], *, include_label: bool) -> tuple[str | None, set[str]]:
    """Resolve every supplied trusted identity slot to one canonical UUID.

    ``user_id`` (top-level or nested) and ``canonical_person_id`` are trusted
    resolver/DB slots.  A bare ``person_uid`` without a chart is an admitted
    engine key and is included only when ``include_label`` is set.  Two
    independently supplied, non-equivalent identities refuse.
    """

    candidates: list[str] = []
    seeds: set[str] = set()
    canonical = raw.get("canonical_person_id")
    if canonical is not None:
        value = canonical_uuid(canonical)
        if value is None:
            raise CompatBoundaryError("identity_invalid", detail="canonical_person_id")
        candidates.append(value)
    person = raw.get("person") if isinstance(raw.get("person"), Mapping) else {}
    keys = [_text(raw.get("user_id")), _text(person.get("user_id"))]
    if include_label:
        keys.append(_text(raw.get("person_uid")))
        keys.append(_text(person.get("person_uid")))
    for key in keys:
        if key is None:
            continue
        value = canonical_uuid(key)
        if value is None:
            value = canonical_uuid(resolve_db_user_id(key))
            if value is None:
                raise CompatBoundaryError("identity_invalid", detail="engine_key")
        seeds.add(key)
        candidates.append(value)
    distinct = sorted(set(candidates))
    if len(distinct) > 1:
        raise CompatBoundaryError("identity_conflict", detail="identity_slots")
    return (distinct[0] if distinct else None), seeds


def _bind_chart(
    chart: Mapping[str, Any],
    canonical_person_id: str,
    seeds: set[str],
    *,
    source: str,
    user_id: str | None,
    vendor: str | None,
    vendor_version: int | None,
    input_fingerprint: str | None,
) -> ResolvedCompatChart:
    try:
        projected = project_bodygraph(chart)
        bound = bind_projection_identity(
            projected,
            canonical_person_id,
            accepted_labels=accepted_identity_labels(canonical_person_id, seeds),
        )
    except BodyGraphProjectionError as exc:
        raise projection_refusal(exc) from None
    return ResolvedCompatChart(
        canonical_person_id=canonical_person_id,
        mapped_chart=bound,
        source=source,
        user_id=user_id,
        vendor=vendor,
        vendor_version=vendor_version,
        input_fingerprint=input_fingerprint,
    )


def _bind_lookup_hit(hit: object, canonical_person_id: str, seeds: set[str]) -> ResolvedCompatChart:
    if isinstance(hit, ResolvedCompatChart):
        if hit.canonical_person_id != canonical_person_id:
            raise CompatBoundaryError("provenance_mismatch", detail="resolved")
        return hit
    if isinstance(hit, MappedBodyGraphRow):
        if hit.user_id != canonical_person_id:
            raise CompatBoundaryError("provenance_mismatch", detail="row")
        return _bind_chart(
            hit.payload,
            canonical_person_id,
            seeds,
            source="db",
            user_id=hit.user_id,
            vendor=hit.vendor,
            vendor_version=hit.vendor_version,
            input_fingerprint=hit.input_fingerprint,
        )
    if isinstance(hit, Mapping):
        row_user_id = _text(hit.get("user_id"))
        if row_user_id is not None and canonical_uuid(row_user_id) != canonical_person_id:
            raise CompatBoundaryError("provenance_mismatch", detail="mapping")
        chart = {key: hit[key] for key in hit if key in _PROJECTION_KEYS}
        if "bodygraph" not in chart:
            raise CompatBoundaryError("chart_incomplete", detail="lookup_hit")
        return _bind_chart(
            chart,
            canonical_person_id,
            seeds,
            source="local",
            user_id=canonical_person_id if row_user_id is not None else None,
            vendor=_text(hit.get("vendor")),
            vendor_version=hit.get("vendor_version") if type(hit.get("vendor_version")) is int else None,
            input_fingerprint=_text(hit.get("input_fingerprint")),
        )
    raise CompatBoundaryError("chart_invalid", detail="lookup_hit")


def _acquire_dry_run(
    canonical_person_id: str,
    seeds: set[str],
    birth: tuple[str | None, str | None, str | None],
    env: Mapping[str, object],
) -> ResolvedCompatChart:
    """Guarded, read-only vendor acquisition through the existing v2 chart path.

    The temporary environment view handed to the vendor client is a private
    copy; it is emptied in ``finally`` before normalization and evaluation and
    on every exception path.  No process-wide setting is edited, rails are never
    opened by this function, nothing is persisted and no ``user_id`` is logged.
    """

    scoped: dict[str, object] = dict(env)
    vendor_env: dict[str, object] = {}
    database_env: dict[str, object] = {}
    try:
        if _truthy(scoped.get("SAFE_MODE")):
            raise VendorError("PROVIDER_REFUSED", "Vendor source is refused under SAFE rails (SAFE_MODE=1).")
        if not _truthy(scoped.get("ALLOW_NETWORK")):
            raise VendorError("PROVIDER_NETWORK_BLOCKED", "Network disabled under current rails.")
        vendor_env = dict(_vendor_config_env(scoped))
        database_env = dict(vendor_env)
        database_env.update(scoped)
        route_policy = _classify_env_route_policy(vendor_env)
        if not route_policy["supported"]:
            raise VendorError(
                str(route_policy["error_code"]),
                "compat acquisition route unsupported for configured base",
                details={
                    "classification": route_policy["classification"],
                    "configured_base_version": route_policy["configured_base_version"],
                    "route_family": route_policy["route_family"],
                    "resource_path": route_policy["resource_path"],
                },
            )
        birthdate, birthtime, location = birth
        missing = [name for name, value in (("birthdate", birthdate), ("birthtime", birthtime), ("location", location)) if not value]
        if missing:
            raise VendorError("PROVIDER_INPUT_MISSING", "birth inputs missing", details={"missing": missing})
        vendor_inputs = VendorInputs(
            user_id=canonical_person_id,
            birthdate=str(birthdate),
            birthtime=str(birthtime),
            location=str(location),
        )
        seed = sorted(seeds)[0] if seeds else canonical_person_id
        user_identity = _ResolvedUserIdentity(database_user_id=canonical_person_id, person_uid_seed=seed)
        resolver_meta: dict[str, object] = {
            "requested_source": "vendor",
            "resolved_source": "vendor",
            "upsert": False,
            "dry_run": True,
            "safe_mode": False,
            "allow_network": True,
            "route_policy": route_policy,
        }
        if route_policy["route_family"] == "recommended_v2_chart":
            outcome = _resolve_vendor_v2_chart(
                user_identity,
                resolver_meta,
                vendor_inputs,
                vendor_env=vendor_env,
                database_env=database_env,
                upsert=False,
                dry_run=True,
                route_policy=route_policy,
            )
            if outcome.status != "ok":
                error = outcome.payload.get("error") if isinstance(outcome.payload, Mapping) else None
                if isinstance(error, Mapping):
                    details = error.get("details")
                    raise VendorError(
                        str(error.get("code") or "PROVIDER_UNAVAILABLE"),
                        str(error.get("message") or "resolver unavailable"),
                        details=details if isinstance(details, Mapping) else None,
                    )
                raise VendorError("PROVIDER_UNAVAILABLE", "resolver unavailable")
            resolved = outcome.payload.get("resolved")
            cache = outcome.payload.get("cache")
            if not isinstance(resolved, Mapping) or not isinstance(cache, Mapping):
                raise CompatBoundaryError("chart_missing", detail="acquisition")
            return _bind_chart(
                resolved,
                canonical_person_id,
                seeds,
                source="vendor_v2_dry_run",
                user_id=_text(cache.get("user_id")),
                vendor=_text(cache.get("vendor")),
                vendor_version=cache.get("vendor_version") if type(cache.get("vendor_version")) is int else None,
                input_fingerprint=_text(cache.get("input_fingerprint")),
            )
        legacy = ingest_vendor_bodygraph(
            vendor_inputs,
            env=database_env,
            dry_run=True,
            retry_log=None,
            success_log=None,
        )
        payload = legacy.payload
        if not isinstance(payload, Mapping) or "bodygraph" not in payload:
            raise CompatBoundaryError("chart_incomplete", detail="legacy_v1")
        return _bind_chart(
            {key: payload[key] for key in payload if key in _PROJECTION_KEYS},
            canonical_person_id,
            seeds,
            source="legacy_v1_dry_run",
            user_id=canonical_person_id,
            vendor=legacy.vendor,
            vendor_version=legacy.vendor_version,
            input_fingerprint=legacy.input_fingerprint,
        )
    finally:
        vendor_env.clear()
        database_env.clear()
        scoped.clear()


def _resolve_stored(
    canonical_person_id: str,
    seeds: set[str],
    birth: tuple[str | None, str | None, str | None],
    *,
    source_policy: str,
    env: Mapping[str, object],
    local_lookup: Callable[[str], object] | None,
    acquisition: Callable[..., object] | None,
    birth_only: bool,
) -> ResolvedCompatChart:
    hit = local_lookup(canonical_person_id) if local_lookup is not None else None
    if hit is not None:
        return _bind_lookup_hit(hit, canonical_person_id, seeds)
    if source_policy == "vendor":
        if acquisition is not None:
            acquired = acquisition(
                canonical_person_id=canonical_person_id,
                seeds=frozenset(seeds),
                birth=birth,
                env=env,
            )
            if isinstance(acquired, ResolvedCompatChart):
                if acquired.canonical_person_id != canonical_person_id:
                    raise CompatBoundaryError("provenance_mismatch", detail="acquisition")
                return _bind_chart(
                    acquired.mapped_chart,
                    canonical_person_id,
                    seeds,
                    source=acquired.source,
                    user_id=acquired.user_id,
                    vendor=acquired.vendor,
                    vendor_version=acquired.vendor_version,
                    input_fingerprint=acquired.input_fingerprint,
                )
            if isinstance(acquired, Mapping):
                return _bind_lookup_hit(acquired, canonical_person_id, seeds)
            raise CompatBoundaryError("chart_missing", detail="acquisition")
        return _acquire_dry_run(canonical_person_id, seeds, birth, env)
    if local_lookup is None:
        # A surface without a read-only store (file/stdin/inline body/GET
        # fixture) cannot resolve a stored key or a birth tuple under the
        # ``local`` policy; PF05 §5.2.3 classifies that input as legacy.
        raise CompatBoundaryError(
            "legacy_input", detail="birth_only" if birth_only else "no_local_store"
        )
    raise CompatBoundaryError("person_unresolved")


def resolve_compat_chart(
    raw_party: object,
    *,
    source_policy: str,
    env: Mapping[str, object] | None,
    local_lookup: Callable[[str], object] | None = None,
    acquisition: Callable[..., object] | None = None,
) -> ResolvedCompatChart:
    """Resolve one party to a complete mapped chart with a verified canonical identity.

    Input classes (PF02 §2.2.1 / PF05 §3.7):

    1. an already-resolved complete mapped chart with trusted identity or
       provenance (``user_id``/``canonical_person_id``, a UUID label, an admitted
       engine alias, or a complete birth tuple beside the chart);
    2. a stored-user key (``user_id``/``person_uid`` engine key or plain string)
       resolved through ``resolve_db_user_id`` and the caller's read-only lookup;
    3. a complete birth-only tuple with no identity: the ``birth-`` seed is bridged
       through ``resolve_db_user_id``, the local lookup is tried first and only a
       ``vendor`` source policy may acquire under open rails, read-only.

    ``source_policy`` is ``"local"`` (no acquisition) or ``"vendor"``.  Identity
    is never derived from Gates, no chart is synthesized, and no successful
    UID-only or hash path exists.
    """

    if source_policy not in SOURCE_POLICIES:
        raise ValueError(f"unsupported source policy '{source_policy}'")
    rails_env: Mapping[str, object] = env if env is not None else _CLOSED_RAILS_ENV
    if isinstance(raw_party, ResolvedCompatChart):
        return raw_party
    if isinstance(raw_party, str):
        raw: Mapping[str, Any] = {"user_id": raw_party}
    elif isinstance(raw_party, Mapping):
        raw = raw_party
    else:
        raise CompatBoundaryError("chart_missing", detail="party")

    has_chart = "bodygraph" in raw
    trusted_id, seeds = _trusted_identity(raw, include_label=not has_chart)
    birth = _birth_fields(raw)
    birth_complete = all(birth)

    if has_chart:
        chart = {key: raw[key] for key in raw if key in _PROJECTION_KEYS}
        canonical_id = trusted_id
        if canonical_id is None:
            label = canonical_uuid(raw.get("person_uid"))
            if label is not None:
                canonical_id = label
            elif birth_complete:
                seed = _derived_birth_uid(raw)
                canonical_id = canonical_uuid(resolve_db_user_id(str(seed)))
                seeds = {str(seed)}
            else:
                raise CompatBoundaryError("identity_unresolved", detail="chart")
        return _bind_chart(
            chart,
            canonical_id,
            seeds,
            source="resolved",
            user_id=canonical_id if (_text(raw.get("user_id")) or raw.get("canonical_person_id")) else None,
            vendor=_text(raw.get("vendor")),
            vendor_version=raw.get("vendor_version") if type(raw.get("vendor_version")) is int else None,
            input_fingerprint=_text(raw.get("input_fingerprint")),
        )

    if trusted_id is not None:
        return _resolve_stored(
            trusted_id,
            seeds,
            birth,
            source_policy=source_policy,
            env=rails_env,
            local_lookup=local_lookup,
            acquisition=acquisition,
            birth_only=False,
        )

    if birth_complete:
        seed = str(_derived_birth_uid(raw))
        canonical_id = canonical_uuid(resolve_db_user_id(seed))
        if canonical_id is None:
            raise CompatBoundaryError("identity_invalid", detail="birth_seed")
        return _resolve_stored(
            canonical_id,
            {seed},
            birth,
            source_policy=source_policy,
            env=rails_env,
            local_lookup=local_lookup,
            acquisition=acquisition,
            birth_only=True,
        )

    raise CompatBoundaryError("legacy_input", detail="no_identity_no_chart")
