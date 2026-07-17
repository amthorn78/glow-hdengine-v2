from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from tools.evidence import run_sanity_pipeline as sanity


def _result(code=0):
    return subprocess.CompletedProcess([], code, "", "")


def test_exact_stage_order_and_canonical_path():
    assert tuple(step.name for step in sanity.default_steps()) == sanity.STAGE_NAMES
    assert len(sanity.STAGE_NAMES) == 17
    assert sanity.SANITY_LOG.relative_to(sanity.ROOT).as_posix() == "audit/gates/sanity_pipeline/sanity_pipeline.log"


def test_first_failure_is_fail_closed_and_later_stages_are_recorded(tmp_path, monkeypatch):
    steps = [sanity.SanityStep("one", ["one"]), sanity.SanityStep("two", ["two"]), sanity.SanityStep("three", ["three"])]
    calls = []
    def run(command):
        calls.append(command)
        return _result(7 if command[0] == "two" else 0)
    monkeypatch.setattr(sanity, "_run_command", run)
    log = tmp_path / "sanity.log"
    assert sanity.run_pipeline(log_path=log, steps=steps) == 7
    assert calls == [("one",), ("two",)]
    text = log.read_text()
    assert "check three:FAIL" in text
    assert "not_executed three:earlier_mandatory_failure=two" in text
    assert "first_failed_stage:two\nsummary:FAIL\n" in text


def test_pass_requires_every_stage_and_log_has_one_lf(tmp_path, monkeypatch):
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result())
    log = tmp_path / "sanity.log"
    assert sanity.run_pipeline(log_path=log, steps=[sanity.SanityStep("one", ["true"])]) == 0
    data = log.read_bytes()
    assert data.endswith(b"\n") and not data.endswith(b"\n\n")
    assert data.count(b"summary:PASS") == 1


def test_canonical_pass_is_written_before_finalizer_and_not_rewritten(tmp_path, monkeypatch):
    steps = [sanity.SanityStep("final", ["seal"])]
    log = tmp_path / "sanity.log"
    observed_during_finalizer = []
    writes = []
    original_write = sanity._write_log
    def write(path, results, first_failure, summary):
        writes.append((tuple(results), first_failure, summary))
        return original_write(path, results, first_failure, summary)
    def run(command):
        observed_during_finalizer.append(log.read_bytes())
        return _result()
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    monkeypatch.setattr(sanity, "default_steps", lambda: steps)
    monkeypatch.setattr(sanity, "_write_log", write)
    monkeypatch.setattr(sanity, "_run_command", run)
    assert sanity.run_pipeline(log_path=log) == 0
    expected = sanity._render_log([("final", "OK")], "NONE", "PASS")
    assert observed_during_finalizer == [expected]
    assert log.read_bytes() == expected
    assert writes == [((("final", "OK"),), "NONE", "PASS")]


def test_relative_canonical_log_path_uses_the_sealing_path(tmp_path, monkeypatch):
    relative = Path("audit/gates/sanity_pipeline/sanity_pipeline.log")
    canonical = tmp_path / relative
    steps = [sanity.SanityStep("final", ["seal"])]
    observed = []
    monkeypatch.setattr(sanity, "ROOT", tmp_path)
    monkeypatch.setattr(sanity, "SANITY_LOG", canonical)
    monkeypatch.setattr(sanity, "default_steps", lambda: steps)
    monkeypatch.setattr(sanity, "_run_command", lambda command: observed.append(canonical.read_bytes()) or _result())
    assert sanity.run_pipeline(log_path=relative) == 0
    expected = sanity._render_log([("final", "OK")], "NONE", "PASS")
    assert observed == [expected]
    assert canonical.read_bytes() == expected


def test_canonical_failure_bytes_are_rebound(tmp_path, monkeypatch):
    steps = [sanity.SanityStep("late", ["false"])]
    log = tmp_path / "sanity.log"
    rebound = []
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    monkeypatch.setattr(sanity, "default_steps", lambda: steps)
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result(1))
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda *, ops_validated: rebound.append(ops_validated) or 0)
    assert sanity.run_pipeline(log_path=log) == 1
    assert rebound == [False]
    assert log.read_text().endswith("first_failed_stage:late\nsummary:FAIL\n")


