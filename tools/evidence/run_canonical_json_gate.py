#!/usr/bin/env python3
"""Run the canonical JSON gate and emit governed artifacts."""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Iterator, Mapping, Sequence

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.evidence import update_evidence_index
from tools.evidence.generate_narrative_registry_diff import (
    validate_registry_snapshot as validate_narrative_registry_snapshot,
)
from adapter.http_reader import create_app
from engine.cli.main import (
    _candidate_from_payload,
    _canonical_pair,
    _conjunction_party_from_payload,
    _derive_uid,
    _load_viewer_prefs,
    _normalize_party,
    _party_from_normalized,
)
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import band_for, compat_public, conjunction_public
from engine.config.registry_loader import load_registry_config
from engine.mech.helpers import canonicalize_declared_set
from engine.narratives.constants import BANDS
from engine.narratives.loader import load_pack
from engine.sampler.core import ViewerProfile, sample_and_rank
from scripts.cut_release_manifest import cut_manifest
from scripts.hd_cli import (
    ADMIN_SELECTION_TRACE,
    DEFAULT_RELEASE_ID,
    _public_envelope_for_release,
)
from tools.cli.generate_cli_conformance_artifacts import (
    CONJUNCTION_AB,
    CONJUNCTION_BA,
    SAMPLER_CANDIDATES,
)
from tools.cli.generate_showcompat_artifacts import PAIR as SHOWCOMPAT_PAIR

CANON_DIR = ROOT / "audit" / "gates" / "canonical_json"
JSON_GATE_DIR = ROOT / "audit" / "gates" / "json_gate" / "canonical"
# Capture-time provenance belongs to this governed gate family.  It must not
# follow catalog/manifest.json's release cut timestamp: AGENTS.md requires an
# intentional release cut to change only that manifest.
GATE_CAPTURED_AT_UTC = "2025-12-26T00:00:00Z"

# These governed CLI captures retain their capture-time identity.  Current
# release-bound identity is produced externally; historical source-tree evidence
# remains immutable.
_CAPTURE_SERVICE_IDENTITY = json.loads(
    (ROOT / "artifacts" / "identity" / "service_identity.json").read_bytes()
)
_CAPTURE_IDENTITY_META = {
    field: _CAPTURE_SERVICE_IDENTITY[field]
    for field in ("engine_tag", "invocation_tag", "release_id")
}


@dataclass(frozen=True)
class Target:
    name: str
    rel_path: str
    validator: str
    schema: str | None = None
    set_rules: tuple[tuple[str, str], ...] = ()


_GENERATED = (
    Target(
        "cli_showcompat_stdout",
        "artifacts/cli/showcompat/stdout.json",
        "canonical_json.generated.showcompat_capture.v1",
    ),
    Target(
        "cli_showcompat_args",
        "artifacts/cli/showcompat/args.json",
        "canonical_json.generated.showcompat_args.v1",
    ),
    Target(
        "cli_reader_dump",
        "artifacts/cli/reader_dump.json",
        "canonical_json.generated.reader_envelope.v1",
    ),
    Target(
        "cli_summary",
        "artifacts/cli/summary.json",
        "canonical_json.generated.cli_conformance_summary.v1",
    ),
    Target(
        "cli_ab_stdout",
        "artifacts/cli/ab.json",
        "canonical_json.generated.conjunction_envelope.v1",
    ),
    Target(
        "cli_ba_stdout",
        "artifacts/cli/ba.json",
        "canonical_json.generated.conjunction_envelope.v1",
    ),
    Target(
        "cli_conjunction_output_ab",
        "artifacts/cli/out.json",
        "canonical_json.generated.reader_envelope.v1",
    ),
    Target(
        "cli_conjunction_output_ba",
        "artifacts/cli/out_ba.json",
        "canonical_json.generated.reader_envelope.v1",
    ),
    Target(
        "cli_conjunction_selection_trace",
        "artifacts/cli/abba_sidecar.json",
        "canonical_json.generated.selection_trace.v1",
    ),
    Target(
        "cli_conjunction_pair_ab",
        "artifacts/audit/cli/pair.json",
        "canonical_json.generated.pair_input.v1",
    ),
    Target(
        "cli_conjunction_pair_ba",
        "artifacts/audit/cli/pair_ba.json",
        "canonical_json.generated.pair_input.v1",
    ),
    Target(
        "cli_conjunction_showcompat_ab",
        "artifacts/audit/cli/showcompat_ab.json",
        "canonical_json.generated.reader_envelope.v1",
    ),
    Target(
        "cli_conjunction_showcompat_ba",
        "artifacts/audit/cli/showcompat_ba.json",
        "canonical_json.generated.reader_envelope.v1",
    ),
)
TARGETS: Sequence[Target] = _GENERATED + (
    Target(
        "catalog_manifest",
        "catalog/manifest.json",
        "scripts.cut_release_manifest.cut_manifest(check=True)",
        set_rules=(("$.files", "path"),),
    ),
    Target(
        "catalog_channels",
        "catalog/channels_v1.json",
        "engine.config.registry_loader.load_registry_config",
        "schemas/channels_v1.schema.json",
        (
            ("$.channels", "id"),
            ("$.channels[*].centers", "value"),
            ("$.channels[*].domains", "value"),
            ("$.channels[*].flags", "value"),
            ("$.channels[*].gates", "value"),
        ),
    ),
    Target(
        "catalog_gates",
        "catalog/gates_v1.json",
        "engine.config.registry_loader.load_registry_config",
        "schemas/gates_v1.schema.json",
    ),
    Target("catalog_magic10", "catalog/magic10.json", "engine.config.registry_loader.load_registry_config"),
    Target("catalog_magic10_caps", "catalog/magic10_caps.json", "engine.config.registry_loader.load_registry_config"),
    Target("catalog_magic10_seeds", "catalog/magic10_seeds.json", "engine.config.registry_loader.load_registry_config"),
    Target(
        "catalog_narratives_keys",
        "catalog/narratives/keys.json",
        "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot",
    ),
    *(
        Target(
            f"catalog_narratives_{name}",
            f"catalog/narratives/{name}.json",
            "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot",
        )
        for name in ("manifest", "palettes", "suppression_map", "templates")
    ),
    Target("schema_gates", "schemas/gates_v1.schema.json", "jsonschema.Draft202012Validator.check_schema"),
    Target("schema_channels", "schemas/channels_v1.schema.json", "jsonschema.Draft202012Validator.check_schema"),
)

EXPECTED_TARGET_PATHS = (
    "artifacts/audit/cli/pair.json",
    "artifacts/audit/cli/pair_ba.json",
    "artifacts/audit/cli/showcompat_ab.json",
    "artifacts/audit/cli/showcompat_ba.json",
    "artifacts/cli/ab.json",
    "artifacts/cli/abba_sidecar.json",
    "artifacts/cli/ba.json",
    "artifacts/cli/out.json",
    "artifacts/cli/out_ba.json",
    "artifacts/cli/reader_dump.json",
    "artifacts/cli/showcompat/args.json",
    "artifacts/cli/showcompat/stdout.json",
    "artifacts/cli/summary.json",
    "catalog/channels_v1.json",
    "catalog/gates_v1.json",
    "catalog/magic10.json",
    "catalog/magic10_caps.json",
    "catalog/magic10_seeds.json",
    "catalog/manifest.json",
    "catalog/narratives/keys.json",
    "catalog/narratives/manifest.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
    "schemas/channels_v1.schema.json",
    "schemas/gates_v1.schema.json",
)

