#!/usr/bin/env python3
"""Generate and validate the evidence index snapshot gate artifact."""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HUMAN_INDEX_REL = "docs/evidence/INDEX.json"
MIRROR_REL = "artifacts/evidence_index.jsonl"
SNAPSHOT_REL = "audit/gates/evidence_index_snapshot/evidence_index_snapshot.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from tools.evidence import update_evidence_index


@dataclass(frozen=True)
class Inputs:
    human_path: Path
    mirror_path: Path
    snapshot_path: Path


def _utc_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_human_keys(path: Path) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("INDEX.json payload must be a list")
    keys: set[str] = set()
    for entry in payload:
        if not isinstance(entry, dict):
            raise ValueError("INDEX.json entry must be a dict")
        key = entry.get("artifact_key") or entry.get("title")
        if not isinstance(key, str) or not key:
            raise ValueError("INDEX.json entry missing artifact_key")
        keys.add(key)
    return keys


def _load_mirror_keys(path: Path) -> set[str]:
    keys: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        if not isinstance(entry, dict):
            raise ValueError("evidence_index.jsonl entry must be an object")
        key = entry.get("artifact_key")
        if not isinstance(key, str) or not key:
            raise ValueError("evidence_index.jsonl entry missing artifact_key")
        keys.add(key)
    return keys


def _render_snapshot(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")


def _write_snapshot(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = _render_snapshot(payload)
    if path.exists() and path.read_bytes() == rendered:
        return
    path.write_bytes(rendered)


def _write_path_proof(path: Path, *, produced_at: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )


def _check_path_proof(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=None,
        produced_at=None,
        default_produced_at=_utc_now(),
        check=True,
        stat_mtime=stat.st_mtime,
    )


def _build_snapshot(inputs: Inputs, *, generated_at: str) -> dict[str, Any]:
    human_sha = _sha256_path(inputs.human_path)
    mirror_sha = _sha256_path(inputs.mirror_path)
    human_keys = _load_human_keys(inputs.human_path)
    mirror_keys = _load_mirror_keys(inputs.mirror_path)
    return {
        "generated_at_utc": generated_at,
        "inputs": {
            "human_index_path": HUMAN_INDEX_REL,
            "human_index_sha256": human_sha,
            "machine_mirror_path": MIRROR_REL,
            "machine_mirror_sha256": mirror_sha,
        },
        "parity": {
            "artifact_keys_match": human_keys == mirror_keys,
        },
        "schema_version": "1",
    }


def _validate_snapshot(inputs: Inputs, snapshot_path: Path) -> list[str]:
    issues: list[str] = []
    if not snapshot_path.exists():
        issues.append("MISSING_SNAPSHOT")
        return issues

    data = snapshot_path.read_bytes()
    try:
        payload = json.loads(data)
    except json.JSONDecodeError as exc:
        issues.append(f"SNAPSHOT_JSON_ERROR:{exc.msg}")
        return issues

    if not isinstance(payload, dict):
        issues.append("SNAPSHOT_NOT_OBJECT")
        return issues

    if payload.get("schema_version") != "1":
        issues.append("SCHEMA_VERSION")
    generated_at = payload.get("generated_at_utc")
    if not isinstance(generated_at, str):
        issues.append("GENERATED_AT")
    else:
        try:
            update_evidence_index._parse_utc_iso8601(generated_at)
        except ValueError:
            issues.append("GENERATED_AT_FORMAT")

    inputs_obj = payload.get("inputs")
    if not isinstance(inputs_obj, dict):
        issues.append("INPUTS")
        inputs_obj = {}

    parity_obj = payload.get("parity")
    if not isinstance(parity_obj, dict):
        issues.append("PARITY")
        parity_obj = {}

    human_path = inputs_obj.get("human_index_path")
    mirror_path = inputs_obj.get("machine_mirror_path")
    if human_path != HUMAN_INDEX_REL:
        issues.append("INPUT_PATH_HUMAN")
    if mirror_path != MIRROR_REL:
        issues.append("INPUT_PATH_MIRROR")

    try:
        human_sha = _sha256_path(inputs.human_path)
        mirror_sha = _sha256_path(inputs.mirror_path)
    except OSError:
        issues.append("INPUT_READ_ERROR")
        return issues

    if inputs_obj.get("human_index_sha256") != human_sha:
        issues.append("INPUT_SHA_HUMAN")
    if inputs_obj.get("machine_mirror_sha256") != mirror_sha:
        issues.append("INPUT_SHA_MIRROR")

    try:
        human_keys = _load_human_keys(inputs.human_path)
        mirror_keys = _load_mirror_keys(inputs.mirror_path)
        parity_expected = human_keys == mirror_keys
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        issues.append(f"INPUT_PARSE:{exc.__class__.__name__}")
        parity_expected = None

    parity_value = parity_obj.get("artifact_keys_match")
    if parity_value is not True:
        issues.append("PARITY_FALSE")
    if parity_expected is not None and parity_value != parity_expected:
        issues.append("PARITY_MISMATCH")

    if data != _render_snapshot(payload):
        issues.append("NON_CANONICAL_JSON")

    try:
        _check_path_proof(snapshot_path)
    except SystemExit as exc:
        issues.append(f"PATH_PROOF:{exc}")

    return issues


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate/validate evidence index snapshot.")
    parser.add_argument("--check", action="store_true", help="validate only; do not rewrite artifacts")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    ensure_determinism_env(apply=True)

    inputs = Inputs(
        human_path=ROOT / HUMAN_INDEX_REL,
        mirror_path=ROOT / MIRROR_REL,
        snapshot_path=ROOT / SNAPSHOT_REL,
    )

    missing_inputs = [
        rel
        for rel, path in ((HUMAN_INDEX_REL, inputs.human_path), (MIRROR_REL, inputs.mirror_path))
        if not path.exists()
    ]
    if missing_inputs:
        print(f"STATUS: TOOLING_BLOCKED missing_inputs={','.join(missing_inputs)}")
        return 2

    if not args.check:
        generated_at = _utc_now()
        try:
            snapshot_payload = _build_snapshot(inputs, generated_at=generated_at)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"STATUS: FAIL_BEHAVIOR build_error={exc.__class__.__name__}")
            return 1
        _write_snapshot(inputs.snapshot_path, snapshot_payload)
        _write_path_proof(inputs.snapshot_path, produced_at=generated_at)

    if not inputs.snapshot_path.exists():
        print("STATUS: TOOLING_BLOCKED missing_snapshot")
        return 2

    issues = _validate_snapshot(inputs, inputs.snapshot_path)
    if issues:
        print(f"STATUS: FAIL_BEHAVIOR issues={','.join(issues)}")
        return 1

    print("STATUS: PASS")
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