def test_canonical_failure_finalization_error_is_propagated(tmp_path, monkeypatch):
    steps = [sanity.SanityStep("late", ["false"])]
    log = tmp_path / "sanity.log"
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    monkeypatch.setattr(sanity, "default_steps", lambda: steps)
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result(1))
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda *, ops_validated: 9)
    assert sanity.run_pipeline(log_path=log) == 9
    assert log.read_text().endswith("first_failed_stage:late\nsummary:FAIL\n")


@pytest.mark.parametrize("ops_validated,extra", [
    (False, ("--exclude-epic038-pr06",)),
    (True, ()),
])
def test_failure_rebind_uses_only_canonical_updater(monkeypatch, ops_validated, extra):
    calls = []
    def run(command):
        calls.append(command)
        return _result()
    monkeypatch.setattr(sanity, "_run_command", run)
    assert sanity._rebind_failure_log(ops_validated=ops_validated) == 0
    assert calls == [(sanity.sys.executable, "tools/evidence/update_evidence_index.py", *extra)]


def test_ops_validation_failure_records_stage_and_stops(monkeypatch, tmp_path):
    steps = [
        sanity.SanityStep(sanity.STAGE_NAMES[11], (("__validate_ops__",),)),
        sanity.SanityStep(sanity.STAGE_NAMES[12], (("must-not-run",),)),
    ]
    monkeypatch.setattr(sanity, "validate_ops_packages", lambda: (_ for _ in ()).throw(ValueError("invalid OPS")))
    monkeypatch.setattr(sanity, "_run_command", lambda command: pytest.fail("later stage executed"))
    log = tmp_path / "sanity.log"
    assert sanity.run_pipeline(log_path=log, steps=steps) == 1
    text = log.read_text()
    assert f"check {sanity.STAGE_NAMES[11]}:FAIL" in text
    assert f"not_executed {sanity.STAGE_NAMES[12]}:earlier_mandatory_failure={sanity.STAGE_NAMES[11]}" in text


