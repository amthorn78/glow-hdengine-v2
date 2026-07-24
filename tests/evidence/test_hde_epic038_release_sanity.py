from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from tools.evidence import run_sanity_pipeline as sanity


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in sanity.DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)


def _result(code: int = 0) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], code, "", "")


def _canonical(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
        + "\n"
    ).encode("utf-8")


def _refresh_ledger(packet: Path, name: str) -> None:
    lines = []
    for line in (packet / "checksums.sha256").read_text(encoding="ascii").splitlines():
        digest, current = line.split("  ")
        if current == name:
            digest = hashlib.sha256((packet / name).read_bytes()).hexdigest()
        lines.append(f"{digest}  {current}")
    (packet / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="ascii")


def _write_json_and_refresh(packet: Path, name: str, value: dict) -> None:
    (packet / name).write_bytes(_canonical(value))
    _refresh_ledger(packet, name)


def _packet_copy(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    target = root / "audit/ops/hde-epic038"
    target.parent.mkdir(parents=True)
    shutil.copytree(sanity.ROOT / "audit/ops/hde-epic038", target)
    shutil.copytree(
        sanity.ROOT / "artifacts/bodygraph/v2_mapped_cache",
        root / "artifacts/bodygraph/v2_mapped_cache",
    )
    for relative in sanity.HISTORICAL_BRIDGE_PRIMARY_SHA256:
        for path in (relative, f"{relative}.path_proof.txt"):
            target_path = root / path
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(sanity.ROOT / path, target_path)
    return root


def _pin_changed_historical_ledger(
    monkeypatch: pytest.MonkeyPatch, packet: Path, *changed_names: str
) -> None:
    for name in (*changed_names, "checksums.sha256"):
        proof = packet / f"{name}.path_proof.txt"
        digest = hashlib.sha256((packet / name).read_bytes()).hexdigest()
        size = (packet / name).stat().st_size
        proof.write_text(
            "".join(
                f"sha256: {digest}\n"
                if line.startswith("sha256: ")
                else f"size_bytes: {size}\n"
                if line.startswith("size_bytes: ")
                else line
                for line in proof.read_text(encoding="utf-8").splitlines(keepends=True)
            ),
            encoding="utf-8",
        )
    monkeypatch.setattr(
        sanity,
        "HISTORICAL_OPS01_LEDGER_SHA256",
        hashlib.sha256((packet / "checksums.sha256").read_bytes()).hexdigest(),
    )


def test_exact_19_stage_order_and_canonical_path():
    assert tuple(step.name for step in sanity.default_steps()) == sanity.STAGE_NAMES
    assert len(sanity.STAGE_NAMES) == 19
    assert sanity.STAGE_NAMES[6:14] == (
        "07 Direct DB selection contract",
        "08 Direct DB posture artifacts",
        "09 BodyGraph policy",
        "10 Architecture snapshot",
        "11 Configured-v2 mapped-cache local evidence",
        "12 Historical bridge evidence integrity",
        "13 OPS-02 mapped-cache packet validation",
        "14 OPS-03 direct DB posture packet validation",
    )
    assert (
        sanity.SANITY_LOG.relative_to(sanity.ROOT).as_posix()
        == "audit/gates/sanity_pipeline/sanity_pipeline.log"
    )


def test_pipeline_has_separate_direct_historical_ops02_and_ops03_validators():
    steps = sanity.default_steps()
    assert steps[6].commands[0] == ("__validate_direct_selection__",)
    assert steps[11].commands == (("__validate_historical_ops01__",),)
    assert steps[12].commands == (("__validate_ops02__",),)
    assert steps[13].commands == (("__validate_ops03__",),)
    assert all("__validate_ops__" not in step.commands for step in steps)


def test_pre_ops_pipeline_consumes_prebuilt_artifacts_without_repairing_them():
    write_capable_generators = {
        "tools/config/generate_config_artifacts.py",
        "tools/config/generate_bundles.py",
        "tools/evidence/generate_identity_provenance.py",
        "tools/evidence/generate_release_bindings.py",
        "tools/evidence/generate_env_matrix_snapshot.py",
        "tools/evidence/generate_determinism_gate_proofs.py",
        "tools/evidence/generate_open_rails_abba_proof.py",
        "tools/evidence/generate_a7_transport_proofs.py",
        "tools/evidence/generate_rails_gate_evidence.py",
        "tools/evidence/generate_db_runtime_posture.py",
        "tools/evidence/generate_bodygraph_policy_proofs.py",
        "tools/evidence/generate_architecture_snapshot.py",
        "tools/evidence/generate_v2_mapped_cache_evidence.py",
    }
    for step in sanity.default_steps()[:11]:
        for command in step.commands:
            scripts = write_capable_generators.intersection(command)
            if scripts:
                assert "--check" in command or "--check-only" in command


def test_pipeline_checks_prebuilt_orientation_without_post_seal_write():
    commands = [command for step in sanity.default_steps() for command in step.commands]
    updater = (sanity.sys.executable, "tools/evidence/update_evidence_index.py")
    updater_check = (*updater, "--check")
    orientation = (sanity.sys.executable, "tools/evidence/orientation_demo.py")
    orientation_check = (*orientation, "--check")
    assert commands.count(updater) == 1
    assert commands.count(updater_check) == 1
    assert commands.count(orientation) == 0
    assert commands.count(orientation_check) == 1
    assert commands.index(updater) < commands.index(updater_check)
    assert commands.index(updater_check) < commands.index(orientation_check)


def test_first_failure_is_fail_closed_and_later_stages_are_recorded(
    tmp_path, monkeypatch
):
    steps = [
        sanity.SanityStep("one", ["one"]),
        sanity.SanityStep("two", ["two"]),
        sanity.SanityStep("three", ["three"]),
    ]
    calls = []

    def run(command):
        calls.append(command)
        return _result(7 if command[0] == "two" else 0)

    monkeypatch.setattr(sanity, "_run_command", run)
    log = tmp_path / "sanity.log"
    assert sanity.run_pipeline(log_path=log, steps=steps) == 7
    assert calls == [("one",), ("two",)]
    text = log.read_text(encoding="utf-8")
    assert "check three:FAIL" in text
    assert "not_executed three:earlier_mandatory_failure=two" in text
    assert "first_failed_stage:two\nsummary:FAIL\n" in text


def test_custom_pipeline_pass_requires_every_stage_and_exact_final_lf(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result())
    log = tmp_path / "sanity.log"
    assert (
        sanity.run_pipeline(
            log_path=log, steps=[sanity.SanityStep("one", ["true"])]
        )
        == 0
    )
    data = log.read_bytes()
    assert data.endswith(b"\n") and not data.endswith(b"\n\n")
    assert data.count(b"summary:PASS") == 1


def test_canonical_pass_is_sealed_once_and_not_rewritten(tmp_path, monkeypatch):
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
    monkeypatch.setattr(
        sanity,
        "_run_command",
        lambda command: observed.append(canonical.read_bytes()) or _result(),
    )
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
    monkeypatch.setattr(
        sanity, "_rebind_failure_log", lambda: rebound.append("called") or 0
    )
    assert sanity.run_pipeline(log_path=log) == 1
    assert rebound == ["called"]
    assert log.read_text(encoding="utf-8").endswith(
        "first_failed_stage:late\nsummary:FAIL\n"
    )


def test_final_pass_does_not_rebind_failure_receipt(tmp_path, monkeypatch):
    log = tmp_path / "sanity.log"
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    _mock_pre_ops_success(monkeypatch)
    monkeypatch.setattr(sanity, "validate_ops03_tracked_packet", lambda: None)
    monkeypatch.setattr(
        sanity,
        "_rebind_failure_log",
        lambda: (_ for _ in ()).throw(AssertionError("failure receipt rebound")),
    )

    assert sanity.run_pipeline(log_path=log) == 0
    assert log.read_bytes() == _final_pass_log()


def test_canonical_failure_finalization_error_is_propagated(tmp_path, monkeypatch):
    steps = [sanity.SanityStep("late", ["false"])]
    log = tmp_path / "sanity.log"
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    monkeypatch.setattr(sanity, "default_steps", lambda: steps)
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result(1))
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda: 9)
    assert sanity.run_pipeline(log_path=log) == 9
    assert log.read_text(encoding="utf-8").endswith(
        "first_failed_stage:late\nsummary:FAIL\n"
    )


