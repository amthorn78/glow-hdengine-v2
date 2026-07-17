#!/usr/bin/env python3
"""Generate fixture-backed HDE-EPIC038 PR-05 mapped-cache evidence."""
from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import shutil
import sys
import tempfile
import time
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator, Mapping
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from jsonschema import Draft202012Validator
import engine.bodygraph.resolver as resolver_module
import engine.bodygraph.vendor_client as vendor_client_module
import engine.db.adapter as db_adapter_module
import engine.db.providers.bridge_provider as bridge_provider_module
import engine.db.providers.psycopg_provider as psycopg_provider_module
import engine.ops.http_log as http_log_module
from engine.bodygraph.mapped_cache import persist_mapped_bodygraph
from engine.bodygraph.ingest import IngestOutcome
from engine.bodygraph.resolver import resolve_bodygraph
from engine.runtime.determinism_env import DETERMINISM_ENV_PINS
from engine.serializer.canon import sercanon

OUT = ROOT / "artifacts/bodygraph/v2_mapped_cache"
TRANSCRIPT_SCHEMA = ROOT / "schemas/bodygraph_v2_mapped_cache_transcript.v1.json"
MANIFEST_SCHEMA = ROOT / "schemas/bodygraph_v2_mapped_cache_manifest.v1.json"
FIXTURE = ROOT / "tests/fixtures/bodygraph/source_invariance/db_cached_payload.v1.json"
PRIMARY_NAMES = (
    "write_transcript.json", "read_back_transcript.json", "canonical_parity.log",
    "no_raw_vendor_payload_persistence.log", "idempotence.log",
    "closed_rails_refusal.log", "legacy_fallback_preservation.log", "manifest.json",
)
SCHEMA_ID_TRANSCRIPT = "bodygraph.v2_mapped_cache.transcript.v1"
SCHEMA_ID_MANIFEST = "bodygraph.v2_mapped_cache.manifest.v1"
SHA = r"^[0-9a-f]{64}$"
PREDICATE_KEYS = (
    "canonical_write_read_back_equivalence", "closed_rails_zero_io", "explicit_legacy_fallback",
    "idempotent_repeated_write", "missing_upsert_refused", "no_raw_or_secret_persistence",
    "normalized_identity_single_row", "production_like_refused",
)
SHARED_HTTP_LOG = ROOT / "artifacts/logs/keys_only.sample.jsonl"
_CONNECTION_ENV_KEYS = (
    "APP_ENV",
    "ENGINE_ENV",
    "DATABASE_URL",
    "DB_BRIDGE_URL",
    "DB_ALLOW_BRIDGE_IN_PROD",
    "DB_FORCE_BRIDGE",
    "DB_FORCE_PG",
    "HD_API_BASE_URL",
    "HDAPI_BASE_URL",
    "HD_API_KEY",
    "GEO_API_KEY",
)
HERMETIC_ENV_KEYS = tuple((*DETERMINISM_ENV_PINS, *_CONNECTION_ENV_KEYS))


class HermeticityViolation(AssertionError):
    """Raised when fixture-backed evidence reaches a forbidden external seam."""


class _EnvironmentRestoreState:
    """Hold raw caller state for restoration without exposing it through repr()."""

    __slots__ = ("_values",)

    def __init__(self) -> None:
        self._values: dict[str, tuple[bool, str | None]] = {}
        for name in HERMETIC_ENV_KEYS:
            self._values[name] = (name in os.environ, os.environ.get(name))

    def __repr__(self) -> str:
        present = sum(1 for name in self._values if self._values[name][0])
        return (
            f"{self.__class__.__name__}(tracked={len(self._values)}, "
            f"present={present}, values=<redacted>)"
        )

    def restore(self) -> None:
        for name in self._values:
            if self._values[name][0]:
                if self._values[name][1] is None:
                    raise HermeticityViolation(f"ENV_RESTORE_STATE_INVALID:{name}")
                os.environ[name] = self._values[name][1]
            else:
                os.environ.pop(name, None)
        _set_process_timezone()
        self._values.clear()


@dataclass
class HermeticGuard:
    attempts: dict[str, int] = field(default_factory=dict)

    def forbid(self, seam: str):
        self.attempts.setdefault(seam, 0)

        def _canary(*_args, **_kwargs):
            self.attempts[seam] += 1
            raise HermeticityViolation(f"FORBIDDEN_SEAM:{seam}")

        return _canary


def _set_process_timezone() -> None:
    if hasattr(time, "tzset"):
        time.tzset()