EXPECTED_TARGET_BINDINGS = (
    ("artifacts/audit/cli/pair.json", "canonical_json.generated.pair_input.v1", None),
    ("artifacts/audit/cli/pair_ba.json", "canonical_json.generated.pair_input.v1", None),
    ("artifacts/audit/cli/showcompat_ab.json", "canonical_json.generated.reader_envelope.v1", None),
    ("artifacts/audit/cli/showcompat_ba.json", "canonical_json.generated.reader_envelope.v1", None),
    ("artifacts/cli/ab.json", "canonical_json.generated.conjunction_envelope.v1", None),
    ("artifacts/cli/abba_sidecar.json", "canonical_json.generated.selection_trace.v1", None),
    ("artifacts/cli/ba.json", "canonical_json.generated.conjunction_envelope.v1", None),
    ("artifacts/cli/out.json", "canonical_json.generated.reader_envelope.v1", None),
    ("artifacts/cli/out_ba.json", "canonical_json.generated.reader_envelope.v1", None),
    ("artifacts/cli/reader_dump.json", "canonical_json.generated.reader_envelope.v1", None),
    ("artifacts/cli/showcompat/args.json", "canonical_json.generated.showcompat_args.v1", None),
    ("artifacts/cli/showcompat/stdout.json", "canonical_json.generated.showcompat_capture.v1", None),
    ("artifacts/cli/summary.json", "canonical_json.generated.cli_conformance_summary.v1", None),
    ("catalog/channels_v1.json", "engine.config.registry_loader.load_registry_config", "schemas/channels_v1.schema.json"),
    ("catalog/gates_v1.json", "engine.config.registry_loader.load_registry_config", "schemas/gates_v1.schema.json"),
    ("catalog/magic10.json", "engine.config.registry_loader.load_registry_config", None),
    ("catalog/magic10_caps.json", "engine.config.registry_loader.load_registry_config", None),
    ("catalog/magic10_seeds.json", "engine.config.registry_loader.load_registry_config", None),
    ("catalog/manifest.json", "scripts.cut_release_manifest.cut_manifest(check=True)", None),
    ("catalog/narratives/keys.json", "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot", None),
    ("catalog/narratives/manifest.json", "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot", None),
    ("catalog/narratives/palettes.json", "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot", None),
    ("catalog/narratives/suppression_map.json", "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot", None),
    ("catalog/narratives/templates.json", "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot", None),
    ("schemas/channels_v1.schema.json", "jsonschema.Draft202012Validator.check_schema", None),
    ("schemas/gates_v1.schema.json", "jsonschema.Draft202012Validator.check_schema", None),
)

EXPECTED_SET_RULES = (
    ("catalog/channels_v1.json", "$.channels", "id"),
    ("catalog/channels_v1.json", "$.channels[*].centers", "value"),
    ("catalog/channels_v1.json", "$.channels[*].domains", "value"),
    ("catalog/channels_v1.json", "$.channels[*].flags", "value"),
    ("catalog/channels_v1.json", "$.channels[*].gates", "value"),
    ("catalog/manifest.json", "$.files", "path"),
)


_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_EXPECTED_SCHEMA_SHA256 = {
    "schemas/channels_v1.schema.json": "a663bf3ffc4d4a7d3da274da359e41c89fea17914f583c963c6f74c0288d8a42",
    "schemas/gates_v1.schema.json": "b3308ca513a1f3e4490ce6c526124675fad1fdcdb5c6abce7257af99d76ed13a",
}
_EXPECTED_RELEASE_MANIFEST_PATHS = (
    "adapter/http_reader.py",
    "catalog/channels_v1.json",
    "catalog/gates_v1.json",
    "catalog/magic10.json",
    "catalog/magic10_caps.json",
    "catalog/magic10_seeds.json",
    "catalog/narratives/keys.json",
    "catalog/narratives/manifest.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
    "engine/presenter/emitter.py",
    "engine/serializer/canon.py",
    "math/thresholds.json",
    "migrations/005_identity.sql",
)
_READER_COUNTERPARTS = {
    "artifacts/cli/out.json": "artifacts/cli/out_ba.json",
    "artifacts/cli/out_ba.json": "artifacts/cli/out.json",
    "artifacts/audit/cli/showcompat_ab.json": "artifacts/audit/cli/showcompat_ba.json",
    "artifacts/audit/cli/showcompat_ba.json": "artifacts/audit/cli/showcompat_ab.json",
}
_READER_BYTE_PARITY = {
    "artifacts/cli/reader_dump.json": "artifacts/cli/reader_cli_parity.bytes",
}
_CONJUNCTION_COUNTERPARTS = {
    "artifacts/cli/ab.json": "artifacts/cli/ba.json",
    "artifacts/cli/ba.json": "artifacts/cli/ab.json",
}
_PAIR_COUNTERPARTS = {
    "artifacts/audit/cli/pair.json": "artifacts/audit/cli/pair_ba.json",
    "artifacts/audit/cli/pair_ba.json": "artifacts/audit/cli/pair.json",
}
_CONJUNCTION_SOURCE_PAIRS = {
    "artifacts/cli/ab.json": CONJUNCTION_AB,
    "artifacts/cli/ba.json": CONJUNCTION_BA,
}
_HD_CLI_READER_PATHS = frozenset(("artifacts/cli/out.json", "artifacts/cli/out_ba.json"))
# These five D1 records are frozen capture-time evidence, byte-identical to the
# approved authoring snapshot.  Their exact digests prevent a coherent rewrite
# of both a capture and its companion from manufacturing new historical facts.
_FROZEN_GENERATED_SHA256 = {
    "artifacts/audit/cli/pair.json": "aba063e58eccc267cdac192782d3e211d2c3bee2ddab82cd8f33072f799e3e4f",
    "artifacts/audit/cli/pair_ba.json": "ad2d8222b8b66a676a0d060da46b16b8c7202d54d648db322d017ce790c70719",
    "artifacts/audit/cli/showcompat_ab.json": "e47d50bb1db574ab3273864b25cc9e106ac5cf606c06d9479f8eca95090ac1a3",
    "artifacts/audit/cli/showcompat_ba.json": "e47d50bb1db574ab3273864b25cc9e106ac5cf606c06d9479f8eca95090ac1a3",
    "artifacts/cli/reader_dump.json": "1c8009b23095fb556225864f04136839ac4433b656465055379235db604fef42",
}


def _require_exact_keys(obj: object, keys: set[str], label: str) -> dict[str, object]:
    if not isinstance(obj, dict):
        raise ValueError(f"{label}_must_be_object")
    if set(obj) != keys:
        raise ValueError(f"{label}_keys_invalid")
    return obj


def _require_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label}_must_be_nonempty_string")
    return value


def _require_hex64(value: object, label: str) -> str:
    text = _require_string(value, label)
    if _HEX64.fullmatch(text) is None:
        raise ValueError(f"{label}_must_be_hex64")
    return text