def _mock_pre_ops_success(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result())
    monkeypatch.setattr(sanity, "validate_pr05_path_proof_prerequisites", lambda: None)
    monkeypatch.setattr(sanity, "validate_direct_selection_contract", lambda: None)
    monkeypatch.setattr(sanity, "validate_historical_bridge_evidence", lambda: None)
    monkeypatch.setattr(sanity, "validate_ops02_package", lambda: None)


def test_pr_a_natural_stage14_missing_ops03_failure_stops_stages15_to19(
    tmp_path, monkeypatch
):
    log = tmp_path / "sanity.log"
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    _mock_pre_ops_success(monkeypatch)
    monkeypatch.setattr(
        sanity,
        "validate_ops03_tracked_packet",
        lambda: (_ for _ in ()).throw(
            sanity.Ops03PacketUnavailable(sanity.PR_A_NONFINAL_REASON)
        ),
    )
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda: 0)

    assert sanity.run_pipeline(log_path=log) == sanity.PR_A_NONFINAL_EXIT
    lines = log.read_text(encoding="utf-8").splitlines()
    assert [line for line in lines if line.startswith("check ")] == [
        f"check {name}:{'OK' if index < 13 else 'FAIL'}"
        for index, name in enumerate(sanity.STAGE_NAMES)
    ]
    for name in sanity.STAGE_NAMES[14:]:
        assert (
            f"not_executed {name}:earlier_mandatory_failure={sanity.STAGE_NAMES[13]}"
            in lines
        )
    assert f"first_failed_stage:{sanity.STAGE_NAMES[13]}" in lines
    assert "summary:FAIL" in lines
    assert "summary:PASS" not in lines


def test_pr_a_never_writes_prospective_pass_before_stage14(
    tmp_path, monkeypatch
):
    log = tmp_path / "sanity.log"
    summaries: list[str] = []
    original_write = sanity._write_log
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    _mock_pre_ops_success(monkeypatch)
    monkeypatch.setattr(
        sanity,
        "validate_ops03_tracked_packet",
        lambda: (_ for _ in ()).throw(
            sanity.Ops03PacketUnavailable(sanity.PR_A_NONFINAL_REASON)
        ),
    )
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda: 0)

    def write(path, results, first_failure, summary):
        summaries.append(summary)
        return original_write(path, results, first_failure, summary)

    monkeypatch.setattr(sanity, "_write_log", write)
    assert sanity.run_pipeline(log_path=log) == sanity.PR_A_NONFINAL_EXIT
    assert summaries == ["FAIL"]
    assert b"summary:PASS" not in log.read_bytes()


@pytest.mark.parametrize(
    ("seal_code", "expected"),
    ((0, sanity.PR_A_NONFINAL_EXIT), (1, 1), (sanity.PR_A_NONFINAL_EXIT, 1)),
)
def test_pr_a_nonfinal_exit_requires_successful_failure_rebind(
    tmp_path, monkeypatch, seal_code, expected
):
    log = tmp_path / "sanity.log"
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    _mock_pre_ops_success(monkeypatch)
    monkeypatch.setattr(
        sanity,
        "validate_ops03_tracked_packet",
        lambda: (_ for _ in ()).throw(
            sanity.Ops03PacketUnavailable(sanity.PR_A_NONFINAL_REASON)
        ),
    )
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda: seal_code)
    assert sanity.run_pipeline(log_path=log) == expected
    assert log.read_text(encoding="utf-8").endswith(
        f"first_failed_stage:{sanity.STAGE_NAMES[13]}\nsummary:FAIL\n"
    )


def test_failure_rebind_uses_only_targeted_canonical_updater(monkeypatch):
    calls = []

    def run(command):
        calls.append(command)
        return _result()

    monkeypatch.setattr(sanity, "_run_command", run)
    assert sanity._rebind_failure_log() == 0
    assert calls == [
        (
            sanity.sys.executable,
            "tools/evidence/update_evidence_index.py",
            "--rebind-sanity-log",
        )
    ]