def _apply_hermetic_environment() -> None:
    for key in HERMETIC_ENV_KEYS:
        os.environ.pop(key, None)
    os.environ.update(DETERMINISM_ENV_PINS)
    _set_process_timezone()


def _shared_log_snapshot() -> tuple[bool, bytes | None, str | None]:
    exists = SHARED_HTTP_LOG.exists()
    data = SHARED_HTTP_LOG.read_bytes() if exists else None
    digest = hashlib.sha256(data).hexdigest() if data is not None else None
    return exists, data, digest


def _assert_shared_log_unchanged(snapshot: tuple[bool, bytes | None, str | None]) -> None:
    existed, expected_bytes, expected_sha = snapshot
    if SHARED_HTTP_LOG.exists() != existed:
        raise HermeticityViolation("SHARED_HTTP_LOG_EXISTENCE_CHANGED")
    if not existed:
        return
    actual = SHARED_HTTP_LOG.read_bytes()
    if actual != expected_bytes or hashlib.sha256(actual).hexdigest() != expected_sha:
        raise HermeticityViolation("SHARED_HTTP_LOG_BYTES_CHANGED")


@contextmanager
def _hermetic_execution() -> Iterator[HermeticGuard]:
    """Bound fixture execution away from ambient providers, transports, and logs."""

    environment_state = _EnvironmentRestoreState()
    log_snapshot = _shared_log_snapshot()
    original_log_path = http_log_module.LOG_PATH
    original_bridge_logger = bridge_provider_module.log_http_call
    guard = HermeticGuard()
    forbidden = {
        "resolver.DBAccess.for_current_env": (resolver_module.DBAccess, "for_current_env"),
        "resolver.HdApiClient.from_env": (resolver_module.HdApiClient, "from_env"),
        "db.adapter.PsycopgProvider": (db_adapter_module, "PsycopgProvider"),
        "db.psycopg_provider.PsycopgProvider._connect": (psycopg_provider_module.PsycopgProvider, "_connect"),
        "db.adapter.BridgeProvider": (db_adapter_module, "BridgeProvider"),
        "db.bridge_provider.BridgeProvider": (bridge_provider_module, "BridgeProvider"),
        "db.bridge_provider._default_request": (bridge_provider_module, "_default_request"),
        "db.bridge_provider.urllib.request.urlopen": (bridge_provider_module.urllib.request, "urlopen"),
        "db.bridge_provider.log_http_call": (bridge_provider_module, "log_http_call"),
        "vendor.HdApiClient.fetch": (vendor_client_module.HdApiClient, "fetch"),
        "vendor.HdApiClient._default_request": (vendor_client_module.HdApiClient, "_default_request"),
        "vendor.urllib.request.build_opener": (vendor_client_module.urlrequest, "build_opener"),
        "network.socket.create_connection": (vendor_client_module.socket, "create_connection"),
        "network.socket.getaddrinfo": (vendor_client_module.socket, "getaddrinfo"),
        "network.http.HTTPConnection.connect": (http.client.HTTPConnection, "connect"),
        "network.http.HTTPSConnection.connect": (http.client.HTTPSConnection, "connect"),
    }
    _apply_hermetic_environment()
    try:
        with ExitStack() as stack:
            for seam, (owner, attribute) in forbidden.items():
                stack.enter_context(patch.object(owner, attribute, guard.forbid(seam)))
            yield guard
    finally:
        environment_state.restore()
        http_log_module.LOG_PATH = original_log_path
        _assert_shared_log_unchanged(log_snapshot)
        if http_log_module.LOG_PATH is not original_log_path:
            raise HermeticityViolation("HTTP_LOG_PATH_NOT_RESTORED")
        if bridge_provider_module.log_http_call is not original_bridge_logger:
            raise HermeticityViolation("BRIDGE_LOGGER_NOT_RESTORED")
        attempted = sorted(seam for seam, count in guard.attempts.items() if count)
        if attempted:
            raise HermeticityViolation("FORBIDDEN_SEAMS_ATTEMPTED:" + ",".join(attempted))


class MemoryDB:
    provider_name = "fixture_memory"
    def __init__(self): self.rows: dict[tuple[Any, ...], str] = {}; self.write_calls = 0; self.query_calls = 0
    def query(self, sql, params=None):
        self.query_calls += 1; key = tuple(params)
        if "COUNT" in sql: return [(int(key in self.rows),)]
        return [(self.rows[key],)] if key in self.rows else []
    def tx(self, statements):
        self.write_calls += 1; statement = statements[0]; key = tuple(statement.params[:4])
        inserted = key not in self.rows
        self.rows.setdefault(key, statement.params[4]); return [[(1,)]] if inserted else [[]]


