from __future__ import annotations

import hashlib
import datetime as _dt
import json

import pytest
from pathlib import Path

from tools.evidence import update_evidence_index
from tools.qa import epic021_qa


COMPAT_TARGETS = [
    ("compat.conjunction.identity_hash", "artifacts/compat/identity_hash.txt"),
]

REPO_TARGETS = [
    ("db_bridge.adapter_selection.snapshot", "artifacts/db_bridge/adapter_selection.snapshot.json"),
    ("db_bridge.health", "artifacts/db_bridge/health.json"),
    ("db_bridge.root", "artifacts/db_bridge/root.json"),
    ("db_bridge.query_select_1", "artifacts/db_bridge/query_select_1.json"),
    ("db.introspect.search_path", "artifacts/db/introspect.search_path.json"),
    ("db.introspect.grants", "artifacts/db/introspect.grants.json"),
    ("db.introspect.fingerprint", "artifacts/db/introspect.fingerprint.json"),
    ("engine.db_adapter.version", "artifacts/engine/db_adapter.version.json"),
    ("engine.db_adapter.search_path", "artifacts/engine/db_adapter.search_path.json"),
    ("engine.db_adapter.fingerprint", "artifacts/engine/db_adapter.fingerprint.json"),
    ("logs.keys_only.sample", "artifacts/logs/keys_only.sample.jsonl"),
    ("ops.rails_open_scope", "artifacts/ops/rails_open_scope.txt"),
    ("cli.showcompat.ab", "artifacts/cli/ab.json"),
    ("cli.showcompat.ba", "artifacts/cli/ba.json"),
    ("cli.showcompat.summary", "artifacts/cli/summary.json"),
    ("cli.help.hdctl", "artifacts/cli/help/hdctl_help.txt"),
    ("cli.help.showcompat", "artifacts/cli/help/showcompat_help.txt"),
    ("cli.help.reject_nonjson", "artifacts/cli/help/reject_nonjson.txt"),
    ("cli.install.entrypoints", "artifacts/cli/install/entrypoints.txt"),
    ("cli.install.installability_summary", "artifacts/cli/install/installability_summary.json"),
    ("cli.guard.serializer_grep", "artifacts/cli/guards/serializer_grep_guard.log"),
    ("cli.guard.emitter_symbol_proof", "artifacts/cli/guards/emitter_symbol_proof.txt"),
    ("cli.showcompat.reader_cli_parity", "artifacts/cli/reader_cli_parity.bytes"),
]

EPIC029_TARGETS = [
    ("epic029.acceptance_map", "docs/acceptance_map_epic029.json"),
    (
        "epic029.token_matrix",
        "audit/qa/hde-epic029/token_evidence_matrix.md",
    ),
    (
        "epic029.acceptance_map_viability",
        "audit/qa/hde-epic029/acceptance_map_viability.log",
    ),
    (
        "epic029.qa_step_logs_manifest",
        "audit/qa/hde-epic029/qa_step_logs_manifest.json",
    ),
    ("epic029.close_report", "audit/EPIC-029_close_report.md"),
    ("epic029.manifest", "audit/EPIC-029_MANIFEST.json"),
    (
        "audit.qa.hde_epic029.checks.acceptance_map_viability.primary.log",
        "audit/qa/hde-epic029/checks/acceptance-map-viability/primary.log",
    ),
    (
        "audit.qa.hde_epic029.checks.po_epic_close_live_qa.primary.log",
        "audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log",
    ),
    (
        "audit.qa.hde_epic029.checks.po_precommit.primary.log",
        "audit/qa/hde-epic029/checks/po-precommit/primary.log",
    ),
    (
        "audit.qa.hde_epic029.checks.po_postcommit.primary.log",
        "audit/qa/hde-epic029/checks/po-postcommit/primary.log",
    ),
]

EPIC027_TARGETS = [
    ("epic027.acceptance_map", "docs/acceptance_map_epic027.json"),
    (
        "epic027.token_matrix",
        "audit/qa/hde-epic027/token_evidence_matrix.md",
    ),
    (
        "epic027.acceptance_map_viability",
        "audit/qa/hde-epic027/acceptance_map_viability.log",
    ),
    (
        "epic027.qa_step_logs_manifest",
        "audit/qa/hde-epic027/qa_step_logs_manifest.json",
    ),
    (
        "epic027.doc_deltas",
        "audit/qa/hde-epic027/00_meta/doc_deltas.md",
    ),
    ("epic027.close_report", "audit/EPIC-027_close_report.md"),
    ("epic027.manifest", "audit/EPIC-027_MANIFEST.json"),
]