def test_direct_selection_validation_failure_stops_before_static_checker(monkeypatch):
    step = sanity.default_steps()[6]
    calls = []
    monkeypatch.setattr(
        sanity,
        "validate_direct_selection_contract",
        lambda: (_ for _ in ()).throw(ValueError("direct selection failed")),
    )
    monkeypatch.setattr(
        sanity, "_run_command", lambda command: calls.append(command) or _result()
    )
    assert sanity._run_stage(step) == 1
    assert calls == []


def test_pr05_proof_preflight_stops_before_generator(monkeypatch):
    step = sanity.default_steps()[10]
    calls = []
    monkeypatch.setattr(
        sanity,
        "validate_pr05_path_proof_prerequisites",
        lambda: (_ for _ in ()).throw(ValueError("missing inherited proof")),
    )
    monkeypatch.setattr(
        sanity, "_run_command", lambda command: calls.append(command) or _result()
    )
    assert step.commands[0] == ("__validate_pr05_proofs__",)
    assert sanity._run_stage(step) == 1
    assert calls == []


def test_missing_ops03_is_reserved_nonfinal_only_at_stage14(
    tmp_path, monkeypatch
):
    step = sanity.default_steps()[13]
    monkeypatch.setattr(
        sanity,
        "validate_ops03_tracked_packet",
        lambda: (_ for _ in ()).throw(
            sanity.Ops03PacketUnavailable(sanity.PR_A_NONFINAL_REASON)
        ),
    )
    assert sanity._run_stage(step) == sanity.PR_A_NONFINAL_EXIT

    earlier = sanity.SanityStep("not-stage-14", (("__validate_ops03__",),))
    log = tmp_path / "earlier.log"
    assert sanity.run_pipeline(log_path=log, steps=[earlier]) == sanity.PR_A_NONFINAL_EXIT
    text = log.read_text(encoding="utf-8")
    assert "check not-stage-14:FAIL" in text
    assert "pr_a_state:nonfinal_fail_closed" not in text


def test_historical_bridge_evidence_validates_frozen_packet_without_execution(
    monkeypatch
):
    monkeypatch.setattr(
        subprocess, "run", lambda *args, **kwargs: pytest.fail("historical command ran")
    )
    sanity.validate_historical_bridge_evidence()


def test_historical_bridge_packet_is_bound_to_exact_frozen_ledger(tmp_path):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    value = json.loads((packet / "bridge_consistency.result.json").read_bytes())
    value["status"] = "FAIL"
    _write_json_and_refresh(packet, "bridge_consistency.result.json", value)
    with pytest.raises(ValueError, match="frozen historical checksum ledger drift"):
        sanity.validate_historical_bridge_evidence(root)


@pytest.mark.parametrize(
    "relative",
    (
        "artifacts/db_bridge/provider_parity.proof.json",
        "artifacts/runtime/env_connectivity.snapshot.json",
        "artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json",
        "schemas/presenter_db_bridge_compare.v1.json",
    ),
)
def test_historical_bridge_primaries_outside_ops01_are_hash_frozen(
    tmp_path, relative
):
    root = _packet_copy(tmp_path)
    path = root / relative
    path.write_bytes(path.read_bytes() + b" ")
    with pytest.raises(ValueError, match="historical bridge primary drift"):
        sanity.validate_historical_bridge_evidence(root)


def test_historical_bridge_primary_path_proof_is_required(tmp_path):
    root = _packet_copy(tmp_path)
    relative = "artifacts/db_bridge/provider_parity.proof.json"
    (root / f"{relative}.path_proof.txt").unlink()
    with pytest.raises(ValueError, match="historical bridge path proof is missing"):
        sanity.validate_historical_bridge_evidence(root)


def test_historical_bridge_directory_rejects_unpinned_extra_entry(tmp_path):
    root = _packet_copy(tmp_path)
    (root / "artifacts/db_bridge/current-looking.json").write_bytes(b"{}\n")

    with pytest.raises(ValueError, match="historical bridge directory inventory drift"):
        sanity.validate_historical_bridge_evidence(root)


def test_historical_integrity_does_not_rederive_bridge_success(
    tmp_path, monkeypatch
):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    value = json.loads((packet / "bridge_consistency.result.json").read_bytes())
    value["status"] = "FAIL"
    value["predicates"] = {
        key: False for key in value.get("predicates", {})
    }
    _write_json_and_refresh(packet, "bridge_consistency.result.json", value)
    _pin_changed_historical_ledger(
        monkeypatch, packet, "bridge_consistency.result.json"
    )

    # The retained packet is historical evidence. Once its newly frozen bytes
    # are integrity-pinned, this stage intentionally does not convert bridge
    # assertions into a current success requirement.
    sanity.validate_historical_bridge_evidence(root)


