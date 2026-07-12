import json
from pathlib import Path

QA_ROOT = Path("audit/qa/hde-epic022")
TOKEN_MATRIX = QA_ROOT / "token_evidence_matrix.md"
ACCEPTANCE_MAP = Path("docs/acceptance_map_epic022.json")
CLOSE_REPORT = Path("audit/EPIC-022_close_report.md")
MANIFEST = Path("audit/EPIC-022_MANIFEST.json")
ENV_TOKEN = "ENV_RAILS_POLICY_OK"
ENV_EXPECTED_EVIDENCE = {
    "ci/checks/check_env_pins.sh (rails gate)",
    "audit/gates/determinism/env_pins.log",
    "parity/errors_reader_cli.vendor_attempt_closed_rails.http.json",
    "parity/errors_reader_cli.vendor_attempt_closed_rails.cli.txt",
    "tests/cli/test_errors_parity.py::test_http_and_cli_parity",
}
ENV_EXPECTED_TESTS = {
    "ci/checks/check_env_pins.sh",
    "tests/cli/test_errors_parity.py::test_http_and_cli_parity",
}
CLI_STDOUT_TOKEN = "CLI_STDOUT_LF_OK"
CLI_STDOUT_EXPECTED_EVIDENCE = {
    "tests/cli/test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical",
    "artifacts/cli/showcompat/stdout.json",
    "artifacts/cli/showcompat/stdout.json.sha256",
    "artifacts/cli/showcompat/args.json",
}
CLI_STDOUT_EXPECTED_TESTS = {
    "tests/cli/test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical",
}
CLI_STDOUT_EXPECTED_ARTIFACTS = {
    Path("artifacts/cli/showcompat/stdout.json"),
    Path("artifacts/cli/showcompat/stdout.json.sha256"),
    Path("artifacts/cli/showcompat/args.json"),
}
INTERNAL_VERSION_CONTRACT_TEST = "tests/transport/test_internal_version_contract.py::test_internal_version_invariants_and_artifacts"
SHOWCOMPAT_TWO_RUN_TEST = "tests/cli/test_showcompat_parity_and_identity.py::test_two_run_identity_and_reemit"
LEGACY_INTERNAL_VERSION_ALIASES = {
    "artifacts/ops/internal_version/cond_if_none_match_headers.txt",
    "artifacts/ops/internal_version/cond_if_modified_since_headers.txt",
}
CANONICAL_INTERNAL_VERSION_CAPTURES = {
    "artifacts/ops/internal_version/headers_cond_if_none_match.txt",
    "artifacts/ops/internal_version/headers_cond_if_modified_since.txt",
}

D3_TOKEN_EXPECTATIONS = {
    "INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK": {
        "artifacts": {
            "artifacts/ops/internal_version/body_get.json",
            "artifacts/ops/internal_version/headers_get.txt",
            "artifacts/ops/internal_version/request_chain_manifest.json",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST},
    },
    "INTERNAL_VERSION_HEAD_PARITY_OK": {
        "artifacts": {
            "artifacts/ops/internal_version/headers_get.txt",
            "artifacts/ops/internal_version/headers_head.txt",
            "artifacts/ops/internal_version/request_chain_manifest.json",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST},
    },
    "INTERNAL_VERSION_CONDITIONALS_IGNORED_OK": {
        "artifacts": {
            "artifacts/ops/internal_version/headers_cond_if_none_match.txt",
            "artifacts/ops/internal_version/headers_cond_if_modified_since.txt",
            "artifacts/ops/internal_version/request_chain_manifest.json",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST},
    },
    "INTERNAL_VERSION_NO_ETAG_OK": {
        "artifacts": {
            "artifacts/ops/internal_version/headers_get.txt",
            "artifacts/ops/internal_version/headers_head.txt",
            "artifacts/ops/internal_version/headers_cond_if_none_match.txt",
            "artifacts/ops/internal_version/headers_cond_if_modified_since.txt",
            "artifacts/ops/internal_version/request_chain_manifest.json",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST},
    },
    "INTERNAL_VERSION_NO_STORE_OK": {
        "artifacts": {
            "artifacts/ops/internal_version/headers_get.txt",
            "artifacts/ops/internal_version/headers_head.txt",
            "artifacts/ops/internal_version/headers_cond_if_none_match.txt",
            "artifacts/ops/internal_version/headers_cond_if_modified_since.txt",
            "artifacts/ops/internal_version/request_chain_manifest.json",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST},
    },
    "TWO_RUN_IDENTITY_OK": {
        "artifacts": {
            "artifacts/audit/cli/two_run_identity.log",
            "artifacts/ops/internal_version/two_run_identity.log",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST, SHOWCOMPAT_TWO_RUN_TEST},
    },
    "RELEASE_ID_RECOMPUTE_OK": {
        "artifacts": {
            "artifacts/math/release_id_recompute.log",
            "artifacts/math/freeze_pack_manifest.json",
            "artifacts/math/release_id.txt",
            "artifacts/ops/internal_version/two_run_identity.log",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST},
    },
    "RELEASE_ID_FROM_MANIFEST_OK": {
        "artifacts": {
            "artifacts/math/freeze_pack_manifest.json",
            "artifacts/math/release_id.txt",
            "artifacts/ops/internal_version/two_run_identity.log",
        },
        "tests": {INTERNAL_VERSION_CONTRACT_TEST},
    },
}