EPIC021_TARGETS = [
    ("epic021.acceptance_map", "docs/acceptance_map_epic021.json"),
    (
        "epic021.token_matrix",
        "audit/qa/hde-epic021/token_evidence_matrix.md",
    ),
    (
        "epic021.acceptance_map_viability",
        "audit/qa/hde-epic021/acceptance_map_viability.log",
    ),
    (
        "epic021.qa_step_logs_manifest",
        "audit/qa/hde-epic021/qa_step_logs_manifest.json",
    ),
    (
        "epic021.doc_deltas",
        "audit/docdeltas/hde-epic021_doc_deltas.md",
    ),
    (
        "epic021.doc_delta_capture",
        "audit/qa/hde-epic021/00_meta/doc_deltas.md",
    ),
    (
        "epic021.qa_readme",
        "audit/qa/hde-epic021/README.md",
    ),
    ("epic021.close_report", "audit/EPIC-021_close_report.md"),
    ("epic021.manifest", "audit/EPIC-021_MANIFEST.json"),
    (
        "audit.qa.hde_epic021.checks.d00_bootstrap.primary.log",
        "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log",
    ),
    (
        "audit.qa.hde_epic021.checks.po_epic021_live_qa.primary.log",
        "audit/qa/hde-epic021/checks/po-epic021-live-qa/primary.log",
    ),
    (
        "audit.qa.hde_epic021.checks.bootstrap_tooling_classification.primary.log",
        "audit/qa/hde-epic021/checks/bootstrap-tooling-classification/primary.log",
    ),
    (
        "epic021.bootstrap_tooling_failure",
        "audit/qa/hde-epic021/00_meta/bootstrap_tooling_failure.log",
    ),
    (
        "audit.qa.hde_epic021.checks.po_precommit.primary.log",
        "audit/qa/hde-epic021/checks/po-precommit/primary.log",
    ),
    (
        "audit.qa.hde_epic021.checks.po_postcommit.primary.log",
        "audit/qa/hde-epic021/checks/po-postcommit/primary.log",
    ),
    (
        "audit.qa.hde_epic021.checks.acceptance_map_viability.primary.log",
        "audit/qa/hde-epic021/checks/acceptance-map-viability/primary.log",
    ),
]


def _assert_targets_present(targets):
    idx_path = Path("docs/evidence/INDEX.json")
    idx_entries = json.loads(idx_path.read_text(encoding="utf-8"))
    assert isinstance(idx_entries, list)

    entries_by_path = {entry["discovered_physical_path"]: entry for entry in idx_entries}

    for key, path in targets:
        assert path in entries_by_path, f"missing {path} in INDEX.json"
        entry = entries_by_path[path]
        assert entry.get("artifact_key") == key
        expected_proof = Path(f"{path}.path_proof.txt")
        assert expected_proof.exists()
        proof_data = update_evidence_index._load_existing_proof(expected_proof)
        assert proof_data.get("path") == path
        assert "mtime_utc" in proof_data
        assert "produced_at_utc" in proof_data
        parsed_mtime = _dt.datetime.fromisoformat(proof_data["mtime_utc"].replace("Z", "+00:00"))
        assert parsed_mtime.tzinfo == _dt.timezone.utc
        assert parsed_mtime.microsecond == 0
        parsed_produced = _dt.datetime.fromisoformat(
            proof_data["produced_at_utc"].replace("Z", "+00:00")
        )
        assert parsed_produced.tzinfo == _dt.timezone.utc
        assert parsed_produced.microsecond == 0

    mirror_path = Path("artifacts/evidence_index.jsonl")
    records = {}
    for line in mirror_path.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        records[(rec["artifact_key"], rec["discovered_physical_path"])] = rec

    for key, path in targets:
        assert (key, path) in records, f"missing {key} in evidence_index.jsonl"
        rec = records[(key, path)]
        expected_proof = f"{path}.path_proof.txt"
        assert rec.get("proof_anchor") == expected_proof
        sha = hashlib.sha256(Path(path).read_bytes()).hexdigest()
        assert rec.get("sha256") == sha
        assert rec.get("size_bytes") == Path(path).stat().st_size