@pytest.mark.parametrize(
    ("mutation", "match"),
    (
        ("malformed", "malformed row"),
        ("duplicate", "duplicate row"),
        ("mismatch", "mismatch for stdout.log"),
    ),
)
def test_historical_checksum_ledger_fails_closed(tmp_path, mutation, match):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    ledger = packet / "checksums.sha256"
    if mutation == "malformed":
        ledger.write_text("not a checksum\n", encoding="ascii")
    elif mutation == "duplicate":
        first = ledger.read_text(encoding="ascii").splitlines()[0]
        ledger.write_text(
            ledger.read_text(encoding="ascii") + first + "\n", encoding="ascii"
        )
    else:
        (packet / "stdout.log").write_text("changed\n", encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        sanity.validate_historical_bridge_evidence(root)


@pytest.mark.parametrize("mutation", ("missing", "hash", "size"))
def test_historical_path_proofs_are_immutable_bindings(tmp_path, mutation):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    proof = packet / "stdout.log.path_proof.txt"
    if mutation == "missing":
        proof.unlink()
    elif mutation == "hash":
        proof.write_text(
            proof.read_text(encoding="utf-8").replace("sha256: ", "sha256: 0"),
            encoding="utf-8",
        )
    else:
        proof.write_text(
            proof.read_text(encoding="utf-8").replace("size_bytes: ", "size_bytes: 0"),
            encoding="utf-8",
        )
    with pytest.raises(ValueError, match="historical path proof"):
        sanity.validate_historical_bridge_evidence(root)


def test_historical_json_must_remain_canonical(tmp_path, monkeypatch):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "nonclaims.json"
    value = json.loads(path.read_bytes())
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    _refresh_ledger(packet, path.name)
    _pin_changed_historical_ledger(monkeypatch, packet, path.name)
    with pytest.raises(ValueError, match="historical JSON is not canonical"):
        sanity.validate_historical_bridge_evidence(root)


def test_historical_packet_keeps_required_nonclaims(tmp_path, monkeypatch):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "nonclaims.json"
    value = json.loads(path.read_bytes())
    value["nonclaims"].remove("no_qa_pass_claim")
    _write_json_and_refresh(packet, path.name, value)
    _pin_changed_historical_ledger(monkeypatch, packet, path.name)
    with pytest.raises(ValueError, match="historical nonclaims are incomplete"):
        sanity.validate_historical_bridge_evidence(root)


def test_historical_and_ops02_validators_are_independent(tmp_path):
    root = _packet_copy(tmp_path)
    (root / "audit/ops/hde-epic038/ops-01/stdout.log").unlink()
    sanity.validate_ops02_package(root)
    with pytest.raises(ValueError, match="ops-01.*stdout.log"):
        sanity.validate_historical_bridge_evidence(root)


def test_ops02_is_validated_without_executing_commands(monkeypatch):
    monkeypatch.setattr(
        subprocess, "run", lambda *args, **kwargs: pytest.fail("OPS-02 command ran")
    )
    sanity.validate_ops02_package()


@pytest.mark.parametrize(
    ("name", "contents", "match"),
    (
        ("debug.log", "benign diagnostic\n", "unexpected retained packet entry"),
        (
            "raw_response.json",
            "HD-Geocode-Key: live-secret\n",
            "unredacted vendor header",
        ),
    ),
)
def test_ops02_unledgered_files_are_never_accepted(tmp_path, name, contents, match):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    (packet / name).write_text(contents, encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        sanity.validate_ops02_package(root)


def test_ops02_command_surface_is_exactly_pinned(tmp_path):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    commands = packet / "commands.txt"
    commands.write_text(
        commands.read_text(encoding="utf-8") + "# checksum-consistent drift\n",
        encoding="utf-8",
    )
    _refresh_ledger(packet, commands.name)
    with pytest.raises(ValueError, match="approved command surface"):
        sanity.validate_ops02_package(root)


def test_ops02_summary_predicate_failure_is_rejected(tmp_path):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "result_summary.json"
    value = json.loads(path.read_bytes())
    value["predicates"]["adapter_mapped"] = False
    _write_json_and_refresh(packet, path.name, value)
    with pytest.raises(ValueError, match="PASS predicate failed"):
        sanity.validate_ops02_package(root)


def test_ops02_failed_lower_level_log_is_rejected(tmp_path):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "canonical_parity.log"
    path.write_text("FAIL pre_write_post_read_match=false\n", encoding="utf-8")
    _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="canonical_parity"):
        sanity.validate_ops02_package(root)


@pytest.mark.parametrize(
    "leak",
    (
        "HD_API_KEY=supersecret",
        "HD_API_KEY: live-secret",
        "GEO_API_KEY : live-secret",
        '"HD_API_KEY": live-secret',
        "'GEO_API_KEY': live-secret",
        "Authorization: Bearer live-secret",
        "HD-Geocode-Key: live-geocode-secret",
        "HD-Api-Key: live-legacy-secret",
        "HD_API_KEY=${HD_API_KEY:-live-secret}",
        "HD-Geocode-Key: ${GEO_API_KEY:=live-secret}",
        "HD_API_KEY=$(printf live-secret)",
        "postgresql://user:password@host/database",
        '{"raw_vendor_payload":{"private":"value"}}',
        '{"birthdate":"1990-01-01","birthtime":"12:34","location":"Private Address"}',
        "--birthdate 1990-01-01 --birthtime 12:34 --location 'Private Address'",
        "birth_date=1990-01-01",
        'dob: "1990-01-01"',
        "{'birthdate': '1990-01-01'}",
        "birthdate=${BIRTHDATE:-1990-01-01}",
    ),
)
def test_ops02_checksum_consistent_secret_or_raw_payload_is_rejected(
    tmp_path, leak
):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"
    path.write_text(leak + "\n", encoding="utf-8")
    _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="unredacted|raw request"):
        sanity.validate_ops02_package(root)


@pytest.mark.parametrize("safe_value", ("false", "null", '"redacted"', '"none"'))
def test_ops02_spaced_safe_raw_payload_values_are_allowed(tmp_path, safe_value):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"
    path.write_text(f'{{"raw_vendor_payload": {safe_value}}}\n', encoding="utf-8")
    _refresh_ledger(packet, path.name)
    sanity.validate_ops02_package(root)


@pytest.mark.parametrize("safe_value", ("REDACTED", "<redacted>", "SET:REDACTED"))
def test_ops02_colon_delimited_redacted_credentials_are_allowed(
    tmp_path, safe_value
):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"
    path.write_text(f"HD_API_KEY: {safe_value}\n", encoding="utf-8")
    _refresh_ledger(packet, path.name)
    sanity.validate_ops02_package(root)


@pytest.mark.parametrize(
    "safe_reference",
    (
        "HD_API_KEY=$HD_API_KEY",
        "HD_API_KEY=${HD_API_KEY}",
        "HD-Geocode-Key: $GEO_API_KEY",
        "'birthdate': '${BIRTHDATE}'",
    ),
)
def test_ops02_bare_environment_references_are_allowed(tmp_path, safe_reference):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"
    path.write_text(safe_reference + "\n", encoding="utf-8")
    _refresh_ledger(packet, path.name)
    sanity.validate_ops02_package(root)


@pytest.mark.parametrize("safe_value", ("REDACTED", "<redacted>", "null"))
def test_ops02_redacted_birth_inputs_are_allowed(tmp_path, safe_value):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "stderr.log"
    path.write_text(
        json.dumps(
            {"birthdate": safe_value, "birthtime": safe_value, "location": safe_value}
        )
        + "\n",
        encoding="utf-8",
    )
    _refresh_ledger(packet, path.name)
    sanity.validate_ops02_package(root)