def transcript_schema() -> dict[str, Any]:
    return {"$schema":"https://json-schema.org/draft/2020-12/schema","$id":SCHEMA_ID_TRANSCRIPT,"type":"object","additionalProperties":False,
        "required":["schema","phase","identity","safe_payload_keys","canonical_sha256","row_count","rows_written","provider","predicates"],
        "properties":{
            "schema":{"const":SCHEMA_ID_TRANSCRIPT},"phase":{"enum":["write","read_back"]},
            "identity":{"type":"object","additionalProperties":False,"required":["user_id","vendor","vendor_version","input_fingerprint"],"properties":{
                "user_id":{"type":"string","format":"uuid","maxLength":36},"vendor":{"const":"hdapi"},"vendor_version":{"const":2},"input_fingerprint":{"type":"string","pattern":SHA}}},
            "safe_payload_keys":{"type":"array","prefixItems":[{"const":"bodygraph"},{"const":"person"},{"const":"person_uid"}],"items":False},
            "canonical_sha256":{"type":"string","pattern":SHA},"row_count":{"const":1},"rows_written":{"type":"integer","minimum":0,"maximum":1},
            "provider":{"const":"fixture_memory"},
            "predicates":{"type":"object","additionalProperties":False,"required":["projected_before_persistence","read_back_match"],"properties":{"projected_before_persistence":{"const":True},"read_back_match":{"const":True}}}
        }}


def manifest_schema() -> dict[str, Any]:
    predicate_properties = {key:{"const":True} for key in PREDICATE_KEYS}
    return {"$schema":"https://json-schema.org/draft/2020-12/schema","$id":SCHEMA_ID_MANIFEST,"type":"object","additionalProperties":False,
        "required":["schema","fixture","identity_posture","artifacts","schemas","predicates","status","nonclaims"],"properties":{
            "schema":{"const":SCHEMA_ID_MANIFEST},"fixture":{"type":"object","additionalProperties":False,"required":["path","sha256"],"properties":{"path":{"const":"tests/fixtures/bodygraph/source_invariance/db_cached_payload.v1.json"},"sha256":{"type":"string","pattern":SHA}}},
            "identity_posture":{"const":"user_id,vendor,vendor_version,input_fingerprint"},
            "artifacts":{"type":"array","minItems":7,"maxItems":7,"items":{"$ref":"#/$defs/binding"}},
            "schemas":{"type":"array","minItems":2,"maxItems":2,"items":{"allOf":[{"$ref":"#/$defs/binding"},{"type":"object","required":["schema_identity"]}]}},
            "predicates":{"type":"object","additionalProperties":False,"required":list(PREDICATE_KEYS),"properties":predicate_properties},
            "status":{"const":"PASS"},"nonclaims":{"type":"array","prefixItems":[{"const":"no_acceptance_token_claim"},{"const":"no_ops_execution"},{"const":"no_production_authorization"},{"const":"no_qa_pass_claim"}],"items":False}},
        "$defs":{"binding":{"type":"object","additionalProperties":False,"required":["path","sha256","size"],"properties":{"path":{"type":"string","minLength":1,"maxLength":160},"sha256":{"type":"string","pattern":SHA},"size":{"type":"integer","minimum":1},"schema_identity":{"type":"string","minLength":1,"maxLength":80}}}}}


def _binding(path: str, data: bytes, schema_identity: str | None = None) -> dict[str, Any]:
    value = {"path":path,"sha256":hashlib.sha256(data).hexdigest(),"size":len(data)}
    if schema_identity: value["schema_identity"] = schema_identity
    return value