def _read_bound_json(rel_path: str) -> object:
    return json.loads((ROOT / rel_path).read_bytes())


def _validate_runtime_identity(value: object) -> dict[str, object]:
    meta = _require_exact_keys(
        value, {"engine_tag", "invocation_tag", "release_id"}, "runtime_identity"
    )
    _require_string(meta["engine_tag"], "runtime_identity.engine_tag")
    _require_string(meta["invocation_tag"], "runtime_identity.invocation_tag")
    _require_hex64(meta["release_id"], "runtime_identity.release_id")
    if meta != _CAPTURE_IDENTITY_META:
        raise ValueError("runtime_identity_source_mismatch")
    return meta


def _validate_reader_meta(value: object) -> None:
    meta = _require_exact_keys(value, {"engine_tag", "invocation_tag"}, "reader_meta")
    _require_string(meta["engine_tag"], "reader_meta.engine_tag")
    _require_string(meta["invocation_tag"], "reader_meta.invocation_tag")


def _validate_compat_payload(value: object) -> dict[str, object]:
    compat = _require_exact_keys(value, {"categories", "meta"}, "compat")
    categories = compat["categories"]
    if not isinstance(categories, list) or len(categories) != len(CATEGORIES_ORDER_V1):
        raise ValueError("compat_categories_invalid")
    ids: list[str] = []
    for index, raw in enumerate(categories):
        row = _require_exact_keys(
            raw,
            {"band", "id", "personal_key", "score", "shared_key"},
            f"compat_category_{index}",
        )
        category_id = _require_string(row["id"], f"compat_category_{index}.id")
        band = _require_string(row["band"], f"compat_category_{index}.band")
        if band not in BANDS:
            raise ValueError(f"compat_category_{index}_band_invalid")
        if type(row["score"]) is not int or not 0 <= row["score"] <= 100:
            raise ValueError(f"compat_category_{index}_score_invalid")
        if band != band_for(row["score"]):
            raise ValueError(f"compat_category_{index}_score_band_mismatch")
        if row["personal_key"] != f"{category_id}_{band.lower()}_personal_v1":
            raise ValueError(f"compat_category_{index}_personal_key_invalid")
        if row["shared_key"] != f"{category_id}_{band.lower()}_shared_v1":
            raise ValueError(f"compat_category_{index}_shared_key_invalid")
        ids.append(category_id)
    if ids != list(CATEGORIES_ORDER_V1):
        raise ValueError("compat_category_order_invalid")
    _validate_runtime_identity(compat["meta"])
    return compat


def _validate_birth(value: object, *, include_tz: bool, label: str) -> None:
    keys = {"birthdate", "birthtime", "location"}
    if include_tz:
        keys.add("tz")
    birth = _require_exact_keys(value, keys, label)
    try:
        dt.date.fromisoformat(_require_string(birth["birthdate"], f"{label}.birthdate"))
        dt.time.fromisoformat(_require_string(birth["birthtime"], f"{label}.birthtime"))
    except ValueError as exc:
        raise ValueError(f"{label}_date_or_time_invalid") from exc
    _require_string(birth["location"], f"{label}.location")
    if include_tz:
        _require_string(birth["tz"], f"{label}.tz")


def _expected_showcompat_capture_bytes() -> bytes:
    viewer_prefs = _load_viewer_prefs(None)
    left_normalized = _normalize_party(dict(SHOWCOMPAT_PAIR["left"]), "left")
    right_normalized = _normalize_party(dict(SHOWCOMPAT_PAIR["right"]), "right")
    left_person, left_chart = _party_from_normalized(left_normalized)
    right_person, right_chart = _party_from_normalized(right_normalized)
    left_person, right_person, _left_chart, _right_chart = _canonical_pair(
        left_person, right_person, left_chart, right_chart
    )
    compat = compat_public(
        left_person,
        right_person,
        viewer_prefs["top_category"],
        viewer_prefs["weights"],
        engine_tag=_CAPTURE_IDENTITY_META["engine_tag"],
        release_id=_CAPTURE_IDENTITY_META["release_id"],
        invocation_tag=_CAPTURE_IDENTITY_META["invocation_tag"],
    )
    return sercanon(
        {
            "a": left_person,
            "b": right_person,
            "compat": compat,
            "viewer_prefs": viewer_prefs,
        },
        sort_keys=True,
    )


def _expected_conjunction_capture_bytes(target: Target) -> bytes:
    source = _CONJUNCTION_SOURCE_PAIRS.get(target.rel_path)
    if source is None:
        raise ValueError("conjunction_source_fixture_missing")
    viewer_prefs = _load_viewer_prefs(None)
    left = _conjunction_party_from_payload(dict(source["left"]), "left")
    right = _conjunction_party_from_payload(dict(source["right"]), "right")
    payload = conjunction_public(
        left,
        right,
        viewer_top=viewer_prefs["top_category"],
        viewer_weights=viewer_prefs["weights"],
        engine_tag=_CAPTURE_IDENTITY_META["engine_tag"],
        release_id=_CAPTURE_IDENTITY_META["release_id"],
        invocation_tag=_CAPTURE_IDENTITY_META["invocation_tag"],
    )
    return sercanon(payload, sort_keys=True)


def _validate_frozen_generated_capture(target: Target, obj: object) -> None:
    expected_sha = _FROZEN_GENERATED_SHA256.get(target.rel_path)
    if expected_sha is None:
        return
    if hashlib.sha256(sercanon(obj, sort_keys=True)).hexdigest() != expected_sha:
        raise ValueError("frozen_generated_capture_mismatch")


def _validate_showcompat_capture(_target: Target, obj: object) -> None:
    payload = _require_exact_keys(obj, {"a", "b", "compat", "viewer_prefs"}, "showcompat")
    for side in ("a", "b"):
        party = _require_exact_keys(payload[side], {"birth", "person_uid"}, f"showcompat_{side}")
        _validate_birth(party["birth"], include_tz=False, label=f"showcompat_{side}.birth")
        _require_string(party["person_uid"], f"showcompat_{side}.person_uid")
    _validate_compat_payload(payload["compat"])
    prefs = _require_exact_keys(
        payload["viewer_prefs"], {"top_category", "weights"}, "viewer_prefs"
    )
    if prefs["top_category"] not in CATEGORIES_ORDER_V1:
        raise ValueError("viewer_prefs_top_category_invalid")
    weights = _require_exact_keys(
        prefs["weights"], set(CATEGORIES_ORDER_V1), "viewer_prefs_weights"
    )
    if any(type(value) is not int or not 0 <= value <= 100 for value in weights.values()):
        raise ValueError("viewer_prefs_weight_invalid")
    if sercanon(obj, sort_keys=True) != _expected_showcompat_capture_bytes():
        raise ValueError("showcompat_capture_source_mismatch")