@pytest.mark.parametrize(
    "mutation",
    ("missing", "predicate", "nonclaim", "proof-bytes", "proof-ledger"),
)
def test_ops02_production_refusal_requires_independent_pr05_evidence(
    tmp_path, mutation
):
    root = _packet_copy(tmp_path)
    path = root / "artifacts/bodygraph/v2_mapped_cache/manifest.json"
    if mutation == "missing":
        path.unlink()
    elif mutation == "proof-bytes":
        (
            root
            / "artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log"
        ).write_text(
            "PASS code=PROVIDER_REFUSED safe_mode=1 allow_network=1 "
            "vendor_calls=0 db_calls=0\n",
            encoding="utf-8",
        )
    else:
        value = json.loads(path.read_bytes())
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
        path.write_bytes(_canonical(value))
    with pytest.raises(ValueError, match="production-like refusal"):
        sanity.validate_ops02_package(root)


@pytest.mark.parametrize(
    ("path_name", "field", "value", "match"),
    (
        ("request_summary.json", "vendor_requests", 2, "request_summary"),
        (
            "mapped_output_summary.json",
            "raw_vendor_envelope_persisted",
            True,
            "mapped_output_summary",
        ),
        ("read_back_summary.json", "read_back_match", False, "read_back_summary"),
    ),
)
def test_ops02_summary_predicates_are_derived_from_primary_evidence(
    tmp_path, path_name, field, value, match
):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / path_name
    primary = json.loads(path.read_bytes())
    primary[field] = value
    _write_json_and_refresh(packet, path.name, primary)
    with pytest.raises(ValueError, match=match):
        sanity.validate_ops02_package(root)


@pytest.mark.parametrize("source", ("request", "read-back"))
def test_ops02_identity_agrees_across_request_and_read_back(tmp_path, source):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    if source == "request":
        path = packet / "request_summary.json"
        value = json.loads(path.read_bytes())
        value["input_fingerprint"] = "0" * 64
    else:
        path = packet / "read_back_summary.json"
        value = json.loads(path.read_bytes())
        value["synthetic_user_id"] = "00000000-0000-4000-8000-000000000000"
    _write_json_and_refresh(packet, path.name, value)
    with pytest.raises(ValueError, match="identity disagreement"):
        sanity.validate_ops02_package(root)


@pytest.mark.parametrize("mutation", ("non-durable", "provider-mismatch"))
def test_ops02_read_back_requires_agreed_durable_provider(tmp_path, mutation):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    read_back_path = packet / "read_back_summary.json"
    stdout_path = packet / "stdout.log"
    read_back = json.loads(read_back_path.read_bytes())
    stdout = json.loads(stdout_path.read_bytes())
    if mutation == "non-durable":
        read_back["provider"] = "memory"
        stdout["provider"] = "memory"
    else:
        stdout["provider"] = "memory"
    _write_json_and_refresh(packet, read_back_path.name, read_back)
    _write_json_and_refresh(packet, stdout_path.name, stdout)
    with pytest.raises(ValueError, match="read_back_summary|stdout"):
        sanity.validate_ops02_package(root)


@pytest.mark.parametrize(
    ("field", "value"),
    (
        ("route", "vendor.hdapi.post:/legacy"),
        ("resource_path", "legacy"),
        ("route_family", "legacy_bodygraph"),
        ("payload_family", "LegacyResponse"),
        ("geocode_required", False),
    ),
)
def test_ops02_requires_exact_configured_v2_route_metadata(
    tmp_path, field, value
):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "request_summary.json"
    request = json.loads(path.read_bytes())
    request[field] = value
    _write_json_and_refresh(packet, path.name, request)
    with pytest.raises(ValueError, match="request_summary"):
        sanity.validate_ops02_package(root)


def test_current_commands_and_exact_proof_paths_are_wired():
    commands = [command for step in sanity.default_steps() for command in step.commands]
    assert (sanity.sys.executable, "scripts/release_id_recompute.py", "--check") in commands
    assert (sanity.sys.executable, "ci/checks/check_release_identity.sh") in commands
    assert (
        sanity.sys.executable,
        "tools/evidence/generate_open_rails_abba_proof.py",
        "--check",
    ) in commands
    assert (
        sanity.sys.executable,
        "tools/evidence/generate_open_rails_abba_proof.py",
        "--live",
        "--check",
    ) in commands
    assert (sanity.ROOT / "artifacts/db/boundary_view.readonly.proof.txt").is_file()
    assert (
        sanity.ROOT / "artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt"
    ).is_file()


def test_wrapper_has_no_legacy_writer_or_epic024_identity():
    text = (sanity.ROOT / "tools/evidence/run_sanity_pipeline_gate.py").read_text(
        encoding="utf-8"
    )
    assert "D07_sanity_pipeline" not in text
    assert "hde-epic024" not in text
    assert "_write_path_proof" not in text
    from tools.evidence import update_evidence_index

    entries = update_evidence_index._load_human_index()
    sanity_paths = {
        entry["discovered_physical_path"]
        for entry in entries
        if entry["artifact_key"] == "sanity.pipeline.log"
    }
    assert sanity_paths == {"audit/gates/sanity_pipeline/sanity_pipeline.log"}
    updater = (sanity.ROOT / "tools/evidence/update_evidence_index.py").read_text(
        encoding="utf-8"
    )
    assert "LEGACY_SANITY_LOG" not in updater
    assert "_sync_legacy_sanity_compatibility" not in updater


def test_pr05_preflight_roster_matches_governed_index_and_current_proofs():
    from tools.evidence import update_evidence_index

    indexed_paths = tuple(
        str(entry["discovered_physical_path"])
        for entry in update_evidence_index.EPIC038_PR05_PRIMARY_ARTIFACTS
    )
    assert sanity.PR05_PRIMARY_PATHS == indexed_paths
    sanity.validate_pr05_path_proof_prerequisites()


def test_pr05_preflight_is_independent_of_clone_filesystem_mtime(
    tmp_path,
):
    root = tmp_path / "repo"
    for rel in sanity.PR05_PRIMARY_PATHS:
        primary = root / rel
        proof = root / f"{rel}.path_proof.txt"
        primary.parent.mkdir(parents=True, exist_ok=True)
        proof.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sanity.ROOT / rel, primary)
        shutil.copy2(sanity.ROOT / f"{rel}.path_proof.txt", proof)
        os.utime(primary, (1, 1))

    sanity.validate_pr05_path_proof_prerequisites(root)


