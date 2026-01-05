from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.qa import token_roster_validate

QA_ROOT = Path("audit/qa/hde-epic023")
MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
ACCEPTANCE_MAP_PATH = Path("docs/acceptance_map_epic023.json")
HUMAN_INDEX_PATH = Path("docs/evidence/INDEX.json")
MIRROR_PATH = Path("artifacts/evidence_index.jsonl")
GOVERNED_ROOTS = {"artifacts", "audit", "docs", "catalog", "schemas"}


def _normalize_status(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def _is_implemented(status: str) -> bool:
    normalized = _normalize_status(status)
    return normalized.startswith("implemented") or normalized.startswith("covered") or normalized in {
        "done",
        "green",
        "ready",
        "pass",
    }


def _parse_matrix() -> tuple[dict[str, dict[str, object]], set[str]]:
    tokens: dict[str, dict[str, object]] = {}
    duplicates: set[str] = set()
    for line in MATRIX_PATH.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().split("|") if part.strip()]
        if len(parts) < 6 or parts[0] in {"Token name", "---"}:
            continue
        token = parts[0]
        entry = {
            "pf_owner": parts[1],
            "evidence": [item.strip() for item in parts[2].split(";") if item.strip()],
            "ci_jobs": [item.strip() for item in parts[3].split(";") if item.strip()],
            "qa_logs": [item.strip() for item in parts[4].split(";") if item.strip()],
            "status": parts[5],
            "notes": parts[6] if len(parts) > 6 else "",
        }
        if token in tokens:
            duplicates.add(token)
        tokens[token] = entry
    return tokens, duplicates


def _parse_acceptance_map() -> tuple[dict[str, dict[str, object]], set[str]]:
    raw = json.loads(ACCEPTANCE_MAP_PATH.read_text(encoding="utf-8"))
    tokens: dict[str, dict[str, object]] = {}
    duplicates: set[str] = set()
    for entry in raw.get("tokens", []):
        name = entry.get("name")
        if not name:
            continue
        if name in tokens:
            duplicates.add(name)
        tokens[name] = entry
    return tokens, duplicates


def _load_registry_tokens() -> set[str]:
    pf04_paths = sorted(Path("docs/pfcanon").glob("PF04-Canon-HDE-Governance-*.md"))
    assert pf04_paths, "expected PF04 governance docs to be present"
    registry_tokens: set[str] = set()
    for path in pf04_paths:
        registry_tokens.update(token_roster_validate.extract_ok_tokens(path.read_text(encoding="utf-8")))

    registry_export = Path("reports/qa_acceptance_tokens.json")
    if registry_export.exists():
        payload = json.loads(registry_export.read_text(encoding="utf-8"))
        registry_tokens.update(
            token["name"] for token in payload.get("tokens", []) if isinstance(token, dict) and token.get("name")
        )
    return registry_tokens


def _load_index() -> list[dict[str, object]]:
    return json.loads(HUMAN_INDEX_PATH.read_text(encoding="utf-8"))


def _load_mirror() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for line in MIRROR_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        records.append(json.loads(line))
    return records


def _looks_like_repo_path(entry: str) -> bool:
    if not entry or entry.startswith("python "):
        return False
    if "::" in entry or " " in entry:
        return False
    if entry.startswith("/") or entry.startswith("~"):
        return False
    return True


@pytest.fixture(autouse=True)
def enforce_env_pins(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")


def test_epic023_acceptance_alignment_and_bindings() -> None:
    matrix_tokens, matrix_duplicates = _parse_matrix()
    acceptance_tokens, acceptance_duplicates = _parse_acceptance_map()
    registry_tokens = _load_registry_tokens()

    assert matrix_tokens, "expected token matrix entries"
    assert acceptance_tokens, "expected acceptance map entries"
    assert not matrix_duplicates, f"duplicate matrix tokens: {sorted(matrix_duplicates)}"
    assert not acceptance_duplicates, f"duplicate acceptance map tokens: {sorted(acceptance_duplicates)}"
    assert set(matrix_tokens) == set(acceptance_tokens), "matrix and acceptance map token sets must match"

    for token_name in matrix_tokens:
        assert token_name in registry_tokens, f"{token_name} missing from token registry"

    index_entries = _load_index()
    mirror_records = _load_mirror()
    index_by_path = {}
    for entry in index_entries:
        path = entry.get("discovered_physical_path")
        if path:
            index_by_path.setdefault(path, []).append(entry)
    mirror_by_path = {}
    for rec in mirror_records:
        path = rec.get("discovered_physical_path")
        if path:
            mirror_by_path.setdefault(path, []).append(rec)

    for token_name, map_entry in acceptance_tokens.items():
        matrix_entry = matrix_tokens[token_name]
        assert _normalize_status(matrix_entry["status"]) == _normalize_status(map_entry.get("status", "")), token_name

        combined_evidence = []
        combined_evidence.extend(matrix_entry["evidence"])
        combined_evidence.extend(map_entry.get("evidence_titles") or [])

        for evidence in combined_evidence:
            assert not evidence.endswith(".path_proof.txt"), f"{token_name} lists path_proof as primary evidence"

        if not _is_implemented(matrix_entry["status"]):
            continue

        assert combined_evidence, f"evidence missing for implemented token {token_name}"
        for evidence in combined_evidence:
            if not _looks_like_repo_path(evidence):
                continue
            parts = Path(evidence).parts
            assert parts, f"invalid evidence path for {token_name}: {evidence}"
            assert parts[0] in GOVERNED_ROOTS, f"evidence path outside governed roots for {token_name}: {evidence}"

            entries = index_by_path.get(evidence, [])
            mirrors = mirror_by_path.get(evidence, [])
            assert entries, f"expected {evidence} in docs/evidence/INDEX.json"
            assert mirrors, f"expected {evidence} in artifacts/evidence_index.jsonl"
            for rec in mirrors:
                assert rec.get("proof_anchor"), f"mirror record missing proof_anchor for {evidence}"
