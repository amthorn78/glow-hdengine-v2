#!/usr/bin/env python3
"""Fail closed if active source reintroduces a retired DB transport."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_PREFIXES = (
    "audit/",
    "artifacts/",
    "docs/crd/",
    "docs/plans/",
    "docs/pfcanon/",
    "docs/design/",
    "docs/adr/",
    "handoff/",
    "tests/",
    "codex/out/",
    "notes/",
)
TEXT_SUFFIXES = {".py", ".md", ".yml", ".yaml", ".sh", ".txt"}
RETIRED_PATHS = (
    "engine/db/providers/bridge_provider.py",
    "scripts/db_bridge/capture_introspection.py",
    "scripts/ops/hde_epic038_ops01r.py",
    "tools/evidence/hde_epic038_ops01_v5.py",
    "tools/evidence/generate_db_bridge_parity.py",
    "ci/checks/check_bridge_consistency.py",
)
FORBIDDEN_SYMBOLS = (
    "BridgeProvider",
    "BridgeUnavailable",
    "BridgeUnsupported",
    "bridge_factory",
    "generate_db_bridge_parity",
    "check_bridge_consistency",
    "hde_epic038_ops01r",
    "hde_epic038_ops01_v5",
)
FORBIDDEN_ACTIVE_PATH_TEXT = (
    "engine.db.providers.bridge_provider",
    "scripts/db_bridge/",
    "artifacts/db_bridge/",
)
RETIRED_KEYS = (
    "DB_ALLOW_BRIDGE_IN_PROD",
    "DB_BRIDGE_URL",
    "DB_FORCE_BRIDGE",
)
RETIRED_KEY_ALLOWLIST = {
    "engine/db/adapter.py",
    "adapter/db_access.py",
    "tools/evidence/generate_hde_epic038_direct_db_selection.py",
    "scripts/ops/hde_epic038_ops03.py",
    "tools/evidence/hde_epic038_ops03.py",
    "tools/evidence/generate_architecture_snapshot.py",
    "tools/evidence/generate_env_matrix_snapshot.py",
    "tools/evidence/retained_evidence_safety.py",
    "ci/checks/check_direct_db_contract.py",
    "docs/ADAPTER_DB.md",
    "docs/SECRETS.md",
}
HISTORICAL_READERS = {
    "tools/evidence/update_evidence_index.py",
    "tools/evidence/run_sanity_pipeline.py",
}
MANDATORY_MARKERS = {
    "engine/db/adapter.py": (
        "RETIRED_DB_TRANSPORT_KEYS",
        "retired_db_transport_keys_present",
        "def readonly_tx",
    ),
    "engine/db/providers/psycopg_provider.py": (
        "SET TRANSACTION READ ONLY",
        "validate_readonly_statements",
        "conn.rollback()",
    ),
    "scripts/ops/hde_epic038_ops03.py": (
        "ORDERED_QUERY_IDS",
        "expected_argv",
        "authorization_bytes_changed",
    ),
    "tools/evidence/hde_epic038_ops03.py": (
        "Draft202012Validator",
        "validate_retained_text_safety",
        "_checksums_valid",
    ),
    "tools/evidence/generate_hde_epic038_direct_db_selection.py": (
        "hde_epic038.direct_db_selection.v1",
        "validate_contract",
        "retired_keys_fail_before_provider_attempt",
    ),
    "scripts/db/_util.py": ("DBAccess.for_current_env()",),
    "scripts/db/capture_epic011_posture.py": (
        "direct PostgreSQL provider required",
        "artifacts/db/ddl_fingerprint.json",
        "artifacts/db/boundary_view.readonly.proof.txt",
    ),
    "scripts/db_adapter/capture_adapter_introspection.py": (
        "DBAccess.for_current_env()",
        "direct PostgreSQL provider required",
    ),
    "scripts/ops/capture_rails_open_scope.py": (
        "capture_adapter_introspection.py",
        "provider: psycopg",
    ),
}
SCHEMAS = (
    "schemas/hde_epic038_direct_db_selection.v1.json",
    "schemas/hde_epic038_ops03_authorization.v1.json",
    "schemas/hde_epic038_ops03_db_posture_summary.v1.json",
    "schemas/hde_epic038_ops03_env_presence.v1.json",
    "schemas/hde_epic038_ops03_failure_receipt.v1.json",
    "schemas/hde_epic038_ops03_nonclaims.v1.json",
    "schemas/hde_epic038_ops03_result_summary.v1.json",
    "schemas/hde_epic038_ops03_validation_receipt.v1.json",
)


def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _active(root: Path, path: Path) -> bool:
    relative = _relative(root, path)
    return (
        path.is_file()
        and path.suffix in TEXT_SUFFIXES
        and relative not in {"CHANGELOG.md", "AGENTS.md"}
        and not any(relative.startswith(prefix) for prefix in EXCLUDED_PREFIXES)
    )


def scan(root: Path = ROOT) -> tuple[str, ...]:
    violations: set[str] = set()
    for relative in RETIRED_PATHS:
        if (root / relative).exists():
            violations.add(f"{relative}:retired_path_present")

    for path in root.rglob("*"):
        if not _active(root, path):
            continue
        relative = _relative(root, path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        if relative != "ci/checks/check_direct_db_contract.py":
            for symbol in FORBIDDEN_SYMBOLS:
                if symbol in text:
                    violations.add(f"{relative}:forbidden_symbol:{symbol}")
        if relative not in HISTORICAL_READERS and relative != "ci/checks/check_direct_db_contract.py":
            for marker in FORBIDDEN_ACTIVE_PATH_TEXT:
                if marker in text:
                    violations.add(f"{relative}:active_retired_path:{marker}")
        for key in RETIRED_KEYS:
            if key in text and relative not in RETIRED_KEY_ALLOWLIST and relative not in HISTORICAL_READERS:
                violations.add(f"{relative}:retired_key_outside_refusal_roster:{key}")

    for relative, markers in MANDATORY_MARKERS.items():
        path = root / relative
        if not path.is_file():
            violations.add(f"{relative}:mandatory_file_missing")
            continue
        text = path.read_text(encoding="utf-8", errors="strict")
        for marker in markers:
            if marker not in text:
                violations.add(f"{relative}:mandatory_marker_missing:{marker}")

    for relative in SCHEMAS:
        path = root / relative
        if not path.is_file():
            violations.add(f"{relative}:schema_missing")
            continue
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            violations.add(f"{relative}:schema_unreadable")
            continue
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            violations.add(f"{relative}:draft_2020_12_missing")
        if schema.get("additionalProperties") is not False:
            violations.add(f"{relative}:top_level_unknown_keys_allowed")
    return tuple(sorted(violations))


def main(_argv: Iterable[str] | None = None) -> int:
    violations = scan()
    if violations:
        print("\n".join(violations))
        return 1
    print("DIRECT_DB_CONTRACT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