def _packet_copy(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    target = root / "audit/ops/hde-epic038"
    target.parent.mkdir(parents=True)
    shutil.copytree(sanity.ROOT / "audit/ops/hde-epic038", target)
    shutil.copytree(
        sanity.ROOT / "artifacts/bodygraph/v2_mapped_cache",
        root / "artifacts/bodygraph/v2_mapped_cache",
    )
    return root


@pytest.mark.parametrize("package,name", [("ops-01", "stdout.log"), ("ops-02", "request_summary.json")])
def test_missing_ops_file_fails(tmp_path, package, name):
    root = _packet_copy(tmp_path)
    (root / f"audit/ops/hde-epic038/{package}/{name}").unlink()
    with pytest.raises(ValueError, match=rf"{package}.*{name}"):
        sanity.validate_ops_packages(root)


def test_zero_byte_ops_file_fails(tmp_path):
    root = _packet_copy(tmp_path)
    (root / "audit/ops/hde-epic038/ops-02/stdout.log").write_bytes(b"")
    with pytest.raises(ValueError, match="stdout.log"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("name,contents,match", [
    ("debug.log", "benign diagnostic\n", "unexpected retained packet entry"),
    ("raw_response.json", "HD-Geocode-Key: live-secret\n", "unredacted vendor header"),
])
def test_unledgered_packet_files_are_never_accepted(tmp_path, name, contents, match):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    (packet / name).write_text(contents)
    with pytest.raises(ValueError, match=match):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("mutation,match", [
    ("malformed", "malformed row"), ("duplicate", "duplicate row"), ("mismatch", "mismatch for stdout.log")
])
def test_checksum_ledger_fails_closed(tmp_path, mutation, match):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    ledger = packet / "checksums.sha256"
    if mutation == "malformed":
        ledger.write_text("not a checksum\n")
    elif mutation == "duplicate":
        first = ledger.read_text().splitlines()[0]
        ledger.write_text(ledger.read_text() + first + "\n")
    else:
        (packet / "stdout.log").write_text("changed\n")
    with pytest.raises(ValueError, match=match):
        sanity.validate_ops_packages(root)


def test_non_ascii_checksum_ledger_fails_cleanly(tmp_path):
    root = _packet_copy(tmp_path)
    ledger = root / "audit/ops/hde-epic038/ops-01/checksums.sha256"
    ledger.write_bytes(b"\xff\n")
    with pytest.raises(ValueError, match="checksums.sha256 is not readable ASCII evidence"):
        sanity.validate_ops_packages(root)


def _refresh_ledger(packet: Path, name: str):
    lines = []
    for line in (packet / "checksums.sha256").read_text().splitlines():
        digest, current = line.split("  ")
        if current == name:
            digest = hashlib.sha256((packet / name).read_bytes()).hexdigest()
        lines.append(f"{digest}  {current}")
    (packet / "checksums.sha256").write_text("\n".join(lines) + "\n")


def _write_json_and_refresh(packet: Path, name: str, value: dict):
    (packet / name).write_text(json.dumps(value, separators=(",", ":")) + "\n")
    _refresh_ledger(packet, name)


@pytest.mark.parametrize("missing_name", sanity.OPS01_PARITY_ROWS)
def test_ops01_requires_every_exact_corpus_row(tmp_path, missing_name):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    parity = json.loads((packet / "provider_parity.proof.json").read_text())
    summary = json.loads((packet / "result_summary.json").read_text())
    parity["capabilities"] = [row for row in parity["capabilities"] if row["name"] != missing_name]
    parity["active_parity_corpus"]["ordered_rows"].remove(missing_name)
    summary["active_parity_rows"].remove(missing_name)
    count = len(sanity.OPS01_PARITY_ROWS) - 1
    parity["live_provider_parity"]["claimed_row_count"] = count
    parity["live_provider_parity"]["matched_row_count"] = count
    summary["observations"]["claimed_rows"] = count
    summary["observations"]["matched_rows"] = count
    _write_json_and_refresh(packet, "provider_parity.proof.json", parity)
    _write_json_and_refresh(packet, "result_summary.json", summary)
    with pytest.raises(ValueError, match="exact corpus"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("mutation", ["reordered", "duplicate", "renamed", "extra", "corpus-name"])
def test_ops01_rejects_noncanonical_corpus_variants(tmp_path, mutation):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    parity = json.loads((packet / "provider_parity.proof.json").read_text())
    summary = json.loads((packet / "result_summary.json").read_text())
    if mutation == "reordered":
        parity["capabilities"].reverse()
        parity["active_parity_corpus"]["ordered_rows"].reverse()
        summary["active_parity_rows"].reverse()
    elif mutation == "duplicate":
        parity["capabilities"].append(parity["capabilities"][-1])
        parity["active_parity_corpus"]["ordered_rows"].append(sanity.OPS01_PARITY_ROWS[-1])
        summary["active_parity_rows"].append(sanity.OPS01_PARITY_ROWS[-1])
    elif mutation in {"renamed", "extra"}:
        new_name = "renamed_row" if mutation == "renamed" else "extra_row"
        if mutation == "renamed":
            parity["capabilities"][-1]["name"] = new_name
            parity["active_parity_corpus"]["ordered_rows"][-1] = new_name
            summary["active_parity_rows"][-1] = new_name
        else:
            extra = dict(parity["capabilities"][-1]); extra["name"] = new_name
            parity["capabilities"].append(extra)
            parity["active_parity_corpus"]["ordered_rows"].append(new_name)
            summary["active_parity_rows"].append(new_name)
    else:
        parity["active_parity_corpus"]["name"] = "self_reported_replacement"
        summary["active_parity_corpus"] = "self_reported_replacement"
    count = len(parity["capabilities"])
    parity["live_provider_parity"]["claimed_row_count"] = count
    parity["live_provider_parity"]["matched_row_count"] = count
    summary["observations"]["claimed_rows"] = count
    summary["observations"]["matched_rows"] = count
    _write_json_and_refresh(packet, "provider_parity.proof.json", parity)
    _write_json_and_refresh(packet, "result_summary.json", summary)
    with pytest.raises(ValueError, match="exact corpus"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("field,value", [
    ("status", "FAIL"),
    ("observation_mode", "write_capable"),
    ("search_path_exact", False),
    ("boundary_views_readonly", False),
    ("partition_plan_status", "FAIL"),
])
def test_ops01_db_posture_primary_failures_are_rejected(tmp_path, field, value):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "db_posture_summary.json"; primary = json.loads(path.read_text())
    primary[field] = value
    _write_json_and_refresh(packet, path.name, primary)
    with pytest.raises(ValueError, match="db_posture_summary"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("mutation", [
    "status", "command-exit", "checker-exit", "checker-result",
    "comparator-exit", "comparator-result", "comparator-hash", "predicate",
])
def test_ops01_bridge_primary_failures_are_rejected(tmp_path, mutation):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "bridge_consistency.result.json"; primary = json.loads(path.read_text())
    if mutation == "status": primary["status"] = "FAIL"
    elif mutation == "command-exit": primary["command_exit_codes"]["canonical_comparison"] = 1
    elif mutation == "checker-exit": primary["governed_checker"]["exit_code"] = 1
    elif mutation == "checker-result": primary["governed_checker"]["result"] = "FAIL"
    elif mutation == "comparator-exit": primary["bodygraph_comparator"]["exit_code"] = 1
    elif mutation == "comparator-result": primary["bodygraph_comparator"]["result"] = "FILE_NE_CANON_BYTES"
    elif mutation == "comparator-hash": primary["bodygraph_comparator"]["canonical_sha256"] = "0" * 64
    else: primary["predicates"]["bodygraph_row_match"] = False
    _write_json_and_refresh(packet, path.name, primary)
    with pytest.raises(ValueError, match="bridge_consistency"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("package,mutation", [
    ("ops-01", "open-rails"),
    ("ops-01", "production-env"),
    ("ops-02", "closed-rails"),
    ("ops-02", "production-env"),
])
def test_ops_execution_rails_are_derived_from_env_presence(tmp_path, package, mutation):
    root = _packet_copy(tmp_path); packet = root / f"audit/ops/hde-epic038/{package}"
    path = packet / "env_presence.json"; value = json.loads(path.read_text())
    if package == "ops-01":
        if mutation == "open-rails": value["execution_rails"]["db_posture_capture"]["ALLOW_NETWORK"] = "1"
        else: value["environment_presence"]["APP_ENV"] = "SET:prod"
    else:
        if mutation == "closed-rails": value["environment_presence"]["SAFE_MODE"] = "1"
        else: value["environment_presence"]["APP_ENV"] = "SET:prod"
    _write_json_and_refresh(packet, path.name, value)
    with pytest.raises(ValueError, match="env_presence"):
        sanity.validate_ops_packages(root)


def test_unavailable_provider_row_is_not_pass(tmp_path):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "provider_parity.proof.json"; value = json.loads(path.read_text())
    value["capabilities"][0]["direct"]["status"] = "unavailable"
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="unavailable"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("row_name", sanity.OPS01_PARITY_ROWS)
def test_ops01_compares_provider_values_and_bodygraph_hashes(tmp_path, row_name):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "provider_parity.proof.json"; value = json.loads(path.read_text())
    row = next(item for item in value["capabilities"] if item["name"] == row_name)
    if row_name == "grants": row["direct"]["value"].append("postgres hde.body_graphs BOGUS")
    elif row_name == "search_path": row["direct"]["value"] = "public, hde"
    elif row_name == "select_one": row["direct"]["value"] = 2
    elif row_name == "ddl_fingerprint": row["direct"]["value"][0]["columns"][0]["data_type"] = "text"
    else: row["direct"]["canonical_sha256"] = "0" * 64
    _write_json_and_refresh(packet, path.name, value)
    with pytest.raises(ValueError, match="provider values|BodyGraph"):
        sanity.validate_ops_packages(root)


def test_malformed_provider_row_is_recorded_as_validation_failure(tmp_path):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "provider_parity.proof.json"; value = json.loads(path.read_text())
    value["capabilities"] = [None]
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="unavailable"):
        sanity.validate_ops_packages(root)


def test_ops02_predicate_failure_is_not_pass(tmp_path):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "result_summary.json"; value = json.loads(path.read_text())
    value["predicates"]["mapped_payload_only"] = False
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="predicate"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("package,field", [("ops-01", "observations"), ("ops-02", "predicates")])
def test_malformed_summary_nested_object_fails_cleanly(tmp_path, package, field):
    root = _packet_copy(tmp_path); packet = root / f"audit/ops/hde-epic038/{package}"
    path = packet / "result_summary.json"; value = json.loads(path.read_text())
    value[field] = None
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match=field):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("leak", [
    "HD_API_KEY=supersecret",
    "HD_API_KEY: live-secret",
    "GEO_API_KEY : live-secret",
    "Authorization: Bearer live-secret",
    "HD-Geocode-Key: live-geocode-secret",
    "HD-Api-Key: live-legacy-secret",
    "postgresql://user:password@host/database",
    '{"raw_vendor_payload":{"private":"value"}}',
])
def test_checksum_consistent_secret_or_raw_payload_is_rejected(tmp_path, leak):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"; path.write_text(leak + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="unredacted|raw request"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("safe_value", ["false", "null", '"redacted"', '"none"'])
def test_spaced_safe_raw_payload_values_are_allowed(tmp_path, safe_value):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"
    path.write_text(f'{{"raw_vendor_payload": {safe_value}}}\n')
    _refresh_ledger(packet, path.name)
    sanity.validate_ops_packages(root)


@pytest.mark.parametrize("safe_value", ["REDACTED", "<redacted>", "SET:REDACTED"])
def test_colon_delimited_redacted_credentials_are_allowed(tmp_path, safe_value):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"
    path.write_text(f"HD_API_KEY: {safe_value}\n")
    _refresh_ledger(packet, path.name)
    sanity.validate_ops_packages(root)


@pytest.mark.parametrize(
    "mutation",
    ["missing", "predicate", "nonclaim", "proof-bytes", "proof-ledger"],
)
def test_ops02_production_refusal_requires_independent_pr05_evidence(tmp_path, mutation):
    root = _packet_copy(tmp_path)
    path = root / "artifacts/bodygraph/v2_mapped_cache/manifest.json"
    if mutation == "missing":
        path.unlink()
    elif mutation == "proof-bytes":
        (root / "artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log").write_text(
            "PASS code=PROVIDER_REFUSED safe_mode=1 allow_network=1 vendor_calls=0 db_calls=0\n"
        )
    else:
        value = json.loads(path.read_text())
        if mutation == "predicate":
            value["predicates"]["production_like_refused"] = False
        elif mutation == "nonclaim":
            value["nonclaims"].remove("no_ops_execution")
        else:
            record = next(
                item
                for item in value["artifacts"]
                if item["path"].endswith("closed_rails_refusal.log")
            )
            record["sha256"] = "0" * 64
        path.write_text(json.dumps(value, separators=(",", ":")) + "\n")
    with pytest.raises(ValueError, match="production-like refusal"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("path_name,mutate,match", [
    ("request_summary.json", lambda value: value.update(vendor_requests=2), "request_summary"),
    ("mapped_output_summary.json", lambda value: value.update(raw_vendor_envelope_persisted=True), "mapped_output_summary"),
    ("read_back_summary.json", lambda value: value.update(read_back_match=False), "read_back_summary"),
])
def test_ops02_summary_predicates_are_derived_from_primary_evidence(tmp_path, path_name, mutate, match):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / path_name; value = json.loads(path.read_text()); mutate(value)
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match=match):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("source", ["request", "read-back"])
def test_ops02_identity_must_agree_across_request_summary_and_read_back(tmp_path, source):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    if source == "request":
        path = packet / "request_summary.json"; value = json.loads(path.read_text())
        value["input_fingerprint"] = "0" * 64
    else:
        path = packet / "read_back_summary.json"; value = json.loads(path.read_text())
        value["synthetic_user_id"] = "00000000-0000-4000-8000-000000000000"
    _write_json_and_refresh(packet, path.name, value)
    with pytest.raises(ValueError, match="identity disagreement"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("field,value", [
    ("route", "vendor.hdapi.post:/legacy"),
    ("resource_path", "legacy"),
    ("route_family", "legacy_bodygraph"),
    ("payload_family", "LegacyResponse"),
    ("geocode_required", False),
])
def test_ops02_requires_exact_configured_v2_route_metadata(tmp_path, field, value):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "request_summary.json"; request = json.loads(path.read_text())
    request[field] = value
    _write_json_and_refresh(packet, path.name, request)
    with pytest.raises(ValueError, match="request_summary"):
        sanity.validate_ops_packages(root)


def test_ops02_failed_lower_level_log_is_rejected(tmp_path):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "canonical_parity.log"; path.write_text("FAIL pre_write_post_read_match=false\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="canonical_parity"):
        sanity.validate_ops_packages(root)


def test_ops_validation_never_executes_commands(monkeypatch):
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: pytest.fail("OPS command executed"))
    sanity.validate_ops_packages()


def test_current_commands_and_exact_proof_paths_are_wired():
    commands = [command for step in sanity.default_steps() for command in step.commands]
    assert (sanity.sys.executable, "scripts/release_id_recompute.py", "--check") in commands
    assert (sanity.sys.executable, "ci/checks/check_release_identity.sh") in commands
    assert (sanity.sys.executable, "tools/evidence/generate_open_rails_abba_proof.py", "--check") in commands
    assert (sanity.sys.executable, "tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check") in commands
    updater = (sanity.ROOT / "tools/evidence/update_evidence_index.py").read_text()
    assert "artifacts/vendor/rails_gate_keys_only.logs.sample" in updater
    assert "artifacts/cards/a3/IDENTITY_OK.txt" in updater
    assert (sanity.ROOT / "artifacts/db/boundary_view.readonly.proof.txt").is_file()
    assert (sanity.ROOT / "artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt").is_file()


def test_wrapper_has_no_legacy_writer_or_epic024_identity():
    text = (sanity.ROOT / "tools/evidence/run_sanity_pipeline_gate.py").read_text()
    assert "D07_sanity_pipeline" not in text
    assert "hde-epic024" not in text
    assert "_write_path_proof" not in text
    from tools.evidence import update_evidence_index
    entries = update_evidence_index._load_human_index()
    sanity_paths = {entry["discovered_physical_path"] for entry in entries if entry["artifact_key"] == "sanity.pipeline.log"}
    assert sanity_paths == {"audit/gates/sanity_pipeline/sanity_pipeline.log"}


def test_failure_index_mode_excludes_unvalidated_pr06_ops():
    from tools.evidence import update_evidence_index
    included = update_evidence_index._load_human_index()
    excluded = update_evidence_index._load_human_index(include_epic038_pr06=False)
    assert any(str(entry["artifact_key"]).startswith("epic038.pr06.") for entry in included)
    assert not any(str(entry["artifact_key"]).startswith("epic038.pr06.") for entry in excluded)


def test_canonical_updater_owns_legacy_sanity_compatibility_mirror(tmp_path, monkeypatch):
    from tools.evidence import update_evidence_index

    canonical = tmp_path / "audit/gates/sanity_pipeline/sanity_pipeline.log"
    legacy = tmp_path / "artifacts/sanity/sanity.log"
    canonical.parent.mkdir(parents=True)
    legacy.parent.mkdir(parents=True)
    canonical_bytes = b"run:sanity-pipeline\nsummary:PASS\n"
    canonical.write_bytes(canonical_bytes)
    legacy.write_bytes(b"stale legacy bytes\n")
    Path(f"{legacy}.path_proof.txt").write_text(
        "path: artifacts/sanity/sanity.log\n"
        "size_bytes: 19\n"
        f"sha256: {hashlib.sha256(legacy.read_bytes()).hexdigest()}\n"
        "mtime_utc: 2025-01-01T00:00:00Z\n"
        "produced_at_utc: 2025-01-01T00:00:00Z\n"
    )

    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)
    monkeypatch.setattr(update_evidence_index, "CANONICAL_SANITY_LOG", canonical)
    monkeypatch.setattr(update_evidence_index, "LEGACY_SANITY_LOG", legacy)

    update_evidence_index._sync_legacy_sanity_compatibility(
        default_produced_at="2026-07-17T00:00:00Z",
        check=False,
    )
    assert legacy.read_bytes() == canonical_bytes

    proof = {}
    for line in Path(f"{legacy}.path_proof.txt").read_text(encoding="utf-8").splitlines():
        key, value = line.split(":", 1)
        proof[key.strip()] = value.strip()
    assert proof["path"] == "artifacts/sanity/sanity.log"
    assert proof["size_bytes"] == str(len(canonical_bytes))
    assert proof["sha256"] == hashlib.sha256(canonical_bytes).hexdigest()
    assert proof["produced_at_utc"] == "2026-07-17T00:00:00Z"

    update_evidence_index._sync_legacy_sanity_compatibility(
        default_produced_at="2026-07-17T00:00:00Z",
        check=True,
    )
    legacy.write_bytes(b"drift\n")
    with pytest.raises(SystemExit, match="STALE"):
        update_evidence_index._sync_legacy_sanity_compatibility(
            default_produced_at="2026-07-17T00:00:00Z",
            check=True,
        )
