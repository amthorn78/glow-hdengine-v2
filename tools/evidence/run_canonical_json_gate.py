#!/usr/bin/env python3
"""Run the canonical JSON gate and emit governed artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import jsonschema

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.evidence import update_evidence_index
from adapter.http_reader import create_app
from engine.config.registry_loader import load_manifest, load_registry_config
from engine.mech.helpers import canonicalize_declared_set

CANON_DIR = ROOT / "audit" / "gates" / "canonical_json"
JSON_GATE_DIR = ROOT / "audit" / "gates" / "json_gate" / "canonical"


@dataclass(frozen=True)
class Target:
    name: str
    rel_path: str
    validator: str
    schema: str | None = None
    set_rules: tuple[tuple[str, str], ...] = ()


_GENERATED = (
    ("cli_showcompat_stdout", "artifacts/cli/showcompat/stdout.json"), ("cli_showcompat_args", "artifacts/cli/showcompat/args.json"),
    ("cli_reader_dump", "artifacts/cli/reader_dump.json"), ("cli_summary", "artifacts/cli/summary.json"),
    ("cli_ab_stdout", "artifacts/cli/ab.json"), ("cli_ba_stdout", "artifacts/cli/ba.json"),
    ("cli_conjunction_output_ab", "artifacts/cli/out.json"), ("cli_conjunction_output_ba", "artifacts/cli/out_ba.json"),
    ("cli_conjunction_selection_trace", "artifacts/cli/abba_sidecar.json"), ("cli_conjunction_pair_ab", "artifacts/audit/cli/pair.json"),
    ("cli_conjunction_pair_ba", "artifacts/audit/cli/pair_ba.json"), ("cli_conjunction_showcompat_ab", "artifacts/audit/cli/showcompat_ab.json"),
    ("cli_conjunction_showcompat_ba", "artifacts/audit/cli/showcompat_ba.json"),
)
TARGETS: Sequence[Target] = tuple(Target(name, path, "json_object_contract") for name, path in _GENERATED) + (
    Target("catalog_manifest", "catalog/manifest.json", "engine.config.registry_loader.load_manifest", set_rules=(("$.files", "path"),)),
    Target("catalog_channels", "catalog/channels_v1.json", "jsonschema.Draft202012Validator", "schemas/channels_v1.schema.json", (("$.channels[*].centers", "value"), ("$.channels[*].domains", "value"), ("$.channels[*].flags", "value"))),
    Target("catalog_gates", "catalog/gates_v1.json", "jsonschema.Draft202012Validator", "schemas/gates_v1.schema.json"),
    Target("catalog_magic10", "catalog/magic10.json", "engine.config.registry_loader.load_registry_config"),
    Target("catalog_magic10_caps", "catalog/magic10_caps.json", "engine.config.registry_loader.load_registry_config"),
    Target("catalog_magic10_seeds", "catalog/magic10_seeds.json", "engine.config.registry_loader.load_registry_config"),
    Target("catalog_narratives_keys", "catalog/narratives/keys.json", "json_array_contract"),
    *(Target(f"catalog_narratives_{name}", f"catalog/narratives/{name}.json", "json_object_contract") for name in ("manifest", "palettes", "suppression_map", "templates")),
    Target("schema_gates", "schemas/gates_v1.schema.json", "jsonschema.Draft202012Validator.check_schema"),
    Target("schema_channels", "schemas/channels_v1.schema.json", "jsonschema.Draft202012Validator.check_schema"),
)

EXPECTED_TARGET_PATHS = frozenset(target.rel_path for target in TARGETS)


def _validate_target(target: Target, obj: object) -> None:
    if not target.validator:
        raise ValueError("unbound_target")
    if target.schema:
        schema = json.loads((ROOT / target.schema).read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(obj)
    elif target.validator.endswith("check_schema"):
        jsonschema.Draft202012Validator.check_schema(obj)
    elif target.validator.endswith("load_manifest"):
        load_manifest(ROOT)
    elif target.validator.endswith("load_registry_config"):
        load_registry_config(ROOT)
    elif target.validator == "json_object_contract":
        if not isinstance(obj, dict):
            raise ValueError("target_must_be_object")
    elif target.validator == "json_array_contract":
        if not isinstance(obj, list):
            raise ValueError("target_must_be_array")
    else:
        raise ValueError(f"unimplemented_validator:{target.validator}")

    for rule_path, identity in target.set_rules:
        if not rule_path or not identity:
            raise ValueError("incomplete_set_rule")
        if rule_path == "$.files" and isinstance(obj, dict):
            values = obj.get("files")
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
    manifest = json.loads((ROOT / "catalog/manifest.json").read_text(encoding="utf-8"))
    generated_at = manifest.get("built_at_utc")
    if not isinstance(generated_at, str) or not generated_at.endswith("Z"):
        raise ValueError("catalog_manifest_built_at_utc_invalid")
    return generated_at


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


def _run_gate(targets: Sequence[Target], *, check_only: bool = False) -> int:
    env = ensure_determinism_env(apply=True)
    generated_at = _generated_at()

    check_rows: list[dict[str, object]] = []
    compare_rows: list[dict[str, object]] = []
    failures: list[str] = []

    if len(targets) != len(EXPECTED_TARGET_PATHS) or {target.rel_path for target in targets} != EXPECTED_TARGET_PATHS:
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