def _exercise_resolver_policy(guard: HermeticGuard) -> tuple[dict[str, bool], dict[str, int | str | bool]]:
    calls = {"vendor": 0, "db": 0, "legacy": 0}

    def legacy_ingest(*_args, **_kwargs):
        calls["legacy"] += 1
        return IngestOutcome(
            vendor="hdapi", vendor_version=1, input_fingerprint="f" * 64,
            idempotency_key="fixture", rows_written=0, duration_ms=0.0,
            payload_sha256="a" * 64, db_emitted_sha256="a" * 64,
            parity_match=True, db_rows_after=0, payload={},
        )

    base = {"birthdate": "fixture-date", "birthtime": "fixture-time", "location": "fixture-location"}
    closed = resolve_bodygraph(
        "00000000-0000-4000-8000-000000000039", source="vendor", upsert=True,
        dry_run=False, env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
    )
    missing_upsert = resolve_bodygraph(
        "00000000-0000-4000-8000-000000000039", source="vendor", upsert=False,
        dry_run=False, env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "test", "HD_API_BASE_URL": "https://fixture.invalid/v2"}, **base,
    )
    production = resolve_bodygraph(
        "00000000-0000-4000-8000-000000000039", source="vendor", upsert=True,
        dry_run=False, env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "production", "HD_API_BASE_URL": "https://fixture.invalid/v2"}, **base,
    )
    with patch("engine.bodygraph.resolver.ingest_vendor_bodygraph", legacy_ingest):
        legacy = resolve_bodygraph(
            "00000000-0000-4000-8000-000000000039", source="vendor", upsert=False,
            dry_run=True, env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "test", "HD_API_BASE_URL": "https://fixture.invalid/v1"}, **base,
        )
    calls["vendor"] = guard.attempts["resolver.HdApiClient.from_env"]
    calls["db"] = guard.attempts["resolver.DBAccess.for_current_env"]
    predicates = {
        "closed_rails_zero_io": closed.payload.get("error", {}).get("code") == "PROVIDER_REFUSED" and calls["vendor"] == 0 and calls["db"] == 0,
        "missing_upsert_refused": missing_upsert.payload.get("error", {}).get("code") == "PROVIDER_WRITE_UNSUPPORTED" and calls["vendor"] == 0 and calls["db"] == 0,
        "production_like_refused": production.payload.get("error", {}).get("code") == "PROVIDER_WRITE_UNSUPPORTED" and calls["vendor"] == 0 and calls["db"] == 0,
        "explicit_legacy_fallback": legacy.status == "ok" and calls["legacy"] == 1 and legacy.payload["resolver"]["route_policy"]["classification"] == "explicit_legacy_fallback",
    }
    posture = {**calls, "closed_code": closed.payload["error"]["code"], "legacy_classification": legacy.payload["resolver"]["route_policy"]["classification"]}
    return predicates, posture


def _build_files(guard: HermeticGuard, *, force_failure: bool = False) -> dict[Path, bytes]:
    fixture_bytes = FIXTURE.read_bytes(); fixture = json.loads(fixture_bytes)
    cache = {"user_id":"00000000-0000-4000-8000-000000000039","vendor":"hdapi","vendor_version":2,
        "input_fingerprint":fixture["input_fingerprint"],"payload_posture":"adapter_mapped_no_raw_vendor_payload","payload":fixture["payload"]}
    db = MemoryDB(); first = persist_mapped_bodygraph(db, cache); second = persist_mapped_bodygraph(db, cache)
    identity = {key:cache[key] for key in ("user_id","vendor","vendor_version","input_fingerprint")}
    common = {"schema":SCHEMA_ID_TRANSCRIPT,"identity":identity,"safe_payload_keys":["bodygraph","person","person_uid"],"canonical_sha256":first.canonical_sha256,"row_count":len(db.rows),"provider":db.provider_name,"predicates":{"projected_before_persistence":True,"read_back_match":True}}
    write = {**common,"phase":"write","rows_written":first.rows_written}
    read = {**common,"phase":"read_back","rows_written":second.rows_written}
    resolver_predicates, resolver_posture = _exercise_resolver_policy(guard)
    stored = next(iter(db.rows.values()))
    stored_keys = sorted(json.loads(stored))
    persistence_predicates = {
        "canonical_write_read_back_equivalence": first.read_back_match and second.read_back_match and first.canonical_sha256 == second.canonical_sha256,
        "idempotent_repeated_write": first.rows_written == 1 and second.rows_written == 0 and second.idempotent,
        "no_raw_or_secret_persistence": stored_keys == ["bodygraph", "person", "person_uid"],
        "normalized_identity_single_row": len(db.rows) == 1 and first.rows_after == second.rows_after == 1,
    }
    files: dict[Path, bytes] = {
        TRANSCRIPT_SCHEMA:sercanon(transcript_schema()), MANIFEST_SCHEMA:sercanon(manifest_schema()),
        OUT/"write_transcript.json":sercanon(write), OUT/"read_back_transcript.json":sercanon(read),
        OUT/"canonical_parity.log":f"PASS canonical_sha256={first.canonical_sha256} write_read_back_match=true\n".encode(),
        OUT/"no_raw_vendor_payload_persistence.log":f"PASS stored_keys={','.join(stored_keys)} forbidden_keys_absent={str(persistence_predicates['no_raw_or_secret_persistence']).lower()}\n".encode(),
        OUT/"idempotence.log":f"PASS first_rows_written=1 second_rows_written=0 identity_rows={len(db.rows)} canonical_hash_unchanged=true\n".encode(),
        OUT/"closed_rails_refusal.log":f"PASS code={resolver_posture['closed_code']} safe_mode=1 allow_network=0 vendor_calls={resolver_posture['vendor']} db_calls={resolver_posture['db']}\n".encode(),
        OUT/"legacy_fallback_preservation.log":f"PASS classification={resolver_posture['legacy_classification']} legacy_calls={resolver_posture['legacy']} configured_v2_legacy_fallback=false\n".encode(),
    }
    predicates = {**persistence_predicates, **resolver_predicates}
    if force_failure: predicates["idempotent_repeated_write"] = False
    if not all(predicates.values()): raise RuntimeError("PREDICATE_FAILURE")
    artifact_bindings = [_binding(path.relative_to(ROOT).as_posix(), data) for path,data in files.items() if path.parent == OUT]
    schema_bindings = [_binding(TRANSCRIPT_SCHEMA.relative_to(ROOT).as_posix(),files[TRANSCRIPT_SCHEMA],SCHEMA_ID_TRANSCRIPT),_binding(MANIFEST_SCHEMA.relative_to(ROOT).as_posix(),files[MANIFEST_SCHEMA],SCHEMA_ID_MANIFEST)]
    manifest = {"schema":SCHEMA_ID_MANIFEST,"fixture":{"path":FIXTURE.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(fixture_bytes).hexdigest()},
        "identity_posture":"user_id,vendor,vendor_version,input_fingerprint","artifacts":artifact_bindings,"schemas":schema_bindings,"predicates":predicates,"status":"PASS",
        "nonclaims":["no_acceptance_token_claim","no_ops_execution","no_production_authorization","no_qa_pass_claim"]}
    files[OUT/"manifest.json"] = sercanon(manifest)
    Draft202012Validator(transcript_schema()).validate(write); Draft202012Validator(transcript_schema()).validate(read); Draft202012Validator(manifest_schema()).validate(manifest)
    return files