@pytest.mark.parametrize(
    "mutation",
    ("missing", "stale", "invalid-mtime", "invalid-produced-at"),
)
def test_pr05_preflight_rejects_missing_or_stale_inherited_proof(
    tmp_path, mutation
):
    root = tmp_path / "repo"
    for rel in sanity.PR05_PRIMARY_PATHS:
        primary = root / rel
        proof = root / f"{rel}.path_proof.txt"
        primary.parent.mkdir(parents=True, exist_ok=True)
        proof.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sanity.ROOT / rel, primary)
        shutil.copy2(sanity.ROOT / f"{rel}.path_proof.txt", proof)
    target = root / f"{sanity.PR05_PRIMARY_PATHS[0]}.path_proof.txt"

    def replace_field(field, value):
        lines = target.read_text(encoding="utf-8").splitlines(keepends=True)
        target.write_text(
            "".join(
                f"{field}: {value}\n" if line.startswith(f"{field}: ") else line
                for line in lines
            ),
            encoding="utf-8",
        )

    if mutation == "missing":
        target.unlink()
    elif mutation == "stale":
        target.write_text(
            target.read_text(encoding="utf-8").replace("sha256: ", "sha256: 0"),
            encoding="utf-8",
        )
    elif mutation == "invalid-mtime":
        replace_field("mtime_utc", "invalid")
    else:
        replace_field("produced_at_utc", "invalid")
    with pytest.raises(ValueError, match="path proof"):
        sanity.validate_pr05_path_proof_prerequisites(root)


def test_targeted_failure_rebind_preserves_index_and_orientation_topology(
    tmp_path, monkeypatch
):
    from tools.evidence import update_evidence_index as updater

    root = tmp_path / "repo"
    copied = (
        "docs/evidence/INDEX.json",
        "docs/evidence/INDEX.sha256",
        "artifacts/evidence_index.jsonl",
        "artifacts/evidence_index.jsonl.sha256",
        "artifacts/evidence_index.jsonl.path_proof.txt",
        "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
        "audit/gates/sanity_pipeline/sanity_pipeline.log",
        "audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt",
        "audit/gates/topology/orientation_demo.txt",
    )
    for rel in copied:
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sanity.ROOT / rel, target)

    human_path = root / "docs/evidence/INDEX.json"
    sentinel_path = root / "docs/evidence/INDEX.sha256"
    mirror_path = root / "artifacts/evidence_index.jsonl"
    mirror_sha_path = root / "artifacts/evidence_index.jsonl.sha256"
    sanity_path = root / updater.SANITY_LOG_REL
    orientation_path = root / "audit/gates/topology/orientation_demo.txt"
    human_before = human_path.read_bytes()
    sentinel_before = sentinel_path.read_bytes()
    orientation_before = orientation_path.read_bytes()
    keys_before = [
        (row["artifact_key"], row["discovered_physical_path"])
        for row in map(json.loads, mirror_path.read_text(encoding="utf-8").splitlines())
    ]

    monkeypatch.setattr(updater, "ROOT", root)
    monkeypatch.setattr(updater, "HUMAN_INDEX", human_path)
    monkeypatch.setattr(updater, "HASH_SENTINEL", sentinel_path)
    monkeypatch.setattr(updater, "MIRROR_PATH", mirror_path)
    monkeypatch.setattr(updater, "MIRROR_SHA_PATH", mirror_sha_path)

    failure_bytes = b"run:sanity-pipeline\nfirst_failed_stage:14\nsummary:FAIL\n"
    sanity_path.write_bytes(failure_bytes)
    updater._rebind_sanity_log_only()

    assert human_path.read_bytes() == human_before
    assert sentinel_path.read_bytes() == sentinel_before
    assert orientation_path.read_bytes() == orientation_before
    records = list(
        map(json.loads, mirror_path.read_text(encoding="utf-8").splitlines())
    )
    keys_after = [
        (row["artifact_key"], row["discovered_physical_path"]) for row in records
    ]
    assert keys_after == keys_before
    assert any(str(key).startswith("epic038.pr06.") for key, _ in keys_after)
    sanity_row = next(
        row
        for row in records
        if (row["artifact_key"], row["discovered_physical_path"])
        == updater.SANITY_LOG_KEY
    )
    assert sanity_row["sha256"] == hashlib.sha256(failure_bytes).hexdigest()
    assert sanity_row["size_bytes"] == len(failure_bytes)
    sanity_proof = updater._load_existing_proof(
        root / f"{updater.SANITY_LOG_REL}.path_proof.txt"
    )
    assert sanity_proof["sha256"] == sanity_row["sha256"]
    mirror_digest = hashlib.sha256(mirror_path.read_bytes()).hexdigest()
    assert mirror_sha_path.read_text(encoding="utf-8") == (
        f"{mirror_digest}  {updater.MIRROR_REL}\n"
    )
    mirror_row = next(
        row for row in records if row["artifact_key"] == "index.machine_mirror"
    )
    mirror_proof = updater._load_existing_proof(
        root / f"{updater.MIRROR_REL}.path_proof.txt"
    )
    assert mirror_proof["sha256"] == mirror_digest
    assert mirror_proof["mirror_body_sha256"] == mirror_row["sha256"]