def _validate_showcompat_args(_target: Target, obj: object) -> None:
    payload = _require_exact_keys(
        obj, {"argv", "artifacts", "env", "generator", "identity", "input"}, "showcompat_args"
    )
    if payload["argv"] != ["python", "scripts/hdctl.py", "showcompat"]:
        raise ValueError("showcompat_args_argv_invalid")
    if payload["generator"] != "tools/cli/generate_showcompat_artifacts.py":
        raise ValueError("showcompat_args_generator_invalid")
    artifacts = _require_exact_keys(
        payload["artifacts"], {"stdout", "stdout_sha256"}, "showcompat_args_artifacts"
    )
    if artifacts != {
        "stdout": "artifacts/cli/showcompat/stdout.json",
        "stdout_sha256": "artifacts/cli/showcompat/stdout.json.sha256",
    }:
        raise ValueError("showcompat_args_artifact_paths_invalid")
    env = _require_exact_keys(
        payload["env"], {"ALLOW_NETWORK", "LANG", "LC_ALL", "SAFE_MODE", "TZ"}, "showcompat_args_env"
    )
    if env != {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}:
        raise ValueError("showcompat_args_env_invalid")
    identity = _require_exact_keys(payload["identity"], {"meta", "source"}, "showcompat_args_identity")
    if identity["source"] != "engine.runtime.identity":
        raise ValueError("showcompat_args_identity_source_invalid")
    meta = _validate_runtime_identity(identity["meta"])
    input_record = _require_exact_keys(
        payload["input"], {"source", "stdin_payload", "stdin_sha256", "trailing_lf"}, "showcompat_args_input"
    )
    if input_record["source"] != "stdin" or input_record["trailing_lf"] is not True:
        raise ValueError("showcompat_args_input_posture_invalid")
    stdin_payload = _require_exact_keys(input_record["stdin_payload"], {"left", "right"}, "showcompat_args_stdin")
    _validate_birth(stdin_payload["left"], include_tz=False, label="showcompat_args_stdin.left")
    _validate_birth(stdin_payload["right"], include_tz=False, label="showcompat_args_stdin.right")
    if stdin_payload != SHOWCOMPAT_PAIR:
        raise ValueError("showcompat_args_source_pair_mismatch")
    stdin_bytes = (
        json.dumps(stdin_payload, separators=(",", ":"), sort_keys=True) + "\n"
    ).encode("utf-8")
    if input_record["stdin_sha256"] != hashlib.sha256(stdin_bytes).hexdigest():
        raise ValueError("showcompat_args_stdin_sha256_invalid")
    stdout_path = ROOT / str(artifacts["stdout"])
    stdout_sha = hashlib.sha256(stdout_path.read_bytes()).hexdigest()
    sidecar_sha = (ROOT / str(artifacts["stdout_sha256"])).read_text(encoding="utf-8").strip()
    if stdout_sha != sidecar_sha:
        raise ValueError("showcompat_stdout_sidecar_mismatch")
    stdout = _require_exact_keys(
        _read_bound_json(str(artifacts["stdout"])),
        {"a", "b", "compat", "viewer_prefs"},
        "showcompat_stdout",
    )
    compat = _require_exact_keys(stdout["compat"], {"categories", "meta"}, "showcompat_stdout.compat")
    if meta != compat["meta"]:
        raise ValueError("showcompat_args_identity_mismatch")
    for output_side, input_side in (("a", "left"), ("b", "right")):
        output_party = _require_exact_keys(
            stdout[output_side], {"birth", "person_uid"}, f"showcompat_stdout.{output_side}"
        )
        if output_party["birth"] != stdin_payload[input_side]:
            raise ValueError("showcompat_args_birth_binding_mismatch")
        if output_party["person_uid"] != _derive_uid(dict(stdin_payload[input_side])):
            raise ValueError("showcompat_args_person_uid_binding_mismatch")


def _validate_reader_envelope(target: Target, obj: object) -> None:
    payload = _require_exact_keys(
        obj,
        {"categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"},
        "reader_envelope",
    )
    if payload["reader_version"] != "v1" or not isinstance(payload["eligible"], bool):
        raise ValueError("reader_envelope_header_invalid")
    _require_hex64(payload["release_id"], "reader_envelope.release_id")
    stored_hash = _require_hex64(payload["idempotence_hash"], "reader_envelope.idempotence_hash")
    _validate_reader_meta(payload["meta"])
    categories = payload["categories"]
    if not isinstance(categories, list):
        raise ValueError("reader_categories_must_be_array")
    allowed_ids = set(CATEGORIES_ORDER_V1) | {f"{band.lower()}_leader" for band in BANDS}
    category_ids: list[str] = []
    for index, raw in enumerate(categories):
        if not isinstance(raw, dict) or set(raw) not in ({"band", "id"}, {"band", "id", "prompt"}):
            raise ValueError(f"reader_category_{index}_keys_invalid")
        if raw["band"] not in BANDS or raw["id"] not in allowed_ids:
            raise ValueError(f"reader_category_{index}_identity_invalid")
        if raw["id"].endswith("_leader") and raw["id"] != f"{raw['band'].lower()}_leader":
            raise ValueError(f"reader_category_{index}_leader_band_mismatch")
        if "prompt" in raw and raw["prompt"] is not None and not isinstance(raw["prompt"], str):
            raise ValueError(f"reader_category_{index}_prompt_invalid")
        category_ids.append(raw["id"])
    if len(category_ids) != len(set(category_ids)):
        raise ValueError("reader_category_id_duplicate")
    if category_ids != sorted(category_ids):
        raise ValueError("reader_category_id_order_invalid")
    preimage = {key: value for key, value in payload.items() if key != "idempotence_hash"}
    if hashlib.sha256(sercanon(preimage, sort_keys=True)).hexdigest() != stored_hash:
        raise ValueError("reader_idempotence_hash_mismatch")
    counterpart = _READER_COUNTERPARTS.get(target.rel_path)
    if counterpart and sercanon(obj, sort_keys=True) != sercanon(
        _read_bound_json(counterpart), sort_keys=True
    ):
        raise ValueError("reader_counterpart_mismatch")
    parity_path = _READER_BYTE_PARITY.get(target.rel_path)
    if parity_path and sercanon(obj, sort_keys=True) != (ROOT / parity_path).read_bytes():
        raise ValueError("reader_cli_parity_mismatch")
    if target.rel_path in _HD_CLI_READER_PATHS and sercanon(
        obj, sort_keys=True
    ) != sercanon(_public_envelope_for_release(DEFAULT_RELEASE_ID), sort_keys=True):
        raise ValueError("reader_hd_cli_source_mismatch")


def _validate_conjunction_envelope(target: Target, obj: object) -> None:
    payload = _require_exact_keys(obj, {"conjunction"}, "conjunction_envelope")
    conjunction = _require_exact_keys(
        payload["conjunction"], {"compat", "left", "right"}, "conjunction"
    )
    _validate_compat_payload(conjunction["compat"])
    expected_uids = {
        side: CONJUNCTION_AB[side]["person_uid"] for side in ("left", "right")
    }
    for side in ("left", "right"):
        party = _require_exact_keys(conjunction[side], {"person_uid"}, f"conjunction_{side}")
        if party["person_uid"] != expected_uids[side]:
            raise ValueError(f"conjunction_{side}_person_uid_source_mismatch")
    counterpart = _CONJUNCTION_COUNTERPARTS[target.rel_path]
    if sercanon(obj, sort_keys=True) != sercanon(_read_bound_json(counterpart), sort_keys=True):
        raise ValueError("conjunction_counterpart_mismatch")
    if sercanon(obj, sort_keys=True) != _expected_conjunction_capture_bytes(target):
        raise ValueError("conjunction_source_mismatch")


