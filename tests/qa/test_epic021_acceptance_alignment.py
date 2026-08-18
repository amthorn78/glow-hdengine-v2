import json
from pathlib import Path

import pytest

from tools.qa import epic021_qa
from tools.qa.qa_harness import HarnessConfig, Status, evaluate_acceptance_map_viability

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
        if len(parts) < 6:
            continue
        first_cell = " ".join(parts[0].split()).lower()
        if first_cell in {"token name", "token_name"} or first_cell.replace(" ", "_") == "token_name":
            continue
        if all(not cell.strip() or set(cell.strip()) <= {"-", ":"} for cell in parts):
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


def test_canonical_renderer_uses_the_complete_current_roster():
    payload = json.loads(epic021_qa._acceptance_map_content())
    names = {token["name"] for token in payload["tokens"]}
    assert len(names) == 21
    assert {
        "CLI_READER_PARITY_OK",
        "QA_HARNESS_DISCIPLINE_OK",
        "QA_BOOTSTRAP_OK",
        "QA_BOOTSTRAP_TOOLING_FAIL",
        "QA_ACCEPTANCE_MAP_VIABILITY_OK",
    } <= names
    assert not names & {
        "PR_OPENED_OK",
        "CLI_READER_EMITTER_PARITY_OK",
        "CLI_SERIALIZER_GUARD_OK",
        "SANITY_PIPELINE_LOGGED_OK",
        "QA_STEP_LOGS_CONSOLIDATED_OK",
        "PF04-DD-QA-BOOTSTRAP-TOKENS",
        "PF19-DD-QA-PLAN-VIABILITY-TOKENS",
    }
    matrix = epic021_qa._token_matrix_content()
    rendered_inputs = (
        json.dumps(payload, sort_keys=True)
        + matrix
        + epic021_qa._readme_content()
    )
    assert "d00-bootstrap" in rendered_inputs
    assert "D00_bootstrap" not in rendered_inputs
    assert "<run-id>" not in matrix
    assert "step_*" not in matrix
    assert "`" not in matrix
    assert all(
        len(line.strip().strip("|").split("|")) == 7
        for line in matrix.splitlines()
        if line.startswith("|")
    )


def test_current_acceptance_inputs_are_strictly_viable():
    result, content = evaluate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC021"), planned_governed_ledger=True
    )
    payload = json.loads(content)
    assert result.status is Status.PASS, payload["broken_references"]
    assert payload["broken_references"] == []
    assert len(payload["token_status"]) == 21
    assert set(payload["token_status"].values()) == {"VALID"}