def test_evidence_index_has_required_compat_artifacts():
    _assert_targets_present(COMPAT_TARGETS)


def test_evidence_index_has_required_repo_artifacts():
    _assert_targets_present(REPO_TARGETS)


def test_evidence_index_has_required_epic021_artifacts():
    _assert_targets_present(EPIC021_TARGETS)


def test_evidence_index_has_required_epic027_artifacts():
    _assert_targets_present(EPIC027_TARGETS)


def test_epic029_primary_roster_matches_canonical_bindings():
    roster = update_evidence_index.EPIC029_PRIMARY_ARTIFACTS
    actual = [
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in roster
    ]

    assert actual == EPIC029_TARGETS
    assert {entry["epic_id"] for entry in roster} == {"HDE-EPIC029"}
    assert len({key for key, _ in actual}) == len(actual)
    assert len({path for _, path in actual}) == len(actual)


def test_epic027_primary_roster_matches_canonical_bindings():
    roster = update_evidence_index.EPIC027_PRIMARY_ARTIFACTS
    actual = [
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in roster
    ]

    assert actual == EPIC027_TARGETS
    assert {entry["epic_id"] for entry in roster} == {"HDE-EPIC027"}
    assert len({key for key, _ in actual}) == len(actual)
    assert len({path for _, path in actual}) == len(actual)


def test_epic021_primary_roster_matches_canonical_bindings():
    roster = update_evidence_index.EPIC021_PRIMARY_ARTIFACTS
    actual = [
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in roster
    ]

    assert actual == EPIC021_TARGETS
    assert {entry["epic_id"] for entry in roster} == {"HDE-EPIC021"}
    assert len({key for key, _ in actual}) == len(actual)
    assert len({path for _, path in actual}) == len(actual)
    indexed_tokens = {
        token for entry in roster for token in entry.get("tokens", [])
    }
    assert indexed_tokens == {token["name"] for token in epic021_qa.TOKENS}


def test_epic021_roster_flows_to_human_index_loader():
    loaded = {
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in update_evidence_index._load_human_index()
    }

    assert set(EPIC021_TARGETS) <= loaded


def test_epic021_superseded_uppercase_bootstrap_is_not_currently_indexed():
    loaded = {
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in update_evidence_index._load_human_index()
    }

    assert not (update_evidence_index.EPIC021_SUPERSEDED_INDEX_KEYS & loaded)
    assert (
        "audit.qa.hde_epic021.checks.d00_bootstrap.primary.log",
        "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log",
    ) in loaded


def test_epic029_roster_flows_to_human_and_machine_renderers(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
):
    loaded = {
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in update_evidence_index._load_human_index()
    }
    assert set(EPIC029_TARGETS) <= loaded

    mirror_path = tmp_path / update_evidence_index.MIRROR_REL
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)
    monkeypatch.setattr(update_evidence_index, "MIRROR_PATH", mirror_path)
    monkeypatch.setattr(update_evidence_index, "_load_mirror_roles", lambda: {})
    monkeypatch.setattr(update_evidence_index, "_read_bytes", lambda _path: b"fixture\n")
    monkeypatch.setattr(update_evidence_index, "_size_bytes", lambda _path: 8)

    proof_requests = []

    def record_proof(rel, **_kwargs):
        proof_requests.append(rel)
        return f"{rel}.path_proof.txt", "2026-08-18T00:00:00Z"

    monkeypatch.setattr(update_evidence_index, "_write_path_proof", record_proof)
    entries = [
        {
            "artifact_key": "index.machine_mirror",
            "discovered_physical_path": update_evidence_index.MIRROR_REL,
        },
        *update_evidence_index.EPIC029_PRIMARY_ARTIFACTS,
    ]

    rendered, _ = update_evidence_index._render_mirror(
        entries,
        produced_default="2026-08-18T00:00:00Z",
        check=True,
    )
    records = [json.loads(line) for line in rendered.splitlines()]
    by_lookup = {
        (record["artifact_key"], record["discovered_physical_path"]): record
        for record in records
    }

    assert set(EPIC029_TARGETS) <= by_lookup.keys()
    assert proof_requests == [path for _, path in EPIC029_TARGETS]
    for key, path in EPIC029_TARGETS:
        assert by_lookup[(key, path)]["proof_anchor"] == f"{path}.path_proof.txt"