def test_internal_version_bindings_use_only_canonical_capture_paths():
    matrix_text = TOKEN_MATRIX.read_text(encoding="utf-8")
    acceptance_text = ACCEPTANCE_MAP.read_text(encoding="utf-8")
    bound_text = matrix_text + "\n" + acceptance_text

    for legacy in LEGACY_INTERNAL_VERSION_ALIASES:
        assert legacy not in bound_text
    for canonical in CANONICAL_INTERNAL_VERSION_CAPTURES:
        assert canonical in bound_text
        assert Path(canonical).is_file()



def test_epic022_scaffold_files_exist():
    assert TOKEN_MATRIX.is_file(), "token_evidence_matrix.md should exist for EPIC022"
    assert ACCEPTANCE_MAP.is_file(), "EPIC022 acceptance map should exist in docs"
    assert CLOSE_REPORT.is_file(), "EPIC022 close report stub should exist"
    assert MANIFEST.is_file(), "EPIC022 manifest should exist"


def test_token_matrix_contains_epic_and_token():
    content = TOKEN_MATRIX.read_text(encoding="utf-8")
    assert "hde-epic022" in content.lower(), "Matrix should include the epic identifier"
    assert "PR_OPENED_OK" in content, "Matrix should seed baseline tokens"


def test_acceptance_map_structure_matches_template():
    template = json.loads(Path("docs/acceptance_map_epic021.json").read_text(encoding="utf-8"))
    data = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    assert set(data.keys()) == set(template.keys()), "Acceptance map keys should mirror the template"
    assert data.get("epic_id") == "HDE-EPIC022", "Acceptance map epic_id should target EPIC022"
    assert isinstance(data.get("tokens"), list), "Acceptance map tokens should be a list"


def test_close_report_mentions_matrix():
    content = CLOSE_REPORT.read_text(encoding="utf-8")
    assert "EPIC-022" in content, "Close report should identify EPIC-022"
    assert "audit/qa/hde-epic022/token_evidence_matrix.md" in content, "Close report should point to the token matrix"


def test_manifest_has_epic022_named_close_pack_bindings():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert str(data.get("epic_id", "")).lower() == "hde-epic022"
    key_outputs = data.get("key_outputs")
    assert isinstance(key_outputs, dict)
    assert key_outputs["close_manifest"] == "audit/EPIC-022_MANIFEST.json"
    assert key_outputs["close_report"] == "audit/EPIC-022_close_report.md"
    assert data["qa_step_manifest_path"] == (
        "audit/qa/hde-epic022/qa_step_logs_manifest.json"
    )


def _parse_matrix_rows():
    content = TOKEN_MATRIX.read_text(encoding="utf-8")
    lines = [line for line in content.splitlines() if line.startswith("|")]
    assert len(lines) >= 3, "Token matrix should include a header, separator, and at least one data row"
    header = [col.strip() for col in lines[0].strip("|").split("|")]
    rows = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    return rows


def _load_acceptance_map_tokens():
    data = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    token_map = {}
    for token in data.get("tokens", []):
        token_map.setdefault(token.get("name"), []).append(token)
    return token_map


def test_env_rails_policy_matrix_is_unique_and_concrete():
    rows = _parse_matrix_rows()
    env_rows = [row for row in rows if row.get("Token name") == ENV_TOKEN]
    assert len(env_rows) == 1, "ENV_RAILS_POLICY_OK should have exactly one row in the token matrix"
    env_row = env_rows[0]

    evidence_cells = {part.strip() for part in env_row["Evidence artifacts (titles / paths / artifact_keys)"].split(";") if part.strip()}
    assert evidence_cells == ENV_EXPECTED_EVIDENCE, "ENV_RAILS_POLICY_OK evidence should be concrete and include closed-rails refusal parity artifacts"
    assert not any("TBD" in entry or "{" in entry or "}" in entry for entry in evidence_cells), "ENV_RAILS_POLICY_OK evidence must not contain placeholders"

    test_cells = {part.strip() for part in env_row["CI jobs / tests (names or node ids)"].split(";") if part.strip()}
    assert ENV_EXPECTED_TESTS.issubset(test_cells), "ENV_RAILS_POLICY_OK tests should include the env pins gate and parity harness"


