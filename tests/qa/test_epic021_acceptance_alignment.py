import json
from pathlib import Path

import pytest

QA_ROOT = Path("audit/qa/hde-epic021")


def _normalize_status(value: str) -> str:
    return value.strip().lower().replace("-", "_")


def _parse_matrix() -> dict[str, dict[str, str]]:
    tokens: dict[str, dict[str, str]] = {}
    matrix_path = QA_ROOT / "token_evidence_matrix.md"
    for line in matrix_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().split("|") if part.strip()]
        if len(parts) < 6 or parts[0] in {"Token name", "---"}:
            continue
        token = parts[0]
        tokens[token] = {
            "evidence": parts[2],
            "status": parts[5],
        }
    return tokens


@pytest.fixture(autouse=True)
def enforce_env_pins(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")


def test_matrix_and_acceptance_map_align():
    matrix_tokens = _parse_matrix()
    acceptance = json.loads(Path("docs/acceptance_map_epic021.json").read_text(encoding="utf-8"))
    acceptance_tokens = {token["name"]: token for token in acceptance.get("tokens", []) if token.get("name")}

    assert matrix_tokens, "expected token matrix entries"
    assert acceptance_tokens, "expected acceptance map entries"
    assert set(matrix_tokens) == set(acceptance_tokens), "matrix and acceptance map token sets must match"

    for name, map_entry in acceptance_tokens.items():
        matrix_entry = matrix_tokens[name]
        assert _normalize_status(matrix_entry["status"]) == _normalize_status(map_entry.get("status", "")), name
        if _normalize_status(matrix_entry["status"]).startswith("implemented"):
            assert matrix_entry["evidence"], f"matrix evidence missing for {name}"
            evidence_titles = map_entry.get("evidence_titles") or []
            assert any(title.strip() for title in evidence_titles), f"acceptance map evidence missing for {name}"