def _expected_sampler_capture() -> tuple[bytes, list[str]]:
    viewer_id = "viewer-cli-conformance"
    ranked = sample_and_rank(
        ViewerProfile(person_uid=viewer_id),
        [_candidate_from_payload(raw) for raw in SAMPLER_CANDIDATES["candidates"]],
    )
    payload = {
        "viewer_id": viewer_id,
        "seed": "seed-cli-conformance",
        "candidates": [
            {
                "person_uid": candidate.person_uid,
                "score": candidate.score,
                "weight": candidate.weight,
                "band": candidate.band,
                "rank": candidate.rank,
                "diversity_key": candidate.diversity_key,
                "is_recent": candidate.is_recent,
            }
            for candidate in ranked.candidates
        ],
    }
    return sercanon(payload, sort_keys=True), [
        candidate.person_uid for candidate in ranked.candidates
    ]


def _validate_cli_summary(_target: Target, obj: object) -> None:
    payload = _require_exact_keys(
        obj,
        {
            "ab_ba_equal", "ab_sha256", "ba_sha256", "commands", "identity",
            "installability", "pf05_command_catalog", "sampler_semantics",
            "two_run_equal", "two_run_sha256",
        },
        "cli_summary",
    )
    ab_bytes = (ROOT / "artifacts/cli/ab.json").read_bytes()
    ba_bytes = (ROOT / "artifacts/cli/ba.json").read_bytes()
    ab_sha = hashlib.sha256(ab_bytes).hexdigest()
    ba_sha = hashlib.sha256(ba_bytes).hexdigest()
    if payload["ab_sha256"] != ab_sha or payload["ba_sha256"] != ba_sha:
        raise ValueError("cli_summary_pair_sha_mismatch")
    if payload["ab_ba_equal"] is not (ab_bytes == ba_bytes):
        raise ValueError("cli_summary_ab_ba_posture_invalid")
    if payload["two_run_sha256"] != ab_sha or payload["two_run_equal"] is not True:
        raise ValueError("cli_summary_two_run_posture_invalid")
    command = ["python", "-m", "engine.cli", "showcompat", "--conjunction"]
    commands = _require_exact_keys(payload["commands"], {"ab", "ba", "two_run"}, "cli_summary_commands")
    if any(commands[name] != command for name in commands):
        raise ValueError("cli_summary_commands_invalid")
    identity = _require_exact_keys(payload["identity"], {"meta", "source"}, "cli_summary_identity")
    if identity["source"] != "engine.runtime.identity":
        raise ValueError("cli_summary_identity_source_invalid")
    meta = _validate_runtime_identity(identity["meta"])
    ab_payload = _require_exact_keys(json.loads(ab_bytes), {"conjunction"}, "cli_summary_ab")
    ab_conjunction = _require_exact_keys(
        ab_payload["conjunction"], {"compat", "left", "right"}, "cli_summary_ab.conjunction"
    )
    ab_compat = _require_exact_keys(ab_conjunction["compat"], {"categories", "meta"}, "cli_summary_ab.compat")
    if meta != ab_compat["meta"]:
        raise ValueError("cli_summary_identity_mismatch")
    installability = _require_exact_keys(
        payload["installability"],
        {
            "console_entrypoint", "console_help", "console_version", "entrypoint_decl",
            "module_help", "module_showcompat_help", "module_version", "script_help",
        },
        "cli_summary_installability",
    )
    if installability["entrypoint_decl"] != "engine.cli.main:cli":
        raise ValueError("cli_summary_entrypoint_invalid")
    for name in ("console_help", "module_help", "module_showcompat_help", "script_help"):
        record = _require_exact_keys(installability[name], {"cmd", "returncode"}, f"cli_summary_{name}")
        expected_commands = {
            "console_help": ["hdctl", "--help"],
            "module_help": ["python", "-m", "engine.cli", "--help"],
            "module_showcompat_help": [
                "python", "-m", "engine.cli", "showcompat", "--help"
            ],
            "script_help": ["python", "scripts/hdctl.py", "--help"],
        }
        if (
            type(record["returncode"]) is not int
            or record["returncode"] != 0
            or record["cmd"] != expected_commands[name]
        ):
            raise ValueError(f"cli_summary_{name}_invalid")
    for name in ("console_version", "module_version"):
        record = _require_exact_keys(
            installability[name], {"cmd", "returncode", "stderr", "stdout"}, f"cli_summary_{name}"
        )
        expected_commands = {
            "console_version": ["hdctl", "--version"],
            "module_version": ["python", "-m", "engine.cli", "--version"],
        }
        expected_stdout = (
            f"hdctl 0.0.0 ({meta['engine_tag']};{meta['release_id']})\n"
        )
        if (
            type(record["returncode"]) is not int
            or record["returncode"] != 0
            or record["cmd"] != expected_commands[name]
            or record["stderr"] != ""
            or record["stdout"] != expected_stdout
        ):
            raise ValueError(f"cli_summary_{name}_invalid")
    entrypoint = _require_exact_keys(
        installability["console_entrypoint"], {"available", "path"}, "cli_summary_console_entrypoint"
    )
    if entrypoint["available"] is not True or entrypoint["path"] != "hdctl":
        raise ValueError("cli_summary_console_entrypoint_invalid")
    pf05 = _require_exact_keys(
        payload["pf05_command_catalog"],
        {
            "argument_policing_capture", "env", "global_flags_checked", "implemented_commands",
            "showcompat_help_capture", "streams_checked",
        },
        "cli_summary_pf05",
    )
    if pf05["global_flags_checked"] != ["--help", "--version"]:
        raise ValueError("cli_summary_pf05_flags_invalid")
    if pf05["implemented_commands"] != ["showcompat", "aux-preview", "bg:resolve", "dev:sampler"]:
        raise ValueError("cli_summary_pf05_commands_invalid")
    if pf05["showcompat_help_capture"] != "artifacts/cli/help/showcompat_help.txt":
        raise ValueError("cli_summary_pf05_help_capture_invalid")
    if pf05["argument_policing_capture"] != "artifacts/cli/help/reject_nonjson.txt":
        raise ValueError("cli_summary_pf05_argument_capture_invalid")
    expected_pf05_env = {
        "ALLOW_NETWORK": "0",
        "APP_ENV": "test",
        "LANG": "C",
        "LC_ALL": "C",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }
    if pf05["env"] != expected_pf05_env:
        raise ValueError("cli_summary_pf05_env_invalid")
    streams = _require_exact_keys(
        pf05["streams_checked"], {"help_stderr_empty", "reject_stdout_empty"}, "cli_summary_streams"
    )
    if any(value is not True for value in streams.values()):
        raise ValueError("cli_summary_streams_invalid")
    sampler = _require_exact_keys(
        payload["sampler_semantics"], {"candidate_order", "cmd", "seed", "sha256", "two_run_equal"}, "cli_summary_sampler"
    )
    sampler_sha = _require_hex64(sampler["sha256"], "cli_summary_sampler.sha256")
    expected_sampler_bytes, expected_candidate_order = _expected_sampler_capture()
    if sampler_sha != hashlib.sha256(expected_sampler_bytes).hexdigest():
        raise ValueError("cli_summary_sampler_sha_mismatch")
    expected_sampler_cmd = [
        "python", "-m", "engine.cli", "dev:sampler", "--viewer",
        "viewer-cli-conformance", "--candidates-file", "<tempfile>",
        "--seed", "seed-cli-conformance",
    ]
    if (
        sampler["two_run_equal"] is not True
        or sampler["cmd"] != expected_sampler_cmd
        or sampler["seed"] != "seed-cli-conformance"
        or sampler["candidate_order"] != expected_candidate_order
    ):
        raise ValueError("cli_summary_sampler_posture_invalid")