def test_env_rails_policy_acceptance_map_binding_is_concrete():
    data = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    tokens = data.get("tokens", [])
    env_entries = [token for token in tokens if token.get("name") == ENV_TOKEN]
    assert env_entries, "ENV_RAILS_POLICY_OK should be present in the acceptance map"
    env_entry = env_entries[0]

    evidence_titles = set(env_entry.get("evidence_titles", []))
    assert evidence_titles == ENV_EXPECTED_EVIDENCE, "Acceptance map should bind ENV_RAILS_POLICY_OK to concrete rails and closed-rails parity evidence"
    assert not any("TBD" in title or "{" in title or "}" in title for title in evidence_titles), "Acceptance map should not contain placeholder evidence for ENV_RAILS_POLICY_OK"


def test_cli_stdout_lf_token_is_unique_and_concrete():
    rows = _parse_matrix_rows()
    cli_rows = [row for row in rows if row.get("Token name") == CLI_STDOUT_TOKEN]
    assert len(cli_rows) == 1, "CLI_STDOUT_LF_OK should have exactly one row in the token matrix"
    row = cli_rows[0]

    evidence_cells = {part.strip() for part in row["Evidence artifacts (titles / paths / artifact_keys)"].split(";") if part.strip()}
    assert evidence_cells == CLI_STDOUT_EXPECTED_EVIDENCE, "CLI_STDOUT_LF_OK evidence should reference the canonical-bytes test and showcompat stdout artifacts"
    assert not any("TBD" in entry or "{" in entry or "}" in entry for entry in evidence_cells), "CLI_STDOUT_LF_OK evidence must not contain placeholders"

    test_cells = {part.strip() for part in row["CI jobs / tests (names or node ids)"].split(";") if part.strip()}
    assert CLI_STDOUT_EXPECTED_TESTS.issubset(test_cells), "CLI_STDOUT_LF_OK should anchor to the canonical-bytes test"


def test_cli_stdout_lf_acceptance_map_is_unique_and_artifacts_exist():
    data = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    tokens = [token for token in data.get("tokens", []) if token.get("name") == CLI_STDOUT_TOKEN]
    assert len(tokens) == 1, "CLI_STDOUT_LF_OK should appear exactly once in the acceptance map"
    entry = tokens[0]

    evidence_titles = set(entry.get("evidence_titles", []))
    assert evidence_titles == CLI_STDOUT_EXPECTED_EVIDENCE, "Acceptance map should bind CLI_STDOUT_LF_OK to the canonical-bytes test and showcompat stdout artifacts"
    assert not any("TBD" in title or "{" in title or "}" in title for title in evidence_titles), "CLI_STDOUT_LF_OK acceptance evidence must not contain placeholders"

    for path in CLI_STDOUT_EXPECTED_ARTIFACTS:
        assert path.is_file(), f"Expected CLI stdout artifact to exist: {path}"


def test_internal_version_and_identity_tokens_are_unique_and_concrete():
    rows = _parse_matrix_rows()
    matrix_index = {}
    for row in rows:
        matrix_index.setdefault(row.get("Token name"), []).append(row)

    acceptance_index = _load_acceptance_map_tokens()

    for token_name, expectation in D3_TOKEN_EXPECTATIONS.items():
        matrix_rows = matrix_index.get(token_name, [])
        assert len(matrix_rows) == 1, f"{token_name} should have exactly one row in the token matrix"
        matrix_row = matrix_rows[0]

        evidence_cells = {
            part.strip()
            for part in matrix_row["Evidence artifacts (titles / paths / artifact_keys)"].split(";")
            if part.strip()
        }
        assert evidence_cells == expectation["artifacts"], f"{token_name} evidence artifacts should be concrete and unique"
        assert not any("TBD" in cell or "{" in cell or "}" in cell for cell in evidence_cells), (
            f"{token_name} matrix evidence must not contain placeholders"
        )

        test_cells = {
            part.strip() for part in matrix_row["CI jobs / tests (names or node ids)"].split(";") if part.strip()
        }
        assert test_cells == expectation["tests"], f"{token_name} should list the expected contract tests"

        acceptance_rows = acceptance_index.get(token_name, [])
        assert len(acceptance_rows) == 1, f"{token_name} should appear exactly once in the acceptance map"
        acceptance_entry = acceptance_rows[0]

        evidence_titles = set(acceptance_entry.get("evidence_titles", []))
        expected_titles = expectation["artifacts"] | expectation["tests"]
        assert evidence_titles == expected_titles, f"{token_name} acceptance evidence should align with the token matrix"
        assert not any("TBD" in title or "{" in title or "}" in title for title in evidence_titles), (
            f"{token_name} acceptance evidence must not contain placeholders"
        )

        for artifact in expectation["artifacts"]:
            path = Path(artifact)
            assert path.is_file(), f"Expected artifact for {token_name} to exist: {path}"
