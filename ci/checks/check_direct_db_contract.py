#!/usr/bin/env python3
"""Fail closed if active source reintroduces a retired DB transport."""
from __future__ import annotations

import ast
import json
import subprocess
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
    "build/",
    "dist/",
    "*.egg-info/",
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
REFUSAL_CONTEXT_WORDS = ("retired", "refusal", "refuse", "absent", "deny", "deprecated", "historical", "nonclaim", "roster", "required_absent")
ACTIVE_GUIDANCE_WORDS = ("set ", "export ", "configure", "use ", "run ", "fallback", "url", "endpoint", "http", "request")
HTTP_MARKERS = ("requests.", "urllib.request", "httpx.", "urlopen", ".post(", ".get(", "http://", "https://")
HISTORICAL_READERS = {
    "tools/evidence/update_evidence_index.py",
    "tools/evidence/run_sanity_pipeline.py",
}
HISTORICAL_REFERENCE_DOCS = {
    "docs/EVIDENCE_INDEX.md",
    "docs/INDEX.md",
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



def _git_tracked_files(root: Path) -> tuple[Path, ...]:
    try:
        result = subprocess.run(["git", "ls-files", "-c", "-m", "-o", "--exclude-standard"], cwd=root, check=True, capture_output=True, text=True)
    except Exception:
        return tuple(path for path in root.rglob("*") if path.is_file())
    return tuple(root / line for line in result.stdout.splitlines() if line.strip())


def _line_refusal_only(line: str) -> bool:
    lowered = line.lower()
    return any(word in lowered for word in REFUSAL_CONTEXT_WORDS) and not (
        any(word in lowered for word in ACTIVE_GUIDANCE_WORDS) and not any(word in lowered for word in ("retired", "refusal", "historical", "must not", "do not"))
    )


def _is_environ_mapping(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Name)
        and node.id == "environ"
        or isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "os"
        and node.attr == "environ"
    )


def _retired_membership_compare(node: ast.Compare) -> bool:
    left = node.left
    for operator, right in zip(node.ops, node.comparators):
        if (
            isinstance(operator, (ast.In, ast.NotIn))
            and isinstance(left, ast.Constant)
            and isinstance(left.value, str)
            and left.value in RETIRED_KEYS
            and _is_environ_mapping(right)
        ):
            return True
        left = right
    return False


def _python_retired_consumption(text: str) -> tuple[int, ...]:
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return ()
    lines: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            func_name = ""
            if isinstance(func, ast.Attribute):
                func_name = func.attr
                if isinstance(func.value, ast.Name):
                    func_name = f"{func.value.id}.{func.attr}"
                elif isinstance(func.value, ast.Attribute):
                    func_name = f"{func.value.attr}.{func.attr}"
            elif isinstance(func, ast.Name):
                func_name = func.id
            args = list(node.args)
            const_args = [arg.value for arg in args if isinstance(arg, ast.Constant) and isinstance(arg.value, str)]
            if func_name in {"os.getenv", "getenv", "os.environ.get", "environ.get"} and any(arg in RETIRED_KEYS for arg in const_args):
                lines.add(node.lineno)
            segment = ast.get_source_segment(text, node) or ""
            if any(key in segment for key in RETIRED_KEYS) and any(marker in segment for marker in HTTP_MARKERS):
                lines.add(node.lineno)
        if isinstance(node, ast.Compare) and _retired_membership_compare(node):
            lines.add(node.lineno)
        if isinstance(node, ast.Subscript):
            segment = ast.get_source_segment(text, node) or ""
            if "os.environ" in segment and any(key in segment for key in RETIRED_KEYS):
                lines.add(node.lineno)
    return tuple(sorted(lines))


def _retired_key_violations(relative: str, text: str) -> list[str]:
    out: list[str] = []
    if relative.endswith(".py"):
        for line_number in _python_retired_consumption(text):
            out.append(f"{relative}:{line_number}:active_retired_key_consumption")
    for line_number, line in enumerate(text.splitlines(), 1):
        if not any(key in line for key in RETIRED_KEYS):
            continue
        if any(marker in line for marker in HTTP_MARKERS):
            out.append(f"{relative}:{line_number}:retired_key_http_bridge_use")
            continue
        if relative.endswith((".md", ".txt", ".yml", ".yaml", ".sh")) and not _line_refusal_only(line):
            out.append(f"{relative}:{line_number}:retired_key_active_guidance")
    return out

def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _active(root: Path, path: Path) -> bool:
    relative = _relative(root, path)
    return (
        path.is_file()
        and path.suffix in TEXT_SUFFIXES
        and relative not in {"CHANGELOG.md", "AGENTS.md"}
        and not any(relative.startswith(prefix) for prefix in EXCLUDED_PREFIXES if not prefix.startswith("*"))
        and ".egg-info/" not in relative
    )


def scan(root: Path = ROOT) -> tuple[str, ...]:
    violations: set[str] = set()
    for relative in RETIRED_PATHS:
        if (root / relative).exists():
            violations.add(f"{relative}:retired_path_present")

    for path in _git_tracked_files(root):
        if not _active(root, path):
            continue
        relative = _relative(root, path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        if relative != "ci/checks/check_direct_db_contract.py":
            for symbol in FORBIDDEN_SYMBOLS:
                if symbol in text:
                    violations.add(f"{relative}:forbidden_symbol:{symbol}")
        if relative not in HISTORICAL_READERS and relative != "ci/checks/check_direct_db_contract.py":
            for line_number, line in enumerate(text.splitlines(), 1):
                for marker in FORBIDDEN_ACTIVE_PATH_TEXT:
                    if marker not in line:
                        continue
                    explicitly_historical = (
                        relative in HISTORICAL_REFERENCE_DOCS
                        and "historical" in line.lower()
                    )
                    if not explicitly_historical:
                        violations.add(
                            f"{relative}:{line_number}:active_retired_path:{marker}"
                        )
        if relative != "ci/checks/check_direct_db_contract.py":
            violations.update(_retired_key_violations(relative, text))

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