def _validate_selection_trace(_target: Target, obj: object) -> None:
    payload = _require_exact_keys(obj, {"selection_trace"}, "selection_trace")
    trace = payload["selection_trace"]
    if trace != list(ADMIN_SELECTION_TRACE):
        raise ValueError("selection_trace_source_mismatch")


def _validate_pair_input(target: Target, obj: object) -> None:
    payload = _require_exact_keys(obj, {"left", "right"}, "pair_input")
    _validate_birth(payload["left"], include_tz=True, label="pair_input.left")
    _validate_birth(payload["right"], include_tz=True, label="pair_input.right")
    counterpart = _require_exact_keys(
        _read_bound_json(_PAIR_COUNTERPARTS[target.rel_path]), {"left", "right"}, "pair_counterpart"
    )
    if payload["left"] != counterpart["right"] or payload["right"] != counterpart["left"]:
        raise ValueError("pair_counterpart_not_reversed")


def _validate_release_manifest_snapshot(_target: Target, obj: object) -> None:
    payload = _require_exact_keys(
        obj, {"root", "version", "built_at_utc", "files"}, "release_manifest"
    )
    files = payload["files"]
    if not isinstance(files, list) or not files:
        raise ValueError("release_manifest_files_invalid")
    if payload["root"] != "catalog/":
        raise ValueError("release_manifest_metadata_invalid")
    version = _require_string(payload["version"], "release_manifest.version")
    built_at_utc = _require_string(
        payload["built_at_utc"], "release_manifest.built_at_utc"
    )
    seen: set[str] = set()
    with tempfile.TemporaryDirectory(prefix="canonical-manifest-") as temp_name:
        temp_root = Path(temp_name)
        for index, raw in enumerate(files):
            entry = _require_exact_keys(raw, {"path", "sha256", "size"}, f"release_manifest_entry_{index}")
            name = _require_string(entry["path"], f"release_manifest_entry_{index}.path")
            parts = name.split("/")
            if (
                name.startswith("/")
                or "\\" in name
                or len(name.encode("utf-8")) > 256
                or any(part in {"", ".", ".."} for part in parts)
                or name in seen
            ):
                raise ValueError("release_manifest_entry_path_unsafe")
            seen.add(name)
            source = ROOT / name
            try:
                source.resolve().relative_to(ROOT.resolve())
            except ValueError as exc:
                raise ValueError("release_manifest_entry_path_unsafe") from exc
            if source.is_symlink() or not source.is_file():
                raise ValueError("release_manifest_source_invalid")
            destination = temp_root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        if tuple(entry["path"] for entry in files) != _EXPECTED_RELEASE_MANIFEST_PATHS:
            raise ValueError("release_manifest_input_roster_invalid")
        manifest_path = temp_root / "catalog" / "manifest.json"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_bytes(sercanon(payload, sort_keys=True))
        result = cut_manifest(
            manifest_path,
            version=version,
            built_at_utc=built_at_utc,
            check=True,
        )
        if result != 0:
            raise ValueError("release_manifest_member_integrity_mismatch")


def _validate_registry_snapshot(target: Target, obj: object) -> None:
    with tempfile.TemporaryDirectory(prefix="canonical-registry-") as temp_name:
        temp_root = Path(temp_name)
        shutil.copytree(ROOT / "catalog", temp_root / "catalog")
        candidate = temp_root / target.rel_path
        candidate.write_bytes(sercanon(obj, sort_keys=True))
        load_registry_config(temp_root)


def _canonical_json_without_lf(obj: object) -> bytes:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True).encode("utf-8")


@contextlib.contextmanager
def _working_directory(path: Path) -> Iterator[None]:
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def _validate_narrative_snapshot(target: Target, obj: object) -> None:
    with tempfile.TemporaryDirectory(prefix="canonical-narratives-") as temp_name:
        temp_root = Path(temp_name)
        catalog_root = temp_root / "catalog" / "narratives"
        shutil.copytree(ROOT / "catalog" / "narratives", catalog_root)
        candidate = temp_root / target.rel_path
        candidate.write_bytes(sercanon(obj, sort_keys=True))
        candidate_sha = hashlib.sha256(_canonical_json_without_lf(obj)).hexdigest()
        candidate.with_suffix(candidate.suffix + ".sha256").write_text(
            candidate_sha + "\n", encoding="utf-8"
        )
        if candidate.name != "manifest.json":
            manifest_path = catalog_root / "manifest.json"
            manifest = json.loads(manifest_path.read_bytes())
            rel = target.rel_path
            matches = [entry for entry in manifest.get("files", []) if entry.get("path") == rel]
            if len(matches) != 1:
                raise ValueError("narrative_manifest_binding_missing_or_duplicate")
            matches[0]["sha256"] = candidate_sha
            matches[0]["size_bytes"] = len(_canonical_json_without_lf(obj))
            manifest_path.write_bytes(sercanon(manifest, sort_keys=True))
            manifest_sha = hashlib.sha256(_canonical_json_without_lf(manifest)).hexdigest()
            manifest_path.with_suffix(".json.sha256").write_text(
                manifest_sha + "\n", encoding="utf-8"
            )
        validate_narrative_registry_snapshot(catalog_root, repo_root=temp_root)
        with _working_directory(temp_root):
            load_pack(Path("catalog/narratives"), temp_root / "narratives")


def _validate_schema_document(target: Target, obj: object) -> None:
    if not isinstance(obj, dict):
        raise ValueError("schema_document_must_be_object")
    if (
        obj.get("$schema") != "https://json-schema.org/draft/2020-12/schema"
        or obj.get("$id") != target.rel_path
    ):
        raise ValueError("schema_document_identity_invalid")
    jsonschema.Draft202012Validator.check_schema(obj)
    expected_sha = _EXPECTED_SCHEMA_SHA256.get(target.rel_path)
    if expected_sha is None:
        raise ValueError("schema_document_contract_unbound")
    if hashlib.sha256(sercanon(obj, sort_keys=True)).hexdigest() != expected_sha:
        raise ValueError("schema_document_contract_mismatch")