def _write_tracked_ops03_packet(root: Path) -> Path:
    from tools.evidence import hde_epic038_ops03 as ops03

    packet = root / sanity.OPS03_TRACKED_ROOT
    packet.mkdir(parents=True)
    run_id = "ops03-fixture-0000000000000001"
    source_commit = "0" * 40
    authorization_sha256 = "1" * 64
    query_results = [
        {
            "query_id": query_id,
            "status": "ok",
            "row_count": 0,
            "canonical_sha256": "2" * 64,
        }
        for query_id in ops03.ORDERED_QUERY_IDS
    ]
    posture = {
        "schema": "hde_epic038.ops03.db_posture_summary.v1",
        "run_id": run_id,
        "source_commit": source_commit,
        "provider": "psycopg",
        "selection_attempts": [
            {"provider": "psycopg", "status": "ok", "reason": None}
        ],
        "ordered_query_ids": list(ops03.ORDERED_QUERY_IDS),
        "query_results": query_results,
        "observations": {
            "connection_identity_presence": True,
            "search_path": ["hde", "public"],
            "runtime_role_flags": {
                "rolsuper": False,
                "rolcreatedb": False,
                "rolcreaterole": False,
                "rolreplication": False,
                "rolbypassrls": False,
                "schema_create": False,
                "relation_write": False,
            },
            "ddl_identity": {
                "schema": "hde.ddl_identity_projection.v1",
                "canonical_sha256": "3" * 64,
            },
            "constraint_count": 1,
            "boundary_views": [
                {"name": "hde.body_graphs_current", "read_only": True},
                {"name": "public.hde_body_graphs_current", "read_only": True},
            ],
            "partition_posture": {
                "expected_tables": ["hde.pair_evaluation", "hde.public_results"],
                "observed_tables": ["hde.pair_evaluation", "hde.public_results"],
                "all_expected_present": True,
            },
        },
        "counts": dict(ops03.EXPECTED_COUNTS),
        "predicates": {name: True for name in ops03.POSTURE_PREDICATES},
        "result": "PASS",
    }
    values = {
        "db_posture_summary.json": posture,
        "env_presence.json": {
            "schema": "hde_epic038.ops03.env_presence.v1",
            "run_id": run_id,
            "app_env": "dev",
            "rails": {
                "safe_mode": "1",
                "allow_network": "0",
                "allow_db_write": "0",
                "db_read_authorized": True,
            },
            "database_url_presence": "SET_REDACTED",
            "retired_key_presence": {
                "DB_BRIDGE_URL": "UNSET",
                "DB_FORCE_BRIDGE": "UNSET",
                "DB_ALLOW_BRIDGE_IN_PROD": "UNSET",
            },
            "determinism_pins": {
                "LC_ALL": "C",
                "LANG": "C",
                "TZ": "UTC",
                "SAFE_MODE": "1",
                "ALLOW_NETWORK": "0",
            },
        },
        "nonclaims.json": {
            "schema": "hde_epic038.ops03.nonclaims.v1",
            "run_id": run_id,
            "nonclaims": list(ops03.NONCLAIMS),
        },
        "result_summary.json": {
            "schema": "hde_epic038.ops03.result_summary.v1",
            "run_id": run_id,
            "source_commit": source_commit,
            "authorization_sha256": authorization_sha256,
            "capture_result": "PASS",
            "decisive_predicates": {
                name: True for name in ops03.POSTURE_PREDICATES
            },
            "primary_files": list(ops03.PRIMARY_FILES),
            "nonclaims_ref": "nonclaims.json",
        },
        ops03.RECEIPT_FILE: {
            "schema": "hde_epic038.ops03.validation_receipt.v1",
            "run_id": run_id,
            "authorization_sha256": authorization_sha256,
            "validated_files": list(ops03.PRIMARY_FILES),
            "predicates": {name: True for name in ops03.RECEIPT_PREDICATES},
            "result": "PASS",
        },
    }
    for name, value in values.items():
        (packet / name).write_bytes(ops03.canonical_bytes(value))

    interpreter = "/usr/bin/python3"
    runner_path = "/repo/scripts/ops/hde_epic038_ops03.py"
    validator_path = "/repo/tools/evidence/hde_epic038_ops03.py"
    authorization = f"/tmp/hde-epic038-ops03/{run_id}/authorization.json"
    candidate = f"/tmp/hde-epic038-ops03/{run_id}/candidate"
    commands = [
        [
            interpreter,
            "-I",
            "-B",
            runner_path,
            "--authorization",
            authorization,
        ],
        [
            interpreter,
            "-I",
            "-B",
            validator_path,
            "--emit-receipt",
            "--authorization",
            authorization,
            "--candidate",
            candidate,
        ],
        [
            interpreter,
            "-I",
            "-B",
            validator_path,
            "--validate",
            "--authorization",
            authorization,
            "--candidate",
            candidate,
        ],
    ]
    (packet / "commands.txt").write_bytes(
        b"".join(
            (
                f"{name}_argv="
                + json.dumps(command, sort_keys=True, separators=(",", ":"))
                + "\n"
            ).encode("utf-8")
            for name, command in zip(("capture", "receipt", "validate"), commands)
        )
    )
    (packet / "stdout.log").write_bytes(b"OPS03_CAPTURE_PASS\n")
    (packet / "stderr.log").write_bytes(b"")
    (packet / "exit_code.txt").write_bytes(b"0\n")
    rows = [
        f"{hashlib.sha256((packet / name).read_bytes()).hexdigest()}  {name}"
        for name in ops03.CHECKSUM_INPUTS
    ]
    (packet / ops03.CHECKSUM_FILE).write_text(
        "\n".join(rows) + "\n", encoding="ascii"
    )
    assert tuple(sorted(path.name for path in packet.iterdir())) == ops03.FINAL_FILES
    return packet


def _refresh_ops03_checksums(packet: Path) -> None:
    from tools.evidence import hde_epic038_ops03 as ops03

    (packet / ops03.CHECKSUM_FILE).write_text(
        "\n".join(
            f"{hashlib.sha256((packet / name).read_bytes()).hexdigest()}  {name}"
            for name in ops03.CHECKSUM_INPUTS
        )
        + "\n",
        encoding="ascii",
    )