def test_historical_bridge_inventory_is_nonclaiming_in_both_indexes():
    expected_paths = update_evidence_index.HISTORICAL_BRIDGE_PRIMARY_PATHS
    human = json.loads(Path("docs/evidence/INDEX.json").read_text(encoding="utf-8"))
    mirror = [
        json.loads(line)
        for line in Path("artifacts/evidence_index.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]

    for records in (human, mirror):
        selected = [
            record
            for record in records
            if record.get("discovered_physical_path") in expected_paths
        ]
        assert {record["discovered_physical_path"] for record in selected} == expected_paths
        assert len(selected) == len(expected_paths)
        for record in selected:
            assert record["record_type"] == "historical_bridge_evidence"
            assert record["notes"] == update_evidence_index.HISTORICAL_BRIDGE_NOTES
            assert "tokens" not in record


def test_historical_bridge_normalization_strips_current_claims():
    normalized = update_evidence_index._normalize_index_entry(
        {
            "artifact_key": "bridge",
            "discovered_physical_path": next(
                iter(update_evidence_index.HISTORICAL_BRIDGE_PRIMARY_PATHS)
            ),
            "record_type": "current_bridge",
            "tokens": ["CURRENT_BRIDGE_OK"],
            "notes": "current provider fallback",
        }
    )

    assert normalized["record_type"] == "historical_bridge_evidence"
    assert normalized["notes"] == update_evidence_index.HISTORICAL_BRIDGE_NOTES
    assert "tokens" not in normalized


def _write_epic038_live_proof(
    root: Path,
    *,
    generated_at_utc: object = "2026-07-27T23:38:12Z",
    top_level_pass: bool = True,
) -> None:
    path = root / "audit/gates/determinism/open_rails_vendor_abba.json"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps(
            {
                "acceptance_token_satisfied": False,
                "artifact_kind": "hde_epic038_pr03_open_rails_vendor_abba_proof",
                "generated_at_utc": generated_at_utc,
                "result": "pass",
                "top_level_pass": top_level_pass,
            }
        )
        + "\n",
        encoding="utf-8",
    )


def test_epic038_live_index_entry_uses_current_artifact_timestamp(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    _write_epic038_live_proof(tmp_path)
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)

    entries = update_evidence_index._load_epic038_pr03_entries()
    by_key = {entry["artifact_key"]: entry for entry in entries}

    assert by_key["epic038.pr03.open_rails_vendor_abba"]["produced_at_utc"] == "2026-07-27T23:38:12Z"
    assert by_key["epic038.pr03.open_rails_abba"]["produced_at_utc"] == "2026-07-14T00:00:00Z"


def test_epic038_live_index_entry_is_omitted_when_conditional_artifact_absent(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)

    entries = update_evidence_index._load_epic038_pr03_entries()

    assert "epic038.pr03.open_rails_vendor_abba" not in {
        entry["artifact_key"] for entry in entries
    }


@pytest.mark.parametrize(
    "generated_at_utc,top_level_pass,expected",
    [
        ("2026-07-27", True, "INVALID_EPIC038_PR03_LIVE_PROOF_TIMESTAMP"),
        ("2026-07-27T23:38:12Z", False, "INVALID_EPIC038_PR03_LIVE_PROOF_POSTURE"),
    ],
)
def test_epic038_live_index_entry_rejects_invalid_provenance(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    generated_at_utc: object,
    top_level_pass: bool,
    expected: str,
) -> None:
    _write_epic038_live_proof(
        tmp_path,
        generated_at_utc=generated_at_utc,
        top_level_pass=top_level_pass,
    )
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)

    with pytest.raises(SystemExit, match=expected):
        update_evidence_index._load_epic038_pr03_entries()


def test_write_if_changed_check_mode_fails_closed_for_missing_target(tmp_path: Path):
    target = tmp_path / "missing.sha256"
    with pytest.raises(SystemExit, match=rf"^STALE:{target}$"):
        update_evidence_index._write_if_changed(target, b"abc\n", check=True)
    assert not target.exists()