_VALIDATOR_REGISTRY: Mapping[str, Callable[[Target, object], None]] = {
    "canonical_json.generated.showcompat_capture.v1": _validate_showcompat_capture,
    "canonical_json.generated.showcompat_args.v1": _validate_showcompat_args,
    "canonical_json.generated.reader_envelope.v1": _validate_reader_envelope,
    "canonical_json.generated.cli_conformance_summary.v1": _validate_cli_summary,
    "canonical_json.generated.conjunction_envelope.v1": _validate_conjunction_envelope,
    "canonical_json.generated.selection_trace.v1": _validate_selection_trace,
    "canonical_json.generated.pair_input.v1": _validate_pair_input,
    "scripts.cut_release_manifest.cut_manifest(check=True)": _validate_release_manifest_snapshot,
    "engine.config.registry_loader.load_registry_config": _validate_registry_snapshot,
    "tools.evidence.generate_narrative_registry_diff.validate_registry_snapshot": _validate_narrative_snapshot,
    "jsonschema.Draft202012Validator.check_schema": _validate_schema_document,
}


def _validate_target(target: Target, obj: object) -> None:
    validator = _VALIDATOR_REGISTRY.get(target.validator)
    if validator is None:
        label = target.validator or "<empty>"
        raise ValueError(f"unimplemented_validator:{label}")
    if target.schema:
        schema = json.loads((ROOT / target.schema).read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(obj)
    validator(target, obj)
    _validate_frozen_generated_capture(target, obj)

    for rule_path, identity in target.set_rules:
        if not rule_path or not identity:
            raise ValueError("incomplete_set_rule")
        if rule_path in {"$.channels", "$.files"} and isinstance(obj, dict):
            field = rule_path.removeprefix("$.")
            values = obj.get(field)
            expected = canonicalize_declared_set(values, identity=identity) if isinstance(values, list) else None
            if values != expected:
                raise ValueError(f"set_not_canonical:{rule_path}")
        elif rule_path.startswith("$.channels[*].") and isinstance(obj, dict):
            field = rule_path.rsplit(".", 1)[-1]
            channels = obj.get("channels")
            if not isinstance(channels, list):
                raise ValueError("channels_set_owner_missing")
            for index, channel in enumerate(channels):
                values = channel.get(field) if isinstance(channel, dict) else None
                if not isinstance(values, list):
                    raise ValueError(f"set_array_missing:{rule_path}:{index}")
                expected = canonicalize_declared_set(values, identity=None if identity == "value" else identity)
                if values != expected:
                    raise ValueError(f"set_not_canonical:{rule_path}:{index}")
        else:
            raise ValueError(f"unimplemented_set_rule:{rule_path}")


@dataclass(frozen=True)
class Probe:
    name: str
    method: str
    route: str
    expected_status: int
    query: Mapping[str, str] | None = None
    payload: Mapping[str, object] | None = None


CONJUNCTION_PROBES: Sequence[Probe] = (
    Probe(
        name="http_reader",
        method="GET",
        route="/reader",
        expected_status=400,
        query={
            "birthdate": "1990-01-01",
            "birthtime": "12:00",
            "location": "UTC",
        },
    ),
    Probe(
        name="http_dev_writer_conjunction",
        method="GET",
        route="/dev/writer/conjunction",
        expected_status=503,
        query={
            "a_user_id": "left",
            "b_user_id": "right",
            "a_birthdate": "1990-01-01",
            "a_birthtime": "08:30",
            "a_location": "Amsterdam",
            "b_birthdate": "1991-02-02",
            "b_birthtime": "09:45",
            "b_location": "Berlin",
        },
    ),
    Probe(
        name="http_dev_reader_conjunction",
        method="GET",
        route="/dev/reader/conjunction",
        expected_status=503,
        query={
            "a_user_id": "left",
            "b_user_id": "right",
            "a_birthdate": "1990-01-01",
            "a_birthtime": "08:30",
            "a_location": "Amsterdam",
            "b_birthdate": "1991-02-02",
            "b_birthtime": "09:45",
            "b_location": "Berlin",
        },
    ),
    Probe(
        name="http_dev_sampler_conjunction",
        method="GET",
        route="/dev/sampler/conjunction",
        expected_status=503,
        query={
            "a_user_id": "left",
            "b_user_id": "right",
            "a_birthdate": "1990-01-01",
            "a_birthtime": "08:30",
            "a_location": "Amsterdam",
            "b_birthdate": "1991-02-02",
            "b_birthtime": "09:45",
            "b_location": "Berlin",
        },
    ),
    Probe(
        name="http_internal_dev_sampler",
        method="POST",
        route="/internal/dev/sampler",
        expected_status=200,
        payload={
            "viewer_id": "viewer-1",
            "candidate_ids": ["candidate-a", "candidate-b"],
            "seed": "seed-1",
        },
    ),
)


def _generated_at() -> str:
    return GATE_CAPTURED_AT_UTC


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_if_changed(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_bytes() == content:
        return
    path.write_bytes(content)


def _write_path_proof(rel_path: str, *, produced_at: str) -> None:
    path = ROOT / rel_path
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel_path,
        sha256=_sha256(path.read_bytes()),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )


def _render_log_lines(rows: Iterable[Mapping[str, object]]) -> bytes:
    serialized = [json.dumps(row, separators=(",", ":"), sort_keys=True) for row in rows]
    return ("\n".join(serialized) + "\n").encode("utf-8")


def _stale_outputs(expected: Mapping[Path, bytes]) -> list[Path]:
    return [
        path
        for path, expected_bytes in expected.items()
        if not path.is_file() or path.read_bytes() != expected_bytes
    ]


def _target_inventory_is_exact(targets: Sequence[Target]) -> bool:
    target_paths = tuple(sorted(target.rel_path for target in targets))
    target_bindings = tuple(
        sorted((target.rel_path, target.validator, target.schema) for target in targets)
    )
    set_rules = tuple(
        sorted(
            (target.rel_path, rule_path, identity)
            for target in targets
            for rule_path, identity in target.set_rules
        )
    )
    return (
        len(targets) == len(EXPECTED_TARGET_PATHS)
        and target_paths == EXPECTED_TARGET_PATHS
        and target_bindings == EXPECTED_TARGET_BINDINGS
        and set_rules == EXPECTED_SET_RULES
    )


def _run_gate(targets: Sequence[Target], *, check_only: bool = False) -> int:
    env = ensure_determinism_env(apply=True)
    generated_at = _generated_at()

    check_rows: list[dict[str, object]] = []
    compare_rows: list[dict[str, object]] = []
    failures: list[str] = []

    if not _target_inventory_is_exact(targets):
        failures.append("target_inventory_incomplete_or_duplicate")
    for target in sorted(targets, key=lambda t: t.rel_path):
        rel = target.rel_path
        path = ROOT / rel
        entry_common = {
            "schema": "canonical_json.check.v1",
            "artifact": target.name,
            "path": rel,
            "checked_at_utc": generated_at,
        }
        compare_common = {
            "schema": "canonical_json.compare.v1",
            "artifact": target.name,
            "path": rel,
            "compared_at_utc": generated_at,
        }

        if not path.exists():
            failure = f"missing:{rel}"
            failures.append(failure)
            check_rows.append({**entry_common, "status": "fail", "issues": [failure]})
            compare_rows.append({**compare_common, "status": "fail", "match": False, "issues": [failure]})
            continue

        data = path.read_bytes()
        issues: list[str] = []
        try:
            obj = json.loads(data)
        except json.JSONDecodeError as exc:
            obj = None
            issues.append(f"json_error:{exc.msg}")

        canonical_bytes = b""
        if obj is not None:
            canonical_bytes = sercanon(obj, sort_keys=True)
            try:
                _validate_target(target, obj)
            except Exception as exc:  # validators deliberately fail closed
                issues.append(f"validation_error:{type(exc).__name__}:{exc}")

        trailing_lf = data.endswith(b"\n")
        if not trailing_lf:
            issues.append("missing_trailing_lf")
        if data.startswith(b"\xef\xbb\xbf"):
            issues.append("utf8_bom_present")
        if not data:
            issues.append("empty_bytes")

        match = bool(obj is not None and data == canonical_bytes)
        if not match:
            issues.append("non_canonical_bytes")

        status = "pass" if not issues else "fail"
        if status == "fail":
            failures.append(rel)

        check_rows.append(
            {
                **entry_common,
                "status": status,
                "issues": issues,
                "sha256": _sha256(data),
                "canonical_sha256": _sha256(canonical_bytes) if canonical_bytes else None,
                "size_bytes": len(data),
                "match": match,
                "trailing_lf": trailing_lf,
            }
        )
        compare_rows.append(
            {
                **compare_common,
                "status": status,
                "match": match,
                "original_sha256": _sha256(data),
                "canonical_sha256": _sha256(canonical_bytes) if canonical_bytes else None,
                "size_bytes": len(data),
                "issues": issues,
            }
        )

    os.environ.setdefault("APP_ENV", "dev")
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        for probe in CONJUNCTION_PROBES:
            entry_common = {
                "schema": "canonical_json.check.v1",
                "artifact": probe.name,
                "path": f"endpoint:{probe.route}",
                "checked_at_utc": generated_at,
            }
            compare_common = {
                "schema": "canonical_json.compare.v1",
                "artifact": probe.name,
                "path": f"endpoint:{probe.route}",
                "compared_at_utc": generated_at,
            }
            if probe.method == "POST":
                response = client.post(
                    probe.route,
                    data=json.dumps(probe.payload),
                    headers={"Content-Type": "application/json; charset=utf-8"},
                )
            else:
                response = client.get(probe.route, query_string=probe.query)
            data = response.data
            issues: list[str] = []
            if response.status_code != probe.expected_status:
                issues.append(f"unexpected_http_status:{response.status_code}!={probe.expected_status}")
            try:
                obj = json.loads(data)
            except json.JSONDecodeError as exc:
                obj = None
                issues.append(f"json_error:{exc.msg}")
            canonical_bytes = b""
            if obj is not None:
                canonical_bytes = sercanon(obj, sort_keys=True)

            trailing_lf = data.endswith(b"\n")
            if not trailing_lf:
                issues.append("missing_trailing_lf")
            if data.startswith(b"\xef\xbb\xbf"):
                issues.append("utf8_bom_present")
            if not data:
                issues.append("empty_bytes")

            match = bool(obj is not None and data == canonical_bytes)
            if not match:
                issues.append("non_canonical_bytes")
            status = "pass" if not issues else "fail"
            if status == "fail":
                failures.append(f"endpoint:{probe.route}")

            check_rows.append(
                {
                    **entry_common,
                    "status": status,
                    "issues": issues,
                    "sha256": _sha256(data),
                    "canonical_sha256": _sha256(canonical_bytes) if canonical_bytes else None,
                    "size_bytes": len(data),
                    "match": match,
                    "trailing_lf": trailing_lf,
                    "http_status": response.status_code,
                    "expected_http_status": probe.expected_status,
                }
            )
            compare_rows.append(
                {
                    **compare_common,
                    "status": status,
                    "match": match,
                    "original_sha256": _sha256(data),
                    "canonical_sha256": _sha256(canonical_bytes) if canonical_bytes else None,
                    "size_bytes": len(data),
                    "issues": issues,
                    "http_status": response.status_code,
                    "expected_http_status": probe.expected_status,
                }
            )

    check_bytes = _render_log_lines(check_rows)
    compare_bytes = _render_log_lines(compare_rows)
    gate_payload = {
        "schema": "canonical_json.gate.v1",
        "generated_at_utc": generated_at,
        "status": "pass" if not failures else "fail",
        "checked_targets": [
            target.rel_path
            for target in sorted(targets, key=lambda target: target.rel_path)
        ],
        "target_bindings": [
            {"path": target.rel_path, "schema": target.schema, "validator": target.validator}
            for target in sorted(targets, key=lambda target: target.rel_path)
        ],
        "set_rules": [
            {"identity": identity, "path": path, "target": target.rel_path}
            for target in sorted(targets, key=lambda target: target.rel_path)
            for path, identity in sorted(target.set_rules)
        ],
        "env": env,
        "outputs": {
            "check_log": "audit/gates/canonical_json/json_canonical_check.log",
            "compare_log": "audit/gates/canonical_json/json_canon_compare.log",
            "gate_summary": "audit/gates/canonical_json/canonical_json.gate.json",
        },
        "failures": failures,
    }
    json_gate_payload = {
        "schema": "canonical_json.gate.v1",
        "generated_at_utc": generated_at,
        "status": "pass" if not failures else "fail",
        "checked_targets": [
            target.rel_path
            for target in sorted(targets, key=lambda target: target.rel_path)
        ],
        "target_bindings": [
            {"path": target.rel_path, "schema": target.schema, "validator": target.validator}
            for target in sorted(targets, key=lambda target: target.rel_path)
        ],
        "set_rules": [
            {"identity": identity, "path": path, "target": target.rel_path}
            for target in sorted(targets, key=lambda target: target.rel_path)
            for path, identity in sorted(target.set_rules)
        ],
        "env": env,
        "outputs": {
            "check_log": "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
            "compare_log": "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
            "structured_record": "audit/gates/json_gate/canonical/json_gate_structured_record.json",
        },
        "failures": failures,
    }
    outputs = {
        CANON_DIR / "json_canonical_check.log": check_bytes,
        CANON_DIR / "json_canon_compare.log": compare_bytes,
        CANON_DIR / "canonical_json.gate.json": sercanon(
            gate_payload,
            sort_keys=True,
        ),
        JSON_GATE_DIR / "json_gate_check_log.ndjson": check_bytes,
        JSON_GATE_DIR / "json_gate_compare_log.ndjson": compare_bytes,
        JSON_GATE_DIR / "json_gate_structured_record.json": sercanon(
            json_gate_payload,
            sort_keys=True,
        ),
    }

    if check_only:
        failures.extend(
            f"stale_gate_artifact:{path.relative_to(ROOT).as_posix()}"
            for path in _stale_outputs(outputs)
        )
    else:
        for path, content in outputs.items():
            _write_if_changed(path, content)
        for path in outputs:
            _write_path_proof(
                path.relative_to(ROOT).as_posix(),
                produced_at=generated_at,
            )

    if failures:
        return 1
    return 0


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the canonical JSON gate")
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="validate targets without rewriting gate artifacts",
    )
    return parser.parse_args(list(argv) if argv is not None else None)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    return _run_gate(TARGETS, check_only=args.check_only)


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