def test_tracked_ops03_fixture_is_validated_without_execution(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    _write_tracked_ops03_packet(root)
    monkeypatch.setattr(
        subprocess, "run", lambda *args, **kwargs: pytest.fail("OPS-03 executed")
    )
    sanity.validate_ops03_tracked_packet(root)


def test_missing_tracked_ops03_is_the_exact_downstream_condition(tmp_path):
    with pytest.raises(ValueError, match="tracked packet root is missing"):
        sanity.validate_ops03_tracked_packet(tmp_path)


@pytest.mark.parametrize(
    ("mutation", "match"),
    (
        ("checksum", "checksum mismatch"),
        ("unexpected", "unexpected tracked entry"),
        ("schema", "schema validation failed"),
        ("commands", "authorized command shape disagreement"),
        ("command_prefix", "command row identity is invalid"),
        ("command_encoding", "command row is not canonical"),
        ("secret", "unredacted service URI"),
    ),
)
def test_tracked_ops03_packet_mutations_fail_closed(
    tmp_path, mutation, match
):
    from tools.evidence import hde_epic038_ops03 as ops03

    root = tmp_path / "repo"
    packet = _write_tracked_ops03_packet(root)
    if mutation == "checksum":
        ledger = packet / ops03.CHECKSUM_FILE
        text = ledger.read_text(encoding="ascii")
        ledger.write_text(("0" if text[0] != "0" else "1") + text[1:], encoding="ascii")
    elif mutation == "unexpected":
        (packet / "debug.log").write_text("debug\n", encoding="utf-8")
    elif mutation == "schema":
        path = packet / "result_summary.json"
        value = json.loads(path.read_bytes())
        value["primary_files"] = value["primary_files"][:-1]
        path.write_bytes(ops03.canonical_bytes(value))
        _refresh_ops03_checksums(packet)
    elif mutation == "commands":
        command_names = ("capture", "receipt", "validate")
        commands = []
        for name, line in zip(
            command_names,
            (packet / "commands.txt").read_text(encoding="utf-8").splitlines(),
        ):
            commands.append(json.loads(line.removeprefix(f"{name}_argv=")))
        commands[1][4] = "--wrong-mode"
        (packet / "commands.txt").write_bytes(
            b"".join(
                (
                    f"{name}_argv="
                    + json.dumps(command, sort_keys=True, separators=(",", ":"))
                    + "\n"
                ).encode("utf-8")
                for name, command in zip(command_names, commands)
            )
        )
        _refresh_ops03_checksums(packet)
    elif mutation == "command_prefix":
        path = packet / "commands.txt"
        path.write_bytes(path.read_bytes().replace(b"capture_argv=", b"runner_argv=", 1))
        _refresh_ops03_checksums(packet)
    elif mutation == "command_encoding":
        path = packet / "commands.txt"
        path.write_bytes(path.read_bytes().replace(b"capture_argv=[", b"capture_argv=[ ", 1))
        _refresh_ops03_checksums(packet)
    else:
        (packet / "stderr.log").write_text(
            "DATABASE_URL=postgres://user:password@db/internal\n", encoding="utf-8"
        )
        _refresh_ops03_checksums(packet)
    with pytest.raises(ValueError, match=match):
        sanity.validate_ops03_tracked_packet(root)


def _final_pass_log() -> bytes:
    return sanity._render_log([(name, "OK") for name in sanity.STAGE_NAMES], "NONE", "PASS")


def test_sanity_gate_accepts_only_exact_final_pass_log(tmp_path, monkeypatch):
    from tools.evidence import run_sanity_pipeline_gate as gate

    log = tmp_path / "sanity_pipeline.log"
    log.write_bytes(_final_pass_log())
    monkeypatch.setattr(gate, "LOG", log)
    assert gate.STAGE_NAMES == sanity.STAGE_NAMES
    assert gate._valid_log() is True
    for old, new in (
        ("summary:PASS", "summary:FAIL"),
        (sanity.STAGE_NAMES[13], sanity.STAGE_NAMES[12]),
        ("stage_result:12:HISTORICAL_INTEGRITY_OK", "stage_result:12:PASS"),
        ("historical_nonclaim=true", "historical_nonclaim=false"),
    ):
        log.write_bytes(_final_pass_log().replace(old.encode(), new.encode(), 1))
        assert gate._valid_log() is False
    for extra in (
        b"summary:PASS\n",
        b"stage_result:12:BRIDGE_PARITY_OK\n",
        b"unexpected:claim\n",
    ):
        log.write_bytes(_final_pass_log() + extra)
        assert gate._valid_log() is False


def test_sanity_gate_rejects_stale_valid_final_pass_log(tmp_path, monkeypatch):
    from tools.evidence import run_sanity_pipeline_gate as gate

    log = tmp_path / "sanity_pipeline.log"
    log.write_bytes(_final_pass_log())
    monkeypatch.setattr(gate, "LOG", log)
    monkeypatch.setattr(
        gate.subprocess,
        "run",
        lambda *args, **kwargs: _result(1),
    )
    assert gate._valid_log() is True
    assert gate.main() == 1


def test_sanity_gate_accepts_fresh_exact_final_pass_log(tmp_path, monkeypatch, capsys):
    from tools.evidence import run_sanity_pipeline_gate as gate

    log = tmp_path / "sanity_pipeline.log"
    log.write_text("stale receipt\n", encoding="utf-8")

    def run(*args, **kwargs):
        log.write_bytes(_final_pass_log())
        return subprocess.CompletedProcess(
            [],
            0,
            "",
            "",
        )

    monkeypatch.setattr(gate, "LOG", log)
    monkeypatch.setattr(gate.subprocess, "run", run)
    assert gate.main() == 0
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


@pytest.mark.parametrize(
    ("returncode", "valid_log", "expected"),
    (
        (0, True, 0),
        (0, False, 1),
        (1, True, 1),
        (2, True, 2),
    ),
)
def test_sanity_gate_only_tolerates_exact_fresh_final_pass_receipt(
    tmp_path, monkeypatch, returncode, valid_log, expected
):
    from tools.evidence import run_sanity_pipeline_gate as gate

    log = tmp_path / "sanity_pipeline.log"
    log.write_text("stale receipt\n", encoding="utf-8")

    def run(*args, **kwargs):
        log.write_text(f"fresh receipt {returncode}\n", encoding="utf-8")
        return subprocess.CompletedProcess(
            [],
            returncode,
            "",
            "",
        )

    monkeypatch.setattr(gate, "LOG", log)
    monkeypatch.setattr(gate.subprocess, "run", run)
    monkeypatch.setattr(gate, "_valid_log", lambda: valid_log)
    assert gate.main() == expected


def test_ci_builds_and_publishes_final_gate_in_external_attestation():
    workflow = (sanity.ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "run: python tools/evidence/run_sanity_pipeline.py" not in workflow
    assert "tools/evidence/regenerate_identity_closure.py" not in workflow
    assert "tools/evidence/build_release_attestation.py" in workflow
    assert '--output "$RUNNER_TEMP/hde-release-attestation"' in workflow
    assert '--verify "$RUNNER_TEMP/hde-release-attestation"' in workflow
    assert "actions/upload-artifact@v4" in workflow
