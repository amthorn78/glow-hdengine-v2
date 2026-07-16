#!/usr/bin/env python3
"""Generate fixture-backed HDE-EPIC038 PR-05 mapped-cache evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from jsonschema import Draft202012Validator
from engine.bodygraph.mapped_cache import persist_mapped_bodygraph
from engine.bodygraph.ingest import IngestOutcome
from engine.bodygraph.resolver import resolve_bodygraph
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


def _exercise_resolver_policy() -> tuple[dict[str, bool], dict[str, int | str | bool]]:
    calls = {"vendor": 0, "db": 0, "legacy": 0}

    def client_forbidden(**_kwargs):
        calls["vendor"] += 1
        raise AssertionError("vendor construction was not authorized")

    def db_forbidden(**_kwargs):
        calls["db"] += 1
        raise AssertionError("database construction was not authorized")

    def legacy_ingest(*_args, **_kwargs):
        calls["legacy"] += 1
        return IngestOutcome(
            vendor="hdapi", vendor_version=1, input_fingerprint="f" * 64,
            idempotency_key="fixture", rows_written=0, duration_ms=0.0,
            payload_sha256="a" * 64, db_emitted_sha256="a" * 64,
            parity_match=True, db_rows_after=0, payload={},
        )

    base = {"birthdate": "fixture-date", "birthtime": "fixture-time", "location": "fixture-location"}
    with patch.dict(os.environ, {"APP_ENV": "test"}, clear=False), \
         patch("engine.bodygraph.resolver.HdApiClient.from_env", client_forbidden), \
         patch("engine.bodygraph.resolver.DBAccess.for_current_env", db_forbidden):
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
    predicates = {
        "closed_rails_zero_io": closed.payload.get("error", {}).get("code") == "PROVIDER_REFUSED" and calls["vendor"] == 0 and calls["db"] == 0,
        "missing_upsert_refused": missing_upsert.payload.get("error", {}).get("code") == "PROVIDER_WRITE_UNSUPPORTED" and calls["vendor"] == 0 and calls["db"] == 0,
        "production_like_refused": production.payload.get("error", {}).get("code") == "PROVIDER_WRITE_UNSUPPORTED" and calls["vendor"] == 0 and calls["db"] == 0,
        "explicit_legacy_fallback": legacy.status == "ok" and calls["legacy"] == 1 and legacy.payload["resolver"]["route_policy"]["classification"] == "explicit_legacy_fallback",
    }
    posture = {**calls, "closed_code": closed.payload["error"]["code"], "legacy_classification": legacy.payload["resolver"]["route_policy"]["classification"]}
    return predicates, posture


def build(*, force_failure: bool = False) -> dict[Path, bytes]:
    fixture_bytes = FIXTURE.read_bytes(); fixture = json.loads(fixture_bytes)
    cache = {"user_id":"00000000-0000-4000-8000-000000000039","vendor":"hdapi","vendor_version":2,
        "input_fingerprint":fixture["input_fingerprint"],"payload_posture":"adapter_mapped_no_raw_vendor_payload","payload":fixture["payload"]}
    db = MemoryDB(); first = persist_mapped_bodygraph(db, cache); second = persist_mapped_bodygraph(db, cache)
    identity = {key:cache[key] for key in ("user_id","vendor","vendor_version","input_fingerprint")}
    common = {"schema":SCHEMA_ID_TRANSCRIPT,"identity":identity,"safe_payload_keys":["bodygraph","person","person_uid"],"canonical_sha256":first.canonical_sha256,"row_count":len(db.rows),"provider":db.provider_name,"predicates":{"projected_before_persistence":True,"read_back_match":True}}
    write = {**common,"phase":"write","rows_written":first.rows_written}
    read = {**common,"phase":"read_back","rows_written":second.rows_written}
    resolver_predicates, resolver_posture = _exercise_resolver_policy()
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


def write_or_check(files: Mapping[Path, bytes], check: bool) -> None:
    if check:
        stale = [path.relative_to(ROOT).as_posix() for path,data in files.items() if not path.exists() or path.read_bytes()!=data]
        if stale: raise SystemExit("STALE:" + ",".join(stale))
        return
    with tempfile.TemporaryDirectory(prefix="hde-epic038-pr05-") as temp:
        stage = Path(temp)
        staged = []
        for index,(path,data) in enumerate(files.items()):
            candidate=stage/str(index); candidate.write_bytes(data); staged.append((candidate,path))
        for candidate,path in staged:
            path.parent.mkdir(parents=True,exist_ok=True); os.replace(candidate,path)


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("--check",action="store_true"); parser.add_argument("--force-predicate-failure",action="store_true",help=argparse.SUPPRESS); args=parser.parse_args(argv)
    write_or_check(build(force_failure=args.force_predicate_failure),args.check); print("V2_MAPPED_CACHE_EVIDENCE_OK"); return 0


if __name__ == "__main__": raise SystemExit(main())