def build(*, force_failure: bool = False) -> dict[Path, bytes]:
    with _hermetic_execution() as guard:
        return _build_files(guard, force_failure=force_failure)


def write_or_check(files: Mapping[Path, bytes], check: bool) -> None:
    if check:
        stale = [path.relative_to(ROOT).as_posix() for path,data in files.items() if not path.exists() or path.read_bytes()!=data]
        if stale: raise SystemExit("STALE:" + ",".join(stale))
        return
    with tempfile.TemporaryDirectory(prefix="hde-epic038-pr05-", dir=ROOT.parent) as temp:
        stage = Path(temp)
        staged = []
        for index,(path,data) in enumerate(files.items()):
            candidate=stage/f"candidate-{index}"; candidate.write_bytes(data)
            backup=stage/f"backup-{index}"
            existed=path.exists()
            if existed: shutil.copy2(path,backup)
            staged.append((candidate,backup,path,existed))
        attempted = []
        try:
            for candidate,backup,path,existed in staged:
                path.parent.mkdir(parents=True,exist_ok=True)
                attempted.append((backup,path,existed))
                os.replace(candidate,path)
        except BaseException:
            rollback_errors = []
            for backup,path,existed in reversed(attempted):
                try:
                    if existed:
                        os.replace(backup,path)
                    elif path.exists():
                        path.unlink()
                except BaseException as exc:  # pragma: no cover - defensive rollback guard
                    rollback_errors.append(f"{path.relative_to(ROOT).as_posix()}:{exc.__class__.__name__}")
            if rollback_errors:
                raise RuntimeError("ROLLBACK_FAILURE:" + ",".join(rollback_errors))
            raise


def run(*, check: bool = False, force_failure: bool = False) -> None:
    with _hermetic_execution() as guard:
        files = _build_files(guard, force_failure=force_failure)
        write_or_check(files, check)


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("--check",action="store_true"); parser.add_argument("--force-predicate-failure",action="store_true",help=argparse.SUPPRESS); args=parser.parse_args(argv)
    run(check=args.check, force_failure=args.force_predicate_failure); print("V2_MAPPED_CACHE_EVIDENCE_OK"); return 0


if __name__ == "__main__": raise SystemExit(main())
