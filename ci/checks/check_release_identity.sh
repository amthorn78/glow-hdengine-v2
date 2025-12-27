#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.serializer import canon
from engine.config.registry_loader import DuplicateIdError, SchemaValidationError, load_manifest
from tools.config.artifacts import require_closed_rails


CATALOG_MANIFEST = ROOT / "catalog" / "manifest.json"
FREEZE_PACK_PATH = ROOT / "artifacts" / "math" / "freeze_pack_manifest.json"
RELEASE_ID_PATH = ROOT / "artifacts" / "math" / "release_id.txt"
MANIFEST_SNAPSHOT_PATH = ROOT / "artifacts" / "math" / "manifest_snapshot.json"
CHECKSUMS_AUDIT_PATH = ROOT / "artifacts" / "math" / "checksums_audit.log"
ENV_PINS_PATH = ROOT / "artifacts" / "proofs" / "env_pins.txt"
RECOMPUTE_LOG_PATH = ROOT / "artifacts" / "math" / "release_id_recompute.log"

REQUIRED_FREEZE_KEYS = {"root", "version", "built_at_utc", "files"}


def _hex64(value: str | None) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(ch in "0123456789abcdef" for ch in value)


def _check_required_paths(errors: list[str]) -> None:
    required = [
        ("identity_input:manifest", CATALOG_MANIFEST),
        ("identity_input:freeze_pack", FREEZE_PACK_PATH),
        ("identity_input:release_id", RELEASE_ID_PATH),
        ("evidence:manifest_snapshot", MANIFEST_SNAPSHOT_PATH),
        ("evidence:checksums_audit", CHECKSUMS_AUDIT_PATH),
        ("evidence:env_pins", ENV_PINS_PATH),
        ("evidence:recompute_log", RECOMPUTE_LOG_PATH),
    ]
    for label, path in required:
        if not path.exists():
            errors.append(f"MISSING:{label}:{path}")
            continue
        if not path.is_file():
            errors.append(f"NOT_FILE:{label}:{path}")
            continue
        if path.stat().st_size == 0:
            errors.append(f"EMPTY:{label}:{path}")


def _load_canonical_manifest(errors: list[str]) -> bytes | None:
    if not CATALOG_MANIFEST.exists():
        errors.append(f"MISSING:manifest:{CATALOG_MANIFEST}")
        return None
    try:
        manifest_bytes = CATALOG_MANIFEST.read_bytes()
    except Exception as exc:  # noqa: BLE001
        errors.append(f"READ_ERROR:manifest:{exc}")
        return None
    try:
        manifest_json = json.loads(manifest_bytes.decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"MANIFEST_JSON_ERROR:{exc}")
        return None

    try:
        canonical_bytes = canon.sercanon(manifest_json, sort_keys=True)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"MANIFEST_CANON_ERROR:{exc}")
        return None

    if manifest_bytes != canonical_bytes:
        errors.append("MANIFEST_NOT_CANONICAL")

    return canonical_bytes


def _validate_manifest_schema(errors: list[str]) -> None:
    if not CATALOG_MANIFEST.exists():
        errors.append(f"MISSING:manifest:{CATALOG_MANIFEST}")
        return
    try:
        load_manifest(CATALOG_MANIFEST.parent.parent)
    except (SchemaValidationError, DuplicateIdError) as exc:
        code = getattr(exc, "code", str(exc))
        errors.append(f"MANIFEST_SCHEMA_ERROR:{code}")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"MANIFEST_SCHEMA_ERROR:{exc}")


def _assert_freeze_pack(canonical_bytes: bytes | None, errors: list[str]) -> None:
    if not FREEZE_PACK_PATH.exists():
        errors.append(f"MISSING:freeze_pack:{FREEZE_PACK_PATH}")
        return

    try:
        freeze_bytes = FREEZE_PACK_PATH.read_bytes()
    except Exception as exc:  # noqa: BLE001
        errors.append(f"READ_ERROR:freeze_pack:{exc}")
        return

    if canonical_bytes is not None and freeze_bytes != canonical_bytes:
        errors.append("FREEZE_PACK_BYTES_MISMATCH")

    try:
        freeze_payload = json.loads(freeze_bytes.decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"FREEZE_PACK_JSON_ERROR:{exc}")
        return

    key_set = set(freeze_payload.keys())
    if key_set != REQUIRED_FREEZE_KEYS:
        errors.append(f"FREEZE_PACK_KEYS_INVALID:{sorted(key_set)}")


def _assert_release_id(expected_release_id: str | None, errors: list[str]) -> None:
    if not RELEASE_ID_PATH.exists():
        errors.append(f"MISSING:release_id:{RELEASE_ID_PATH}")
        return

    value = RELEASE_ID_PATH.read_text(encoding="utf-8").strip()
    if not _hex64(value):
        errors.append("RELEASE_ID_INVALID")
        return
    if expected_release_id and value != expected_release_id:
        errors.append("RELEASE_ID_MISMATCH")


def _run_recompute_check(errors: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "release_id_recompute.py"), "--check"],
        capture_output=True,
        text=True,
        env=os.environ.copy(),
    )
    if proc.returncode != 0:
        errors.append(f"RECOMPUTE_CHECK_FAILED:{proc.returncode}")
        if proc.stdout:
            sys.stderr.write(proc.stdout)
        if proc.stderr:
            sys.stderr.write(proc.stderr)


def main() -> int:
    require_closed_rails()

    errors: list[str] = []
    _run_recompute_check(errors)
    _check_required_paths(errors)
    _validate_manifest_schema(errors)

    canonical_bytes = _load_canonical_manifest(errors)
    expected_release_id = hashlib.sha256(canonical_bytes).hexdigest() if canonical_bytes is not None else None
    _assert_freeze_pack(canonical_bytes, errors)
    _assert_release_id(expected_release_id, errors)

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
